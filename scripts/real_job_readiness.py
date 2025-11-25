"""
Real Job Readiness Assessment
Checks if students can actually get junior developer jobs
Based on real job requirements, not arbitrary metrics
"""
import json

# What junior devs ACTUALLY need to know (from real job postings)
JOB_REQUIREMENTS = {
    'python': {
        'essential': {
            'Build a web API': ['flask', 'django', 'fastapi', 'rest'],
            'Work with databases': ['sql', 'orm', 'sqlalchemy', 'postgresql', 'mysql'],
            'Write tests': ['pytest', 'unittest', 'test', 'mock'],
            'Use Git': ['git', 'branch', 'merge', 'commit'],
            'Handle errors': ['exception', 'try', 'except', 'error'],
            'Work with data': ['json', 'csv', 'pandas', 'api'],
        },
        'common': {
            'Async programming': ['async', 'await', 'asyncio', 'concurrent'],
            'Docker/deployment': ['docker', 'deploy', 'container'],
            'AWS/Cloud': ['aws', 's3', 'lambda', 'cloud'],
            'Data science basics': ['numpy', 'pandas', 'matplotlib'],
        },
        'interview': {
            'Algorithms': ['algorithm', 'sort', 'search', 'complexity'],
            'Data structures': ['list', 'dict', 'set', 'tree', 'graph'],
            'System design': ['design', 'architecture', 'scalability'],
        }
    },
    'java': {
        'essential': {
            'Spring Boot apps': ['spring boot', '@springbootapplication', '@restcontroller'],
            'REST APIs': ['rest', '@getmapping', '@postmapping', 'api'],
            'Database/JPA': ['jpa', 'hibernate', '@entity', 'repository'],
            'Write tests': ['junit', 'mockito', 'test', '@test'],
            'Use Git/Maven': ['git', 'maven', 'build'],
            'Handle errors': ['exception', 'try', 'catch', 'throw'],
        },
        'common': {
            'Streams/Lambdas': ['stream', 'lambda', 'filter', 'map', 'collect'],
            'Spring Security': ['security', 'authentication', 'authorization'],
            'Docker/K8s': ['docker', 'kubernetes', 'container'],
            'Microservices': ['microservice', 'kafka', 'message', 'feign'],
        },
        'interview': {
            'Algorithms': ['algorithm', 'sort', 'search', 'complexity'],
            'Data structures': ['list', 'map', 'set', 'tree', 'graph', 'queue'],
            'Design patterns': ['pattern', 'singleton', 'factory', 'strategy'],
        }
    }
}

def check_requirement(lessons, keywords):
    """Check if requirement is covered by lessons"""
    matching_lessons = []

    for lesson in lessons:
        title_lower = lesson['title'].lower()
        tutorial_lower = lesson.get('tutorial', '').lower()
        solution_lower = lesson.get('fullSolution', '').lower()

        # Check if any keyword matches
        for keyword in keywords:
            if (keyword in title_lower or
                keyword in tutorial_lower or
                keyword in solution_lower):
                matching_lessons.append(lesson)
                break

    return matching_lessons

def assess_project_capability(lessons, lang):
    """Can students build a real project?"""

    if lang == 'python':
        # Can they build a Flask/Django app with database?
        web_lessons = [l for l in lessons if any(fw in l['title'].lower()
                                                   for fw in ['flask', 'django', 'fastapi'])]
        db_lessons = [l for l in lessons if any(db in l['title'].lower()
                                                  for db in ['sql', 'database', 'orm'])]

        has_routes = any('@app.route' in l.get('fullSolution', '') or
                        '@api.get' in l.get('fullSolution', '') or
                        'path(' in l.get('fullSolution', '')
                        for l in web_lessons)

        has_models = any('class' in l.get('fullSolution', '') and
                        ('Model' in l.get('fullSolution', '') or
                         'db.' in l.get('fullSolution', ''))
                        for l in db_lessons)

        return {
            'web_framework': len(web_lessons) >= 10,
            'database': len(db_lessons) >= 5,
            'routes': has_routes,
            'models': has_models,
            'ready': len(web_lessons) >= 10 and len(db_lessons) >= 5 and has_routes and has_models
        }

    else:  # java
        # Can they build a Spring Boot app with JPA?
        spring_lessons = [l for l in lessons if 'spring' in l['title'].lower()]
        jpa_lessons = [l for l in lessons if any(term in l['title'].lower()
                                                   for term in ['jpa', 'hibernate', 'database'])]

        has_controllers = any('@RestController' in l.get('fullSolution', '') or
                             '@Controller' in l.get('fullSolution', '')
                             for l in spring_lessons)

        has_entities = any('@Entity' in l.get('fullSolution', '')
                          for l in jpa_lessons)

        return {
            'spring_boot': len(spring_lessons) >= 15,
            'database': len(jpa_lessons) >= 5,
            'controllers': has_controllers,
            'entities': has_entities,
            'ready': len(spring_lessons) >= 15 and len(jpa_lessons) >= 5 and has_controllers and has_entities
        }

