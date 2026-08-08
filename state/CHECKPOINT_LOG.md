# CHECKPOINT LOG (append-only)

## CHECKPOINT — 2026-08-02, PM (inception run)

Global params: stablecoins −0.62% 7d ($306.7B, shrinking) | MVRV BTC 1.19 / ETH 0.90 | F&G 27 (Fear, Δ7d +1) | funding regime: near-zero across the board (no crowding either way)
Deployed: 0% across 0 positions | Cash: 100% ($10,000 USDT)
Holdings: none
Signals: armed — none (top counts: ADA 5/10, UNI 5/10, BNB 4, CAKE 4, ENA 4, ONDO 4) | confirmed — none | exit-warned — n/a

Decisions & reasoning:
- Inception checkpoint. No coin reaches the 7/10 gate; nothing armed, nothing traded. With p1 (sentiment) unavoidably Neutral this run, the effective ceiling was 6/10 — and no coin cleared even that.
- Regime read: fear (F&G 27) with SHRINKING stablecoin supply and ETH MVRV < 1. Contrarian-constructive on valuation (p9 Bullish), but liquidity (p8) is Bearish — capital is leaving the sidelines pool, not entering. Correct posture is 100% USDT and patience.
- ADA (5/10): +14.9% 7d breakout with RSI 65, golden state, volume z +1.78 on an up day, OI +13% with price. The closest thing to a setup on the board. Needs sentiment + one more parameter to arm.
- UNI (5/10): +28% 30d, RSI 63, OI +19% with price — but 23.5% above its 50DMA, brushing the overextension line (25%). If it arms via further rally, p2 flips Bearish; self-limiting.
- Mechanical label review: no overrides. PUMP p2 correctly Bearish at +30.8% above 50DMA despite uptrend (overextension rule).

Red-team summary: Strongest case against "do nothing": F&G 27 is close to the contrarian-Bullish band (<25) and MVRV says mid-cycle, not top — waiting could miss a fear-bottom bid in ADA/UNI. Rebuttal: the gate exists precisely so that we don't buy 5/10 boards on regime vibes; shrinking stables mean rallies lack fuel. If the bid is real, counts will rise and the 2-checkpoint sequence will catch it a day late — an acceptable cost.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT, damage $0. No de-risk action possible or needed.

Sector exposure: none (all cash)
Watchlist changes: inception build — 10 permanent (BTC, ETH, BNB, XRP, SOL, TRX, DOGE, ZEC, ADA, LINK) + 20 rotating. Sector-cap note: Major-L1 cap (4) fully consumed by permanents ETH/SOL/ADA/TRX → AVAX/SUI/NEAR blocked from rotating slots. Excluded (red flags): none from knowledge; CryptoPanic headlines unavailable (no API key) — flagged as a data gap.
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-02 PM), this report. JOURNAL/SHADOW_BOOK: nothing to write (no entries, no rejected confirmed-candidates).

Known gaps for next runs: (1) p1 sentiment source not wired — cloud routine should do an X/web sentiment pass per coin near the gate (counts ≥6) and log contrarian reasoning; (2) CryptoPanic key missing; (3) SHIB/PEPE have no Binance USDT perp → p6/p7 read Neutral structurally, their ceiling is 8/10.

## CHECKPOINT — 2026-08-04, AM

Global params: stablecoins −0.47% 7d ($306.9B, shrinking) | MVRV BTC 1.20 / ETH 0.91 | F&G 25 (Fear, Δ7d −4) | funding regime: near-zero to mildly negative across the board (no crowding either way) | futures: fapi.binance.com unreachable (geo-block) — params 6-7 sourced from Hyperliquid fallback for all 30 coins, noted per-coin `futures_source`; p7 (OI Δ) reads null → Neutral for every coin, only ~3 snapshots (~12.7h) of self-built OI_HISTORY.json so far, well short of the 1–7 day threshold.
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none
Signals: armed — none (top mechanical counts: BNB 4/10, ENA 4/10, ONDO 4/10, PEPE 4/10, PUMP 4/10 [entry_blocked — red flag], SHIB 4/10, TRX 4/10, ZEC 4/10) | confirmed — none | exit-warned — n/a

Decisions & reasoning:
- Second checkpoint since inception (first since 2026-08-02 PM; no AM/PM/MID ran on 08-03 — tooling commits only). Nothing was armed at the prior checkpoint, so no coin could confirm today regardless.
- No coin reaches ≥5 mechanical Bullish (p2–p10), so per the Section 0 amendment the Grok/X sentiment pass (`scripts/sentiment.py`) was not triggered this run — there are also no holdings. p1 (sentiment) is logged Neutral for all 30 coins this checkpoint, never fabricated.
- Reviewed all mechanical p2–p10 labels against the Section 7 rubric (raw values in PARAMETERS.json cross-checked against golden-state/RSI/overextension/rvol/volz thresholds for every coin). No overrides warranted — no RSI<30-capitulation-with-intact-thesis cases (RENDER 34.4, TAO 41.8, XLM 39.2, SOL 44.8, LTC 42.2 are all in downtrends without a clean capitulation setup), no overextension mislabels (PUMP correctly Bearish on p2 at +34.7% above 50DMA despite its uptrend).
- LTC and PUMP remain `entry_blocked` (MWEB reorg / class-action + unlock, both flagged 2026-08-03, proposed drop 2026-08-16) — correctly excluded from any arming consideration regardless of count; both scored below the gate anyway (LTC 3/10, PUMP 4/10 mechanical).
- Regime read: F&G 25 sits right on the fear boundary with MVRV<1.2 (not overheated), but stablecoin supply is still shrinking (p8 Bearish globally) — sideline liquidity is not confirming a bottom. Correct posture is unchanged: 100% USDT, patience.

Red-team summary: Strongest case against another do-nothing checkpoint — F&G at 25 and sub-1.2 MVRV argue the market is cheap, and BNB/TRX/ZEC (low-beta, structurally resilient) sit at 4/10 holding up while risk names lag. Rebuttal: none of them clear even half the 7/10 gate, and part of today's ceiling is a structural data gap (p7 OI still null pending Hyperliquid history) rather than a genuine bearish read — lowering the bar to compensate for missing data is exactly the failure mode Section 9 warns against. The 2-consecutive-checkpoint gate exists so a real move gets caught one cycle late at acceptable cost, not chased on a partial board.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — AM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked from 2026-08-03.
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-04 AM), this report, state/BRIEFING.md. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Tuesday).

## CHECKPOINT — 2026-08-04, MID (sourcing)

Global params: stablecoins −0.51% 7d ($306.8B, shrinking) | MVRV BTC 1.20 / ETH 0.91 | F&G 25 (Fear, Δ7d −4) | funding regime: near-zero to mildly negative | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins, p7 (OI Δ) still reads null/Neutral (OI_HISTORY.json short of the 1–7 day threshold).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00). No trading decisions this routine (MID never trades).

