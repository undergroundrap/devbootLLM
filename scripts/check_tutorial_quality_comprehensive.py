#!/usr/bin/env python3
"""
Comprehensive tutorial quality check for all lessons.
"""

import json
import re

def check_tutorial_quality():
    print('=' * 80)
    print('COMPREHENSIVE TUTORIAL QUALITY CHECK')
    print('=' * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        py_data = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    all_lessons = py_data + java_data

    print(f'Checking {len(all_lessons)} lessons...')
    print()

    # Issues tracking
    issues = {
        'missing_tutorial': [],
        'too_short': [],  # < 500 chars
        'very_short': [],  # < 200 chars
        'no_sections': [],  # Missing h2 or h3 headers
        'no_code_examples': [],  # Missing code blocks
        'placeholder_content': [],  # Generic/placeholder text
        'poor_formatting': [],  # No formatting at all
    }

    for lesson in all_lessons:
        lid = lesson['id']
        title = lesson.get('title', 'Unknown')
        lang = lesson.get('language', 'unknown')
        tutorial = lesson.get('tutorial', '')
        additional = lesson.get('additionalExamples', '')

        # Check 1: Missing tutorial
        if not tutorial or not tutorial.strip():
            issues['missing_tutorial'].append((lid, lang, title))
            continue

        tutorial_len = len(tutorial)

        # Check 2: Tutorial length
        if tutorial_len < 200:
            issues['very_short'].append((lid, lang, title, tutorial_len))
        elif tutorial_len < 500:
            issues['too_short'].append((lid, lang, title, tutorial_len))

        # Check 3: Section headers (h2, h3, or h4)
        has_sections = bool(re.search(r'<h[234]', tutorial))
        if not has_sections and tutorial_len > 300:
            issues['no_sections'].append((lid, lang, title))

        # Check 4: Code examples (check both tutorial and additionalExamples)
        # Use regex to match code tags with or without attributes
        has_code_tutorial = bool(re.search(r'<code[^>]*>', tutorial)) or bool(re.search(r'<pre[^>]*>', tutorial)) or '```' in tutorial
        has_code_additional = bool(re.search(r'<code[^>]*>', additional)) or bool(re.search(r'<pre[^>]*>', additional)) or '```' in additional
        has_code = has_code_tutorial or has_code_additional
        if not has_code and tutorial_len > 500:
            issues['no_code_examples'].append((lid, lang, title))

        # Check 5: Placeholder/generic content
        placeholder_phrases = [
            'lorem ipsum',
            'FIXME',
            'placeholder content',
            'coming soon',
            'to be written',
        ]
        # Check for TODO but exclude if:
        # - It's part of "Todo List" in the title
        # - It's instructional content about removing TODOs
        has_placeholder = any(phrase.lower() in tutorial.lower() for phrase in placeholder_phrases)
        has_todo = 'TODO' in tutorial and 'todo list' not in title.lower() and 'remove todo' not in tutorial.lower()

        if has_placeholder or has_todo:
            issues['placeholder_content'].append((lid, lang, title))

        # Check 6: Poor formatting (just plain text, no HTML)
        has_formatting = bool(re.search(r'<[^>]+>', tutorial))
        if not has_formatting and tutorial_len > 100:
            issues['poor_formatting'].append((lid, lang, title))

    # Report results
    print('=' * 80)
    print('RESULTS BY ISSUE TYPE')
    print('=' * 80)
    print()

    total_issues = 0

    for issue_type, lessons in issues.items():
        if lessons:
            total_issues += len(lessons)
            print(f'[{issue_type.upper().replace("_", " ")}] {len(lessons)} lessons')
            for item in lessons[:5]:
                if len(item) == 3:
                    lid, lang, title = item
                    print(f'  Lesson {lid:4d} ({lang:6s}): {title[:50]}')
                else:
                    lid, lang, title, length = item
                    print(f'  Lesson {lid:4d} ({lang:6s}): {title[:50]} ({length} chars)')
            if len(lessons) > 5:
                print(f'  ... and {len(lessons) - 5} more')
            print()

    # Summary
    print('=' * 80)
    print('SUMMARY')
    print('=' * 80)
    print()

    if total_issues == 0:
        print('[SUCCESS] All tutorials are high quality!')
        print()
        print('All 2,107 lessons have:')
        print('  - Complete tutorials present')
        print('  - Adequate length (>500 chars)')
        print('  - Proper section structure')
        print('  - Code examples included')
        print('  - No placeholder content')
        print('  - Good HTML formatting')
        return True
    else:
        print(f'[WARNING] Found {total_issues} tutorial quality issues')
        print()
        print('Issues breakdown:')
        for issue_type, lessons in issues.items():
            if lessons:
                print(f'  {issue_type.replace("_", " ").title()}: {len(lessons)}')
        return False

if __name__ == '__main__':
    success = check_tutorial_quality()
    exit(0 if success else 1)
