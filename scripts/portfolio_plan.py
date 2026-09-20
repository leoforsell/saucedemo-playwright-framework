#!/usr/bin/env python3
"""Derive tracking from PORTFOLIO_PLAN.md. Offline preview unless --apply is set."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def weeks(text):
    matches = list(re.finditer(r'^#### Week (\d+) - (.+)$', text, re.M))
    if [int(m[1]) for m in matches] != list(range(1, 17)):
        raise ValueError('Expected exactly Week 1 through Week 16, in order')
    result = []
    for index, match in enumerate(matches):
        section = text[match.end():matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        section = section.split('\n## Misa IT Review Checkpoints')[0]
        objective = re.search(r'\*\*Objective:\*\* (.+)', section)
        criteria = re.search(r'\*\*Definition of Done:\*\*\s*\n(.*?)\n\*\*Acceptance evidence:', section, re.S)
        evidence = re.search(r'\*\*Acceptance evidence:\*\* (.+)', section)
        if not objective or not criteria or not evidence or '- [ ]' not in criteria[1]:
            raise ValueError(f'Week {match[1]} lacks objective, criteria, or evidence')
        result.append(dict(week=int(match[1]), title=match[2], objective=objective[1], criteria=criteria[1].strip(), evidence=evidence[1]))
    return result


def manifest(items):
    rows = ['# GitHub milestone manifest', '',
            'Generated from `PORTFOLIO_PLAN.md` by `python3 scripts/portfolio_plan.py --write-manifest`. Do not edit titles here independently.', '',
            '| Week | Milestone | Objective |', '| ---: | --- | --- |']
    for item in items:
        rows.append(f"| {item['week']} | Week {item['week']:02} - {item['title']} | {item['objective']} |")
    return '\n'.join(rows) + '\n'


def issue_body(item):
    return (f"## Objective\n\n{item['objective']}\n\n## Acceptance criteria\n\n{item['criteria']}\n\n"
            f"## Acceptance evidence\n\n{item['evidence']}\n\n"
            "## Working record\n\n- PR:\n- Actual validation and evidence:\n- Blockers / next action:\n\n"
            "Use PORTFOLIO_PLAN.md and ARTIFACT_CATALOG.md in this repository. Close only when criteria and review are complete.\n")


def existing_week(items, week):
    matches = [x for x in items if not x.get('pull_request') and
               re.match(rf'^Week 0?{week}(?:\s*[-:]|\s*$)', x.get('title', ''))]
    if len(matches) > 1:
        raise ValueError(f'Multiple existing records for Week {week}; reconcile manually')
    return matches[0] if matches else None


def gh_api(endpoint, payload=None):
    args = ['gh', 'api', endpoint]
    if payload is None:
        args += ['--paginate', '--slurp']
        pages = json.loads(subprocess.run(args, check=True, text=True, capture_output=True).stdout)
        return [item for page in pages for item in page]
    args += ['--method', 'POST', '--input', '-']
    return json.loads(subprocess.run(args, input=json.dumps(payload), check=True, text=True, capture_output=True).stdout)


def apply(items, kind, repo):
    # Read both open and closed records. Never duplicate completed weeks or reopen them.
    endpoint = f'repos/{repo}/{kind}'
    current = gh_api(endpoint + '?state=all&per_page=100')
    milestone_records = gh_api(f'repos/{repo}/milestones?state=all&per_page=100') if kind == 'issues' else []
    # Check ambiguity before any remote write.
    for item in items:
        existing_week(current, item['week'])
        if kind == 'issues':
            existing_week(milestone_records, item['week'])
    for item in items:
        week = item['week']
        title = f"Week {week:02}{' -' if kind == 'milestones' else ':'} {item['title']}"
        old = existing_week(current, week)
        if old:
            suffix = ' (title differs; update this existing record after plan review)' if old['title'] != title else ''
            print(f"Skip existing #{old['number']}: {old['title']}{suffix}")
            continue
        if kind == 'milestones':
            payload = dict(title=title, description=item['objective'])
        else:
            milestone = existing_week(milestone_records, week)
            if not milestone or milestone['title'] != f"Week {week:02} - {item['title']}":
                raise ValueError(f'Week {week}: create or align the milestone before creating an issue')
            payload = dict(title=title, body=issue_body(item), milestone=milestone['number'])
        created = gh_api(endpoint, payload)
        current.append(created)
        print(f"Created #{created['number']}: {title}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind', choices=['milestones', 'issues'], default='milestones')
    parser.add_argument('--repo', default=os.environ.get('GH_REPO'))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true', help='Create missing records via authenticated GitHub CLI')
    mode.add_argument('--check', action='store_true', help='Validate plan, manifest, catalog titles and local Markdown links')
    mode.add_argument('--write-manifest', action='store_true')
    args = parser.parse_args()
    items = weeks((ROOT / 'PORTFOLIO_PLAN.md').read_text())
    path = ROOT / '.github/milestones.md'
    if args.write_manifest:
        path.write_text(manifest(items))
        print('Updated .github/milestones.md')
    elif args.check:
        if path.read_text() != manifest(items):
            raise ValueError('Stale milestone manifest: run --write-manifest')
        catalog = (ROOT / 'ARTIFACT_CATALOG.md').read_text()
        for item in items:
            if f"Week {item['week']:02} - {item['title']}" not in catalog:
                raise ValueError(f"Catalog missing current Week {item['week']} title")
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', path.read_text()):
                if target.startswith(('http:', 'https:', 'mailto:', '#')):
                    continue
                local = target.split('#')[0]
                if local and not (path.parent / local).exists():
                    raise ValueError(f'Broken local link: {path.relative_to(ROOT)} → {target}')
        print('PASS: 16 complete plan sections, current manifest/catalog titles, and local Markdown file links')
    elif args.apply:
        if not args.repo or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', args.repo):
            raise ValueError('--apply requires --repo owner/repository (or GH_REPO)')
        apply(items, args.kind, args.repo)
    else:
        for item in items:
            print(f"\nWeek {item['week']:02} - {item['title']}\n")
            print(issue_body(item) if args.kind == 'issues' else item['objective'])
        print('\nOffline preview only. No GitHub data read or changed.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)
