import json
import re

def find_stubs_to_upgrade():
    """Find all framework stubs that need upgrading to realistic simulations"""

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    stubs = []
    simulations = []

    for lesson in python_lessons + java_lessons:
        if not lesson.get('isFramework'):
            continue

        lid = lesson.get('id')
        title = lesson.get('title', '')
        framework = lesson.get('frameworkName', '')
        language = lesson.get('language', '')
        solution = lesson.get('fullSolution', '')

        # Check if it's a realistic simulation or a stub
        is_realistic = False

        # Criteria for realistic simulation:
        # 1. Length > 1000 chars
        # 2. Has class definition OR significant logic
        # 3. Not just print/println

        if len(solution) > 1000:
            has_class = 'class ' in solution
            code_lines = [l for l in solution.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('//')]

            if has_class and len(code_lines) > 30:
                is_realistic = True

        # Check if it's just a print stub
        is_print_stub = False
        lines = [l.strip() for l in solution.split('\n') if l.strip() and not l.strip().startswith('#') and not l.strip().startswith('//')]

        if language == 'python':
            print_lines = [l for l in lines if l.startswith('print(')]
            if len(print_lines) > 0 and len(lines) < 10:
                is_print_stub = True
        elif language == 'java':
            print_lines = [l for l in lines if 'System.out.println(' in l]
            if len(print_lines) > 0 and len(lines) < 15:
                is_print_stub = True

        if is_realistic:
            simulations.append({
                'id': lid,
                'title': title,
                'framework': framework,
                'language': language,
                'length': len(solution)
            })
        else:
            stubs.append({
                'id': lid,
                'title': title,
                'framework': framework,
                'language': language,
                'length': len(solution),
                'is_print_stub': is_print_stub
            })

    # Group stubs by framework
    stubs_by_framework = {}
    for stub in stubs:
        fw = stub['framework']
        if fw not in stubs_by_framework:
            stubs_by_framework[fw] = []
        stubs_by_framework[fw].append(stub)

    print("="*70)
    print("FRAMEWORK STUBS NEEDING UPGRADE")
    print("="*70)
    print(f"\nTotal realistic simulations: {len(simulations)}")
    print(f"Total stubs to upgrade: {len(stubs)}")
    print()

    # Priority frameworks
    priority = ['Kafka', 'Redis', 'Flask', 'FastAPI', 'pandas', 'boto3', 'Celery', 'gRPC', 'GraphQL']

    print("HIGH PRIORITY UPGRADES:")
    print("-"*70)
    total_priority = 0
    for fw in priority:
        if fw in stubs_by_framework:
            count = len(stubs_by_framework[fw])
            print_count = len([s for s in stubs_by_framework[fw] if s['is_print_stub']])
            print(f"{fw}: {count} stubs ({print_count} are just print statements)")
            total_priority += count

    print(f"\nTotal high-priority stubs: {total_priority}")

    print("\n\nOTHER FRAMEWORKS:")
    print("-"*70)
    for fw in sorted(stubs_by_framework.keys()):
        if fw not in priority:
            count = len(stubs_by_framework[fw])
            print(f"{fw}: {count} stubs")

    # Save detailed list
    with open('framework_stubs_to_upgrade.json', 'w', encoding='utf-8') as f:
        json.dump({
            'stubs': stubs,
            'simulations': simulations,
            'by_framework': stubs_by_framework,
            'priority_frameworks': priority
        }, f, indent=2, ensure_ascii=False)

    print("\n\nDetailed list saved to: framework_stubs_to_upgrade.json")

    return stubs, simulations, stubs_by_framework

if __name__ == '__main__':
    find_stubs_to_upgrade()
