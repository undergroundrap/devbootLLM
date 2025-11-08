#!/usr/bin/env python3
import json
import subprocess
import tempfile
import os
import sys
import random

def test_python_solution(lesson):
    """Test if a Python solution compiles and runs"""
    lesson_id = lesson['id']
    title = lesson['title']
    solution = lesson.get('fullSolution', '')
    expected = lesson.get('expectedOutput', '')

    if not solution or len(solution.strip()) < 5:
        return {'status': 'skip', 'reason': 'No solution provided'}

    # Create temp file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
        f.write(solution)
        temp_file = f.name

    try:
        # Run Python code
        result = subprocess.run(
            ['python', temp_file],
            capture_output=True,
            text=True,
            timeout=5,
            encoding='utf-8',
            errors='replace'
        )

        # Check for compilation/runtime errors
        if result.returncode != 0:
            return {
                'status': 'error',
                'error': result.stderr,
                'code': result.returncode
            }

        # Get output
        actual_output = result.stdout.strip()

        # Compare with expected (if provided)
        if expected:
            expected_clean = expected.strip()
            if actual_output != expected_clean:
                return {
                    'status': 'mismatch',
                    'expected': expected_clean,
                    'actual': actual_output
                }

        return {
            'status': 'success',
            'output': actual_output
        }

    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'reason': 'Execution took too long'}
    except Exception as e:
        return {'status': 'exception', 'error': str(e)}
    finally:
        # Clean up
        try:
            os.unlink(temp_file)
        except:
            pass

def test_java_solution(lesson):
    """Test if a Java solution compiles and runs"""
    lesson_id = lesson['id']
    title = lesson['title']
    solution = lesson.get('fullSolution', '')
    expected = lesson.get('expectedOutput', '')

    if not solution or len(solution.strip()) < 10:
        return {'status': 'skip', 'reason': 'No solution provided'}

    # Extract class name from solution
    import re
    match = re.search(r'public\s+class\s+(\w+)', solution)
    if not match:
        return {'status': 'error', 'error': 'No public class found in solution'}

    class_name = match.group(1)

    # Create temp directory
    temp_dir = tempfile.mkdtemp()
    java_file = os.path.join(temp_dir, f'{class_name}.java')

    try:
        # Write Java file
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(solution)

        # Compile
        compile_result = subprocess.run(
            ['javac', java_file],
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8',
            errors='replace'
        )

        if compile_result.returncode != 0:
            return {
                'status': 'compile_error',
                'error': compile_result.stderr
            }

        # Run
        run_result = subprocess.run(
            ['java', '-cp', temp_dir, class_name],
            capture_output=True,
            text=True,
            timeout=5,
            encoding='utf-8',
            errors='replace'
        )

        if run_result.returncode != 0:
            return {
                'status': 'runtime_error',
                'error': run_result.stderr
            }

        # Get output (combine stdout and stderr since Java logging goes to stderr)
        actual_output = (run_result.stdout + run_result.stderr).strip()

        # Compare with expected (if provided)
        if expected:
            expected_clean = expected.strip()
            if actual_output != expected_clean:
                return {
                    'status': 'mismatch',
                    'expected': expected_clean,
                    'actual': actual_output
                }

        return {
            'status': 'success',
            'output': actual_output
        }

    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'reason': 'Execution took too long'}
    except Exception as e:
        return {'status': 'exception', 'error': str(e)}
    finally:
        # Clean up
        try:
            import shutil
            shutil.rmtree(temp_dir)
        except:
            pass

