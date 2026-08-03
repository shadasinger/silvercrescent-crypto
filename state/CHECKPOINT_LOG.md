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

---

## CHECKPOINT — 2026-08-03, MID (sourcing routine — no trading decisions)

Global params: stablecoins −0.41% 7d ($306.9B, still shrinking) | MVRV BTC 1.20 / ETH 0.92 | F&G 28 (Fear, Δ7d −2) | funding regime **UNAVAILABLE — see data outage**
Deployed: 0% across 0 positions | Cash: 100% ($10,000 USDT)
Holdings: none
Signals: n/a — MID does not score confluence or append to SIGNALS.csv (Section 6: no trading decisions)

### DATA OUTAGE (material — read before the PM checkpoint)

**Binance futures is geo-blocked from this runner: `fapi.binance.com` returns HTTP 451** ("restricted location"), persistent across retries. Confirmed still blocked on `dapi.binance.com` and `www.binance.com/fapi`; no Binance-official mirror serves futures data.

Consequence: **parameter 6 (funding) and parameter 7 (open interest) are Neutral for all 30 coins**, 0/30 populated. At inception (2026-08-02) both populated for 28/30, so this is a new environmental block, not a code regression.

- Per CLAUDE.md Section 0, affected parameters are labeled Neutral and the outage is recorded. **No values were fabricated and no substitute exchange was silently swapped in** — the rubric names "Binance futures" as the source, and changing it is a rulebook amendment requiring user sign-off (Section 13).
- Effective confluence ceiling this run is **8/10**, and the entry gate needs 7/10. Two dead parameters means a qualifying coin must now be near-perfect on the remaining eight.
- **Decision required from the user:** either (a) accept the 8/10 ceiling while the block persists, (b) sign off on an alternative funding/OI source (Bybit, OKX, Coinglass) as a logged rulebook amendment, or (c) treat p6/p7 outage as an automatic no-trade condition. Until then the book simply cannot arm anything.

A second, unrelated blocker was found and **fixed** in code: `scripts/universe.py` called `api.binance.com/api/v3/exchangeInfo`, which is also 451-blocked, so the routine could not run at all. Repointed to `data-api.binance.vision` — Binance's own public market-data mirror, already used by `scripts/parameters.py` for exactly this reason. Same provider, same data, different hostname; not a rulebook change.

### Step 1-2 — universe & data cards

`scripts/universe.py`: **114 candidates** (mcap > $100M AND Binance spot USDT, stablecoins/wrapped excluded), 12 stable/wrapped filtered. Identical count to the inception run — consistent, not a coverage regression. CoinGecko enrichment now working properly with `COINGECKO_API_KEY`: **60 coins category-tagged, 56 with sentiment votes** (vs 4 in the earlier smoke test).

The rulebook's "~250-350 candidates" estimate is running ~2.5x high against reality; 114 is what the stated filters actually yield. Flagging as an estimate to correct, not a fault.

Permanent-slot audit: BTC, ETH + top-8 Binance-tradeable by mcap = BNB, XRP, SOL, TRX, DOGE, ZEC, ADA, LINK. **Unchanged; no rotation required.** Universe gap worth noting — HYPE ($12.1B, rank 10), XMR ($6.8B, 17), WBT ($16.3B, 18) and LEO ($9.0B, 13) are all top-20 by mcap but have **no Binance spot USDT pair**, so they are structurally untradeable for this book and cannot occupy permanent slots.

### Step 3 — candidate scoring & red-flag screen

No-chase rule (>50% in 7d): **nothing triggers** — the largest 7d gain anywhere in the universe is DCR +17.5%, and off-watchlist the max is +17.5%. KAITO (+57.6%) and ZAMA (+59.4%) are hot on the **30d** window only, which the rule does not cover; both were penalized on judgment instead.

**AUTO-EXCLUDED (red flags, logged):**

| Coin | Category | Basis |
|---|---|---|
| **DEXE** | Team exit / suspected insider distribution | −97% from $49.43 ATH to ~$1.56 in 11 days; −88% single-day 2026-07-21. Ceffu custody wallets moved 797,917 DEXE to Binance across six txs from 07-13; ~625,000 DEXE (~$6.2M) from believed team-linked wallets hit Binance on 07-21. No exploit. Caveat recorded: the analyst explicitly called this "an early assessment" and **no evidence proves** DWF Labs/Falcon/Ceffu/the team caused it — not a legally confirmed rug. Unexplained custody outflows into a thin market meet the spirit of the rule. |
| **WLFI** | Regulatory action (active) | US House probe (Rep. Khanna) into a $500M/49% stake by Abu Dhabi–linked "Aryam Investment 1", document deadline 2026-03-01; Sens. Warren and Reed requested a federal investigation citing alleged sales to sanctioned/high-risk buyers. |
| **WLD** | Regulatory action (multi-jurisdiction) | Philippine C&D vs Tools for Humanity, Brazil ANPD ban, Kenya suspension + court-ordered biometric deletion, Indonesia suspension. Latest dated action Oct 2025 — a structural overhang rather than a fresh event, but for a coin being considered for **addition** the conservative call is exclude. |

