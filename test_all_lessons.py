import json
import subprocess
import sys
import os
import tempfile
from pathlib import Path

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def test_python_lesson(lesson_id, code, expected_output):
    """Test a Python lesson by running the code and checking output."""
    try:
        # Create a temporary file for the code
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        try:
            # Run the Python code
            result = subprocess.run(
                [sys.executable, temp_file],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8'
            )

            actual_output = result.stdout.strip()
            expected = expected_output.strip()

            if result.returncode != 0:
                return {
                    'success': False,
                    'error': f'Runtime error: {result.stderr}',
                    'type': 'runtime'
                }

            if actual_output != expected:
                return {
                    'success': False,
                    'error': f'Output mismatch. Expected: "{expected}", Got: "{actual_output}"',
                    'type': 'output'
                }

            return {'success': True}

        finally:
            # Clean up temp file
            try:
                os.unlink(temp_file)
            except:
                pass

    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Execution timeout (>10s)',
            'type': 'timeout'
        }
    except SyntaxError as e:
        return {
            'success': False,
            'error': f'Syntax error: {str(e)}',
            'type': 'syntax'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Unexpected error: {str(e)}',
            'type': 'unexpected'
        }

def test_java_lesson(lesson_id, code, expected_output):
    """Test a Java lesson by compiling and running the code."""
    try:
        # Create a temporary directory for Java files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Java class must be named Main for this to work
            java_file = os.path.join(temp_dir, 'Main.java')

            # Write the code to file
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            # Compile the Java code
            compile_result = subprocess.run(
                ['javac', java_file],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8'
            )

            if compile_result.returncode != 0:
                return {
                    'success': False,
                    'error': f'Compilation error: {compile_result.stderr}',
                    'type': 'compilation'
                }

            # Run the compiled Java code
            run_result = subprocess.run(
                ['java', '-cp', temp_dir, 'Main'],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-8'
            )

            if run_result.returncode != 0:
                return {
                    'success': False,
                    'error': f'Runtime error: {run_result.stderr}',
                    'type': 'runtime'
                }

            actual_output = run_result.stdout.strip()
            expected = expected_output.strip()

            if actual_output != expected:
                return {
                    'success': False,
                    'error': f'Output mismatch. Expected: "{expected}", Got: "{actual_output}"',
                    'type': 'output'
                }

            return {'success': True}

    except subprocess.TimeoutExpired:
        return {
            'success': False,
            'error': 'Execution timeout (>10s)',
            'type': 'timeout'
        }
    except FileNotFoundError:
        return {
            'success': False,
            'error': 'Java compiler (javac) not found. Please install JDK.',
            'type': 'missing_compiler'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Unexpected error: {str(e)}',
            'type': 'unexpected'
        }

def test_all_lessons():
    """Test all lessons in both Python and Java tracks."""

    results = {
        'python': {'total': 0, 'passed': 0, 'failed': 0, 'errors': []},
        'java': {'total': 0, 'passed': 0, 'failed': 0, 'errors': []}
    }

    # Test Python lessons
    print("=" * 80)
    print("TESTING PYTHON LESSONS")
    print("=" * 80)

    try:
        with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
            python_lessons = json.load(f)

        for lesson in python_lessons:
            lesson_id = lesson.get('id', 'unknown')
            title = lesson.get('title', 'Untitled')
            code = lesson.get('fullSolution', '')
            expected = lesson.get('expectedOutput', '')

            results['python']['total'] += 1

            print(f"\nTesting Lesson {lesson_id}: {title}...", end=' ')

            result = test_python_lesson(lesson_id, code, expected)

            if result['success']:
                results['python']['passed'] += 1
                print("✓ PASSED")
            else:
                results['python']['failed'] += 1
                print(f"✗ FAILED")
                error_info = {
                    'id': lesson_id,
                    'title': title,
                    'error': result['error'],
                    'type': result['type']
                }
                results['python']['errors'].append(error_info)
                print(f"  Error: {result['error']}")

    except FileNotFoundError:
        print("ERROR: lessons-python.json not found!")
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in lessons-python.json: {e}")

    # Test Java lessons
    print("\n" + "=" * 80)
    print("TESTING JAVA LESSONS")
    print("=" * 80)

    try:
        with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
            java_lessons = json.load(f)

        for lesson in java_lessons:
            lesson_id = lesson.get('id', 'unknown')
            title = lesson.get('title', 'Untitled')
            code = lesson.get('fullSolution', '')
            expected = lesson.get('expectedOutput', '')

            results['java']['total'] += 1

            print(f"\nTesting Lesson {lesson_id}: {title}...", end=' ')

            result = test_java_lesson(lesson_id, code, expected)

            if result['success']:
                results['java']['passed'] += 1
                print("✓ PASSED")
            else:
                results['java']['failed'] += 1
                print(f"✗ FAILED")
                error_info = {
                    'id': lesson_id,
                    'title': title,
                    'error': result['error'],
                    'type': result['type']
                }
                results['java']['errors'].append(error_info)
                print(f"  Error: {result['error']}")

    except FileNotFoundError:
        print("ERROR: lessons-java.json not found!")
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in lessons-java.json: {e}")

    # Print summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    print(f"\nPython Lessons:")
    print(f"  Total: {results['python']['total']}")
    print(f"  Passed: {results['python']['passed']} ✓")
    print(f"  Failed: {results['python']['failed']} ✗")
    if results['python']['failed'] > 0:
        print(f"  Success Rate: {results['python']['passed']/results['python']['total']*100:.1f}%")

    print(f"\nJava Lessons:")
    print(f"  Total: {results['java']['total']}")
    print(f"  Passed: {results['java']['passed']} ✓")
    print(f"  Failed: {results['java']['failed']} ✗")
    if results['java']['failed'] > 0:
        print(f"  Success Rate: {results['java']['passed']/results['java']['total']*100:.1f}%")

    # Print detailed error report
    if results['python']['errors'] or results['java']['errors']:
        print("\n" + "=" * 80)
        print("DETAILED ERROR REPORT")
        print("=" * 80)

        if results['python']['errors']:
            print("\nPython Errors:")
            for err in results['python']['errors']:
                print(f"\n  Lesson {err['id']}: {err['title']}")
                print(f"    Type: {err['type']}")
                print(f"    Error: {err['error']}")

        if results['java']['errors']:
            print("\nJava Errors:")
            for err in results['java']['errors']:
                print(f"\n  Lesson {err['id']}: {err['title']}")
                print(f"    Type: {err['type']}")
                print(f"    Error: {err['error']}")

    return results

if __name__ == '__main__':
    results = test_all_lessons()

    # Exit with error code if any tests failed
    total_failed = results['python']['failed'] + results['java']['failed']
    sys.exit(0 if total_failed == 0 else 1)
