#!/usr/bin/env python3
"""Fix Phase 2 lesson tags to match original lesson style"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

# Enhanced tag mappings for Phase 2 lessons
python_tag_fixes = {
    # Flask Advanced (783-792)
    783: {'tags': ['Flask', 'Web/APIs', 'Architecture', 'Expert'], 'difficulty': 'Expert'},
    784: {'tags': ['Flask', 'Web/APIs', 'Design Patterns', 'Expert'], 'difficulty': 'Expert'},
    785: {'tags': ['Flask', 'Database', 'ORM', 'Advanced'], 'difficulty': 'Advanced'},
    786: {'tags': ['Flask', 'Web/APIs', 'Error Handling', 'Advanced'], 'difficulty': 'Advanced'},
    787: {'tags': ['Flask', 'Web/APIs', 'Middleware', 'Advanced'], 'difficulty': 'Advanced'},
    788: {'tags': ['Flask', 'Security', 'Authentication', 'Expert'], 'difficulty': 'Expert'},
    789: {'tags': ['Flask', 'Database', 'Migrations', 'Advanced'], 'difficulty': 'Advanced'},
    790: {'tags': ['Flask', 'Performance', 'Caching', 'Advanced'], 'difficulty': 'Advanced'},
    791: {'tags': ['Flask', 'Web/APIs', 'CORS', 'Advanced'], 'difficulty': 'Advanced'},
    792: {'tags': ['Flask', 'Deployment', 'Production', 'Expert'], 'difficulty': 'Expert'},

    # SQLAlchemy Advanced (793-802)
    793: {'tags': ['SQLAlchemy', 'Database', 'ORM', 'Advanced'], 'difficulty': 'Advanced'},
    794: {'tags': ['SQLAlchemy', 'Database', 'Performance', 'Expert'], 'difficulty': 'Expert'},
    795: {'tags': ['SQLAlchemy', 'Database', 'Query Optimization', 'Expert'], 'difficulty': 'Expert'},
    796: {'tags': ['SQLAlchemy', 'Database', 'OOP', 'Advanced'], 'difficulty': 'Advanced'},
    797: {'tags': ['SQLAlchemy', 'Database', 'Events', 'Advanced'], 'difficulty': 'Advanced'},
    798: {'tags': ['SQLAlchemy', 'Database', 'ORM', 'Advanced'], 'difficulty': 'Advanced'},
    799: {'tags': ['SQLAlchemy', 'Database', 'Relationships', 'Advanced'], 'difficulty': 'Advanced'},
    800: {'tags': ['SQLAlchemy', 'Database', 'OOP', 'Expert'], 'difficulty': 'Expert'},
    801: {'tags': ['SQLAlchemy', 'Database', 'Performance', 'Expert'], 'difficulty': 'Expert'},
    802: {'tags': ['SQLAlchemy', 'Database', 'Migrations', 'Advanced'], 'difficulty': 'Advanced'},

    # AWS boto3 (803-812)
    803: {'tags': ['AWS', 'Cloud', 'Storage', 'Expert'], 'difficulty': 'Expert'},
    804: {'tags': ['AWS', 'Cloud', 'Compute', 'Expert'], 'difficulty': 'Expert'},
    805: {'tags': ['AWS', 'Cloud', 'Serverless', 'Expert'], 'difficulty': 'Expert'},
    806: {'tags': ['AWS', 'Database', 'NoSQL', 'Expert'], 'difficulty': 'Expert'},
    807: {'tags': ['AWS', 'Cloud', 'Messaging', 'Expert'], 'difficulty': 'Expert'},
    808: {'tags': ['AWS', 'Cloud', 'Messaging', 'Expert'], 'difficulty': 'Expert'},
    809: {'tags': ['AWS', 'Cloud', 'Monitoring', 'Expert'], 'difficulty': 'Expert'},
    810: {'tags': ['AWS', 'Security', 'IAM', 'Expert'], 'difficulty': 'Expert'},
    811: {'tags': ['AWS', 'Database', 'RDS', 'Expert'], 'difficulty': 'Expert'},
    812: {'tags': ['AWS', 'Cloud', 'Infrastructure as Code', 'Expert'], 'difficulty': 'Expert'},

    # FastAPI Advanced (813-821)
    813: {'tags': ['FastAPI', 'Web/APIs', 'Design Patterns', 'Expert'], 'difficulty': 'Expert'},
    814: {'tags': ['FastAPI', 'Async', 'Background Tasks', 'Expert'], 'difficulty': 'Expert'},
    815: {'tags': ['FastAPI', 'WebSocket', 'Real-time', 'Expert'], 'difficulty': 'Expert'},
    816: {'tags': ['FastAPI', 'Security', 'Authentication', 'Expert'], 'difficulty': 'Expert'},
    817: {'tags': ['FastAPI', 'Web/APIs', 'Versioning', 'Advanced'], 'difficulty': 'Advanced'},
    818: {'tags': ['FastAPI', 'Database', 'Async', 'Expert'], 'difficulty': 'Expert'},
    819: {'tags': ['FastAPI', 'Testing', 'Async', 'Advanced'], 'difficulty': 'Advanced'},
    820: {'tags': ['FastAPI', 'Web/APIs', 'Documentation', 'Advanced'], 'difficulty': 'Advanced'},
    821: {'tags': ['FastAPI', 'Deployment', 'Production', 'Expert'], 'difficulty': 'Expert'},
}

java_tag_fixes = {
    # Spring Data Advanced (786-797)
    786: {'tags': ['Spring Data', 'Database', 'JPA', 'Expert'], 'difficulty': 'Expert'},
    787: {'tags': ['Spring Data', 'Database', 'Query Building', 'Expert'], 'difficulty': 'Expert'},
    788: {'tags': ['Spring Data', 'Database', 'JPA', 'Advanced'], 'difficulty': 'Advanced'},
    789: {'tags': ['Spring Data', 'Database', 'Performance', 'Advanced'], 'difficulty': 'Advanced'},
    790: {'tags': ['Spring Data', 'Database', 'Auditing', 'Advanced'], 'difficulty': 'Advanced'},
    791: {'tags': ['Spring Data', 'Database', 'Multi-tenancy', 'Expert'], 'difficulty': 'Expert'},
    792: {'tags': ['Spring Data', 'Database', 'Stored Procedures', 'Advanced'], 'difficulty': 'Advanced'},
    793: {'tags': ['Spring Data', 'Database', 'Custom Implementation', 'Expert'], 'difficulty': 'Expert'},
    794: {'tags': ['Spring Data', 'Database', 'Performance', 'Expert'], 'difficulty': 'Expert'},
    795: {'tags': ['Spring Data', 'Database', 'Caching', 'Advanced'], 'difficulty': 'Advanced'},
    796: {'tags': ['Spring Data', 'Database', 'Transactions', 'Expert'], 'difficulty': 'Expert'},
    797: {'tags': ['Spring Data', 'Database', 'Performance', 'Expert'], 'difficulty': 'Expert'},

    # Kubernetes (798-807)
    798: {'tags': ['Kubernetes', 'DevOps', 'Containers', 'Advanced'], 'difficulty': 'Advanced'},
    799: {'tags': ['Kubernetes', 'DevOps', 'Networking', 'Advanced'], 'difficulty': 'Advanced'},
    800: {'tags': ['Kubernetes', 'DevOps', 'Configuration', 'Advanced'], 'difficulty': 'Advanced'},
    801: {'tags': ['Kubernetes', 'DevOps', 'Storage', 'Advanced'], 'difficulty': 'Advanced'},
    802: {'tags': ['Kubernetes', 'DevOps', 'Deployment', 'Advanced'], 'difficulty': 'Advanced'},
    803: {'tags': ['Kubernetes', 'DevOps', 'StatefulSets', 'Expert'], 'difficulty': 'Expert'},
    804: {'tags': ['Kubernetes', 'DevOps', 'Ingress', 'Advanced'], 'difficulty': 'Advanced'},
    805: {'tags': ['Kubernetes', 'DevOps', 'Monitoring', 'Advanced'], 'difficulty': 'Advanced'},
    806: {'tags': ['Kubernetes', 'DevOps', 'Resource Management', 'Advanced'], 'difficulty': 'Advanced'},
    807: {'tags': ['Kubernetes', 'DevOps', 'Production', 'Expert'], 'difficulty': 'Expert'},

    # JVM Performance (808-817)
    808: {'tags': ['JVM', 'Performance', 'Architecture', 'Expert'], 'difficulty': 'Expert'},
    809: {'tags': ['JVM', 'Performance', 'GC Tuning', 'Expert'], 'difficulty': 'Expert'},
    810: {'tags': ['JVM', 'Performance', 'Memory', 'Expert'], 'difficulty': 'Expert'},
    811: {'tags': ['JVM', 'Performance', 'Compilation', 'Expert'], 'difficulty': 'Expert'},
    812: {'tags': ['JVM', 'Performance', 'Debugging', 'Advanced'], 'difficulty': 'Advanced'},
    813: {'tags': ['JVM', 'Performance', 'Debugging', 'Expert'], 'difficulty': 'Expert'},
    814: {'tags': ['JVM', 'Performance', 'Profiling', 'Expert'], 'difficulty': 'Expert'},
    815: {'tags': ['JVM', 'Performance', 'Monitoring', 'Advanced'], 'difficulty': 'Advanced'},
    816: {'tags': ['JVM', 'Performance', 'GC Algorithms', 'Expert'], 'difficulty': 'Expert'},
    817: {'tags': ['JVM', 'Performance', 'Production', 'Expert'], 'difficulty': 'Expert'},

    # GraphQL Java (818-827)
    818: {'tags': ['GraphQL', 'Web/APIs', 'API Design', 'Advanced'], 'difficulty': 'Advanced'},
    819: {'tags': ['GraphQL', 'Web/APIs', 'Configuration', 'Advanced'], 'difficulty': 'Advanced'},
    820: {'tags': ['GraphQL', 'Web/APIs', 'Schema', 'Advanced'], 'difficulty': 'Advanced'},
    821: {'tags': ['GraphQL', 'Web/APIs', 'Resolvers', 'Advanced'], 'difficulty': 'Advanced'},
    822: {'tags': ['GraphQL', 'Web/APIs', 'Mutations', 'Advanced'], 'difficulty': 'Advanced'},
    823: {'tags': ['GraphQL', 'Web/APIs', 'Real-time', 'Expert'], 'difficulty': 'Expert'},
    824: {'tags': ['GraphQL', 'Web/APIs', 'Performance', 'Expert'], 'difficulty': 'Expert'},
    825: {'tags': ['GraphQL', 'Web/APIs', 'Error Handling', 'Advanced'], 'difficulty': 'Advanced'},
    826: {'tags': ['GraphQL', 'Security', 'Authentication', 'Expert'], 'difficulty': 'Expert'},
    827: {'tags': ['GraphQL', 'Web/APIs', 'Production', 'Expert'], 'difficulty': 'Expert'},
}

print("=" * 60)
print("FIXING PHASE 2 LESSON TAGS")
print("=" * 60)

# Load Python lessons
print("\nLoading Python lessons...")
py_lessons = load_lessons('public/lessons-python.json')
print(f"Current: {len(py_lessons)} lessons")

# Fix Python tags
print("\nFixing Python Phase 2 tags (IDs 783-821)...")
fixed_count = 0
for lesson in py_lessons:
    if lesson['id'] in python_tag_fixes:
        old_tags = lesson['tags'].copy()
        old_diff = lesson['difficulty']

        lesson['tags'] = python_tag_fixes[lesson['id']]['tags']
        lesson['difficulty'] = python_tag_fixes[lesson['id']]['difficulty']

        fixed_count += 1
        if fixed_count <= 5:  # Show first 5 as examples
            print(f"  ID {lesson['id']}: {lesson['title']}")
            print(f"    Tags: {old_tags} -> {lesson['tags']}")
            print(f"    Difficulty: {old_diff} -> {lesson['difficulty']}")

print(f"[OK] Fixed {fixed_count} Python lessons")

# Save Python lessons
save_lessons('public/lessons-python.json', py_lessons)
print("[OK] Saved Python lessons")

# Load Java lessons
print("\nLoading Java lessons...")
java_lessons = load_lessons('public/lessons-java.json')
print(f"Current: {len(java_lessons)} lessons")

# Fix Java tags
print("\nFixing Java Phase 2 tags (IDs 786-827)...")
fixed_count = 0
for lesson in java_lessons:
    if lesson['id'] in java_tag_fixes:
        old_tags = lesson['tags'].copy()
        old_diff = lesson['difficulty']

        lesson['tags'] = java_tag_fixes[lesson['id']]['tags']
        lesson['difficulty'] = java_tag_fixes[lesson['id']]['difficulty']

        fixed_count += 1
        if fixed_count <= 5:  # Show first 5 as examples
            print(f"  ID {lesson['id']}: {lesson['title']}")
            print(f"    Tags: {old_tags} -> {lesson['tags']}")
            print(f"    Difficulty: {old_diff} -> {lesson['difficulty']}")

print(f"[OK] Fixed {fixed_count} Java lessons")

# Save Java lessons
save_lessons('public/lessons-java.json', java_lessons)
print("[OK] Saved Java lessons")

print("\n" + "=" * 60)
print("PHASE 2 TAG FIXES COMPLETE!")
print("=" * 60)
print(f"Total lessons fixed: {39 + 42} (39 Python + 42 Java)")
print("Tags now match original lesson style with proper categorization")
