# Requirements and test cases

## Acceptance criteria

| Requirement | Observable acceptance criterion |
| --- | --- |
| REQ-01 | Member lookup and updates use a stable member ID, even when names match |
| REQ-02 | Viewer role cannot submit edits; editor role can update permitted fields |
| REQ-03 | A valid accepted address appears unchanged in the core and CRM within 60 seconds |
| REQ-04 | Duplicate delivery applies one logical update; rejected/late updates show truthful status |
| REQ-05 | Reconciliation identifies missing/rejected updates with member and request IDs |
| REQ-06 | Staff can reach lookup, edit, and status controls by keyboard, with understandable errors |
| REQ-07 | Rollback preserves/reconciles pending changes without losing accepted work |

## Executable test specifications

These are specifications for the fictional system. They have not been executed against a real product.

| Case | Level | Setup and action | Expected result |
| --- | --- | --- | --- |
| TC-01 | Integration | Seed two members named Alex Lee with distinct IDs; update only member M-002 | Only M-002 changes; M-001 remains byte-for-byte unchanged in permitted contact fields |
| TC-02 | API | Viewer submits a direct edit request for M-002 | 403; no state change and an audit event records the denied action |
| TC-03 | API | Editor submits a valid address to M-002 | Accepted request has a correlation ID; core and CRM match input within 60 seconds |
| TC-04 | Integration | Redeliver TC-03 with the same request key after simulated timeout | Same logical outcome; no second change event or duplicate reconciliation record |
| TC-05 | Integration/UI | Force the core to reject a valid-looking address | CRM shows rejected/failed status, never completed; original core address remains |
| TC-06 | API/integration | Submit lengths 1, 120, and 121 for a fictional max-120 line; include Café and emoji | First two preserved exactly; 121 rejected before dispatch; no silent truncation |
| TC-07 | Reconciliation | Accept a request at gateway, intentionally drop before core, run nightly reconciliation | Exception includes member ID, request ID, reason, and recovery owner |
| TC-08 | Manual/UI | Use keyboard only through lookup, edit, invalid submission, and status | Logical focus order; focus/error association is understandable; no keyboard trap |
| TC-09 | Integration | Hold an accepted update in pending state; rehearse rollback and replay | Pending request survives; one accepted outcome; pre/post counts and values reconcile |
| TC-10 | Integration/UI | Delay core response beyond 60 seconds, then deliver it | Status stays pending/late until actual acceptance; late event resolves without duplicate work |

For each execution capture build, environment, data seed, request ID, timestamps, actual result, and evidence links. Treat blocked cases as blocked; do not turn them into passes. The address length limit is invented for this exercise.
