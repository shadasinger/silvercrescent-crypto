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

## EXIT POST-MORTEM — TRX — 2026-08-19 AM (full exit, remaining half)

**P&L:** Two tranches. 08-16 AM trim-half: -$7.22 (proceeds $492.78 vs cost $500.00). 08-19 AM full exit of remainder: -$4.09 (proceeds $495.91 vs cost basis $499.99 at avg entry $0.33595). **Total realized P&L on the hold: -$11.31** on ~$999.55 deployed at peak (10% of portfolio) — roughly -1.13% on the position, -0.11% of total portfolio.

**Realized R vs planned:** Tranche 1: -0.27 vs planned 2.15. Tranche 2: -0.15 vs planned 2.15. Neither tranche came close to the planned R — the position never reached target or hit a hard stop; it was closed on thesis-test failure instead.

**Thesis verdict:** Broken. The entry thesis's stated confirmation leg — "OI keeps expanding alongside price, not diverging" — ran in reverse almost the entire hold. 7d OI went from +19.0% (day of entry) to -13.6% (day of exit), decelerating or negative in 7 of the last 8 checkpoints. Price itself held up reasonably well throughout (never breached invalidation, stayed in golden-cross structure to the end) — this was an OI-divergence failure, not a price-structure failure.

**Per-parameter verdict (frozen AM 2026-08-12 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Neutral | Irrelevant | Never a standalone signal; stayed Neutral-to-mixed most of the hold, no strong read either direction. |
| 2 | DMA | Bullish | Right (but insufficient alone) | Price stayed above both DMAs the entire hold — structure never failed. |
| 3 | RSI | Bullish (66.3) | Right short-term, faded | Cooled from 66→58 over the hold, tracking the broader momentum fade rather than leading it. |
| 4 | Rvol | Bullish | Neutral/uninformative | Compression thesis didn't translate into a breakout; vol stayed muted throughout. |
| 5 | Volume z | Neutral | Uninformative | Never cleared a threshold either direction during the hold. |
| 6 | Funding | Bullish | Right | Stayed near-zero the whole hold — no crowding risk materialized in either direction, as expected. |
| 7 | OI Δ | Bullish | **Wrong — the critical miss** | This was the thesis's named confirmation leg and it inverted almost immediately after entry and kept deteriorating for 7 of 8 checkpoints. The single parameter that should have carried this trade instead killed it. |
| 8 | Stablecoins | Bullish | Irrelevant to this name | Global parameter, applies identically to all coins — no coin-specific information. |
| 9 | MVRV | Bullish | Irrelevant to this name | Same — global regime parameter, not TRX-specific. |
| 10 | F&G | Neutral | Irrelevant to this name | Same — global regime parameter. |

**p calibration:** Stated p=0.42 at entry. Outcome: loss, consistent with p<0.5, but the trade didn't fail on a probabilistic miss (price never hit invalidation) — it failed on thesis-test invalidation via OI, a mechanism the expectancy sheet didn't explicitly price in. Not a clean calibration data point either way.

**Sizing/timing verdict:** Sizing discipline worked as designed — the 08-16 AM trim-half on the first Weakening signal cut expected loss roughly in half versus holding the full position to today's exit. Timing verdict: the exit itself was arguably late, not early — the OI thesis-test had been failing for 6+ checkpoints before this exit; a stricter rule (e.g., act on the first negative 7d OI print rather than waiting for repeated confirmation) would have saved most of the -$11.31.

**Counterfactual vs runner-ups (AM 08-12 entry):** BNB and LINK both armed the checkpoint before TRX's entry and failed to confirm (mechanical counts collapsed). Neither would have been a better outcome to chase — this wasn't a selection-skill miss, TRX was the correct pick of that cohort at entry.

**One testable lesson:** *Hypothesis: when a position's entry thesis names a single specific confirmation metric (here, OI Δ), a sustained reversal in that metric alone — even without 4/10 Bearish or an invalidation breach — should trigger faster de-risking than the general conviction ladder allows. Proposed rule change: add a "named thesis-test breach" exit trigger — 3 consecutive checkpoints of the entry thesis's stated confirmation metric moving the wrong direction should mandate at least a trim, independent of the general Bearish-count gate. Evidence that would confirm: future positions where this rule fires save realized loss vs. the general gate on a backtest of this and future holds. Evidence that would kill it: cases where the named metric round-trips and a fast trim would have cut a position that went on to recover.*

## EXIT POST-MORTEM — CAKE — 2026-08-19 AM (staged-entry cut, no confirmation)

**P&L:** +$11.96 on $499.46 deployed (+2.39% on the half-position, +0.12% of total portfolio). Realized R +0.32 vs planned 2.16 — small win, nowhere near target, but the only one of the four cuts to close green.

**Thesis verdict:** Playing Out, not Broken — this cut was a rule mechanic (no second-half confirmation), not a thesis failure. Price rose +2.4% and OI kept expanding (7d +23.3%, even stronger than entry's +11.6%) in the 12-18 hours between entry and cut.

**Per-parameter verdict (frozen PM 08-18 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Bearish | Wrong direction, right call to flag | Contrarian-Bearish read didn't precede a reversal in the ~12h window — too short a window to fairly judge a sentiment call. |
| 2 | DMA | Bullish | Right | Price extended further above both DMAs by exit. |
| 3 | RSI | Bullish (67.0) | Faded to Neutral (71.6) | Correctly flagged as approaching the top of the healthy band at entry; it crossed into the Neutral zone one checkpoint later, exactly the kind of overextension risk the rubric exists to catch. |
| 4 | Rvol | Bullish | Faded to Neutral | Compression thesis partially exhausted within one checkpoint. |
| 5 | Volume z | Neutral | Flipped Bearish | The move worth watching — the price gain came on thin/negative volume-z, a genuine no-conviction signal that the mechanical rule correctly caught even though price itself was up. |
| 6 | Funding | Bullish | Right | Stayed near-zero. |
| 7 | OI Δ | Bullish | Right, even stronger | 7d OI accelerated from +11.6% to +23.3% — the strongest fundamental confirmation of any parameter in this cut. |
| 8-10 | Global (stables/MVRV/F&G) | Bullish | Right | Regime stayed constructive. |

**p calibration:** Stated p=0.48. Outcome: small win. Single data point, not calibration-informative at n=1.

**Sizing/timing verdict:** The staged-entry rule did its job of limiting downside-if-wrong, but this is the clearest case among the four cuts that the *rule* (not the thesis) drove the exit — RSI/volume-z cooling one checkpoint after entry is a thin bar for cutting a position where price and OI both strengthened. Worth flagging for the monthly review as a possible false-negative case for the staged-confirmation rule.

**Counterfactual vs runner-ups:** N/A — no competing candidate this slot at entry.

**One testable lesson:** *Hypothesis: the staged-entry "cut on no confirmation" rule may be too strict when the cut is driven by RSI/volume-z noise rather than a reversal in price or OI (the two parameters most connected to the entry thesis). Proposed rule change: at the staged-entry confirmation checkpoint, weight price-direction and OI-direction more heavily than the full mechanical count — require confluence ≥7 OR (price up + OI up + confluence ≥5) to hold the second half. Evidence that would confirm: cases like this one where price/OI stayed strong but a low-signal parameter (RSI/volz) forced an unnecessary cut that left money on the table. Evidence that would kill it: cases where price/OI strength was a lagging, not leading, indicator and the mechanical cut correctly avoided a reversal shortly after.*

## EXIT POST-MORTEM — ETH — 2026-08-19 AM (staged-entry cut, no confirmation)

**P&L:** -$0.04 on $499.46 deployed — essentially breakeven. Realized R -0.00 vs planned 2.13.

**Thesis verdict:** Stalled, not Broken — price was flat (-0.01%) over the ~12h hold, the shortest and most inconclusive of the four cuts. The entry thesis explicitly named this the weakest structural setup of the wave (DMA mechanically Neutral, not golden-cross) and flagged it as "the first candidate to cut if the second-half confirmation doesn't come through" — that flag played out exactly as anticipated.

**Per-parameter verdict (frozen PM 08-18 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Bullish (thin margin, logged as lower-conviction) | Correctly flagged as low-conviction | The capitulation tilt that justified it did not reappear the next checkpoint — the "thinner margin than usual" caveat at entry proved prescient. |
| 2 | DMA | Neutral | Right to flag as weakest leg | Never resolved into a golden cross; still the structural gap the entry thesis explicitly said needed to close. |
| 3 | RSI | Bullish | Right, unchanged | Stayed mid-band. |
| 4 | Rvol | Bullish | Right, unchanged | Stayed compressed. |
| 5 | Volume z | Neutral | Unchanged | No new information. |
| 6 | Funding | Bullish | Right | Stayed near-zero. |
| 7 | OI Δ | Bullish | Faded to Neutral | 7d OI decelerated sharply (+13.4%→+2.0%) alongside the flat price — the one parameter that visibly weakened. |
| 8-10 | Global | Bullish | Right | Regime stayed constructive. |

**p calibration:** Stated p=0.42 (already the lowest of the wave, correctly reflecting the weakest setup). Outcome: flat. Consistent with a low-conviction call that didn't resolve either way.

**Sizing/timing verdict:** This is the cleanest validation of the staged-entry rule among the four — the position was flagged at entry as the first cut candidate, and it was the first (tied) to fail confirmation on genuinely fading fundamentals (OI deceleration), not just noisy sub-indicators. Sizing (half-size, 5%) correctly limited exposure to the weakest thesis of the wave.

**Counterfactual vs runner-ups:** N/A.

**One testable lesson:** *Hypothesis: an entry-day self-flagged "weakest structural leg" (here, non-golden-cross DMA) is a reliable predictor of staged-entry non-confirmation. Proposed rule change: when an entry's DMA reads mechanically Neutral rather than Bullish (i.e., not a clean golden cross) at confluence-gate time, cap initial sizing below the standard half-target rather than the full half, since these entries appear more likely to fail next-checkpoint confirmation. Evidence that would confirm: a pattern across future holds where Neutral-DMA entries fail confirmation at a higher rate than golden-cross entries. Evidence that would kill it: a Neutral-DMA entry that confirms and performs as well as golden-cross entries, showing DMA state isn't predictive of confirmation odds.*

## EXIT POST-MORTEM — ZEC — 2026-08-19 AM (staged-entry cut, no confirmation)

**P&L:** -$12.86 on $998.93 deployed (-1.29% on the half-position, -0.13% of total portfolio). Realized R -0.24 vs planned 2.95 — the largest planned-R gap of the four cuts (this was the Tier B, cleanest-structure entry of the wave).

**Thesis verdict:** Stalled, not Broken — price pulled back -1.3% over the ~12h hold, a normal pullback within a still-intact golden-cross structure (still +1.3% above the 50DMA, well clear of invalidation). OI kept expanding (7d +10.0% vs +9.5% at entry) — the core thesis-test held.

**Per-parameter verdict (frozen PM 08-18 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Neutral | Right, unchanged | Stayed factual/flat, no crowd extreme either checkpoint. |
| 2 | DMA | Bullish | Right | Structure held, still golden-cross. |
| 3 | RSI | Neutral (54.8, just under the 55 floor) | Stayed Neutral | The entry table already flagged this as "just under" the Bullish band — it cooled further to a genuine Neutral read, not a reversal, just continued softness. |
| 4 | Rvol | Bullish | Faded to Neutral | Compression thesis partially exhausted, similar pattern to CAKE. |
| 5 | Volume z | Neutral | Unchanged | No new information. |
| 6 | Funding | Bullish | Right | Stayed near-zero. |
| 7 | OI Δ | Bullish | Right, even stronger | 7d OI held up and edged higher — the strongest-performing parameter of this cut, same pattern as CAKE. |
| 8-10 | Global | Bullish | Right | Regime stayed constructive. |

**p calibration:** Stated p=0.45. Outcome: small loss on a short window. Not calibration-informative at n=1, but notable that this was the highest-conviction (Tier B, R=2.95) entry of the wave and still failed same-day confirmation — a reminder that a strong expectancy sheet at entry doesn't buy immunity from the next-checkpoint confirmation bar.

**Sizing/timing verdict:** Like CAKE, the two parameters most tied to the actual thesis (DMA, OI) stayed constructive while softer indicators (RSI, rvol) drove the mechanical count below 7 — a recurring pattern across three of the four cuts this checkpoint (CAKE, ETH, ZEC) worth flagging together for the monthly review.

**Counterfactual vs runner-ups:** N/A.

**One testable lesson:** *Hypothesis: three of today's four staged-entry cuts (CAKE, ETH, ZEC) failed confirmation primarily because RSI and realized-vol-ratio cooled from the top of their Bullish bands to Neutral one checkpoint after entry, while price and OI — the parameters most connected to each thesis — stayed constructive or improved. This suggests entries clustered near the top of the RSI/rvol Bullish bands (RSI 65-70, rvol near 0.75-0.80) are structurally likely to roll to Neutral within one checkpoint on pure mean-reversion, independent of thesis quality. Proposed rule change: at the staged-entry confirmation checkpoint, if the ONLY parameters that rolled over are RSI and/or rvol (both mean-reverting, range-bound indicators) while price, OI, and DMA all held or improved, treat that as a softer non-confirmation — hold the half rather than cutting, revisit at the following checkpoint. Evidence that would confirm: held-instead-of-cut positions matching this pattern subsequently re-qualify and outperform a full cut. Evidence that would kill it: this same pattern preceding a subsequent invalidation breach, showing RSI/rvol rollover was an early warning that should not be ignored.*

## EXIT POST-MORTEM — MORPHO — 2026-08-19 AM (staged-entry cut, no confirmation)

**P&L:** -$18.98 on $499.46 deployed (-3.80% on the half-position, -0.19% of total portfolio) — the largest loss of today's four cuts. Realized R -0.45 vs planned 2.32.

**Thesis verdict:** Broken on the specific named metric, within one checkpoint. The entry thesis called this "the strongest OI conviction of the four adds (24h+17.6%, 7d+29.8%)" and flagged overextension (dev-from-50DMA +7.0%, the most extended of the wave) as "the main structural risk to watch, not a lack of momentum." Both risks materialized simultaneously: 24h OI reversed to -16.3% and price fell -3.8%, the sharpest same-day reversal of any of today's four cuts.

**Per-parameter verdict (frozen PM 08-18 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Neutral | Right, unchanged | Stayed factual/flat both checkpoints. |
| 2 | DMA | Bullish | Faded but held | Still above 50DMA, extension eased from +7.0% to +2.8% on the pullback — consistent with the overextension risk flagged at entry. |
| 3 | RSI | Bullish (64.6) | Right, roughly unchanged | Held mid-band (56.4). |
| 4 | Rvol | Neutral | Unchanged | No new information. |
| 5 | Volume z | Neutral | Unchanged | No new information. |
| 6 | Funding | Bullish | Right | Stayed near-zero. |
| 7 | OI Δ | Bullish | **Wrong — the critical miss, same day** | The single parameter the entry thesis leaned on hardest inverted within one checkpoint (24h OI +17.6%→-16.3%). Overridden Bullish→Bearish this checkpoint on rubric-misread grounds. |
| 8-10 | Global | Bullish | Right | Regime stayed constructive. |

**p calibration:** Stated p=0.45. Outcome: the largest loss of the four cuts, on the position the entry thesis itself flagged as carrying the most structural risk (overextension). The self-identified risk factor was the one that fired.

**Sizing/timing verdict:** The half-size staging and same-checkpoint cut worked exactly as designed here — this is the strongest validation this checkpoint of why the staged-entry rule exists: an aggressive, extended entry reversed hard and fast, and the rule caught it after one checkpoint rather than after a full-size position rode it down further.

**Counterfactual vs runner-ups:** N/A.

**One testable lesson:** *Hypothesis: entries where dev-from-50DMA is the most extended of a confirmed-candidate cohort (here, MORPHO's +7.0% vs +1.3-6.4% for CAKE/ZEC/ETH) carry disproportionate same-day reversal risk even when OI backing looks strongest, because extended OI/price moves are also the ones most prone to sharp mean-reversion. Proposed rule change: when a confirmed candidate's dev-from-50DMA exceeds ~2x the cohort median at entry, cap its initial stage-1 size below the standard half-target regardless of tier/R, and treat any single-checkpoint OI reversal (not just a sustained one) as sufficient for a hard cut. Evidence that would confirm: future extended entries showing this same fast-reversal pattern. Evidence that would kill it: extended entries that continue trending without reversal, showing overextension alone isn't predictive.*

## ENTRY — XLM — 2026-08-21 AM

**Confluence history:** armed PM 2026-08-20 (8/10), confirmed AM 2026-08-21 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (AM 2026-08-21, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | interest rising; euphoria markers ("40% pump" chatter, price targets 0.3+, Trump/CLARITY-Act tailwind narrative) | Bearish | Crowd arriving, no capitulation offset — contrarian Bearish, the one caution flag on an otherwise clean mechanical picture. |
| 2 | Price vs 50/200DMA | $0.1874 vs 50DMA $0.177084, 200DMA $0.172997; +5.8% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA, moderate extension. |
| 3 | RSI-14 | 67.4 | Bullish | Mid-band 55-70. |
| 4 | Realized vol ratio 7d/30d | 1.39 | Bullish | Expansion on an upside breakout. |
| 5 | Volume z-score | -0.20 | Neutral | Doesn't clear either threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +1.5%/24h, +8.3%/7d | Bullish | OI rising with price rising. |
| 8 | Stablecoin supply 7d Δ | +0.51% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.39 / ETH 1.10 | Bullish | Healthy sub-2 band. |
| 10 | Fear & Greed | 72, Δ7d +43 | Neutral | Approaching but not past the 75 overheated threshold; largest weekly swing logged this phase. |

**Confluence: 7/10 Bullish, 1/10 Bearish.** (Mechanical p2-p10 unchanged/clean at 7/9 Bullish, 0 Bearish across both the arming and confirming checkpoints — the total eased from 8 to 7 solely because p1 flipped Neutral→Bearish on today's data, not because any structural leg weakened.)

**Expectancy sheet:**
- Entry: $0.1874 (Binance spot, fetched 2026-08-21T07:10:07Z via `parameters.py`)
- Target: $0.223 (+19.00%) — continuation within the 2-8wk horizon, consistent with the +18.5% 7d move already behind it
- Invalidation: $0.170 (-9.28%) — below the 200DMA, breaking the golden-cross structure
- R = 19.00 / 9.28 = **2.05** (clears the 2.0 floor)
- Stated p = **0.42** (confluence 7/10, tempered by the contrarian-Bearish sentiment flag and a market-wide F&G reading close to the overheated line)
- EV = 0.42×19.00% − 0.58×9.28% = **+2.59%** (clears EV>0 floor)
- Tier: **C** (R=2.05 falls short of Tier B's 2.5 floor) → size band 5-15%
- Sizing: target 10% (low-Tier-C, conservative given the broad market extension), staged half-open this checkpoint = **5% ($498.44 notional, 2659.7652 XLM)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-21); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** FIL (armed PM 2026-08-20 at 7/10) lapsed to 6/10 (p5_volz rolled Bullish→Bearish, p1 read Neutral not Bullish) — no confirmation. PEPE (armed PM 2026-08-20 at 7/10) lapsed sharply to 4/10 (RSI cooled to Neutral, funding flipped Bearish) — no confirmation. No other coin reached a first-occurrence arm this checkpoint; next-highest non-arming reads were TRX/UNI/MORPHO/ONDO/ARB/SHIB/JUP at 6/10.

**Sector:** Payments. 1 of 5 positions, 1 of 2 max in sector.

**Context note:** this entry opens into a market-wide melt-up with F&G at 72 (Δ7d +43, the sharpest weekly swing logged this phase) and broad RSI overextension across the watchlist (BTC 83.8, ETH 85.7, SOL 80.6, BNB 80.3, XRP 79.8, LINK 83.7). XLM is the only coin on the board that cleared 7/10 cleanly on structure (moderate 5.8% extension, RSI still mid-band, OI genuinely confirming) rather than riding the broad beta wave that pushed most majors into overbought/euphoric territory and correctly excluded them via p3/p1. Sized at the conservative end of Tier C for this reason — see the AM 2026-08-21 checkpoint report red-team pass for the full reasoning.

## STAGE-2 ADD — XLM — 2026-08-21 PM

Confluence held **8/10 Bullish, 0/10 Bearish** at this checkpoint (immediate next trading checkpoint since the AM 08-21 half-open, count 7/10 -> 8/10) — per Section 5 step 9, the second half opens at full target size; the rule requires the count to hold >=7, and here it strengthened rather than merely held.

Mechanical parameters improved from AM (p6 funding rolled Neutral->Bullish; DMA golden-state, RSI mid-band, rvol/volz/OI/stables/MVRV all unchanged Bullish); p1 sentiment cooled from AM's contrarian-Bearish euphoria read ("40% pump" chatter, price targets) to Neutral this checkpoint — flat interest, zero euphoria and zero capitulation markers, narrative fundamentals-led (Stellar developer growth, institutional interest) with a mild lag-frustration undertone rather than a crowd extreme. Price $0.1897 (+1.23% vs entry $0.1874), OI accelerating (24h +27.7%, 7d +37.1%, both well above AM's +1.5%/+8.3%), invalidation $0.170 not breached (11.3% headroom).

**Fill:** BUY 2627.5171 XLM @ $0.1897 = $498.44 notional, 2026-08-21T19:14:11Z (Binance spot via `parameters.py` refresh). Position now 5287.2823 XLM, avg entry $0.188543, ~10.06% of portfolio ($1,003.00 / $9,974.91) — full target size reached. No further staging; ongoing test is the same OI/price/DMA structure through the 2026-09-04 interim review.

## ENTRY — UNI — 2026-08-22 AM

**Confluence history:** armed PM 2026-08-21 (8/10), confirmed AM 2026-08-22 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (AM 2026-08-22, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | interest flat; mild euphoria markers ("25% up", "cooking", breakout talk) but thin/normal-trader framing, no crowd-wide dominance, no capitulation offset needed | Neutral | Doesn't clear the Bearish bar (not "everyone's in"), doesn't clear the Bullish bar either (no improving-interest-without-euphoria or capitulation pattern) — genuinely mixed/mild, logged Neutral. |
| 2 | Price vs 50/200DMA | $4.214 vs 50DMA $3.6958, 200DMA $3.4287; +14.0% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA, moderate extension (under the 25% overextension line). |
| 3 | RSI-14 | 64.6 | Bullish | Mid-upper 55-70 band, still has room before overheated. |
| 4 | Realized vol ratio 7d/30d | 0.83 | Neutral | Just above the 0.8 compression threshold — doesn't clear either bar. |
| 5 | Volume z-score | +1.23 | Bullish | z > +1 on up days. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk despite the broad market-wide funding heat elsewhere. |
| 7 | Open interest Δ | -11.5%/24h, +3.7%/7d | Bullish | 7d trend (the more stable window) still confirms the uptrend even though the 24h print pulled back; not treated as a divergence override. |
| 8 | Stablecoin supply 7d Δ | +0.68% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.48 | Bullish | Healthy 1-2 band. |
| 10 | Fear & Greed | 71, Δ7d +37 | Neutral | Elevated and rising fast but not past the 75 overheated threshold. |

**Confluence: 7/10 Bullish, 0/10 Bearish.** Mechanical p2-p10 read 7 Bullish/0 Bearish/2 Neutral both the arming (PM 08-21, 8/10) and confirming (AM 08-22, 7/10) checkpoints — the one-point drop from 8 to 7 is p6 funding easing from Bullish (arming) to... actually funding stayed Bullish; the drop traces to p1 cooling from the PM 08-21 read to today's Neutral read plus one mechanical parameter easing. Structure itself stayed clean (0/10 Bearish both checkpoints).

**Expectancy sheet:**
- Entry: $4.214 (Binance spot, fetched 2026-08-22T07:xx via `parameters.py`)
- Target: $5.342 (+26.77%) — continuation off the already-strong +30.1% 7d move, consistent with the 2-8wk horizon
- Invalidation: $3.65 (-13.38%) — just under the 50DMA ($3.6958), breaking the golden-cross structure
- R = 26.77 / 13.38 = **2.00** (exactly at the floor)
- Stated p = **0.40** (Tier C floor; deliberately conservative — UNI is already +30.1% in 7 days and entering into a market-wide melt-up, not a fresh breakout)
- EV = 0.40×26.77% − 0.60×13.38% = **+2.68%** (clears EV>0 floor)
- Tier: **C** (R sits exactly at the 2.0 floor, well short of Tier B's 2.5) → size band 5-15%
- Sizing: target 10%, staged half-open this checkpoint = **5% ($504.80 notional, 119.791 UNI)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-22); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** TRX, ONDO, JUP all armed PM 2026-08-21 (7/10) and all LAPSED this checkpoint — TRX and JUP fell to 6/10 (mechanical count eased one notch each, p1 Neutral), ONDO fell to 5/10 (mechanical rvol/volz softened, plus a red-flag-adjacent p1 Bearish read on an unverified team-multisig-to-Coinbase claim). No other coin reached a first-occurrence arm this checkpoint; next-highest fresh reads were ASTER/MORPHO/SOL/ZEC at 6/10.

**Sector:** DEX. 2 of 5 positions, 1 of 2 max in sector (CAKE/JUP/ASTER also DEX-tagged on the watchlist but none currently held).

**Context note:** this entry opens into the same broad market-wide melt-up flagged at the XLM 2026-08-21 entry, now further advanced — BTC RSI 82.5 (up from 83.8→ still extreme), F&G 71 (Δ7d +37), most majors mechanically Bearish on p3 RSI and p6 funding this checkpoint (AAVE, ADA, ARB, BCH, BNB, BTC, CAKE, DOGE, ENA, ETH, HBAR, LINK, PEPE, SOL, TRX, XRP, ZEC all print at least one Bearish mechanical read from overheating). UNI is one of only two coins (with XLM held) that cleared 7/10 cleanly this checkpoint, on genuinely moderate extension (+14.0% vs 50DMA, RSI 64.6 mid-band) rather than riding the broad beta wave into overbought territory. R sitting exactly at the 2.0 floor and p held at the Tier C floor (0.40) reflect deliberate conservatism given the market-wide overheating — see the AM 2026-08-22 checkpoint report red-team pass for the full reasoning.
