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

## EXIT POST-MORTEM — UNI — 2026-08-22 PM (staged-entry cut, no confirmation)

**P&L:** +$5.15 on $504.80 deployed (+1.02% on the half-position, +0.05% of total portfolio). Realized R +0.08 vs planned 2.00 — a small win, the second of five staged-entry cuts (after CAKE 08-19) to close green rather than flat/red.

**Thesis verdict:** Playing Out, not Broken — this cut was a rule mechanic (no second-half confirmation), not a thesis failure. Price actually rose +1.02% (from $4.214 to $4.257) and OI held constructive (24h +12.5%, 7d +19.3%, both still positive) in the ~12 hours between entry and cut; the confluence drop was driven by funding crossing the crowded-long threshold, not by price or OI weakening.

**Per-parameter verdict (frozen AM 08-22 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Neutral | Right | Interest kept falling (mech read at exit also Neutral, no crowd extreme) — no reversal signal from this parameter either way. |
| 2 | DMA | Bullish | Right | Price extended further above the 50DMA by exit (dev 15.2% vs 14.0% at entry). |
| 3 | RSI | Bullish (64.6) | Right, strengthened | Rose to 65.4, still comfortably mid-band, no overheating signal. |
| 4 | Rvol | Neutral (0.83) | Faded slightly (0.81) | Stayed right at the borderline Neutral read both checkpoints — never actually resolved either direction. |
| 5 | Volume z | Bullish | Right, strengthened | Rose to 3.6 from entry's level, still confirming. |
| 6 | Funding | Bullish (0.01%/8h) | Flipped Bearish (0.0761%/8h) | **The parameter that actually drove the cut** — funding rate moved from flat to crossing the ~0.05%/8h crowded-long threshold in a single checkpoint, a genuinely fast-moving signal on this name specifically (most of the board saw funding heat up this checkpoint, so this may be partly a beta effect rather than UNI-specific crowding). |
| 7 | OI Δ | Bullish | Right | 24h/7d OI both stayed positive and roughly stable (+12.5%/+19.3% vs entry's -11.5%/+3.7% — actually an improvement on the 24h print). |
| 8-10 | Global (stables/MVRV/F&G) | Bullish/Bullish/Neutral | F&G faded to Neutral | F&G eased 71→71 flat but the mechanical read still resolved Neutral both checkpoints (unchanged); p8/p9 stayed Bullish. |

**p calibration:** Stated p=0.40. Outcome: small win at n=1, not calibration-informative on its own, but directionally consistent (conservative p, positive small outcome).

**Sizing/timing verdict:** Same pattern as the CAKE 08-19 cut — the staged-confirmation rule fired on a single fast-moving parameter (funding) while price and OI, the two legs most directly tied to the entry thesis, both held or strengthened. This is now the second of five staged-entry cuts where price moved in the intended direction after the cut rather than against it, worth weighing at the monthly review alongside the CAKE precedent and the existing LESSONS.md hypothesis on this exact failure mode.

**Counterfactual vs runner-ups:** TRX/ONDO/JUP (the three PM 08-21 arms that lapsed at AM 08-22) stayed lapsed this PM checkpoint too (all at or below 6/10) — none would have been a better use of the freed capital had UNI's second half opened instead of cutting.

**One testable lesson:** *Hypothesis: same as the CAKE 08-19 finding — the staged-entry "cut on no confirmation" rule doesn't distinguish between a confluence drop driven by price/OI reversing (a real thesis-test failure) and one driven by a single fast-moving overlay parameter like funding, especially during a market-wide melt-up where funding is heating up across most of the board simultaneously (a regime effect, not a UNI-specific one). Proposed rule change: at the staged-entry confirmation checkpoint, treat a confluence drop driven solely by p6 funding or p10 F&G (the two parameters most likely to move on broad-market beta rather than idiosyncratic weakening) as insufficient on its own to cut — require price direction or OI direction to also have reversed. Evidence that would confirm: further cases (this one, CAKE 08-19) where the cut was funding/global-driven and price/OI kept confirming post-cut. Evidence that would kill it: a case where funding alone deteriorating was the leading indicator of an actual reversal one or two checkpoints later.*

## ENTRY SNAPSHOT — ONDO — 2026-08-24 AM

**Confluence history:** armed PM 2026-08-23 (8/10), confirmed AM 2026-08-24 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (AM 2026-08-24, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | interest rising, dominant euphoria ($1.40/+1500% price targets, rocket emojis, new-ATH scenarios), zero capitulation offset | Bearish | Rubric's "euphoria/everyone's in" branch fires cleanly — a flip from PM 08-23's Neutral read as hype intensified alongside the price extension. |
| 2 | Price vs 50/200DMA | $0.3757 vs 50DMA $0.358702, 200DMA $0.317495; +4.7% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA, the least-extended structure of any coin confirmed this month. |
| 3 | RSI-14 | 55.4 | Bullish | Mid-band, well clear of overbought, plenty of room to extend. |
| 4 | Realized vol ratio 7d/30d | 1.56 | Bullish | Expansion on an upside breakout. |
| 5 | Volume z-score | -0.7 | Neutral | Below the +1 threshold, doesn't clear the Bullish bar. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +0.9%/24h, +62.2%/7d | Bullish | Strong, accelerating 7d OI confirming the uptrend alongside price. |
| 8 | Stablecoin supply 7d Δ | +0.77% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.47 | Bullish | Healthy 1-2 band. |
| 10 | Fear & Greed | 73, Δ7d +42 | Neutral | Elevated but the mechanical read stays Neutral (not past the overheated cut). |

**Confluence: 7/10 Bullish, 1/10 Bearish.** Mechanical p2-p10 read 7 Bullish/0 Bearish/2 Neutral both the arming (PM 08-23, 8/10) and confirming (AM 08-24, 7/10) checkpoints — unchanged, clean structure both times. The one-point drop from 8 to 7 total is entirely p1 sentiment flipping from PM's Neutral to today's contrarian-Bearish as euphoria markers appeared.

**Expectancy sheet:**
- Entry: $0.3757 (Binance spot, fetched 2026-08-24T07:14:11Z via `parameters.py`)
- Target: $0.45 (+19.78%) — consistent with the 2-8wk horizon, below the euphoric $1.40 social-media targets
- Invalidation: $0.34 (-9.50%) — just under the 50DMA ($0.358702), breaking the golden-cross structure
- R = 19.78 / 9.50 = **2.08**
- Stated p = **0.42** (Tier C; the clean, low-extension mechanical structure argues for slightly above the 0.40 floor, but the fresh sentiment euphoria flag caps confidence below 0.45)
- EV = 0.42×19.78% − 0.58×9.50% = **+2.79%** (clears EV>0 floor)
- Tier: **C** (R=2.08, just above the 2.0 floor) → size band 5-15%
- Sizing: target 10%, staged half-open this checkpoint = **5% ($500.91 notional, 1333.2614 ONDO)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-24); no confirmation there cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint:** ICP armed fresh this checkpoint (6/10 PM 08-23 → 7/10 AM 08-24, p1 flipped contrarian-Bullish on a capitulation-while-thesis-intact read) — first occurrence, not a second-consecutive confirmation, so it did not compete for this slot. No other coin reached 7/10; next-highest reads were a wide 6/10 cluster (ADA, UNI, CAKE, JUP, SHIB — several carrying their own p1 Bearish flags).

**Sector:** RWA (new sector for the book — no existing RWA exposure). 2 of 5 positions (with XLM), 1 of 2 max in sector.

**Context note:** entered inside the same broad melt-up flagged at every recent entry — BTC RSI 80.8, ETH RSI elevated, F&G 73 (Δ7d +42, the highest reading of the hold to date). ONDO's own structure (only +4.7% dev-from-50DMA, RSI 55.4 mid-band) is notably less extended than the board average, which is the main reason conviction in the mechanical picture stayed high despite the melt-up backdrop; the p1 euphoria flag is logged as the explicit watch item, mirroring the same pattern already being tracked on the XLM hold.

## STAGE-2 ADD — ONDO — 2026-08-24 PM

Confluence held **8/10 Bullish, 0/10 Bearish** at this checkpoint (immediate next trading checkpoint since the AM 08-24 half-open, count 7/10 -> 8/10) — per Section 5 step 9, the second half opens at full target size; the rule requires the count to hold >=7, and here it strengthened rather than merely held.

Mechanical parameters unchanged from AM (7/9 Bullish, 0 Bearish — p5 volz, p10 F&G still Neutral); p1 sentiment cooled from AM's contrarian-Bearish euphoria read ($1.40/+1500% targets, rocket emojis, new-ATH calls) to contrarian-Bullish this checkpoint — rising interest with no euphoria markers and no capitulation markers, base-building/double-bottom/support-defense framing read as measured technical chatter rather than a hype stack, fitting the p1 Bullish branch ("improving interest without euphoria") on its own terms rather than being read generously to justify the add. Price $0.3814 (+1.52% vs entry $0.3757), still the least-extended structure on the board (dev-from-50DMA +6.3%), OI accelerating (24h +5.0%, 7d +83.5%, both above AM's +0.9%/+62.2%), invalidation $0.34 not breached (~10.9% headroom).

**Fill:** BUY 1313.3456 ONDO @ $0.3814 = $500.91 notional, 2026-08-24T19:05:45Z (Binance spot via `parameters.py` refresh). Position now 2646.607 ONDO, avg entry $0.378529, ~10.09% of portfolio ($1,009.42 / $10,000.87) — full target size reached. No further staging; ongoing test is the same OI/price/DMA structure through the 2026-09-07 interim review.

## ENTRY — MORPHO — 2026-08-26 AM

**Frozen 10-parameter table (AM 2026-08-26, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | flat interest, no clean euphoria/capitulation dominance (isolated buy-dip/$4.20-ATH-target chatter diluted by trending-list spam) | Neutral | Neither branch fires cleanly. |
| 2 | Price vs 50/200DMA | $2.516 vs 50DMA $2.06728, 200DMA $1.877215; +21.7% above 50DMA | Bullish | Golden state: price > 50DMA > 200DMA, moderately extended, under the 25% overextension line. |
| 3 | RSI-14 | 61.9 | Bullish | Mid-band, room to extend. |
| 4 | Realized vol ratio 7d/30d | 1.85 | Bullish | Expansion on an upside breakout. |
| 5 | Volume z-score | -0.57 | Neutral | Below the +1 threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | -7.0%/24h, +41.6%/7d | Bullish | Strong weekly OI confirming the uptrend; single-day 24h dip not a divergence against the dominant weekly trend. |
| 8 | Stablecoin supply 7d Δ | +1.09% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.48 | Bullish | Healthy 1-2 band. |
| 10 | Fear & Greed | 65, Δ7d +19 | Neutral | Elevated but not past the mechanical overheated cut. |

**Confluence: 7/10 Bullish, 0/10 Bearish.** Second consecutive checkpoint >=7/10 (PM 08-25 7/10 armed, 0/10 Bearish -> AM 08-26 7/10 confirmed, 0/10 Bearish) — the cleanest mechanical read of the four candidates (MORPHO, JUP, AAVE, ASTER) that reached confirmation this checkpoint.

**Expectancy sheet:**
- Entry: $2.516 (Binance spot, fetched 2026-08-26T07:18:08Z via `parameters.py`)
- Target: $3.0066 (+19.50%)
- Invalidation: $2.2795 (-9.40%) — below the recent breakout support, well above the 50DMA
- R = 19.50 / 9.40 = **2.07**
- Stated p = **0.40** (Tier C floor; clean 0/10-Bearish mechanical structure, but +21.7% extension caps confidence at the floor)
- EV = 0.40×19.50% − 0.60×9.40% = **+2.16%**
- Tier: **C** → size band 5-15%
- Sizing: target 10%, staged half-open this checkpoint = **5% ($496.06 notional, 197.1634 MORPHO)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-26); no confirmation there cuts the half.

**Runner-up candidates this checkpoint — the 4-way EV tie-break:** MORPHO, JUP, AAVE, and ASTER all confirmed at exactly 7/10 Bullish this checkpoint, competing for 3 open slots (max 5 concurrent positions, XLM and ONDO already held). Per Section 5 step 6, confluence-count ties break on EV: **ASTER +2.45% > MORPHO +2.16% > JUP +1.96% > AAVE +1.58%.** AAVE — the only one of the four carrying a Bearish flag (p2_dma, dev-from-50DMA +32.2%, the most extended read on the board) — lost the tie-break and was assigned a lower stated p (0.38) reflecting that standing overextension risk (flagged explicitly in the PM 08-25 red-team pass). AAVE is logged as a rejected confirmed-candidate in `state/SHADOW_BOOK.md` with a virtual entry at today's price for ongoing comparison. CAKE, the fifth coin armed at PM 08-25, lapsed (mechanical count eased to 5/9, total 5/10) and did not reach confirmation. TRX newly armed this checkpoint (7/10, first occurrence) — not yet eligible for confirmation.

**Sector:** DeFi Lending (new sector for the book). 3 of 5 positions after this checkpoint's three entries (with XLM, ONDO), 1 of 2 max in sector.

**Context note:** entered inside the ongoing broad melt-up (BTC RSI 80.5, F&G 65 Δ7d+19) that has been the standing pre-mortem base case for every recent entry — three simultaneous half-sized staged entries this checkpoint raise the book's altcoin beta materially (from 2 to 5 positions, ~20% to ~35% deployed), a point raised explicitly in this checkpoint's red-team pass.

## ENTRY — JUP — 2026-08-26 AM

**Frozen 10-parameter table (AM 2026-08-26, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | scam/fake-airdrop-bait euphoria discounted as inauthentic; genuine capitulation markers (-6.4% 24h drop, "rebound hopes?") + undervalued/long-term-conviction chatter | Bullish | Capitulation-while-thesis-intact branch, consistent with the PM 08-25 discount-euphoria precedent. |
| 2 | Price vs 50/200DMA | $0.2145 vs 50DMA $0.191998, 200DMA $0.183816; +11.7% above 50DMA | Bullish | Golden state, the least-extended structure of the four confirmed candidates. |
| 3 | RSI-14 | 66.7 | Bullish | Mid-upper band, room to extend. |
| 4 | Realized vol ratio 7d/30d | 1.21 | Neutral | Below the 0.8 compression bar and below the expansion-on-breakout read. |
| 5 | Volume z-score | -0.81 | Neutral | Below the +1 threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | -7.2%/24h, +17.0%/7d | Bullish | Weekly OI confirming the uptrend; single-day dip not a divergence. |
| 8 | Stablecoin supply 7d Δ | +1.09% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.48 | Bullish | Healthy 1-2 band. |
| 10 | Fear & Greed | 65, Δ7d +19 | Neutral | Elevated but not past the mechanical overheated cut. |

**Confluence: 7/10 Bullish, 0/10 Bearish.** Second consecutive checkpoint >=7/10 (PM 08-25 7/10 armed, 0/10 Bearish -> AM 08-26 7/10 confirmed, 0/10 Bearish).

**Expectancy sheet:**
- Entry: $0.2145 (Binance spot, fetched 2026-08-26T07:18:08Z via `parameters.py`)
- Target: $0.2563 (+19.49%)
- Invalidation: $0.1943 (-9.42%) — below the recent breakout support, just under the 50DMA
- R = 19.49 / 9.42 = **2.07**
- Stated p = **0.40** (Tier C floor)
- EV = 0.40×19.49% − 0.60×9.42% = **+1.96%**
- Tier: **C** → size band 5-15%
- Sizing: target 10%, staged half-open this checkpoint = **5% ($496.06 notional, 2312.648 JUP)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-26); no confirmation there cuts the half.

**Runner-up candidates:** see the MORPHO entry above for the full 4-way EV tie-break (ASTER +2.45% > MORPHO +2.16% > JUP +1.96% > AAVE +1.58%) and the CAKE-lapsed / TRX-newly-armed context.

**Sector:** DEX. 3 of 5 positions after this checkpoint (with XLM, ONDO); DEX will be at 2/2 max once ASTER also enters below.

**Context note:** same melt-up backdrop as MORPHO above.

## ENTRY — ASTER — 2026-08-26 AM

**Frozen 10-parameter table (AM 2026-08-26, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | capitulation-heavy despair dominant (35-week stagnation complaints, "-73% underperformance vs other perps DEXes", "only project down" vs BTC/ETH/SOL/BNB), no euphoria offset, no new confirmed red-flag event | Bullish | Genuine crowd despair on an intact underlying (buyback/burn, staking APY) thesis, consistent with the PM 08-25 read. |
| 2 | Price vs 50/200DMA | $0.704 vs 50DMA $0.62414, 200DMA $0.660705; +12.8% above 50DMA | Neutral | Above both DMAs but the mechanical rubric reads this dev band as Neutral rather than clean golden-state Bullish. |
| 3 | RSI-14 | 67.7 | Bullish | Mid-upper band, room to extend. |
| 4 | Realized vol ratio 7d/30d | 1.79 | Bullish | Expansion on an upside breakout. |
| 5 | Volume z-score | -0.53 | Neutral | Below the +1 threshold. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +6.6%/24h, +118.4%/7d | Bullish | The strongest OI confirmation of any candidate this checkpoint, both windows accelerating. |
| 8 | Stablecoin supply 7d Δ | +1.09% | Bullish | Sideline liquidity growing. |
| 9 | MVRV (BTC proxy) | BTC 1.48 | Bullish | Healthy 1-2 band. |
| 10 | Fear & Greed | 65, Δ7d +19 | Neutral | Elevated but not past the mechanical overheated cut. |

**Confluence: 7/10 Bullish, 0/10 Bearish.** Second consecutive checkpoint >=7/10 (PM 08-25 7/10 armed, 0/10 Bearish -> AM 08-26 7/10 confirmed, 0/10 Bearish).

**Expectancy sheet:**
- Entry: $0.704 (Binance spot, fetched 2026-08-26T07:18:08Z via `parameters.py`)
- Target: $0.8413 (+19.50%)
- Invalidation: $0.6378 (-9.40%) — below the recent breakout support, well under the 50DMA
- R = 19.50 / 9.40 = **2.07**
- Stated p = **0.41** (Tier C; slightly above the floor given the strongest OI confirmation of the group and a clean capitulation-driven sentiment setup)
- EV = 0.41×19.50% − 0.59×9.40% = **+2.45%** — the highest of the four confirmed candidates
- Tier: **C** → size band 5-15%
- Sizing: target 10%, staged half-open this checkpoint = **5% ($496.06 notional, 704.6349 ASTER)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (PM 2026-08-26); no confirmation there cuts the half.

**Runner-up candidates:** see the MORPHO entry above for the full 4-way EV tie-break and the CAKE-lapsed / TRX-newly-armed context. ASTER won the tie-break outright on the highest EV of the group.

**Sector:** DEX, 2/2 max reached (with JUP). 5 of 5 positions after this checkpoint's three entries — book is now at maximum concurrent positions.

**Context note:** ASTER has been inside its 2-week minimum-hold window since being added to the watchlist 2026-08-16 (unlocks 2026-08-30) — irrelevant to entry eligibility (the minimum-hold rule governs rotation-off, not trading), noted for completeness.

## EXIT POST-MORTEM — JUP — 2026-08-26 PM (staged-entry cut, no confirmation)

**P&L:** +$4.63 on $496.06 deployed (+0.93% on the half-position, +0.05% of total portfolio). Realized R +0.099 vs planned 2.07 — a small win, not a loss.

**Thesis verdict:** Playing Out, not Broken — this cut was a rule mechanic (no second-half confirmation), not a thesis failure. Price rose +0.93% and the mechanical p2-10 picture stayed unchanged (6/9 Bullish, 0 Bearish, both checkpoints) between the AM entry and this PM cut.

**Per-parameter verdict (frozen AM 08-26 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Bullish (contrarian, capitulation read) | Flipped Neutral | AM's -6.4%-drop/capitulation chatter did not repeat this checkpoint; flat interest, no crowd extreme. The single parameter that drove the cut. |
| 2 | DMA | Bullish | Right | Price extended further above both DMAs. |
| 3 | RSI | Bullish | Right | Stayed in the healthy band. |
| 4 | Rvol | Neutral | Unchanged | No signal either way. |
| 5 | Volume z | Neutral | Unchanged | No signal either way. |
| 6 | Funding | Bullish | Right | Stayed flat, no crowding. |
| 7 | OI Δ | Bullish | Right | Confirmation held. |
| 8-10 | Global (stables/MVRV/F&G) | Bullish/Neutral | Right | Regime unchanged. |

**p calibration:** Stated p=0.40. Outcome: small win. Single data point, not calibration-informative at n=1.

**Sizing/timing verdict:** Same pattern as the CAKE/ZEC/UNI precedents already logged in LESSONS.md hypotheses #2 and #9 — but this time the sole driver is p1 sentiment (a judgment-call parameter, not a mechanical sub-indicator), which is a distinct mechanism from those hypotheses (RSI/rvol or funding/F&G rollover). The rule fired correctly on its own terms: a genuine re-read of the sentiment window, not noise in a technical indicator.

**Counterfactual vs runner-ups:** AAVE took the freed slot this same checkpoint (see AAVE entry below) — the book stayed at its post-cut position count rather than sitting idle.

**One testable lesson:** No new hypothesis — this is a p1-driven staged-entry cut, already covered conceptually by LESSONS.md hypothesis #8 (p1 volatility/asymmetry in a rising tape). Logged as an additional data point rather than a new entry.

## EXIT POST-MORTEM — ASTER — 2026-08-26 PM (staged-entry cut, no confirmation)

**P&L:** -$2.82 on $496.06 deployed (-0.57% on the half-position, -0.03% of total portfolio). Realized R -0.060 vs planned 2.07 — a small loss.

**Thesis verdict:** Playing Out, not Broken — this cut was a rule mechanic (no second-half confirmation), not a thesis failure. Price was essentially flat (-0.57%) and the mechanical p2-10 picture stayed unchanged (6/9 Bullish, 0 Bearish, both checkpoints) between the AM entry and this PM cut.

**Per-parameter verdict (frozen AM 08-26 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Bullish (contrarian, capitulation read) | Flipped Neutral | AM's one-sided despair stack (35-week-stagnation complaints, no euphoria offset) was genuinely balanced this run by fresh euphoria ($2-3 targets, "most bullish in months") alongside the persisting despair — no longer a clean crowd extreme either way. |
| 2 | DMA | Neutral | Unchanged | Never a clean golden cross at entry — the weakest structural leg from the start. |
| 3 | RSI | Bullish | Right | Stayed in the healthy band. |
| 4 | Rvol | Bullish | Right | Held. |
| 5 | Volume z | Neutral | Unchanged | No signal either way. |
| 6 | Funding | Bullish | Right | Stayed flat, no crowding. |
| 7 | OI Δ | Bullish | Right | The strongest OI confirmation of the four-way tie-break (7d +118.4% at entry) held through the cut. |
| 8-10 | Global (stables/MVRV/F&G) | Bullish/Neutral | Right | Regime unchanged. |

**p calibration:** Stated p=0.41. Outcome: small loss. Single data point, not calibration-informative at n=1.

**Sizing/timing verdict:** Same mechanism as JUP above — p1 sentiment genuinely cooling from one-sided despair to a balanced mix is the entire driver, not a mechanical sub-indicator rollover. The Neutral p2_dma at entry (never a clean golden cross) was the one structural yellow flag named at entry; it stayed Neutral through the cut rather than deteriorating further.

**Counterfactual vs runner-ups:** AAVE took one of the two slots freed this checkpoint by the JUP+ASTER cuts (see AAVE entry below).

**One testable lesson:** No new hypothesis — p1-driven cut, same category as JUP above.

## ENTRY — AAVE — 2026-08-26 PM

**Frozen 10-parameter table (2026-08-26 PM, reconfirming checkpoint — 3rd consecutive ≥7/10 read):**

| # | Parameter | Value | Label |
|---|---|---|---|
| 1 | Sentiment (contrarian) | Flat interest, capitulation persists ("overvalued", "DAO value extraction"), unverified $52M-extraction claim treated as unverified crowd noise | Bullish |
| 2 | DMA | Price $123.78 vs 50DMA $96.95, 200DMA $96.36 — dev-from-50DMA +27.7%, still past the 25% override line | Bearish |
| 3 | RSI-14 | 65.4 | Bullish |
| 4 | Rvol (7d/30d) | Expansion on upside | Bullish |
| 5 | Volume z-score | -0.18 | Neutral |
| 6 | Funding | 0.01%/8h | Bullish |
| 7 | OI Δ | 7d +32.0%, 24h -4.7% | Bullish |
| 8 | Stablecoin supply | +1.05%/7d | Bullish |
| 9 | MVRV (BTC proxy) | 1.48 | Bullish |
| 10 | Fear & Greed | 65, Δ7d +19 | Neutral |

**Confluence: 7/10 Bullish, 1/10 Bearish.** 3rd consecutive checkpoint ≥7/10 (PM 08-25 armed → AM 08-26 confirmed but bumped by EV tie-break, no open slot → PM 08-26 reconfirmed). JUP and ASTER both stage1-cut this checkpoint on non-confirmation, freeing 2 of the book's 5 slots; AAVE — the only other coin at ≥7/10 this checkpoint besides held MORPHO — takes one.

**Expectancy sheet:**
- Entry: $123.78 (Binance spot, fetched 2026-08-26T19:07:58Z via `parameters.py`)
- Target: $147.9171 (+19.50%)
- Invalidation: $112.1447 (-9.40%) — below both the 50DMA/200DMA cluster
- R = 19.50 / 9.40 = **2.074**
- Stated p = **0.40** (Tier C floor) — nudged up from AM's tie-break-discounted 0.38: dev-from-50DMA eased +32.2% (AM) → +27.7% (PM) as price pulled back -3.5% intraday, a genuine (if modest) reduction in the standing overextension risk that originally justified the discount below the Tier C floor. The overextension flag itself (p2_dma Bearish) has not cleared — still past the 25% line — so p is capped at the floor, not raised further. **Flagged explicitly as a marginal, judgment-driven call in the red-team pass below.**
- EV = 0.40×19.50% − 0.60×9.40% = **+2.16%**
- Tier C (R≥2, p≥0.40)
- Sizing: target 10%, staged half-open this checkpoint = **5% ($493.72 notional, 3.9887 AAVE)**. Second half opens only if confluence holds ≥7/10 at the 2026-08-27 AM checkpoint; no confirmation there cuts the half.

**Runner-up candidates this checkpoint:** none newly reached 7/10 for the first time this PM. TRX (armed at AM 08-26, first occurrence) lapsed to 6/10, did not reconfirm.

**Sector:** DeFi Lending, now 2 of 4 positions (with MORPHO) — at the max 2/5-positions-per-sector cap. Deployed-capital check: DeFi Lending = $1,474.01 of $3,383.26 deployed (43.6%), under the 50%-of-deployed-capital cap.

**Context note:** entered with the book still inside the standing melt-up regime (BTC RSI 79.4, dev-from-50DMA +18.6%, F&G 65 Δ7d+19) — the fourth altcoin in a four-position book with no BTC/cash hedge beyond the ~66% cash buffer. See this checkpoint's pre-mortem for the explicit BTC-dump scenario read against this now-4-position book.

## STAGE-2 ADD — AAVE — 2026-08-27 AM (hard-rule capped)

**Confluence: 7/10 Bullish, 1/10 Bearish.** Held ≥7/10 at the immediate next checkpoint since the PM 08-26 stage-1 half-entry (7/10 → 7/10, held). Mechanical p2-10 unchanged (6/9 Bullish, 1 Bearish — p2_dma stays Bearish, dev-from-50DMA now +29.9%, slightly *more* extended than PM's +27.7%). p1 sentiment flipped Bearish (PM 08-26) → Bullish (AM 08-27): flat interest, zero euphoria, genuine capitulation marker ("quietly exiting aave positions before the next cycle"), no offsetting hype.

**Sector-cap conflict (first of its kind this book):** the standard stage-2 add matches the stage-1 notional ($493.72). Doing so here would have pushed DeFi Lending (MORPHO + AAVE) to ~51.2% of deployed capital — a direct breach of Section 3 rule 8 ("≤50% of deployed capital in one sector," a hard rule, never break, no exceptions). This is distinct from the max-2-positions-per-sector cap, which is satisfied (2/5). Since the confluence gate and staged-entry confirmation rule were both independently satisfied, the choice was between (a) executing the full add and breaching a hard rule, (b) cutting the add entirely despite a genuine reconfirmation, or (c) sizing the add to the largest amount compliant with the sector cap. Chose (c): **$397.00 notional (3.125 AAVE @ $127.04)**, landing DeFi Lending at 49.99% of deployed capital. Position now 7.1137 AAVE, avg entry $125.211915, ~9.04% of portfolio — short of the 10% target size solely because of the sector cap, not a discretionary read on the trade's merit.

**Red-team note:** is capping here just a different way of overriding a confirmed signal? Rebuttal — the confluence/staged-entry rule governs *whether* to add and *how much would normally be added*; the sector cap is a separate, independent hard constraint on total sector concentration that binds regardless of any single trade's merit. Sizing down to comply is not a judgment call on AAVE's thesis (which stayed Intact/Playing Out) — it is mechanical rule compliance, the same category of action as a staged-entry cut, just triggered by a different rule.

**Sector exposure after trade:** DeFi Lending (MORPHO $1,047.35 + AAVE $904.02) = $1,951.37 of $3,905.65 deployed = 49.98%. Book at 4/5 positions, ~39.1% deployed, ~60.9% cash.

## SIGNAL — XRP armed — 2026-08-27 AM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10 at PM 08-26, no prior qualifying read to confirm against). Mechanical p2-10: 6/9 Bullish, 0 Bearish (dev-from-50DMA +24.8%, just under the 25% override line; RSI 69.7 mid-upper band). p1 sentiment read Bullish (contrarian): falling interest, zero euphoria, genuine capitulation markers (long-term-holder frustration, sarcasm about unmet targets, "13 years and still can't hit $4") — fits capitulation-while-thesis-intact cleanly. Needs a 2nd consecutive ≥7/10 checkpoint (PM 08-27) to confirm. One open slot remains in the book (4/5 positions held) if XRP confirms.

## TRIM HALF — ONDO — 2026-08-28 PM (Weakening conviction, discretionary)

Broad market-wide risk-off day: BTC -3.33% 24h, most of the 30-coin watchlist down 3-9%. ONDO price $0.3529 (-4.34% vs AM close $0.3689, -6.76% vs avg entry $0.378529).

**This trim was not triggered by the confluence-count or invalidation rules** (confluence 3/10, 0/10 Bearish — short of both the ≥4/10-Bearish single-checkpoint trim threshold and the exit gate; invalidation $0.34 not breached, ~3.8% headroom remaining). It is a discretionary Weakening-conviction call on two converging signals the raw confluence count masks:

1. **Thesis_test breach:** price is now *below* the current 50DMA ($0.362324, dev -2.6%) for the first time this hold — a direct failure of the entry thesis's own explicitly named test ("price holds above the 50DMA"). Price remains above the 200DMA ($0.319723), so the mechanical p2_dma label reads Neutral (not Bearish) — this masks the structural break rather than flagging it.
2. **OI-pillar reversal:** 7d OI flipped to -9.9% (24h -4.6%), a genuine reversal from the strongly-positive OI-expansion regime (peaked +134% 7d) that was this thesis's core confirmation pillar since entry.

Sentiment (p1) read Neutral — falling interest, no clean crowd-extreme dominance, not a factor in this call.

**Action:** SOLD 1323.3035 ONDO @ $0.3529 = $466.99 proceeds, 2026-08-28T19:12:21Z (Binance spot, same `parameters.py` refresh). Avg entry unchanged $0.378529. Realized P&L on the trimmed half: -$33.91 (-0.665R vs planned R=2.08). Position remains open at half size (1323.3035 ONDO, ~4.77% of portfolio) — flagged for confirmation at the next checkpoint per the capital-velocity/weakening-trim rule (Section 5 step 4).

**Red-team note (see also PM 08-28 checkpoint report):** the 50DMA breach and OI reversal are both consistent with a market-wide BTC-led pullback rather than an ONDO-specific narrative failure (no red-flag news, sentiment shows no despair). If price reclaims the 50DMA and OI re-expands next checkpoint, this trim will read as the conservative call on a broad-market wobble rather than a genuine thesis break. If the breach deepens or persists, the remaining half is the next exit candidate.

**Counterfactual tracked in SHADOW_BOOK.md** at the next refresh: the trimmed half continues as a virtual position for comparison against the hold-full-size counterfactual.

## TRIM HALF — AAVE — 2026-08-28 PM (sector-cap correction, not a thesis call)

Immediately after the ONDO trim above, DeFi Lending sector exposure (MORPHO+AAVE) mechanically breached the ≤50%-of-deployed-capital hard rule (Section 3 rule 8) — not because MORPHO or AAVE changed, but because trimming ONDO shrank total deployed capital while leaving the sector numerator untouched, pushing the ratio to ~56.6%. This is a "never break, no exceptions" rule; correction could not wait for the next checkpoint.

**Why AAVE, not MORPHO:** AAVE carries the lower confluence this checkpoint (5/10 vs MORPHO's 6/10) and was already the position constrained by this same sector rule at entry (`stage2_add_capped`, PM 08-26/AM 08-27) — trimming it further extends the same logic rather than introducing a new judgment. This is explicitly **not** a read that AAVE's thesis is weaker: thesis stays Playing Out, conviction Intact, and AAVE in fact has the healthiest invalidation headroom (~8.7%) and least overextension (dev-from-50DMA +23.8%, back under the 25% line) of any holding this checkpoint.

**Action:** SOLD 3.5568 AAVE @ $121.87 = $433.47 proceeds, 2026-08-28T19:12:21Z (Binance spot, same `parameters.py` refresh). Avg entry unchanged $125.211915. Realized P&L on the trimmed half: -$11.89 (-0.256R vs planned R=2.074). Position now 3.5568 AAVE (~4.42% of portfolio).

**Post-trim sector exposure:** DeFi Lending (MORPHO $963.53 + AAVE $433.47 market value) = 49.84% of deployed capital — back under the cap with a small buffer.

**Lesson candidate for LESSONS.md:** a Weakening-conviction trim on one position can silently push a *different* sector over its hard cap by shrinking the denominator. Worth checking sector-exposure ratios as an explicit step after any trim or exit, not only after adds — flagging for the next monthly review.

## TRIM HALF — XLM — 2026-08-29 AM (Weakening conviction, named thesis-test breach)

Price $0.1776, flat vs PM 08-28 close. **This trim was not triggered by the confluence-count or invalidation rules** (confluence 4/10, 0/10 Bearish; invalidation $0.170 not breached, ~4.3% headroom). It is a discretionary Weakening call on the exact watch item flagged explicitly at the end of the PM 08-28 checkpoint ("XLM now has the least invalidation headroom of any holding — a further leg down without a bounce is the next actionable signal").

1. **Structural compression:** dev-from-50DMA fell to +0.8% — the thinnest cushion of the entire hold (prior low +2.1%) — price is barely holding above the 50DMA ($0.176166), directly threatening the entry thesis's own named test ("price holds above the 50DMA").
2. **RSI exiting its band:** 50.0, the second straight checkpoint out of the 55-70 Bullish band and the lowest print of the hold.
3. **Corroborating OI reversal:** 7d OI -14.3% (24h -4.3%), a sharp swing from the strongly-positive regime that anchored this thesis — flagged with an explicit data-quality caveat, since `state/OI_HISTORY.json` is a self-built, ~10-day rolling window (Section 0 amendment) and a single-checkpoint swing of this size is plausible as a rolling-window edge effect rather than a clean signal. Weighted as corroborating, not the primary trigger — the DMA/RSI structural read carries this decision on its own.

**Action:** SOLD 2643.6411 XLM @ $0.1776 = $469.51 proceeds, 2026-08-29T07:12:00Z (Binance spot, same `parameters.py` refresh). Avg entry unchanged $0.188543. Realized P&L on the trimmed half: -$28.93 (-0.590R vs planned R=2.05). Position remains open at half size (2643.6412 XLM, ~4.79% of portfolio) — flagged for confirmation next checkpoint: a 50DMA breach or continued OI deterioration is the next exit signal.

## FULL EXIT — ONDO — 2026-08-29 AM

**P&L:** -$71.79 combined realized across both tranches (PM 08-28 trim -$33.91/-0.665R + AM 08-29 exit -$37.88/-0.743R) vs. planned Tier C setup (R=2.08, stated p=0.42, EV=+2.79% at entry).

**Thesis verdict:** Broken/Failing, not by news or a Section-2 red flag, but by a clean failure of the entry thesis's own named confirmation metrics. The PM 08-28 trim-half set an explicit standing condition: "if the 50DMA breach and OI reversal persist or deepen, the remaining half is the next exit candidate." Both deepened — the 50DMA breach widened from -2.6% to -3.6%, 7d OI stayed clearly negative (-9.9% → -7.7%, not a re-expansion), RSI fell further (52.4 → 46.8). The condition fired as designed.

**Per-parameter verdict at entry (2026-08-24 AM, confluence 7/10):** p2_dma, p3_rsi, p6_funding, p7_oi, p8_stables, p9_mvrv all read Bullish at entry — RIGHT initially (thesis played out well through 08-25/08-26, price up to $0.3904 at one point, +3.1% above entry). p7_oi (the explicitly named thesis-test pillar) was the parameter that ultimately turned and stayed turned — WRONG in hindsight as the durable signal, though it was correctly read at entry. p1 sentiment oscillated Bullish/Neutral/Bearish across the hold with no lasting directional signal — largely IRRELEVANT to the outcome. p5 volz flagged early (08-25 PM) and was an early, correctly-read warning that preceded the eventual breakdown by three checkpoints.

**p calibration:** stated p=0.42 at entry; outcome was a loss, consistent with p<0.5 pricing in a meaningful chance of failure — no overconfidence flag here.

**Sizing/timing verdict:** staged entry (half-then-half) worked as designed — it capped downside to a $500-notional-equivalent full position rather than a full 10% target size taking the whole loss. The PM 08-28 trim-half correctly de-risked ahead of the full breakdown rather than holding to a full exit in one step.

**Counterfactual vs. runner-ups:** at entry (08-24 AM), ONDO won confirmation outright (only qualifying candidate that checkpoint, no competing runner-up). No forgone alternative to compare against.

**One testable lesson:** when an entry thesis names OI as its explicit confirmation pillar, a 7d OI print flipping negative for 2+ consecutive checkpoints (not just one) after a prior strongly-positive regime is a higher-value trim/exit trigger than the 50DMA break alone — both here and in the TRX precedent (LESSONS.md #1), the OI reversal was the more durable signal, arguably deserving the first trim rather than a secondary confirmation.

## TRIM — MORPHO — 2026-08-29 AM (sector-cap correction, not a thesis call)

Same sector-cap cascade as ONDO/AAVE on 2026-08-28 PM, larger this time: the XLM trim and ONDO full exit (both this same checkpoint, unrelated sectors) shrank total deployed capital, pushing DeFi Lending (MORPHO+AAVE) to ~74.9% of deployed capital. AAVE absorbed the correction first (see below) on lowest-confluence-first logic, but zeroing AAVE alone still left MORPHO's full-target position at ~67.3% of the now-smaller deployed capital — still a breach. MORPHO absorbed the remainder needed to land the sector at ~49%.

**Explicitly not a thesis call:** MORPHO carries the strongest read of any coin scored this checkpoint (confluence 7/10, 0/10 Bearish, p1 flipped contrarian Bullish on genuinely rising interest with zero euphoria — Base USDC dominance, Coinbase routing, Robinhood listing). Thesis stays Playing Out, conviction stays Intact.

**Action:** SOLD 212.4305 MORPHO @ $2.416 = $513.23 proceeds, 2026-08-29T07:12:00Z (Binance spot, same `parameters.py` refresh). Avg entry unchanged $2.485638. Realized P&L on the trimmed tranche: -$14.79 (-0.338R vs planned R=2.07). Position now 186.7117 MORPHO (~4.60% of portfolio).

## FULL EXIT — AAVE — 2026-08-29 AM (sector-cap correction, not a thesis call)

**P&L:** -$21.82 combined realized across both tranches (08-28 PM trim -$11.89/-0.256R + 08-29 AM exit -$9.93/-0.214R) vs. planned Tier C setup (R=2.074, stated p=0.40, EV=+2.16% at entry).

**Why AAVE absorbed first (again):** lower confluence this checkpoint (6/10 vs MORPHO's 7/10) and already twice-constrained by this exact hard rule (`stage2_add_capped` at entry, `trimmed_half_sector_cap` on 08-28 PM) — extends the same precedent rather than introducing new judgment. AAVE's own structure was healthy this checkpoint (dev-from-50DMA back under the 25% line at +23.7%, RSI 62.7) with one flagged exception: 7d OI at -24.9%, the sharpest single-checkpoint OI reversal of any holding this book has recorded — a genuine breach of this thesis's own named "OI keeps expanding" test, so the compliance-driven pick also happens to align with the position carrying the weakest thesis-test signal this checkpoint.

**Per-parameter verdict at entry (2026-08-26 PM, confluence 7/10):** p2_dma read Bearish at entry (overextension, dev +27.7%) and stayed the standing risk flag through most of the hold — a correctly-flagged risk that never resolved into an outright breakdown before the position was closed on compliance grounds, so its ultimate verdict is INCONCLUSIVE (never got to play out either way). p3_rsi, p6_funding, p8_stables, p9_mvrv all Bullish at entry and stayed constructive through the hold — RIGHT. p1 sentiment oscillated across nearly every checkpoint with no durable signal — IRRELEVANT. p7_oi read Neutral at entry and stayed Neutral by the mechanical rubric even as the raw 7d OI number swung to -24.9% by exit — this is the second position this checkpoint (after XLM/ONDO) where the mechanical p7_oi label lagged the raw OI trend; worth flagging for the monthly parameter scorecard.

**Sizing/timing verdict:** the sector-cap-capped stage-2 add (entered below the 10% target at ~9.04%) meant this position was already smaller than a standard full-size hold when the compliance exits hit — the cap constraint reduced this position's realized loss twice, once at entry sizing and once by forcing an earlier partial exit than a pure thesis read alone would have triggered.

**Counterfactual vs. runner-ups:** AAVE won its slot at entry via an EV tie-break among MORPHO/JUP/AAVE/ASTER (all tied at 7/10) — AAVE had the lowest EV of the four (+1.58%) but still qualified for the last open slot after JUP/ASTER cut on non-confirmation. No clean forgone-alternative counterfactual since it was the only remaining qualified candidate at the time.

**One testable lesson:** this is the second consecutive checkpoint where a trim in one sector forced a correction in DeFi Lending specifically (ONDO→AAVE on 08-28 PM, then XLM/ONDO→AAVE+MORPHO on 08-29 AM) — with only 2-3 positions typically held, a 2-position sector is structurally fragile to the 50%-of-deployed-capital cap whenever a position in a *different* sector shrinks. See LESSONS.md evidence note below.

## CONFIRMED ENTRY — JUP — 2026-09-01 AM (Tier C, staged half)

**Frozen 10-parameter table at entry (AM 09-01, confluence 7/10, 0/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Neutral | falling interest, zero euphoria/capitulation — staking-yield/voting/support-ticket chatter, no crowd-extreme read |
| p2 DMA | Bullish | price $0.2208 above 50DMA $0.193854 and 200DMA $0.186077 |
| p3 RSI | Bullish | 58.8, mid-band with room |
| p4 rvol | Bullish | 1.47 (expansion, not compression) |
| p5 volz | Neutral | -0.87 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +13.1%, 24h +3.4% |
| p8 stables | Bullish | +0.43%/7d |
| p9 MVRV | Bullish | BTC 1.48, ETH 1.10 |
| p10 F&G | Neutral | 69, -5/7d |

**Both consecutive checkpoint counts:** PM 08-31 7/10 Bullish (0/10 Bearish, first occurrence — armed) → AM 09-01 7/10 Bullish (0/10 Bearish, second consecutive — confirmed). Mechanical p2-10 held flat at 7/9 Bullish/0 Bearish both checkpoints; p1 held Neutral both checkpoints — this is the first time in the JUP watchlist history this paper phase that a JUP arm has NOT lapsed on a euphoria-driven p1 flip (PM 08-26 stage1-cut on non-confirmation, PM 08-29 arm lapsed at AM 08-30).

**Expectancy sheet:** Entry $0.2208, Target $0.2582 (+16.94%), Invalidation $0.203 (-8.06%, a recent consolidation-support level with the 50DMA $0.193854 as further backstop). R = 2.10. Stated p = 0.42. EV = +2.44%. Tier C (R≥2, p≥0.40) → 5-15% size band; staged half now at 5% of $9,822.04 portfolio = $491.10 notional, 2224.1939 JUP.

**Runner-up candidates this checkpoint:** ETH (7/10, 0/10 Bearish) and PYTH (7/10, 0/10 Bearish) both reached the gate for the first time this checkpoint — armed, not confirmed, awaiting PM 09-01 for their own 2nd consecutive read. Neither competed with JUP for a slot since JUP was the only *confirmed* candidate (3 open slots pre-entry, no anti-churn or EV tie-break needed).

**Sizing/sector context:** DEX sector was empty pre-entry (UNI, CAKE, ASTER, JUP all watchlist DEX names but none held) — no sector-cap constraint. 2/5 positions held pre-entry (XLM, MORPHO) → 3/5 post-entry, 2 slots remain open.

**Red-team note (see PM checkpoint report for full pass):** JUP's confirmation leans on p1 holding Neutral rather than mechanical strengthening (mechanical count was flat at 7/9 both checkpoints) — flagged and accepted as a genuine, not manufactured, sentiment cooldown given the described falling-interest/no-crowd-extreme reads on both fetches, with the staged half-entry capping downside if this reading proves wrong.

## SIGNAL — ETH armed — 2026-09-01 AM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10 with 2/10 Bearish at PM 08-31, no prior qualifying read to confirm against). Mechanical p2-10: 7/9 Bullish, 0 Bearish (DMA golden-cross, RSI 69.3 upper-mid band, OI 7d +21.3%). p1 sentiment flipped Bearish (PM 08-31, dominant one-sided euphoria) → Neutral (AM 09-01, thin/offset euphoria via a genuine two-sided $2000-dip-vs-$4000-target debate). Needs a 2nd consecutive ≥7/10 checkpoint (PM 09-01) to confirm. 2 open slots remain in the book (3/5 positions held post-JUP-entry) if ETH confirms.

## SIGNAL — PYTH armed — 2026-09-01 AM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10 with 1/10 Bearish at PM 08-31, no prior qualifying read to confirm against). Mechanical p2-10: 7/9 Bullish, 0 Bearish (DMA golden-cross, RSI 63.4 mid-band, OI 7d +15.9% — p7_oi flipped Neutral→Bullish vs PM). p1 sentiment held Neutral both checkpoints (flat interest, zero euphoria/capitulation, factual oracle-integration narrative). Needs a 2nd consecutive ≥7/10 checkpoint (PM 09-01) to confirm. 2 open slots remain in the book (3/5 positions held post-JUP-entry) if PYTH confirms.

## FULL EXIT — XLM — 2026-09-02 AM (final tranche, thesis Stalled/Failing)

**P&L:** -$61.43 combined realized across all four tranches (AM 08-29 trim -$28.93/-0.590R + AM 08-31 trim -$15.79/-0.644R + PM 09-01 trim -$8.22/-0.671R + AM 09-02 final exit -$8.49/-0.693R) vs. planned Tier C setup (R=2.05, stated p=0.42, EV=+2.59% at entry). Invalidation ($0.170) was never breached across the entire ~12-day hold — this was a thesis-test/structural-compression exit throughout, not a stop-loss.

**Thesis verdict:** Stalled → Failing, via the exact mechanism named at the first trim (AM 08-29): a "named thesis-test breach" (dev-from-50DMA compression + RSI exiting its 55-70 band + a deteriorating OI trend), recurring three more times (AM 08-31, PM 09-01, and finally this exit) each time deepening rather than resolving. The PM 09-01 red-team explicitly pre-committed the exit criterion for this checkpoint ("a further RSI/dev/OI deterioration or an outright 50DMA breach at AM 09-02 would be treated as the exit signal for the remaining eighth, not a fourth trim") and it fired as designed: no metric reclaimed (RSI and dev-from-50DMA both printed fresh hold-lows, 24h OI worsened, 7d OI stayed deeply negative for a fourth straight checkpoint at -21.4%).

**Per-parameter verdict at entry (2026-08-21 AM, confluence 7/10, 1/10 Bearish):**
- p2 DMA: Bullish at entry — WRONG as a durable signal. The golden-cross structure never technically broke (p2 stayed mechanically Bullish/Neutral through the entire hold, even at the final exit), but the raw dev-from-50DMA metric it's built on compressed from +5.8% at entry to +0.1% at exit — the single clearest advance warning of the breakdown, just below the mechanical rubric's threshold to flip the label itself.
- p3 RSI: Bullish at entry (67.4, mid-band) — WRONG as a durable signal. RSI never recovered the 55-70 band after 2026-08-28 and printed five consecutive sub-55 checkpoints into the exit, exactly the named thesis_test condition ("RSI stays out of overbought... as price extends") failing in the opposite direction the thesis didn't anticipate (a slow bleed, not a spike).
- p7 OI: Bullish at entry (+1.5%/24h, +8.3%/7d) — RIGHT initially (OI expansion peaked at +142.5%/7d on 08-23, the strongest confirmation of the whole hold), then WRONG as a durable signal — reversed to persistently negative from PM 08-31 onward (four straight negative-7d checkpoints into the exit), the second-clearest advance warning after p2/p3, and the one explicitly named in the entry thesis_test ("OI keeps expanding alongside price, not diverging").
- p4 rvol, p6 funding, p8 stables, p9 MVRV: Bullish at entry and never flagged Bearish for more than a checkpoint at a time — IRRELEVANT to the outcome, neither confirming nor warning.
- p1 sentiment: Bearish at entry (euphoria, no capitulation offset) and oscillated Bullish/Neutral/Bearish on nearly every subsequent checkpoint with no lasting directional signal — IRRELEVANT, consistent with every other post-mortem this phase; sentiment never drove a single trim or the final exit decision.
- p10 F&G: Neutral at entry — IRRELEVANT, a market-wide overlay that never became the deciding factor for this coin-specific breakdown.

**p calibration:** stated p=0.42 at entry, reflecting the contrarian-Bearish sentiment flag and a market-wide overheated F&G reading; outcome was a loss. Consistent with p<0.5 pricing in a meaningful chance of failure — no overconfidence flag. Worth noting for the calibration audit: this is now the second Tier C XLM-style entry (alongside TRX, ONDO) where the position round-tripped through multiple discretionary trims before a final exit rather than resolving cleanly one way or the other — the staged-trim mechanic works as a capital-preservation tool, but three trims consuming three separate checkpoints' worth of judgment calls on the same recurring pattern is a lot of process for a position that only ever traded in a roughly ±13% band around entry.

**Sizing/timing verdict:** the staged-trim ladder (half → quarter → eighth → exit) worked exactly as designed — total realized loss (-$61.43, roughly -0.66R blended) is far smaller than a single full-size stop-out at invalidation would have been (a full 10% target position hitting the -9.28% invalidation would have cost roughly -$93 on the eventual $9,823 base, without the multiple opportunities this ladder had to be cut earlier on genuinely deepening signals). Each individual trim was arguably late relative to its own triggering data (the pattern recurred three times before finally being acted on decisively), but each was also small — the position was already down to an eighth of target by the time this final exit fired, capping the cost of that lateness.

**Counterfactual vs. runner-ups:** at entry (2026-08-21 AM), XLM was the only coin to reach confirmation that checkpoint (FIL and PEPE both lapsed from PM 08-20 arms without confirming) — no forgone alternative to compare against at entry. Over the hold, JUP and MORPHO (both entered later, both still open and both net positive or flat) represent the opportunity cost of the capital tied up in XLM's repeated trims, though the staged-sizing meant that capital was mostly freed back to cash rather than locked in.

**One testable lesson:** a named thesis-test breach that resolves via partial reclaim twice (AM 08-29→PM 08-29, AM 08-31→PM 08-31) before recurring a third time and failing to reclaim at all (PM 09-01→AM 09-02) suggests the reclaim bar itself was too easy to clear on the first two passes — both "successful" reclaims left RSI still under 55 (51.3 and 51.0 respectively), never actually satisfying the thesis's own named condition, just moving further from the day's worst print. Proposed refinement for LESSONS.md: a genuine reclaim confirmation should require the named thesis-test metric to *fully* clear its stated band (e.g. RSI back above 55, not merely off its low), not just improve directionally — otherwise the trim ladder keeps resetting on partial credit and the position round-trips through avoidable extra checkpoints before the pattern is finally treated as decisive.

## CONFIRMED ENTRY — ETH — 2026-09-04 PM (Tier C, staged half)

**Frozen 10-parameter table at entry (PM 09-04, confluence 8/10, 0/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Bullish (contrarian) | zero euphoria markers; despair-flavored capitulation stack (sentiment scores dipping negative, "narrative exhaustion," bearish smart-money read, "struggling around $2.4K with limited upside") |
| p2 DMA | Bullish | price $2454.07 above 50DMA $2078.25 and 200DMA $2034.63, golden cross |
| p3 RSI | Bullish | 62.5, mid-band with room |
| p4 rvol | Bullish | 0.66 (compression setup) |
| p5 volz | Neutral | 0.70 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +20.4%, 24h -3.5% (single-day dip on a strong weekly print) |
| p8 stables | Bullish | +0.37%/7d |
| p9 MVRV | Bullish | BTC 1.53, ETH 1.11 |
| p10 F&G | Neutral | 74, +1/7d |

**Both consecutive checkpoint counts:** AM 09-04 7/10 Bullish (0/10 Bearish, first occurrence — armed) → PM 09-04 8/10 Bullish (0/10 Bearish, second consecutive — confirmed, strengthened not just held). Mechanical p2-10 improved 7/9 → 8/9 Bullish between the two checkpoints (p4_rvol flipped Neutral→Bullish on the rv_ratio compressing to 0.66); p1 flipped Neutral (AM) → Bullish/contrarian (PM) as the sentiment read shifted from a genuinely mixed stack to a clean capitulation-without-euphoria one. This is the cleanest confirmed-candidate read of the paper phase to date (no prior confirmed entry — MORPHO, JUP, ONDO, AAVE — reached 8/10 with 0 Bearish at confirmation).

**Expectancy sheet:** Entry $2454.07, Target $2900.00 (+18.17%), Invalidation $2249.00 (-8.36%, a recent consolidation/breakout-support level with the 50DMA $2078.25 as further backstop). R = 2.17. Stated p = 0.43 (modestly above the book's typical 0.40-0.42 Tier C baseline, reflecting the unusually clean 8/10-with-zero-Bearish confirmation). EV = +3.05%. Tier C (R≥2, p≥0.40, R<2.5 keeps it out of Tier B) → 5-15% size band, target 10%; staged half now at 5% of $9,816.66 portfolio = $490.814 notional, 0.2000 ETH.

**Runner-up candidates this checkpoint:** LINK (7/10, 1/10 Bearish) and SOL (7/10, 0/10 Bearish) both reached the gate for the first time this checkpoint — armed, not confirmed, awaiting AM 09-05 for their own 2nd consecutive read. Neither competed with ETH for a slot since ETH was the only *confirmed* candidate (2 open slots pre-entry, no anti-churn or EV tie-break needed). ETHFI and NEAR (both armed AM 09-04 at 7/10) lapsed this checkpoint, falling to 6/10 each on p1 sentiment flips to clean euphoria-dominant Bearish reads with no capitulation offset.

**Sizing/sector context:** Major L1 sector was empty pre-entry (BTC, ETH, SOL, TRX, ADA all watchlist Major L1 names but none held) — no sector-cap constraint. 2/5 positions held pre-entry (MORPHO, JUP) → 3/5 post-entry, 2 slots remain open. Post-entry sector split: DeFi Lending ~32%, DEX ~32%, Major L1 ~36% of deployed capital — three single-position sectors, each comfortably under the 50% cap, a materially more balanced structure than the two-sector 50/50 split that produced six consecutive drift-only sector-cap trims (LESSONS.md #11) since 2026-08-27.

**Red-team note (see PM checkpoint report for full pass):** ETH is already the market's most closely-watched large-cap, and an 8/10-with-zero-Bearish read invites the "too good to be real" question — but every individual parameter is independently clean (moderate not extreme dev-from-50DMA, RSI mid-band not overbought, OI confirming both windows, funding flat) and the p1 read is a genuine capitulation stack (zero euphoria markers), not a forced contrarian call. Staged half-entry caps downside if the read proves overextended.

## SIGNAL — LINK armed — 2026-09-04 PM (first occurrence)

Confluence 7/10 Bullish, 1/10 Bearish — first occurrence this checkpoint (was 6/10 at AM 09-04, no prior qualifying read to confirm against). Mechanical p2-10: 6/9 Bullish, 0 Bearish (DMA golden-cross, RSI mid-band, OI confirming). p1 sentiment read Bearish this checkpoint — dominant euphoria ($50-100 2027-29 targets, rocket-emoji $12/$15.5/$20 calls, institutional-onboarding hype), zero capitulation offset, contrarian Bearish despite the genuine underlying utility narrative. Needs a 2nd consecutive ≥7/10 checkpoint (AM 09-05) to confirm. 2 open slots remain in the book (3/5 positions held post-ETH-entry) if LINK confirms.

## SIGNAL — SOL armed — 2026-09-04 PM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10 at AM 09-04, no prior qualifying read to confirm against). Mechanical p2-10: 6/9 Bullish, 0 Bearish (DMA golden-cross, RSI mid-band, OI confirming on the 24h window though p7_oi itself reads Neutral on a mixed cross-window read). p1 sentiment read Bullish (contrarian) this checkpoint — zero euphoria markers, despair-flavored capitulation language ("fucked right now, nobody believes in anything longer than dumping on someone," treated "like a casino chip"), zero euphoria offset. Needs a 2nd consecutive ≥7/10 checkpoint (AM 09-05) to confirm. 2 open slots remain in the book (3/5 positions held post-ETH-entry) if SOL confirms.

## SIGNAL — ETHFI lapsed — 2026-09-04 PM

Armed at AM 09-04 (7/10, 2/10 Bearish, first occurrence) — did not hold at PM 09-04, easing to 6/10 (1/10 Bearish, mechanical p4_rvol flipped Bullish→Neutral) with p1 sentiment holding Bearish (strong euphoria — "10X potential," "sky is the limit" — narrowly outweighing thin capitulation counter-signals: a single closed-long mention, an unverified fraud accusation). Arm lapses per Section 5 step 5; a fresh arm would need to restart from a new first-occurrence ≥7/10 read.

## SIGNAL — NEAR lapsed — 2026-09-04 PM

Armed at AM 09-04 (7/10, 0/10 Bearish, first occurrence) — did not hold at PM 09-04, easing to 6/10 (1/10 Bearish) as p6_funding flipped Bullish→Neutral and p1 sentiment flipped Neutral→Bearish (clean euphoria — $10 targets, "gonna pump more during weekend" — with zero capitulation offset this checkpoint, unlike AM's mixed foundation-dumping-complaint read). Arm lapses per Section 5 step 5; a fresh arm would need to restart from a new first-occurrence ≥7/10 read.

## CONFIRMED ENTRY — LINK — 2026-09-05 AM (Tier C, staged half)

**Frozen 10-parameter table at entry (AM 09-05, confluence 7/10, 1/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Bearish (contrarian) | euphoria dominant: rocket emojis, $12-14.34 price-target chasing, "pomp it," "biblical pump," "parabolic"; zero capitulation offset |
| p2 DMA | Bullish | price $11.728 above 50DMA $9.592 and 200DMA $8.9945, golden cross |
| p3 RSI | Bullish | 64.6, mid-band with room |
| p4 rvol | Bullish | 0.78 (compression, setup intact) |
| p5 volz | Neutral | -1.21 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +14.6%, 24h -2.0% (mild single-day dip on a strong weekly print) |
| p8 stables | Bullish | +0.36%/7d |
| p9 MVRV | Bullish | BTC 1.50, ETH 1.09 |
| p10 F&G | Neutral | 73, +5/7d |

**Both consecutive checkpoint counts:** PM 09-04 7/10 Bullish (1/10 Bearish, first occurrence — armed) → AM 09-05 7/10 Bullish (1/10 Bearish, second consecutive — confirmed, held exactly steady on the same sole Bearish parameter, p1). Mechanical p2-10 unchanged (6/9 Bullish both checkpoints). This is the book's third confirmed entry this week (after MORPHO/JUP earlier and ETH PM 09-04), and the first to confirm at a flat (not strengthened) read.

**Expectancy sheet:** Entry $11.728, Target $13.80 (+17.7%, set deliberately below the $14.34 social-media hype level flagged in the p1 fade — the thesis is not borrowing its target from the euphoria being contrarian-faded), Invalidation $10.75 (-8.3%, a support level above the 50DMA $9.592). R = 2.12. Stated p = 0.42 (standard Tier C baseline, consistent with a confirmed candidate carrying a single Bearish sentiment flag). EV = +2.58%. Tier C (R≥2, p≥0.40; confluence 7/10 keeps it out of Tier A regardless of R) → 5-15% size band, target 10%; staged half now at 5% of $9,813.3137 portfolio = $490.6657 notional, 41.837115 LINK.

**Runner-up candidates this checkpoint:** SOL, armed alongside LINK at PM 09-04 (7/10, 0/10 Bearish), lapsed this checkpoint — eased to 6/10 as p7_oi rolled Bullish→Neutral (OI turned mildly negative both windows) and p1 flipped Neutral-leaning-Bullish→Bearish (rising interest, meme-profit-call euphoria, zero capitulation offset). No EV tie-break was needed — LINK was the sole confirmed candidate.

**Sizing/sector context:** Oracle sector was empty pre-entry — no cap constraint. 2/5 positions held pre-entry (MORPHO, JUP, after ETH's stage-1 cut this same checkpoint freed a slot) → 3/5 post-entry, 2 slots remain open. Post-entry sector split: DeFi Lending ~32.0%, DEX ~32.1%, Oracle ~35.8% of deployed capital (~14.0% of portfolio, 86.0% cash) — mirrors the three-single-position-sector structure the book held briefly with ETH before its cut.

**Red-team note (see AM checkpoint report for full pass):** LINK's confluence held exactly flat (7/10 both checkpoints) rather than strengthening, and dev-from-50DMA at +22.3% is the second-most-extended of the three current holdings (behind ETH's former +17.4%... actually ahead of it) — worth watching for overextension, though still under the 25% override line. The p1 Bearish flag (euphoria) is the sole drag on an otherwise clean 6/9 mechanical board, consistent with how every other genuinely euphoric name has been read this week (ADA, ARB, CAKE, ETHFI, HBAR, JUP, SOL) — not a forced override, a real crowd-extreme signal being faded as designed.

## EXIT POST-MORTEM — ETH (stage-1 half) — 2026-09-05 AM

**P&L:** +$0.098 realized (+0.0024R vs planned R=2.17) on the 0.2000 ETH stage-1 half, bought PM 09-04 at $2454.07, sold AM 09-05 at $2454.56 (+0.02% price move over one checkpoint). Essentially a flat round-trip — this was a rule-mechanic exit, not a losing thesis call, and not a stop-loss (invalidation $2249.00 was never remotely close).

**Thesis verdict:** Playing Out / Intact, right up to the cut — this was not a thesis failure. The position was closed purely because Section 5 step 9's staged-entry confirmation mechanic requires confluence to hold ≥7/10 at the immediate next checkpoint to add the second half; ETH's confluence eased 8/10 (entry, 0 Bearish) → 6/10 (this checkpoint, 1 Bearish), two full parameters short. No confirmation → cut the half, per the rule as written. This is now the eighth instance of a staged-entry non-confirmation cut this paper phase (TRX-adjacent precedent aside: CAKE, ETH×2 [this is the second ETH cut of the phase, a different hold than the 08-19 one], ZEC, MORPHO-early, UNI, JUP-early, ASTER all preceded it).

**Per-parameter verdict at entry (2026-09-04 PM, confluence 8/10, 0/10 Bearish) vs. this checkpoint's cut:**
- p1 sentiment: Bullish (contrarian capitulation) at entry → Neutral this checkpoint. The despair-flavored stack that justified entry (sentiment scores dipping negative, "narrative exhaustion") did not persist — this checkpoint's fetch showed flat/mixed sentiment (6.0/10 scores, 81/19 bull/bear split) with zero clean euphoria or capitulation markers. Genuine data change, not a misread either time — sentiment is inherently noisy checkpoint-to-checkpoint and this is exactly the kind of parameter the book's own LESSONS.md (#2, #9) flags as prone to false-negative-driving rollovers.
- p7 OI: Bullish (7d +20.4%, mild 24h dip) at entry → Bearish this checkpoint (24h -3.0%, 7d +19.6% — the 7d print is still strongly positive, but the mechanical rubric reads the mixed cross-window combination as Bearish). This is the named thesis-test's own pillar ("OI keeps expanding alongside price, not diverging") and the parameter LESSONS.md's Section-3 parameter scorecard flags as the highest-variance, most consequential single point of failure in the rubric.
- p2 DMA, p3 RSI, p4 rvol, p6 funding, p8 stables, p9 MVRV: all stayed Bullish, unchanged — the structural/technical legs of the thesis never wavered. Price itself was essentially flat (+0.02%), not down.
- p5 volz, p10 F&G: Neutral at both checkpoints — irrelevant to the confluence swing either way.

**p calibration:** stated p=0.43 at entry; outcome was a flat round-trip, not a resolved bet either way (the staged-entry mechanic intervened before the probabilistic call was ever tested) — consistent with essentially every other closed leg this paper phase per the 2026-09-01 monthly review's calibration-audit finding (zero legs have yet reached target or invalidation).

**Sizing/timing verdict:** the staged half-entry worked exactly as designed — capping exposure to 5% rather than the full 10% target meant a non-confirmation cost nothing beyond a flat round-trip trade, rather than exposing a full-size position to a two-parameter confluence swing driven mostly by mean-reverting/regime-adjacent readings (p1, p7) rather than a price breakdown.

**Counterfactual vs. runner-ups:** LINK confirmed this same checkpoint (7/10, 1/10 Bearish, held steady) and took the freed slot with its own staged half — no capital sat idle as a result of ETH's cut. SOL, ETH's other PM 09-04 cohort-mate, also failed to confirm (lapsed from its own 7/10 arm) — a broader pattern this checkpoint of PM 09-04's three ≥7/10 reads (ETH confirmed+cut, LINK armed+confirmed, SOL armed+lapsed) resolving 1-for-3 by AM 09-05, worth watching as a shadow-book comparison point (ETH's virtual continuation vs. its actual flat cut) at the next Monday refresh.

**One testable lesson (continuing evidence, not a new hypothesis):** this is a second, independent data point for the already-logged LESSONS.md Proposal 1 ("soft non-confirmation" when only mean-reverting/regime-overlay parameters roll over while price/OI hold) — except this case cuts *against* a blanket adoption of that proposal, since here p7 OI (one of the two parameters the proposal explicitly treats as thesis-defining, alongside price) was itself one of the two parameters that rolled over, not just p1/p3/p4/p6/p10. A future monthly review should track whether "soft non-confirmation" cases that include an OI rollover perform differently from ones that don't, before extending Proposal 1 to cover this pattern.

## SIGNAL — SOL lapsed — 2026-09-05 AM

Armed at PM 09-04 (7/10, 0/10 Bearish, first occurrence) — did not hold at AM 09-05, easing to 6/10 (1/10 Bearish) as p7_oi flipped Bullish→Neutral (OI turned mildly negative both windows, 24h -2.4%/7d -2.6%) and p1 sentiment flipped from a mixed/Bullish-leaning read to Bearish (rising interest, clean meme-profit-call euphoria — 5.5x/28x gain bragging — zero capitulation offset). Arm lapses per Section 5 step 5; a fresh arm would need to restart from a new first-occurrence ≥7/10 read.

## EXIT POST-MORTEM — LINK (stage-1 half) — 2026-09-05 PM

**P&L:** +$11.9236 realized (+0.2914R vs planned R=2.12) on the 41.837115 LINK stage-1 half, bought AM 09-05 at $11.728, sold PM 09-05 at $12.013 (+2.43% price move over one checkpoint). A modest gain, not a losing thesis call — the position ran in the right direction but the staged-entry confirmation mechanic still intervened because the very move that made money also flipped the DMA overextension check.

**Thesis verdict:** Playing Out / Intact, right up to the cut — not a thesis failure. Section 5 step 9 requires confluence to hold ≥7/10 at the immediate next checkpoint to add the second half; LINK's confluence eased 7/10 (entry, 1 Bearish) → 5/10 (this checkpoint, 1 Bearish), two full parameters short. No confirmation → cut the half, per the rule as written.

**Per-parameter verdict at entry (2026-09-05 AM, confluence 7/10, 1/10 Bearish) vs. this checkpoint's cut:**
- p2 DMA: Bullish at entry (dev-from-50DMA +22.3%) → Bearish this checkpoint (dev crossed to +25.2%, just over the rubric's own 25% overextension override line). The price gain that would normally read as thesis-confirming instead tripped the rubric's overextension check — a genuine mechanical flip, not a misread, but a reminder that a fast, favorable move can itself be what kills a staged-entry confirmation.
- p1 sentiment: Bearish (contrarian, euphoria dominant) at entry → Neutral this checkpoint. The rocket-emoji/"biblical pump"/"parabolic" $12-14.34 price-target stack that justified the entry's one caution flag cleared to thin, low-engagement chatter (Robinhood-leaderboard vote, generic trend-list mention) — a genuine cooldown, not a forced read either time.
- p3 RSI, p6 funding, p7 OI, p8 stables, p9 MVRV: all stayed Bullish, unchanged — OI in particular strengthened (7d +14.6%→+20.2%, 24h -2.0%→+5.5%), directly confirming rather than contradicting the thesis test.
- p4 rvol, p5 volz, p10 F&G: Neutral at both checkpoints — irrelevant to the confluence swing.

**p calibration:** stated p=0.42 at entry; outcome was a flat-to-modest-gain round-trip, not a resolved bet either way (the staged-entry mechanic intervened before target or invalidation were ever tested) — consistent with every other closed leg this paper phase.

**Sizing/timing verdict:** the staged half-entry worked as designed — a full-size position would have been sitting on the same overextension flag with 10% exposure instead of 5%, for no difference in outcome given the position is being closed rather than trimmed.

**Counterfactual vs. runner-ups:** LINK was the sole confirmed candidate at its own entry (AM 09-05); no runner-up was displaced. This checkpoint (PM 09-05), BNB and ETH both newly armed at ≥7/10 (first occurrence each) — LINK's freed slot and cash sit available for either to confirm at AM 09-06.

**One testable lesson:** a price move favorable enough to trip the p2_dma overextension override (25%) within a single checkpoint of a staged half-entry is a distinct non-confirmation pattern from the "sentiment/regime-only rollover" cases LESSONS.md Proposal 1 addresses — here the move that hurt confirmation was fundamentally bullish (price up 2.4%), not bearish. Worth tracking separately: does a "cut on its own overextension" case tend to re-arm quickly (since price/OI/RSI all stayed constructive), unlike a genuine deterioration cut?

## SIGNAL — BNB armed — 2026-09-05 PM (first occurrence)

Confluence 7/10 Bullish, 1/10 Bearish — first occurrence this checkpoint (mechanical count was <5 at AM 09-05, not fetched for sentiment; jumped to 7/9 mechanical Bullish this checkpoint on a strong Axiom-launch-driven session, 24h +7.4%/7d +11.9%, OI confirming sharply both windows +41.9%/+43.5%). Sole Bearish flag is p3_rsi (79.4, overheated, over the 75 threshold) — a real overextension caution on an otherwise clean board (dev-from-50DMA 23.6%, still under the 25% override line). p1 sentiment read Neutral — flat interest, Axiom-platform-launch excitement without a clean price-target euphoria stack, no capitulation offset either. Needs a 2nd consecutive ≥7/10 checkpoint (AM 09-06) to confirm. 3 open slots remain in the book (2/5 positions held after LINK's cut this checkpoint) if BNB confirms.

## SIGNAL — ETH armed — 2026-09-05 PM (first occurrence, fresh sequence)

Confluence 8/10 Bullish, 0/10 Bearish — first occurrence of a fresh arming sequence (ETH's prior confirmed position was fully closed at AM 09-05 on a staged-entry non-confirmation, breaking the earlier chain; this is a new first-occurrence read, not a continuation). Mechanical p2-10: 7/9 Bullish, 0 Bearish — golden-cross clean (dev-from-50DMA 18.5%, RSI 63.8 mid-band, OI confirming both windows, funding flat). p1 sentiment read Bullish (contrarian) — falling interest, a genuine capitulation stack ("momentum dead at $2418," "could dump to $2200," negative-ETF-flow framing), zero euphoria offset, against a mechanically clean structure — the same capitulation-with-intact-structure pattern that produced ETH's prior 8/10 confirmed entry three checkpoints ago. Needs a 2nd consecutive ≥7/10 checkpoint (AM 09-06) to confirm as a fresh sequence. 3 open slots remain in the book (2/5 positions held after LINK's cut this checkpoint) if ETH confirms.

## ENTRY SNAPSHOT — ETH — 2026-09-06 AM

**Frozen 10-parameter table (confluence 7/10 Bullish, 0/10 Bearish):**

| # | Parameter | Label | Reading |
|---|---|---|---|
| p1 | Social sentiment (contrarian) | Neutral | Flat interest, zero euphoria/capitulation markers — dominant narrative purely factual (wave-4 consolidation holding the $2355 low, $226M ETF inflows, institutional targeting). Cooled from PM 09-05's genuine capitulation stack ("momentum dead at $2418," "could dump to $2200") that produced the arm. |
| p2 | Price vs 50/200DMA | Bullish | $2507.31 above 50DMA ($2103.9476) and 200DMA ($2039.8348), golden-cross, dev-from-50DMA +19.2% (moderate, well under the 25% override). |
| p3 | RSI-14 | Bullish | 65.4, mid-upper band with room. |
| p4 | Realized vol ratio (7d/30d) | Bullish | 0.63 — compression, setup read. |
| p5 | Volume z-score | Neutral | -1.05. |
| p6 | Funding rate | Bullish | 0.01%/8h — near-zero, no crowded-long risk. |
| p7 | Open interest Δ | Bullish | 24h +2.9%, 7d +16.6% — OI confirming alongside price on both windows. |
| p8 | Stablecoin supply 7d Δ | Bullish | Global block, +0.6%. |
| p9 | MVRV (BTC proxy) | Bullish | BTC 1.5, ETH 1.1 — healthy 1-2 band. |
| p10 | Fear & Greed | Neutral | 73, Δ7d +4 — constructive but not the >75/falling-fast Bearish band nor the <25/rising-from-<30 Bullish band. |

**Two-consecutive-checkpoint confirmation:** PM 09-05 8/10 Bullish (0/10 Bearish, armed, first occurrence of this fresh sequence) → AM 09-06 7/10 Bullish (0/10 Bearish, confirmed). Both checkpoints cleared the ≥7/10 gate with zero Bearish flags.

**Expectancy sheet:** Entry $2507.31 | Target $2900.00 | Invalidation $2355.00 (sentiment-sourced wave-4 consolidation low) | R = (2900-2507.31)/(2507.31-2355) = **2.58** | p = 0.43 | upside 15.66% | downside 6.07% | EV = 0.43×15.66% - 0.57×6.07% = **+3.27%**. Floor (R≥2.0, EV>0) cleared comfortably; R≥2.5 clears the Tier B R-threshold but p=0.43 falls short of Tier B's p≥0.45 floor, so this is **Tier C** (R≥2, p≥0.40) — target size 10%, staged half now.

**Runner-ups this checkpoint:** ETHFI newly armed 7/10 Bullish (2/10 Bearish, first occurrence) on rising interest + dominant euphoria ("10x potential," "sky is the limit") — needs PM 09-06 to confirm, not yet competing for a slot. BNB, armed at PM 09-05 (7/10, 1 Bearish), **lapsed** to 5/10 this checkpoint (p4_rvol and p5_volz both rolled Bullish→Neutral) — did not reach a second consecutive confirmation. No anti-churn conflict: 2/5 positions held pre-entry (MORPHO, JUP, both single-position sectors), 3/5 post-entry, ample room without displacing anything.

**Staged entry:** BUY 0.196942 ETH @ $2507.31 = $493.7946 notional (5.0% of $9,875.8703 portfolio), 2026-09-06T07:12:00Z (Binance spot, same `parameters.py` refresh used for this checkpoint). Second half adds only if confluence holds ≥7/10 at the 2026-09-06 PM checkpoint; no confirmation cuts the half (per the standing Section 5 step 9 mechanic — LESSONS.md Proposal 1's "soft non-confirmation" relaxation remains unadopted pending explicit user sign-off).

## SIGNAL — ETHFI armed — 2026-09-06 AM (first occurrence)

Confluence 7/10 Bullish, 2/10 Bearish — first occurrence (PM 09-05 was 6/10, none). Mechanical p2-10 improved to 7/9 Bullish (p4_rvol flipped Neutral→Bullish), 1/9 Bearish (p5_volz). p1 sentiment read Bearish (contrarian) — rising interest, dominant euphoria ("10x potential," "sky is the limit," "strongest communities"), zero capitulation offset — the same recurring euphoria-driven pattern that has repeatedly capped ETHFI's confluence this phase (see AM/PM 09-04, AM 09-05 status history). Needs a 2nd consecutive ≥7/10 checkpoint (PM 09-06) to confirm. 2 open slots remain in the book (3/5 positions held after ETH's entry this checkpoint) if ETHFI confirms.

## SIGNAL — BNB lapsed — 2026-09-06 AM

Armed at PM 09-05 (7/10, 1/10 Bearish, first occurrence) — did not hold at AM 09-06, easing to 5/10 (1/10 Bearish) as p4_rvol and p5_volz both rolled Bullish→Neutral (RSI stays overheated at 75.6, p3_rsi still the standing Bearish flag). p1 sentiment stayed Neutral both checkpoints — hype-flavored narrative (BNB V2/"BSC super cycle") without a clean price-target euphoria stack, this checkpoint additionally offset by a genuine leverage-trap/OI-divergence caution. Arm lapses per Section 5 step 5; a fresh arm would need to restart from a new first-occurrence ≥7/10 read.

## STAGE-2 ADD — ETH — 2026-09-06 PM

Confluence held **8/10 Bullish, 0/10 Bearish** at this checkpoint (second consecutive checkpoint since the AM 09-06 half-open confirmation, strengthened from 7/10) — per Section 5 step 9, the second half opens at full target size, no confirmation needed beyond the hold itself.

Mechanical parameters unchanged in shape from AM (DMA golden-state, dev-from-50DMA +18.5% moderate, RSI 64.7 mid-band, funding flat, OI confirming both windows, stables/MVRV healthy); p1 sentiment flipped Neutral (AM) → Bullish/contrarian (PM) as capitulation-flavored bearish trader chatter appeared (double-top calls, "bears gaining control," low single-digit sentiment scores) with zero euphoria offset — read as capitulation while the thesis stays Playing Out/Intact, not a deteriorating narrative.

**Fill:** BUY 0.198078 ETH @ $2492.93 = $493.7946 notional (matching the stage-1 half's original ~$493.79 sizing), 2026-09-06T19:10:00Z (Binance spot via `parameters.py` refresh). Position now 0.395020 ETH, avg entry $2500.099323, ~9.92% of portfolio ($987.59 / $9,929.34) — full target size reached. No further staging; ongoing test is the same OI/price/RSI/DMA structure through the 2026-09-20 interim review.

## CONFIRMED ENTRY — ETHFI — 2026-09-06 PM (Tier C, staged half)

**Frozen 10-parameter table at entry (PM 09-06, confluence 7/10, 1/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Bearish (contrarian) | rising interest, euphoria dominant (whale-attention alerts, rocket emojis, breakout-momentum hype, "+87% spot almost 2x, patience paying off"), zero capitulation offset |
| p2 DMA | Bullish | price $0.5722 above 50DMA $0.476054 and 200DMA $0.441853, golden cross |
| p3 RSI | Bullish | 57.7, mid-band with room |
| p4 rvol | Bullish | 0.76 (mild compression) |
| p5 volz | Neutral | -0.59 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +23.7%, 24h +0.6% |
| p8 stables | Bullish | +0.6%/7d |
| p9 MVRV | Bullish | BTC 1.50, ETH 1.10 |
| p10 F&G | Neutral | 73, +4/7d |

**Both consecutive checkpoint counts:** AM 09-06 7/10 Bullish (2/10 Bearish, first occurrence — armed) → PM 09-06 7/10 Bullish (1/10 Bearish, second consecutive — confirmed). Mechanical p2-10 held clean 7/9 Bullish, 0/9 Bearish both checkpoints; p1 held Bearish both checkpoints on the same recurring euphoria-driven pattern that has capped ETHFI's confluence repeatedly this phase (AM/PM 09-04, AM 09-05) — this is the first time the p1 read has NOT prevented a confirmation, because mechanical p2-10 alone already clears 7/9.

**Expectancy sheet:** Entry $0.5722, Target $0.68 (+18.84%), Invalidation $0.52 (-9.12%, a recent consolidation-support level with the 50DMA $0.476054 as further backstop). R = 2.07. Stated p = 0.41. EV = +2.34%. Tier C (R≥2, p≥0.40, R<2.5 keeps it out of Tier B) → 5-15% size band, target 10%; staged half now at 5% of $9,929.3401 portfolio = $496.467 notional, 867.6459 ETHFI.

**Runner-up candidates this checkpoint:** ONDO (7/10, 0/10 Bearish) reached the gate for the first time this checkpoint — armed, not confirmed, awaiting AM 09-07 for its own 2nd consecutive read. Did not compete with ETHFI for a slot since ETHFI was the only *confirmed* candidate (1 open slot pre-entry, no anti-churn or EV tie-break needed).

**Sizing/sector context:** Liquid Staking sector was empty pre-entry — no sector-cap constraint. 3/5 positions held pre-entry (MORPHO, JUP, ETH) → 4/5 post-entry, 1 slot remains open. Post-entry sector split (of deployed capital): DeFi Lending ~18.3%, DEX ~21.6%, Major L1 ~40.0%, Liquid Staking ~20.2% — four single-position sectors, each comfortably under the 50% cap.

**Red-team note (see PM checkpoint report for full pass):** ETHFI's p1 read has been the recurring reason this ticker's arms lapsed three times already this phase (AM 09-04, and two earlier cycles) — is a 7/9-mechanical-clean confirmation with a *known* euphoria-driven p1 flag different from those prior failures, or just the same pattern finally clearing on a technicality? Mechanical p2-10 is genuinely stronger this time (7/9 Bullish both checkpoints vs. 6/9 or weaker on the prior lapses), and the entry gate is a confluence-count test, not a "p1 must agree" test — a Bearish p1 costs nothing against the bullish count as designed. Staged half-entry caps downside if the euphoria proves to be the leading edge of a blow-off rather than sustainable momentum.

## SIGNAL — ONDO armed — 2026-09-06 PM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10, 2/10 Bearish at AM 09-06, no prior qualifying read to confirm against). Mechanical p2-10 improved to 7/9 Bullish, 0/9 Bearish (golden-cross clean, RSI mid-band, OI confirming both windows). p1 sentiment read Neutral — flat interest, mild dismissive/capitulation-flavored chatter ("shit token," "no value," range-bound complaints) mixed with routine technical setups and factual RWA/tokenized-collateral narrative, not a clean crowd-extreme either way. Not currently held (exited 2026-08-29, sector-cap correction, not a thesis failure). Needs AM 09-07 to confirm. 1 open slot remains in the book (4/5 positions held post-ETHFI-entry) if ONDO confirms.

## STAGE-2 ADD — ETHFI — 2026-09-07 AM

Confluence held **7/10 Bullish, 1/10 Bearish** at this checkpoint (second consecutive checkpoint since the PM 09-06 confirmation, held flat) — per Section 5 step 9, the second half opens at full target size on the hold.

Mechanical parameters unchanged in shape from PM 09-06 (DMA golden-state, dev-from-50DMA +20.4% moderate, RSI 58.4 mid-band, funding flat, OI confirming both windows, stables/MVRV healthy); p1 sentiment held Bearish both checkpoints on the same recurring euphoria-driven pattern for this ticker (rising interest, "+90% last week," rocket emojis, 50-100% breakout targets, whale-positioning hype, zero capitulation offset) — costs nothing against the bullish count, as with the PM 09-06 confirmation itself.

**Fill:** BUY 860.8757 ETHFI @ $0.5767 = $496.467 notional (matching the stage-1 half's original ~$496.467 sizing), 2026-09-07T07:20:00Z (Binance spot via `parameters.py` refresh). Position now 1728.5216 ETHFI, avg entry $0.574441, ~10.06% of portfolio ($996.84 / $9,909.77) — full target size reached. No further staging; ongoing test is the same OI/price/RSI/DMA structure through the 2026-09-20 interim review.

## SIGNAL — ONDO lapsed — 2026-09-07 AM

Armed at PM 09-06 (7/10, 0/10 Bearish, first occurrence) — did not hold at AM 09-07, easing to 6/10 (0/10 Bearish) as p6_funding rolled Bullish→Neutral (funding ticked up to 0.0316%/8h, into the rubric's ambiguous 0.02-0.05% Neutral band). p1 sentiment held Neutral both checkpoints — falling interest, zero euphoria/capitulation markers, purely technical/factual chatter. Second consecutive ≥7/10 checkpoint not reached — arm lapses per Section 5 step 5. Not currently held (exited 2026-08-29). Would need a fresh first-occurrence ≥7/10 read to re-arm.

## SIGNAL — BNB armed — 2026-09-07 AM (first occurrence)

Confluence 7/10 Bullish, 2/10 Bearish — first occurrence this fresh sequence (PM 09-06 was 5/10, none; BNB previously armed PM 09-05 and lapsed AM 09-06). Mechanical p2-10 strong (7/9 Bullish, 1/9 Bearish — p5_volz Bearish on an elevated volume z-score despite the price surge). Price structure golden-cross, dev-from-50DMA +17.5%, RSI 69.0 upper band with some room, OI strongly confirming (24h +1.7%, 7d +34.7%), funding flat. p1 sentiment read Bearish (contrarian) — rising interest, euphoria dominant (price targets $775-880, short-squeeze/breakout framing, "$140M shorts liquidated"), zero capitulation offset. Not currently held. Needs PM 09-07 to confirm. 1 open slot remains in the book (4/5 positions held) if BNB confirms.

## SIGNAL — XRP armed — 2026-09-07 AM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this fresh sequence (PM 09-06 was 5/10, none). Mechanical p2-10 clean (6/9 Bullish, 0/9 Bearish — dev-from-50DMA +18.5% moderate, RSI 60.6 mid-band, OI confirming 7d +7.9%, funding flat). p1 sentiment read Bullish (contrarian) — flat interest, zero euphoria markers, genuine capitulation-flavored dismissal (scam/trash/manipulation accusations, price-underperformance complaints) with no euphoria offset. Not currently held. Needs PM 09-07 to confirm. 1 open slot remains in the book (4/5 positions held) if XRP confirms.

## CONFIRMED ENTRY — BNB — 2026-09-07 PM (Tier B-floor, staged half)

**Frozen 10-parameter table at entry (PM 09-07, confluence 7/10, 0/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Neutral | flat interest, cautious/mixed technical chatter (overbought-RSI-79.7 correction-risk calls, "bearish distribution and sell pressure") mixed with unrelated BNB-chain meme-coin shilling — no clean crowd-extreme dominance |
| p2 DMA | Bullish | price $739.53 above 50DMA $633.9506 and 200DMA $622.0518, golden cross |
| p3 RSI | Bullish | 66.8, upper-mid band with some room |
| p4 rvol | Bullish | 1.40 (expansion) |
| p5 volz | Neutral | -0.27 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +27.2%, 24h -7.2% (single-day dip on a strong weekly print) |
| p8 stables | Bullish | +0.55%/7d |
| p9 MVRV | Bullish | BTC 1.51, ETH 1.12 |
| p10 F&G | Neutral | 71, +9/7d |

**Both consecutive checkpoint counts:** AM 09-07 7/10 Bullish (2/10 Bearish, first occurrence — armed) → PM 09-07 7/10 Bullish (0/10 Bearish, second consecutive — confirmed). Mechanical p2-10 held clean 7/9 Bullish both checkpoints (Bearish count eased 2→0 as p1 cooled from AM's euphoria-driven Bearish read to a fresh Neutral, and p5_volz's AM Bearish flag eased to Neutral).

**Expectancy sheet:** Entry $739.53, Target $851.00 (+15.07%, mid-upper end of the sentiment-cited $775-880 short-squeeze/breakout zone, taken conservatively rather than at the top of that hype-flavored range), Invalidation $695.00 (-6.02%, the approximate price level from ~7 days before this breakout leg, with the 50DMA $633.9506 as further backstop). R = 2.50. Stated p = 0.45. EV = +3.47%. Both R and p sit exactly at the Tier B floor (R≥2.5, p≥0.45) — sized at the low end of the 15-25% Tier B range (15% target) given the borderline stats; staged half now at 7.5% of $9,885.6851 portfolio = $741.4264 notional, 1.002564 BNB.

**Runner-up candidates this checkpoint:** XRP also confirmed 7/10 Bullish, 0/10 Bearish this checkpoint (its own 2nd consecutive read since AM 09-07's arm) — tied with BNB for the book's one open slot. EV tie-break per Section 5 step 6: BNB +3.47% > XRP +3.27% (R=2.41, p=0.42; Entry $1.3956, Target $1.65, Invalidation $1.29). XRP loses by a narrow margin and is logged as a rejected runner-up with a virtual entry in SHADOW_BOOK.md, to be marked-to-market at the next Monday shadow-book refresh (2026-09-14).

**Sizing/sector context:** Exchange sector was empty pre-entry — no sector-cap constraint. 4/5 positions held pre-entry (MORPHO, JUP, ETH, ETHFI) → 5/5 post-entry — book now at the maximum concurrent-positions hard rule (Section 3 rule 1). Post-entry sector split (of deployed capital): DeFi Lending ~11.7%, DEX ~13.5%, Major L1 ~26.9%, Liquid Staking ~27.5%, Exchange ~20.3% — five single-position sectors, each comfortably under the 50% cap.

**Red-team note (see PM checkpoint report for full pass):** with F&G at 71 (Greed) and both BNB and XRP arming/confirming in the same 24-hour window, is the entry gate simply easier to clear because the regime is hot rather than either name having a genuinely strong setup? p10_fg reads Neutral for every coin this checkpoint (71 sits inside the rubric's Neutral band, not yet the >75 Bearish trigger) — it isn't inflating anyone's count. BNB's confirmation is driven by coin-specific mechanical strength (7/9 mechanical Bullish on real OI/RSI/DMA confirmation, unchanged both checkpoints) rather than a regime tailwind on the count itself. The genuine risk from the hot regime is architectural, not a gate-integrity problem: taking the book to 5/5 positions (maximum concurrent) while F&G continues climbing raises the stakes of the standing "BTC -15% overnight" pre-mortem scenario, addressed explicitly below rather than by declining the confirmed entry.

## SIGNAL — AAVE armed — 2026-09-07 PM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this fresh sequence (AM 09-07 and the two checkpoints before it were 6/10, none). Mechanical p2-10 clean (7/9 Bullish, 0/9 Bearish — golden-cross, RSI 62.0 mid-band, OI confirming both windows). p1 sentiment read Neutral — flat interest, thin excitement markers ("waking up for real, this could get wild") mixed with factual UK/HMRC tax-regulation-response news, too sparse for a clean crowd-extreme read (a cooldown from PM 09-06's euphoria-dominant contrarian-Bearish read). Not currently held. Needs AM 09-08 to confirm. No open slot remains in the book post-BNB-entry (5/5 positions held, at the maximum concurrent-positions hard rule) — would need a future anti-churn win or an open slot to enter even if it confirms.

## SIGNAL — ONDO armed — 2026-09-07 PM (fresh first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — fresh first occurrence (the AM 09-07 lapse broke the PM 09-06 arm's sequence). Funding rolled back Neutral→Bullish this checkpoint (0.0316%/8h AM → back inside the near-zero Bullish band), reversing the single-parameter shift that caused the AM lapse. Mechanical p2-10 clean (7/9 Bullish, 0/9 Bearish). p1 sentiment read Neutral — flat interest, zero euphoria/capitulation markers, purely technical chatter (rising-wedge/bearish-breakdown setups, tokenized-stock collateral narrative). Not currently held (exited 2026-08-29). Needs AM 09-08 to confirm. No open slot remains in the book post-BNB-entry (5/5 positions held).

## SIGNAL — ONDO lapsed — 2026-09-08 AM

Armed at PM 09-07 (7/10, 0/10 Bearish, fresh first occurrence) — did not hold at AM 09-08, easing to 6/10 (0/10 Bearish) as p3_rsi rolled Bullish→Neutral (RSI eased to 54.4 on a near-flat dev-from-50DMA of +2.1%, the setup losing its mid-band strength rather than breaking down). p1 sentiment stayed Neutral (flat interest, purely technical chart chatter, no clean crowd-extreme dominance) — honestly graded Neutral rather than forced Bullish to complete a 7th parameter, per the standing guardrail against manufacturing confirmations. Arm lapses per Section 5 step 5; a fresh arm would need to restart from a new first-occurrence ≥7/10 read. Moot for slot purposes this checkpoint regardless — the book's one open slot (freed by the MORPHO anti-churn exit) went to AAVE, which did confirm; see the AAVE entry below.

## EXIT POST-MORTEM — MORPHO (anti-churn displacement) — 2026-09-08 AM

**P&L:** -$12.1461 realized (-0.34R vs planned R=2.07) on the full 174.417 MORPHO position, entered 2026-08-26 at an avg cost of $2.485638, exited 2026-09-08 AM at $2.416 (-2.80% over the 13-day hold). A small realized loss, not a stop-out — invalidation ($2.28) was never remotely threatened (~5.6% headroom remained at exit).

**Thesis verdict:** Playing Out / Intact, right up to the exit — this was not a thesis failure. MORPHO was closed purely because Section 5 step 7's anti-churn rule permits displacing a Playing-Out/Intact holding when a confirmed candidate's confluence exceeds it by ≥2: AAVE confirmed 7/10 Bullish (0/10 Bearish) this checkpoint while MORPHO's own confluence had eased to 5/10 (0/10 Bearish) — exactly a 2-parameter gap, the minimum required. Both names sit in the same DeFi Lending sector, so this is a direct like-for-like rotation rather than a diversification or cap-driven move.

**Per-parameter verdict at entry (2026-08-26 AM, confluence 7/10, 0/10 Bearish) vs. this checkpoint's exit (5/10, 0/10 Bearish):**
- p3 RSI: Bullish (61.9) at entry → Neutral this checkpoint (51.3) — RSI drifted toward the middle of its range as the position went essentially sideways-to-down; not a breakdown signal, just lost the mid-upper-band edge that scored Bullish at entry.
- p7 OI: Bullish (7d +41.6%) at entry → Neutral this checkpoint (24h +4.8%, 7d -7.8%) — the single biggest driver of the confluence drift. This softness was flagged as a likely `OI_HISTORY.json` rolling-window artifact repeatedly across the hold (never definitively resolved either way), consistent with the parameter scorecard's standing note that p7 is the rubric's highest-variance, most consequential single point of failure.
- p2 DMA, p4 rvol, p6 funding, p8 stables, p9 MVRV: all stayed Bullish, unchanged — the structural/technical legs of the thesis never wavered; price stayed above both DMAs in golden-cross structure the entire hold.
- p1 sentiment, p5 volz, p10 F&G: Neutral across most of the hold — never a swing factor either way.
- Thesis's own named risk ("thin volume") materialized as exactly the p7/OI softness that drove the confluence gap this checkpoint — the entry thesis correctly flagged the vulnerability that ultimately triggered the anti-churn displacement, even though it never became a genuine breakdown.

**p calibration:** stated p=0.40 at entry; outcome was a small negative round-trip, not a resolved bet against target or invalidation (neither was reached) — the anti-churn mechanic intervened before the probabilistic call was ever tested, consistent with most other closed legs this paper phase.

**Sizing/timing verdict:** MORPHO never reached its 10% target size (capped at 4.53% historically per its `trimmed_sector_cap` stage tag, though no sector cap was actually binding this checkpoint — five single-position sectors). The undersized position limited the loss to a modest $12.15 on what was, in dollar terms, a fairly muted -2.8% move; sizing discipline did its job here regardless of the exit trigger.

**Counterfactual vs. runner-ups:** AAVE, the anti-churn winner, is the same-sector deeper-liquidity blue chip MORPHO's own entry thesis explicitly named as the competitor MORPHO was "taking share from." No other candidate competed for this slot this checkpoint (ONDO armed at PM 09-07 lapsed to 6/10 before it could confirm). Tracked as a virtual continuation in `SHADOW_BOOK.md` against AAVE's actual performance from this point forward — the cleanest head-to-head comparison the shadow book has run yet (same sector, same-day rotation, not a staged-entry non-confirmation or a thesis-broken exit).

**One testable lesson:** this is the paper phase's first anti-churn displacement of a Playing-Out/Intact holding (as opposed to a thesis-broken exit or a staged-entry non-confirmation cut) — worth tracking as its own category going forward. Hypothesis: a displacement triggered by the *displaced* position's OI softening (rather than the *entering* candidate's outright strength) may be more prone to false-negative regret than one triggered by a genuinely superior new setup, since OI softness has repeatedly proven noisy/rolling-window-prone in this book's own parameter scorecard. The MORPHO/AAVE shadow-book pair over the next few weeks is the direct test.

## CONFIRMED ENTRY — AAVE — 2026-09-08 AM (Tier C, staged half, anti-churn displacement)

**Frozen 10-parameter table at entry (AM 09-08, confluence 7/10, 0/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Neutral | flat interest, zero euphoria/capitulation markers — purely factual protocol news (V4 rewards live, deposits crossing $600M, BTC-collateral testing, scattered whale-buy mentions) |
| p2 DMA | Bullish | price $131.06 above 50DMA $106.334 and 200DMA $97.016, golden cross, dev +23.3% |
| p3 RSI | Bullish | 61.1, mid-band with room |
| p4 rvol | Bullish | 0.49 (compression/setup) |
| p5 volz | Neutral | -1.02 |
| p6 funding | Bullish | 0.01%/8h, flat, no crowding |
| p7 OI | Bullish | 7d +5.1%, 24h -3.0% (single-day dip on an otherwise-positive weekly print) |
| p8 stables | Bullish | +0.53%/7d |
| p9 MVRV | Bullish | BTC 1.49, ETH 1.10 |
| p10 F&G | Neutral | 69, +0/7d |

**Both consecutive checkpoint counts:** PM 09-07 7/10 Bullish (0/10 Bearish, first occurrence — armed) → AM 09-08 7/10 Bullish (0/10 Bearish, second consecutive — confirmed). Mechanical p2-10 held clean 7/9 Bullish both checkpoints; p1 stayed Neutral both times (a cooldown from PM 09-06's euphoria-driven Bearish read, per the SIGNAL log).

**Expectancy sheet:** Entry $131.06, Target $154.50 (+17.88%, a conservative ~18% swing target consistent with this book's typical Tier C sizing given no explicit sentiment-cited resistance zone was found — price has been broadly range-extending on the V4-deposits catalyst), Invalidation $120.00 (-8.44%, the approximate consolidation zone from the prior week before the latest advance leg, with the 50DMA $106.334 as further backstop). R = 2.12. Stated p = 0.42. EV = +2.61%. Tier C (R≥2, p≥0.40) — sized at the standard 10% target consistent with MORPHO/JUP/ETHFI's own Tier C sizing; staged half now at 5.0% of $9,869.9711 portfolio = $493.4986 notional, 3.76544 AAVE.

**Anti-churn justification (Section 5 step 7):** the book was at 5/5 positions (maximum concurrent) pre-checkpoint with no staged-entry non-confirmation freeing a slot. AAVE's confluence (7, 0 Bearish) exceeds the weakest Playing-Out/Intact holding, MORPHO (5, 0 Bearish), by exactly the required ≥2-parameter gap — the minimum threshold, not a blowout. Both names are DeFi Lending, so this is a like-for-like sector rotation, not a diversification play: AAVE is the deeper-liquidity blue chip (vol/mcap 0.15 per its watchlist entry) that MORPHO's own thesis named as the incumbent it was "taking share from," while MORPHO's own thesis separately flagged thin volume as its standing risk — the OI softness that drove its confluence drift this checkpoint is exactly that risk materializing (see the MORPHO exit post-mortem above for the full per-parameter breakdown).

**Runner-up candidates this checkpoint:** none — AAVE was the sole coin reaching 7/10 this checkpoint (ONDO, PM 09-07's other arm, lapsed to 6/10 before it could confirm; see the SIGNAL log above). No EV tie-break needed.

**Red-team pass:** Three objections considered before executing.
1. *Is this genuine signal or noise-driven churn?* MORPHO's thesis is not broken (still golden-cross, invalidation untouched, 0/10 Bearish) — displacing it purely on a 2-point confluence gap risks reacting to day-to-day parameter noise (p3 RSI and p7 OI both softened, and OI has read mixed/soft on MORPHO for multiple recent checkpoints, flagged repeatedly as a possible rolling-window artifact that never fully resolved). Counter: the anti-churn rule was written explicitly to permit exactly this kind of capital-velocity rotation at a ≥2 gap — refusing to ever use it defeats its purpose, and MORPHO's own entry thesis independently named the exact vulnerability (thin volume/liquidity) that is now showing up as OI softness.
2. *Same-sector concentration risk.* Rotating MORPHO→AAVE keeps DeFi Lending at exactly one position (no net sector-count change) but makes the book's DeFi Lending exposure entirely dependent on one thesis (institutional/RWA-adjacent lending demand) rather than diversified across two related-but-distinct plays. Accepted as a reasonable tradeoff — AAVE is the structurally stronger, deeper-liquidity name of the two, and Hard Rule 8 (max 2/5 positions, ≤50% capital per sector) is nowhere close to binding with a single position.
3. *Realizing a loss to fund a marginal-edge entry.* The MORPHO exit locks in a small realized loss (-$12.15, -0.34R) rather than waiting for the 2026-09-09 interim review date (one day out) where a Stalled-designation trim might have applied more gradually. Counter: the entry gate's 2-consecutive-checkpoint confirmation is time-sensitive by design (Section 9: "action bias is your enemy," but so is *inaction* bias once a candidate has genuinely cleared the bar) — delaying AAVE's entry by a day to avoid a small realized loss on MORPHO would be optimizing for paper-loss-aversion over the stated capital-velocity rule.

Net: proceed. The gap is real (not forced), the rotation is sector-neutral and thesis-coherent (challenger → incumbent within the same narrative), and the realized loss is small and within normal expectancy variance.

**Sizing/sector context:** DeFi Lending sector unchanged at one position (MORPHO's slot passed directly to AAVE). Post-trade sector split (of deployed capital): DEX ~4.9%, Major L1 ~9.9%, Liquid Staking ~10.2%, Exchange ~15.1%, DeFi Lending ~5.0% (staged half) — five single-position sectors, all comfortably under the 50% cap. Book remains at 5/5 positions (maximum concurrent, Hard Rule 1).

## EXIT POST-MORTEM — AAVE — 2026-09-08 PM (staged-entry non-confirmation)

**P&L:** -$7.0414 realized on the 3.76544 AAVE half-tranche (entry $131.06, exit $129.19, -1.43%). Realized R -0.169 vs planned R=2.12 (a small loss on a fraction of a full position; the second half was never opened).

**Thesis verdict:** Playing Out / Intact at exit — this was not a thesis failure and not a Bearish-count trigger (0/10 Bearish at both the AM 09-08 entry and this PM 09-08 exit). AAVE was closed purely because Section 5's staged-entry mechanic requires confluence to hold ≥7/10 at the immediate next trading checkpoint to justify adding the second half; it eased to 6/10 instead. Per the standing rule (applied identically to LINK on 2026-09-05 PM and ETH on 2026-09-05 AM), no confirmation at that checkpoint means the half is cut, not carried forward to wait for a later recovery.

**Per-parameter verdict at entry (AM 09-08, confluence 7/10, 0/10 Bearish) vs. this checkpoint's exit (6/10, 0/10 Bearish):**
- p7 OI: Bullish (7d +5.1%, 24h -3.0%) at entry → Neutral this checkpoint (24h -2.1%, 7d -1.6%) — the sole parameter that flipped, and the entire driver of the confluence drop. A mixed-soft two-window read rather than a genuine reversal; this is the same OI-metric fragility flagged repeatedly in this book's parameter scorecard (MORPHO's own exit post-mortem immediately above names the identical failure mode).
- p2 DMA, p3 RSI, p4 rvol, p6 funding, p8 stables, p9 MVRV: all stayed Bullish, unchanged — golden-cross structure, RSI mid-band (59.0), and funding/stablecoin/MVRV backdrop never wavered across the one-checkpoint hold.
- p1 sentiment, p5 volz, p10 F&G: Neutral at both checkpoints — never a swing factor.
- No thesis-test condition was breached (invalidation $120.00 never approached within ~7.5%; RSI never overbought).

**p calibration:** stated p=0.42 at entry; the position was closed before the probabilistic bet against target/invalidation was ever tested — the staged-entry mechanic intervened on a single-parameter wobble, consistent with the LINK/ETH precedents from 2026-09-05.

**Sizing/timing verdict:** the staged-entry rule did exactly what it is designed to do — capped downside to a half-size tranche ($493.50 notional, 5.0% of portfolio) and a modest $7.04 loss rather than committing the full 10% target size on a read that didn't hold for even one additional checkpoint.

**Counterfactual vs. runner-ups:** no competing candidate existed at entry (AAVE was the sole confirmed candidate via anti-churn displacement of MORPHO). ONDO, this same PM 09-08 checkpoint's fresh arm at 7/10 (0/10 Bearish), is the closest live comparison — logged as newly armed, not yet a confirmed alternative. Tracked for the next Monday (2026-09-14) shadow-book weekly refresh alongside the other staged-entry cuts.

**One testable lesson:** this is the third staged-entry non-confirmation cut driven specifically by a single p7_oi flip (Bullish→Neutral on a mixed 24h/7d read), following ETH and LINK's own 2025-09-05 cuts (though those were driven by p2_dma overextension, not p7_oi). Given the parameter scorecard's standing note that OI is the rubric's highest-variance single point of failure (also named in the MORPHO exit above, same checkpoint), this strengthens the case for the next monthly review to examine whether p7_oi's Hyperliquid-fallback-sourced 24h/7d dual-window read is unusually prone to flipping a position's confluence by exactly one parameter — right at the margin of the 7/10 gate — more often than the other eight parameters combined.

## CONFIRMED ENTRY — TRX — 2026-09-09 PM (Tier C, staged half)

**Frozen 10-parameter table at entry (PM 09-09, confluence 7/10, 0/10 Bearish):**

| # | Parameter | Label | Raw |
|---|---|---|---|
| p1 sentiment | Bullish | rising interest, euphoria markers read as factual catalyst coverage of the live Cboe TRXS staked-TRX ETF launch (Canary Capital) and TRON Inc./TRXS dual-structure narrative rather than manic crowd hype, zero capitulation — improving interest without euphoria around a genuine dated catalyst |
| p2 DMA | Bullish | price $0.3398 above 50DMA $0.33265 and 200DMA $0.325559, golden cross, dev only +2.1% — low-vol/low-beta profile |
| p3 RSI | Bullish | 57.9, mid-band with room |
| p4 rvol | Bullish | 0.58 (compression/setup) |
| p5 volz | Neutral | -0.88 |
| p6 funding | Bullish | 0.0067%/8h, flat, no crowding |
| p7 OI | Neutral | 24h -0.5%, 7d -9.4% — mild mixed read, immaterial to the gate |
| p8 stables | Bullish | +0.58%/7d |
| p9 MVRV | Bullish | BTC 1.47, ETH 1.10 |
| p10 F&G | Neutral | 66, +3/7d |

**Both consecutive checkpoint counts:** AM 09-09 7/10 Bullish (0/10 Bearish, first occurrence — armed) → PM 09-09 7/10 Bullish (0/10 Bearish, second consecutive — confirmed). Mechanical p2-10 held clean 6/9 Bullish, 0/9 Bearish both checkpoints (p7_oi Neutral throughout); p1 sentiment is what tipped the gate both times, flipping from its long-standing Neutral read to Bullish specifically around the dated ETF-launch catalyst.

**Expectancy sheet:** Entry $0.3398, Target $0.378 (+11.24%), Invalidation $0.322 (-5.24%, set just under the 200DMA $0.325559 as the structural golden-cross backstop) — deliberately tight bands reflecting TRX's low-vol/low-beta profile (only +2.1% above its own 50DMA at entry, the tightest extension of any position on the book). R = 2.15. Stated p = 0.42. EV = +1.68%. Tier C (R≥2, p≥0.40) — sized at the standard 10% target; staged half now at 5.0% of $9,896.2535 portfolio = $494.8127 notional, 1456.1881 TRX.

**Runner-up candidates this checkpoint:** PYTH newly armed at 7/10 (0/10 Bearish) — first occurrence, not yet confirmed (needs AM 09-10 to confirm). No EV tie-break needed since PYTH did not confirm this checkpoint. Book was at 4/5 positions pre-checkpoint (one open slot) — TRX fills it directly, no anti-churn displacement required.

**Red-team pass:** Three objections considered before executing.
1. *Is the ETF-launch catalyst genuinely durable, or a one-day news spike?* The Cboe TRXS staked-TRX ETF launched today (09-09) — the euphoria markers observed are explicitly catalyst-linked (ETF-listing coverage, TRON Inc./TRXS dual-structure discussion) rather than generic price-target hype, and this same factual-coverage read held across both the AM armed checkpoint and this PM confirmation, giving two independent data points rather than a single-day spike. Counter-risk: once the launch-day news cycle fades, p1 could just as quickly revert to its long-standing Neutral baseline, which would drop TRX to 6/10 — the position is already staged (half-size) specifically to manage this risk, and the second half explicitly requires the read to hold one more checkpoint.
2. *R:R math is thin for the confluence spent.* TRX's low volatility genuinely constrains the achievable R — a wider, more typical Tier-C target (15-20%) was not defensible against TRX's own price history (only +4.5% over the past 7 days), so both target and invalidation were compressed to stay proportional. R=2.15 clears the 2.0 floor but with little margin; a larger adverse slippage on the actual fill would have failed the gate entirely. Accepted — the floor is the floor, and forcing a wider target purely to build R margin would fabricate an unrealistic price target for a genuinely low-beta asset.
3. *Sector concentration.* TRX shares Major L1 with the held ETH position, taking that sector to 2 of 5 positions (~32.84% of deployed capital) — within both the max-2-per-sector and the 50%-of-deployed-capital caps, but now the book's largest single-sector concentration. Accepted — both names have genuinely distinct theses (ETH settlement-layer/RWA vs. TRX stablecoin-rails/ETF-institutionalization) and the cap is nowhere close to binding.

Net: proceed with a staged half-entry. The catalyst is real and dated, the expectancy math clears the floor (if narrowly), and sector/position limits are respected with room to spare.

**Sizing/sector context:** Post-trade sector split (of deployed capital): DEX (JUP) ~10.99%, Major L1 (ETH+TRX) ~32.84%, Liquid Staking (ETHFI) ~23.34%, Exchange (BNB) ~32.83% — four sectors, Major L1 now two positions, all comfortably under the 50% cap. Book now at 5/5 positions, maximum concurrent per Hard Rule 1.

## STAGE-2 ADD — TRX — 2026-09-10 AM

Confluence held **7/10 Bullish, 0/10 Bearish** at this checkpoint (second consecutive checkpoint since the PM 09-09 half-open confirmation) — per Section 5 step 9, the second half opens at full target size, no confirmation needed beyond the hold itself.

Mechanical parameters unchanged in shape from PM 09-09 (golden-cross intact, dev-from-50DMA a modest +2.1% — the least-extended position on the book, RSI 58.0 mid-band, funding flat, OI Neutral-mixed); p1 sentiment held Bullish — rising interest, narrative still centered on the live Cboe TRXS staked-ETF launch and TRX's expanding reach into TradFi, described as factual catalyst coverage ("no artificial pump, just strong activity") rather than crowd hype, zero capitulation.

**Fill:** BUY 1456.1881 TRX @ $0.3398 = $494.8127 notional (matching the stage-1 half's original ~$494.8127 sizing), 2026-09-10T07:10:00Z (Binance spot via `parameters.py` refresh). Position now 2912.3762 TRX, avg entry $0.3398, ~10.04% of portfolio ($989.63 / $9,854.84) — full target size reached. No further staging; ongoing test is the same OI/price/RSI/DMA structure through the 2026-09-23 interim review.

## SIGNAL — PYTH lapsed — 2026-09-10 AM

PYTH's PM 09-09 arm (7/10, first occurrence) did not confirm: confluence eased to 6/10 (0/10 Bearish) this checkpoint as p1 sentiment cooled from Bullish (rising interest, factual record-metrics reporting) to Neutral (flat interest; mild community-fandom euphoria language — "Pyth pilled," "never stop cooking," a gamified rewards-wheel — without a genuine price-target mania, so neither a clean euphoria call nor "improving interest" applied cleanly). Mechanical p2-10 held flat at 6/9 Bullish, 0/9 Bearish both checkpoints — the swing was entirely on the p1 judgment call, applied honestly rather than forced to confirm a trade into an already-full (5/5) book that would have required an anti-churn displacement. No action; sequence resets, would need two fresh consecutive ≥7/10 reads to re-arm and confirm.

## TRIM HALF — ETHFI — 2026-09-12 AM (Weakening conviction, named thesis-test breach)

Price $0.7286 (+8.65% vs PM 09-11 close $0.6706, +26.84% vs avg entry $0.574441) — the position has now moved decisively past its own original $0.68 target (+7.15% beyond it), with the two technical pillars of the entry thesis's own named `thesis_test` both giving way for the first time in this multi-week hold:

1. **Named thesis-test breach:** RSI printed 76.2, crossing above 75 — the exact line the entry thesis's `thesis_test` named explicitly ("RSI stays out of overbought (<75) as price extends toward target"). RSI has hovered just under this line and been flagged as a proximity watch item at nearly every checkpoint since PM 09-10 (73.5 → 71.9 → 70.8 → 76.2) but never before crossed it.
2. **Overextension at a new hold-high:** dev-from-50DMA deepened to +45.8% (from +35.9% PM 09-11, +37.8% AM 09-11, +43.0% PM 09-10) — widening again after two checkpoints of mild easing, and by a wide margin the deepest overextension anywhere on the book.

Mechanical p2_dma and p3_rsi both flipped Bearish this checkpoint — the first time both have read Bearish simultaneously in this hold — lifting the Bearish count to 3/10 alongside the recurring p1 sentiment Bearish read (flat interest, clear euphoria dominance: price targets 0.7117–0.7432, bullish-structure claims, "leading gainers" mentions, zero capitulation offset, the same pattern flagged nearly every checkpoint of this hold). 3/10 Bearish is still short of the ≥4/10-for-1-checkpoint mechanical trim gate — this trim is triggered by the named thesis-test breach under Section 5 step 4's "Weakening → trim half" branch, independent of the Bearish-count gate.

**Red-team counterpoint (why a trim, not a full exit):** OI still strongly confirms the underlying trend (7d +56.8%, real capital continuing to flow in — not the OI-divergence-on-a-rally pattern that would mark a genuine blow-off top) and funding stays flat (0.01%/8h, no crowded-long unwind risk). The flow/positioning pillars remain healthy even as the price/technical pillars have overshot — thesis stays **Playing Out**, conviction downgraded **Intact → Weakening** (not Failing), and the call is a half-trim on strength, not a loss-cutting exit.

**Action:** SOLD 864.2608 ETHFI @ $0.7286 = $629.7004 proceeds, 2026-09-12T07:11:00Z (Binance spot, same `parameters.py` refresh, generated_at 2026-09-12T07:06:41Z). Avg entry unchanged $0.574441. Realized P&L on the trimmed half: **+$133.2336 (+2.8317R vs planned R=2.07)** — the best realized-R tranche of this hold to date, a profit-taking trim rather than a loss-cutting one. Position now 864.2608 ETHFI, ~6.23% of portfolio (down from ~11.6%). Invalidation $0.52 not breached (~28.6% headroom, still the widest on the book).

**Flagged for confirmation next checkpoint:** if RSI reclaims <75 and dev-from-50DMA stabilizes/narrows with OI still confirming, the remaining half stays held as a normal Playing-Out/Intact position at its new half size. If RSI stays >75, the Bearish count reaches 4/10, or overextension deepens further, the remaining half becomes the next trim/exit candidate.

**Counterfactual tracked in SHADOW_BOOK.md** at the next refresh: the trimmed half continues as a virtual position for comparison against the hold-full-size counterfactual.

## EXIT POST-MORTEM — ETHFI — 2026-09-12 PM (full exit, remaining half)

**P&L:** Two tranches. 09-12 AM trim-half: +$133.2336 (proceeds $629.7004 vs cost basis $496.467 on 864.2608 ETHFI at avg entry $0.574441). 09-12 PM full exit of remainder: +$140.7526 (proceeds $637.2195 vs cost basis $496.467 on the same 864.2608-unit second half — both halves shared the identical avg entry price since this was a single unstaged confirmed entry, not a two-stage buy). **Total realized P&L on the hold: +$273.9862** on $629.7004 deployed at peak (5% of portfolio at entry) — roughly +43.5% on the position, +2.71% of total portfolio at entry-time sizing. This is the single most profitable closed position of the paper phase to date.

**Realized R vs planned:** Tranche 1 (AM trim): +2.8317 vs planned 2.07. Tranche 2 (PM full exit): +2.9915 vs planned 2.07. Both tranches comfortably exceeded the planned R — the position ran well past its original $0.68 target on both legs (final exit at $0.7373, +8.4% beyond target) rather than being cut on a loss.

**Thesis verdict:** Playing Out through both trims, marked **Broken only at the very end**, and only on its own narrow technical test — not on the trend thesis itself. The entry thesis's `thesis_test` had three named legs: (1) OI keeps expanding alongside price, (2) price holds above the 50DMA, (3) RSI stays out of overbought (<75). Legs 1 and 2 held clean for the entire hold (OI +56-57% 7d at both trims, price never remotely threatened the 50DMA). Leg 3 — the RSI ceiling — broke at the AM 09-12 checkpoint (76.2) and, critically, **did not revert**: it printed 76.8 again this PM, alongside a fresh new high in dev-from-50DMA (47.5%, up from 45.8% AM). The thesis wasn't wrong about direction (ETHFI kept running higher through both exits) — it was right about the trend and wrong only about how far the position should have chased it once its own stated overextension guardrail failed to reset.

**Per-parameter verdict (frozen PM 2026-09-06 entry table):**
| # | Parameter | Entry label | Verdict | Note |
|---|---|---|---|---|
| 1 | Sentiment | Bearish (contrarian) | Right, and stayed right the entire hold | Euphoria-dominant reads (price targets, rocket emojis, breakout hype) recurred at nearly every single checkpoint from entry through final exit — the most consistent single-parameter signal of any hold this phase, though per Section 3 rule 6 it was never used as a standalone reason to act until paired with the named thesis-test breach. |
| 2 | DMA | Bullish (golden cross) at entry, flipped Bearish at both exit checkpoints | Right at entry, correctly flipped at the top | Golden-cross structure was genuine at entry (dev only +20.2% above 50DMA); by exit dev-from-50DMA had run to +47.5%, correctly triggering the rubric's own >25%-overextension override. The mechanical rubric called the turn accurately. |
| 3 | RSI | Bullish (57.7, mid-band) at entry, flipped Bearish at both exit checkpoints | Right at entry, correctly flipped at the top, and the actual exit trigger | This was the specific named thesis-test leg that broke and never reverted — the single parameter that actually ended the hold. |
| 4 | Rvol | Bullish (0.76, mild compression) | Right | Compression at entry preceded a genuine expansion move, exactly the setup case in the rubric. |
| 5 | Volz | Neutral at entry | Uninformative at entry, later confirmed | Cleared to Bullish mid-hold (genuine breakout volume, not a no-conviction spike) — consistent with the move being real, not manipulated. |
| 6 | Funding | Bullish (flat, 0.01%/8h) | Right, and stayed right the entire hold | Funding never once showed crowded-long risk despite the price nearly doubling from entry to exit — the derivatives market never got euphoric even as spot did, an important divergence that argued (correctly) for a staged trim rather than a panic full exit at the first overextension signal. |
| 7 | OI | Bullish (7d +23.7%) at entry | Right, and stayed right the entire hold | OI kept expanding in lockstep with price through both exits (7d +56-57% at the end) — this position never showed the OI-divergence failure pattern that killed the TRX and MORPHO holds (see their own post-mortems); the flow pillar was never the problem here. |
| 8 | Stablecoins | Bullish | Irrelevant to this name | Global regime parameter, applies identically to all coins. |
| 9 | MVRV | Bullish | Irrelevant to this name | Global regime parameter. |
| 10 | F&G | Neutral | Irrelevant to this name | Global regime parameter. |

**p calibration:** Stated p=0.41 at entry. Outcome: large win, well above the p<0.5 pricing — the position never tested its probabilistic bet against invalidation at all (invalidation $0.52 was never remotely threatened, ~28-29% headroom throughout); the exit was driven entirely by the thesis-test overextension guardrail, not by the target/invalidation race the stated p was pricing. Not a clean calibration data point on p itself, but a strong data point that this book's conservative Tier-C p estimates (0.40-0.42 range) can understate genuine trend-continuation upside when the flow pillars (OI, funding) stay clean.

**Sizing/timing verdict:** Sizing discipline worked well in both directions here: the confirmed entry sized to a standard 5% (Tier C), and the two-stage trim (half at the first RSI>75 print, the rest one checkpoint later on confirmed non-reversion) captured the bulk of the move while still de-risking promptly once the named guardrail failed — a materially better outcome than either (a) holding the full position through both checkpoints hoping for reversion, which would have left more capital exposed to a genuine top, or (b) cutting the entire position in one shot at the first RSI>75 print, which would have left real money on the table given OI/funding still confirmed at that moment. Timing verdict: close to optimal for a rules-based, non-clairvoyant process — the exit didn't chase a bottom-tick top, but it also didn't wait for a third checkpoint of confirmation once two straight prints showed no reversion whatsoever.

**Counterfactual vs runner-ups (PM 09-06 entry):** ONDO armed 7/10 the same checkpoint but did not compete for a slot (ETHFI was the sole confirmed candidate, 1 open slot). No selection-skill miss here — the entry pick was correct and the position was this phase's best single-name outcome by realized P&L.

**One testable lesson:** *This closes the loop opened by LESSONS.md hypothesis #18's "evidence to confirm" case: an unrealized-gain position's named thesis-test condition breached, a half-trim was taken, and the remaining half was exited cleanly one checkpoint later because the breached metric (RSI>75, dev-from-50DMA) did not reclaim its band and instead printed new worse highs on both measures. Proposed rule change (formalizing hypothesis #1/#18 into a general staged-exit protocol): when a named thesis-test condition breaches and triggers a half-trim, treat the very next checkpoint as a binary confirmation test on that same named metric alone (not the general Bearish-count gate) — metric reclaims its band → hold the remainder as a normal position; metric fails to reclaim or worsens further → exit the remainder in full, no third-checkpoint grace period. Evidence that would confirm: future thesis-test-breach trims where this binary rule produces a better realized outcome than waiting for the general ≥4/10-Bearish-for-2-consecutive gate. Evidence that would kill it: a case where the metric round-trips back into its healthy band on the very next checkpoint after a premature full exit was already taken, showing the one-checkpoint grace window is too short.*

## ENTRY — ASTER — 2026-09-18 PM

**Confluence history:** armed AM 2026-09-18 (7/10, first occurrence — PM 09-17 was 6/10), confirmed PM 2026-09-18 (7/10) — 2 consecutive trading checkpoints >=7/10, per Section 5 step 5-6.

**Frozen 10-parameter table (PM 2026-09-18, confirming checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | 400M-token team-lock extension to Sept 2027 (float overhang reduced), buyback/burn to veASTER, "rises 3.3% on positive news and social flows," whale accumulation, new perp-listing buzz; explicit "consensus mixed but leaning cautiously bullish" framing | Bullish | Improving interest without euphoria — 4th consecutive checkpoint on this read, no blow-off-top language at any point. |
| 2 | Price vs 50/200DMA | $0.752 vs 50DMA $0.6684; dev +12.5% | Bullish | Golden state, moderate (non-overextended) deviation. |
| 3 | RSI-14 | 60.4 | Bullish | Healthy 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.72 | Bullish | Compression, under 0.8. |
| 5 | Volume z-score | -0.34 | Neutral | Doesn't clear either Bullish or Bearish band. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | -4.2%/24h, -5.1%/7d | Neutral | Mild pullback on both windows, not a clean divergence against price either direction. |
| 8 | Stablecoin supply 7d Δ | +0.25% | Bullish | Sideline liquidity growing (global). |
| 9 | MVRV (BTC proxy) | BTC 1.44 / ETH 1.08 | Bullish | Healthy sub-2 band (global). |
| 10 | Fear & Greed | 56, Δ7d 0 | Neutral | Mid-band, not at either contrarian extreme (global). |

**Confluence: 7/10 Bullish, 0/10 Bearish.** (Mechanical p2-10 held flat at 6/9 Bullish, 0/9 Bearish both the AM armed and PM confirming checkpoints.)

**Expectancy sheet:**
- Entry: $0.752 (Binance spot, fetched 2026-09-18T19:06:07Z via `parameters.py`)
- Target: $0.93 (+23.7%) — measured-move estimate off the buyback/burn + team-lock-driven float-shrink thesis within the 2-8wk horizon
- Invalidation: $0.665 (-11.6%) — near the 50DMA ($0.6684); a close below breaks the golden-cross structure this thesis rests on
- R = 23.7 / 11.6 = **2.05** (clears the 2.0 floor)
- Stated p = **0.42** (Tier C default for a fresh, non-A/B-tier confirmed candidate with no idiosyncratic edge over the book's standard estimate)
- EV = 0.42×23.7% − 0.58×11.6% = **+3.24%** (clears EV>0 floor)
- Tier: **C** (R>=2, p>=0.40; confluence 7/10 falls short of Tier A's 8/10) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($512.61 notional, 681.6606 ASTER)**. Second half opens only if confluence holds >=7/10 at the next checkpoint (AM 2026-09-19); no confirmation cuts the half per Section 5 step 9.

**Runner-up candidates this checkpoint (did not enter):**
- **POL** — confirmed the same checkpoint at 7/10 (2nd consecutive, AM 09-18 armed → PM 09-18 confirmed, 0/10 Bearish both). Expectancy: Entry $0.10473, Target $0.128, Invalidation $0.093, R=2.03, p=0.40, EV=+2.36%. Lost the EV/R tiebreak to ASTER (Section 5 step 6: "highest confluence wins; EV breaks ties" — confluence tied at 7/10, ASTER's EV and R both marginally higher). Logged `confirmed-no-slot` in SIGNALS.csv, carried forward for the next open slot rather than requiring a fresh 2-checkpoint re-arm (precedent: XRP, PM 09-07).
- **SOL** — also confirmed at 8/10 (2nd consecutive, AM 09-18 armed → PM 09-18 confirmed), the highest confluence count of the three, but hard-rule-BLOCKED from entry: Major L1 sector already holds its 2-position cap (ETH, TRX) per Section 3 rule 8 — cannot enter regardless of confluence unless a Major L1 position exits first. This is a genuine "would have won the slot on confluence alone" case that the sector-cap rule overrides; flagged as a LESSONS.md hypothesis given the rulebook doesn't explicitly sequence sector caps against the highest-confluence-wins tiebreak rule.
- **ONDO** — newly armed this checkpoint at 7/10 (first occurrence, AM 09-18 was 6/10) — one checkpoint away from its own confirmation, not yet competing for a slot.

**Sector:** DEX (already held via JUP, 1→2/5 positions in-sector post-entry, within the max-2-per-sector cap; ~23.1% of deployed capital post-entry, within the 50%-of-deployed-capital sector cap). Book now at 5/5 positions — maximum concurrent per Section 3 rule 1.

## EXIT POST-MORTEM — ASTER — 2026-09-19 AM (staged-entry non-confirmation)

**P&L:** +$4.7716 realized on the 681.6606 ASTER half-tranche (entry $0.752, exit $0.759, +0.93%). Realized R +0.0805 vs planned R=2.05 (a small gain on a fraction of a full position; the second half was never opened).

**Thesis verdict:** Playing Out / Intact at exit — not a thesis failure and not a Bearish-count trigger (0/10 Bearish at both the PM 09-18 confirming checkpoint and this AM 09-19 exit). Closed purely because Section 5's staged-entry mechanic requires confluence to hold ≥7/10 at the immediate next trading checkpoint; it eased to 5/10 instead. Per the standing rule (applied identically to AAVE 09-08 PM, ETH/LINK 09-05), no confirmation means the half is cut, not carried forward to wait for a later recovery.

**Per-parameter verdict at entry (PM 09-18, confluence 7/10, 0/10 Bearish) vs. this checkpoint's exit (5/10, 0/10 Bearish):**
- p4 rvol: Bullish (0.72, compression) at entry → Neutral this checkpoint (0.81, crossed back above the 0.8 compression line) — one of the two parameters that flipped.
- p1 sentiment: Bullish (steady improving-interest read, 4 consecutive checkpoints) at entry → Neutral this checkpoint — the ticker-specific F&G-76/euphoria and unlock-drop data surfaced this run both traced to an early-Sept (~Sept 4) event already described by its own source as faded, so the read eased rather than flipped hard to Bearish; still the second parameter driving the drop below the reconfirmation bar.
- p2 DMA, p3 RSI, p6 funding, p8 stables, p9 MVRV: all stayed Bullish, unchanged — golden-cross structure, RSI mid-band (60.7), funding/stablecoin/MVRV backdrop never wavered across the one-checkpoint hold.
- p5 volz, p7 OI, p10 F&G: Neutral at both checkpoints — never a swing factor (p7 OI stayed soft-mixed, 24h +0.4%/7d -3.6%, consistent with the mild pullback flagged at entry).
- No thesis-test condition was breached (invalidation $0.665 never approached within ~14% at either checkpoint; RSI never overbought).

**p calibration:** stated p=0.42 at entry; the position was closed before the probabilistic bet against target/invalidation was ever tested — the staged-entry mechanic intervened on a two-parameter wobble (rvol + sentiment) after a single checkpoint, consistent with the AAVE/ETH/LINK precedents.

**Sizing/timing verdict:** the staged-entry rule did what it is designed to do — capped downside to a half-size tranche ($512.61 notional, 5.0% of portfolio) rather than committing the full 10% target size on a read that held for only one checkpoint. In this instance the tranche closed with a small gain rather than a loss, since price (barely) held above the entry despite the confluence reversal.

**Counterfactual vs. runner-ups:** POL, logged `confirmed-no-slot` at the same PM 09-18 checkpoint ASTER entered, filled the slot this ASTER cut freed — see the POL entry snapshot below, same checkpoint. Tracked for the next Monday (2026-09-21) shadow-book weekly refresh alongside other staged-entry cuts.

**One testable lesson:** this is the first staged-entry non-confirmation cut driven by a *joint* rvol+sentiment easing (both parameters moving only one notch, neither cleanly reversing) rather than a single clean flip (contrast AAVE's lone p7_oi flip, ETH/LINK's p2_dma overextension flips). Worth tracking whether a "two parameters easing by one notch each" pattern behaves differently on re-arm odds than a "one parameter flipping hard" pattern — ASTER's underlying fundamentals (team-lock, buyback/burn) never weakened, only the sentiment read cooled off a stale news cycle and the vol-compression setup normalized, which could mean this re-arms faster than a genuine deterioration-driven cut would. Evidence to confirm: ASTER re-arming to ≥7/10 within 2-3 checkpoints on a fresh sentiment or rvol reclaim. Evidence to kill: ASTER staying suppressed below 7/10 for a longer stretch, suggesting the two-notch easing was actually the leading edge of a genuine cooling rather than noise.

## ENTRY — POL — 2026-09-19 AM (carried-forward confirmed-no-slot)

**Confluence history:** originally armed AM 2026-09-18 (7/10) → confirmed PM 2026-09-18 (7/10, lost the EV/R tiebreak to ASTER, logged `confirmed-no-slot` per LESSONS #24/XRP-precedent) → confluence held exactly at 7/10 again this checkpoint (mechanical-only, 7/9 Bullish, p1 Neutral both checkpoints) — no re-arm required since it never dropped below 7/10 in the interim. Slot opened this checkpoint via ASTER's staged-entry non-confirmation cut (see exit post-mortem above).

**Frozen 10-parameter table (2026-09-19 AM, entering checkpoint):**

| # | Parameter | Value | Label | Reasoning |
|---|---|---|---|---|
| 1 | Sentiment (contrarian) | CMC-AI: "consensus mixed but leaning bullish," fundamentals (8B cumulative tx, enterprise adoption, rumored Coinme chatter) outperforming price action; F&G 61/Greed vs. technical-sentiment gauge only ~37% bullish | Neutral | Same mixed, no-dominance split as the original PM 09-18 confirmation — unchanged. |
| 2 | Price vs 50/200DMA | $0.10286, dev +13.6% | Bullish | Golden state, moderate deviation. |
| 3 | RSI-14 | 57.4 | Bullish | Healthy 55-70 band. |
| 4 | Realized vol ratio 7d/30d | 0.74 | Bullish | Compression, under 0.8. |
| 5 | Volume z-score | -0.8 | Neutral | Doesn't clear either band. |
| 6 | Funding rate | 0.01%/8h | Bullish | Near-zero, no crowded-long risk. |
| 7 | Open interest Δ | +18.6%/24h, +29.7%/7d | Bullish | Confirming the uptrend on both windows. |
| 8 | Stablecoin supply 7d Δ | +0.27% | Bullish | Sideline liquidity growing (global). |
| 9 | MVRV (BTC proxy) | BTC 1.52 / ETH 1.15 | Bullish | Healthy sub-2 band (global). |
| 10 | Fear & Greed | 71, Δ7d +8 | Neutral | Elevated but not past the 75/falling-fast contrarian thresholds (global). |

**Confluence: 7/10 Bullish, 0/10 Bearish.**

**Expectancy sheet (refreshed on today's fill price; Target/Invalidation carried forward as technical levels from the original PM 09-18 estimate):**
- Entry: $0.10286 (Binance spot, fetched 2026-09-19T07:07:14Z via `parameters.py`)
- Target: $0.128 (+24.4%) — unchanged technical level
- Invalidation: $0.093 (-9.6%) — unchanged technical level
- R = 24.4 / 9.6 = **2.55** (improved from the original estimate's 2.03, since entry pulled back closer to invalidation while the target held fixed)
- Stated p = **0.40** (unchanged Tier C default — underlying thesis unchanged from the original PM 09-18 assessment)
- EV = 0.40×24.4% − 0.60×9.6% = **+4.03%** (improved from the original +2.36%)
- Tier: **C** (R≥2, p≥0.40; confluence 7/10 falls short of Tier A's 8/10, p=0.40 falls short of Tier B's 0.45) → size band 5-15%
- Sizing: target 10% (mid-Tier-C), staged half-open this checkpoint = **5% ($513.2116 notional, 4989.4186 POL)**. Second half opens only if confluence holds ≥7/10 at the next checkpoint.

**Runner-up candidates this checkpoint:** none newly competing — ONDO's PM 09-18 arm lapsed this checkpoint (mechanical eased 7/9→5/9 Bullish, capping total confluence at 6/10 regardless of p1); SOL remains confirmed at 7/10 but hard-rule-blocked by the Major L1 sector cap (ETH, TRX unchanged).

**Red-team pass:** Two objections considered before executing.
1. *Is carrying forward a confirmed status from 12+ hours ago, on an unrelated position's exit, too mechanical?* POL's own confluence was independently re-verified this checkpoint (still 7/10 mechanical-only, unchanged in composition from PM 09-18) rather than assumed — this is a fresh confirmation reading, not a stale one being rubber-stamped. Per LESSONS #24's proposed codification, a confirmed candidate whose confluence hasn't dropped below 7/10 in the interim is treated as still qualifying without a fresh 2-checkpoint re-arm; that condition is met here on independently re-checked data.
2. *Sizing math relies on the same $0.128/$0.093 technical levels set 12 hours ago — are they stale?* No material news or technical-structure shift was found for POL between PM 09-18 and this checkpoint (same mixed fundamentals-vs-price narrative persists); the levels are support/resistance-based, not time-decaying, so carrying them forward while refreshing only the entry price (as any staged second-half add already does) is consistent with existing practice.

Net: proceed with a staged half-entry. Sector L2 — POL is the book's only L2 position, no cap issue; DEX drops to 1/5 (JUP only) with ASTER's exit. Book stays at 5/5 positions (ASTER out, POL in) — maximum concurrent per Section 3 rule 1.

## EXIT POST-MORTEM — POL — 2026-09-19 PM (staged-entry non-confirmation)

**P&L:** +$9.6795 realized on the 4989.4186 POL half-tranche (entry $0.10286, exit $0.1048, +1.89%). Realized R +0.1968 vs planned R=2.5497 (a small gain on a fraction of a full position; the second half was never opened). Held ~12 hours.

**Thesis verdict:** Playing Out / Intact at exit — not a thesis failure and not a Bearish-count trigger (0/10 Bearish at both the AM 09-19 entry checkpoint and this PM exit). Closed purely because Section 5's staged-entry mechanic requires confluence to hold ≥7/10 at the immediate next trading checkpoint; it held at 6/10 instead — one parameter short. Per the standing rule (applied identically to AAVE 09-08 PM, ETH/LINK 09-05, ASTER this same morning), no confirmation means the half is cut, not carried forward to wait for a later recovery. Second staged-entry non-confirmation cut of the same trading day.

**Per-parameter verdict at entry (AM 09-19, confluence 7/10, 0/10 Bearish) vs. this checkpoint's exit (6/10, 0/10 Bearish):**
- p1 sentiment: Neutral at both checkpoints — the swing factor was not a flip but a failure to flip *to* Bullish. AM's read was the mixed CMC-AI "consensus leaning bullish but F&G 61 vs. technical-sentiment only ~37% bullish" split; this checkpoint's fresh web-search data (Twitter 41.25%/17.5%/58.75% bullish/bearish/neutral, "comeback excitement" vs. "lingering skepticism" on token utility) was genuinely stronger-tilted than AM's but still majority-neutral with an explicit skeptic voice present — judged not to clear the Bullish bar a second time. This is the parameter that would have supplied the 7th flag.
- p2 DMA, p3 RSI, p6 funding, p7 OI, p9 MVRV: all stayed Bullish, unchanged — golden-cross structure intact, RSI mid-band (59.9), OI still confirming (24h +4.3%, 7d +29.2%), funding/MVRV backdrop unchanged across the one-checkpoint hold.
- p4 rvol: Bullish at both checkpoints (compression/breakout setup continued).
- p5 volz, p8 stables, p10 F&G: Neutral at both checkpoints — never a swing factor.
- No thesis-test condition was breached (invalidation $0.093 never approached within ~13% at either checkpoint; RSI never overbought).

**p calibration:** stated p=0.40 at entry; the position was closed before the probabilistic bet against target/invalidation was ever tested — the staged-entry mechanic intervened on a single-parameter (p1) miss after one checkpoint, consistent with the ASTER/AAVE/ETH/LINK precedents.

**Sizing/timing verdict:** the staged-entry rule did what it is designed to do — capped downside to a half-size tranche ($513.21 notional, 5.0% of portfolio) rather than committing the full 10% target size on a read that held for only one checkpoint. The tranche closed with a small gain rather than a loss, since price (barely) held above entry despite the non-confirmation.

**Counterfactual vs. runner-ups:** no confirmed candidate existed to fill the freed slot this checkpoint — ONDO newly armed at 7/10 (first occurrence, needs AM 09-20 to confirm) and SOL eased to 6/10 (no longer re-verifiable even before considering it remains sector-blocked by the Major L1 2-position cap). The freed slot sits open into AM 09-20. Tracked for the Monday 2026-09-21 shadow-book weekly refresh alongside ASTER's own same-week cut.

**One testable lesson:** two staged-entry non-confirmation cuts landed on the same calendar day (ASTER AM, POL PM), both driven by a sentiment parameter failing to hold/reach Bullish rather than a mechanical (p2-p10) breakdown — in both cases the mechanical base stayed at 5-6/9 Bullish with 0 Bearish, and it was specifically the discretionary p1 judgment call that determined whether the position cleared 7/10. Worth tracking whether requiring the *sentiment* parameter specifically (as opposed to any one of the nine) to hold at the reconfirmation checkpoint is systematically harder than holding a mechanical parameter, given p1 is read contrarian and mixed/split data is deliberately kept Neutral rather than forced. Evidence to confirm: a pattern of staged second-half adds failing specifically on p1 flips/non-flips across several more entries. Evidence to kill: a roughly even split between p1-driven and mechanical-parameter-driven non-confirmations going forward.

## SIGNAL — ONDO armed — 2026-09-19 PM (first occurrence)

Confluence 7/10 Bullish, 0/10 Bearish — first occurrence this checkpoint (was 6/10 at AM 09-19 on the prior lapsed-arm cycle's mechanical base). Mechanical p2-10 held flat at 6/9 Bullish, 0/9 Bearish (golden-cross clean, RSI mid-band 66.6, volz and OI both confirming). p1 sentiment flipped Neutral → Bullish this checkpoint: a web-search fallback read found a real, dated, non-hype catalyst (Ondo Network launch — faster/more-private tokenized-asset trading architecture) plus an "aggressive rally" with a "confirmed breakout from a long-term downtrend" attracting momentum buyers, with no explicit euphoria language and — unlike the same checkpoint's POL read — no significant skeptic/bearish counter-voice surfacing in the data. Not currently held. Needs AM 09-20 to confirm. 1 open slot remains in the book (4/5 positions held post-POL-cut) if ONDO confirms.
