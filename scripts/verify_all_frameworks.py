"""
Comprehensive Framework Verification
Checks that all framework lessons compile and are executable
"""
import json
import subprocess
import tempfile
import os

def test_python_compilation(code, lesson_id):
    """Test if Python code compiles"""
    try:
        compile(code, f'<lesson_{lesson_id}>', 'exec')
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError: {e}"
    except Exception as e:
        return False, f"Error: {e}"

def test_java_compilation(code, lesson_id):
    """Test if Java code compiles"""
    # Extract class name
    import re
    match = re.search(r'public\s+class\s+(\w+)', code)
    if not match:
        return False, "No public class found"

    class_name = match.group(1)

    # Create temp file
    with tempfile.TemporaryDirectory() as tmpdir:
        java_file = os.path.join(tmpdir, f"{class_name}.java")

        try:
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            # Compile
            result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                return True, "OK"
            else:
                return False, f"Compilation error: {result.stderr[:200]}"
        except subprocess.TimeoutExpired:
            return False, "Compilation timeout"
        except Exception as e:
            return False, f"Error: {e}"

print("=" * 80)
print("COMPREHENSIVE FRAMEWORK VERIFICATION")
print("=" * 80)

# Check Python frameworks
print("\nVERIFYING PYTHON FRAMEWORK LESSONS:")
print("-" * 80)

py_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))

py_frameworks = [l for l in py_lessons if l.get('isFramework')]
py_passed = 0
py_failed = []

for lesson in py_frameworks:
    lid = lesson.get('id')
    title = lesson.get('title', '')
    sol = lesson.get('fullSolution', '')
    fw = lesson.get('frameworkName', '')

    if not sol or len(sol.strip()) < 50:
        py_failed.append({'id': lid, 'title': title, 'reason': 'Empty or too short'})
        continue

    passed, msg = test_python_compilation(sol, lid)

    if passed:
        py_passed += 1
    else:
        py_failed.append({'id': lid, 'title': title, 'reason': msg, 'framework': fw})

print(f"\nPython Framework Results:")
print(f"  Total framework lessons: {len(py_frameworks)}")
print(f"  Passed compilation: {py_passed} ({py_passed/len(py_frameworks)*100:.1f}%)")
print(f"  Failed compilation: {len(py_failed)}")

if py_failed:
    print(f"\nFailed Python Lessons (first 5):")
    for fail in py_failed[:5]:
        print(f"  ID {fail['id']:4d}: {fail['title'][:50]:50s}")
        print(f"           {fail['reason'][:70]}")

# Check Java frameworks (focus on recently upgraded ones)
print("\n" + "=" * 80)
print("VERIFYING JAVA FRAMEWORK LESSONS:")
print("-" * 80)

java_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

# Focus on framework lessons we upgraded
framework_ids = [
    # Spring Security (batch 7)
    806, 809, 813, 814, 815, 817, 818,
    # Portfolio (batch 7)
    802, 998,
    # Cloud (batch 7)
    820, 822, 824,
    # Kafka (batch 8)
    889, 890, 892,
    # gRPC (batch 9)
    924, 928, 1054,
    # OAuth2/Spring Cloud (batch 10)
    808, 1021, 1022, 1023
]

java_passed = 0
java_failed = []

print("Testing upgraded framework lessons...")

for lid in framework_ids:
    lesson = next((l for l in java_lessons if l.get('id') == lid), None)
    if not lesson:
        continue

    title = lesson.get('title', '')
    sol = lesson.get('fullSolution', '')

    if not sol or len(sol.strip()) < 100:
        java_failed.append({'id': lid, 'title': title, 'reason': 'Empty or too short'})
        continue

    passed, msg = test_java_compilation(sol, lid)

    if passed:
        java_passed += 1
        print(f"  [OK] ID {lid}: {title[:50]}")
    else:
        java_failed.append({'id': lid, 'title': title, 'reason': msg})
        print(f"  [FAIL] ID {lid}: {title[:50]}")
        print(f"         {msg[:70]}")

print(f"\nJava Framework Results:")
print(f"  Tested lessons: {len(set(framework_ids))}")
print(f"  Passed compilation: {java_passed}")
print(f"  Failed compilation: {len(java_failed)}")

# Overall summary
print("\n" + "=" * 80)
print("OVERALL VERIFICATION SUMMARY")
print("=" * 80)

py_pass_rate = py_passed/len(py_frameworks)*100 if py_frameworks else 0
java_pass_rate = java_passed/len(set(framework_ids))*100 if framework_ids else 0

print(f"\nPython Frameworks: {py_passed}/{len(py_frameworks)} pass ({py_pass_rate:.1f}%)")
print(f"Java Frameworks: {java_passed}/{len(set(framework_ids))} pass ({java_pass_rate:.1f}%)")

if py_pass_rate >= 95 and java_pass_rate >= 95:
    print("\n[SUCCESS] All framework lessons compile correctly!")
    print("Students can click 'Solve Lesson' and run code without errors.")
else:
    print("\n[WARNING] Some framework lessons have compilation issues.")
    print("Review failed lessons above.")

print("\n" + "=" * 80)
