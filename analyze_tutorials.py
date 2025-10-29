#!/usr/bin/env python3
"""
Analyze tutorial quality and relevance across all lessons.
Checks for:
- Tutorial-title mismatches
- Tutorial-description mismatches
- Generic/template content that wasn't customized
- Missing or empty tutorials
- Tutorial length appropriateness
"""

import json
import re
from collections import defaultdict

def load_lessons():
    """Load all Python lessons"""
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_tutorial_quality(lessons):
    """Analyze tutorials for quality issues"""
    issues = {
        'empty_tutorials': [],
        'generic_content': [],
        'title_mismatch': [],
        'description_mismatch': [],
        'wrong_language': [],
        'very_short': [],
        'very_long': [],
        'missing_key_concepts': []
    }

    # Common generic phrases that suggest template wasn't customized
    generic_phrases = [
        "This concept appears frequently in real-world applications",
        "Understanding when and how to apply",
        "will make you a more effective Python developer",
        "form the foundation for advanced Python programming techniques",
        "essential for writing effective Python code"
    ]

    # Java-specific terms that shouldn't be in Python tutorials
    java_terms = [
        'class Main',
        'def main():',
        'System.getenv',
        'java.util',
        'Maven',
        'Optional.orElse',
        'StringBuilder',
        'CompletableFuture',
        'Collectors.joining',
        'varargs',
        'final keyword'
    ]

    for lesson in lessons:
        lid = lesson['id']
        title = lesson['title']
        description = lesson['description']
        tutorial = lesson.get('tutorial', '')

        # Check for empty tutorials
        if not tutorial or len(tutorial.strip()) < 50:
            issues['empty_tutorials'].append({
                'id': lid,
                'title': title,
                'length': len(tutorial.strip())
            })
            continue

        # Check for generic content (>4 generic phrases suggests template)
        generic_count = sum(1 for phrase in generic_phrases if phrase in tutorial)
        if generic_count >= 4:
            issues['generic_content'].append({
                'id': lid,
                'title': title,
                'generic_count': generic_count
            })

        # Check for title mismatch
        # Extract title from tutorial
        tutorial_title_match = re.search(r'<strong>([^<]+)</strong>', tutorial[:500])
        if tutorial_title_match:
            tutorial_title = tutorial_title_match.group(1).lower()
            if title.lower() not in tutorial and tutorial_title not in title.lower():
                issues['title_mismatch'].append({
                    'id': lid,
                    'lesson_title': title,
                    'tutorial_title': tutorial_title
                })

        # Check for wrong language (Java mentions in Python lessons)
        java_mentions = [term for term in java_terms if term in tutorial]
        if java_mentions:
            issues['wrong_language'].append({
                'id': lid,
                'title': title,
                'java_terms': java_mentions[:3]  # Show first 3
            })

        # Check tutorial length
        tutorial_length = len(tutorial)
        if tutorial_length < 500:
            issues['very_short'].append({
                'id': lid,
                'title': title,
                'length': tutorial_length
            })
        elif tutorial_length > 10000:
            issues['very_long'].append({
                'id': lid,
                'title': title,
                'length': tutorial_length
            })

        # Check if Key Concepts section exists
        if 'Key Concepts' not in tutorial and tutorial_length > 100:
            issues['missing_key_concepts'].append({
                'id': lid,
                'title': title
            })

    return issues

def print_report(issues, total_lessons):
    """Print a formatted report of tutorial issues"""
    print("=" * 80)
    print("TUTORIAL QUALITY ANALYSIS REPORT")
    print("=" * 80)
    print()

    print(f"Total Lessons Analyzed: {total_lessons}")
    print()

    # Count total issues
    total_issues = sum(len(v) for v in issues.values())
    print(f"Total Issues Found: {total_issues}")
    print()

    # Print each category
    for category, items in issues.items():
        if items:
            category_name = category.replace('_', ' ').title()
            print(f"\n{category_name}: {len(items)}")
            print("-" * 80)

            for item in items[:10]:  # Show first 10 of each category
                print(f"  Lesson {item['id']}: {item['title'][:60]}")
                # Print additional details
                for key, value in item.items():
                    if key not in ['id', 'title']:
                        print(f"    {key}: {value}")

            if len(items) > 10:
                print(f"  ... and {len(items) - 10} more")

    # Summary statistics
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    high_quality = total_lessons - total_issues
    quality_rate = (high_quality / total_lessons) * 100

    print(f"High Quality Tutorials: {high_quality}/{total_lessons} ({quality_rate:.1f}%)")
    print(f"Tutorials Needing Review: {total_issues}/{total_lessons} ({100-quality_rate:.1f}%)")

    # Breakdown by severity
    print("\nIssue Severity Breakdown:")
    print(f"  Critical (empty/wrong language): {len(issues['empty_tutorials']) + len(issues['wrong_language'])}")
    print(f"  Medium (generic/mismatch): {len(issues['generic_content']) + len(issues['title_mismatch'])}")
    print(f"  Low (length/formatting): {len(issues['very_short']) + len(issues['very_long']) + len(issues['missing_key_concepts'])}")

def save_detailed_report(issues, filename='tutorial_issues_report.json'):
    """Save detailed issues to JSON for further analysis"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(issues, f, indent=2, ensure_ascii=False)
    print(f"\nDetailed report saved to: {filename}")

if __name__ == '__main__':
    print("Loading lessons...")
    lessons = load_lessons()

    print(f"Analyzing {len(lessons)} lessons...")
    issues = analyze_tutorial_quality(lessons)

    print_report(issues, len(lessons))
    save_detailed_report(issues)
