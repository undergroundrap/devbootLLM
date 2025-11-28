#!/usr/bin/env python3
"""
Estimate learning timelines for students starting from zero.
Based on lesson difficulty, category, and realistic practice time.
"""

import json
from collections import defaultdict

def estimate_learning_timeline():
    print('=' * 80)
    print('LEARNING TIMELINE ESTIMATOR')
    print('How long to learn to code from ZERO?')
    print('=' * 80)
    print()

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        py_data = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    # Analyze each language
    for language, data in [('Python', py_data), ('Java', java_data)]:
        print('=' * 80)
        print(f'{language.upper()} LEARNING TIMELINE')
        print('=' * 80)
        print()

        analyze_timeline(data, language)
        print()

def analyze_timeline(lessons, language):
    """Calculate realistic learning timelines"""

    # Time estimates per lesson (in minutes)
    # Based on: reading tutorial, understanding concept, writing code, debugging, testing
    time_per_lesson = {
        'Beginner': 25,      # 25 min: Simple concepts, short code, quick to understand
        'Intermediate': 40,  # 40 min: More complex logic, longer code, some debugging
        'Advanced': 60,      # 60 min: Complex patterns, significant debugging, research
        'Expert': 90         # 90 min: Very complex, lots of debugging, deep understanding needed
    }

    # Count lessons by difficulty
    difficulty_counts = defaultdict(int)
    category_counts = defaultdict(int)

    for lesson in lessons:
        diff = lesson.get('difficulty', 'Beginner')
        cat = lesson.get('category', 'Unknown')
        difficulty_counts[diff] += 1
        category_counts[cat] += 1

    # Calculate total time
    total_minutes = 0
    breakdown = {}

    for diff, count in difficulty_counts.items():
        minutes = count * time_per_lesson.get(diff, 30)
        total_minutes += minutes
        breakdown[diff] = {'count': count, 'minutes': minutes}

    # Convert to hours and weeks
    total_hours = total_minutes / 60

    # Different pacing scenarios
    print('TIME BREAKDOWN BY DIFFICULTY:')
    print('-' * 80)
    for diff in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
        if diff in breakdown:
            count = breakdown[diff]['count']
            minutes = breakdown[diff]['minutes']
            hours = minutes / 60
            avg_time = time_per_lesson[diff]
            print(f'{diff:15s}: {count:4d} lessons × {avg_time:2d} min = {hours:6.1f} hours')
    print('-' * 80)
    print(f'{"TOTAL":15s}: {sum(d["count"] for d in breakdown.values()):4d} lessons = {total_hours:6.1f} hours')
    print()

    # Learning pace scenarios
    print('TIMELINE SCENARIOS:')
    print('=' * 80)
    print()

    scenarios = [
        {
            'name': 'PART-TIME LEARNER (5 hours/week)',
            'hours_per_week': 5,
            'description': 'Working full-time, studying evenings/weekends'
        },
        {
            'name': 'DEDICATED LEARNER (15 hours/week)',
            'hours_per_week': 15,
            'description': 'Part-time job or reduced hours, serious commitment'
        },
        {
            'name': 'BOOTCAMP PACE (40 hours/week)',
            'hours_per_week': 40,
            'description': 'Full-time study, immersive learning'
        },
        {
            'name': 'INTENSIVE (60 hours/week)',
            'hours_per_week': 60,
            'description': 'No other commitments, maximum intensity'
        }
    ]

    for scenario in scenarios:
        name = scenario['name']
        hours_week = scenario['hours_per_week']
        desc = scenario['description']

        # Calculate different milestones
        beginner_hours = breakdown.get('Beginner', {}).get('minutes', 0) / 60
        basic_hours = beginner_hours + breakdown.get('Intermediate', {}).get('minutes', 0) / 60
        job_ready_hours = total_hours * 0.7  # 70% of curriculum = job-ready

        print(f'{name}')
        print(f'  {desc}')
        print()

        # Milestone 1: Complete all beginner lessons
        weeks_beginner = beginner_hours / hours_week
        months_beginner = weeks_beginner / 4.33
        print(f'  [BASICS COMPLETE] ({breakdown.get("Beginner", {}).get("count", 0)} beginner lessons):')
        print(f'     {weeks_beginner:.1f} weeks ({months_beginner:.1f} months)')
        print(f'     You can: Write simple programs, understand syntax, use variables/loops/functions')
        print()

        # Milestone 2: Beginner + Intermediate
        weeks_basic = basic_hours / hours_week
        months_basic = weeks_basic / 4.33
        intermediate_count = breakdown.get('Beginner', {}).get('count', 0) + breakdown.get('Intermediate', {}).get('count', 0)
        print(f'  [BASIC COMPETENCE] ({intermediate_count} lessons):')
        print(f'     {weeks_basic:.1f} weeks ({months_basic:.1f} months)')
        print(f'     You can: Build small apps, work with APIs, use OOP, handle databases')
        print()

        # Milestone 3: Job-ready (70% of all lessons)
        weeks_job = job_ready_hours / hours_week
        months_job = weeks_job / 4.33
        job_lesson_count = int(len(lessons) * 0.7)
        print(f'  [JOB-READY DEVELOPER] (~{job_lesson_count} lessons):')
        print(f'     {weeks_job:.1f} weeks ({months_job:.1f} months)')
        print(f'     You can: Apply for junior dev roles, build full applications, interview confidently')
        print()

        # Milestone 4: Complete curriculum
        weeks_complete = total_hours / hours_week
        months_complete = weeks_complete / 4.33
        print(f'  [COMPLETE MASTERY] (all {len(lessons)} lessons):')
        print(f'     {weeks_complete:.1f} weeks ({months_complete:.1f} months)')
        print(f'     You can: Handle advanced topics, work with any framework, mentor others')
        print()
        print('-' * 80)
        print()

    # Recommendations
    print('=' * 80)
    print('REALISTIC RECOMMENDATIONS:')
    print('=' * 80)
    print()

    print('[FASTEST PATH TO EMPLOYMENT]:')
    print()
    print('  1. BEGINNER TRACK (2-3 months at 15 hrs/week):')
    print(f'     - Complete all {breakdown.get("Beginner", {}).get("count", 0)} beginner lessons')
    print('     - Build 3-5 small projects from scratch')
    print('     - You understand: variables, loops, functions, basic OOP')
    print()
    print('  2. INTERMEDIATE TRACK (3-4 months at 15 hrs/week):')
    print(f'     - Complete {breakdown.get("Intermediate", {}).get("count", 0)} intermediate lessons')
    print('     - Build 2-3 medium-sized applications')
    print('     - You can: Work with databases, APIs, web frameworks')
    print()
    print('  3. JOB-READY PROJECTS (1-2 months):')
    print('     - Build 2-3 portfolio projects using advanced lessons')
    print('     - Deploy to production (Heroku/AWS/Vercel)')
    print('     - Write clean code, tests, documentation')
    print()

    total_job_months = (breakdown.get('Beginner', {}).get('minutes', 0) / 60 +
                       breakdown.get('Intermediate', {}).get('minutes', 0) / 60) / 15 / 4.33 + 1.5

    print(f'  [TOTAL TO JOB-READY]: ~{total_job_months:.0f} months')
    print('     (At 15 hours/week with focused practice)')
    print()
    print()

    # Quality matters more than speed
    print('=' * 80)
    print('[IMPORTANT NOTES]:')
    print('=' * 80)
    print()
    print('  - These are MINIMUM times assuming focused, quality practice')
    print('  - SLOWER IS BETTER than rushing and not understanding')
    print('  - Taking 2x longer but mastering concepts = better outcome')
    print('  - Build projects outside the curriculum for real learning')
    print('  - Review and practice is NOT included in these estimates')
    print('  - Job-ready = technical skills + portfolio + interview prep')
    print()
    print('  [Most successful students]:')
    print('     - Take 6-12 months to feel job-ready (part-time)')
    print('     - Spend 50% time on lessons, 50% on projects')
    print('     - Review concepts multiple times')
    print('     - Build things they are passionate about')
    print()

if __name__ == '__main__':
    estimate_learning_timeline()
