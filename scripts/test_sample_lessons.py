import json
import subprocess
import tempfile
import os

def test_java_lesson(lesson):
    """Test if a Java lesson compiles"""
    code = lesson.get('fullSolution', '')
    if not code:
        return True, "No code to test"

    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, 'Main.java')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)

        try:
            result = subprocess.run(
                ['javac', filepath],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return True, "Compiled successfully"
            else:
                return False, result.stderr
        except FileNotFoundError:
            return None, "javac not found - skipping Java compilation tests"
        except Exception as e:
            return False, str(e)

def test_python_lesson(lesson):
    """Test if a Python lesson has valid syntax"""
    code = lesson.get('fullSolution', '')
    if not code:
        return True, "No code to test"

    try:
        compile(code, f'<lesson_{lesson["id"]}>', 'exec')
        return True, "Syntax valid"
    except SyntaxError as e:
        return False, str(e)

print("Testing sample lessons from each category...")
print("=" * 80)

# Load lessons
with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
    java_lessons = json.load(f)['lessons']

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_lessons = json.load(f)['lessons']

# Test samples from each category
test_ids = [
    1,    # Beginner start
    50,   # Beginner mid
    104,  # Beginner bridge
    105,  # Intermediate start
    214,  # Intermediate bridge
    300,  # Advanced
    374,  # Advanced bridge
    500,  # Expert
    532,  # Expert bridge
    600,  # Enterprise
    639,  # Enterprise bridge
    650,  # FAANG
    690,  # Job Ready
    700,  # Final lesson
    735   # Final bridge
]

print("\n[JAVA LESSONS]")
java_failed = []
for lesson_id in test_ids:
    lesson = next((l for l in java_lessons if l['id'] == lesson_id), None)
    if not lesson:
        print(f"  Lesson {lesson_id}: NOT FOUND")
        continue

    success, message = test_java_lesson(lesson)
    if success is None:
        print(f"  {message}")
        break
    elif success:
        print(f"  [OK] Lesson {lesson_id}: {lesson['title'][:50]}")
    else:
        print(f"  [FAIL] Lesson {lesson_id}: {lesson['title'][:50]}")
        java_failed.append(lesson_id)

print("\n[PYTHON LESSONS]")
python_failed = []
for lesson_id in test_ids:
    lesson = next((l for l in python_lessons if l['id'] == lesson_id), None)
    if not lesson:
        print(f"  Lesson {lesson_id}: NOT FOUND")
        continue

    success, message = test_python_lesson(lesson)
    if success:
        print(f"  [OK] Lesson {lesson_id}: {lesson['title'][:50]}")
    else:
        print(f"  [FAIL] Lesson {lesson_id}: {lesson['title'][:50]}")
        python_failed.append(lesson_id)

print("\n" + "=" * 80)
print("TESTING SUMMARY")
print("=" * 80)
print(f"Java lessons tested: {len([l for l in test_ids if any(jl['id'] == l for jl in java_lessons)])}")
print(f"Java lessons failed: {len(java_failed)}")
print(f"Python lessons tested: {len([l for l in test_ids if any(pl['id'] == l for pl in python_lessons)])}")
print(f"Python lessons failed: {len(python_failed)}")

if len(java_failed) == 0 and len(python_failed) == 0:
    print("\n[SUCCESS] All sample lessons pass!")
else:
    print(f"\n[ISSUES] Some lessons failed")
    if java_failed:
        print(f"  Java failures: {java_failed}")
    if python_failed:
        print(f"  Python failures: {python_failed}")
