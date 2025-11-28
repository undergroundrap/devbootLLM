#!/usr/bin/env python3
"""
Comprehensive quality check for all lessons.
Finds various quality issues beyond just placeholder code.
"""

import json
import re

def check_lesson_quality(lesson, language):
    """Check a lesson for various quality issues"""
    issues = []
    code = lesson.get('fullSolution', '')
    title = lesson.get('title', '')

    if not code.strip():
        return [("Empty code", "No solution provided")]

    lines = code.split('\n')

    # Remove empty lines for analysis
    non_empty_lines = [l for l in lines if l.strip()]

    # Count different types of lines
    comment_lines = [l for l in non_empty_lines if l.strip().startswith('#') or l.strip().startswith('//')]
    code_lines = [l for l in non_empty_lines if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('//')]

    # Issue 1: Too many comments (>70% of non-empty lines are comments)
    if len(non_empty_lines) > 10 and len(comment_lines) / len(non_empty_lines) > 0.7:
        issues.append(("Too many comments", f"{len(comment_lines)}/{len(non_empty_lines)} lines are comments"))

    # Issue 2: Too short (less than 5 lines of actual code for advanced lessons)
    difficulty = lesson.get('difficulty', '')
    if difficulty in ['Advanced', 'Expert'] and len(code_lines) < 5:
        issues.append(("Too short for difficulty", f"Only {len(code_lines)} lines for {difficulty} lesson"))

    # Issue 3: Only print statements (already covered by detect_truly_bad_lessons.py, but double-check)
    print_lines = [l for l in code_lines if 'print(' in l or 'println(' in l or 'System.out' in l]
    if len(print_lines) == len(code_lines) and len(print_lines) > 10:
        issues.append(("Only print statements", f"All {len(print_lines)} lines are prints"))

    # Issue 4: Generic placeholder text in code
    placeholder_patterns = [
        'TODO', 'FIXME', 'XXX', 'HACK',
        'placeholder', 'example implementation',
        'implement this', 'fill this in',
        'your code here', 'add code here'
    ]

    for pattern in placeholder_patterns:
        if pattern.lower() in code.lower():
            issues.append(("Placeholder text", f"Contains '{pattern}'"))
            break

    # Issue 5: Excessive repetition (same line repeated >3 times)
    line_counts = {}
    for line in code_lines:
        stripped = line.strip()
        if len(stripped) > 10:  # Only check substantial lines
            line_counts[stripped] = line_counts.get(stripped, 0) + 1

    for line, count in line_counts.items():
        if count > 3:
            issues.append(("Excessive repetition", f"Line repeated {count} times: {line[:50]}"))
            break

    # Issue 6: No real logic (no control structures for non-trivial lessons)
    if len(code_lines) > 15:
        has_logic = any(keyword in code for keyword in [
            'if ', 'for ', 'while ', 'def ', 'class ',
            'function ', 'switch ', 'try', 'catch'
        ])

        if not has_logic and 'Basics' not in title and 'Hello' not in title:
            issues.append(("No control structures", "No if/for/while/class/def in 15+ line lesson"))

    # Issue 7: Generic variable names throughout (x, y, z, foo, bar, baz, test)
    generic_vars = ['foo', 'bar', 'baz', 'test123', 'example', 'sample']
    generic_count = sum(1 for var in generic_vars if var in code.lower())

    if generic_count >= 3:
        issues.append(("Generic variable names", f"Uses {generic_count} generic names (foo/bar/test)"))

    # Issue 8: Commented out code (lines starting with # or // that look like code)
    commented_code_count = 0
    for line in comment_lines:
        # Remove comment markers
        content = line.strip().lstrip('#').lstrip('/').strip()
        # Check if it looks like code (has = or () or [])
        if any(char in content for char in ['=', '()', '[]', '{}']):
            commented_code_count += 1

    if commented_code_count > 5:
        issues.append(("Commented out code", f"{commented_code_count} lines of commented code"))

    # Issue 9: Very long solution (>300 lines might indicate copy-paste or bloat)
    if len(lines) > 300:
        issues.append(("Very long", f"{len(lines)} lines - may need simplification"))

    # Issue 10: Missing proper structure (for OOP lessons, no class definition)
    if 'OOP' in lesson.get('category', '') or 'Class' in title or 'Object' in title:
        if language == 'Python':
            if 'class ' not in code:
                issues.append(("Missing class", "OOP lesson with no class definition"))
        elif language == 'Java':
            if 'class ' not in code and 'interface ' not in code:
                issues.append(("Missing class", "OOP lesson with no class/interface"))

    return issues

def main():
    print("=" * 80)
    print("COMPREHENSIVE LESSON QUALITY CHECK")
    print("=" * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    all_issues = []

    # Check Python lessons
    print("Checking Python lessons...")
    for lesson in python_data:
        issues = check_lesson_quality(lesson, 'Python')
        if issues:
            all_issues.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Python',
                'category': lesson.get('category', 'Unknown'),
                'difficulty': lesson.get('difficulty', 'Unknown'),
                'issues': issues
            })

    # Check Java lessons
    print("Checking Java lessons...")
    for lesson in java_data:
        issues = check_lesson_quality(lesson, 'Java')
        if issues:
            all_issues.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'language': 'Java',
                'category': lesson.get('category', 'Unknown'),
                'difficulty': lesson.get('difficulty', 'Unknown'),
                'issues': issues
            })

    print(f"Found {len(all_issues)} lessons with quality issues")
    print()

    if all_issues:
        # Group by issue type
        from collections import defaultdict
        by_issue_type = defaultdict(list)

        for item in all_issues:
            for issue_type, issue_desc in item['issues']:
                by_issue_type[issue_type].append(item)

        print("=" * 80)
        print("ISSUES BY TYPE:")
        print("=" * 80)
        print()

        for issue_type, items in sorted(by_issue_type.items()):
            print(f"{issue_type}: {len(items)} lessons")
            for item in items[:5]:  # Show first 5
                print(f"  Lesson {item['id']:4d} ({item['language']:6s}): {item['title'][:50]}")
            if len(items) > 5:
                print(f"  ... and {len(items) - 5} more")
            print()

        # Show high priority issues
        high_priority = [
            "Empty code", "Placeholder text", "Only print statements",
            "Missing class", "No control structures"
        ]

        critical = [item for item in all_issues
                   if any(issue[0] in high_priority for issue in item['issues'])]

        if critical:
            print("=" * 80)
            print(f"HIGH PRIORITY ISSUES ({len(critical)} lessons):")
            print("=" * 80)
            print()

            for item in critical[:20]:
                print(f"Lesson {item['id']:4d} ({item['language']:6s}): {item['title']}")
                for issue_type, issue_desc in item['issues']:
                    if issue_type in high_priority:
                        print(f"  ! {issue_type}: {issue_desc}")
                print()
    else:
        print("=" * 80)
        print("[SUCCESS] No quality issues found!")
        print("=" * 80)

    return len(all_issues)

if __name__ == '__main__':
    total = main()
    print(f"\nTotal lessons with issues: {total}")
