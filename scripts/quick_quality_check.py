"""
Quick Quality Check - Find issues without compilation testing
Focuses on content quality issues
"""
import json

def check_lesson_issues(lesson, lang):
    """Check for quality issues"""
    issues = []
    solution = lesson.get('fullSolution', '')
    tutorial = lesson.get('tutorial', '')
    difficulty = lesson.get('difficulty', '')
    title = lesson['title']

    # 1. Empty solution
    if len(solution.strip()) < 20:
        issues.append('[CRITICAL] Solution too short or empty')
        return issues

    # 2. Solution length for difficulty
    min_lengths = {'Beginner': 50, 'Intermediate': 150, 'Advanced': 400, 'Expert': 500}
    min_len = min_lengths.get(difficulty, 50)

    if len(solution) < min_len:
        issues.append(f'Solution short for {difficulty}: {len(solution)} chars (need {min_len}+)')

    # 3. Tutorial length
    min_tutorial = {'Beginner': 300, 'Intermediate': 500, 'Advanced': 800, 'Expert': 1000}
    min_tut = min_tutorial.get(difficulty, 300)

    if len(tutorial) < min_tut:
        issues.append(f'Tutorial short for {difficulty}: {len(tutorial)} chars (need {min_tut}+)')

    # 4. Framework imports (Python)
    if lang == 'python':
        if 'flask' in title.lower() and 'from flask' not in solution.lower():
            issues.append('[HIGH] Flask lesson missing Flask imports')

        if 'django' in title.lower() and 'django' not in solution.lower():
            issues.append('[HIGH] Django lesson missing Django code')

        if 'pandas' in title.lower() and 'pandas' not in solution.lower() and 'pd.' not in solution:
            issues.append('[HIGH] Pandas lesson missing pandas')

    # 5. Framework annotations (Java)
    if lang == 'java':
        if 'spring' in title.lower():
            # Check for any Spring annotation
            spring_annotations = [
                '@SpringBoot', '@RestController', '@Service', '@Repository', '@Component',
                '@Entity', '@Autowired', '@Transactional', '@Cacheable', '@CachePut', '@CacheEvict',
                '@KafkaListener', '@Bean', '@Configuration', '@ConditionalOnClass',
                '@Procedure', '@CreatedDate', '@LastModifiedDate', '@EnableJpaAuditing'
            ]
            if not any(a in solution for a in spring_annotations):
                issues.append('[HIGH] Spring lesson missing annotations')

    # 6. Expected output
    expected = lesson.get('expectedOutput', '')
    if ('print(' in solution or 'System.out' in solution) and len(expected.strip()) < 5:
        issues.append('Solution prints but expectedOutput missing')

    return issues

def quick_check(lessons_file, lang):
    """Quick quality check"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print(f'\n{"="*70}')
    print(f'QUICK QUALITY CHECK - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Checking {len(lessons)} lessons...\n')

    critical = []
    high = []
    medium = []

    for lesson in lessons:
        issues = check_lesson_issues(lesson, lang)
        if not issues:
            continue

        data = {'id': lesson['id'], 'title': lesson['title'], 'difficulty': lesson.get('difficulty', ''), 'issues': issues}

        has_critical = any('[CRITICAL]' in i for i in issues)
        has_high = any('[HIGH]' in i for i in issues)

        if has_critical:
            critical.append(data)
        elif has_high:
            high.append(data)
        else:
            medium.append(data)

    # Report
    print(f'=== CRITICAL ISSUES ===')
    print(f'Found: {len(critical)} lessons\n')
    for i, l in enumerate(critical[:10], 1):
        print(f'{i}. Lesson {l["id"]}: {l["title"]} ({l["difficulty"]})')
        for issue in l['issues']:
            print(f'   {issue}')
    if len(critical) > 10:
        print(f'   ... and {len(critical)-10} more')

    print(f'\n=== HIGH PRIORITY ===')
    print(f'Found: {len(high)} lessons\n')
    for i, l in enumerate(high[:10], 1):
        print(f'{i}. Lesson {l["id"]}: {l["title"]} ({l["difficulty"]})')
        for issue in l['issues']:
            print(f'   {issue}')
    if len(high) > 10:
        print(f'   ... and {len(high)-10} more')

    print(f'\n=== MEDIUM PRIORITY ===')
    print(f'Found: {len(medium)} lessons')

    print(f'\n=== SUMMARY ===')
    print(f'Critical:  {len(critical)}')
    print(f'High:      {len(high)}')
    print(f'Medium:    {len(medium)}')
    print(f'Clean:     {len(lessons) - len(critical) - len(high) - len(medium)}')

    must_fix = len(critical) + len(high)
    if must_fix == 0:
        print(f'\n[OK] No critical or high priority issues!')
    else:
        print(f'\n[ACTION] Need to fix {must_fix} lessons')

    print(f'{"="*70}\n')

    return critical, high, medium

if __name__ == '__main__':
    print('\n' + '='*70)
    print('QUICK QUALITY CHECK - CONTENT ONLY')
    print('='*70)

    py_c, py_h, py_m = quick_check('public/lessons-python.json', 'python')
    java_c, java_h, java_m = quick_check('public/lessons-java.json', 'java')

    print(f'{"="*70}')
    print('OVERALL')
    print(f'{"="*70}')
    print(f'Python - Critical: {len(py_c)}, High: {len(py_h)}, Medium: {len(py_m)}')
    print(f'Java   - Critical: {len(java_c)}, High: {len(java_h)}, Medium: {len(java_m)}')

    total = len(py_c) + len(py_h) + len(java_c) + len(java_h)
    print(f'\nTOTAL MUST-FIX: {total}')

    if total == 0:
        print('[SUCCESS] All lessons are job-ready!')
    else:
        print(f'[TODO] Fix {total} lessons')

    print(f'{"="*70}\n')
