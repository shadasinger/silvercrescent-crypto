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

## STAGE-2 ADD — TRX — 2026-08-12 PM

Confluence held **7/10 Bullish, 0/10 Bearish** at this checkpoint (second consecutive checkpoint since the AM 08-12 half-open) — per Section 5 step 9, the second half opens at full target size, no confirmation needed beyond the hold itself.

Mechanical parameters unchanged in shape from AM (DMA golden-state, RSI 65.9 healthy band, rvol compressed, funding near-zero, OI still expanding, stables/MVRV healthy); p1 sentiment read Neutral for a third consecutive checkpoint (flat interest, zero euphoria/capitulation markers, DeFi-yield/GasFree chatter — genuine break from the earlier-week euphoria pattern, not a contrarian fade).

**Fill:** BUY 1488.98 TRX @ $0.3358 = $500.00 notional, 2026-08-12T19:06:31Z (Binance spot via `parameters.py` refresh). Position now 2976.6315 TRX, avg entry $0.33595, 10.0% of portfolio ($999.55 / $9999.55) — full target size reached. No further staging; ongoing test is the same OI/price/funding/DMA structure through the 2026-08-26 interim review.

## ENTRY — CAKE — 2026-08-18 PM

**Confluence history:** armed AM 2026-08-18 (8/10), confirmed PM 2026-08-18 (8/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (PM 2026-08-18, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest; euphoria cluster (rockets, "$50 target/55x", tokenization hype) | Bearish | One-sided euphoria, zero capitulation offset — fits the "everyone's in" bar despite the clean mechanical picture. |
| 2 | Price vs 50/200DMA | $1.504 vs 50DMA $1.41348, 200DMA $1.41011; +6.4% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA in a tight cluster. |
| 3 | RSI-14 | 67.0 | Bullish | Upper-mid 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.75 | Bullish | Compression, under 0.8. |
| 5 | Volume z-score | 0.11 | Neutral | Doesn't clear either threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +10.6%/24h, +11.6%/7d | Bullish | OI rising with price rising. |
| 8 | Stablecoin supply 7d Δ | +0.42% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.22 / ETH 0.93 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 41, Δ7d +12 | Bullish | Rising from Fear toward Neutral. |

**Confluence: 8/10 Bullish, 1/10 Bearish.**

**Expectancy sheet:**
- Entry: $1.504 (Binance spot, fetched 2026-08-18T19:05:57Z via `parameters.py`)
- Target: $1.75 (+16.36%) — momentum/burn-narrative continuation within the 2-8wk horizon
- Invalidation: $1.39 (-7.58%) — below the tight 50/200DMA cluster, breaking the golden-cross structure
- R = 16.36 / 7.58 = **2.16** (clears the 2.0 floor)
- Stated p = **0.48** (confluence 8/10, tempered by the contrarian-Bearish sentiment flag)
- EV = 0.48×16.36% − 0.52×7.58% = **+3.91%** (clears EV>0 floor)
- Tier: **C** (R=2.16 falls short of Tier B's 2.5 floor despite confluence 8/10 — R/p bands gate tier, not confluence alone) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($499.46 notional, 332.0878 CAKE)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (AM 2026-08-19); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** none competing for this slot — 4 confirmed candidates (CAKE, ETH, ZEC, MORPHO) filled exactly the 4 open position slots (1 of 5 held by TRX), so no anti-churn or highest-confluence tiebreak was triggered. SOL armed for the first time this checkpoint (7/10, 1/10 Bearish) but is a first occurrence, not a confirmed candidate — carried forward for AM 2026-08-19.

**Sector:** DEX. 1 of 5 positions, 1 of 2 max in sector.

## ENTRY — ETH — 2026-08-18 PM

**Confluence history:** armed AM 2026-08-18 (7/10), confirmed PM 2026-08-18 (8/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (PM 2026-08-18, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest; capitulation-tilted 3:1 ("life support", "exhaustion", "who's still max longing") vs one isolated rocket-target TA post | Bullish | Net one-sided despair, though thinner margin than a clean zero-offset read — logged as a lower-conviction sentiment call. |
| 2 | Price vs 50/200DMA | $1916.02 vs 50DMA $1850.76 (above), 200DMA $2005.38 (still overhead) | Neutral | Not a golden cross — price above 50DMA but below 200DMA. Weakest structural leg of this entry. |
| 3 | RSI-14 | 57.1 | Bullish | Mid 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.47 | Bullish | Well under 0.8, compression. |
| 5 | Volume z-score | -0.72 | Neutral | Doesn't clear either threshold. |
| 6 | Funding rate | 0.0079%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +1.0%/24h, +13.4%/7d | Bullish | OI rising with price rising. |
| 8 | Stablecoin supply 7d Δ | +0.42% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (ETH) | 0.93 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 41, Δ7d +12 | Bullish | Rising from Fear toward Neutral. |

**Confluence: 8/10 Bullish, 0/10 Bearish.**

**Expectancy sheet:**
- Entry: $1916.02 (Binance spot, fetched 2026-08-18T19:05:57Z via `parameters.py`)
- Target: $2100 (+9.60%) — a reclaim of the 200DMA overhead resistance zone within the 2-8wk horizon
- Invalidation: $1830 (-4.49%) — below the 50DMA, eliminating even the partial structural support
- R = 9.60 / 4.49 = **2.14** (clears the 2.0 floor, but the thinnest margin of this wave)
- Stated p = **0.42** (confluence strong but the weakest structural setup of the four — matched to TRX's original conservative first-trade calibration)
- EV = 0.42×9.60% − 0.58×4.49% = **+1.43%** (clears EV>0 floor, but the thinnest of this wave)
- Tier: **C** (R=2.14 well short of Tier B's 2.5 floor) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($499.46 notional, 0.2607 ETH)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (AM 2026-08-19); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** none competing for this slot — see CAKE entry above for the shared context (4 confirmed candidates filled exactly 4 open slots).

**Sector:** Major L1 — now 2 of 5 positions in this sector (TRX + ETH), at the sector cap boundary (Section 3 rule 8, max 2 of 5 positions per sector) but not exceeding it.

## ENTRY — ZEC — 2026-08-18 PM

**Confluence history:** armed AM 2026-08-18 (7/10), confirmed PM 2026-08-18 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (PM 2026-08-18, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest, no euphoria/capitulation — mining-expansion/listing/privacy-tooling narrative, factual | Neutral | No crowd extreme. |
| 2 | Price vs 50/200DMA | $509.37 vs 50DMA $494.49, 200DMA $395.42; +3.0% above 50DMA | Bullish | Golden state, wide cushion to 200DMA. |
| 3 | RSI-14 | 54.8 | Neutral | Just under the 55 floor of the Bullish band. |
| 4 | Realized vol ratio 7d/30d | 0.78 | Bullish | Under 0.8, compression. |
| 5 | Volume z-score | -0.58 | Neutral | Doesn't clear either threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +6.0%/24h, +9.5%/7d | Bullish | OI rising with price rising. |
| 8 | Stablecoin supply 7d Δ | +0.42% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.22 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 41, Δ7d +12 | Bullish | Rising from Fear toward Neutral. |

**Confluence: 7/10 Bullish, 0/10 Bearish.**

**Expectancy sheet:**
- Entry: $509.37 (Binance spot, fetched 2026-08-18T19:05:57Z via `parameters.py`)
- Target: $590 (+15.83%) — momentum continuation with real room before RSI overbought, within the 2-8wk horizon
- Invalidation: $482 (-5.37%) — below the 50DMA
- R = 15.83 / 5.37 = **2.95** (clears the 2.0 floor and the 2.5 Tier B floor)
- Stated p = **0.45** (confluence 7/10, cleanest structure of this wave — wide 200DMA cushion, no Bearish flags)
- EV = 0.45×15.83% − 0.55×5.37% = **+4.17%** (clears EV>0 floor, strongest of this wave)
- Tier: **B** (R=2.95 >= 2.5, p=0.45 >= 0.45) → size band 15-25%
- Sizing: target 20% (mid-Tier-B), staged half-open this checkpoint = **10% ($998.93 notional, 1.9611 ZEC)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (AM 2026-08-19); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** none competing for this slot — see CAKE entry above for the shared context (4 confirmed candidates filled exactly 4 open slots).

**Sector:** Privacy (permanent slot). 1 of 5 positions, 1 of 2 max in sector.

## ENTRY — MORPHO — 2026-08-18 PM

**Confluence history:** armed AM 2026-08-18 (7/10), confirmed PM 2026-08-18 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6. (Note: MORPHO armed once before, 2026-08-16 PM at 7/10, and lapsed the next checkpoint without confirming — this is a fresh arm/confirm sequence starting 2026-08-18 AM.)

**Frozen 10-parameter table (PM 2026-08-18, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest, no euphoria/capitulation — TVL/institutional-ties narrative, factual | Neutral | No crowd extreme. |
| 2 | Price vs 50/200DMA | $2.131 vs 50DMA $1.9925, 200DMA $1.82542; +7.0% above 50DMA | Bullish | Golden state, but the most extended of this wave's four adds. |
| 3 | RSI-14 | 64.6 | Bullish | Upper-mid 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.85 | Neutral | Above the 0.8 compression threshold. |
| 5 | Volume z-score | 0.24 | Neutral | Doesn't clear either threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +17.6%/24h, +29.8%/7d | Bullish | Strongest OI conviction of this wave. |
| 8 | Stablecoin supply 7d Δ | +0.42% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.22 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 41, Δ7d +12 | Bullish | Rising from Fear toward Neutral. |

**Confluence: 7/10 Bullish, 0/10 Bearish.**

**Expectancy sheet:**
- Entry: $2.131 (Binance spot, fetched 2026-08-18T19:05:57Z via `parameters.py`)
- Target: $2.55 (+19.66%) — momentum continuation backed by the strongest OI signal of this wave, within the 2-8wk horizon
- Invalidation: $1.95 (-8.49%) — below the 50DMA
- R = 19.66 / 8.49 = **2.32** (clears the 2.0 floor)
- Stated p = **0.45** (confluence 7/10, strong OI backing offset by the most-extended DMA deviation of this wave)
- EV = 0.45×19.66% − 0.55×8.49% = **+4.18%** (clears EV>0 floor)
- Tier: **C** (R=2.32 short of Tier B's 2.5 floor) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($499.46 notional, 234.3782 MORPHO)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (AM 2026-08-19); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** none competing for this slot — see CAKE entry above for the shared context (4 confirmed candidates filled exactly 4 open slots).

**Sector:** DeFi Lending. 1 of 5 positions, 1 of 2 max in sector.
