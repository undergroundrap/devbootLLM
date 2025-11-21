#!/usr/bin/env python3
"""
Create detailed validation report with categorized issues.
"""

import json
import re


def analyze_warnings(lessons, language):
    """Analyze and categorize all warnings."""
    categories = {
        'no_hints': [],
        'no_todo_marker': [],
        'short_tutorial': [],
        'empty_examples': [],
        'few_tags': [],
        'short_description': []
    }

    for lesson in lessons:
        lid = lesson['id']
        title = lesson['title']

        # Check hints
        hints = lesson.get('hints', [])
        if not hints or len(hints) == 0:
            categories['no_hints'].append((lid, title))

        # Check TODO marker
        base_code = lesson.get('baseCode', '')
        if base_code and 'TODO' not in base_code and 'Your code here' not in base_code:
            categories['no_todo_marker'].append((lid, title))

        # Check tutorial length
        tutorial = lesson.get('tutorial', '')
        if tutorial and len(tutorial) < 100:
            categories['short_tutorial'].append((lid, title))

        # Check examples
        examples = lesson.get('additionalExamples', '')
        if not examples or len(examples) < 50:
            categories['empty_examples'].append((lid, title))

        # Check tags
        tags = lesson.get('tags', [])
        if not tags or len(tags) < 2:
            categories['few_tags'].append((lid, title))

        # Check description
        description = lesson.get('description', '')
        if description and len(description) < 20:
            categories['short_description'].append((lid, title))

    return categories


def main():
    """Generate detailed report."""
    print("\n" + "="*80)
    print("DETAILED VALIDATION REPORT")
    print("="*80)

    # Load lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    print("\nAnalyzing Java lessons...")
    java_cats = analyze_warnings(java_lessons, 'java')

    print("Analyzing Python lessons...")
    python_cats = analyze_warnings(python_lessons, 'python')

    # Report
    print("\n" + "="*80)
    print("JAVA WARNING CATEGORIES")
    print("="*80 + "\n")

    for cat, items in java_cats.items():
        print(f"{cat.replace('_', ' ').title()}: {len(items)} lessons")

    print("\n" + "="*80)
    print("PYTHON WARNING CATEGORIES")
    print("="*80 + "\n")

    for cat, items in python_cats.items():
        print(f"{cat.replace('_', ' ').title()}: {len(items)} lessons")

    # Samples
    print("\n" + "="*80)
    print("SAMPLE ISSUES (First 10 from each category)")
    print("="*80 + "\n")

    print("JAVA - Lessons with no TODO markers:")
    for lid, title in java_cats['no_todo_marker'][:10]:
        print(f"  Lesson {lid}: {title}")

    print("\nPYTHON - Lessons with no TODO markers:")
    for lid, title in python_cats['no_todo_marker'][:10]:
        print(f"  Lesson {lid}: {title}")

    print("\nJAVA - Lessons with no hints:")
    for lid, title in java_cats['no_hints'][:10]:
        print(f"  Lesson {lid}: {title}")

    print("\nPYTHON - Lessons with no hints:")
    for lid, title in python_cats['no_hints'][:10]:
        print(f"  Lesson {lid}: {title}")

    print("\n" + "="*80)


if __name__ == "__main__":
    main()
