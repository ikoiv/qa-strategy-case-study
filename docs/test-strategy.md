# Test strategy

## Goal and assumptions

Prevent incorrect member data, unauthorized changes, and silent integration failures during the fictional Northstar CRM rollout. The CRM and core service are independent systems; messages may be delivered more than once. For this exercise, the core is the source of truth, updates are asynchronous, and an accepted update must appear within 60 seconds. A failed update must show a clear staff-visible status.

## Scope

Member lookup; least-privilege viewing/editing; address validation; synchronization; retries; reconciliation; staff usability and selected accessibility checks. Explicitly excluded: payments, lending decisions, account opening, production security certification, and unrelated legacy modules.

## Approach

| Level | Focus | Why |
| --- | --- | --- |
| Unit/component | Field rules, mapping, duplicate-message handling | Fast feedback on branching logic |
| API/contract | Payloads, authorization, failures, version compatibility | Interfaces can break without a visible UI error |
| Integration | CRM → gateway → core → reconciliation | Verify state and outcomes across boundaries |
| UI automation | Lookup, edit, and visible status | Protect a small set of critical staff workflows |
| Exploratory/manual | Delays, stale records, recovery, keyboard/screen-reader behavior | Investigate interactions beyond scripted expectations |
| UAT | Daily staff work with realistic synthetic cases | Confirm usefulness and understandable outcomes |

## Environment and data

Use isolated test identities for viewer/editor roles. Seed synthetic members with normal, long, incomplete, duplicate-name, and non-ASCII contact data. Record dataset version, build, configuration, and correlation IDs with every result. No production exports. Provision a controllable integration sandbox that can delay, reject, and redeliver messages.

## Responsibilities and collaboration

QA owns coverage, evidence review, defect triage preparation, and the release recommendation. Developers own unit checks and implementation fixes. Vendor developers participate in interface reviews and joint failure reproduction; every fix includes its build/version and retest evidence. Business owners define acceptable staff outcomes and own UAT acceptance. The release owner makes the final release decision after reviewing unresolved risks.

## Entry and exit

Entry: agreed acceptance criteria, stable contract version, deployable build, seeded data, working observability, and sandbox fault controls.

Exit: all critical cases executed successfully; no unresolved defects that permit unauthorized access, data corruption, or silent loss; lower-severity issues have documented impact and approved workarounds; UAT is signed off; rollback is rehearsed. A high pass percentage cannot override a critical failure.

## Delivery rhythm

Review requirements before implementation, run component/API checks on changes, run integration and UI smoke checks per deploy, and reserve exploratory/UAT sessions before release. Report coverage gaps and blocked cases separately from failures. Investigate retries and flaky tests rather than counting a rerun as clean evidence.
