#!/usr/bin/env python3
"""
Find lessons with placeholder/dummy implementations that teach nothing.
"""

import json
import re

def is_placeholder_lesson(code, title):
    """Detect if a lesson is just a placeholder."""
    issues = []

    # Normalize code
    code_lower = code.lower()

    # Pattern 1: Generic "Example implementation" placeholders
    if 'system.out.println("example implementation")' in code_lower:
        issues.append("Generic 'Example implementation' placeholder")

    # Pattern 2: Just println statements with no real logic
    lines = code.split('\n')
    code_lines = [l.strip() for l in lines if l.strip() and not l.strip().startswith('//')]
    println_count = sum(1 for l in code_lines if 'system.out.println' in l.lower() or 'print(' in l.lower())

    # If more than 70% of code is just print statements, it's likely a placeholder
    if len(code_lines) > 5 and println_count / len(code_lines) > 0.7:
        issues.append(f"Mostly println statements ({println_count}/{len(code_lines)} lines)")

    # Pattern 3: "Complete working example" but no actual implementation
    if 'complete working example' in code_lower and println_count > 5:
        issues.append("Claims 'complete working example' but only has print statements")

    # Pattern 4: "demonstration" or "demonstrate" in println
    if 'demonstration complete' in code_lower or 'demonstrate' in code_lower:
        # Check if there's actual logic
        has_logic = any(keyword in code_lower for keyword in [
            'if (', 'for (', 'while (', 'switch (', 'try {',
            'new ', '.add(', '.get(', '.set(', 'return ',
            '= new ', '[]', 'class ', 'interface '
        ])

        if not has_logic and println_count > 3:
            issues.append("Says 'demonstration' but no actual logic/implementation")

    # Pattern 5: Observer Pattern specific issue
    if 'observer pattern' in title.lower():
        if 'observerpattern demonstration complete' in code_lower.replace(' ', ''):
            issues.append("Observer Pattern lesson with no actual observer implementation")

    # Pattern 6: Excessive comments with minimal code
    comment_lines = sum(1 for l in lines if l.strip().startswith('//'))
    if comment_lines > 15 and len(code_lines) < 10:
        issues.append(f"Too many comments ({comment_lines}) vs actual code ({len(code_lines)})")

    # Pattern 7: Generic variable names with no real usage
    if '"demonstration"' in code_lower and 'demonstration =' not in code_lower:
        # It's just printing the word, not using a variable
        pass

    return issues

def main():
    print("=" * 80)
    print("FINDING PLACEHOLDER/DUMMY LESSONS")
    print("=" * 80)
    print()

    # Check Python lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    python_issues = []
    for lesson in python_data:
        code = lesson.get('fullSolution', '')
        title = lesson.get('title', '')
        issues = is_placeholder_lesson(code, title)

        if issues:
            python_issues.append({
                'id': lesson['id'],
                'title': title,
                'issues': issues,
                'code_length': len(code),
                'language': 'Python'
            })

    # Check Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    java_issues = []
    for lesson in java_data:
        code = lesson.get('fullSolution', '')
        title = lesson.get('title', '')
        issues = is_placeholder_lesson(code, title)

        if issues:
            java_issues.append({
                'id': lesson['id'],
                'title': title,
                'issues': issues,
                'code_length': len(code),
                'language': 'Java'
            })

    all_issues = python_issues + java_issues

    print(f"Found {len(python_issues)} Python lessons with placeholder code")
    print(f"Found {len(java_issues)} Java lessons with placeholder code")
    print(f"Total: {len(all_issues)} lessons need fixing")
    print()

    if all_issues:
        print("=" * 80)
        print("LESSONS WITH PLACEHOLDER/DUMMY CODE:")
        print("=" * 80)
        print()

        for item in all_issues[:50]:  # Show first 50
            print(f"Lesson {item['id']:4d} ({item['language']}): {item['title']}")
            for issue in item['issues']:
                print(f"  - {issue}")
            print()

        if len(all_issues) > 50:
            print(f"... and {len(all_issues) - 50} more issues")

        print()
        print("=" * 80)
        print(f"TOTAL: {len(all_issues)} lessons need real implementations")
        print("=" * 80)
    else:
        print("[SUCCESS] No placeholder lessons found!")

    return len(all_issues)

if __name__ == '__main__':
    total = main()
    print(f"\nTotal placeholder lessons: {total}")
