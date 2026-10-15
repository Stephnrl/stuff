#!/usr/bin/env python3
"""Deterministic, offline task-brief renderer. No model calls or command execution."""
import argparse
import json
import re
import sys
from pathlib import Path

SENSITIVE = [
    re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
    re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*["\']?[^\s"\']{8,}'),
]


def has_sensitive(text: str) -> bool:
    """Heuristic only; cannot guarantee detection of all secrets."""
    return any(p.search(text) for p in SENSITIVE)


def validate_source(obj: dict) -> None:
    if not isinstance(obj, dict):
        raise ValueError('Input must be a JSON object')
    if not isinstance(obj.get('outcome'), str) or not obj['outcome'].strip():
        raise ValueError('outcome must be a non-empty string')
    mode = obj.get('mode', 'investigate')
    if mode not in {'edit', 'investigate', 'operate', 'communicate'}:
        raise ValueError('mode must be edit, investigate, operate, or communicate')
    for key in ('scope','restrictions','evidence'):
        if key in obj and (not isinstance(obj[key], list) or any(not isinstance(v, str) for v in obj[key])):
            raise ValueError(f'{key} must be a list of strings')
    for key in ('target','context','approval_gate'):
        if key in obj and not isinstance(obj[key], str):
            raise ValueError(f'{key} must be a string')
    if has_sensitive(json.dumps(obj)):
        raise ValueError('Input may contain a credential. Remove it and use a placeholder before generating.')


def render(obj: dict) -> str:
    validate_source(obj)
    mode=obj.get('mode', 'investigate')
    parts = [f"Target: {obj.get('target') or 'generic'}", f"Mode: {mode}",
             f"Outcome: {obj['outcome'].strip()}"]
    if obj.get('context'):
        parts.append('Known context: ' + obj['context'].strip())
    def add_list(title, key):
        values=[v.strip() for v in obj.get(key, []) if v.strip()]
        if values:
            parts.append(title+'\n'+'\n'.join('- '+v for v in values))
    add_list('Scope:', 'scope')
    add_list('Restrictions:', 'restrictions')
    add_list('Evidence to return:', 'evidence')
    if obj.get('approval_gate'):
        parts.append('Approval gate: '+obj['approval_gate'].strip())
    elif mode == 'operate':
        parts.append('Approval gate: Stop before any mutating or destructive operation.')
    return '\n\n'.join(parts)+'\n'


def main(argv=None) -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True, help='JSON brief specification')
    p.add_argument('--output', type=Path, help='Write to this Markdown file instead of stdout')
    p.add_argument('--stats', action='store_true', help='Write length metrics to stderr (not tokenizer counts)')
    args=p.parse_args(argv)
    try:
        data=json.loads(args.input.read_text(encoding='utf-8'))
        output=render(data)
        if args.output:
            args.output.write_text(output,encoding='utf-8')
        else:
            sys.stdout.write(output)
        if args.stats:
            print(f'characters={len(output)} whitespace_words={len(output.split())}; these are NOT token counts', file=sys.stderr)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print('mux-brief: '+str(e), file=sys.stderr)
        return 2

if __name__=='__main__':
    raise SystemExit(main())
