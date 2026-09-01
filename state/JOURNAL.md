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
