import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8'))

# Find all stub lessons (not boto3)
stubs = []
for l in lessons:
    if l.get('isFramework'):
        sol = l.get('fullSolution', '')
        is_stub = not('# In production:' in sol and len(sol) > 2000)
        fw = l.get('frameworkName', '').lower()

        if is_stub and fw != 'boto3':
            stubs.append({
                'id': l['id'],
                'title': l['title'],
                'framework': fw,
                'chars': len(sol)
            })

print('REMAINING NON-BOTO3 STUBS (9 lessons):\n')
print('=' * 80)
for s in sorted(stubs, key=lambda x: (x['framework'], x['id'])):
    print(f"{s['framework']:12s} | ID {s['id']:4d} | {s['title'][:55]:55s} | {s['chars']:3d} chars")

print('\n' + '=' * 80)
print(f'\nTotal: {len(stubs)} stubs remaining')
print('RECOMMENDATION: Upgrade these to reach 149/176 (84.7%) coverage')
print('This would make the platform essentially complete for Python frameworks!')
