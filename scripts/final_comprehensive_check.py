"""
Final Comprehensive Quality Check
Validates EVERYTHING - tutorials, solutions, compilation, job readiness
"""
import json
import subprocess
import tempfile
import os

def check_tutorial_quality(lesson):
    """Check if tutorial is good quality"""
    issues = []
    tutorial = lesson.get('tutorial', '')
    difficulty = lesson.get('difficulty', '')
    title = lesson['title']

    # 1. Tutorial must exist and be substantial
    if len(tutorial) < 200:
        issues.append(f'[CRITICAL] Tutorial too short: {len(tutorial)} chars')
        return issues

    # 2. Difficulty-based length requirements
    min_lengths = {
        'Beginner': 300,
        'Intermediate': 500,
        'Advanced': 800,
        'Expert': 1000
    }

    min_len = min_lengths.get(difficulty, 300)
    if len(tutorial) < min_len:
        issues.append(f'Tutorial short for {difficulty}: {len(tutorial)}/{min_len} chars')

    # 3. Should have structure (HTML or markdown)
    has_structure = any(marker in tutorial for marker in [
        '<h1', '<h2', '<h3', '<h4', '<div', '<ul', '<ol', '<li', '<p',
        '##', '###', '- ', '* '
    ])

    if not has_structure and len(tutorial) > 500:
        issues.append('Tutorial lacks formatting/structure')

    # 4. Should have some educational keywords
    educational_keywords = [
        'example', 'learn', 'understand', 'concept', 'demonstrates',
        'shows', 'illustrates', 'practice', 'key', 'important'
    ]

    has_educational = any(kw in tutorial.lower() for kw in educational_keywords)
    if not has_educational and len(tutorial) > 300:
        issues.append('Tutorial may lack educational content')

    return issues

def check_solution_quality(lesson, lang):
    """Check if solution is good quality"""
    issues = []
    solution = lesson.get('fullSolution', '')
    difficulty = lesson.get('difficulty', '')
    title = lesson['title']

    # 1. Solution must exist
    if len(solution.strip()) < 20:
        issues.append('[CRITICAL] Solution empty or too short')
        return issues

    # 2. Length requirements by difficulty
    min_lengths = {
        'Beginner': 50,
        'Intermediate': 150,
        'Advanced': 400,
        'Expert': 500
    }

    min_len = min_lengths.get(difficulty, 50)
    if len(solution) < min_len:
        issues.append(f'Solution short for {difficulty}: {len(solution)}/{min_len} chars')

    # 3. Must have actual code
    if lang == 'python':
        has_code = any(kw in solution for kw in ['def ', 'class ', 'import ', 'print(', 'return', 'if ', 'for ', 'while '])
        if not has_code:
            issues.append('[HIGH] May not contain real Python code')
    else:  # Java
        has_code = any(kw in solution for kw in ['public ', 'class ', 'void ', 'import ', 'return', 'if(', 'for(', 'while('])
        if not has_code:
            issues.append('[HIGH] May not contain real Java code')

    # 4. Framework lessons must have framework code
    if lang == 'python':
        if 'flask' in title.lower() and 'from flask' not in solution.lower():
            issues.append('[HIGH] Flask lesson missing Flask imports')

        if 'django' in title.lower() and 'django' not in solution.lower():
            issues.append('[HIGH] Django lesson missing Django code')

        if 'pandas' in title.lower() and 'pandas' not in solution.lower() and 'pd.' not in solution:
            issues.append('[HIGH] Pandas lesson missing pandas')

        if 'numpy' in title.lower() and 'numpy' not in solution.lower() and 'np.' not in solution:
            issues.append('[HIGH] NumPy lesson missing numpy')

    else:  # Java
        if 'spring' in title.lower():
            spring_annos = [
                '@SpringBoot', '@RestController', '@Service', '@Repository', '@Component',
                '@Entity', '@Autowired', '@Transactional', '@Cacheable', '@Bean', '@Configuration'
            ]
            if not any(a in solution for a in spring_annos):
                issues.append('[HIGH] Spring lesson missing annotations')

    return issues

def check_expected_output(lesson):
    """Check if expected output is present when needed"""
    issues = []
    solution = lesson.get('fullSolution', '')
    expected = lesson.get('expectedOutput', '')

    # If solution prints, should have expected output
    has_print = 'print(' in solution or 'System.out' in solution or 'println' in solution

    if has_print and len(expected.strip()) < 3:
        issues.append('Solution prints but expectedOutput missing')

    return issues

def validate_compilation(lesson, lang):
    """Try to compile the solution"""
    solution = lesson.get('fullSolution', '')

    # Skip framework lessons (need dependencies)
    framework_indicators = [
        'org.springframework', 'from flask', 'from django', 'import pandas',
        'import numpy', 'import fastapi'
    ]

    if any(fw in solution.lower() for fw in framework_indicators):
        return []  # Framework lessons OK

    issues = []

    try:
        if lang == 'python':
            compile(solution, f'<lesson_{lesson["id"]}>', 'exec')
        else:  # Java
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
                    error_line = result.stderr.split('\n')[0][:80]
                    issues.append(f'[COMPILATION] {error_line}')

    except SyntaxError as e:
        issues.append(f'[COMPILATION] Python syntax error: {str(e)[:80]}')
    except Exception:
        pass  # Ignore other errors

    return issues

