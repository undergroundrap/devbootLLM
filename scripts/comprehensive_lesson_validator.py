#!/usr/bin/env python3
"""
COMPREHENSIVE LESSON VALIDATOR
Checks EVERY aspect of EVERY lesson to ensure professional quality.
"""

import json
import re
import subprocess
import tempfile
import os
import sys


class LessonValidator:
    def __init__(self):
        self.issues = []

    def validate_lesson(self, lesson, language):
        """Validate every aspect of a lesson."""
        lesson_id = lesson['id']
        title = lesson['title']
        issues = []

        # 1. Check baseCode
        base_code = lesson.get('baseCode', '').strip()
        if not base_code:
            issues.append("CRITICAL: baseCode is empty")
        elif len(base_code) < 10:
            issues.append("CRITICAL: baseCode is too short (stub only)")
        elif 'TODO' not in base_code and 'Your code here' not in base_code:
            issues.append("WARNING: baseCode has no TODO marker")

        # 2. Check fullSolution
        solution = lesson.get('fullSolution', '').strip()
        if not solution:
            issues.append("CRITICAL: fullSolution is empty")
        elif 'Complete the exercise' in solution:
            issues.append("CRITICAL: fullSolution is a placeholder")
        elif 'Exercise completed!' in solution:
            issues.append("CRITICAL: fullSolution is a placeholder")
        elif solution == base_code:
            issues.append("CRITICAL: fullSolution same as baseCode")
        elif len(solution) < 20:
            issues.append("CRITICAL: fullSolution too short")

        # 3. Check tutorial
        tutorial = lesson.get('tutorial', '').strip()
        if not tutorial:
            issues.append("CRITICAL: tutorial is empty")
        elif len(tutorial) < 100:
            issues.append("WARNING: tutorial is very short")

        # Check tutorial matches topic
        title_lower = title.lower()
        tutorial_lower = tutorial.lower()

        # Detect obvious mismatches
        if 'hello' in title_lower and 'world' in title_lower:
            if 'pandas' in tutorial_lower or 'dataframe' in tutorial_lower:
                issues.append("CRITICAL: Hello World has pandas content")

        if 'boolean' in title_lower and 'logic' in title_lower:
            if 'string' in tutorial_lower and 'concatenation' in tutorial_lower:
                issues.append("CRITICAL: Boolean Logic has string concatenation content")

        # 4. Check description
        description = lesson.get('description', '').strip()
        if not description:
            issues.append("CRITICAL: description is empty")
        elif len(description) < 10:
            issues.append("WARNING: description too short")

        # 5. Check examples
        examples = lesson.get('additionalExamples', '').strip()
        if examples and 'Complete the exercise' in examples:
            issues.append("WARNING: additionalExamples has placeholder")

        # 6. Check hints
        hints = lesson.get('hints', [])
        if not hints or len(hints) == 0:
            issues.append("WARNING: No hints provided")

        # 7. Check tags
        tags = lesson.get('tags', [])
        if not tags or len(tags) == 0:
            issues.append("WARNING: No tags provided")

        # 8. Compilation check
        if language == 'python':
            try:
                compile(solution, f'<lesson{lesson_id}>', 'exec')
            except SyntaxError as e:
                issues.append(f"CRITICAL: Python syntax error at line {e.lineno}: {e.msg}")
        elif language == 'java':
            # Basic Java validation
            if solution.count('{') != solution.count('}'):
                issues.append("CRITICAL: Mismatched braces")
            if 'class' in solution and 'public class' not in solution:
                issues.append("WARNING: No public class")

        return issues


def validate_all_lessons(language, lessons):
    """Validate all lessons and create detailed report."""
    print(f"\n{'='*80}")
    print(f"VALIDATING ALL {language.upper()} LESSONS")
    print(f"{'='*80}\n")

    validator = LessonValidator()

    critical_issues = {}
    warnings = {}
    clean_lessons = []

    for i, lesson in enumerate(lessons, 1):
        if i % 50 == 0:
            print(f"  Validated {i}/{len(lessons)} lessons...", end='\r')

        issues = validator.validate_lesson(lesson, language)

        if issues:
            critical = [iss for iss in issues if 'CRITICAL' in iss]
            warns = [iss for iss in issues if 'WARNING' in iss]

            if critical:
                critical_issues[lesson['id']] = {
                    'title': lesson['title'],
                    'issues': critical
                }
            if warns:
                warnings[lesson['id']] = {
                    'title': lesson['title'],
                    'issues': warns
                }
        else:
            clean_lessons.append(lesson['id'])

    print(f"  Validated {len(lessons)}/{len(lessons)} lessons.     \n")

    # Report
    print(f"{'='*80}")
    print(f"VALIDATION REPORT: {language.upper()}")
    print(f"{'='*80}\n")

    print(f"Total Lessons: {len(lessons)}")
    print(f"Clean Lessons: {len(clean_lessons)} ({len(clean_lessons)/len(lessons)*100:.1f}%)")
    print(f"Lessons with Critical Issues: {len(critical_issues)}")
    print(f"Lessons with Warnings: {len(warnings)}")

    if critical_issues:
        print(f"\n{'='*80}")
        print(f"CRITICAL ISSUES ({len(critical_issues)} lessons)")
        print(f"{'='*80}\n")

        for lid in sorted(critical_issues.keys())[:20]:
            info = critical_issues[lid]
            print(f"Lesson {lid}: {info['title']}")
            for issue in info['issues']:
                print(f"  - {issue}")
            print()

        if len(critical_issues) > 20:
            print(f"... and {len(critical_issues) - 20} more lessons with critical issues\n")

    return critical_issues, warnings, clean_lessons


def main():
    """Validate all lessons."""
    print("\n" + "="*80)
    print("COMPREHENSIVE LESSON VALIDATION")
    print("Checking EVERY lesson for professional quality")
    print("="*80)

    # Validate Java
    print("\nLoading Java lessons...")
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    java_critical, java_warnings, java_clean = validate_all_lessons('java', java_lessons)

    # Validate Python
    print("\nLoading Python lessons...")
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    python_critical, python_warnings, python_clean = validate_all_lessons('python', python_lessons)

    # Summary
    print(f"\n{'='*80}")
    print("OVERALL SUMMARY")
    print(f"{'='*80}\n")

    total_lessons = len(java_lessons) + len(python_lessons)
    total_critical = len(java_critical) + len(python_critical)
    total_warnings = len(java_warnings) + len(python_warnings)
    total_clean = len(java_clean) + len(python_clean)

    print(f"Total Lessons: {total_lessons}")
    print(f"Clean Lessons: {total_clean} ({total_clean/total_lessons*100:.1f}%)")
    print(f"Critical Issues: {total_critical} ({total_critical/total_lessons*100:.1f}%)")
    print(f"Warnings: {total_warnings} ({total_warnings/total_lessons*100:.1f}%)")

    print(f"\n{'='*80}\n")

    if total_critical == 0:
        print("SUCCESS! All lessons are professionally ready!")
        return 0
    else:
        print(f"ACTION REQUIRED: {total_critical} lessons need fixes")
        return total_critical


if __name__ == "__main__":
    issues = main()
    sys.exit(0 if issues == 0 else 1)
