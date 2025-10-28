import json
import re

def check_for_java_syntax(code):
    """Check if code contains Java-specific syntax"""
    java_indicators = [
        r'\bpublic\s+class\b',
        r'\bprivate\s+\w+\s+\w+',
        r'\bpublic\s+static\s+void\s+main',
        r'\bSystem\.out\.println',
        r'\bString\[\]',
        r'Map<.*?>',
        r'List<.*?>',
        r'ArrayList<.*?>',
        r'HashMap<.*?>',
        r'\bvoid\s+\w+\(',
        r'\bint\s+\w+\s*=',
        r'\bString\s+\w+\s*=',
        r'\/\/',  # Java-style comments at start of line
    ]

    for pattern in java_indicators:
        if re.search(pattern, code):
            return True
    return False

def check_for_python_syntax(code):
    """Check if code contains Python-specific syntax"""
    python_indicators = [
        r'\bdef\s+\w+\(',
        r'\bclass\s+\w+:',
        r'\bimport\s+\w+',
        r'\bfrom\s+\w+\s+import',
        r'\bprint\(',
        r'^#\s+',  # Python-style comments
        r':\s*$',  # Colon at end of line (Python syntax)
        r'\bNone\b',
        r'\bTrue\b',
        r'\bFalse\b',
        r'\bself\.',
    ]

    for pattern in python_indicators:
        if re.search(pattern, code, re.MULTILINE):
            return True
    return False

print("Checking language purity in all lessons...")
print("=" * 80)

# Check Java lessons
print("\n[JAVA LESSONS - Checking for Python code contamination]")
print("-" * 80)

with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

java_issues = []
for lesson in java_data['lessons']:
    code = lesson.get('fullSolution', '')
    initial = lesson.get('initialCode', '')

    has_python_in_solution = check_for_python_syntax(code)
    has_python_in_initial = check_for_python_syntax(initial)

    if has_python_in_solution or has_python_in_initial:
        java_issues.append({
            'id': lesson['id'],
            'title': lesson['title'],
            'in_solution': has_python_in_solution,
            'in_initial': has_python_in_initial
        })

if java_issues:
    print(f"\nFound {len(java_issues)} Java lessons with Python code:")
    for issue in java_issues[:10]:  # Show first 10
        where = []
        if issue['in_solution']: where.append('solution')
        if issue['in_initial']: where.append('initialCode')
        print(f"  - Lesson {issue['id']}: {issue['title']} [{', '.join(where)}]")
    if len(java_issues) > 10:
        print(f"  ... and {len(java_issues) - 10} more")
else:
    print("✓ All Java lessons contain only Java code")

# Check Python lessons
print("\n[PYTHON LESSONS - Checking for Java code contamination]")
print("-" * 80)

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

python_issues = []
for lesson in python_data['lessons']:
    code = lesson.get('fullSolution', '')
    initial = lesson.get('initialCode', '')

    has_java_in_solution = check_for_java_syntax(code)
    has_java_in_initial = check_for_java_syntax(initial)

    if has_java_in_solution or has_java_in_initial:
        python_issues.append({
            'id': lesson['id'],
            'title': lesson['title'],
            'in_solution': has_java_in_solution,
            'in_initial': has_java_in_initial
        })

if python_issues:
    print(f"\nFound {len(python_issues)} Python lessons with Java code:")
    for issue in python_issues[:10]:  # Show first 10
        where = []
        if issue['in_solution']: where.append('solution')
        if issue['in_initial']: where.append('initialCode')
        print(f"  - Lesson {issue['id']}: {issue['title']} [{', '.join(where)}]")
    if len(python_issues) > 10:
        print(f"  ... and {len(python_issues) - 10} more")
else:
    print("✓ All Python lessons contain only Python code")

# Summary
print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Java lessons with Python code: {len(java_issues)}")
print(f"Python lessons with Java code: {len(python_issues)}")

if len(java_issues) == 0 and len(python_issues) == 0:
    print("\n✓ All lessons have correct language-specific code!")
else:
    print(f"\n✗ Total issues to fix: {len(java_issues) + len(python_issues)}")

# Save detailed report
if java_issues or python_issues:
    with open('language_purity_report.json', 'w', encoding='utf-8') as f:
        json.dump({
            'java_issues': java_issues,
            'python_issues': python_issues
        }, f, indent=2)
    print("\nDetailed report saved to: language_purity_report.json")
