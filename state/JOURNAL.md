# JOURNAL — entry snapshots & exit post-mortems

## ENTRY — TRX — 2026-08-12 AM (first confirmed entry of paper phase)

**Confluence history:** armed PM 2026-08-11 (8/10), confirmed AM 2026-08-12 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (AM 2026-08-12, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest, zero euphoria/capitulation markers | Neutral | Genuine break from the rocket-emoji/stacked-price-target euphoria pattern flagged the prior 4 checkpoints (also read Neutral at PM); dominant chatter is burns/DeFi-incentive/giveaway content, not crowd extremity. |
| 2 | Price vs 50/200DMA | $0.3361 vs 50DMA $0.3269, 200DMA $0.31839; +2.8% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA, moderate (non-overextended) deviation. |
| 3 | RSI-14 | 66.3 | Bullish | Healthy 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.64 | Bullish | Compression, well under 0.8. |
| 5 | Volume z-score | -2.02 | Neutral | Negative on an up move — doesn't meet either Bullish (z>+1 up day) or Bearish (z>+1 down day / z<-1 in a rally) threshold cleanly enough to force a label either way per mechanical rubric; forced to Neutral by the script's banding. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +12.7%/24h, +13.1%/7d | Bullish | OI rising with price rising — conviction behind the move. |
| 8 | Stablecoin supply 7d Δ | +0.25% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.21 / ETH 0.92 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 27, Δ7d 0 | Neutral | Fear zone but flat, not sharply rising from <30 — mechanical Neutral. |

**Confluence: 7/10 Bullish, 0/10 Bearish.**

**Expectancy sheet:**
- Entry: $0.3361 (Binance spot, fetched 2026-08-12T07:17:14Z via `parameters.py`)
- Target: $0.375 (+11.57%) — measured-move estimate off the deflationary-burn/OI-expansion narrative within the 2-8wk horizon
- Invalidation: $0.318 (-5.39%) — just under the 200DMA; a close below breaks the "price>50DMA>200DMA" golden-cross structure this thesis rests on
- R = 11.57 / 5.39 = **2.15** (clears the 2.0 floor)
- Stated p = **0.42** (first trade of paper phase, confluence 7/10 not 8/10 — conservative estimate, no calibration history yet)
- EV = 0.42×11.57% − 0.58×5.39% = **+1.74%** (clears EV>0 floor)
- Tier: **C** (R>=2, p>=0.40; confluence 7/10 falls short of Tier A's 8/10 requirement even though R would otherwise qualify) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($500 notional, 1487.65 TRX)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-12); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint (did not confirm):**
- **BNB** — armed PM 2026-08-11 at 7/10; mechanical count collapsed to 4/9 this AM (rvol, volume-z, OI all rolled from Bullish to Neutral/negative) — max possible even with a Bullish sentiment read was 5/10. Arm broken, not a confirmation.
- **LINK** — armed PM 2026-08-11 at 7/10; mechanical count fell to 5/9 (rvol, volume-z rolled over) — total 5/10 with Neutral sentiment. Arm broken.
- **CAKE** — never armed; mechanical 6/9, but sentiment read Bearish (contrarian fade on stacked euphoria markers — rocket-emoji $10 target, "entered top 100" hype) capped it at 6/10.

**Sector:** Major L1 (TRX permanent slot). First position — no sector-cap or concurrent-position constraints triggered (1 of 5 max positions, 1 of 2 max in sector).
