#!/usr/bin/env python3
"""Reorganize lessons by framework grouping instead of chronological order"""

import json
from collections import defaultdict

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

def get_framework(lesson):
    """Extract framework from lesson title"""
    title = lesson['title']

    # Check for framework prefixes in title
    if title.startswith('Flask -'):
        return 'Flask'
    elif title.startswith('Django -') or 'Django' in title:
        return 'Django'
    elif title.startswith('FastAPI -'):
        return 'FastAPI'
    elif title.startswith('SQLAlchemy -'):
        return 'SQLAlchemy'
    elif title.startswith('pandas -') or 'pandas' in title:
        return 'pandas'
    elif title.startswith('NumPy -'):
        return 'NumPy'
    elif title.startswith('scikit-learn -') or 'scikit-learn' in title:
        return 'scikit-learn'
    elif title.startswith('Celery -'):
        return 'Celery'
    elif title.startswith('pytest -'):
        return 'pytest'
    elif title.startswith('AWS boto3 -'):
        return 'AWS boto3'
    elif title.startswith('Redis -'):
        return 'Redis'
    elif title.startswith('Docker -'):
        return 'Docker'
    elif title.startswith('asyncio -'):
        return 'asyncio'
    elif title.startswith('Data Engineering -'):
        return 'Data Engineering'

    # Check tags for framework
    tags = lesson.get('tags', [])
    for tag in tags:
        if tag in ['Flask', 'Django', 'FastAPI', 'SQLAlchemy', 'pandas', 'NumPy',
                   'scikit-learn', 'Celery', 'pytest', 'AWS', 'boto3', 'Redis',
                   'Docker', 'asyncio']:
            return tag

    # Default to category or 'Core Python'
    return lesson.get('category', 'Core Python')

def get_java_framework(lesson):
    """Extract framework from Java lesson title"""
    title = lesson['title']

    # Check for framework prefixes
    if 'Spring Boot' in title:
        return 'Spring Boot'
    elif 'Spring Data' in title:
        return 'Spring Data'
    elif 'Spring Security' in title:
        return 'Spring Security'
    elif 'Spring Cloud' in title:
        return 'Spring Cloud'
    elif 'Reactive' in title or 'WebFlux' in title:
        return 'Reactive'
    elif 'Kafka' in title:
        return 'Kafka'
    elif 'Kubernetes' in title:
        return 'Kubernetes'
    elif 'JVM' in title:
        return 'JVM'
    elif 'GraphQL' in title:
        return 'GraphQL'
    elif 'Mockito' in title:
        return 'Mockito'
    elif 'Testcontainers' in title:
        return 'Testcontainers'
    elif 'JUnit' in title:
        return 'JUnit'
    elif 'Docker' in title:
        return 'Docker'
    elif 'gRPC' in title:
        return 'gRPC'
    elif 'Quarkus' in title:
        return 'Quarkus'

    # Check tags
    tags = lesson.get('tags', [])
    for tag in tags:
        if tag in ['Spring Boot', 'Spring Data', 'Spring Security', 'Spring Cloud',
                   'Reactive', 'Kafka', 'Kubernetes', 'JVM', 'GraphQL', 'Mockito',
                   'Testcontainers', 'JUnit', 'Docker', 'gRPC', 'Quarkus']:
            return tag

    return lesson.get('category', 'Core Java')

print("=" * 60)
print("REORGANIZING LESSONS BY FRAMEWORK")
print("=" * 60)

# Load lessons
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

print(f"\nCurrent: {len(py_lessons)} Python, {len(java_lessons)} Java lessons")

# Group Python lessons by framework
print("\n--- Grouping Python lessons by framework ---")
py_by_framework = defaultdict(list)
for lesson in py_lessons:
    framework = get_framework(lesson)
    py_by_framework[framework].append(lesson)

print("\nPython frameworks found:")
for framework in sorted(py_by_framework.keys()):
    count = len(py_by_framework[framework])
    print(f"  {framework}: {count} lessons")

# Group Java lessons by framework
print("\n--- Grouping Java lessons by framework ---")
java_by_framework = defaultdict(list)
for lesson in java_lessons:
    framework = get_java_framework(lesson)
    java_by_framework[framework].append(lesson)

print("\nJava frameworks found:")
for framework in sorted(java_by_framework.keys()):
    count = len(java_by_framework[framework])
    print(f"  {framework}: {count} lessons")

