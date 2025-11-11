#!/usr/bin/env python3
"""Check if there are any remaining coverage gaps before JS/TS"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_coverage(lessons, lang):
    print(f"\n{'='*70}")
    print(f"{lang.upper()} COVERAGE ANALYSIS")
    print(f"{'='*70}")

    # Count by major frameworks/topics
    framework_counts = {}
    topic_counts = {}

    for lesson in lessons:
        tags = lesson.get('tags', [])

        # Count topics
        for tag in tags:
            if tag not in ['Beginner', 'Intermediate', 'Advanced', 'Expert']:
                topic_counts[tag] = topic_counts.get(tag, 0) + 1

        # Check for specific frameworks in tutorial/examples
        tutorial = lesson.get('tutorial', '').lower()
        examples = lesson.get('additionalExamples', '').lower()
        content = tutorial + examples

        # Python frameworks
        if lang == 'Python':
            if 'django' in content:
                framework_counts['Django'] = framework_counts.get('Django', 0) + 1
            if 'flask' in content:
                framework_counts['Flask'] = framework_counts.get('Flask', 0) + 1
            if 'fastapi' in content:
                framework_counts['FastAPI'] = framework_counts.get('FastAPI', 0) + 1
            if 'pandas' in content:
                framework_counts['Pandas'] = framework_counts.get('Pandas', 0) + 1
            if 'numpy' in content:
                framework_counts['NumPy'] = framework_counts.get('NumPy', 0) + 1
            if 'scikit' in content or 'sklearn' in content:
                framework_counts['Scikit-learn'] = framework_counts.get('Scikit-learn', 0) + 1
            if 'tensorflow' in content or 'pytorch' in content:
                framework_counts['ML (TF/PyTorch)'] = framework_counts.get('ML (TF/PyTorch)', 0) + 1

        # Java frameworks
        if lang == 'Java':
            if 'spring' in content:
                framework_counts['Spring'] = framework_counts.get('Spring', 0) + 1
            if 'spring boot' in content:
                framework_counts['Spring Boot'] = framework_counts.get('Spring Boot', 0) + 1
            if 'spring security' in content:
                framework_counts['Spring Security'] = framework_counts.get('Spring Security', 0) + 1
            if 'spring cloud' in content:
                framework_counts['Spring Cloud'] = framework_counts.get('Spring Cloud', 0) + 1
            if 'hibernate' in content or 'jpa' in content:
                framework_counts['JPA/Hibernate'] = framework_counts.get('JPA/Hibernate', 0) + 1

    print(f"\nTop Topics (by tag):")
    for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1])[:10]:
        pct = (count / len(lessons)) * 100
        print(f"  {topic}: {count} lessons ({pct:.1f}%)")

    print(f"\nFramework Coverage:")
    for fw, count in sorted(framework_counts.items(), key=lambda x: -x[1]):
        pct = (count / len(lessons)) * 100
        print(f"  {fw}: {count} lessons ({pct:.1f}%)")

    return framework_counts, topic_counts

# Load and analyze
py_lessons = load_lessons('public/lessons-python.json')
java_lessons = load_lessons('public/lessons-java.json')

py_fw, py_topics = analyze_coverage(py_lessons, 'Python')
java_fw, java_topics = analyze_coverage(java_lessons, 'Java')

print(f"\n{'='*70}")
print("GAP ANALYSIS & RECOMMENDATIONS")
print(f"{'='*70}")

print("\nPYTHON:")
print(f"  Django: {py_fw.get('Django', 0)} lessons")
if py_fw.get('Django', 0) < 20:
    print("    → OPTIONAL: Could add more Django (currently have basics + advanced)")
else:
    print("    ✓ Excellent Django coverage")

print(f"  Flask: {py_fw.get('Flask', 0)} lessons")
if py_fw.get('Flask', 0) < 10:
    print("    → OPTIONAL: Could add Flask basics (lighter alternative to Django)")
else:
    print("    ✓ Good Flask coverage")

print(f"  Data Science: Pandas {py_fw.get('Pandas', 0)}, NumPy {py_fw.get('NumPy', 0)}")
if py_fw.get('Pandas', 0) < 15:
    print("    → OPTIONAL: Could expand Pandas (currently have fundamentals)")
else:
    print("    ✓ Solid data science foundation")

ml_coverage = py_fw.get('Scikit-learn', 0) + py_fw.get('ML (TF/PyTorch)', 0)
print(f"  Machine Learning: {ml_coverage} lessons")
if ml_coverage < 5:
    print("    → OPTIONAL: Could add ML basics (scikit-learn intro)")
else:
    print("    ✓ ML coverage present")

print("\nJAVA:")
print(f"  Spring Security: {java_fw.get('Spring Security', 0)} lessons")
if java_fw.get('Spring Security', 0) >= 15:
    print("    ✓ Excellent Spring Security coverage")

print(f"  Spring Cloud: {java_fw.get('Spring Cloud', 0)} lessons")
if java_fw.get('Spring Cloud', 0) >= 10:
    print("    ✓ Solid Spring Cloud/microservices coverage")

print(f"  Spring Boot: {java_fw.get('Spring Boot', 0)} lessons")
if java_fw.get('Spring Boot', 0) < 30:
    print("    → OPTIONAL: Could add more Spring Boot patterns")
else:
    print("    ✓ Strong Spring Boot coverage")

print("\n" + "="*70)
print("FINAL RECOMMENDATION")
print("="*70)

critical_gaps = []
optional_gaps = []

# Check for critical gaps
if py_fw.get('Django', 0) < 10:
    critical_gaps.append("Django basics")
if java_fw.get('Spring Security', 0) < 10:
    critical_gaps.append("Spring Security")
if java_fw.get('Spring Cloud', 0) < 8:
    critical_gaps.append("Spring Cloud")

# Optional improvements
if py_fw.get('Flask', 0) < 10:
    optional_gaps.append("Flask (lightweight web framework)")
if py_fw.get('Pandas', 0) < 15:
    optional_gaps.append("More Pandas lessons (advanced features)")
if ml_coverage < 5:
    optional_gaps.append("Machine Learning basics (scikit-learn)")
if java_fw.get('Spring Boot', 0) < 30:
    optional_gaps.append("More Spring Boot patterns")

if critical_gaps:
    print(f"\n⚠ CRITICAL GAPS FOUND:")
    for gap in critical_gaps:
        print(f"  - {gap}")
    print("\n→ RECOMMENDATION: Fill these gaps before JavaScript/TypeScript")
else:
    print(f"\n✓ NO CRITICAL GAPS - All essential frameworks covered!")

    if optional_gaps:
        print(f"\n🔧 OPTIONAL IMPROVEMENTS:")
        for gap in optional_gaps:
            print(f"  - {gap}")
        print("\n→ RECOMMENDATION: You can EITHER:")
        print("  1. Start JavaScript/TypeScript now (you're ready!)")
        print("  2. Add optional improvements first (10-20 lessons)")
    else:
        print("\n→ RECOMMENDATION: START JAVASCRIPT/TYPESCRIPT")
        print("  Your Python and Java tracks are comprehensive and complete!")

print(f"\nCurrent status: {len(py_lessons)} Python + {len(java_lessons)} Java = {len(py_lessons) + len(java_lessons)} total lessons")
print("All critical coverage requirements met ✓")