Universe build: `scripts/universe.py` → 116 candidates (12 stablecoin/wrapped excluded), enriched top 60 (categories + CoinGecko sentiment votes via COINGECKO_API_KEY).

Scoring & rotation review: Reviewed enriched candidates not on the watchlist (AVAX, SUI, NEAR, DOT, ALGO, ATOM, ICP, WLD, etc. — top by mcap) against catalyst quality / liquidity / no-chase (>50% 7d exclude — none triggered this run, no candidate is even close). None are actionable: **all 20 rotating slots were added 2026-08-02 and remain inside the Section 2 two-week minimum hold (unlocks 2026-08-16)** — no slot-change is legal this run regardless of score, so no scored candidate can displace an incumbent. AVAX/SUI/NEAR remain additionally blocked by the Major-L1 4-per-sector cap (fully consumed by permanents ETH/SOL/ADA/TRX) even after 08-16.

Red-flag screen: fresh web-search pass across all 30 watchlist tickers, news window 2026-07-21 → 2026-08-04. No new hack / regulatory-action / team-exit events found beyond the two already logged (LTC — MWEB exploit/reorg; PUMP — class-action + unlock), both still `entry_blocked`, proposed drop 2026-08-16, unchanged. FYI only, no exclude triggered (wallet-layer not protocol-layer, non-ticker-specific): Coldcard hardware-wallet seed-gen flaw (~$116M drained across BTC addresses) and a minor SOL third-party wallet-phishing wave (~$5.8M) — logged as market-wide security noise, not held against BTC or SOL.

Decisions & reasoning: No watchlist changes this run — mechanically locked by the 2-week minimum, not a judgment call. Refreshed `state/PARAMETERS.json` for all 30 coins so the PM checkpoint starts warm (prices, DMA/RSI/vol/funding/OI recomputed; global block updated).

Sector exposure: none (100% cash)
Watchlist changes (MID only): none — 2-week minimum hold blocks all rotation until 2026-08-16 regardless of scoring. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03).
Simulated fills: n/a
Learning artifacts written: `state/WATCHLIST.json` (updated_utc + notes refreshed, no coin changes), `state/PARAMETERS.json` (full refresh, 30 coins + global), `data/universe.json` (116 candidates), this report, `state/BRIEFING.md`.

## CHECKPOINT — 2026-08-04, PM

Global params: stablecoins −0.46% 7d ($306.9B, shrinking) | MVRV BTC 1.20 / ETH 0.91 | F&G 25 (Fear, Δ7d −4) | funding regime: near-zero to mildly negative across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) mostly reads null/Neutral pending OI_HISTORY.json reaching the 1–7 day threshold.
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- Third checkpoint since inception. Nothing was armed at AM or MID (max mechanical count 4/10 both times), so nothing could confirm today regardless of this run's counts.
- Sentiment pass: ran `scripts/sentiment.py ZEC SHIB PUMP` (the three coins at ≥5 mechanical Bullish this run — no holdings to add). Grok/X pulls for all three showed clear euphoria markers (price-target chasing, rocket-emoji hype, "100x"/"alt szn incoming"/"biggest bull run incoming" posts) with zero capitulation markers — contrarian read is **Bearish** on p1 for all three, logged with one-line reasoning each in SIGNALS.csv. This pulls ZEC and PUMP down to 5/10 bull vs 3 bear, and SHIB to 5/10 bull vs 2 bear — none close the gate.
- Remaining 27 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not fabricated), unchanged from AM/MID.
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric (RSI<30 capitulation-with-intact-thesis scan found zero coins below 30 RSI this run; overextension and rvol/volz thresholds spot-checked against suggested_labels). No overrides warranted.
- LTC and PUMP remain `entry_blocked` (unchanged since 2026-08-03, proposed drop 2026-08-16); PUMP's 5/10 mechanical count is moot for trading regardless of today's read.
- Top board: PUMP/SHIB/ZEC 5/10, then a cluster at 4/10 (ADA, ARB, BNB, ENA, HBAR, ONDO, PEPE, TAO, TRX, UNI, XRP). Nothing within 2 of the 7/10 gate. Regime unchanged: F&G 25 (fear, not yet at the <25 contrarian-Bullish threshold... at the boundary), MVRV sub-1.2 (not overheated), but stablecoin supply still shrinking (p8 Bearish globally) — sideline liquidity isn't confirming a bottom. Correct posture: 100% USDT, patience.

Red-team summary: Strongest case against another do-nothing PM — three coins (PUMP, SHIB, ZEC) cleared 5/9 mechanically and only missed sentiment because the contrarian read caught genuine euphoria; if that euphoria cools without the underlying trend breaking, the mechanical board alone still isn't close to 7/10, so the miss isn't costing much. Rebuttal accepted: none of tonight's candidates are within 2 parameters of the gate even under the most generous read, and PUMP is red-flag entry_blocked besides. No change of posture is defensible.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT, damage $0. No positions to de-risk; cash remains the correct hedge given shrinking stablecoin supply and a fear-leaning but not-yet-capitulating regime.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — PM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked.
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-04 PM, incl. logged p1 sentiment reasoning for ZEC/SHIB/PUMP), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only).

## CHECKPOINT — 2026-08-05, AM

Global params: stablecoins +0.08% 7d ($307.2B, flat/marginally growing — first non-shrinking read since inception) | MVRV BTC 1.22 / ETH 0.91 | F&G 27 (Fear, Δ7d −2) | funding regime: near-zero to mildly negative across the board (no crowding either way) | futures: fapi.binance.com still unreachable (geo-block) — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ 24h) now populated for all coins, p7 OI Δ 7d still null pending OI_HISTORY.json reaching the 7-day threshold.
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count ≥5 this run for ZEC (6/9) and BNB (5/9) — ran `scripts/sentiment.py ZEC BNB`. Both pulls show flat/low-engagement X activity, no euphoria markers, no capitulation markers, no narrative change (ZEC: scattered $470-490 consolidation chat + long-term store-of-value framing; BNB: low-volume price/chain-promo/CZ posts). Neither everyone's-in hype nor capitulation-with-thesis — logged p1 **Neutral** for both with reasoning in SIGNALS.csv, this is a genuine "nothing interesting" read, not a fallback default.
- Remaining 28 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases (lowest RSI this run: XLM 35.4, RENDER 37.2 — both above the 30 threshold, no override candidates). No overextension mislabels (PUMP correctly Bearish on p2 at +47.0% above 50DMA, most extreme dev50 on the board). p8 stablecoin flip to +0.08% correctly reads Neutral under the ±0.1% mechanical band (script threshold), not a strong enough signal to call Bullish yet — noted as a regime watch-item, not an override. No overrides applied this run.
- Final confluence: **ZEC leads at 6/10** (6 bull / 1 bear, p1 Neutral), **BNB second at 5/10** (5 bull / 1 bear, p1 Neutral). Both short of the 7/10 arming bar — no coin arms or confirms this checkpoint. Next tier: ONDO/PUMP/SHIB/TAO/TRX/VIRTUAL all at 4/10. LTC (3/10) and PUMP (4/10, entry_blocked) remain correctly excluded from arming consideration regardless — moot this run since neither reaches the gate anyway.
- Regime read: F&G ticked up to 27 (still Fear-leaning, not yet the <25 contrarian-Bullish threshold), MVRV sub-1.2 on BTC / sub-1.0 on ETH (healthy, not overheated), and stablecoin supply's 7d change turned marginally positive for the first time since inception — a mild tailwind, but +0.08% is noise-level, not a confirmed liquidity-in signal. Correct posture: 100% USDT, patience.

