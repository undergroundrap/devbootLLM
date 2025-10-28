import json

def has_java_contamination(code):
    """Check if Python code actually contains Java code (not just similar patterns)"""
    if not code or not code.strip():
        return False

    # Strong Java indicators that shouldn't be in Python
    java_signatures = [
        'public class',
        'public static void main',
        'System.out.println',
        'private class',
        'protected class',
        ') {',  # Java method/control structure opening
        '};',   # Java statement ending
    ]

    for sig in java_signatures:
        if sig in code:
            return True
    return False

def has_python_contamination(code):
    """Check if Java code actually contains Python code"""
    if not code or not code.strip():
        return False

    # Strong Python indicators that shouldn't be in Java
    # (but be careful not to flag comments)
    lines = code.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') and not stripped.startswith('# '):
            # Could be a preprocessor directive in Java, skip
            continue

        # Check for Python-specific patterns not in comments
        if not stripped.startswith('//') and not stripped.startswith('/*') and not stripped.startswith('*'):
            if stripped.startswith('def '):
                return True
            if stripped.startswith('import ') and 'java' not in stripped:
                return True
            if stripped.startswith('from ') and 'import' in stripped:
                return True
            if 'print(' in stripped and 'System.out.println' not in code:
                return True

    return False

print("Checking for actual code contamination...")
print("=" * 80)

# Check Python lessons for Java code
print("\n[PYTHON LESSONS]")
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

python_contaminated = []
for lesson in python_data['lessons']:
    code = lesson.get('fullSolution', '')
    initial = lesson.get('initialCode', '')

    if has_java_contamination(code) or has_java_contamination(initial):
        python_contaminated.append(lesson['id'])
        print(f"  [!] Lesson {lesson['id']}: {lesson['title']}")

if not python_contaminated:
    print("  [OK] All Python lessons contain only Python code")
else:
    print(f"\n  Found {len(python_contaminated)} Python lessons with Java code")

# Check Java lessons for Python code
print("\n[JAVA LESSONS]")
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_data = json.load(f)

java_contaminated = []
for lesson in java_data['lessons']:
    code = lesson.get('fullSolution', '')
    initial = lesson.get('initialCode', '')

    if has_python_contamination(code) or has_python_contamination(initial):
        java_contaminated.append(lesson['id'])
        print(f"  [!] Lesson {lesson['id']}: {lesson['title']}")

if not java_contaminated:
    print("  [OK] All Java lessons contain only Java code")
else:
    print(f"\n  Found {len(java_contaminated)} Java lessons with Python code")

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Python lessons with Java contamination: {len(python_contaminated)}")
print(f"Java lessons with Python contamination: {len(java_contaminated)}")
print(f"Total issues: {len(python_contaminated) + len(java_contaminated)}")

if len(python_contaminated) + len(java_contaminated) == 0:
    print("\n[SUCCESS] All lessons have pure language-specific code!")
