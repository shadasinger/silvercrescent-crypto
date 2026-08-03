# Confluence — paper crypto trading system

A rules-based, evidence-generating paper trading system for Binance spot pairs, run by Claude Code cloud routines. **Simulated ledger only** — no exchange orders, no API keys, no funds at risk. The full rulebook lives in [`CLAUDE.md`](CLAUDE.md); Claude Code reads it automatically on every run.

Inception: 2026-08-02 · Paper capital: $10,000 USDT · Entry gate: ≥7/10 parameters Bullish at 2 consecutive trading checkpoints.

## Layout

```
CLAUDE.md              rulebook + repo operations (the system's brain)
scripts/universe.py    CoinGecko × Binance universe builder (MID routine)
scripts/parameters.py  10-parameter refresh + mechanical rubric labels
state/                 all persistent state (portfolio, watchlist, signals,
                       ledger, journal, shadow book, lessons, checkpoint log)
data/universe.json     latest candidate universe (regenerated at MID)
```

Both scripts are Python 3 stdlib-only — no installs needed. Data sources (all free): Binance spot & futures, CoinGecko, DefiLlama, Coin Metrics community, alternative.me.

**Environment variables** (set in the cloud routine environment):

| Variable | Required | Purpose |
|---|---|---|
| `COINGECKO_API_KEY` | recommended | CoinGecko demo key. Unlocks MID data-card enrichment (category/sector tags + community sentiment votes for the top-60 candidates) and rate-limit headroom. Without it, `universe.py` still runs; enrichment is skipped. |
| `XAI_API_KEY` | recommended | xAI key (console.x.ai, starts `xai-`). Powers `scripts/sentiment.py` — X-only Grok Live Search for parameter 1, run for holdings + near-gate coins. Without it, p1 falls back to web search / Neutral. |
| `XAI_MODEL` | no | Grok model for sentiment (default `grok-3-mini`). |
| `CG_ENRICH_TOP` | no | How many top candidates to enrich (default 60; throttled to demo-tier 30 calls/min). |

**Domain allowlist** for the cloud environment: `data-api.binance.vision`, `fapi.binance.com` (may 451 — fallback engages), `api.hyperliquid.xyz`, `api.coingecko.com`, `stablecoins.llama.fi`, `community-api.coinmetrics.io`, `api.alternative.me`, `api.x.ai`.

Params 6–7 fall back to Hyperliquid perps when Binance futures is geo-blocked (451). OI deltas then come from the self-built `state/OI_HISTORY.json` and read Neutral until ~1/~7 days of snapshots accumulate — expected warm-up, not a bug.

## Cloud routine setup (Claude Code on the web)

Create three scheduled routines on this repo, each on the default branch with permission to commit and push:

| Routine | Schedule (local) | Prompt |
|---|---|---|
| AM checkpoint | daily ~08:00 | Run the AM trading checkpoint exactly per CLAUDE.md Section 5. Before scoring, run `python3 scripts/sentiment.py <tickers>` for all holdings plus any coin whose mechanical count is ≥5, then make your own contrarian p1 read from its output with logged reasoning (fall back to web search if the script fails). Commit all state changes. |
| MID sourcing | daily ~14:00 | Run the MID sourcing routine exactly per CLAUDE.md Section 6. No trading decisions. Commit all state changes. |
| PM checkpoint | daily ~20:00 | Run the PM trading checkpoint exactly per CLAUDE.md Section 5, including the daily pre-mortem. Before scoring, run `python3 scripts/sentiment.py <tickers>` for all holdings plus any coin whose mechanical count is ≥5, then make your own contrarian p1 read from its output with logged reasoning (fall back to web search if the script fails). Commit all state changes. |

Monthly: on the first AM run of each month, the AM routine also writes `state/REVIEW-YYYY-MM.md` (CLAUDE.md Section 13) — this is in the rulebook, no separate routine needed.

A run that doesn't end in a commit did not happen. Commit format: `checkpoint(AM|PM|MID): YYYY-MM-DD — <summary>`.

## Known gaps (logged at inception)

- **Sentiment (parameter 1)** is wired via `scripts/sentiment.py` (xAI Grok, X-only Live Search, citations stored) — but the script only *collects*; the contrarian Bullish/Neutral/Bearish judgment stays with the decision engine per hard rule 6. Without `XAI_API_KEY`, p1 falls back to web search, then Neutral (never fabricated).
- **News red-flag screening** runs on web search during MID Step 3 — CoinGecko's `/news` endpoint is Pro-only, so no news API is wired (CryptoPanic was considered and dropped in favor of the CoinGecko key, 2026-08-03).
- SHIB and PEPE have no Binance USDT perp → parameters 6–7 are structurally Neutral for them (ceiling 8/10).

## Status

See `state/CHECKPOINT_LOG.md` for every run, `state/SIGNALS.csv` for the auditable confluence history, and `state/TRADE_LEDGER.csv` for fills. Going live requires an explicit user instruction to switch modes — the rulebook forbids it otherwise.