Red-team summary: Strongest case against another do-nothing AM — ZEC at 6/10 is the closest any coin has come to arming since inception, and the stablecoin flow turning positive alongside a slightly-less-fearful F&G could mark the start of a broader bid. Rebuttal: 6/10 is still one full parameter short of even arming (which itself only starts the 2-checkpoint clock), the stablecoin move is within noise of the mechanical Neutral band, and manufacturing a 7th Bullish label to force an arm is exactly the failure mode Section 9 exists to prevent. No change of posture is defensible — hold and let the data clear the bar on its own.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — AM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-05 AM, incl. logged p1 sentiment reasoning for ZEC/BNB), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; today is Wednesday, not the Monday shadow-book refresh; not the first AM of the month, no monthly review due).

## CHECKPOINT — 2026-08-05, MID (sourcing)

Global params: stablecoins −0.04% 7d ($306.9B, essentially flat) | MVRV BTC 1.22 / ETH 0.91 | F&G 27 (Fear, Δ7d −2) | funding regime: near-zero to mildly negative | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins.
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00). No trading decisions this routine (MID never trades).

Universe build: `scripts/universe.py` → 114 candidates (12 stablecoin/wrapped excluded), enriched top 60 (categories + CoinGecko sentiment votes via COINGECKO_API_KEY).

Scoring & rotation review: Reviewed enriched candidates not on the watchlist (GRAM, AVAX, SUI, NEAR, WLFI, ASTER, DOT, SKY, ICP, WLD, ETC, QNT, ALGO, POL, ATOM, etc. — top by mcap) against catalyst quality / liquidity / no-chase (>50% 7d exclude — none triggered; highest non-watchlist 7d mover, DOT at +11.3%, isn't close). No candidate is actionable: **all 20 rotating slots were added 2026-08-02 and remain inside the Section 2 two-week minimum hold (unlocks 2026-08-16)** — no slot-change is legal this run regardless of score. AVAX/SUI/NEAR remain additionally blocked by the Major-L1 4-per-sector cap (fully consumed by permanents ETH/SOL/ADA/TRX) even after 08-16.

Red-flag screen: fresh web-search pass across all 30 watchlist tickers, news window 2026-08-04 → 2026-08-05. No new hack / regulatory-action / team-exit events. LTC and PUMP remain `entry_blocked` (unchanged since 2026-08-03, proposed drop 2026-08-16) — both saw incremental escalation of their *existing* logged incidents, not new triggers: LTC issued a critical MWEB soft fork on 2026-08-04 (miners given 7 days to upgrade, hardens the same validation flaw); PUMP's class action advanced with a RICO case statement plus fresh layoff claims. FYI only, no exclude triggered (governance turnover, not a protocol hack/regulatory action/project-team exit, and not ticker-specific to a single watchlist coin): broad Ethereum Foundation leadership churn (8 senior figures departed over 5 months, including a co-executive director exit) — logged for awareness; ETH is a permanent slot and not subject to rotation/exclude regardless.

Decisions & reasoning: No watchlist changes this run — mechanically locked by the 2-week minimum, not a judgment call. Refreshed `state/PARAMETERS.json` for all 30 coins so the PM checkpoint starts warm (prices, DMA/RSI/vol/funding/OI recomputed; global block updated). Mechanical confluence board (p1 sentiment excluded, judgment-only at trading checkpoints): ZEC leads 6/9, UNI and BNB 5/9, then a 4/9 cluster (TRX, SHIB, PUMP, TAO, SOL, ONDO, ENA) — unchanged leadership from this morning's AM checkpoint, nothing new to flag ahead of PM.

Sector exposure: none (100% cash)
Watchlist changes (MID only): none — 2-week minimum hold blocks all rotation until 2026-08-16 regardless of scoring. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03).
Simulated fills: n/a
Learning artifacts written: `state/WATCHLIST.json` (updated_utc + notes refreshed, no coin changes), `state/PARAMETERS.json` (full refresh, 30 coins + global), `data/universe.json` (114 candidates), this report, `state/BRIEFING.md`.

## CHECKPOINT — 2026-08-05, PM

Global params: stablecoins −0.02% 7d ($307.2B, essentially flat) | MVRV BTC 1.22 / ETH 0.91 | F&G 27 (Fear, Δ7d −2) | funding regime: near-zero to mildly positive across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 OI Δ 7d still null pending OI_HISTORY.json reaching the 7-day threshold.
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count ≥5 this run for ZEC (6/9), BNB (6/9), PEPE (5/9), UNI (5/9) — ran `scripts/sentiment.py ZEC BNB PEPE UNI`. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **ZEC → Bearish**: euphoria markers present (price-target chasing $512-530, "incredibly bullish", "looks great"), zero capitulation. Narrative also carries an unverified red-flag claim (an Orchard exploit attempt, reportedly caught by whitehats) — not a confirmed hack, so no watchlist exclude triggered, but flagged for the next MID red-flag screen.
  - **BNB → Neutral**: genuinely mixed — bullish-structure calls offset by dismissive/bearish posts ("BNB called shit due to MEV issues," rotate to SOL) and "bearish distribution" chatter. Neither euphoria nor capitulation dominates.
  - **PEPE → Bearish**: textbook meme-coin euphoria (new-ATH calls, "3x-5x is all I see," rocket emojis), zero capitulation markers.
  - **UNI → Bullish**: zero euphoria and zero capitulation despite UNI +97%/month — discussion is fundamentals-driven (fee-switch buybacks live, token burns, V4/RWA shipping, Robinhood Chain integration). Matches "improving interest without euphoria" cleanly; a genuine bullish p1 read, not a default.
