#!/usr/bin/env python3
"""Confluence — parameter refresh (checkpoint Step 2).

For every coin in state/WATCHLIST.json, computes raw values for parameters 2-7
(price/DMA, RSI-14, realized vol ratio, volume z-score, funding, OI deltas) and
the global block for parameters 8-10 (stablecoin supply, MVRV, Fear & Greed).
Also emits MECHANICAL SUGGESTED LABELS per the Section 7 rubric — the decision
engine (Claude) must review these, may override with logged reasoning, and owns
parameter 1 (sentiment) entirely. Writes state/PARAMETERS.json.
"""
import json
import math
import statistics
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"

SPOT = "https://data-api.binance.vision"   # mirror of api.binance.com, market data only
FUT = "https://fapi.binance.com"


def get(url, retries=3, quiet=False):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "confluence/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception:
            if i == retries - 1:
                if quiet:
                    return None
                raise
            time.sleep(3 * (i + 1))


def rsi14(closes):
    if len(closes) < 15:
        return None
    gains, losses = [], []
    for i in range(1, len(closes)):
        d = closes[i] - closes[i - 1]
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    ag = sum(gains[:14]) / 14
    al = sum(losses[:14]) / 14
    for i in range(14, len(gains)):
        ag = (ag * 13 + gains[i]) / 14
        al = (al * 13 + losses[i]) / 14
    if al == 0:
        return 100.0
    return round(100 - 100 / (1 + ag / al), 1)


def realized_vol(closes, days):
    rets = [math.log(closes[i] / closes[i - 1]) for i in range(len(closes) - days, len(closes))]
    return statistics.pstdev(rets) * math.sqrt(365)


def coin_params(bsym):
    """Parameters 2-5 from daily klines, 6-7 from futures."""
    kl = get(f"{SPOT}/api/v3/klines?symbol={bsym}&interval=1d&limit=210", quiet=True)
    if not kl or len(kl) < 60:
        return None
    closes = [float(k[4]) for k in kl]
    vols = [float(k[7]) for k in kl]  # quote asset volume
    price = closes[-1]
    dma50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else None
    dma200 = sum(closes[-200:]) / 200 if len(closes) >= 200 else None
    dev50 = round((price / dma50 - 1) * 100, 1) if dma50 else None
    rv7 = realized_vol(closes, 7)
    rv30 = realized_vol(closes, 30)
    vol_hist = vols[-31:-1]
    mu, sd = statistics.mean(vol_hist), statistics.pstdev(vol_hist)
    vz = round((vols[-1] - mu) / sd, 2) if sd else 0.0
    chg24 = round((closes[-1] / closes[-2] - 1) * 100, 2)
    chg7d = round((closes[-1] / closes[-8] - 1) * 100, 2) if len(closes) >= 8 else None

    # funding (param 6) and open interest (param 7) — may not exist for all coins
    funding = None
    fr = get(f"{FUT}/fapi/v1/fundingRate?symbol={bsym}&limit=6", quiet=True)
    if isinstance(fr, list) and fr:
        funding = round(statistics.mean(float(x["fundingRate"]) for x in fr) * 100, 4)  # %/8h

    oi_24h = oi_7d = None
    oh = get(f"{FUT}/futures/data/openInterestHist?symbol={bsym}&period=1d&limit=8", quiet=True)
    if isinstance(oh, list) and len(oh) >= 2:
        vals = [float(x["sumOpenInterestValue"]) for x in oh]
        oi_24h = round((vals[-1] / vals[-2] - 1) * 100, 1)
        if len(vals) >= 8:
            oi_7d = round((vals[-1] / vals[0] - 1) * 100, 1)

    return {
        "price": price, "chg_24h_pct": chg24, "chg_7d_pct": chg7d,
        "dma50": round(dma50, 6) if dma50 else None,
        "dma200": round(dma200, 6) if dma200 else None,
        "dev_from_50dma_pct": dev50,
        "rsi14": rsi14(closes),
        "rv_ratio_7d_30d": round(rv7 / rv30, 2) if rv30 else None,
        "volume_z": vz,
        "funding_pct_8h": funding,
        "oi_delta_24h_pct": oi_24h, "oi_delta_7d_pct": oi_7d,
    }


