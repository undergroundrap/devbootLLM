"""
Test framework lessons using the ACTUAL platform validation logic
"""
import json
import tempfile
import subprocess
import os

def validate_java_like_platform(code):
    """Mimics the platform's Java validation logic"""
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, 'Main.java')
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)

            result = subprocess.run(['javac', filepath], capture_output=True, text=True, timeout=30, cwd=tmpdir)

            if result.returncode == 0:
                return True, "Compiles successfully"

            # Check if errors are only framework-related (platform logic from lines 113-121)
            compile_error = result.stderr
            is_only_framework = (compile_error and
                'class, interface, enum, or record expected' not in compile_error and
                'illegal start of expression' not in compile_error and
                'not a statement' not in compile_error and
                '; expected' not in compile_error and
                'reached end of file while parsing' not in compile_error and
                (('package' in compile_error and 'does not exist' in compile_error) or
                 'cannot find symbol' in compile_error))

            if is_only_framework:
                return True, "Syntax valid (framework imports missing)"
            else:
                return False, f"Syntax error: {compile_error[:200]}"

        except Exception as e:
            return False, f"Error: {str(e)}"

print("=" * 80)
print("FRAMEWORK VALIDATION - USING ACTUAL PLATFORM LOGIC")
print("=" * 80)

java_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

# Test all our upgraded framework lessons
framework_ids = [
    806, 809, 813, 814, 815, 817, 818,  # Spring Security
    802, 998,  # Portfolio
    820, 822, 824,  # Cloud
    889, 890, 892,  # Kafka
    924, 928, 1054,  # gRPC
    808, 1021, 1022, 1023  # OAuth2/Spring Cloud
]

passed = 0
failed = []

print("\nTesting upgraded Java framework lessons...")
print("-" * 80)

for lid in sorted(set(framework_ids)):
    lesson = next((l for l in java_lessons if l.get('id') == lid), None)
    if not lesson:
        continue

    title = lesson.get('title', '')
    code = lesson.get('fullSolution', '')

    success, msg = validate_java_like_platform(code)

    if success:
        passed += 1
        print(f"  [PASS] ID {lid:4d}: {title[:50]}")
    else:
        failed.append({'id': lid, 'title': title, 'reason': msg})
        print(f"  [FAIL] ID {lid:4d}: {title[:50]}")
        print(f"         {msg[:70]}")

print("\n" + "=" * 80)
print("RESULTS USING PLATFORM VALIDATION LOGIC")
print("=" * 80)
print(f"\nTotal tested: {len(set(framework_ids))}")
print(f"Passed: {passed} ({passed/len(set(framework_ids))*100:.1f}%)")
print(f"Failed: {len(failed)}")

if failed:
    print(f"\nFailed lessons:")
    for fail in failed:
        print(f"  ID {fail['id']}: {fail['title']}")

# Now test Python
print("\n" + "=" * 80)
print("PYTHON FRAMEWORK VALIDATION")
print("=" * 80)

py_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))
py_frameworks = [l for l in py_lessons if l.get('isFramework')]

py_passed = 0
py_failed = 0

for lesson in py_frameworks:
    code = lesson.get('fullSolution', '')
    try:
        compile(code, '<test>', 'exec')
        py_passed += 1
    except:
        py_failed += 1

print(f"\nTotal Python frameworks: {len(py_frameworks)}")
print(f"Syntax valid: {py_passed} ({py_passed/len(py_frameworks)*100:.1f}%)")
print(f"Syntax errors: {py_failed}")

print("\n" + "=" * 80)
print("FINAL SUMMARY")
print("=" * 80)

if passed == len(set(framework_ids)) and py_failed == 0:
    print("\n[SUCCESS] All framework lessons work with platform validation!")
    print("Students can click 'Solve Lesson' and see proper validation.")
    print()
    print("Platform behavior:")
    print("  - Python: Syntax validation with py_compile")
    print("  - Java: Compilation with javac (allows missing framework imports)")
    print("  - Framework lessons show message about syntax validation only")
else:
    print(f"\n[STATUS] Most framework lessons working")
    print(f"  Java: {passed}/{len(set(framework_ids))} pass")
    print(f"  Python: {py_passed}/{len(py_frameworks)} pass")
