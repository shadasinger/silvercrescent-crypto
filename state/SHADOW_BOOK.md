# SHADOW BOOK — rejected runner-ups & virtual continuations

Refresh Mondays AM; grade at 6 weeks.

## Weekly refresh log

- **2026-08-17 (Monday AM):** checked for entries. No confirmed candidates have ever been rejected for a slot (the only entry sequence to date, TRX, was never in competition with another confirmed candidate), and no positions have been exited/closed — `closed_positions` in PORTFOLIO.json is still empty. MORPHO armed at 7/10 on 2026-08-16 PM but did not reach a second consecutive >=7/10 checkpoint this AM (6/10) -- this is a lapsed arm, not a rejected confirmed-candidate, so it does not qualify for a shadow-book virtual entry per Section 11.2's definition. Nothing to add this week; book remains empty.

- **2026-08-24 (Monday AM):** first refresh with real exit history to grade. Six tranches closed since the 08-17 refresh, all via `closed_positions` in PORTFOLIO.json: TRX (trim 08-16 AM -$7.22, full exit 08-19 AM -$4.09, thesis Broken on sustained OI collapse), CAKE (staged-cut 08-19 AM +$11.96), ETH (staged-cut 08-19 AM -$0.04), ZEC (staged-cut 08-19 AM -$12.86), MORPHO (staged-cut 08-19 AM -$18.98), UNI (staged-cut 08-22 PM +$5.15). Virtual continuation — mark the exited quantity at today's price (2026-08-24 AM, `parameters.py` generated_at 07:14:11Z) against original cost basis, vs. what was actually realized:

  | Ticker | Exited qty @ price | Realized P&L | Virtual mark-to-now | Virtual P&L (full position vs cost) | Divergence |
  |---|---|---|---|---|---|
  | TRX | 2976.6315 total @ avg exit ~$0.3322 | -$11.31 | $0.3444 | +$25.36 | +$36.67 |
  | CAKE | 332.0878 @ $1.54 | +$11.96 | $1.742 | +$79.04 | +$67.08 |
  | ETH | 0.2607 @ $1915.86 | -$0.04 | $2470.46 | +$144.59 | +$144.63 |
  | ZEC | 1.9611 @ $502.81 | -$12.86 | $850.04 | +$668.14 | +$681.00 |
  | MORPHO | 234.3782 @ $2.05 | -$18.98 | $2.762 | +$147.89 | +$166.87 |
  | UNI | 119.791 @ $4.257 | +$5.15 | $4.458 | +$29.35 | +$24.20 |

  **Total realized across the six: -$31.23. Total virtual (if none had been cut/exited): +$1,094.37. Opportunity cost: -$1,125.60 on the $10,000 book**, continuing to widen from the -$437.86 read at the 2026-08-21 audit (LESSONS.md #7) as the market-wide melt-up (F&G 46→73 over the period) kept extending. ZEC (+$681.00) and ETH (+$144.63) are now the two largest single-ticker divergences of the book's history — both staged-entry cuts driven by RSI/rvol (ZEC, hypothesis #2) and non-golden-cross DMA (ETH, hypothesis #3) rather than by price or OI reversing. TRX and MORPHO's cuts were *correctly identified* thesis-test breaches at the time (named-metric OI divergence, overextension) that still cost money to have acted on, given how far the broad rally has since run — the regime-timing failure mode named in LESSONS.md #7(b), not a signal-quality problem. New evidence logged in LESSONS.md this checkpoint. No confirmed candidates were rejected for a slot this week (ONDO confirmed 2026-08-24 AM into an open slot, no competition) — nothing to add on that front.


## Rejected confirmed-candidate — AAVE — 2026-08-26 AM

**First real slot competition among confirmed candidates.** AAVE confirmed 7/10 Bullish (1/10 Bearish) at 2 consecutive checkpoints (PM 08-25 7/10 armed -> AM 08-26 7/10 confirmed), tied with MORPHO, JUP, and ASTER (all also 7/10) for 3 open slots (max 5 concurrent positions, XLM/ONDO already held). Per Section 5 step 6, tied confluence counts break on EV: ASTER +2.45% > MORPHO +2.16% > JUP +1.96% > **AAVE +1.58%** — AAVE lost the tie-break, driven by a lower stated p (0.38 vs 0.40-0.41 for the other three) reflecting its standing overextension flag (dev-from-50DMA +32.2%, the most extended read on the board, and the only one of the four carrying its own p2_dma Bearish mechanical flag) — a risk explicitly named in the PM 08-25 red-team pass ("the one arm to treat with extra skepticism").

**Virtual entry (for tracking only, no capital deployed):**
- Entry: $128.31 (2026-08-26 AM, `parameters.py` generated_at 2026-08-26T07:18:08Z)
- Target: $153.33 (+19.5%) | Invalidation: $116.25 (-9.4%) | R = 2.075 | stated p = 0.38 | EV = +1.58%
- Virtual size: 5% staged-half equivalent, i.e. tracked as if 496.06/128.31 = 3.8659 AAVE were bought at $128.31.
- Confluence at rejection: 7/10 Bullish, 1/10 Bearish (mechanical p2-10: 6 Bullish/1 Bearish/2 Neutral; p1 contrarian Bullish on capitulation-flavored chatter — whales heavily short, "building through the ugly part").

To be marked-to-market at the next Monday AM shadow-book refresh (2026-09-01, also first-of-month — will combine with the monthly review) against its virtual target/invalidation, same as the real positions' thesis tests.

## AAVE rejected-candidate tracking closed — converted to a real position, 2026-08-26 PM

The AM 08-26 AAVE virtual entry above (rejected on the EV tie-break, no open slot) is superseded: JUP and ASTER both stage1-cut this checkpoint on non-confirmation, freeing a slot, and AAVE reconfirmed ≥7/10 for a 3rd consecutive checkpoint — it entered as a real staged half-position (see `state/PORTFOLIO.json` / `state/JOURNAL.md` ENTRY — AAVE — 2026-08-26 PM). No further virtual tracking needed; real ledger now applies.

## Exited-position virtual continuations — JUP, ASTER — 2026-08-26 PM (staged-entry cuts)

Both cut on the standard staged-entry non-confirmation rule (Section 5 step 9), not thesis failure — tracked here per Section 11.2 for continuation comparison at the next weekly refresh (2026-09-01, Monday AM, combined with the monthly review):

- **JUP** — exited 2312.648 @ $0.2165 (2026-08-26T19:10:00Z). Virtual continuation: hold the same qty at the same cost basis ($0.2145) forward from this timestamp, mark at each weekly refresh against the original target ($0.2563) / invalidation ($0.1943).
- **ASTER** — exited 704.6349 @ $0.70 (2026-08-26T19:10:00Z). Virtual continuation: hold the same qty at the same cost basis ($0.704) forward from this timestamp, mark at each weekly refresh against the original target ($0.8413) / invalidation ($0.6378).

## Weekly refresh — 2026-08-31 (Monday AM)

**Note on timing:** the 2026-08-26 PM entry above projected this refresh for "2026-09-01, also first-of-month". That was a miscalculation of the calendar — 2026-08-31 is the actual Monday per the system clock (confirmed: 2026-08-30 was Sunday per the MID checkpoint log), and 2026-09-01 is a Tuesday, not the first-of-month AM trigger either (the monthly review fires on the first AM checkpoint of a calendar month, which will be 2026-09-01 AM, a Tuesday). Running the shadow-book refresh on its correct Monday date now; the monthly review will run separately on its own trigger.

Four tranches closed since the 2026-08-24 refresh, all cut/exited between 2026-08-26 PM and 2026-08-29 AM: JUP (staged-cut 08-26 PM, non-confirmation), ASTER (staged-cut 08-26 PM, non-confirmation), ONDO (Weakening trim 08-28 PM + full exit 08-29 AM, named thesis-test breach), AAVE (sector-cap trim 08-28 PM + sector-cap exit 08-29 AM, compliance-driven not thesis-driven). Virtual continuation — mark the exited quantity at today's price (2026-08-31 AM, `parameters.py` generated_at 07:16:04Z) against original cost basis, vs. what was actually realized:

| Ticker | Exited qty @ avg cost | Realized P&L | Current price | Virtual mark-to-now | Virtual P&L (vs cost) | Divergence |
|---|---|---|---|---|---|---|
| JUP | 2312.648 @ $0.2145 | +$4.63 | $0.2067 | $478.02 | -$18.04 | -$22.67 |
| ASTER | 704.6349 @ $0.704 | -$2.82 | $0.698 | $491.84 | -$4.23 | -$1.41 |
| ONDO | 2646.607 @ $0.378529 | -$71.79 | $0.3488 | $923.14 | -$78.68 | -$6.89 |
| AAVE | 7.1136 @ $125.211915 | -$21.82 | $123.47 | $878.32 | -$12.39 | +$9.43 |

**Total realized across the four: -$91.80. Total virtual (if none had been cut/exited): -$113.34. Opportunity cost: -$21.54 on the $10,000 book** — a small NEGATIVE divergence (i.e. cutting/exiting was, in aggregate, mildly *better* than holding would have been), the first batch since tracking began where the sign flips against the "false-negative cut" pattern that dominated every prior weekly refresh (-$437.86 at 08-21, widening to -$1,125.60 at 08-24). This lines up with the regime context: F&G has cooled from the 73 peak referenced in LESSONS.md #10 to 62 this checkpoint (-11/7d), and JUP/ASTER/ONDO/AAVE all traded lower or flat over the tracking window rather than continuing to run. Individually: JUP and ONDO's cuts both look correct in hindsight (both kept falling); ASTER is roughly a wash; AAVE's cut cost a modest $9.43 (it was a sector-cap-forced correction, not a thesis call, so this reads as a data point on the sector-cap mechanism from LESSONS.md #11, not on the RSI/rvol or DMA hypotheses #2/#3). This is exactly the kind of reversal case LESSONS.md #7 and #10 named as the evidence that would weaken those hypotheses ("a reversal that erases some of this virtual gap... would show the divergence was a temporary artifact of an ongoing melt-up rather than a durable rule flaw") — logged as a data point for the next monthly review (2026-09-01 AM), not yet enough on its own (N=2 weekly readings in each direction) to revise Section 5's rules either way.

No confirmed candidates were rejected for a slot this week (no coin reached 7/10 confluence at all between 2026-08-26 PM and this checkpoint — ICP armed once at PM 08-30 but lapsed on non-confirmation this AM, never reaching a second consecutive qualifying checkpoint) — nothing to add on that front. No new exited-position virtual continuations to open this checkpoint (XLM and MORPHO's trims this week were partial trims of still-open positions, not full exits, and are tracked in `PORTFOLIO.json` status_history rather than here per the shadow book's closed-position/rejected-candidate scope).
