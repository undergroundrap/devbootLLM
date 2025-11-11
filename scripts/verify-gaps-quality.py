#!/usr/bin/env python3
"""Verify gap-filling lesson quality and organization"""

import json
import random

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

print('='*60)
print('VERIFYING GAP-FILLING LESSONS QUALITY')
print('='*60)

# Load lessons
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

print(f'\nTotal: {len(py_lessons)} Python, {len(java_lessons)} Java')

# ============================================================
# PYTHON QUALITY CHECK
# ============================================================

print('\n--- Python Quality Analysis ---')

# Original lessons (first 725)
original = [l for l in py_lessons if l['id'] <= 725]
sample_original = random.sample(original, min(20, len(original)))

orig_tutorial_avg = sum(len(l.get('tutorial', '')) for l in sample_original) / len(sample_original)
orig_examples_avg = sum(len(l.get('additionalExamples', '')) for l in sample_original) / len(sample_original)

print(f'\nOriginal lessons (sample of {len(sample_original)}):')
print(f'  Avg tutorial: {orig_tutorial_avg:.0f} chars')
print(f'  Avg examples: {orig_examples_avg:.0f} chars')

# Phase 2 lessons (enhanced)
phase2 = [l for l in py_lessons if 637 <= l['id'] <= 686]  # Flask, Django, FastAPI, SQLAlchemy sections
if phase2:
    phase2_tutorial_avg = sum(len(l.get('tutorial', '')) for l in phase2) / len(phase2)
    phase2_examples_avg = sum(len(l.get('additionalExamples', '')) for l in phase2) / len(phase2)

    print(f'\nPhase 2 lessons ({len(phase2)} lessons):')
    print(f'  Avg tutorial: {phase2_tutorial_avg:.0f} chars')
    print(f'  Avg examples: {phase2_examples_avg:.0f} chars')

# Gap-filling lessons
numpy_gaps = [l for l in py_lessons if 'NumPy' in l['title'] and l['id'] >= 719]
redis_gaps = [l for l in py_lessons if 'Redis' in l['title'] and l['id'] >= 800]
docker_gaps = [l for l in py_lessons if 'Docker' in l['title'] and l['id'] >= 839]
asyncio_gaps = [l for l in py_lessons if 'asyncio' in l['title'] and l['id'] >= 787]
data_eng_gaps = [l for l in py_lessons if 'Data Engineering' in l['title'] and l['id'] >= 856]

print(f'\nGap-filling lessons:')

if numpy_gaps:
    numpy_tutorial_avg = sum(len(l.get('tutorial', '')) for l in numpy_gaps) / len(numpy_gaps)
    numpy_examples_avg = sum(len(l.get('additionalExamples', '')) for l in numpy_gaps) / len(numpy_gaps)
    print(f'\n  NumPy Advanced ({len(numpy_gaps)} lessons):')
    print(f'    Avg tutorial: {numpy_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {numpy_examples_avg:.0f} chars')
    print(f'    Sample titles:')
    for l in numpy_gaps[:3]:
        print(f'      ID {l["id"]}: {l["title"]}')

if redis_gaps:
    redis_tutorial_avg = sum(len(l.get('tutorial', '')) for l in redis_gaps) / len(redis_gaps)
    redis_examples_avg = sum(len(l.get('additionalExamples', '')) for l in redis_gaps) / len(redis_gaps)
    print(f'\n  Redis ({len(redis_gaps)} lessons):')
    print(f'    Avg tutorial: {redis_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {redis_examples_avg:.0f} chars')
    print(f'    Sample titles:')
    for l in redis_gaps[:3]:
        print(f'      ID {l["id"]}: {l["title"]}')

if docker_gaps:
    docker_tutorial_avg = sum(len(l.get('tutorial', '')) for l in docker_gaps) / len(docker_gaps)
    docker_examples_avg = sum(len(l.get('additionalExamples', '')) for l in docker_gaps) / len(docker_gaps)
    print(f'\n  Docker ({len(docker_gaps)} lessons):')
    print(f'    Avg tutorial: {docker_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {docker_examples_avg:.0f} chars')

if asyncio_gaps:
    asyncio_tutorial_avg = sum(len(l.get('tutorial', '')) for l in asyncio_gaps) / len(asyncio_gaps)
    asyncio_examples_avg = sum(len(l.get('additionalExamples', '')) for l in asyncio_gaps) / len(asyncio_gaps)
    print(f'\n  asyncio Advanced ({len(asyncio_gaps)} lessons):')
    print(f'    Avg tutorial: {asyncio_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {asyncio_examples_avg:.0f} chars')

if data_eng_gaps:
    de_tutorial_avg = sum(len(l.get('tutorial', '')) for l in data_eng_gaps) / len(data_eng_gaps)
    de_examples_avg = sum(len(l.get('additionalExamples', '')) for l in data_eng_gaps) / len(data_eng_gaps)
    print(f'\n  Data Engineering ({len(data_eng_gaps)} lessons):')
    print(f'    Avg tutorial: {de_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {de_examples_avg:.0f} chars')

