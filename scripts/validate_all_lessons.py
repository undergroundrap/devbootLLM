#!/usr/bin/env python3
"""
Comprehensive lesson validation script.
Executes the fullSolution of every lesson and checks if output matches expectedOutput.
"""
import json
import subprocess
import sys
import tempfile
import os
from pathlib import Path

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def normalize_output(text):
    """Normalize output for comparison (same logic as frontend)"""
    if text is None:
        return ''
    return text.strip().replace('\r\n', '\n')

def run_python_code(code, timeout=10):
    """Execute Python code and return output, error status, and error message"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        try:
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            if result.returncode != 0:
                return result.stderr, True, 'runtime'
            return result.stdout, False, None
        finally:
            try:
                os.unlink(temp_file)
            except:
                pass
    except subprocess.TimeoutExpired:
        return '', True, 'timeout'
    except Exception as e:
        return str(e), True, 'execution'

def run_java_code(code, timeout=10):
    """Execute Java code and return output, error status, and error message"""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Write Java file
            java_file = Path(temp_dir) / 'Main.java'
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            # Compile
            compile_result = subprocess.run(
                ['javac', str(java_file)],
                capture_output=True,
                text=True,
                cwd=temp_dir,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            if compile_result.returncode != 0:
                return compile_result.stderr, True, 'compilation'

            # Run
            try:
                run_result = subprocess.run(
                    ['java', '-Xmx64m', '-cp', temp_dir, 'Main'],
                    capture_output=True,
                    text=True,
                    cwd=temp_dir,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='replace'
                )

                if run_result.returncode != 0:
                    return run_result.stderr, True, 'runtime'
                return run_result.stdout, False, None
            except subprocess.TimeoutExpired:
                return '', True, 'timeout'
    except Exception as e:
        return str(e), True, 'execution'

def validate_lesson(lesson, language):
    """Validate a single lesson by running its fullSolution"""
    lesson_id = lesson.get('id')
    title = lesson.get('title', 'Unknown')
    full_solution = lesson.get('fullSolution', '')
    expected_output = lesson.get('expectedOutput', '')

    if not full_solution:
        return {
            'id': lesson_id,
            'title': title,
            'status': 'missing_solution',
            'message': 'No fullSolution provided'
        }

    # Run the code
    if language == 'python':
        actual_output, has_error, error_type = run_python_code(full_solution)
    elif language == 'java':
        actual_output, has_error, error_type = run_java_code(full_solution)
    else:
        return {
            'id': lesson_id,
            'title': title,
            'status': 'invalid_language',
            'message': f'Unknown language: {language}'
        }

    # Check for execution errors
    if has_error:
        return {
            'id': lesson_id,
            'title': title,
            'status': 'execution_error',
            'error_type': error_type,
            'message': actual_output[:500]  # Limit error message length
        }

    # Special check for Lesson 134 (Creating Methods - dynamic output)
    if lesson_id == 134 and language == 'java':
        # For lesson 134, we need to check if the code has a greetUser method call
        # The output format should be "Hello, {name}!" where name is extracted from the code
        import re
        method_call_match = re.search(r'greetUser\s*\(\s*"([^"]+)"\s*\)', full_solution)
        if method_call_match:
            name = method_call_match.group(1)
            expected_output = f"Hello, {name}!"

    # Compare outputs
    if normalize_output(actual_output) == normalize_output(expected_output):
        return {
            'id': lesson_id,
            'title': title,
            'status': 'pass'
        }
    else:
        return {
            'id': lesson_id,
            'title': title,
            'status': 'output_mismatch',
            'expected': expected_output,
            'actual': actual_output
        }

def validate_lessons_file(file_path, language):
    """Validate all lessons in a file"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}Validating {language.upper()} lessons from: {file_path}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lessons = json.load(f)
    except Exception as e:
        print(f"{Colors.RED}Error loading file: {e}{Colors.RESET}")
        return []

    # Handle both array and object with lessons array
    if isinstance(lessons, dict) and 'lessons' in lessons:
        lessons = lessons['lessons']

    if not isinstance(lessons, list):
        print(f"{Colors.RED}Invalid file format: expected array of lessons{Colors.RESET}")
        return []

    print(f"Found {Colors.BOLD}{len(lessons)}{Colors.RESET} lessons to validate\n")

    results = []
    pass_count = 0
    fail_count = 0
    error_count = 0

    for i, lesson in enumerate(lessons, 1):
        lesson_id = lesson.get('id', i)
        title = lesson.get('title', f'Lesson {lesson_id}')

        # Progress indicator
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(lessons)} lessons validated...")

        result = validate_lesson(lesson, language)
        results.append(result)

        if result['status'] == 'pass':
            pass_count += 1
            try:
                print(f"{Colors.GREEN}✓{Colors.RESET} {lesson_id:3d}. {title[:60]}")
            except UnicodeEncodeError:
                print(f"{Colors.GREEN}[PASS]{Colors.RESET} {lesson_id:3d}. {title[:60]}")
        elif result['status'] == 'output_mismatch':
            fail_count += 1
            try:
                print(f"{Colors.RED}✗{Colors.RESET} {lesson_id:3d}. {title[:60]}")
            except UnicodeEncodeError:
                print(f"{Colors.RED}[FAIL]{Colors.RESET} {lesson_id:3d}. {title[:60]}")
            try:
                print(f"  {Colors.YELLOW}Expected:{Colors.RESET} {repr(result['expected'][:100])}")
                print(f"  {Colors.YELLOW}Actual:{Colors.RESET}   {repr(result['actual'][:100])}")
            except UnicodeEncodeError:
                print(f"  {Colors.YELLOW}Expected:{Colors.RESET} <output contains special characters>")
                print(f"  {Colors.YELLOW}Actual:{Colors.RESET}   <output contains special characters>")
        else:
            error_count += 1
            print(f"{Colors.MAGENTA}!{Colors.RESET} {lesson_id:3d}. {title[:60]}")
            print(f"  {Colors.YELLOW}Status:{Colors.RESET} {result['status']}")
            if 'message' in result:
                try:
                    print(f"  {Colors.YELLOW}Error:{Colors.RESET} {result['message'][:200]}")
                except UnicodeEncodeError:
                    print(f"  {Colors.YELLOW}Error:{Colors.RESET} <error message contains special characters>")

    # Summary
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}Summary for {language.upper()}:{Colors.RESET}")
    print(f"  {Colors.GREEN}Passed:{Colors.RESET}  {pass_count:4d} / {len(lessons)}")
    print(f"  {Colors.RED}Failed:{Colors.RESET}  {fail_count:4d} / {len(lessons)}")
    print(f"  {Colors.MAGENTA}Errors:{Colors.RESET}  {error_count:4d} / {len(lessons)}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    return results

def main():
    script_dir = Path(__file__).parent
    public_dir = script_dir.parent / 'public'

    python_file = public_dir / 'lessons-python.json'
    java_file = public_dir / 'lessons-java.json'

    all_results = {}

    # Validate Python lessons
    if python_file.exists():
        python_results = validate_lessons_file(python_file, 'python')
        all_results['python'] = python_results
    else:
        print(f"{Colors.YELLOW}Warning: {python_file} not found{Colors.RESET}")

    # Validate Java lessons
    if java_file.exists():
        java_results = validate_lessons_file(java_file, 'java')
        all_results['java'] = java_results
    else:
        print(f"{Colors.YELLOW}Warning: {java_file} not found{Colors.RESET}")

    # Overall summary
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}OVERALL SUMMARY{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    total_lessons = 0
    total_pass = 0
    total_fail = 0
    total_error = 0

    for lang, results in all_results.items():
        total_lessons += len(results)
        total_pass += sum(1 for r in results if r['status'] == 'pass')
        total_fail += sum(1 for r in results if r['status'] == 'output_mismatch')
        total_error += sum(1 for r in results if r['status'] not in ['pass', 'output_mismatch'])

    print(f"  {Colors.BOLD}Total Lessons:{Colors.RESET} {total_lessons}")
    print(f"  {Colors.GREEN}Total Passed:{Colors.RESET}  {total_pass} ({100*total_pass//total_lessons if total_lessons else 0}%)")
    print(f"  {Colors.RED}Total Failed:{Colors.RESET}  {total_fail} ({100*total_fail//total_lessons if total_lessons else 0}%)")
    print(f"  {Colors.MAGENTA}Total Errors:{Colors.RESET}  {total_error} ({100*total_error//total_lessons if total_lessons else 0}%)")

    # Save detailed report
    report_file = script_dir.parent / 'validation_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"\n{Colors.CYAN}Detailed report saved to: {report_file}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")

    # Exit with error if any failures
    if total_fail > 0 or total_error > 0:
        sys.exit(1)
    else:
        try:
            print(f"{Colors.GREEN}{Colors.BOLD}🎉 All lessons passed validation!{Colors.RESET}")
        except UnicodeEncodeError:
            print(f"{Colors.GREEN}{Colors.BOLD}All lessons passed validation!{Colors.RESET}")
        sys.exit(0)

if __name__ == '__main__':
    main()
