# UAT and defect triage

## Business sessions

Run three short sessions with staff representatives: lookup/member disambiguation, address changes with pending/rejected statuses, and reconciliation exception follow-up. Give each participant a synthetic dataset and task goals without prescribing every click. QA observes and records friction; the business owner decides whether the workflow meets the operational need.

Capture participant role, scenario, expected business outcome, actual outcome, build, evidence, defect ID, and acceptance decision. Track unexecuted scenarios and blocked participants separately. Retest failed cases with the same role and a fresh dataset after the fix.

## Triage rules

| Severity | Example | Handling |
| --- | --- | --- |
| Critical | Wrong member updated or unauthorized edit succeeds | Stop affected testing; release blocker; joint developer/vendor reproduction |
| High | Rejected update displayed as completed | Release blocker; inspect correlated logs and field state |
| Medium | Understandable workaround exists but status workflow is confusing | Assign owner/date; business reviews operational impact |
| Low | Cosmetic issue with no workflow or accessibility effect | Prioritize with other improvements |

Severity describes impact; priority describes repair order. Include reproducible steps, seed IDs, expected/actual outcomes, first affected build, and relevant logs without real member data. Do not assign blame to the vendor: agree the contract, locate the failing boundary, and retest the complete workflow after an interface fix.

A daily triage review resolves owner, severity, fix target, retest needs, and coverage consequences. Reopened defects retain their prior history. Workaround acceptance requires a named business owner and evidence it is practical; it does not automatically remove a data-integrity blocker.
