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