- Remaining 26 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases (lowest RSI this run: RENDER 33.4, XLM 36.7 — both above the 30 threshold). PUMP correctly Bearish on p2 at +44.6% above 50DMA (most extreme dev50 on the board, overextension rule). Funding reads Bullish across the board (all near-zero-to-capped-positive, well under the 0.05%/8h crowded-longs threshold) — consistent with prior checkpoints, no anomaly. No overrides applied this run.
- Final confluence: **BNB, UNI, and ZEC tie at 6/10** (BNB 6 bull/0 bear, UNI 6 bull/0 bear, ZEC 6 bull/1 bear). All short of the 7/10 arming bar — no coin arms or confirms this checkpoint (AM's board also topped out at 6/10 with none armed, so there was no "second consecutive" possibility regardless). Next tier: DOGE/VIRTUAL/TAO/SOL/PUMP/ONDO/TRX/SHIB/ETH/ENA all at 4/10.
- Regime read: F&G 27 (Fear-leaning, not yet the <25 contrarian-Bullish threshold), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply flipped back to essentially flat/marginally negative (−0.02%, noise-level, not a confirmed liquidity-in signal). Correct posture: 100% USDT, patience.

Red-team summary: Strongest case against another do-nothing PM — three separate coins (BNB, UNI, ZEC) now sit at 6/10, the closest the board has been to arming since inception, and UNI's p1 read is a genuine, not-manufactured Bullish on real fundamental catalysts (fee switch, burns, V4). Rebuttal: 6/10 is still one full parameter short of even arming, and manufacturing a 7th Bullish label on any of the three (e.g. squinting at BNB's p2 DMA position or ZEC's p5 volume z-score) to force an arm is exactly the failure mode Section 9 exists to prevent. Two of the three closest candidates (ZEC, PEPE) got pulled down specifically because contrarian sentiment caught real euphoria — that's the system working, not a miss. No change of posture is defensible — hold and let the data clear the bar on its own.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT, damage $0. No positions to de-risk; cash remains the correct hedge given a still-fear-leaning regime, flat (not clearly growing) stablecoin sidelines, and no coin within one parameter of the entry gate.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — PM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16). ZEC's unverified Orchard-exploit claim (caught by whitehats per the sentiment pull) is not a confirmed hack — no exclude triggered, flagged for the next MID news screen to verify.
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-05 PM, incl. logged p1 sentiment reasoning for ZEC/BNB/PEPE/UNI), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only).

## CHECKPOINT — 2026-08-06, AM

Global params: stablecoins +0.23% 7d ($307.7B, growing) | MVRV BTC 1.23 / ETH 0.93 | F&G 25 (Fear, Δ7d −3) | funding regime: near-zero across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still reads null pending OI_HISTORY.json reaching the 7-day threshold (24h deltas are populated and used).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count (p2–p10) ≥5 this run for BNB, TRX, ZEC, ENA, ONDO, SHIB, VIRTUAL (5/9 each) — ran `scripts/sentiment.py BNB TRX ZEC ENA ONDO SHIB VIRTUAL`. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **BNB → Neutral**: interest trend falling, zero euphoria/capitulation markers, scattered low-engagement chatter. No crowd extremity either direction.
  - **TRX → Neutral**: interest flat (not improving), zero euphoria/capitulation markers — fundamentals chatter (JustLend staking, MoonPay gasless tx) doesn't clear the "improving interest" bar on its own.
  - **ZEC → Bearish**: euphoria markers present (price targets $3,900–8,000 vs BTC, "hype zec pump"), zero capitulation. Same euphoria pattern flagged 2026-08-05 PM, persisting.
  - **ENA → Bearish**: rising interest with clear euphoria markers (rocket emojis on accumulation posts, "whales piling in," Arthur Hayes conviction narrative dominant) — crowd-follows-whales hype outweighs the lone fee-switch criticism (a capitulation-flavored counter-marker, but not dominant).
  - **ONDO → Neutral**: interest falling, zero euphoria/capitulation markers, low-volume promotional/TA chatter only.
  - **SHIB → Neutral**: interest flat, zero euphoria/capitulation markers — chart-pattern and burn-stat chatter, no crowd extremity.
  - **VIRTUAL → Neutral**: interest flat, zero euphoria/capitulation markers — mixed TA calls (one bearish-trend note), no crowd extremity.
