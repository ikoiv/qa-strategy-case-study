# Risk register

Scores use impact × likelihood on a 1–5 scale. Likelihood is an assumption for prioritization, not a measured probability. Scores 15–25 receive first attention, 8–14 follow, and 1–7 are monitored.

| ID | Failure | Impact | Likelihood | Score | Mitigation / evidence |
| --- | --- | --- | --- | --- | --- |
| R-01 | Address written to the wrong member | 5 | 3 | 15 | Stable member ID, duplicate-name test, before/after core comparison |
| R-02 | Viewer can edit or enumerate another member | 5 | 3 | 15 | Server-side authorization tests; denied request must not change state |
| R-03 | Timeout creates a duplicate accepted change | 4 | 4 | 16 | Redeliver identical correlation/idempotency key; one logical change |
| R-04 | UI says success while core rejects update | 5 | 4 | 20 | Core rejection fault injection; status and reconciliation evidence |
| R-05 | Unicode/long address fields are truncated | 4 | 3 | 12 | Boundary/Unicode inputs; exact field-level comparison |
| R-06 | Nightly reconciliation misses a lost update | 5 | 3 | 15 | Intentionally omit a message; exception must identify the member/request |
| R-07 | Staff cannot navigate status/error controls by keyboard | 3 | 3 | 9 | Keyboard and assistive-technology exploratory session |
| R-08 | Rollback restores app but loses queued changes | 5 | 2 | 10 | Rehearsal with pending messages; reconcile before/after rollback |

Each mitigation maps to a named case in [traceability](traceability.md). Revisit likelihood as real execution evidence becomes available. Security and data-integrity failures can remain release blockers even with a lower numerical score.
