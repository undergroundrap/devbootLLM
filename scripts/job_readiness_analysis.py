"""
Job Readiness Analysis
Checks if lessons cover all skills needed for junior developer positions
"""
import json
import re

# Skills required for junior positions
JUNIOR_DEV_SKILLS = {
    'python': {
        'core': ['variables', 'loops', 'functions', 'classes', 'exceptions', 'file handling'],
        'web': ['flask', 'django', 'fastapi', 'rest api', 'http'],
        'database': ['sql', 'orm', 'sqlalchemy', 'migrations'],
        'testing': ['pytest', 'unittest', 'mocking', 'tdd'],
        'tools': ['git', 'docker', 'ci/cd'],
        'data': ['pandas', 'numpy', 'json', 'csv'],
        'async': ['asyncio', 'concurrent', 'threading'],
        'interview': ['algorithms', 'data structures', 'system design'],
    },
    'java': {
        'core': ['variables', 'loops', 'methods', 'classes', 'exceptions', 'collections'],
        'spring': ['spring boot', 'spring data', 'spring security', 'rest'],
        'database': ['jpa', 'hibernate', 'jdbc', 'sql'],
        'testing': ['junit', 'mockito', 'integration test'],
        'tools': ['maven', 'git', 'docker'],
        'advanced': ['streams', 'lambda', 'optional', 'generics'],
        'microservices': ['kafka', 'rest client', 'service'],
        'interview': ['algorithms', 'data structures', 'design patterns'],
    }
}

def analyze_skill_coverage(lessons, lang):
    """Check which job skills are covered"""

    skills = JUNIOR_DEV_SKILLS[lang]
    coverage = {}

    for category, keywords in skills.items():
        coverage[category] = {
            'keywords': keywords,
            'lessons': [],
            'count': 0
        }

        for lesson in lessons:
            title_lower = lesson['title'].lower()
            tutorial_lower = lesson.get('tutorial', '').lower()

            # Check if lesson covers this skill
            for keyword in keywords:
                if keyword in title_lower or keyword in tutorial_lower:
                    coverage[category]['lessons'].append({
                        'id': lesson['id'],
                        'title': lesson['title'],
                        'difficulty': lesson.get('difficulty', '')
                    })
                    coverage[category]['count'] += 1
                    break

    return coverage

def check_lesson_quality(lesson):
    """Check if lesson meets job-ready standards"""
    issues = []

    title = lesson['title']
    tutorial = lesson.get('tutorial', '')
    solution = lesson.get('fullSolution', '')
    difficulty = lesson.get('difficulty', '')

    # Check tutorial length (should explain concepts well)
    if len(tutorial) < 500 and difficulty in ['Intermediate', 'Advanced', 'Expert']:
        issues.append(f'Short tutorial ({len(tutorial)} chars) for {difficulty}')

    # Check solution length
    if len(solution) < 100:
        issues.append(f'Very short solution ({len(solution)} chars)')

    # Check for generic placeholders
    generic_patterns = [
        'TODO', 'FIXME', 'placeholder', 'example here',
        'your code here', 'implement this'
    ]

    for pattern in generic_patterns:
        if pattern.lower() in solution.lower():
            issues.append(f'Contains placeholder: {pattern}')
            break

    # Check for real code patterns
    has_real_code = (
        'def ' in solution or 'class ' in solution or  # Python
        'public ' in solution or 'private ' in solution  # Java
    )

    if not has_real_code and len(solution) > 50:
        issues.append('May not contain real code')

    return issues

def find_weak_lessons(lessons, lang):
    """Find lessons that need improvement for job readiness"""

    weak_lessons = []

    for lesson in lessons:
        issues = check_lesson_quality(lesson)

        if issues:
            weak_lessons.append({
                'id': lesson['id'],
                'title': lesson['title'],
                'difficulty': lesson.get('difficulty', ''),
                'tutorial_len': len(lesson.get('tutorial', '')),
                'solution_len': len(lesson.get('fullSolution', '')),
                'issues': issues
            })

    return weak_lessons

