import json
import sys

def check_python_syntax(code, lesson_id, title):
    """Check if Python code has basic syntax issues"""
    try:
        compile(code, f'<lesson_{lesson_id}>', 'exec')
        return None
    except SyntaxError as e:
        return f"Lesson {lesson_id} ({title}): {e}"

def check_java_syntax(code, lesson_id, title):
    """Check for common Java syntax issues"""
    issues = []

    # Basic checks
    if 'public class Main' not in code and 'class Main' not in code:
        issues.append(f"Lesson {lesson_id} ({title}): Missing 'class Main'")

    # Check for unmatched braces
    open_braces = code.count('{')
    close_braces = code.count('}')
    if open_braces != close_braces:
        issues.append(f"Lesson {lesson_id} ({title}): Unmatched braces ({{ {open_braces} vs }} {close_braces})")

    # Check for unmatched parentheses
    open_parens = code.count('(')
    close_parens = code.count(')')
    if open_parens != close_parens:
        issues.append(f"Lesson {lesson_id} ({title}): Unmatched parentheses")

    return issues

# Check Java lessons
print("Checking Java lessons...")
print("=" * 80)

with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

java_issues = []
for lesson in java_data['lessons']:
    code = lesson.get('fullSolution', '')
    if code:
        issues = check_java_syntax(code, lesson['id'], lesson['title'])
        if issues:
            java_issues.extend(issues)

if java_issues:
    print(f"\nFound {len(java_issues)} Java issues:")
    for issue in java_issues[:20]:  # Show first 20
        print(f"  - {issue}")
else:
    print("No Java syntax issues found!")

print("\n" + "=" * 80)
print("Checking Python lessons...")
print("=" * 80)

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

python_issues = []
for lesson in python_data['lessons']:
    code = lesson.get('fullSolution', '')
    if code:
        error = check_python_syntax(code, lesson['id'], lesson['title'])
        if error:
            python_issues.append(error)

if python_issues:
    print(f"\nFound {len(python_issues)} Python issues:")
    for issue in python_issues[:20]:  # Show first 20
        print(f"  - {issue}")
else:
    print("No Python syntax issues found!")

print("\n" + "=" * 80)
print(f"Summary: {len(java_issues)} Java issues, {len(python_issues)} Python issues")
