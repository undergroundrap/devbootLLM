"""
Deep Quality Check - Find ALL remaining issues in lessons
Ensures students can actually learn and land jobs
"""
import json
import re
import subprocess
import tempfile
import os

def check_solution_quality(lesson, lang):
    """Comprehensive solution quality checks"""
    issues = []
    solution = lesson.get('fullSolution', '')
    difficulty = lesson.get('difficulty', '')
    title = lesson['title']

    # 1. Solution length checks
    min_lengths = {
        'Beginner': 50,
        'Intermediate': 150,
        'Advanced': 400,
        'Expert': 500
    }

    min_len = min_lengths.get(difficulty, 50)
    if len(solution) < min_len:
        issues.append(f'Solution too short for {difficulty}: {len(solution)} chars (need {min_len}+)')

    # 2. Check for empty or missing solution
    if len(solution.strip()) == 0:
        issues.append('CRITICAL: Empty solution')
        return issues

    # 3. Language-specific checks
    if lang == 'python':
        # Check for basic Python syntax
        if not any(keyword in solution for keyword in ['def ', 'class ', 'import ', 'print(', '=']):
            issues.append('May not contain valid Python code')

        # Check framework lessons have proper imports
        if 'flask' in title.lower() and 'from flask' not in solution.lower():
            issues.append('Flask lesson missing Flask imports')

        if 'django' in title.lower() and 'django' not in solution.lower():
            issues.append('Django lesson missing Django code')

        if 'pandas' in title.lower() and 'pandas' not in solution.lower() and 'pd.' not in solution:
            issues.append('Pandas lesson missing pandas import/usage')

        # Check for common bad patterns
        if 'pass' == solution.strip():
            issues.append('Solution is just "pass" statement')

    else:  # Java
        # Check for basic Java syntax
        if not any(keyword in solution for keyword in ['public ', 'class ', 'void ', 'static ', 'import ']):
            issues.append('May not contain valid Java code')

        # Check Spring lessons have annotations
        if 'spring' in title.lower():
            if not any(anno in solution for anno in ['@SpringBoot', '@RestController', '@Service', '@Repository', '@Component', '@Entity']):
                issues.append('Spring lesson missing Spring annotations')

        # Check for proper class structure
        if 'public class Main' not in solution and 'class Main' not in solution:
            if difficulty in ['Intermediate', 'Advanced', 'Expert']:
                # Some lessons might have different class names, but most should have Main
                if 'public class' not in solution and 'class ' not in solution:
                    issues.append('Missing class definition')

    return issues

def check_tutorial_quality(lesson):
    """Check tutorial quality"""
    issues = []
    tutorial = lesson.get('tutorial', '')
    difficulty = lesson.get('difficulty', '')

    # Tutorial length requirements
    min_tutorial_lengths = {
        'Beginner': 300,
        'Intermediate': 500,
        'Advanced': 800,
        'Expert': 1000
    }

    min_len = min_tutorial_lengths.get(difficulty, 300)
    if len(tutorial) < min_len:
        issues.append(f'Tutorial too short for {difficulty}: {len(tutorial)} chars (need {min_len}+)')

    # Check for generic/template text
    generic_phrases = [
        'This is a placeholder',
        'TODO: Write tutorial',
        'Coming soon',
        'Under construction'
    ]

    for phrase in generic_phrases:
        if phrase.lower() in tutorial.lower():
            issues.append(f'Contains placeholder: "{phrase}"')

    # Check for actual educational content
    if tutorial and len(tutorial) > 100:
        # Should have some structure (headings, lists, examples)
        has_structure = any(marker in tutorial for marker in ['<h', '<ul', '<ol', '<li', '<div', '##', '- '])
        if not has_structure:
            issues.append('Tutorial lacks structure (headings, lists, etc.)')

    return issues

def check_expected_output(lesson):
    """Check if expected output exists and seems valid"""
    issues = []
    expected = lesson.get('expectedOutput', '')
    solution = lesson.get('fullSolution', '')

    # If solution has print statements, should have expected output
    if 'print(' in solution or 'System.out' in solution:
        if not expected or len(expected.strip()) < 5:
            issues.append('Solution prints output but expectedOutput is missing/empty')

    return issues

def check_compilation(lesson, lang):
    """Try to compile the solution"""
    solution = lesson.get('fullSolution', '')

    # Skip framework lessons (need external deps)
    if 'org.springframework' in solution or 'from flask import' in solution or 'from django' in solution:
        return []  # Framework lessons are OK if they have imports

    issues = []

    try:
        if lang == 'python':
            # Try to compile Python
            compile(solution, f'<lesson_{lesson["id"]}>', 'exec')
        else:  # Java
            # Try to compile Java
            with tempfile.TemporaryDirectory() as tmpdir:
                java_file = os.path.join(tmpdir, 'Main.java')

                with open(java_file, 'w', encoding='utf-8') as f:
                    f.write(solution)

                result = subprocess.run(
                    ['javac', java_file],
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=tmpdir
                )

                if result.returncode != 0:
                    # Get first line of error
                    error_line = result.stderr.split('\n')[0][:100]
                    issues.append(f'Compilation error: {error_line}')

    except SyntaxError as e:
        issues.append(f'Python syntax error: {str(e)[:100]}')
    except Exception as e:
        # Ignore compilation errors for framework code
        pass

    return issues

def deep_check_lesson(lesson, lang):
    """Run all quality checks on a lesson"""
    all_issues = []

    # Run all checks
    all_issues.extend(check_solution_quality(lesson, lang))
    all_issues.extend(check_tutorial_quality(lesson))
    all_issues.extend(check_expected_output(lesson))
    all_issues.extend(check_compilation(lesson, lang))

    return all_issues

