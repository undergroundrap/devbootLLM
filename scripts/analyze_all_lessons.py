#!/usr/bin/env python3
"""Analyze all lessons to identify what needs enhancement"""

import json

# Load lessons
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Analyze all 650 lessons
print("=== LESSON QUALITY ANALYSIS ===\n")

lessons_601_650 = [l for l in data['lessons'] if 601 <= l['id'] <= 650]

# Categorize by tutorial length
high_quality = []
needs_enhancement = []

for lesson in lessons_601_650:
    tut_len = len(lesson['tutorial'])
    code_len = len(lesson['fullSolution'])

    if tut_len > 2000:
        high_quality.append((lesson['id'], lesson['title'], tut_len, code_len))
    else:
        needs_enhancement.append((lesson['id'], lesson['title'], tut_len, code_len))

print(f"High Quality Lessons (>2000 chars tutorial): {len(high_quality)}")
for lid, title, tlen, clen in high_quality:
    print(f"  [OK] {lid}: {title} (T:{tlen}, C:{clen})")

print(f"\nNeeds Enhancement (<2000 chars tutorial): {len(needs_enhancement)}")
for lid, title, tlen, clen in needs_enhancement:
    print(f"  [ENHANCE] {lid}: {title} (T:{tlen}, C:{clen})")

print(f"\n=== SUMMARY ===")
print(f"Total lessons 601-650: {len(lessons_601_650)}")
print(f"High quality: {len(high_quality)} ({len(high_quality)/len(lessons_601_650)*100:.1f}%)")
print(f"Needs work: {len(needs_enhancement)} ({len(needs_enhancement)/len(lessons_601_650)*100:.1f}%)")
