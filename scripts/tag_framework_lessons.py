"""
Tag framework lessons so they can be handled with mock compilation.
"""

import json

def tag_framework_lessons():
    """Add isFramework flag to lessons that need external dependencies."""

    framework_keywords = {
        'python': ['flask', 'django', 'fastapi', 'sqlalchemy', 'boto3', 'kafka',
                   'redis', 'celery', 'sklearn', 'tensorflow', 'pandas', 'numpy'],
        'java': ['spring', 'hibernate', 'jpa', 'kafka', 'kubernetes', 'graphql',
                 'grpc', 'reactor', 'webflux']
    }

    print("=" * 80)
    print("TAGGING FRAMEWORK LESSONS FOR MOCK COMPILATION")
    print("=" * 80)
    print()

    # Tag Python lessons
    print("[PROCESSING PYTHON LESSONS]")
    print("-" * 80)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        py_data = json.load(f)

    py_tagged = 0
    for lesson in py_data:
        solution = lesson.get('fullSolution', '')
        title = lesson.get('title', '').lower()

        # Check if it's a framework lesson
        is_framework = False
        detected_framework = None

        for fw in framework_keywords['python']:
            if fw in solution.lower() or fw in title:
                is_framework = True
                detected_framework = fw
                break

        if is_framework:
            lesson['isFramework'] = True
            lesson['frameworkName'] = detected_framework.title()
            py_tagged += 1

            if py_tagged <= 10:
                print(f"  Tagged lesson {lesson['id']}: {lesson['title'][:50]} ({detected_framework})")
        else:
            # Explicitly mark as non-framework for clarity
            lesson['isFramework'] = False

    print(f"Tagged {py_tagged} Python framework lessons")
    print()

    # Tag Java lessons
    print("[PROCESSING JAVA LESSONS]")
    print("-" * 80)

    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    java_tagged = 0
    for lesson in java_data:
        solution = lesson.get('fullSolution', '')
        title = lesson.get('title', '').lower()

        # Check if it's a framework lesson
        is_framework = False
        detected_framework = None

        for fw in framework_keywords['java']:
            if fw in solution.lower() or fw in title:
                is_framework = True
                detected_framework = fw
                break

        if is_framework:
            lesson['isFramework'] = True
            lesson['frameworkName'] = detected_framework.title()
            java_tagged += 1

            if java_tagged <= 10:
                print(f"  Tagged lesson {lesson['id']}: {lesson['title'][:50]} ({detected_framework})")
        else:
            lesson['isFramework'] = False

    print(f"Tagged {java_tagged} Java framework lessons")
    print()

    # Save changes
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(py_data, f, indent=2, ensure_ascii=False)

    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_data, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Python framework lessons tagged: {py_tagged}")
    print(f"Java framework lessons tagged:   {java_tagged}")
    print(f"Total framework lessons:         {py_tagged + java_tagged}")
    print()
    print("[SUCCESS] All lessons tagged with isFramework flag")
    print("Framework lessons will use syntax-only validation")
    print("=" * 80)

if __name__ == '__main__':
    tag_framework_lessons()
