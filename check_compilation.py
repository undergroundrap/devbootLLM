#!/usr/bin/env python3
"""
Check which lessons have external dependencies or likely compilation issues.
"""

import json
import re

def check_java_dependencies(code, lesson_id):
    issues = []

    # Split code into lines and check for actual import statements (not in string literals)
    lines = code.split('\n')
    imports = [l.strip() for l in lines if l.strip().startswith('import')]

    # Check for actual Jackson imports (not in standard library)
    jackson_imports = [imp for imp in imports if 'com.fasterxml.jackson' in imp]
    if jackson_imports:
        issues.append(f"Lesson {lesson_id}: Uses Jackson library (external dependency)")

    # Check for actual Spring imports (not in standard library)
    spring_imports = [imp for imp in imports if 'org.springframework' in imp]
    if spring_imports:
        # Lesson 64 intentionally demonstrates Spring stub - that's OK
        if lesson_id != 64:
            issues.append(f"Lesson {lesson_id}: Uses Spring framework (external dependency)")

    # Check for missing Main class (unless it's a multi-class lesson like 64)
    if 'public class Main' not in code and lesson_id not in [64]:
        if 'public class' in code:  # Has a class but not Main
            issues.append(f"Lesson {lesson_id}: Has public class but not named 'Main'")

    return issues

def check_python_dependencies(code, lesson_id):
    issues = []

    # Check for imports that might not be standard
    # Most stdlib modules should be fine, but flag unusual ones
    if 'import numpy' in code or 'import pandas' in code or 'import requests' in code:
        issues.append(f"Lesson {lesson_id}: Uses non-standard library")

    return issues

def main():
    print("=" * 80)
    print("COMPILATION DEPENDENCY CHECK")
    print("=" * 80)

    # Check Java
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    java_issues = []
    for lesson in java_data['lessons']:
        code = lesson.get('fullSolution', '')
        issues = check_java_dependencies(code, lesson['id'])
        java_issues.extend(issues)

    print("\nJava Lessons with External Dependencies:")
    print("-" * 80)
    if java_issues:
        for issue in java_issues:
            print(f"  {issue}")
    else:
        print("  [OK] No external dependencies found")

    # Check Python
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_data = json.load(f)

    python_issues = []
    for lesson in python_data['lessons']:
        code = lesson.get('fullSolution', '')
        issues = check_python_dependencies(code, lesson['id'])
        python_issues.extend(issues)

    print("\nPython Lessons with External Dependencies:")
    print("-" * 80)
    if python_issues:
        for issue in python_issues:
            print(f"  {issue}")
    else:
        print("  [OK] No external dependencies found")

    print("\n" + "=" * 80)
    print(f"SUMMARY: Found {len(java_issues)} Java issues, {len(python_issues)} Python issues")
    print("=" * 80)

if __name__ == "__main__":
    main()
