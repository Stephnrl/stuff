#!/usr/bin/env python3
"""Basic offline structural checks; not a replacement for `claude plugin validate`."""
import json
import pathlib
import re
import sys

root=pathlib.Path(__file__).resolve().parents[1]
plug=root/'plugins/mux-brief'
skill=plug/'skills/mux-brief'
errors=[]
for p in (root/'.claude-plugin/marketplace.json',plug/'.claude-plugin/plugin.json'):
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except (ValueError,OSError) as exc:
        errors.append(f'{p}: {exc}')
manifest=json.loads((plug/'.claude-plugin/plugin.json').read_text())
market=json.loads((root/'.claude-plugin/marketplace.json').read_text())
if manifest.get('name')!='mux-brief': errors.append('Unexpected plugin name')
if not market.get('plugins') or market['plugins'][0].get('source')!='./plugins/mux-brief':
    errors.append('Bad marketplace source')
content=(skill/'SKILL.md').read_text(encoding='utf-8')
if not content.startswith('---\n'):
    errors.append('Skill frontmatter missing')
front=content.split('---',2)[1] if content.startswith('---') else ''
if not re.search(r'^name: mux-brief$',front,re.M): errors.append('Wrong skill name')
if not re.search(r'^description: .+',front,re.M): errors.append('Description missing')
if len(content.splitlines())>500: errors.append('SKILL.md exceeds 500 lines')
for rel in ['references/code-agents.md','references/cloud-ops.md','references/communication.md','scripts/brief.py']:
    if not (skill/rel).is_file(): errors.append(f'Missing {rel}')
if errors:
    print('\n'.join(errors),file=sys.stderr)
    raise SystemExit(1)
print('Offline structural checks passed (use claude plugin validate for host validation).')
