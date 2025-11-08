#!/usr/bin/env python3
import json

# Load lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_lessons = json.load(f)

# All enhanced frameworks
enhanced_frameworks = {
    'boto3', 'flask', 'fastapi', 'aiohttp', 'asyncpg', 'sqlalchemy', 'psycopg2',
    'redis', 'bcrypt', 'jwt', 'cryptography', 'pandas', 'numpy', 'kafka', 'pika',
    'prometheus_client', 'requests', 'bs4', 'selenium', 'pydantic', 'click',
    'dotenv', 'dateutil', 'zoneinfo', 'pathlib', 'itertools', 're.compile',
    'traceback', 'from collections import', 'from functools import',
    'from contextlib import', 'contextmanager', 'string.Template', 'textwrap',
    'class BankAccount', 'class Vehicle', 'from dataclasses import',
    'class DataManager', 'class DataItem', '@dataclass', 'from abc import ABC'
}

remaining = []
for lesson in python_lessons:
    examples = lesson.get('additionalExamples', '')
    if not examples:
        continue

    has_framework = any(fw in examples.lower() for fw in enhanced_frameworks)
    if not has_framework:
        remaining.append({
            'id': lesson['id'],
            'title': lesson['title'],
            'difficulty': lesson.get('difficulty', 'unknown'),
            'tags': lesson.get('tags', []),
            'ex_len': len(examples)
        })

print(f"Remaining: {len(remaining)}/700")
print(f"Current coverage: {(700-len(remaining))/700*100:.1f}%")

# Find patterns in remaining
import re

# Check for common keywords
keywords = {}
for lesson in remaining:
    title = lesson['title'].lower()

    # Extract potential keywords
    for word in title.split():
        if len(word) > 3 and word not in ['with', 'from', 'that', 'this']:
            keywords[word] = keywords.get(word, 0) + 1

print("\nMost common keywords in remaining lessons:")
sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_keywords[:15]:
    print(f"  {word:20s}: {count}")

# Show high-value lessons (longer examples, easier to enhance)
print("\n" + "="*80)
print("HIGH-VALUE LESSONS TO ENHANCE (sorted by example length):")
print("="*80)

sorted_remaining = sorted(remaining, key=lambda x: x['ex_len'], reverse=True)
for lesson in sorted_remaining[:30]:
    print(f"{lesson['id']:3d}: {lesson['title'][:60]:60s} ({lesson['ex_len']:4d} chars)")
