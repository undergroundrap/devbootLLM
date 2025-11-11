#!/usr/bin/env python3
"""Fix lesson schema to standardize all lessons"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

def infer_difficulty(lesson):
    """Infer difficulty level from lesson content"""
    title = lesson.get('title', '').lower()
    tags = [tag.lower() for tag in lesson.get('tags', [])]
    description = lesson.get('description', '').lower()

    # Expert level indicators
    expert_keywords = ['advanced', 'expert', 'production', 'optimization', 'performance',
                      'architecture', 'design patterns', 'best practices', 'deployment',
                      'security', 'oauth', 'jwt', 'kubernetes', 'docker', 'cloud']

    # Advanced level indicators
    advanced_keywords = ['async', 'threading', 'decorators', 'generators', 'metaclass',
                        'reflection', 'annotations', 'streams', 'lambda', 'reactive']

    # Beginner level indicators
    beginner_keywords = ['basics', 'hello', 'introduction', 'getting started', 'first',
                        'simple', 'basic', 'beginner', 'fundamentals']

    # Check for expert indicators
    if any(keyword in title or keyword in description or keyword in tags for keyword in expert_keywords):
        return 'Expert'

    # Check for beginner indicators
    if any(keyword in title or keyword in description or keyword in tags for keyword in beginner_keywords):
        return 'Beginner'

    # Check for advanced indicators
    if any(keyword in title or keyword in description or keyword in tags for keyword in advanced_keywords):
        return 'Advanced'

    # Default to Intermediate
    return 'Intermediate'

def infer_category(lesson):
    """Infer category from lesson content"""
    title = lesson.get('title', '').lower()
    tags = [tag.lower() for tag in lesson.get('tags', [])]

    # Category mapping based on keywords
    category_keywords = {
        'Web Development': ['web', 'http', 'flask', 'django', 'fastapi', 'rest', 'api', 'html', 'css'],
        'Database': ['sql', 'database', 'sqlalchemy', 'orm', 'postgresql', 'mysql', 'mongodb'],
        'Data Science': ['pandas', 'numpy', 'matplotlib', 'data', 'analysis', 'visualization'],
        'Machine Learning': ['machine learning', 'ml', 'scikit-learn', 'tensorflow', 'model'],
        'Testing': ['test', 'pytest', 'unittest', 'mock', 'testing', 'junit', 'mockito', 'testcontainers'],
        'DevOps': ['docker', 'kubernetes', 'ci/cd', 'deployment', 'devops', 'container'],
        'Cloud': ['aws', 'cloud', 'lambda', 's3', 'ec2', 'boto3'],
        'Async': ['async', 'asyncio', 'asynchronous', 'concurrency', 'threading'],
        'Security': ['security', 'authentication', 'authorization', 'oauth', 'jwt', 'encryption'],
        'Algorithms': ['algorithm', 'sorting', 'searching', 'tree', 'graph', 'dynamic programming'],
        'OOP': ['class', 'object', 'inheritance', 'polymorphism', 'oop', 'encapsulation'],
        'Functional': ['functional', 'lambda', 'map', 'filter', 'reduce'],
    }

    # Check tags and title for category keywords
    for category, keywords in category_keywords.items():
        if any(keyword in title or keyword in tags for keyword in keywords):
            return category

    # Language-specific defaults
    if lesson.get('language') == 'python':
        return 'Core Python'
    elif lesson.get('language') == 'java':
        return 'Core Java'
    else:
        return 'Programming'

print('='*60)
print('FIXING LESSON SCHEMA')
print('='*60)

# Load lessons
print('\nLoading lessons...')
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

print(f'Loaded {len(py_lessons)} Python lessons and {len(java_lessons)} Java lessons')

# Fix Python lessons
print('\n--- Fixing Python Lessons ---')
fixed_py = 0
for lesson in py_lessons:
    changed = False

    # Rename initialCode to baseCode
    if 'initialCode' in lesson:
        lesson['baseCode'] = lesson.pop('initialCode')
        changed = True

    # Add missing difficulty
    if 'difficulty' not in lesson or not lesson.get('difficulty'):
        lesson['difficulty'] = infer_difficulty(lesson)
        changed = True

    # Add missing category
    if 'category' not in lesson or not lesson.get('category'):
        lesson['category'] = infer_category(lesson)
        changed = True

    if changed:
        fixed_py += 1

print(f'[OK] Fixed {fixed_py} Python lessons')

# Fix Java lessons
print('\n--- Fixing Java Lessons ---')
fixed_java = 0
for lesson in java_lessons:
    changed = False

    # Rename initialCode to baseCode
    if 'initialCode' in lesson:
        lesson['baseCode'] = lesson.pop('initialCode')
        changed = True

    # Add missing difficulty
    if 'difficulty' not in lesson or not lesson.get('difficulty'):
        lesson['difficulty'] = infer_difficulty(lesson)
        changed = True

    # Add missing category
    if 'category' not in lesson or not lesson.get('category'):
        lesson['category'] = infer_category(lesson)
        changed = True

    if changed:
        fixed_java += 1

print(f'[OK] Fixed {fixed_java} Java lessons')

# Save lessons
print('\n--- Saving lessons ---')
save_lessons('public/lessons-python.json', py_lessons)
save_lessons('public/lessons-java.json', java_lessons)

print('[OK] Saved Python lessons')
print('[OK] Saved Java lessons')

# Verify fix
print('\n--- Verification ---')
print('Checking sample lessons...')

sample_py = py_lessons[0]
print(f'\nPython lesson ID 1 fields: {list(sample_py.keys())}')
print(f'  - Has baseCode: {"baseCode" in sample_py}')
print(f'  - Has difficulty: {"difficulty" in sample_py}')
print(f'  - Has category: {"category" in sample_py}')
print(f'  - Difficulty: {sample_py.get("difficulty")}')
print(f'  - Category: {sample_py.get("category")}')

sample_java = java_lessons[0]
print(f'\nJava lesson ID 1 fields: {list(sample_java.keys())}')
print(f'  - Has baseCode: {"baseCode" in sample_java}')
print(f'  - Has difficulty: {"difficulty" in sample_java}')
print(f'  - Has category: {"category" in sample_java}')
print(f'  - Difficulty: {sample_java.get("difficulty")}')
print(f'  - Category: {sample_java.get("category")}')

print('\n' + '='*60)
print('LESSON SCHEMA FIXED!')
print('='*60)
print(f'Total fixed: {fixed_py + fixed_java} lessons ({fixed_py} Python + {fixed_java} Java)')
print('\nAll lessons now have:')
print('  - baseCode field (renamed from initialCode)')
print('  - difficulty field (Beginner/Intermediate/Advanced/Expert)')
print('  - category field (Web Development, Database, Testing, etc.)')