- Remaining 23 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases this run (lowest RSI: XLM 32.1, RENDER 33.6 — both above the 30 threshold, no override). No overextension mislabels (PUMP correctly Bearish on p2 at +38.0% above 50DMA, the most extreme dev50 on the board; SHIB's +21.0% dev50 stays under the 25% cap, correctly Bullish). Funding reads Bullish across the board (all near-zero, well under the 0.05%/8h crowded-longs threshold), consistent with prior checkpoints. No overrides applied this run.
- Final confluence: **BNB, ENA, ONDO, SHIB, TRX, VIRTUAL, ZEC all tie at 5/10** (BNB/ONDO/SHIB/TRX 5 bull/0 bear; VIRTUAL 5 bull/1 bear; ENA/ZEC 5 bull/2 bear — the two coins where the contrarian sentiment flip cost them a clean board). All well short of the 7/10 arming bar; no coin arms or confirms this checkpoint. PM's 08-05 board topped out at 6/10 with nothing armed, so no "second consecutive" possibility existed regardless. Next tier: a broad cluster at 4/10 (AAVE, ADA, ARB, BCH, DOGE, ETH, FIL, HBAR, JUP, MORPHO, PEPE, PUMP, SOL, TAO, UNI, XLM, XRP).
- Regime read: F&G 25 sits back at the fear boundary (Δ7d −3, falling — not yet the "rising from <30" contrarian-Bullish pattern), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply flipped back to growing (+0.23% 7d, a reversal from PM's flat/marginal-negative read) — a mild liquidity-in signal but not yet a strong one. Correct posture: 100% USDT, patience.

Red-team summary: Strongest case against another do-nothing AM — seven coins now cluster at 5/10 with clean mechanical boards (four of them 5/0, no bearish parameter at all), and stablecoin supply just turned positive after two checkpoints of flat/negative — a first hint the liquidity picture may be turning. Rebuttal: 5/10 is two full parameters short of arming, and the four cleanest names (BNB, ONDO, SHIB, TRX) are clean specifically because they're unremarkable — flat sentiment, no catalyst, no volume conviction (p4/p5 mostly Neutral) — not because they're building toward a breakout. Manufacturing urgency from a one-day stablecoin uptick, before it's even confirmed as a trend, is the action-bias failure mode Section 9 warns against. Hold and let the data clear the bar on its own.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — AM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-06 AM, incl. logged p1 sentiment reasoning for BNB/TRX/ZEC/ENA/ONDO/SHIB/VIRTUAL), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Thursday).

## CHECKPOINT — 2026-08-06, MID

Global params (refreshed): stablecoins +0.27% 7d ($307.8B, growing) | MVRV BTC 1.23 / ETH 0.93 | F&G 25 (Fear, Δ7d −3) | funding regime: near-zero across the board | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still null pending OI_HISTORY.json reaching the 7-day threshold.

Step 1 — Universe: `scripts/universe.py` rerun. 113 candidates (12 stablecoin/wrapped excluded), top 60 enriched with CoinGecko categories + community sentiment votes.

Step 2/3 — Data cards & scoring: Reviewed top ~25 non-watchlist candidates by market-cap rank plus a full 7d-change sweep for chasers. No-chase check clean — zero candidates (watchlist or not) at >50% 7d gain this run. Top non-watchlist names unchanged from prior runs: AVAX/SUI/NEAR/DOT/ALGO/ATOM (all L1-tagged, blocked by the Major-L1 4-per-sector cap already filled by ETH/SOL/ADA/TRX permanents) and WLFI/ASTER (uncapped sectors, but score below the current DeFi-Lending/DEX rotating names on catalyst quality). Red-flag web screen (window 2026-08-05 to 2026-08-06) across all 30 watchlist tickers plus top candidates: no new hack/regulatory/team-exit events found.
  - LTC: MWEB root-cause fix confirmed deployed (patches the spring 2026 exploit family behind the 2026-08-03 incident). Incident stays logged; LTC stays `entry_blocked` — a deployed fix doesn't reverse an active block mid-cycle, per the 2-week-minimum hold. Drop review remains 2026-08-16.
  - PUMP: class-action status unchanged (pre-SAC-deadline, no new filing this window). Stays `entry_blocked`, drop review 2026-08-16.
  - ZEC: the "Orchard exploit" chatter flagged by sentiment.py in the 2026-08-05 PM checkpoint was run down — it references the already-disclosed, already-patched June 2026 Orchard counterfeiting bug (fixed 2026-06-01, no evidence it was ever exploited). Recycled old news, not a new incident. No exclude triggered.
  - FYI-only, no exclude (not ticker-specific to any watchlist protocol): broad crypto team-exit headlines this window (1inch co-founder firing, Polygon layoffs) — neither POL nor 1inch's token is on the watchlist.

Step 4 — Watchlist reassembly: **No changes.** All 20 rotating slots were added 2026-08-02 and remain inside the 2-week minimum hold (unlocks 2026-08-16) — no drops or adds are legal this run regardless of scoring, identical to the 2026-08-05 MID conclusion. 10 permanents untouched. `slot_changes_this_week` stays 0.

Step 5 — Parameters refresh: `scripts/parameters.py` rerun for all 30 coins + global block → `state/PARAMETERS.json` updated, PM checkpoint starts warm. Mechanical suggested-label sweep (p2–p10, pre-sentiment) tops out at 5/9 this run (TRX, ONDO, ENA — ENA carrying 1 mechanical Bearish on p7 OI), consistent with AM's post-sentiment board (also topped at 5/10: BNB/ONDO/SHIB/TRX/VIRTUAL clean, ENA/ZEC at 5/10 with 2 Bearish). No trading decisions taken (MID routine, per Section 6).

Watchlist changes: none. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, drop proposed 2026-08-16).
Learning artifacts written: `state/WATCHLIST.json` (notes updated with this run's screen), `state/PARAMETERS.json` (refreshed), this report, `state/BRIEFING.md`.

## CHECKPOINT — 2026-08-06, PM

Global params: stablecoins +0.30% 7d ($308.0B, growing) | MVRV BTC 1.23 / ETH 0.93 | F&G 25 (Fear, Δ7d −3) | funding regime: near-zero across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still reads null pending OI_HISTORY.json reaching the 7-day threshold (24h deltas populated and used).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count (p2–p10) ≥5 this run for ADA, ENA, ONDO, PUMP, TRX, ZEC (5/9 each) — ran `scripts/sentiment.py TRX ZEC ADA ENA ONDO PUMP`. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **TRX → Neutral**: interest flat (not improving), zero euphoria/capitulation markers — fundamentals chatter (Tron Inc. treasury buys, MoonPay gasless USDT, ETF filing) doesn't clear the "improving interest" bar on its own.
  - **ZEC → Neutral**: interest flat, zero euphoria markers this window (no price-target chasing found, unlike the 08-05 PM / 08-06 AM reads) and zero capitulation markers — narrative is tactical short/reversal trade chatter plus a P2P milestone post, no crowd extremity either direction. Flagging the discontinuity: prior two checkpoints read ZEC Bearish on euphoria; this window's pull genuinely shows none, so the label follows the evidence rather than the streak.
  - **ADA → Bearish**: euphoria markers present (rocket-emoji breakout targets to $0.23, 240M-ADA whale-buy hype) despite only +25% weekly — price-target chasing and whale-following narrative reads as building euphoria, not clean accumulation.
  - **ENA → Bearish**: euphoria markers (price targets $0.13–0.14, rocket emojis, bullish reversal setups) outweigh a couple of tactical short posts — whale-staking hype ("40M ENA, $3.7M") plus TA-target chasing reads as crowd-following, not capitulation.
  - **ONDO → Neutral**: interest falling, zero euphoria/capitulation markers — mixed low-conviction chatter (Genesis Badge deadline notice, one +16% TA post, one consolidation call), no crowd extremity.
  - **PUMP → Bearish**: euphoria markers (rocket emojis, 52% rally claims, breakout price targets, bull-breakout language) on a coin already `entry_blocked` for red-flag/class-action reasons — clear crowd chasing, zero capitulation markers. Sentiment result is moot for entry (still blocked) but scored for shadow-book/parameter-scorecard completeness.
- Remaining 24 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases this run (lowest RSI: BTC 51.9 region typical, no coin under 30). ADA's RSI 71.6 sits just above the 55–70 Bullish band but short of the 75 Bearish threshold — correctly Neutral, no override. PUMP correctly Bearish on p2 at +39.7% above 50DMA (most extreme dev50 on the board, overextension rule). Funding reads Bullish across the board (all near-zero, well under the 0.05%/8h crowded-longs threshold), consistent with prior checkpoints. No overrides applied this run.
- Final confluence: **ADA, ENA, ONDO, PUMP, TRX, ZEC all tie at 5/10** (ONDO/TRX 5 bull/0 bear clean; ADA/ENA/ZEC 5 bull/1 bear; PUMP 5 bull/2 bear, and separately `entry_blocked` regardless). All well short of the 7/10 arming bar; no coin arms or confirms this checkpoint. AM's board also topped out at 5/10 with nothing armed, so no "second consecutive" possibility existed regardless. Next tier: a broad cluster at 4/10 (AAVE, ARB, BCH, BNB, DOGE, ETH, FIL, HBAR, JUP, MORPHO, PEPE, SHIB, SOL, TAO, UNI, VIRTUAL, XLM).
- Regime read: F&G 25 unchanged from AM (Δ7d −3, still falling, not yet the "rising from <30" contrarian-Bullish pattern), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply +0.30% 7d (marginal continuation of the AM's mild growth read, still not a strong liquidity-in signal). Correct posture: 100% USDT, patience.

Red-team summary: Strongest case against a third straight do-nothing checkpoint — six coins now cluster at 5/10, unchanged in count from AM but with the composition shifting (ADA joins the group, ZEC's sentiment read flipped from Bearish to Neutral on genuinely different evidence, not manufactured drift) — the board is stable, not deteriorating, and stablecoin supply has now posted two consecutive positive readings. Rebuttal: 5/10 is still two full parameters short of arming, and both "clean" names (ONDO, TRX) are clean because they're quiet (falling/flat interest, no catalyst, Neutral RSI/volume) — not because they're building toward a breakout. Two consecutive positive stablecoin prints is thin evidence (+0.27%, +0.30%) for a trend call, and forcing a parameter to Bullish to close the gap on any of these six is exactly the failure mode Section 9 exists to prevent. Hold and let the data clear the bar on its own.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT, damage $0. If this were to hit while the current 5/10 cluster (ADA/ENA/ONDO/PUMP/TRX/ZEC) were instead a live 5-position book, correlation to BTC would be the default assumption per Section 9 and all five would likely draw down together regardless of their individual confluence reads — a reminder that the cash stance is not just "no signal yet" but also a structural hedge against the single scenario that damages the most positions at once. No de-risking action needed today; cash remains the correct posture given a still fear-leaning regime, only marginally growing stablecoin sidelines, and no coin within two parameters of the entry gate.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — PM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-06 PM, incl. logged p1 sentiment reasoning for TRX/ZEC/ADA/ENA/ONDO/PUMP), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Thursday).

## CHECKPOINT — 2026-08-07, AM

Global params: stablecoins +0.47% 7d ($307.7B, growing) | MVRV BTC 1.22 / ETH 0.93 | F&G 29 (Fear, Δ7d +4) | funding regime: near-zero across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still reads null pending OI_HISTORY.json reaching the 7-day threshold (24h deltas populated and used).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count (p2–p10) ≥5 this run for ENA, ETH, LTC, ONDO, TRX, ZEC (5/9 each) — ran `scripts/sentiment.py ETH TRX ZEC ENA ONDO LTC`. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **ETH → Neutral**: interest flat, no euphoria markers; critical/skeptical commentary (L2 revenue capture, monetary-policy changes) reads as persistent skepticism, not acute capitulation — no fear-extremity language, doesn't clear either bar.
  - **TRX → Neutral**: interest falling, zero euphoria/capitulation markers — routine fundamentals chatter (MoonPay gasless tx, JustLend staking yield), no crowd extremity.
  - **ZEC → Neutral**: interest falling, zero euphoria markers, one throwaway capitulation-adjacent joke in an otherwise sparse/spam-heavy feed — not enough signal to call capitulation.
  - **ENA → Bearish**: euphoria markers persist (price targets to $0.14, rocket emojis, bullish reversal setups, whale-staking hype) despite flat interest — same chasing pattern as the last two checkpoints, third straight Bearish read.
  - **ONDO → Neutral**: interest flat, zero euphoria/capitulation markers — fundamentals narrative (228k+ holders, RWA expansion) plus routine TA, no crowd extremity.
  - **LTC → Bearish**: euphoria markers (multi-year wedge targets to $55-130, rocket emojis, "build up a stack" language) outweigh coexisting Extreme-Fear/bearish-lean TA chatter — outsized upside-target chasing reads as the dominant crowd behavior. Entry_blocked (red-flag) regardless; scored for shadow-book/parameter-scorecard completeness only.
- Remaining 24 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases this run (lowest RSI: XLM 32.5, RENDER 33.9 — both above the 30 threshold). No overextension mislabels (PUMP correctly Bearish on p2 at +34.1% above 50DMA, the most extreme dev50 on the board; ADA's +20.7% dev50 stays under the 25% cap, correctly Neutral). Funding reads Bullish/near-zero across the board (MORPHO's -0.03%/8h is the most negative print, well short of "deeply negative" contrarian territory), no crowding either way. F&G sits at 29 with a +4 7d rise — checked against the "rising from <30" Bullish criterion, but the script's own delta threshold (>5) isn't cleared by a 4-point move; a weak, sub-threshold uptick doesn't warrant overriding to Bullish, left Neutral. No overrides applied this run.
- Final confluence: **ENA, ETH, LTC, ONDO, TRX, ZEC all tie at 5/10** (ETH/ONDO/TRX 5 bull/0 bear clean; LTC/ZEC 5 bull/1 bear; ENA 5 bull/2 bear). All well short of the 7/10 arming bar; no coin arms or confirms this checkpoint. PM's 08-06 board also topped out at 5/10 with nothing armed, so no "second consecutive" possibility existed regardless. Next tier: a broad cluster at 4/10 (12 coins spanning AAVE, ADA, ARB, BCH, BTC, DOGE, FIL, HBAR, PEPE, PUMP, SOL, TAO, UNI, VIRTUAL, XLM — 15 total).
- Regime read: F&G 29 ticked up from 25 (Δ7d now +4 vs prior −3 — a genuine reversal off the recent low, though still shy of the script's own "rising" confirmation threshold), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply +0.47% 7d (third consecutive positive print, the largest of the three — a strengthening liquidity-in signal). Correct posture remains 100% USDT, patience.

Red-team summary: Strongest case against a fourth straight do-nothing checkpoint — six coins now cluster at 5/10 (ETH newly joins, replacing ADA/PUMP from PM's cluster), F&G has reversed off its low for the first time in over a week, and stablecoin supply has now posted three consecutive positive prints with accelerating magnitude (+0.27%, +0.30%, +0.47%) — a plausible early liquidity-rotation signal building across the last several checkpoints, not just noise. Rebuttal: 5/10 is still two full parameters short of arming, and the three cleanest names (ETH, ONDO, TRX) are clean because they're quiet — flat/falling sentiment interest, no catalyst, Neutral RSI/volume — not because they're building toward a breakout. A three-print stablecoin trend is real but still small in absolute terms (7d Δ well under 1%), and F&G rising 4 points off 25 is not yet the sharp reversal the rubric rewards. Forcing any of these six to a 7th Bullish parameter today would be exactly the failure mode Section 9 warns against. Hold and let the data clear the bar on its own — but flag the liquidity trend explicitly for the next checkpoint's review, since three consecutive prints is the kind of pattern worth tracking closely.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — AM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-07 AM, incl. logged p1 sentiment reasoning for ETH/TRX/ZEC/ENA/ONDO/LTC), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Friday).

## CHECKPOINT — 2026-08-07, MID

Global params (refreshed): stablecoins +0.44% 7d ($307.7B, growing) | MVRV BTC 1.22 / ETH 0.93 | F&G 29 (Fear, Δ7d +4) | funding regime: near-zero across the board | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still null pending OI_HISTORY.json reaching the 7-day threshold.

Step 1 — Universe: `scripts/universe.py` rerun. 117 candidates (12 stablecoin/wrapped excluded), top 60 enriched with CoinGecko categories + community sentiment votes.

Step 2/3 — Data cards & scoring: Reviewed top 40 non-watchlist candidates by market-cap plus a full 7d-change sweep for chasers. No-chase check clean — zero candidates (watchlist or not) at >50% 7d gain this run (ALGO +13.8% and ZRO +13.2% are the highest prints, well under threshold). Top non-watchlist names unchanged from prior runs: AVAX/SUI/NEAR/DOT/ALGO/ATOM (all L1-tagged, blocked by the Major-L1 4-per-sector cap already filled by ETH/SOL/ADA/TRX permanents) and WLFI/ASTER (uncapped sectors, but score below the current DeFi-Lending/DEX rotating names on catalyst quality). Red-flag web screen (window 2026-08-06 to 2026-08-07) across all 30 watchlist tickers plus top candidates: no new hack/regulatory/team-exit events found on any watchlist ticker. Broad sweep surfaced only items outside the watchlist entirely — Coinbase leadership reshuffle (4 execs), BitMEX ceasing operations Sept 23, Drift Protocol $286M suspected-DPRK hack (none are watchlist protocols).
  - LTC: no update this window. Stays `entry_blocked` (MWEB reorg incident, 2026-08-03), drop review remains 2026-08-16.
  - PUMP: class-action escalated — a whistleblower surfaced 5,000+ internal messages alleging coordinated MEV/market rigging, feeding a second amended complaint. Escalation of the existing incident, not a new one. Stays `entry_blocked`, drop review remains 2026-08-16.

Step 4 — Watchlist reassembly: **No changes.** All 20 rotating slots were added 2026-08-02 and remain inside the 2-week minimum hold (unlocks 2026-08-16) — no drops or adds are legal this run regardless of scoring, identical to the 2026-08-05 and 2026-08-06 MID conclusions. 10 permanents untouched. `slot_changes_this_week` stays 0.

Step 5 — Parameters refresh: `scripts/parameters.py` rerun for all 30 coins + global block → `state/PARAMETERS.json` updated, PM checkpoint starts warm. Mechanical suggested-label sweep (p2–p10, pre-sentiment) tops out at 6/9 this run (ZEC, carrying 1 mechanical Bearish on p5 volume z-score), with BTC/ETH/TRX/ADA/ENA/ONDO/BCH clustered at 5/9 clean. Broadly consistent with AM's post-sentiment board (topped at 5/10: ENA/ETH/LTC/ONDO/TRX/ZEC). No trading decisions taken (MID routine, per Section 6).

Watchlist changes: none. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, drop proposed 2026-08-16).
Learning artifacts written: `state/WATCHLIST.json` (notes updated with this run's screen), `state/PARAMETERS.json` (refreshed), `data/universe.json` (refreshed), this report, `state/BRIEFING.md`.

## CHECKPOINT — 2026-08-07, PM

Global params: stablecoins +0.50% 7d ($307.9B, growing) | MVRV BTC 1.22 / ETH 0.93 | F&G 29 (Fear, Δ7d +4) | funding regime: near-zero across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still reads null pending OI_HISTORY.json reaching the 7-day threshold (24h deltas populated and used).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count (p2–p10) ≥5 this run for ETH, TRX, ZEC (5, 5, 6 respectively) — ran `scripts/sentiment.py ETH TRX ZEC`. No holdings, so no additional tickers required. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **ETH → Neutral**: interest flat, no euphoria markers — mixed low-conviction technical chatter (EIP-8361 burn-proposal debate, bearish-below-trendline calls, one bullish burn-momentum post), no crowd extremity either direction.
  - **TRX → Bullish**: interest trend flipped to *rising* this window (Canary Capital Staked TRX ETF filing, S&P crypto index inclusion, best-DCA-since-2022 stat) with zero euphoria markers — a clean "improving interest without euphoria" read per the p1 rubric. First Bullish p1 for TRX after two straight flat/falling reads; genuinely new evidence (ETF filing + index inclusion), not manufactured drift.
  - **ZEC → Bearish**: euphoria markers present (10x price-target chatter, "$500 buy calls", bullish-AI-stock framing) despite flat overall interest — crowd chasing upside on thin volume, not capitulation. Reverses PM 08-06's/AM 08-07's Neutral read on new evidence (this window surfaced target-chasing language the prior two windows didn't).
- Remaining 27 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases this run (lowest RSI: XLM 31.6, RENDER 32.3 — both above the 30 threshold). No overextension mislabels (PUMP correctly Bearish on p2 at +36.4% above 50DMA, the most extreme dev50 on the board; ADA's +19.9% dev50 stays under the 25% cap, correctly Neutral). Funding reads Bullish across the board except no coin crosses the >0.05%/8h crowded-longs threshold; JUP's -0.0818%/8h correctly reads Bullish (deeply negative, contrarian crowded-shorts case). No overrides applied this run.
- Final confluence: **TRX and ZEC both reach 6/10** (TRX 6 bull/0 bear clean; ZEC 6 bull/0 bear clean — ZEC's p5 volume-z flipped from Bearish to Neutral vs PM 08-06, and p1 flipped Bullish→Bearish on the new euphoria evidence, netting the same 6). **ETH sits at 5/10** (5 bull/1 bear, p7 OI Bearish on Hyperliquid's -17.8% 24h OI print against a rising price). All three well short of the 7/10 arming bar; no coin arms or confirms this checkpoint — AM's board also topped out at 5/10 with nothing armed, so no "second consecutive" possibility existed regardless. Next tier: XRP at 3 bull/3 bear (mixed, not a setup); a broad cluster at 4/10 spans 22 other coins.
- Regime read: F&G 29 unchanged from AM/MID (Δ7d +4, a genuine reversal off the recent low but still shy of the script's own "rising" confirmation threshold), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply +0.50% 7d (fourth consecutive positive print, continuing the mild liquidity-in trend flagged at AM). Correct posture remains 100% USDT, patience.

Red-team summary: Strongest case against a fifth straight do-nothing checkpoint — TRX and ZEC have both cleared 6/10 for the first time this week, TRX on a genuinely new institutional catalyst (ETF filing, index inclusion) rather than noise, and stablecoin supply has now posted four consecutive positive prints. A case could be made that TRX's p1 flip plus a friendly regime is "close enough" to force an eighth override. Rebuttal: 6/10 is still one full parameter short of the gate, and the rule exists precisely to prevent "close enough" from becoming a trade — TRX's remaining Neutral parameters (RSI 49.9, volume-z -1.26, OI flat) show a quiet, non-committal tape underneath the one positive catalyst, not a broadening bullish picture. ZEC's Bearish p1 this run is a reason for caution, not comfort, despite the raw 6/10 count. No coin is within striking distance of two consecutive 7/10 checkpoints; forcing either would be exactly the failure mode Section 9 exists to prevent. Hold and let the data clear the bar on its own.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT, damage $0. If this were to hit while TRX/ZEC (the current 6/10 leaders) were instead a live 2-position book, correlation to BTC would be the default assumption per Section 9 and both would likely draw down together regardless of their individual confluence reads — the cash stance remains both "no signal yet" and a structural hedge against the single scenario that damages the most positions at once. No de-risking action needed today; cash remains the correct posture given a still fear-leaning regime (F&G 29), a modestly growing but still-thin stablecoin sideline, and no coin within one parameter of the entry gate.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — PM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-07 PM, incl. logged p1 sentiment reasoning for ETH/TRX/ZEC), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Friday).

## CHECKPOINT — 2026-08-08, AM

Global params: stablecoins +0.29% 7d ($307.3B, growing) | MVRV BTC 1.23 / ETH 0.94 | F&G 30 (Fear, Δ7d +3) | funding regime: near-zero across the board (no crowding either way) | futures: fapi.binance.com still geo-blocked — params 6-7 sourced from Hyperliquid fallback for all 30 coins; p7 (OI Δ) 7d still reads null pending OI_HISTORY.json reaching the 7-day threshold (24h deltas populated and used).
Deployed: 0% across 0 positions | Cash: 100% ($10,000.00)
Holdings: none

Decisions & reasoning:
- No holdings to review (Section 5 step 4 n/a).
- Sentiment pass: mechanical count (p2–p10) ≥5 this run for ETH, BNB, SOL, TRX, ZEC, UNI, ONDO, PEPE, TAO (all 5/9, ZEC 6/9) — ran `scripts/sentiment.py ETH BNB SOL TRX ZEC UNI ONDO PEPE TAO`. Contrarian reads, logged with reasoning in SIGNALS.csv:
  - **ETH → Neutral**: interest flat; euphoria markers are isolated pump-signal-account chatter, not broad crowd extremity; dominant narrative is routine TA/ETF notes.
  - **BNB → Neutral**: interest flat, genuinely mixed chatter (breakout bulls vs RSI-bearish short-setup calls in roughly equal measure) — no crowd extremity either direction.
  - **SOL → Bullish**: capitulation markers dominant ("beautiful corpse" down 40% from peak, "everyone calling it dead at $73", fear-index-25 framing) while on-chain signals stay intact (62k dormant wallets waking with $2B memecoin volume, SGP-0003 burns, Take-Two listing, Solana Pay adoption) — textbook capitulation-while-thesis-intact contrarian Bullish.
  - **TRX → Neutral**: interest flat, zero euphoria/capitulation markers this window — pure support/resistance TA chatter. PM 08-07's ETF-filing catalyst is absent from this window, so the read reverts from that checkpoint's Bullish back to Neutral on the new evidence (not manufactured drift — the catalyst chatter genuinely isn't present today).
  - **ZEC → Bearish**: euphoria markers persist (multiple long-signal TP posts, "less risky at $500 now than $50 last year" reframing of a 10x run as safe) outweighing a mild hopium-warning caveat — crowd still chasing/justifying upside on a name already +9.7% 7d. Continues PM 08-07's Bearish read on materially the same evidence pattern.
  - **UNI → Neutral**: interest flat, no euphoria; mild fading-enthusiasm chatter ("bear season, trading elsewhere") isn't capitulation panic — no crowd extremity either direction.
  - **ONDO → Neutral**: interest falling but the single capitulation-adjacent line ("people dumping while product scales") is thin next to routine dip-buy entries and a product-scaling narrative (tokenised COIN on MEXC) — not a dominant capitulation signal.
  - **PEPE → Neutral**: interest flat, no euphoria or capitulation markers — mixed bull/bear TA calls, routine low-engagement chatter.
  - **TAO → Bearish**: euphoria markers dominant — rocket-emoji shill posts, price-target chasing ("$193 will look ridiculous in future"), repeated "heavy conviction" thesis-affirmation — crowd re-affirming a long-held bullish narrative, no capitulation markers to counter it.
- Remaining 21 coins: mechanical count <5 and no holdings, so per the Section 0 amendment p1 stays Neutral (not triggered, not fabricated).
- Mechanical label review: checked all 30 coins' raw values against the Section 7 rubric. No RSI<30 capitulation-with-intact-thesis cases this run (lowest RSI: RENDER 33.5, XLM 34.4 — both above the 30 threshold). No overextension mislabels (PUMP correctly Bearish on p2 at +31.4% above 50DMA, the most extreme dev50 on the board; ADA's +19.0% dev50 stays under the 25% cap, correctly Neutral). Funding reads Bullish/near-zero across the board (MORPHO's -0.0599%/8h is the most negative print, already correctly flipped Bullish as contrarian crowded-shorts — not yet "deeply negative" outlier territory beyond that). F&G sits at 30 with a +3 7d rise — checked against the "rising from <30" Bullish criterion, but the current value is at the boundary (not clearly <30) and the delta is sub-threshold; left Neutral, consistent with the last several checkpoints' treatment of this same borderline read. No overrides applied this run.
- Final confluence: **SOL and ZEC both reach 6/10** (SOL 6 bull/1 bear on a fresh contrarian-Bullish p1; ZEC 6 bull/2 bear, continuing its Bearish p1 trend). **BNB, TRX, UNI sit at 5/10 clean** (5 bull/0 bear); **ETH, ONDO, PEPE at 5/10** (5 bull/1 bear); **TAO at 5/10** (5 bull/2 bear). All well short of the 7/10 arming bar; no coin arms or confirms this checkpoint — PM 08-07's board also topped out at 6/10 (TRX/ZEC) with nothing armed, so no "second consecutive" possibility existed regardless. Next tier: a broad cluster at 4/10 spans 17 coins; XRP sits at 3 bull/3 bear (mixed, not a setup).
- Regime read: F&G 30 ticked up from 29 (Δ7d now +3, still a mild reversal off the recent low but shy of a decisive move), MVRV sub-1.25 BTC / sub-1.0 ETH (healthy, not overheated — p9 Bullish), stablecoin supply +0.29% 7d — a deceleration from PM 08-07's +0.50% (fourth-consecutive-positive-print streak continues but the magnitude shrank, tempering the "building liquidity rotation" read flagged over the last two days). Correct posture remains 100% USDT, patience.

Red-team summary: Strongest case against a sixth straight do-nothing checkpoint — SOL and ZEC have both cleared 6/10, SOL on a genuinely fresh contrarian sentiment read (capitulation-while-thesis-intact, not manufactured), and the stablecoin liquidity trend, while decelerating, is still net positive for a fifth-ish consecutive session. A case could be made that SOL's mix of "everyone calling it dead" capitulation plus intact on-chain activity plus a healthy MVRV is close to a genuine base-building setup. Rebuttal: 6/10 is still one full parameter short of the gate, and SOL's own p2 (price still below both 50/200DMA) is a structural point squarely against the "base forming" story — the trend line itself hasn't turned yet, only sentiment has. ZEC's raw count is inflated by a persistently Bearish p1 that should be read as a caution flag, not a green light, and its p5 volume-z Bearish print says the recent rally already lacks conviction. Stablecoin growth decelerating (0.50%→0.29%) cuts against, not for, the liquidity-rotation thesis from the last two checkpoints. No coin is within one clean parameter of arming; forcing either SOL or ZEC's 7th would be exactly the failure mode Section 9 exists to prevent. Hold and let the data clear the bar on its own.

Sector exposure: none (100% cash)
Watchlist changes (MID only): n/a — AM checkpoint, no rotation decisions. Excluded (red flags): none new; LTC and PUMP remain entry_blocked (unchanged since 2026-08-03, proposed drop 2026-08-16).
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows, checkpoint 2026-08-08 AM, incl. logged p1 sentiment reasoning for ETH/BNB/SOL/TRX/ZEC/UNI/ONDO/PEPE/TAO), this report, `state/BRIEFING.md`. JOURNAL/SHADOW_BOOK: nothing to write (no entries/exits this run; shadow book refresh is Monday-only, today is Saturday).