def test_language(filename, language, test_func, sample_size=50):
    """Test solutions for a language"""
    with open(filename, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f"\n{'='*80}")
    print(f"{language.upper()} SOLUTION TESTING")
    print(f"{'='*80}\n")

    # Test all lessons but report sample
    print(f"Testing all {len(lessons)} lessons...")

    results = {
        'success': [],
        'error': [],
        'compile_error': [],
        'runtime_error': [],
        'mismatch': [],
        'timeout': [],
        'skip': [],
        'exception': []
    }

    # Test lessons
    for i, lesson in enumerate(lessons):
        if (i + 1) % 50 == 0:
            print(f"  Tested {i + 1}/{len(lessons)} lessons...")

        result = test_func(lesson)
        status = result['status']

        results[status].append({
            'id': lesson['id'],
            'title': lesson['title'],
            'result': result
        })

    print(f"  Completed {len(lessons)}/{len(lessons)} lessons\n")

    # Report results
    print(f"{'='*80}")
    print(f"RESULTS SUMMARY")
    print(f"{'='*80}\n")

    total_tested = len(lessons) - len(results['skip'])
    success_count = len(results['success'])

    print(f"Total lessons: {len(lessons)}")
    print(f"Tested: {total_tested}")
    print(f"Skipped: {len(results['skip'])}")
    print(f"\nSuccessful: {success_count}/{total_tested} ({success_count/total_tested*100:.1f}%)")

    if results['compile_error']:
        print(f"\nCompile errors: {len(results['compile_error'])}")
        for item in results['compile_error'][:5]:
            print(f"  Lesson {item['id']}: {item['title']}")
            error = item['result']['error'][:200]
            print(f"    {error}")
        if len(results['compile_error']) > 5:
            print(f"  ... and {len(results['compile_error']) - 5} more")

    if results['runtime_error']:
        print(f"\nRuntime errors: {len(results['runtime_error'])}")
        for item in results['runtime_error'][:5]:
            print(f"  Lesson {item['id']}: {item['title']}")
            error = item['result']['error'][:200]
            print(f"    {error}")
        if len(results['runtime_error']) > 5:
            print(f"  ... and {len(results['runtime_error']) - 5} more")

    if results['error']:
        print(f"\nOther errors: {len(results['error'])}")
        for item in results['error'][:5]:
            print(f"  Lesson {item['id']}: {item['title']}")
            error = item['result'].get('error', item['result'].get('reason', 'Unknown'))
            print(f"    {error[:200]}")
        if len(results['error']) > 5:
            print(f"  ... and {len(results['error']) - 5} more")

    if results['mismatch']:
        print(f"\nOutput mismatches: {len(results['mismatch'])}")
        for item in results['mismatch'][:5]:
            print(f"  Lesson {item['id']}: {item['title']}")
            print(f"    Expected: {item['result']['expected'][:100]}")
            print(f"    Actual:   {item['result']['actual'][:100]}")
        if len(results['mismatch']) > 5:
            print(f"  ... and {len(results['mismatch']) - 5} more")

    if results['timeout']:
        print(f"\nTimeouts: {len(results['timeout'])}")
        for item in results['timeout'][:5]:
            print(f"  Lesson {item['id']}: {item['title']}")

    if results['exception']:
        print(f"\nExceptions: {len(results['exception'])}")
        for item in results['exception'][:3]:
            print(f"  Lesson {item['id']}: {item['title']}")
            print(f"    {item['result']['error'][:200]}")

    # Overall status
    print(f"\n{'='*80}")
    total_issues = (len(results['compile_error']) + len(results['runtime_error']) +
                   len(results['error']) + len(results['mismatch']) +
                   len(results['timeout']) + len(results['exception']))

    if total_issues == 0:
        print(f"STATUS: ALL SOLUTIONS COMPILE AND RUN CORRECTLY!")
    elif total_issues < total_tested * 0.01:  # Less than 1%
        print(f"STATUS: EXCELLENT - {total_issues} minor issues ({total_issues/total_tested*100:.2f}%)")
    elif total_issues < total_tested * 0.05:  # Less than 5%
        print(f"STATUS: GOOD - {total_issues} issues need attention ({total_issues/total_tested*100:.1f}%)")
    else:
        print(f"STATUS: NEEDS ATTENTION - {total_issues} issues found ({total_issues/total_tested*100:.1f}%)")

    print(f"{'='*80}\n")

    return results

# Test Python
print("\nStarting solution compilation tests...")
print("This will test ALL 1,400 lessons - may take 5-10 minutes\n")

python_results = test_language('public/lessons-python.json', 'Python', test_python_solution)

# Test Java
java_results = test_language('public/lessons-java.json', 'Java', test_java_solution)

# Overall summary
print(f"\n{'='*80}")
print(f"OVERALL SUMMARY")
print(f"{'='*80}")

py_tested = 700 - len(python_results['skip'])
py_success = len(python_results['success'])
py_issues = py_tested - py_success

java_tested = 700 - len(java_results['skip'])
java_success = len(java_results['success'])
java_issues = java_tested - java_success

print(f"\nPython: {py_success}/{py_tested} passing ({py_success/py_tested*100:.1f}%)")
print(f"Java:   {java_success}/{java_tested} passing ({java_success/java_tested*100:.1f}%)")
print(f"\nTotal:  {py_success + java_success}/{py_tested + java_tested} passing ({(py_success + java_success)/(py_tested + java_tested)*100:.1f}%)")
print(f"Total issues: {py_issues + java_issues}")

if py_issues + java_issues == 0:
    print(f"\n*** ALL LESSONS ARE REAL AND FUNCTIONAL! ***")
else:
    print(f"\n*** {py_issues + java_issues} lessons need fixes ***")

print(f"{'='*80}\n")

# Save detailed results
report = {
    'python': {
        'tested': py_tested,
        'success': py_success,
        'issues': py_issues,
        'details': {k: len(v) for k, v in python_results.items()}
    },
    'java': {
        'tested': java_tested,
        'success': java_success,
        'issues': java_issues,
        'details': {k: len(v) for k, v in java_results.items()}
    }
}

with open('COMPILATION_TEST_REPORT.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2)

print("Detailed report saved to: COMPILATION_TEST_REPORT.json\n")