def analyze_job_readiness(lessons_file, lang):
    """Real job readiness assessment"""

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    requirements = JOB_REQUIREMENTS[lang]

    print(f'\n{"="*70}')
    print(f'REAL JOB READINESS ASSESSMENT - {lang.upper()}')
    print(f'{"="*70}')
    print(f'Total lessons: {len(lessons)}\n')

    # Check essential skills
    print('=== ESSENTIAL SKILLS (Must Have for Junior Jobs) ===\n')
    essential_met = 0
    for skill, keywords in requirements['essential'].items():
        matching = check_requirement(lessons, keywords)
        is_met = len(matching) >= 3  # Need at least 3 lessons per skill

        status = '[OK]' if is_met else '[!!]'
        print(f'{status} {skill}: {len(matching)} lessons')

        if is_met:
            essential_met += 1
        elif len(matching) < 3:
            print(f'     [WARNING] Need more coverage - only {len(matching)} lessons')

        print()

    essential_score = 100 * essential_met / len(requirements['essential'])

    # Check common skills
    print('=== COMMON SKILLS (Often Required) ===\n')
    common_met = 0
    for skill, keywords in requirements['common'].items():
        matching = check_requirement(lessons, keywords)
        is_met = len(matching) >= 2

        status = '[OK]' if is_met else '[ ]'
        print(f'{status} {skill}: {len(matching)} lessons')

        if is_met:
            common_met += 1
        print()

    common_score = 100 * common_met / len(requirements['common']) if requirements['common'] else 100

    # Check interview skills
    print('=== INTERVIEW SKILLS (For Getting Hired) ===\n')
    interview_met = 0
    for skill, keywords in requirements['interview'].items():
        matching = check_requirement(lessons, keywords)
        is_met = len(matching) >= 5

        status = '[OK]' if is_met else '[ ]'
        print(f'{status} {skill}: {len(matching)} lessons')

        if is_met:
            interview_met += 1
        print()

    interview_score = 100 * interview_met / len(requirements['interview']) if requirements['interview'] else 100

    # Project capability
    print('=== PROJECT BUILDING CAPABILITY ===\n')
    project = assess_project_capability(lessons, lang)

    for capability, met in project.items():
        if capability == 'ready':
            continue
        status = '[OK]' if met else '[!!]'
        print(f'{status} {capability}: {met}')

    print()

    # Overall assessment
    print(f'{"="*70}')
    print('JOB READINESS SCORE')
    print(f'{"="*70}')
    print(f'Essential Skills:  {essential_score:5.1f}% ({essential_met}/{len(requirements["essential"])})')
    print(f'Common Skills:     {common_score:5.1f}% ({common_met}/{len(requirements["common"])})')
    print(f'Interview Skills:  {interview_score:5.1f}% ({interview_met}/{len(requirements["interview"])})')
    print(f'Project Ready:     {"YES" if project["ready"] else "NO"}')

    # Weighted score (essential skills matter most)
    final_score = (
        essential_score * 0.50 +  # 50% weight
        common_score * 0.25 +     # 25% weight
        interview_score * 0.25    # 25% weight
    )

    print(f'\nFINAL SCORE: {final_score:.1f}/100')

    if final_score >= 90:
        print('[EXCELLENT] Students can definitely land junior positions!')
    elif final_score >= 75:
        print('[GOOD] Students are job-ready with strong preparation!')
    elif final_score >= 60:
        print('[FAIR] Students need more practice in key areas')
    else:
        print('[NEEDS WORK] Missing critical job skills')

    if project['ready']:
        print('[OK] Can build production-ready projects')
    else:
        print('[!!] Need more project-building practice')

    print(f'{"="*70}\n')

    return final_score

if __name__ == '__main__':
    print('\n' + '='*70)
    print('JUNIOR DEVELOPER JOB READINESS - REAL ASSESSMENT')
    print('Based on actual job requirements from tech companies')
    print('='*70)

    python_score = analyze_job_readiness('public/lessons-python.json', 'python')
    java_score = analyze_job_readiness('public/lessons-java.json', 'java')

    print(f'{"="*70}')
    print('FINAL VERDICT')
    print(f'{"="*70}')
    print(f'Python: {python_score:.1f}/100')
    print(f'Java:   {java_score:.1f}/100')

    avg_score = (python_score + java_score) / 2
    print(f'\nOverall: {avg_score:.1f}/100')

    if avg_score >= 85:
        print('\n[SUCCESS] Your students ARE READY to land junior developer jobs!')
        print('They have the skills, projects, and interview prep needed.')
    else:
        print(f'\n[WORK NEEDED] Students need stronger coverage in essential areas.')

    print(f'{"="*70}\n')
