# QA strategy case study

A fictional CRM integration project used to explore the decisions around testing: what to prioritize, how to make coverage visible, and what evidence should support a release.

I enjoy organizing a complicated problem into something a team can work through. This notebook brings together risk, automation, exploratory testing, UAT, and release judgment around one small scenario.

## The scenario

**Northstar Member Services** is a fictional organization introducing a CRM that reads member contact details from a core system and submits address updates through an integration service. Staff can view the synchronization status. A nightly reconciliation finds rejected or missing updates.

These are invented requirements and sample artifacts, not an account of an employer's implementation. The project has no real member information.

## Read the notebook

1. [Test strategy](docs/test-strategy.md): scope, assumptions, environments, responsibilities, and approach.
2. [Risk register](docs/risk-register.md): risk scores and concrete mitigations.
3. [Requirements and test cases](docs/test-cases.md): acceptance criteria, inputs, expected results, and test levels.
4. [Traceability](docs/traceability.md): requirements linked to risks and evidence.
5. [UAT and triage](docs/uat-and-triage.md): business scenarios, vendor collaboration, and defect decisions.
6. [Release assessment](docs/release-assessment.md): a worked fictional hold decision and the evidence needed to revisit it.
7. [Exploratory charters](docs/exploratory-charters.md): timeboxed investigations beyond scripted cases.

## Check the artifact links

Python 3.12+:

```bash
python tools/check_docs.py
```

CI checks relative Markdown links and traceability identifiers. That protects the notebook's structure; it does not prove that a fictional product meets its requirements. All test outcomes in the worked release example are clearly labeled illustrative.

Next experiments: extending the case study with API contract examples and a more detailed migration validation plan.

MIT licensed.
