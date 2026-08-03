#!/usr/bin/env python3
"""Confluence — X/Twitter sentiment collector for parameter 1 (xAI Grok Live Search).

Usage: python3 scripts/sentiment.py TICKER [TICKER ...]   (e.g. ADA UNI SOL)
Env:   XAI_API_KEY (required, from console.x.ai — starts 'xai-')
       XAI_MODEL   (default grok-3-mini)

Design contract (hard rule 6): Grok DESCRIBES, Claude JUDGES. This script asks
Grok for observations only — interest trend, euphoria/capitulation markers,
narrative, red-flag claims — with X-only live search and citations. The
contrarian mapping to Bullish/Neutral/Bearish stays with the decision engine
at the checkpoint, with reasoning logged in SIGNALS.csv. Output is written to
state/PARAMETERS.json under coins[TICKER].sentiment so every p1 label is
auditable back to actual posts.

Cost note: Live Search bills per source retrieved — run this only for holdings
and coins at >=5 mechanical count, not the whole watchlist.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state"

API = "https://api.x.ai/v1/chat/completions"
KEY = os.environ.get("XAI_API_KEY", "")
MODEL = os.environ.get("XAI_MODEL", "grok-3-mini")
WINDOW_H = int(os.environ.get("SENTIMENT_WINDOW_H", "48"))

SYSTEM = (
    "You are a sentiment data collector for a trading research system. Report "
    "observations from X posts only. Never give a trade recommendation, price "
    "prediction, or bullish/bearish verdict — describe what you see. Reply with "
    "a single JSON object, no prose."
)

USER_TMPL = """Search X for posts about {name} (${ticker}) from the last {h} hours.
Return JSON with exactly these keys:
- interest_trend: "rising" | "flat" | "falling" — post volume/engagement vs what looks typical
- euphoria_markers: list of observed euphoria signs (price targets, rocket emojis, "everyone's in", influencer pile-on) or []
- capitulation_markers: list of observed despair/giving-up signs or []
- dominant_narrative: one sentence — what people are actually talking about
- narrative_change: one sentence — how this differs from the prevailing story, or "none apparent"
- red_flag_claims: list of hack/exploit/regulatory/team-departure claims seen (mark each verified/unverified) or []
- representative_posts: 2-4 short paraphrases of typical posts"""


def collect(ticker, name):
    body = {
        "model": MODEL,
        "temperature": 0,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": USER_TMPL.format(
                name=name, ticker=ticker, h=WINDOW_H)},
        ],
        "search_parameters": {
            "mode": "on",
            "sources": [{"type": "x", "post_favorite_count": 30}],
            "from_date": (datetime.now(timezone.utc)
                          - timedelta(hours=WINDOW_H)).strftime("%Y-%m-%d"),
            "max_search_results": 25,
            "return_citations": True,
        },
    }
    req = urllib.request.Request(
        API, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {KEY}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        resp = json.load(r)
    msg = resp["choices"][0]["message"]
    text = msg["content"].strip()
    if text.startswith("```"):
        text = text.strip("`").lstrip("json").strip()
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {"raw": text, "parse_error": True}
    return {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "model": MODEL,
        "window_h": WINDOW_H,
        "data": data,
        "citations": resp.get("citations") or msg.get("citations") or [],
        "note": "descriptive only — contrarian Bullish/Neutral/Bearish read is "
                "made by the decision engine and logged in SIGNALS.csv",
    }


def main():
    if not KEY:
        sys.exit("XAI_API_KEY not set (get one at console.x.ai — starts 'xai-')")
    tickers = [t.upper() for t in sys.argv[1:]]
    if not tickers:
        sys.exit("usage: sentiment.py TICKER [TICKER ...]")
    wl = json.loads((STATE / "WATCHLIST.json").read_text())
    names = {c["ticker"]: c.get("name") or c["ticker"] for c in wl["coins"]}
    ppath = STATE / "PARAMETERS.json"
    params = json.loads(ppath.read_text())
    done, failed = [], []
    for t in tickers:
        if t not in params["coins"]:
            failed.append((t, "not in PARAMETERS.json"))
            continue
        try:
            params["coins"][t]["sentiment"] = collect(t, names.get(t, t))
            done.append(t)
        except Exception as e:
            failed.append((t, str(e)[:120]))
    ppath.write_text(json.dumps(params, indent=2))
    print(f"sentiment: wrote {len(done)} coin(s) {done} to state/PARAMETERS.json")
    for t, err in failed:
        print(f"  FAILED {t}: {err}")
    if failed and not done:
        sys.exit(1)


if __name__ == "__main__":
    main()
