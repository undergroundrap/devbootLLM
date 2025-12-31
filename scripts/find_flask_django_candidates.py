import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

flask_lessons = [l for l in lessons if 'Flask' in l['title'] and len(l['fullSolution']) < 13000]
django_lessons = [l for l in lessons if 'Django' in l['title'] and len(l['fullSolution']) < 13000]

print('Flask lessons under 13k chars:')
print('=' * 60)
for l in sorted(flask_lessons, key=lambda x: len(x['fullSolution']))[:10]:
    print(f'  {l["id"]:4d}: {l["title"]:45s} {len(l["fullSolution"]):>6,} chars')

print()
print('Django lessons under 13k chars:')
print('=' * 60)
for l in sorted(django_lessons, key=lambda x: len(x['fullSolution']))[:10]:
    print(f'  {l["id"]:4d}: {l["title"]:45s} {len(l["fullSolution"]):>6,} chars')
