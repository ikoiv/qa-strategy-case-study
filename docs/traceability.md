# Traceability

Coverage links requirements to concrete risks and cases. Presence in this table is planned coverage, not evidence of a pass.

| Requirement | Risks | Cases | Evidence to retain |
| --- | --- | --- | --- |
| REQ-01 | R-01 | TC-01 | Two member records before/after; selected stable ID |
| REQ-02 | R-02 | TC-02, TC-03 | Role claims, HTTP result, unchanged-state check, audit event |
| REQ-03 | R-05 | TC-03, TC-06 | Input/core/CRM comparison; elapsed time |
| REQ-04 | R-03, R-04 | TC-04, TC-05, TC-10 | Correlation IDs, delivery count, status history |
| REQ-05 | R-06 | TC-07 | Known dropped message and reconciliation exception |
| REQ-06 | R-07 | TC-08 | Keyboard session notes, focus/error observations |
| REQ-07 | R-08 | TC-09 | Queue snapshot, replay count, balance of accepted/pending outcomes |

See [test cases](test-cases.md), [risk register](risk-register.md), and [release assessment](release-assessment.md).