# ============================================================
# JAVA QUALITY CHECK
# ============================================================

print('\n\n--- Java Quality Analysis ---')

# Original Java lessons
java_original = [l for l in java_lessons if l['id'] <= 725]
sample_java_original = random.sample(java_original, min(20, len(java_original)))

java_orig_tutorial_avg = sum(len(l.get('tutorial', '')) for l in sample_java_original) / len(sample_java_original)
java_orig_examples_avg = sum(len(l.get('additionalExamples', '')) for l in sample_java_original) / len(sample_java_original)

print(f'\nOriginal lessons (sample of {len(sample_java_original)}):')
print(f'  Avg tutorial: {java_orig_tutorial_avg:.0f} chars')
print(f'  Avg examples: {java_orig_examples_avg:.0f} chars')

# Gap-filling lessons
mockito_gaps = [l for l in java_lessons if 'Mockito' in l['title'] and l['id'] >= 696]
tc_gaps = [l for l in java_lessons if 'Testcontainers' in l['title'] and l['id'] >= 707]
security_gaps = [l for l in java_lessons if 'Spring Security' in l['title'] and l['id'] >= 746]
docker_java_gaps = [l for l in java_lessons if 'Docker' in l['title'] and l['id'] >= 827]
grpc_gaps = [l for l in java_lessons if 'gRPC' in l['title'] and l['id'] >= 844]
quarkus_gaps = [l for l in java_lessons if 'Quarkus' in l['title'] and l['id'] >= 870]

print(f'\nGap-filling lessons:')

if mockito_gaps:
    mockito_tutorial_avg = sum(len(l.get('tutorial', '')) for l in mockito_gaps) / len(mockito_gaps)
    mockito_examples_avg = sum(len(l.get('additionalExamples', '')) for l in mockito_gaps) / len(mockito_gaps)
    print(f'\n  Mockito Advanced ({len(mockito_gaps)} lessons):')
    print(f'    Avg tutorial: {mockito_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {mockito_examples_avg:.0f} chars')
    print(f'    Sample titles:')
    for l in mockito_gaps[:3]:
        print(f'      ID {l["id"]}: {l["title"]}')

if tc_gaps:
    tc_tutorial_avg = sum(len(l.get('tutorial', '')) for l in tc_gaps) / len(tc_gaps)
    tc_examples_avg = sum(len(l.get('additionalExamples', '')) for l in tc_gaps) / len(tc_gaps)
    print(f'\n  Testcontainers ({len(tc_gaps)} lessons):')
    print(f'    Avg tutorial: {tc_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {tc_examples_avg:.0f} chars')
    print(f'    Sample titles:')
    for l in tc_gaps[:3]:
        print(f'      ID {l["id"]}: {l["title"]}')

if security_gaps:
    security_tutorial_avg = sum(len(l.get('tutorial', '')) for l in security_gaps) / len(security_gaps)
    security_examples_avg = sum(len(l.get('additionalExamples', '')) for l in security_gaps) / len(security_gaps)
    print(f'\n  Spring Security Advanced ({len(security_gaps)} lessons):')
    print(f'    Avg tutorial: {security_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {security_examples_avg:.0f} chars')

if grpc_gaps:
    grpc_tutorial_avg = sum(len(l.get('tutorial', '')) for l in grpc_gaps) / len(grpc_gaps)
    grpc_examples_avg = sum(len(l.get('additionalExamples', '')) for l in grpc_gaps) / len(grpc_gaps)
    print(f'\n  gRPC ({len(grpc_gaps)} lessons):')
    print(f'    Avg tutorial: {grpc_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {grpc_examples_avg:.0f} chars')

if quarkus_gaps:
    quarkus_tutorial_avg = sum(len(l.get('tutorial', '')) for l in quarkus_gaps) / len(quarkus_gaps)
    quarkus_examples_avg = sum(len(l.get('additionalExamples', '')) for l in quarkus_gaps) / len(quarkus_gaps)
    print(f'\n  Quarkus ({len(quarkus_gaps)} lessons):')
    print(f'    Avg tutorial: {quarkus_tutorial_avg:.0f} chars')
    print(f'    Avg examples: {quarkus_examples_avg:.0f} chars')

# ============================================================
# ORGANIZATION CHECK
# ============================================================

print('\n\n--- Organization Verification ---')

