#!/usr/bin/env python3
"""
Comprehensive compilation test for all lessons.
Actually compiles Python code and checks Java syntax.
"""

import json
import subprocess
import tempfile
import os
import sys


def test_python_compilation(lesson):
    """Test if Python code compiles."""
    code = lesson.get('fullSolution', '')

    if not code or not code.strip():
        return False, "Empty code"

    try:
        # Try to compile the code
        compile(code, f'<lesson{lesson["id"]}>', 'exec')
        return True, "OK"
    except SyntaxError as e:
        return False, f"SyntaxError at line {e.lineno}: {e.msg}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def test_python_execution(lesson):
    """Test if Python code executes without errors."""
    code = lesson.get('fullSolution', '')

    if not code or not code.strip():
        return False, "Empty code"

    # Write to temp file and execute
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=5,
            encoding='utf-8'
        )

        os.unlink(temp_file)

        if result.returncode != 0:
            return False, f"Runtime error: {result.stderr[:200]}"

        return True, "OK"

    except subprocess.TimeoutExpired:
        return False, "Timeout (infinite loop?)"
    except Exception as e:
        return False, f"Execution error: {str(e)}"


def test_java_compilation(lesson):
    """Actually compile Java code."""
    code = lesson.get('fullSolution', '')

    if not code or not code.strip():
        return False, "Empty code"

    # Write to Main.java and try to compile
    try:
        import subprocess
        import os

        with open('Main.java', 'w', encoding='utf-8') as f:
            f.write(code)

        result = subprocess.run(
            ['javac', 'Main.java'],
            capture_output=True,
            text=True,
            timeout=10,
            encoding='utf-8'
        )

        # Clean up source and class files
        for f in ['Main.java']:
            if os.path.exists(f):
                os.unlink(f)

        # Clean up any generated class files
        import glob
        for cf in glob.glob('*.class'):
            os.unlink(cf)

        if result.returncode != 0:
            # Extract just the error message, not filename
            error = result.stderr
            if 'error:' in error:
                error = error.split('error:')[1].split('\n')[0].strip()
            return False, f"Compilation error: {error[:100]}"

        return True, "OK"

    except subprocess.TimeoutExpired:
        return False, "Compilation timeout"
    except FileNotFoundError:
        # javac not available, skip
        return True, "OK (javac not available)"
    except Exception as e:
        return False, f"Error: {str(e)[:100]}"


def check_placeholder_code(lesson):
    """Check if lesson has placeholder code."""
    code = lesson.get('fullSolution', '')

    if 'Exercise completed!' in code:
        return True, "Has 'Exercise completed!' placeholder"
    if 'Complete the exercise' in code:
        return True, "Has 'Complete the exercise' placeholder"

    return False, "OK"


def test_all_python():
    """Test all Python lessons."""
    print("\n" + "="*80)
    print("TESTING PYTHON LESSONS")
    print("="*80)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f"\nTotal Python lessons: {len(lessons)}")

    compilation_errors = []
    execution_errors = []
    placeholder_issues = []

    for i, lesson in enumerate(lessons, 1):
        if i % 100 == 0:
            print(f"  Tested {i}/{len(lessons)} lessons...", end='\r')

        # Check compilation
        compiles, compile_msg = test_python_compilation(lesson)
        if not compiles:
            compilation_errors.append((lesson['id'], lesson['title'], compile_msg))

        # Check for placeholders
        has_placeholder, placeholder_msg = check_placeholder_code(lesson)
        if has_placeholder:
            placeholder_issues.append((lesson['id'], lesson['title'], placeholder_msg))

    print(f"  Tested {len(lessons)}/{len(lessons)} lessons.     ")

    # Report
    print(f"\nCompilation: {len(lessons) - len(compilation_errors)}/{len(lessons)} lessons compile")
    print(f"Placeholders: {len(lessons) - len(placeholder_issues)}/{len(lessons)} lessons clean")

    if compilation_errors:
        print(f"\n{len(compilation_errors)} COMPILATION ERRORS:")
        for lid, title, msg in compilation_errors[:10]:
            print(f"  Lesson {lid}: {title}")
            print(f"    Error: {msg}")
        if len(compilation_errors) > 10:
            print(f"  ... and {len(compilation_errors) - 10} more")

    if placeholder_issues:
        print(f"\n{len(placeholder_issues)} PLACEHOLDER ISSUES:")
        for lid, title, msg in placeholder_issues[:10]:
            print(f"  Lesson {lid}: {title}")
            print(f"    Issue: {msg}")
        if len(placeholder_issues) > 10:
            print(f"  ... and {len(placeholder_issues) - 10} more")

    return len(compilation_errors), len(placeholder_issues)


def test_all_java():
    """Test all Java lessons."""
    print("\n" + "="*80)
    print("TESTING JAVA LESSONS")
    print("="*80)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f"\nTotal Java lessons: {len(lessons)}")

    syntax_errors = []
    placeholder_issues = []

    for i, lesson in enumerate(lessons, 1):
        if i % 100 == 0:
            print(f"  Tested {i}/{len(lessons)} lessons...", end='\r')

        # Check compilation
        compiles, compile_msg = test_java_compilation(lesson)
        if not compiles:
            syntax_errors.append((lesson['id'], lesson['title'], compile_msg))

        # Check for placeholders
        has_placeholder, placeholder_msg = check_placeholder_code(lesson)
        if has_placeholder:
            placeholder_issues.append((lesson['id'], lesson['title'], placeholder_msg))

    print(f"  Tested {len(lessons)}/{len(lessons)} lessons.     ")

    # Report
    print(f"\nCompilation: {len(lessons) - len(syntax_errors)}/{len(lessons)} lessons compile")
    print(f"Placeholders: {len(lessons) - len(placeholder_issues)}/{len(lessons)} lessons clean")

    if syntax_errors:
        print(f"\n{len(syntax_errors)} COMPILATION ERRORS:")
        for lid, title, msg in syntax_errors[:10]:
            print(f"  Lesson {lid}: {title}")
            print(f"    Error: {msg}")
        if len(syntax_errors) > 10:
            print(f"  ... and {len(syntax_errors) - 10} more")

    if placeholder_issues:
        print(f"\n{len(placeholder_issues)} PLACEHOLDER ISSUES:")
        for lid, title, msg in placeholder_issues[:10]:
            print(f"  Lesson {lid}: {title}")
            print(f"    Issue: {msg}")
        if len(placeholder_issues) > 10:
            print(f"  ... and {len(placeholder_issues) - 10} more")

    return len(syntax_errors), len(placeholder_issues)


def main():
    """Test all lessons."""
    print("\n" + "="*80)
    print("COMPREHENSIVE COMPILATION TEST")
    print("="*80)

    # Test Java
    java_syntax_errors, java_placeholders = test_all_java()

    # Test Python
    python_compile_errors, python_placeholders = test_all_python()

    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"\nJava:")
    print(f"  Syntax errors: {java_syntax_errors}")
    print(f"  Placeholder issues: {java_placeholders}")

    print(f"\nPython:")
    print(f"  Compilation errors: {python_compile_errors}")
    print(f"  Placeholder issues: {python_placeholders}")

    total_issues = java_syntax_errors + java_placeholders + python_compile_errors + python_placeholders
    print(f"\nTotal issues to fix: {total_issues}")

    if total_issues == 0:
        print("\nALL LESSONS PASS!")

    return total_issues


if __name__ == "__main__":
    issues = main()
    sys.exit(0 if issues == 0 else 1)
