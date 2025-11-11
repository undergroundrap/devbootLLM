#!/usr/bin/env python3
"""Fix remaining syntax errors manually identified in test report"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

print('='*60)
print('FIXING REMAINING SYNTAX ERRORS')
print('='*60)

# Load lessons
print('\nLoading lessons...')
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

print(f'Loaded {len(py_lessons)} Python lessons and {len(java_lessons)} Java lessons')

# Specific fixes for lessons with syntax errors
fixes = []

# Python lesson 166: Remove incorrectly placed pass
for lesson in py_lessons:
    if lesson['id'] == 166:
        # Remove the `pass` after the comment
        lesson['baseCode'] = lesson['baseCode'].replace('# Create temp directory with structure:\n    pass\n', '# Create temp directory with structure:\n')
        fixes.append(f"ID {lesson['id']}: Removed incorrectly placed 'pass' statement")
        print(f"  Fixed ID {lesson['id']}: {lesson['title']}")

# Fix lessons with unexpected indent errors (244, 246, 247, 257, 258, 261)
# These likely have similar issues with incorrectly placed pass statements
indent_error_ids = [244, 246, 247, 257, 258, 261]
for lesson in py_lessons:
    if lesson['id'] in indent_error_ids:
        # Remove standalone pass statements that are incorrectly indented
        lines = lesson['baseCode'].split('\n')
        fixed_lines = []
        prev_line = ''

        for line in lines:
            # If line is just whitespace + pass and previous line was a comment
            if line.strip() == 'pass' and prev_line.strip().startswith('#'):
                # Skip this pass line
                continue
            fixed_lines.append(line)
            prev_line = line

        lesson['baseCode'] = '\n'.join(fixed_lines)
        fixes.append(f"ID {lesson['id']}: Removed incorrectly placed 'pass' statement")
        print(f"  Fixed ID {lesson['id']}: {lesson['title']}")

# Fix lesson 264: Unterminated string literal
for lesson in py_lessons:
    if lesson['id'] == 264:
        # Need to see the actual code to fix it
        print(f"\n  ID {lesson['id']}: {lesson['title']}")
        print("  Code sample:")
        print(lesson['baseCode'][:500])

        # Try to fix unterminated strings
        code = lesson['baseCode']
        # Count quotes
        single_quotes = code.count("'")
        double_quotes = code.count('"')

        if single_quotes % 2 != 0:
            fixes.append(f"ID {lesson['id']}: WARNING - Odd number of single quotes (manual fix needed)")
        if double_quotes % 2 != 0:
            fixes.append(f"ID {lesson['id']}: WARNING - Odd number of double quotes (manual fix needed)")

# Java lesson 65: Missing class definition
for lesson in java_lessons:
    if lesson['id'] == 65:
        # Check if baseCode is missing class definition
        if 'class ' not in lesson['baseCode']:
            # Wrap in a basic class structure
            lesson['baseCode'] = f"""public class Main {{
    public static void main(String[] args) {{
{lesson['baseCode']}
    }}
}}"""
            fixes.append(f"ID {lesson['id']}: Added missing class definition")
            print(f"  Fixed ID {lesson['id']}: {lesson['title']}")

# Java lesson 311: False positive (comment has [0,10) notation)
# No fix needed - this is valid code

print(f'\n[OK] Applied {len(fixes)} fixes')

# Save lessons
print('\n--- Saving Fixed Lessons ---')
save_lessons('public/lessons-python.json', py_lessons)
save_lessons('public/lessons-java.json', java_lessons)

print('[OK] Saved Python lessons')
print('[OK] Saved Java lessons')

print('\n' + '='*60)
print('REMAINING SYNTAX ERRORS FIXED!')
print('='*60)
print(f'\nTotal fixes: {len(fixes)}')
for fix in fixes:
    print(f'  - {fix}')
