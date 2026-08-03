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

## CHECKPOINT — 2026-08-03, PM

Global params: stablecoins −0.42% 7d ($306.9B, shrinking) | MVRV BTC 1.20 / ETH 0.92 | F&G 28 (Fear, Δ7d −2) | funding regime: near-zero-to-slightly-positive across the board (no crowding either way) | futures_source: hyperliquid for all 30 (fapi.binance.com still geo-blocked, per 2026-08-03 amendment)
Deployed: 0% across 0 positions | Cash: 100% ($10,000 USDT)
Holdings: none
Signals: armed — none (top counts: ENA 5/10, ADA 4, BNB 4, ONDO 4, PEPE 4, SHIB 4, TRX 4, ZEC 4) | confirmed — none | exit-warned — n/a

Decisions & reasoning:
- Second trading checkpoint since inception (no AM checkpoint ran today — this PM run is picking up the sequence; nothing was armed at the prior 2026-08-02 PM checkpoint, so nothing is eligible for confirmation regardless of today's counts).
- Sentiment pass run for ENA only (the sole coin at ≥5 mechanical Bullish; no holdings to cover). Grok/X read: interest_trend flat in aggregate but individual posts show euphoria markers — rocket emojis, multiple explicit long-setup/price-target calls ("breakout in progress," entries with TPs), no capitulation markers. Judged **Bearish** contrarian: this looks like retail chasing an already-extended tape (+11.7% above 50DMA, RSI 60.5, rv_ratio 1.31 expansion, vol z +1.03), not quiet accumulation. Net ENA: 5 Bull / 2 Bear — still 2 short of the gate, so the call doesn't swing anything this run, but it's logged honestly per SIGNALS.csv notes rather than forced Bullish to inch it closer.
- All other 29 coins: mechanical count <5, so p1 defaults Neutral per protocol. Ceiling for the board (excluding ENA) is 4/10 (ADA, BNB, ONDO, PEPE, SHIB, TRX, ZEC) — nowhere near the 7/10 gate.
- No coin armed, no coin confirmed, no trades. System working as designed.
- Mechanical label review: no overrides. Checked explicitly for RSI<30 capitulation misreads (none present — RENDER lowest at 34.9 in a confirmed downtrend, correctly Bearish) and >25% overextension misreads (PUMP correctly Bearish p2 at +34.0% above 50DMA; PUMP remains entry_blocked anyway on its own red flag). MORPHO's mildly negative funding (−0.0499%/8h) reads Bullish per the contrarian-crowded-shorts logic — consistent, no override needed.
- p7 (OI Δ) reads Neutral board-wide — Hyperliquid's OI_HISTORY.json has only ~2 days of accumulated samples vs. the ~7-day bar noted in the amendment; expect this to resolve over the next several sessions, not a data failure.
- p8 (stablecoin supply) still Bearish board-wide (−0.42% 7d, continuing to shrink); p9 (MVRV) still Bullish board-wide (BTC 1.20 / ETH 0.92, both in the 1–2 healthy band); p10 (F&G) Neutral — 28 is close to the <25 contrarian-Bullish band but falling (Δ7d −2), not rising from under 30, so it doesn't qualify yet.

Red-team summary: Strongest case against "do nothing": ENA's mechanicals are the strongest on the board, and a more charitable sentiment read (interest_trend was labeled flat, not surging) could have landed p1 Bullish, putting ENA at 6/10 — one parameter from relevant. Rebuttal: even granting that generous read, 6/10 still misses the 7/10 gate this checkpoint, so the call is moot in effect; the honest contrarian read (euphoria markers were present in the actual post content, regardless of the flat aggregate-trend label) is the more defensible one, and forcing Bullish to inch a coin toward relevance is exactly the failure mode Section 7 exists to prevent. Second case: the board is capped by two structural ceilings this early in the paper phase — p1 defaulting Neutral below the mechanical-5 threshold, and p7 defaulting Neutral from thin OI history — either could be masking a real setup among the 4/10 names (ADA, BNB, ONDO, SHIB, TRX, ZEC). Rebuttal: these are honest data gaps, not judgment calls to paper over; fabricating either would violate the never-fabricate rule, and both ceilings relax on their own as history accumulates and as more names cross the sentiment-pass threshold.

Pre-mortem (PM): scenario "BTC −15% overnight" — book is 100% USDT across 0 positions, so realized damage = $0 regardless. No de-risk action possible or necessary.

Sector exposure: none (100% cash)
Watchlist changes: none (PM checkpoint — rotation is MID-only). LTC and PUMP remain entry_blocked on their red flags (MWEB reorg / class-action+unlock, respectively); both reach their 2-week minimum-stay mark on 2026-08-16 and become drop-eligible at the next MID sourcing routine on/after that date.
Simulated fills: n/a
Learning artifacts written: SIGNALS.csv (30 rows appended, checkpoint 2026-08-03 PM, incl. logged ENA sentiment reasoning), this report. JOURNAL.md/SHADOW_BOOK.md: nothing to write (no entries, no confirmed-but-rejected candidates, no exits).
