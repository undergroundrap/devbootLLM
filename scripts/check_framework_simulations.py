"""
Check framework simulation status - ASCII version
"""
import json

print("=" * 80)
print("FRAMEWORK SIMULATION STATUS")
print("=" * 80)

# Python frameworks
py_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))
py_frameworks = [l for l in py_lessons if l.get('isFramework')]

py_simulations = []
py_stubs = []

for lesson in py_frameworks:
    sol = lesson.get('fullSolution', '')
    fw = lesson.get('frameworkName', 'Unknown')
    has_sim = '# In production:' in sol and len(sol) > 2000

    if has_sim:
        py_simulations.append(fw)
    else:
        py_stubs.append({
            'id': lesson.get('id'),
            'title': lesson.get('title', ''),
            'framework': fw,
            'chars': len(sol)
        })

print(f'\nPYTHON FRAMEWORK LESSONS: {len(py_frameworks)} total')
print(f'  [OK] Realistic Simulations: {len(py_simulations)} ({len(py_simulations)/len(py_frameworks)*100:.1f}%)')
print(f'  [STUB] Still Need Simulation: {len(py_stubs)} ({len(py_stubs)/len(py_frameworks)*100:.1f}%)')

# Group stubs by framework
stub_by_fw = {}
for stub in py_stubs:
    fw = stub['framework'].lower()
    if fw not in stub_by_fw:
        stub_by_fw[fw] = []
    stub_by_fw[fw].append(stub)

if py_stubs:
    print(f'\n{"="*80}')
    print('PYTHON STUBS REMAINING (Need Simulation):')
    print('=' * 80)

    for fw, stubs in sorted(stub_by_fw.items(), key=lambda x: len(x[1]), reverse=True):
        print(f'\n{fw.upper()}: {len(stubs)} lessons')
        for stub in stubs[:5]:
            print(f'  ID {stub["id"]:4d}: {stub["title"][:50]:50s} ({stub["chars"]:4d} chars)')
        if len(stubs) > 5:
            print(f'  ... and {len(stubs)-5} more')

# Java frameworks
java_lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

java_frameworks = []
for lesson in java_lessons:
    title = lesson.get('title', '').lower()
    cat = lesson.get('category', '').lower()

    is_framework = any([
        'spring' in title or 'spring' in cat,
        'kafka' in title or 'kafka' in cat,
        'grpc' in title or 'grpc' in cat,
        'oauth' in title,
        'jwt' in title,
        'microservices' in cat,
        'cloud' in cat,
        'istio' in title,
        'resilience4j' in title,
        'feign' in title,
    ])

    if is_framework:
        java_frameworks.append(lesson)

java_sims = 0
java_stubs_list = []

for lesson in java_frameworks:
    sol = lesson.get('fullSolution', '')
    has_sim = '// In production:' in sol and len(sol) > 2000

    if has_sim:
        java_sims += 1
    else:
        java_stubs_list.append({
            'id': lesson.get('id'),
            'title': lesson.get('title', ''),
            'category': lesson.get('category', ''),
            'chars': len(sol)
        })

print(f'\n{"="*80}')
print('JAVA FRAMEWORK LESSONS:')
print('=' * 80)
print(f'\nTotal framework-related: {len(java_frameworks)} lessons')
print(f'  [OK] Have Simulations: {java_sims} ({java_sims/len(java_frameworks)*100:.1f}% if java_frameworks else 0)')
print(f'  [STUB] Still Need Simulation: {len(java_stubs_list)} ({len(java_stubs_list)/len(java_frameworks)*100:.1f}% if java_frameworks else 0)')

if java_stubs_list:
    print(f'\nJava lessons needing simulation (showing all):')
    for stub in sorted(java_stubs_list, key=lambda x: -x['chars']):
        print(f'  ID {stub["id"]:4d}: {stub["title"][:45]:45s} | {stub["category"]:15s} | {stub["chars"]:4d} chars')

# Overall summary
print(f'\n{"="*80}')
print('OVERALL PLATFORM STATUS:')
print('=' * 80)

total_frameworks = len(py_frameworks) + len(java_frameworks)
total_sims = len(py_simulations) + java_sims
total_stubs = len(py_stubs) + len(java_stubs_list)

print(f'\nTotal Framework Lessons Requiring Packages: {total_frameworks}')
print(f'  [OK] Simulated (No Install Needed): {total_sims} ({total_sims/total_frameworks*100:.1f}%)')
print(f'  [STUB] Still Need Simulation: {total_stubs} ({total_stubs/total_frameworks*100:.1f}%)')

print(f'\n{"="*80}')
print('ANALYSIS:')
print('=' * 80)

boto3_count = len([s for s in py_stubs if s['framework'].lower() == 'boto3'])
non_boto3 = len(py_stubs) - boto3_count

print(f'\nPython Breakdown:')
print(f'  - boto3 stubs: {boto3_count} (AWS-specific, kept minimal intentionally)')
print(f'  - Other stubs: {non_boto3}')

print(f'\nJava Breakdown:')
print(f'  - Framework stubs: {len(java_stubs_list)}')

if boto3_count == len(py_stubs) and len(java_stubs_list) == 0:
    print(f'\n{"="*80}')
    print('[SUCCESS] ALL JOB-CRITICAL FRAMEWORKS ARE SIMULATED!')
    print('=' * 80)
    print('\n[OK] Only boto3 AWS stubs remain (intentionally minimal)')
    print('[OK] All other frameworks have realistic simulations')
    print('[OK] Students can learn without installing packages')
    effective = total_sims / (total_sims + non_boto3 + len(java_stubs_list)) * 100 if (total_sims + non_boto3 + len(java_stubs_list)) > 0 else 0
    print(f'\nEffective Coverage: {effective:.1f}%')
elif non_boto3 == 0:
    print(f'\n{"="*80}')
    print('[NEARLY COMPLETE] Python 100% simulated!')
    print('=' * 80)
    print(f'\nRemaining: {len(java_stubs_list)} Java framework lessons')
    print('These could be upgraded for even better coverage')
else:
    print(f'\n{"="*80}')
    print('[IN PROGRESS] Framework simulation ongoing')
    print('=' * 80)
    print(f'\nStill needed:')
    print(f'  - Python: {non_boto3} lessons')
    print(f'  - Java: {len(java_stubs_list)} lessons')
