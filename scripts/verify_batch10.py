#!/usr/bin/env python3
"""Verify batch 10 upgrades are pure Java"""

import json

lessons_file = r'c:\devbootLLM-app\public\lessons-java.json'

with open(lessons_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

target_ids = [808, 1021, 1022, 1023]
lessons = [l for l in data if l['id'] in target_ids]

print('VERIFYING PURE JAVA CODE (NO MARKDOWN)')
print('=' * 70)
print()

all_pass = True

for lesson in sorted(lessons, key=lambda x: x['id']):
    code = lesson['fullSolution']
    has_markdown_blocks = '```' in code
    has_many_headers = code.count('\n#') > 2
    starts_with_import = code.strip().startswith('import')

    status = 'PASS' if starts_with_import and not has_markdown_blocks else 'FAIL'
    if status == 'FAIL':
        all_pass = False

    print(f"ID {lesson['id']}: {lesson['title'][:40]:40}")
    print(f"  Length: {len(code):>6,} chars")
    print(f"  Starts with import: {starts_with_import}")
    print(f"  Has markdown blocks: {has_markdown_blocks}")
    print(f"  Status: {status}")
    print()

print('=' * 70)
if all_pass:
    print('SUCCESS: All 4 lessons are pure Java code!')
else:
    print('FAILURE: Some lessons contain markdown!')
print('=' * 70)