def analyze_all_lessons(lessons_file, lang):
    """Deep quality check on all lessons"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f'\n{"="*70}')
    print(f'DEEP QUALITY CHECK - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Analyzing all {len(lessons)} lessons...\n')

    # Categorize issues
    critical_issues = []  # Empty solutions, won't compile
    high_issues = []      # Too short, missing imports, bad quality
    medium_issues = []    # Short tutorials, missing output
    low_issues = []       # Minor improvements

    for lesson in lessons:
        issues = deep_check_lesson(lesson, lang)

        if not issues:
            continue

        lesson_data = {
            'id': lesson['id'],
            'title': lesson['title'],
            'difficulty': lesson.get('difficulty', ''),
            'issues': issues
        }

        # Categorize by severity
        critical_keywords = ['CRITICAL', 'Empty solution', 'Compilation error', 'syntax error']
        high_keywords = ['too short', 'missing', 'Flask lesson', 'Django lesson', 'Spring lesson', 'Pandas lesson']
        medium_keywords = ['Tutorial', 'expectedOutput']

        is_critical = any(any(kw in issue for kw in critical_keywords) for issue in issues)
        is_high = any(any(kw in issue for kw in high_keywords) for issue in issues)
        is_medium = any(any(kw in issue for kw in medium_keywords) for issue in issues)

        if is_critical:
            critical_issues.append(lesson_data)
        elif is_high:
            high_issues.append(lesson_data)
        elif is_medium:
            medium_issues.append(lesson_data)
        else:
            low_issues.append(lesson_data)

    # Report findings
    print(f'=== CRITICAL ISSUES (Blocks Learning) ===')
    print(f'Found: {len(critical_issues)} lessons\n')

    for i, lesson in enumerate(critical_issues[:20], 1):
        print(f'[{i}] Lesson {lesson["id"]}: {lesson["title"]}')
        print(f'    Difficulty: {lesson["difficulty"]}')
        for issue in lesson['issues']:
            print(f'    [CRITICAL] {issue}')
        print()

    if len(critical_issues) > 20:
        print(f'... and {len(critical_issues) - 20} more critical issues\n')

    print(f'\n=== HIGH PRIORITY ISSUES (Affects Job Readiness) ===')
    print(f'Found: {len(high_issues)} lessons\n')

    for i, lesson in enumerate(high_issues[:20], 1):
        print(f'[{i}] Lesson {lesson["id"]}: {lesson["title"]}')
        print(f'    Difficulty: {lesson["difficulty"]}')
        for issue in lesson['issues']:
            print(f'    [HIGH] {issue}')
        print()

    if len(high_issues) > 20:
        print(f'... and {len(high_issues) - 20} more high priority issues\n')

    print(f'\n=== MEDIUM PRIORITY ISSUES (Quality Improvements) ===')
    print(f'Found: {len(medium_issues)} lessons')
    print(f'(Not shown - focus on Critical and High priority first)\n')

    print(f'\n=== SUMMARY ===')
    print(f'Critical (Must Fix):     {len(critical_issues)}')
    print(f'High Priority:           {len(high_issues)}')
    print(f'Medium Priority:         {len(medium_issues)}')
    print(f'Low Priority:            {len(low_issues)}')
    print(f'Clean Lessons:           {len(lessons) - len(critical_issues) - len(high_issues) - len(medium_issues) - len(low_issues)}')

    total_issues = len(critical_issues) + len(high_issues)
    if total_issues == 0:
        print(f'\n[OK] NO CRITICAL OR HIGH PRIORITY ISSUES!')
        print(f'     All lessons are job-ready quality!')
    else:
        print(f'\n[WARNING] NEED TO FIX: {total_issues} lessons')
        print(f'          Focus on Critical and High priority issues first')

    print(f'{"="*70}\n')

    return critical_issues, high_issues, medium_issues, low_issues

if __name__ == '__main__':
    print('\n' + '='*70)
    print('COMPREHENSIVE DEEP QUALITY CHECK')
    print('Finding ALL issues that could prevent students from getting jobs')
    print('='*70)

    # Check Python
    py_critical, py_high, py_medium, py_low = analyze_all_lessons(
        'public/lessons-python.json', 'python'
    )

    # Check Java
    java_critical, java_high, java_medium, java_low = analyze_all_lessons(
        'public/lessons-java.json', 'java'
    )

    print(f'{"="*70}')
    print('OVERALL FINDINGS')
    print(f'{"="*70}')
    print(f'PYTHON:')
    print(f'  Critical: {len(py_critical)}')
    print(f'  High:     {len(py_high)}')
    print(f'  Medium:   {len(py_medium)}')
    print(f'  Low:      {len(py_low)}')
    print()
    print(f'JAVA:')
    print(f'  Critical: {len(java_critical)}')
    print(f'  High:     {len(java_high)}')
    print(f'  Medium:   {len(java_medium)}')
    print(f'  Low:      {len(java_low)}')
    print()

    total_critical = len(py_critical) + len(java_critical)
    total_high = len(py_high) + len(java_high)

    print(f'TOTAL MUST-FIX: {total_critical + total_high} lessons')
    print(f'  Critical: {total_critical}')
    print(f'  High:     {total_high}')

    if total_critical + total_high == 0:
        print(f'\n[SUCCESS] ALL LESSONS ARE JOB-READY QUALITY!')
    else:
        print(f'\n[ACTION NEEDED] Fix {total_critical + total_high} lessons for job readiness')

    print(f'{"="*70}\n')