def analyze_job_readiness(lessons_file, lang):
    """Comprehensive job readiness analysis"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f'\n{"="*70}')
    print(f'JOB READINESS ANALYSIS - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Total lessons: {len(lessons)}\n')

    # 1. Skill coverage
    print('=== SKILL COVERAGE (Junior Dev Requirements) ===\n')
    coverage = analyze_skill_coverage(lessons, lang)

    for category, data in coverage.items():
        count = data['count']
        keywords = ', '.join(data['keywords'])
        status = '[OK]' if count > 0 else '[!!]'

        print(f'{status} {category.upper()}: {count} lessons')
        if count == 0:
            print(f'  [WARNING] MISSING: {keywords}')
        elif count < 5:
            print(f'  [WARNING] LOW COVERAGE: Only {count} lessons')
        print()

    # 2. Difficulty distribution
    print('=== DIFFICULTY DISTRIBUTION ===\n')
    difficulty_counts = {}
    for lesson in lessons:
        diff = lesson.get('difficulty', 'Unknown')
        difficulty_counts[diff] = difficulty_counts.get(diff, 0) + 1

    for diff, count in sorted(difficulty_counts.items()):
        pct = 100 * count / len(lessons)
        print(f'{diff:15} {count:4} lessons ({pct:5.1f}%)')

    # 3. Quality issues
    print('\n=== QUALITY ISSUES ===\n')
    weak = find_weak_lessons(lessons, lang)

    if weak:
        print(f'Found {len(weak)} lessons with quality issues:\n')

        # Group by issue type
        issue_types = {}
        for lesson in weak:
            for issue in lesson['issues']:
                issue_type = issue.split('(')[0].strip()
                if issue_type not in issue_types:
                    issue_types[issue_type] = []
                issue_types[issue_type].append(lesson)

        for issue_type, affected_lessons in sorted(issue_types.items()):
            print(f'  {issue_type}: {len(affected_lessons)} lessons')

        print(f'\nShowing first 20 lessons with issues:')
        for i, lesson in enumerate(weak[:20], 1):
            print(f'\n  [{i}] Lesson {lesson["id"]}: {lesson["title"]}')
            print(f'      Difficulty: {lesson["difficulty"]}')
            print(f'      Tutorial: {lesson["tutorial_len"]} chars, Solution: {lesson["solution_len"]} chars')
            for issue in lesson['issues']:
                print(f'      [!] {issue}')
    else:
        print('[OK] No quality issues found!')

    # 4. Summary
    print(f'\n{"="*70}')
    print('SUMMARY')
    print(f'{"="*70}')

    total_skills = sum(len(data['keywords']) for data in coverage.values())
    covered_categories = sum(1 for data in coverage.values() if data['count'] > 0)
    total_categories = len(coverage)

    print(f'Skill Coverage: {covered_categories}/{total_categories} categories covered')
    print(f'Quality Issues: {len(weak)} lessons need improvement')

    job_ready_score = 100 * (covered_categories / total_categories) * (1 - min(len(weak) / len(lessons), 0.5))
    print(f'\nJob Readiness Score: {job_ready_score:.1f}/100')

    if job_ready_score >= 90:
        print('[EXCELLENT] Students ready for junior positions!')
    elif job_ready_score >= 75:
        print('[GOOD] Students well-prepared with minor gaps')
    elif job_ready_score >= 60:
        print('[FAIR] Need more coverage in key areas')
    else:
        print('[NEEDS WORK] Significant improvements needed')

    return coverage, weak

if __name__ == '__main__':
    print('\n' + '='*70)
    print('JUNIOR DEVELOPER JOB READINESS ANALYSIS')
    print('Evaluating if students can land junior positions after completing all lessons')
    print('='*70)

    # Analyze Python
    python_coverage, python_weak = analyze_job_readiness('public/lessons-python.json', 'python')

    # Analyze Java
    java_coverage, java_weak = analyze_job_readiness('public/lessons-java.json', 'java')

    print(f'\n{"="*70}')
    print('OVERALL ASSESSMENT')
    print(f'{"="*70}')
    print(f'Python lessons with issues: {len(python_weak)}')
    print(f'Java lessons with issues: {len(java_weak)}')
    print(f'Total improvements needed: {len(python_weak) + len(java_weak)}')
    print(f'{"="*70}\n')
