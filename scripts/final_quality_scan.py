#!/usr/bin/env python3
"""
Final comprehensive quality scan for all lessons.
Look for any remaining issues with tutorials, examples, placeholders, etc.
"""
import json
import re

def scan_lessons(filename, language):
    """Scan lessons for quality issues."""
    with open(filename, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    issues = {
        'placeholder_text': [],
        'generic_tutorials': [],
        'empty_examples': [],
        'missing_fields': [],
        'short_solutions': [],
        'todo_comments': [],
        'placeholder_outputs': [],
        'duplicate_descriptions': {}
    }

    descriptions_seen = {}

    for lesson in lessons:
        lid = lesson['id']
        title = lesson.get('title', '')

        # Check for missing critical fields
        if not lesson.get('fullSolution'):
            issues['missing_fields'].append((lid, title, 'missing fullSolution'))
        if not lesson.get('description'):
            issues['missing_fields'].append((lid, title, 'missing description'))
        if 'expectedOutput' not in lesson:
            issues['missing_fields'].append((lid, title, 'missing expectedOutput'))

        # Check solution length (very short = likely placeholder)
        solution = lesson.get('fullSolution', '')
        if solution and len(solution.strip()) < 50:
            issues['short_solutions'].append((lid, title, len(solution)))

        # Check for placeholder patterns in solution
        if solution:
            placeholder_patterns = [
                r'Complete!',
                r'Done!',
                r'TODO:.*Complete',
                r'Placeholder',
                r'Fix me',
                r'Your code here'
            ]
            for pattern in placeholder_patterns:
                if re.search(pattern, solution, re.IGNORECASE):
                    issues['placeholder_text'].append((lid, title, pattern))
                    break

        # Check expected output for placeholders
        expected = lesson.get('expectedOutput', '')
        if expected:
            if re.search(r'Complete!|Done!|Placeholder|TODO', expected, re.IGNORECASE):
                issues['placeholder_outputs'].append((lid, title, expected[:50]))

        # Check tutorial for generic/placeholder content
        tutorial = lesson.get('tutorial', '')
        if tutorial:
            generic_patterns = [
                r'Understanding\s+\w+\s*$',
                r'This lesson covers',
                r'Example code demonstrating',
                r'TODO:',
                r'<placeholder>',
                r'This foundational lesson'
            ]
            for pattern in generic_patterns:
                if re.search(pattern, tutorial, re.IGNORECASE):
                    issues['generic_tutorials'].append((lid, title, pattern))
                    break

        # Check example for placeholder or empty
        example = lesson.get('example', '')
        if not example or example.strip() == '':
            # Empty example is OK, not an issue
            pass
        elif re.search(r'Example code demonstrating|TODO|<placeholder>', example, re.IGNORECASE):
            issues['empty_examples'].append((lid, title, example[:50]))

        # Check for TODO comments in solutions
        if solution and 'TODO:' in solution:
            # Check if it's an instructional TODO (OK) or placeholder TODO (bad)
            if re.search(r'TODO:.*Complete|TODO:.*Implement|TODO:.*Fix', solution, re.IGNORECASE):
                issues['todo_comments'].append((lid, title))

        # Track duplicate descriptions
        desc = lesson.get('description', '').strip()
        if desc:
            if desc in descriptions_seen:
                descriptions_seen[desc].append(lid)
            else:
                descriptions_seen[desc] = [lid]

    # Find duplicate descriptions
    for desc, lesson_ids in descriptions_seen.items():
        if len(lesson_ids) > 1:
            issues['duplicate_descriptions'][desc[:50]] = lesson_ids

    return issues, len(lessons)

def print_report(issues, total_lessons, language):
    """Print quality report."""
    print(f"\n{'='*80}")
    print(f"{language.upper()} QUALITY SCAN - {total_lessons} lessons")
    print(f"{'='*80}")

    total_issues = 0

    for issue_type, items in issues.items():
        if issue_type == 'duplicate_descriptions':
            count = len(items)
            if count > 0:
                print(f"\n{issue_type.replace('_', ' ').title()}: {count}")
                for desc, lesson_ids in list(items.items())[:3]:
                    print(f"  '{desc}...' in lessons: {lesson_ids[:5]}")
                if count > 3:
                    print(f"  ... and {count - 3} more")
                total_issues += count
        else:
            count = len(items)
            if count > 0:
                print(f"\n{issue_type.replace('_', ' ').title()}: {count}")
                for item in items[:5]:
                    if len(item) == 2:
                        print(f"  Lesson {item[0]}: {item[1]}")
                    elif len(item) == 3:
                        print(f"  Lesson {item[0]}: {item[1]} - {item[2]}")
                if count > 5:
                    print(f"  ... and {count - 5} more")
                total_issues += count

    print(f"\n{'-'*80}")
    if total_issues == 0:
        print("✓ NO ISSUES FOUND - All lessons look good!")
    else:
        print(f"TOTAL ISSUES: {total_issues}")
    print(f"{'='*80}\n")

# Scan both Java and Python
print("\nFINAL QUALITY SCAN")
print("="*80)

java_issues, java_total = scan_lessons('public/lessons-java.json', 'Java')
print_report(java_issues, java_total, 'Java')

python_issues, python_total = scan_lessons('public/lessons-python.json', 'Python')
print_report(python_issues, python_total, 'Python')

# Summary
java_issue_count = sum(len(v) if not isinstance(v, dict) else len(v) for v in java_issues.values())
python_issue_count = sum(len(v) if not isinstance(v, dict) else len(v) for v in python_issues.values())
total_issue_count = java_issue_count + python_issue_count

print(f"\nGRAND TOTAL: {total_issue_count} issues across {java_total + python_total} lessons")
if total_issue_count == 0:
    print("✓✓✓ ALL LESSONS PASS QUALITY CHECKS ✓✓✓")
print()
