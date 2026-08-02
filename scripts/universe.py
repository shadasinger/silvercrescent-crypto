#!/usr/bin/env python3
"""Confluence — universe builder (MID sourcing, Step 1-2).

Pulls CoinGecko markets, filters to mcap > $100M AND Binance spot USDT pairs,
excludes stablecoins/wrapped tokens, and writes data cards to data/universe.json.
No LLM judgment here — scoring happens in the MID routine (CLAUDE.md Section 6).
"""
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

MIN_MCAP = 100_000_000

# Symbols/name fragments that mark stablecoins, wrapped/staked wrappers, etc.
EXCLUDE_SYMBOLS = {
    "usdt", "usdc", "dai", "fdusd", "tusd", "usdd", "usde", "pyusd", "usds",
    "usdp", "gusd", "frax", "lusd", "susd", "usd1", "usd0", "eurc", "eurt",
    "xaut", "paxg", "bfusd", "rlusd",  # gold-pegged & yield-stable tokens
    "wbtc", "weth", "wbnb", "wsteth", "steth", "reth", "cbeth", "cbbtc",
    "meth", "rseth", "ezeth", "weeth", "eeth", "solvbtc", "lbtc", "tbtc",
    "jitosol", "msol", "bnsol", "wbeth", "jupsol",
}
EXCLUDE_PATTERNS = re.compile(
    r"(wrapped|staked|restaked|bridged|\busd\b|stable|liquid staking)", re.I
)


def get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "confluence/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            if i == retries - 1:
                raise
            time.sleep(5 * (i + 1))


def binance_usdt_bases():
    info = get("https://api.binance.com/api/v3/exchangeInfo")
    return {
        s["baseAsset"].upper()
        for s in info["symbols"]
        if s["quoteAsset"] == "USDT" and s["status"] == "TRADING"
        and s.get("isSpotTradingAllowed", True)
    }


def coingecko_markets(pages=4):
    out = []
    for p in range(1, pages + 1):
        url = (
            "https://api.coingecko.com/api/v3/coins/markets"
            "?vs_currency=usd&order=market_cap_desc&per_page=250"
            f"&page={p}&price_change_percentage=7d%2C30d%2C200d"
        )
        out += get(url)
        time.sleep(3)  # free-tier rate limit
    return out


def main():
    bases = binance_usdt_bases()
    markets = coingecko_markets()
    cards, excluded = [], []
    seen = set()
    for c in markets:
        sym = (c.get("symbol") or "").lower()
        name = c.get("name") or ""
        mcap = c.get("market_cap") or 0
        if mcap < MIN_MCAP:
            continue
        if sym.upper() not in bases:
            continue
        if sym in seen:
            continue
        if sym in EXCLUDE_SYMBOLS or EXCLUDE_PATTERNS.search(name):
            excluded.append({"symbol": sym.upper(), "name": name, "reason": "stable/wrapped"})
            continue
        seen.add(sym)
        vol = c.get("total_volume") or 0
        cards.append({
            "symbol": sym.upper(),
            "binance_symbol": sym.upper() + "USDT",
            "name": name,
            "coingecko_id": c.get("id"),
            "market_cap": mcap,
            "mcap_rank": c.get("market_cap_rank"),
            "volume_24h": vol,
            "vol_mcap_ratio": round(vol / mcap, 4) if mcap else None,
            "chg_7d": c.get("price_change_percentage_7d_in_currency"),
            "chg_30d": c.get("price_change_percentage_30d_in_currency"),
            "chg_200d": c.get("price_change_percentage_200d_in_currency"),
            "price": c.get("current_price"),
        })
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "candidate_count": len(cards),
        "candidates": cards,
        "excluded_stable_wrapped": excluded,
    }
    (DATA / "universe.json").write_text(json.dumps(out, indent=2))
    print(f"universe: {len(cards)} candidates written to data/universe.json "
          f"({len(excluded)} stable/wrapped excluded)")


if __name__ == "__main__":
    main()