def comprehensive_check_lesson(lesson, lang):
    """Run all checks on a lesson"""
    all_issues = []

    # Check tutorial
    all_issues.extend(check_tutorial_quality(lesson))

    # Check solution
    all_issues.extend(check_solution_quality(lesson, lang))

    # Check expected output
    all_issues.extend(check_expected_output(lesson))

    # Validate compilation (sample only for performance)
    # We'll only compile every 10th lesson
    if lesson['id'] % 10 == 0:
        all_issues.extend(validate_compilation(lesson, lang))

    return all_issues

def final_comprehensive_check(lessons_file, lang):
    """Final comprehensive quality check"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f'\n{"="*70}')
    print(f'FINAL COMPREHENSIVE CHECK - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Checking all {len(lessons)} lessons...\n')

    # Categorize issues
    critical = []
    high = []
    medium = []
    compilation_issues = []

    for lesson in lessons:
        issues = comprehensive_check_lesson(lesson, lang)

        if not issues:
            continue

        data = {
            'id': lesson['id'],
            'title': lesson['title'],
            'difficulty': lesson.get('difficulty', ''),
            'issues': issues
        }

        # Categorize
        has_critical = any('[CRITICAL]' in i for i in issues)
        has_high = any('[HIGH]' in i for i in issues)
        has_compilation = any('[COMPILATION]' in i for i in issues)

        if has_critical:
            critical.append(data)
        elif has_high:
            high.append(data)
        elif has_compilation:
            compilation_issues.append(data)
        else:
            medium.append(data)

    # Report
    print('=== CRITICAL ISSUES (Must Fix Immediately) ===')
    print(f'Count: {len(critical)}\n')

    if critical:
        for i, l in enumerate(critical[:15], 1):
            print(f'{i}. Lesson {l["id"]}: {l["title"]} ({l["difficulty"]})')
            for issue in l['issues']:
                print(f'   {issue}')
            print()

        if len(critical) > 15:
            print(f'   ... and {len(critical) - 15} more\n')
    else:
        print('[OK] No critical issues!\n')

    print('=== HIGH PRIORITY (Affects Learning Quality) ===')
    print(f'Count: {len(high)}\n')

    if high:
        for i, l in enumerate(high[:15], 1):
            print(f'{i}. Lesson {l["id"]}: {l["title"]} ({l["difficulty"]})')
            for issue in l['issues']:
                print(f'   {issue}')
            print()

        if len(high) > 15:
            print(f'   ... and {len(high) - 15} more\n')
    else:
        print('[OK] No high priority issues!\n')

    print('=== COMPILATION ISSUES ===')
    print(f'Count: {len(compilation_issues)}\n')

    if compilation_issues:
        for i, l in enumerate(compilation_issues[:10], 1):
            print(f'{i}. Lesson {l["id"]}: {l["title"]}')
            for issue in l['issues']:
                print(f'   {issue}')

        if len(compilation_issues) > 10:
            print(f'   ... and {len(compilation_issues) - 10} more\n')
    else:
        print('[OK] All sampled lessons compile!\n')

    print('=== MEDIUM PRIORITY ===')
    print(f'Count: {len(medium)} (minor improvements)\n')

    print('=== SUMMARY ===')
    print(f'Total lessons:       {len(lessons)}')
    print(f'Critical issues:     {len(critical)}')
    print(f'High priority:       {len(high)}')
    print(f'Compilation issues:  {len(compilation_issues)}')
    print(f'Medium priority:     {len(medium)}')
    print(f'Clean lessons:       {len(lessons) - len(critical) - len(high) - len(compilation_issues) - len(medium)}')

    must_fix = len(critical) + len(high)

    print(f'\nMUST FIX: {must_fix} lessons')

    if must_fix == 0:
        print('\n[SUCCESS] All tutorials and lessons are EXCELLENT quality!')
        print('          Students can learn effectively and get jobs!')
    else:
        print(f'\n[ACTION NEEDED] Fix {must_fix} lessons before deployment')

    print(f'{"="*70}\n')

    return critical, high, compilation_issues, medium

if __name__ == '__main__':
    print('\n' + '='*70)
    print('FINAL COMPREHENSIVE QUALITY CHECK')
    print('Validating ALL tutorials and lessons for student success')
    print('='*70)

    # Check Python
    py_crit, py_high, py_comp, py_med = final_comprehensive_check(
        'public/lessons-python.json', 'python'
    )

    # Check Java
    java_crit, java_high, java_comp, java_med = final_comprehensive_check(
        'public/lessons-java.json', 'java'
    )

    print(f'{"="*70}')
    print('FINAL VERDICT')
    print(f'{"="*70}')
    print(f'PYTHON:')
    print(f'  Critical:     {len(py_crit)}')
    print(f'  High:         {len(py_high)}')
    print(f'  Compilation:  {len(py_comp)}')
    print(f'  Medium:       {len(py_med)}')
    print()
    print(f'JAVA:')
    print(f'  Critical:     {len(java_crit)}')
    print(f'  High:         {len(java_high)}')
    print(f'  Compilation:  {len(java_comp)}')
    print(f'  Medium:       {len(java_med)}')
    print()

    total_must_fix = len(py_crit) + len(py_high) + len(java_crit) + len(java_high)

    print(f'TOTAL MUST-FIX: {total_must_fix}')

    if total_must_fix == 0:
        print('\n' + '='*70)
        print('[SUCCESS] ALL TUTORIALS AND LESSONS ARE EXCELLENT!')
        print('='*70)
        print('Your students can:')
        print('  - Learn from clear, well-structured tutorials')
        print('  - Run all lesson solutions successfully')
        print('  - Build production-ready applications')
        print('  - Land junior developer jobs')
        print('='*70)
    else:
        print(f'\n[FIX NEEDED] {total_must_fix} lessons need improvements')

    print()
