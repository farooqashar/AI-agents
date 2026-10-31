#!/usr/bin/env python3
"""Validate the deliberately small agent metadata schema without dependencies."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ('Use when', 'Required inputs', 'Workflow', 'Boundaries', 'Output', 'Verification')


def validate(root):
    errors = []
    agents = []
    registry = (root / 'README.md').read_text()
    for path in sorted(root.glob('*.md')):
        text = path.read_text()
        if path.name in ('README.md', 'HOW_TO_USE.md'):
            continue
        agents.append(path.name)
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        if not match:
            errors.append(f'{path.name}: missing frontmatter')
            continue
        lines = match[1].splitlines()
        expected = [r'description: .+', r'mode: subagent', r'permission:',
                    r'  edit: (allow|deny)', r'  bash: (allow|deny)', r'  web: (allow|deny)']
        if len(lines) != len(expected) or any(not re.fullmatch(pattern, line) for pattern, line in zip(expected, lines)):
            errors.append(f'{path.name}: invalid or incomplete metadata')
        body = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', text, flags=re.M | re.S)
        headings = re.findall(r'^## (.+)$', body, re.M)
        if headings != list(SECTIONS):
            errors.append(f'{path.name}: expected the six contract sections in order')
        for section in SECTIONS:
            if not re.search(r'^## ' + re.escape(section) + r'\n\n\S', text, re.M):
                errors.append(f'{path.name}: empty section {section}')
        if f']({path.name})' not in registry:
            errors.append(f'{path.name}: missing registry link')
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
            if '://' in link or link.startswith(('#', 'mailto:')):
                continue
            target = link.split('#', 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f'{path.relative_to(root)}: broken local link {link}')
    cases_path = root / 'evals/cases.yaml'
    if cases_path.exists():
        try:
            cases = json.loads(cases_path.read_text())['cases']
            seen = set()
            if not cases:
                raise ValueError('no cases')
            for case in cases:
                if case['id'] in seen or case['agent'] not in agents:
                    raise ValueError('duplicate id or unknown agent')
                seen.add(case['id'])
                if not case['input'].strip() or not case['pass_criteria'] or not all(isinstance(x, str) and x.strip() for x in case['pass_criteria']):
                    raise ValueError('empty input or pass criteria')
        except (ValueError, KeyError, TypeError) as exc:
            errors.append(f'evals/cases.yaml: invalid case structure: {exc}')
    return agents, errors


if __name__ == '__main__':
    agents, errors = validate(ROOT)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print(f'Validated {len(agents)} agents, local links, and evaluation case structure.')
