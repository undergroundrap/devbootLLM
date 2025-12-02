import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))

# Batch 4 lesson IDs
django_4a = [515, 516, 517, 518, 519, 752, 753, 754, 755, 756, 757, 758, 759]
django_4b = [762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772, 773, 774]
sqlalchemy_4c = [782, 783, 784, 785, 786, 787, 964, 965, 966, 967, 968, 969]
pytest_4d = [508, 808, 809, 810, 811, 812, 813, 814, 847, 982, 983, 984, 985]

all_batch4 = django_4a + django_4b + sqlalchemy_4c + pytest_4d

print('BATCH 4 VERIFICATION:\n')
print('=' * 80)

# Django 4a
print('\nDJANGO BATCH 4A (13 lessons):')
total_chars = 0
for lid in django_4a:
    lesson = next((l for l in lessons if l.get('id') == lid), None)
    sol = lesson.get('fullSolution', '') if lesson else ''
    has_prod = '# In production:' in sol
    length = len(sol)
    total_chars += length
    status = "SIMULATION" if (has_prod and length > 2000) else "STUB"
    print(f'  ID {lid}: {lesson.get("title", "")[:45]:45s} - {length:5d} chars - {status}')
print(f'  Total: {total_chars:,} chars, avg {total_chars//len(django_4a):,} chars/lesson')

# Django 4b
print('\nDJANGO BATCH 4B (13 lessons):')
total_chars = 0
for lid in django_4b:
    lesson = next((l for l in lessons if l.get('id') == lid), None)
    sol = lesson.get('fullSolution', '') if lesson else ''
    has_prod = '# In production:' in sol
    length = len(sol)
    total_chars += length
    status = "SIMULATION" if (has_prod and length > 2000) else "STUB"
    print(f'  ID {lid}: {lesson.get("title", "")[:45]:45s} - {length:5d} chars - {status}')
print(f'  Total: {total_chars:,} chars, avg {total_chars//len(django_4b):,} chars/lesson')

# SQLAlchemy 4c
print('\nSQLALCHEMY BATCH 4C (12 lessons):')
total_chars = 0
for lid in sqlalchemy_4c:
    lesson = next((l for l in lessons if l.get('id') == lid), None)
    sol = lesson.get('fullSolution', '') if lesson else ''
    has_prod = '# In production:' in sol
    length = len(sol)
    total_chars += length
    status = "SIMULATION" if (has_prod and length > 2000) else "STUB"
    print(f'  ID {lid}: {lesson.get("title", "")[:45]:45s} - {length:5d} chars - {status}')
print(f'  Total: {total_chars:,} chars, avg {total_chars//len(sqlalchemy_4c):,} chars/lesson')

# pytest 4d
print('\nPYTEST BATCH 4D (13 lessons):')
total_chars = 0
for lid in pytest_4d:
    lesson = next((l for l in lessons if l.get('id') == lid), None)
    sol = lesson.get('fullSolution', '') if lesson else ''
    has_prod = '# In production:' in sol
    length = len(sol)
    total_chars += length
    status = "SIMULATION" if (has_prod and length > 2000) else "STUB"
    print(f'  ID {lid}: {lesson.get("title", "")[:45]:45s} - {length:5d} chars - {status}')
print(f'  Total: {total_chars:,} chars, avg {total_chars//len(pytest_4d):,} chars/lesson')

# Overall summary
print('\n' + '=' * 80)
print('BATCH 4 SUMMARY:')
print('=' * 80)
batch4_lessons = [l for l in lessons if l.get('id') in all_batch4]
total_batch4_chars = sum(len(l.get('fullSolution', '')) for l in batch4_lessons)
simulations = sum(1 for l in batch4_lessons if '# In production:' in l.get('fullSolution', '') and len(l.get('fullSolution', '')) > 2000)

print(f'Total lessons: {len(all_batch4)}')
print(f'Simulations: {simulations}/{len(all_batch4)}')
print(f'Total code: {total_batch4_chars:,} characters')
print(f'Average: {total_batch4_chars//len(all_batch4):,} chars/lesson')

print('\n' + '=' * 80)
print('COMPLETE FRAMEWORK STATUS:')
print('=' * 80)
print('Previous: 111 simulations (batches 1-3)')
print(f'Batch 4:  {simulations} simulations (Django, SQLAlchemy, pytest)')
print(f'NEW TOTAL: {111 + simulations} simulations')
print('=' * 80)