**Red flags found ON the existing watchlist — handled by entry block, not by drop:**

Rotation is locked (below), so a drop is not available today. Both coins remain listed but are marked `entry_blocked` in WATCHLIST.json, which enforces the Section 2 exclude rule at the only point it can actually cause harm — entry — without churning the list on stale or ambiguous news one day after inception. Both are proposed formal drops on 2026-08-16.

- **LTC — score 6 → 3, ENTRY BLOCKED.** MWEB/MimbleWimble zero-day: malformed input metadata let ~1–2 LTC back an >85,000 LTC pegout (2026-03); a re-exploit attempt on 2026-04-25 **forced a 13-block reorg rewriting ~3 hours of chain history**. ~$600K realized loss, patched in v0.21.5.4. Judgment: stale (3–4 months) and resolved, which is why it is not a unilateral drop — but a settlement-assurance failure is thesis-critical for a coin whose entire thesis is *payments*. The thesis, not just the price, is impaired.
- **PUMP — score 6 → 2, ENTRY BLOCKED (rank #1 drop candidate).** Live SDNY class action alleging Pump.fun ran an unlicensed "memecoin casino"/Ponzi — $722M revenue against $4–5.5B alleged retail losses — with a whistleblower leak of 5,000+ internal messages alleging coordinated launch manipulation and MEV insider trading; amended complaint permitted 2025-12-09, live through 2026. Strictly a *private* class action, not a regulator action, so it fails the literal wording of the auto-exclude rule. It passes the intent comfortably: the revenue the thesis capitalises is the revenue alleged to be unlawful. Compounded by **41% of total supply unlocking 2026-07-12**.

**Watchlist findings that are NOT excludes** (logged to WATCHLIST.json `flag` fields): BTC (Coldcard *vendor* RNG flaw, ~1,367 BTC drained — protocol unaffected); ETH (EF co-ED resigned 06-18 — foundation governance, not abandonment); SOL (SDNY MEV class action — private suit); ZEC (Orchard counterfeiting vuln, **patched before disclosure, no exploitation**; Coinbase delisting — Binance spot, our only venue, unaffected); HBAR (Bonzo Lend oracle exploit ~$9.05M — app-layer, core network intact, but ecosystem TVL −40%); RENDER (dormant legacy Polygon contract accessed, no funds lost); ARB (third-party AFX bridge −$24.15M, not the protocol; 92.65M unlock); MORPHO (flash-loan *rail* in two exploits, not the vulnerable component); CAKE (exploits were in listed tokens' burn mechanics, not PancakeSwap); AAVE (not exploited); ENA (heavy dilution); JUP (DAO suspended governance votes — credibility, not a category hit); SHIB (Shibarium exploit was 2025-09, resolved).

**Unresolved data quality — TAO.** The screen surfaced three conflicting hack claims that could **not** be verified: an "$8M hack" that is the real July **2024** event misdated by the search index, a "$28M hack resolved October 2026" that is future-dated and therefore impossible, and an unsourced "April 2026 Covenant AI incident". None carried a citable dated source from a reputable outlet. TAO is recorded **clear but requires a manual re-check before any entry** — it is not being treated as flagged on the strength of unverifiable noise, nor as clean on the strength of absence.

Sector-wide context, not attributable to any watchlist coin: July 2026 saw ~30 hacks (~$110–210M) and H1 2026 set a record 212 exploits / $1.1B. Binance's July delisting waves touched ALCX, ARDR, NFP, POND — **none of the 30**. Regulatory posture is loosening, not tightening (SEC dropped the Uniswap Labs probe; SEC/CFTC joint classification interpretation 2026-03-17; CLARITY Act through committee).

### Step 4 — watchlist assembly: NO CHANGES

**All 20 rotating slots were added 2026-08-02 and sit inside the 2-week minimum hold — every one is ineligible until 2026-08-16.** Zero rotations are permissible today. The 5-changes/week budget is untouched at 0/5. Only a red-flag auto-exclude could override the minimum hold, and the two candidates for that were resolved with entry blocks as argued above.

This is the rule working as designed on day 2, not a failed sourcing run. The bench below is what the screen actually bought us: a ranked, red-flag-cleared queue for the 08-16 window.

**Ranked bench for 2026-08-16** (scored on catalyst quality / red flags / liquidity health):

| Rank | Coin | Score | Sector | Catalyst | Liquidity (vol/mcap) |
|---|---|---|---|---|---|
| 1 | **INJ** | 8 | DeFi Infra | Coinbase native mainnet migration (07-03), SEC transfer-agent filing + MiCA whitepaper, Injective Mint RWA platform (07-20/22) | 0.083 healthy |
| 2 | **ASTER** | 8 | DEX | Buyback/burn expanded to 99% of daily fees, supply target 8B→3B; monthly unlocks cut ~97% via staking switch; record fees 07-29 | 0.030 healthy |
| 3 | **ICP** | 7 | AI/Infra | Mission 70 cuts annual inflation 9.72% → ~2.92% by end-2026; Caffeine AI V2 live | 0.022 healthy |
| 4 | **LDO** | 7 | Liquid Staking | Lido V3 multi-product transition, stVaults + MetaVaults, automated buybacks, proposed 10,000 stETH one-time buyback | 0.078 healthy |
| 5 | **TIA** | 7 | Data Availability | Matcha upgrade 8MB → 128MB block capacity, inflation cut; major unlocks completed late 2025 (overhang cleared) | 0.057 healthy |

Open slots for these at 08-16 exist in DEX (3/4), AI (3/4), Liquid Staking (1/4) and DePIN — INJ/ASTER/ICP/LDO/TIA all fit without breaching a cap.

**Blocked by the Major-L1 sector cap (4/4, fully consumed by permanents ETH/SOL/ADA/TRX)** despite scoring well: AVAX (Helicon upgrade on testnet, VanEck spot ETF live, Bitwise staking-ETF filing), NEAR (Confidential Intents GA, x402 Foundation, Ledger integration across 7.5M+ devices), SUI (gasless stablecoin payments live 07-27), DOT, ALGO. These cannot enter until a permanent rotates out of the top-8. **This cap is now binding on the four best-catalyst names in the universe** — worth revisiting at the monthly review, since the permanents are consuming a cap that was presumably meant to limit *discretionary* concentration.

**Scored but not recommended:** KAITO **3** — no red flag, but a dated **2026-08-20 unlock of 32.6M tokens (~$37.8M): 3.3% of supply but ~13.5% of market cap**, with 15M going to creator incentives, the cohort most likely to sell on receipt. A hard argument against entry before late August. ZAMA **6** — clear screen, real product (confidential RFQ swaps live 07-24, public release after beta ends Sept 2026), 63% of circulating supply staked, but **no vesting schedule was findable in any source**; with a Feb 2026 TGE a 12-month cliff is plausible. The missing data is an open risk, not a clean bill. SKY **3** (buyback cut ~87%, vol/mcap 0.005 — untradeable size), DCR **2** (vol/mcap 0.002), QNT **5** (thin at 0.007), FET **5** (Ocean Protocol withdrew from the ASI Alliance — partner exit degrades the merged-alliance thesis), JST **6** (SEC settled with Sun/Tron for $10M **dismissed with prejudice** 2026-03 — a clearing event, not a flag), CRV 6, PENGU 6 (Meme at cap), POL 5, ATOM 5.

### Parameter refresh

`scripts/parameters.py` re-run against the unchanged 30 → `state/PARAMETERS.json` warm for the PM checkpoint. 30/30 coins have spot data (price, DMA, RSI, realized vol, volume z); **0/30 have funding or OI** per the outage above.

Board shape going into PM — the strongest mechanical read is **3/10 Bullish** (PEPE, ZEC, UNI, TRX, SHIB, ONDO, ENA, ADA), against a 7/10 gate. Even granting p1 Bullish on judgment, the ceiling for any coin tonight is 4/10. Global block is the drag: p8 Bearish (stables −0.41%), p9 Bullish (MVRV 1.20), p10 Neutral (F&G 28, Δ −2), p6/p7 dead. ADA is the most interesting single name (+23.2% 7d, RSI 67, volume z +1.1 on an up day, 16.0% above its 50DMA) but p2 reads Neutral, correctly — price is above the 50DMA while the 50 is still below the 200, so there is no golden state to claim.

**Expect no trades at the PM checkpoint.** Nothing can arm from 3/10.

Watchlist changes (MID only): **none** — all 20 rotating slots inside the 2-week minimum hold until 2026-08-16. Slot changes used this week: 0/5.
Excluded (red flags): **DEXE, WLFI, WLD** (candidates, never listed). On-list red flags **LTC, PUMP** → entry-blocked, proposed drops 08-16.
Simulated fills: n/a — MID makes no trading decisions.
Learning artifacts written: `data/universe.json` (114 cards, 60 enriched), `state/PARAMETERS.json` (30 coins + global), `state/WATCHLIST.json` (scores + red-flag/watch flags + 2 entry blocks), this report. No SIGNALS.csv row — MID is not a trading checkpoint.

Open items for the user: (1) **the futures 451 block and the resulting 8/10 ceiling — needs a decision**; (2) LTC and PUMP entry blocks — confirm or overrule ahead of 08-16; (3) Major-L1 cap consumed entirely by permanents is blocking the four best-catalyst names; (4) TAO needs a manual news re-check; (5) p1 sentiment still has no wired source — unchanged from inception.
