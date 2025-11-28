#!/usr/bin/env python3
"""
Detect lessons that are TRULY bad (only print statements describing concepts, no real code).
vs lessons that use print statements but actually demonstrate the concept.
"""

import json

def is_truly_bad(code, title):
    """
    Detect if lesson only describes a concept without showing real code.

    TRULY BAD: Just prints describing what something is
    OK: Uses print to show results of actual operations
    """

    lines = code.split('\n')

    # Remove comments and empty lines
    code_lines = [l.strip() for l in lines if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('//')]

    if len(code_lines) == 0:
        return True, "No code"

    # Count different types of lines
    print_lines = [l for l in code_lines if 'print(' in l or 'println(' in l or 'System.out' in l]

    # If ALL code is just print statements
    if len(print_lines) == len(code_lines):
        # If more than 10 print lines with NO real code, it's likely just narrative
        if len(print_lines) > 10:
            return True, f"Only print statements, no real code ({len(print_lines)} lines)"

        # Check if prints are describing concepts vs showing results
        describing_keywords = [
            'current state', 'phase ', 'step ', 'deploying', 'monitoring',
            'health checks', 'metrics', 'version:', '===', 'demonstration',
            'key concepts', 'benefits', 'trade-offs', 'understanding',
            'zero downtime', 'rollback', 'canary', 'strategy', 'pattern',
            'policy', 'compliance', 'security', 'authentication', 'requirements:',
            'solutions:', 'aws ', 'azure ', 'google cloud', 'hashicorp'
        ]

        describing_count = sum(1 for line in print_lines
                             if any(kw in line.lower() for kw in describing_keywords))

        # If more than 50% of prints are describing/narrating, it's bad
        if describing_count / len(print_lines) > 0.5:
            return True, f"Only narrative print statements ({describing_count}/{len(print_lines)})"

    # Check for actual code patterns (good)
    good_patterns = [
        'for ', 'while ', 'if ', '= ', 'def ', 'class ', 'return ',
        '.append(', '.split(', '.join(', '.replace(', '.lower(', '.upper(',
        '[', '{', 'try:', 'except:', 'with ', 'import ', 'from '
    ]

    has_real_code = any(pattern in code for pattern in good_patterns)

    if not has_real_code and len(print_lines) > 10:
        return True, "No real code patterns, only print statements"

    return False, "OK"


def main():
    print("=" * 80)
    print("DETECTING TRULY BAD LESSONS")
    print("=" * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    truly_bad = []

    # Check Python
    for lesson in python_data:
        code = lesson.get('fullSolution', '')
        title = lesson.get('title', '')

        bad, reason = is_truly_bad(code, title)

        if bad:
            truly_bad.append({
                'id': lesson['id'],
                'title': title,
                'language': 'Python',
                'reason': reason,
                'category': lesson.get('category', 'Unknown')
            })

    # Check Java
    for lesson in java_data:
        code = lesson.get('fullSolution', '')
        title = lesson.get('title', '')

        bad, reason = is_truly_bad(code, title)

        if bad:
            truly_bad.append({
                'id': lesson['id'],
                'title': title,
                'language': 'Java',
                'reason': reason,
                'category': lesson.get('category', 'Unknown')
            })

    print(f"Found {len(truly_bad)} TRULY BAD lessons")
    print()

    if truly_bad:
        print("=" * 80)
        print("LESSONS THAT NEED FIXING:")
        print("=" * 80)
        print()

        for item in truly_bad:
            print(f"Lesson {item['id']:4d} ({item['language']:6s}): {item['title']}")
            print(f"  Category: {item['category']}")
            print(f"  Reason: {item['reason']}")
            print()

    return len(truly_bad)

if __name__ == '__main__':
    total = main()
    print(f"\nTotal truly bad lessons: {total}")