def suggest_labels(p, g):
    """Mechanical rubric labels for params 2-10. Param 1 (sentiment) = None (Claude's)."""
    L = {}
    price, d50, d200, dev = p["price"], p["dma50"], p["dma200"], p["dev_from_50dma_pct"]
    up = d50 is not None and price > d50
    golden = up and d200 is not None and d50 > d200
    if dev is not None and dev > 25:
        L["p2_dma"] = "Bearish"  # overextended
    elif golden and (dev is None or dev <= 25):
        L["p2_dma"] = "Bullish"
    elif d50 and d200 and price < d50 and price < d200:
        L["p2_dma"] = "Bearish"
    else:
        L["p2_dma"] = "Neutral"

    r = p["rsi14"]
    downtrend = d50 is not None and price < d50
    if r is None:
        L["p3_rsi"] = "Neutral"
    elif 55 <= r <= 70:
        L["p3_rsi"] = "Bullish"
    elif r > 75 or (r < 45 and downtrend):
        L["p3_rsi"] = "Bearish"   # r<30 w/ intact thesis may be flipped by Claude w/ justification
    else:
        L["p3_rsi"] = "Neutral"

    rv = p["rv_ratio_7d_30d"]
    down_week = (p["chg_7d_pct"] or 0) < 0
    if rv is None:
        L["p4_rvol"] = "Neutral"
    elif rv < 0.8:
        L["p4_rvol"] = "Bullish"
    elif rv > 1.3 and down_week:
        L["p4_rvol"] = "Bearish"
    elif rv > 1.3 and not down_week:
        L["p4_rvol"] = "Bullish"  # expansion on upside
    else:
        L["p4_rvol"] = "Neutral"

    z, up_day = p["volume_z"], (p["chg_24h_pct"] or 0) > 0
    if z is None:
        L["p5_volz"] = "Neutral"
    elif z > 1 and up_day:
        L["p5_volz"] = "Bullish"
    elif (z > 1 and not up_day) or (z < -1 and (p["chg_7d_pct"] or 0) > 5):
        L["p5_volz"] = "Bearish"
    else:
        L["p5_volz"] = "Neutral"

    f = p["funding_pct_8h"]
    if f is None:
        L["p6_funding"] = "Neutral"
    elif f > 0.05:
        L["p6_funding"] = "Bearish"
    elif f < -0.01:
        L["p6_funding"] = "Bullish"  # crowded shorts, contrarian
    elif -0.01 <= f <= 0.02:
        L["p6_funding"] = "Bullish"  # near zero-to-slightly-positive
    else:
        L["p6_funding"] = "Neutral"

    oi = p["oi_delta_7d_pct"] if p["oi_delta_7d_pct"] is not None else p["oi_delta_24h_pct"]
    week_up = (p["chg_7d_pct"] or 0) > 0
    if oi is None:
        L["p7_oi"] = "Neutral"
    elif oi > 2 and week_up:
        L["p7_oi"] = "Bullish"
    elif (oi > 2 and not week_up) or (oi < -15 and week_up):
        L["p7_oi"] = "Bearish"
    else:
        L["p7_oi"] = "Neutral"

    # global 8-10 (same for all coins)
    s = g["stablecoin_supply_7d_pct"]
    L["p8_stables"] = "Bullish" if (s is not None and s > 0.1) else ("Bearish" if (s is not None and s < -0.1) else "Neutral")
    m = g["mvrv_btc"]
    L["p9_mvrv"] = "Neutral" if m is None else ("Bullish" if m < 2.0 else ("Bearish" if m > 3.0 else "Neutral"))
    fg, fgd = g["fear_greed"], g["fear_greed_7d_delta"]
    if fg is None:
        L["p10_fg"] = "Neutral"
    elif fg < 25 or (fg < 45 and (fgd or 0) > 5 and fg - (fgd or 0) < 30):
        L["p10_fg"] = "Bullish"
    elif fg > 75 or (fg < 60 and (fgd or 0) < -15):
        L["p10_fg"] = "Bearish"
    else:
        L["p10_fg"] = "Neutral"
    return L


def global_params():
    g = {"stablecoin_supply_7d_pct": None, "mvrv_btc": None, "mvrv_eth": None,
         "fear_greed": None, "fear_greed_7d_delta": None}
    try:
        d = get("https://stablecoins.llama.fi/stablecoins?includePrices=false")
        cur = prev = 0.0
        for a in d["peggedAssets"]:
            c = a.get("circulating", {}).get("peggedUSD") or 0
            p = a.get("circulatingPrevWeek", {}).get("peggedUSD") or 0
            cur += c
            prev += p
        if prev:
            g["stablecoin_supply_7d_pct"] = round((cur / prev - 1) * 100, 2)
            g["stablecoin_supply_usd"] = round(cur / 1e9, 1)  # $B
    except Exception:
        pass
    for asset in ("btc", "eth"):
        # community API sorts asset-major; query separately, paging from end
        d = get("https://community-api.coinmetrics.io/v4/timeseries/asset-metrics"
                f"?assets={asset}&metrics=CapMVRVCur&paging_from=end&page_size=1",
                quiet=True)
        try:
            g["mvrv_" + asset] = round(float(d["data"][-1]["CapMVRVCur"]), 2)
        except Exception:
            pass
    d = get("https://api.alternative.me/fng/?limit=8", quiet=True)
    try:
        vals = [int(x["value"]) for x in d["data"]]
        g["fear_greed"] = vals[0]
        g["fear_greed_7d_delta"] = vals[0] - vals[7] if len(vals) >= 8 else None
    except Exception:
        pass
    return g


def main():
    from concurrent.futures import ThreadPoolExecutor
    wl = json.loads((STATE / "WATCHLIST.json").read_text())
    g = global_params()
    tickers = [(c["ticker"], c.get("binance_symbol") or (c["ticker"] + "USDT"))
               for c in wl["coins"]]
    coins = {}
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = ex.map(lambda t: (t[0], coin_params(t[1])), tickers)
    for tick, p in results:
        if p is None:
            coins[tick] = {"error": "no kline data"}
            continue
        p["suggested_labels"] = suggest_labels(p, g)
        coins[tick] = p
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "global": g,
        "coins": coins,
        "note": ("suggested_labels are mechanical rubric outputs for params 2-10. "
                 "Claude reviews/overrides with logged reasoning and assigns param 1 "
                 "(sentiment) itself. Param 1 is never auto-labeled."),
    }
    (STATE / "PARAMETERS.json").write_text(json.dumps(out, indent=2))
    print(f"parameters: {len(coins)} coins + global block written to state/PARAMETERS.json")
    print("global:", json.dumps(g))


if __name__ == "__main__":
    main()