# Define difficulty order
difficulty_order = {'Beginner': 1, 'Intermediate': 2, 'Advanced': 3, 'Expert': 4}

# Sort lessons within each framework by difficulty
print("\n--- Sorting lessons within frameworks ---")
for framework in py_by_framework:
    py_by_framework[framework].sort(key=lambda x: difficulty_order.get(x.get('difficulty', 'Intermediate'), 2))

for framework in java_by_framework:
    java_by_framework[framework].sort(key=lambda x: difficulty_order.get(x.get('difficulty', 'Intermediate'), 2))

# Define framework order for Python (beginner -> advanced topics)
py_framework_order = [
    'Core Python',
    'Strings',
    'Collections',
    'Functions',
    'OOP',
    'Control Flow',
    'Algorithms',
    'Data Processing',
    'Flask',
    'Django',
    'FastAPI',
    'SQLAlchemy',
    'Database',
    'pandas',
    'NumPy',
    'scikit-learn',
    'Data Engineering',
    'pytest',
    'Celery',
    'asyncio',
    'Redis',
    'AWS boto3',
    'AWS',
    'Docker',
    'Concurrency',
    'Web Development',
    'Security',
    'Performance',
]

# Define framework order for Java
java_framework_order = [
    'Core Java',
    'Collections',
    'OOP',
    'Control Flow',
    'Algorithms',
    'JUnit',
    'Mockito',
    'Testcontainers',
    'Spring Boot',
    'Spring Data',
    'Spring Security',
    'Spring Cloud',
    'Reactive',
    'Kafka',
    'JVM',
    'GraphQL',
    'Docker',
    'gRPC',
    'Kubernetes',
    'Quarkus',
    'Database',
    'Web Development',
    'Security',
    'Performance',
]

# Reorganize Python lessons
print("\n--- Reorganizing Python lessons ---")
reorganized_py = []
next_id = 1

for framework in py_framework_order:
    if framework in py_by_framework:
        framework_lessons = py_by_framework[framework]
        print(f"  Adding {len(framework_lessons)} {framework} lessons (IDs {next_id}-{next_id + len(framework_lessons) - 1})")

        for lesson in framework_lessons:
            lesson['id'] = next_id
            reorganized_py.append(lesson)
            next_id += 1

# Add any remaining frameworks not in the order
for framework in sorted(py_by_framework.keys()):
    if framework not in py_framework_order:
        framework_lessons = py_by_framework[framework]
        print(f"  Adding {len(framework_lessons)} {framework} lessons (IDs {next_id}-{next_id + len(framework_lessons) - 1})")

        for lesson in framework_lessons:
            lesson['id'] = next_id
            reorganized_py.append(lesson)
            next_id += 1

# Reorganize Java lessons
print("\n--- Reorganizing Java lessons ---")
reorganized_java = []
next_id = 1

for framework in java_framework_order:
    if framework in java_by_framework:
        framework_lessons = java_by_framework[framework]
        print(f"  Adding {len(framework_lessons)} {framework} lessons (IDs {next_id}-{next_id + len(framework_lessons) - 1})")

        for lesson in framework_lessons:
            lesson['id'] = next_id
            reorganized_java.append(lesson)
            next_id += 1

# Add any remaining frameworks
for framework in sorted(java_by_framework.keys()):
    if framework not in java_framework_order:
        framework_lessons = java_by_framework[framework]
        print(f"  Adding {len(framework_lessons)} {framework} lessons (IDs {next_id}-{next_id + len(framework_lessons) - 1})")

        for lesson in framework_lessons:
            lesson['id'] = next_id
            reorganized_java.append(lesson)
            next_id += 1

print(f"\n--- Summary ---")
print(f"Python lessons reorganized: {len(reorganized_py)} lessons (was {len(py_lessons)})")
print(f"Java lessons reorganized: {len(reorganized_java)} lessons (was {len(java_lessons)})")

# Save reorganized lessons
print("\n--- Saving reorganized lessons ---")
save_lessons('public/lessons-python.json', reorganized_py)
save_lessons('public/lessons-java.json', reorganized_java)

print("\n" + "=" * 60)
print("LESSON REORGANIZATION COMPLETE!")
print("=" * 60)
print("\nLessons are now grouped by framework with sequential IDs")
print("Order: Beginner frameworks → Advanced frameworks")
print("Within each framework: Beginner → Intermediate → Advanced → Expert")
