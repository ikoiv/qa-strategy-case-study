"""Check relative links and planned-coverage identifiers in this notebook."""
from pathlib import Path
import re
# Resolve from this script rather than the working directory so local and CI runs agree.
root = Path(__file__).resolve().parents[1]
errors = []
# Check local Markdown links; external websites and in-page anchors are out of scope.
for file in root.rglob('*.md'):
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', file.read_text()):
        if link.startswith(('http:', 'https:', '#', 'mailto:')): continue
        target = (file.parent / link.split('#')[0]).resolve()
        if not target.is_file(): errors.append(f'{file.relative_to(root)}: missing {link}')
# Compare defined IDs with traceability references to catch both missing coverage and typos.
requirements = (root/'docs/test-cases.md').read_text()
risks = (root/'docs/risk-register.md').read_text()
trace = (root/'docs/traceability.md').read_text()
for prefix, source in [('REQ',requirements),('TC',requirements),('R',risks)]:
    defined = set(re.findall(r'\b'+prefix+r'-\d+\b',source))
    referenced = set(re.findall(r'\b'+prefix+r'-\d+\b',trace))
    if defined != referenced: errors.append(f'{prefix}: coverage mismatch {defined ^ referenced}')
# A nonzero exit code makes broken documentation fail the GitHub Actions check.
if errors: raise SystemExit('\n'.join(errors))
print('Relative links and requirement/risk/case identifiers are consistent.')
