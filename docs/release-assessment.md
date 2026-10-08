# Worked release assessment — fictional example

**Illustrative only:** The outcomes below are invented to show release judgment. They are not results from a real CRM or an executed automation suite.

Candidate: Northstar CRM 0.8.0, sandbox build. Ten critical-path cases planned: eight illustrative passes, one illustrative failure, one blocked.

| Finding | Evidence in this example | Decision consequence |
| --- | --- | --- |
| TC-05 fails | Core rejects request N-042; CRM incorrectly displays completed | High-severity blocker: staff could rely on data that was never saved |
| TC-09 blocked | Rollback environment lacks queue replay configuration | Recovery is unproven; completion required before release |
| Other eight cases pass | Example execution records include builds, IDs, timestamps, comparisons | Useful coverage but does not cancel either gap |

**Recommendation: hold the release.** An 80% pass rate is not an adequate release argument when truthful status and recovery remain unproven.

## Evidence required to reconsider

Fix the rejection-to-status mapping and retest TC-05 plus delayed/duplicate status cases TC-04 and TC-10. Complete TC-09 with queue snapshots and accepted/pending counts before and after rollback. Repeat a clean smoke run on the new candidate, obtain business UAT acceptance, and document any remaining lower-severity defects with owners/workarounds.

The release owner reviews that evidence with QA, engineering, and the business owner. Record candidate version, open risks, evidence links, decision, decision-maker, and timestamp. Do not reuse evidence from a different candidate without explaining why it remains valid.