# Check Python organization
print('\nPython frameworks (in order):')
current_framework = None
framework_count = 0
for lesson in py_lessons:
    # Determine framework from title
    title = lesson['title']
    if 'Flask' in title:
        framework = 'Flask'
    elif 'Django' in title:
        framework = 'Django'
    elif 'FastAPI' in title:
        framework = 'FastAPI'
    elif 'SQLAlchemy' in title:
        framework = 'SQLAlchemy'
    elif 'pandas' in title:
        framework = 'pandas'
    elif 'NumPy' in title:
        framework = 'NumPy'
    elif 'Redis' in title:
        framework = 'Redis'
    elif 'Docker' in title:
        framework = 'Docker'
    elif 'asyncio' in title:
        framework = 'asyncio'
    elif 'Data Engineering' in title or 'Airflow' in title:
        framework = 'Data Engineering'
    else:
        continue  # Skip core Python lessons

    if framework != current_framework:
        if current_framework and framework_count > 0:
            print(f'  {current_framework}: {framework_count} lessons')
        current_framework = framework
        framework_count = 1
    else:
        framework_count += 1

if current_framework:
    print(f'  {current_framework}: {framework_count} lessons')

# Check Java organization
print('\nJava frameworks (in order):')
current_framework = None
framework_count = 0
for lesson in java_lessons:
    title = lesson['title']
    if 'Mockito' in title:
        framework = 'Mockito'
    elif 'Testcontainers' in title:
        framework = 'Testcontainers'
    elif 'Spring Security' in title:
        framework = 'Spring Security'
    elif 'Docker' in title:
        framework = 'Docker'
    elif 'gRPC' in title:
        framework = 'gRPC'
    elif 'Quarkus' in title:
        framework = 'Quarkus'
    else:
        continue

    if framework != current_framework:
        if current_framework and framework_count > 0:
            print(f'  {current_framework}: {framework_count} lessons')
        current_framework = framework
        framework_count = 1
    else:
        framework_count += 1

if current_framework:
    print(f'  {current_framework}: {framework_count} lessons')

# ============================================================
# QUALITY VERDICT
# ============================================================

print('\n\n' + '='*60)
print('QUALITY VERDICT')
print('='*60)

# Calculate overall gap-filling quality
all_py_gaps = numpy_gaps + redis_gaps + docker_gaps + asyncio_gaps + data_eng_gaps
all_java_gaps = mockito_gaps + tc_gaps + security_gaps + docker_java_gaps + grpc_gaps + quarkus_gaps

if all_py_gaps:
    py_gaps_tutorial_avg = sum(len(l.get('tutorial', '')) for l in all_py_gaps) / len(all_py_gaps)
    py_gaps_examples_avg = sum(len(l.get('additionalExamples', '')) for l in all_py_gaps) / len(all_py_gaps)
else:
    py_gaps_tutorial_avg = 0
    py_gaps_examples_avg = 0

if all_java_gaps:
    java_gaps_tutorial_avg = sum(len(l.get('tutorial', '')) for l in all_java_gaps) / len(all_java_gaps)
    java_gaps_examples_avg = sum(len(l.get('additionalExamples', '')) for l in all_java_gaps) / len(all_java_gaps)
else:
    java_gaps_tutorial_avg = 0
    java_gaps_examples_avg = 0

print(f'\nPython:')
print(f'  Original avg: {orig_tutorial_avg:.0f} tutorial, {orig_examples_avg:.0f} examples')
print(f'  Gap-filling avg: {py_gaps_tutorial_avg:.0f} tutorial, {py_gaps_examples_avg:.0f} examples')
print(f'  Quality: {"PASS" if py_gaps_tutorial_avg >= 4000 and py_gaps_examples_avg >= 4000 else "FAIL"}')

print(f'\nJava:')
print(f'  Original avg: {java_orig_tutorial_avg:.0f} tutorial, {java_orig_examples_avg:.0f} examples')
print(f'  Gap-filling avg: {java_gaps_tutorial_avg:.0f} tutorial, {java_gaps_examples_avg:.0f} examples')
print(f'  Quality: {"PASS" if java_gaps_tutorial_avg >= 4000 and java_gaps_examples_avg >= 4000 else "FAIL"}')

# Check if any lessons are too short
print('\n--- Quality Issues ---')
issues_found = False

for lesson in all_py_gaps:
    tutorial_len = len(lesson.get('tutorial', ''))
    examples_len = len(lesson.get('additionalExamples', ''))
    if tutorial_len < 4000 or examples_len < 4000:
        if not issues_found:
            print('\nPython lessons below 4000 char threshold:')
            issues_found = True
        print(f'  ID {lesson["id"]}: {lesson["title"]}')
        print(f'    Tutorial: {tutorial_len} chars, Examples: {examples_len} chars')

issues_found_java = False
for lesson in all_java_gaps:
    tutorial_len = len(lesson.get('tutorial', ''))
    examples_len = len(lesson.get('additionalExamples', ''))
    if tutorial_len < 4000 or examples_len < 4000:
        if not issues_found_java:
            print('\nJava lessons below 4000 char threshold:')
            issues_found_java = True
        print(f'  ID {lesson["id"]}: {lesson["title"]}')
        print(f'    Tutorial: {tutorial_len} chars, Examples: {examples_len} chars')

if not issues_found and not issues_found_java:
    print('\nNo quality issues found - all gap-filling lessons meet standards!')

print('\n' + '='*60)
print('VERIFICATION COMPLETE')
print('='*60)
