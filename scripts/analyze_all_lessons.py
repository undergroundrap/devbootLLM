import json
import re

def analyze_tutorials(lessons):
    """Analyze tutorial completeness and quality"""

    issues = {
        'missing_tutorial': [],
        'too_short': [],
        'missing_overview': [],
        'missing_key_concepts': [],
        'missing_examples': [],
        'missing_best_practices': [],
        'missing_pitfalls': [],
        'missing_real_world': []
    }

    section_patterns = {
        'overview': r'<h4[^>]*>.*?(overview|introduction)',
        'key_concepts': r'<h4[^>]*>.*?key concepts?',
        'examples': r'<h4[^>]*>.*?(code examples?|examples?|implementation)',
        'best_practices': r'<h4[^>]*>.*?best practices?',
        'pitfalls': r'<h4[^>]*>.*?(common pitfalls?|pitfalls?|mistakes)',
        'real_world': r'<h4[^>]*>.*?(real.world|applications?|practical)'
    }

    for lesson in lessons:
        lid = lesson['id']
        tutorial = lesson.get('tutorial', '')

        if not tutorial:
            issues['missing_tutorial'].append(lid)
            continue

        if len(tutorial) < 500:
            issues['too_short'].append((lid, len(tutorial)))

        tutorial_lower = tutorial.lower()

        for section, pattern in section_patterns.items():
            if not re.search(pattern, tutorial_lower, re.IGNORECASE):
                issues[f'missing_{section}'].append(lid)

    return issues

def analyze_tags(lessons):
    """Analyze tag coverage and consistency"""

    all_tags = set()
    tag_frequency = {}
    lessons_without_tags = []
    lessons_with_few_tags = []

    for lesson in lessons:
        lid = lesson['id']
        tags = lesson.get('tags', [])

        if not tags:
            lessons_without_tags.append(lid)
        elif len(tags) < 3:
            lessons_with_few_tags.append((lid, len(tags), tags))

        for tag in tags:
            all_tags.add(tag)
            tag_frequency[tag] = tag_frequency.get(tag, 0) + 1

    return {
        'total_unique_tags': len(all_tags),
        'all_tags': sorted(all_tags),
        'tag_frequency': sorted(tag_frequency.items(), key=lambda x: x[1], reverse=True),
        'no_tags': lessons_without_tags,
        'few_tags': lessons_with_few_tags
    }

def get_recommended_tags():
    """Return comprehensive list of recommended tags for curriculum"""

    return {
        'Fundamentals': [
            'Variables', 'Data Types', 'Operators', 'Control Flow', 'Loops',
            'Functions', 'Methods', 'Arrays', 'String', 'Input/Output'
        ],
        'OOP': [
            'OOP', 'Classes', 'Objects', 'Inheritance', 'Polymorphism',
            'Encapsulation', 'Abstraction', 'Interface', 'Abstract Class'
        ],
        'Data Structures': [
            'ArrayList', 'LinkedList', 'HashMap', 'HashSet', 'TreeMap', 'TreeSet',
            'Queue', 'Stack', 'Deque', 'PriorityQueue', 'Collections'
        ],
        'Advanced Java': [
            'Generics', 'Lambda', 'Streams', 'Optional', 'Functional Programming',
            'Method References', 'CompletableFuture'
        ],
        'Concurrency': [
            'Threads', 'Concurrency', 'Synchronization', 'Locks', 'Executor',
            'Thread Safety', 'Parallelism', 'Atomic'
        ],
        'Design Patterns': [
            'Design Patterns', 'Singleton', 'Factory', 'Builder', 'Strategy',
            'Observer', 'Decorator', 'Adapter', 'Facade', 'Proxy'
        ],
        'Algorithms': [
            'Algorithms', 'Sorting', 'Searching', 'Recursion', 'Dynamic Programming',
            'Greedy', 'Backtracking', 'Graph Algorithms', 'Tree Algorithms'
        ],
        'Testing & Quality': [
            'Testing', 'Unit Testing', 'JUnit', 'TDD', 'Mocking', 'Debugging',
            'Code Review', 'Best Practices', 'Clean Code'
        ],
        'Database': [
            'Database', 'SQL', 'JDBC', 'JPA', 'Hibernate', 'Transactions',
            'Connection Pooling'
        ],
        'Web & APIs': [
            'REST', 'API', 'HTTP', 'JSON', 'Web Services', 'Spring',
            'Microservices', 'Spring Boot'
        ],
        'Enterprise': [
            'Enterprise', 'Architecture', 'Distributed Systems', 'Messaging',
            'Caching', 'Logging', 'Monitoring', 'Configuration'
        ],
        'Cloud & DevOps': [
            'Cloud', 'AWS', 'Docker', 'Kubernetes', 'CI/CD', 'Jenkins',
            'Git', 'Version Control'
        ],
        'Security': [
            'Security', 'Authentication', 'Authorization', 'Encryption',
            'HTTPS', 'SQL Injection', 'XSS', 'CSRF'
        ],
        'Performance': [
            'Performance', 'Optimization', 'Memory Management', 'GC',
            'Profiling', 'JVM'
        ],
        'Career': [
            'Interview Prep', 'System Design', 'Career', 'Portfolio',
            'Job Ready', 'FAANG', 'Professional Development'
        ],
        'Difficulty': [
            'Beginner', 'Intermediate', 'Advanced', 'Expert', 'Enterprise'
        ]
    }

def main():
    print("="*80)
    print("COMPREHENSIVE LESSON ANALYSIS - TUTORIALS & TAGS")
    print("="*80)

    # Load Java lessons
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_data = json.load(f)

    lessons = java_data['lessons']
    print(f"\nAnalyzing {len(lessons)} Java lessons...")

    # Analyze tutorials
    print("\n" + "="*80)
    print("TUTORIAL QUALITY ANALYSIS")
    print("="*80)

    tutorial_issues = analyze_tutorials(lessons)

    print(f"\n[Tutorial Completeness]")
    print(f"  Missing tutorial entirely: {len(tutorial_issues['missing_tutorial'])} lessons")
    print(f"  Tutorial too short (<500 chars): {len(tutorial_issues['too_short'])} lessons")

    print(f"\n[Missing Tutorial Sections]")
    print(f"  Missing Overview: {len(tutorial_issues['missing_overview'])} lessons")
    print(f"  Missing Key Concepts: {len(tutorial_issues['missing_key_concepts'])} lessons")
    print(f"  Missing Code Examples: {len(tutorial_issues['missing_examples'])} lessons")
    print(f"  Missing Best Practices: {len(tutorial_issues['missing_best_practices'])} lessons")
    print(f"  Missing Common Pitfalls: {len(tutorial_issues['missing_pitfalls'])} lessons")
    print(f"  Missing Real-World Apps: {len(tutorial_issues['missing_real_world'])} lessons")

    # Show samples of issues
    if tutorial_issues['missing_overview']:
        print(f"\n  Sample lessons missing Overview:")
        for lid in tutorial_issues['missing_overview'][:5]:
            lesson = next(l for l in lessons if l['id'] == lid)
            print(f"    Lesson {lid}: {lesson['title'][:60]}")

    if tutorial_issues['too_short']:
        print(f"\n  Sample lessons with short tutorials:")
        for lid, length in tutorial_issues['too_short'][:5]:
            lesson = next(l for l in lessons if l['id'] == lid)
            print(f"    Lesson {lid}: {lesson['title'][:50]} ({length} chars)")

    # Analyze tags
    print("\n" + "="*80)
    print("TAG ANALYSIS")
    print("="*80)

    tag_analysis = analyze_tags(lessons)

    print(f"\n[Tag Statistics]")
    print(f"  Total unique tags in use: {tag_analysis['total_unique_tags']}")
    print(f"  Lessons without tags: {len(tag_analysis['no_tags'])}")
    print(f"  Lessons with <3 tags: {len(tag_analysis['few_tags'])}")

    print(f"\n[Top 20 Most Used Tags]")
    for i, (tag, count) in enumerate(tag_analysis['tag_frequency'][:20], 1):
        bar = "#" * (count // 10)
        print(f"  {i:2}. {tag:30} {count:4} {bar}")

    if tag_analysis['no_tags']:
        print(f"\n  Lessons without any tags:")
        for lid in tag_analysis['no_tags'][:10]:
            lesson = next(l for l in lessons if l['id'] == lid)
            print(f"    Lesson {lid}: {lesson['title'][:60]}")

    if tag_analysis['few_tags']:
        print(f"\n  Sample lessons with few tags:")
        for lid, count, tags in tag_analysis['few_tags'][:10]:
            lesson = next(l for l in lessons if l['id'] == lid)
            print(f"    Lesson {lid}: {lesson['title'][:50]} - {tags}")

    # Show recommended tag categories
    print("\n" + "="*80)
    print("RECOMMENDED TAG SYSTEM")
    print("="*80)

    recommended = get_recommended_tags()
    print("\nComprehensive tag categories for curriculum coverage:")

    for category, tags in recommended.items():
        print(f"\n{category}:")
        print(f"  {', '.join(tags)}")

    # Find tags currently in use but not in recommended list
    all_recommended = set()
    for tags in recommended.values():
        all_recommended.update(tags)

    extra_tags = set(tag_analysis['all_tags']) - all_recommended
    if extra_tags:
        print(f"\n[Tags in use but not in recommended list] ({len(extra_tags)}):")
        for tag in sorted(extra_tags)[:30]:
            count = next(c for t, c in tag_analysis['tag_frequency'] if t == tag)
            print(f"  - {tag} ({count} lessons)")

    # Summary statistics
    print("\n" + "="*80)
    print("SUMMARY & RECOMMENDATIONS")
    print("="*80)

    total_issues = (
        len(tutorial_issues['missing_tutorial']) +
        len(tutorial_issues['too_short']) +
        len(tutorial_issues['missing_overview']) +
        len(tutorial_issues['missing_key_concepts']) +
        len(tutorial_issues['missing_examples']) +
        len(tutorial_issues['missing_best_practices']) +
        len(tutorial_issues['missing_pitfalls']) +
        len(tutorial_issues['missing_real_world'])
    )

    print(f"\n[Overall Statistics]")
    print(f"  Total lessons: {len(lessons)}")
    print(f"  Lessons with tutorial issues: {total_issues}")
    print(f"  Lessons with tag issues: {len(tag_analysis['no_tags']) + len(tag_analysis['few_tags'])}")

    quality_score = ((len(lessons) - total_issues // 6) / len(lessons)) * 100
    print(f"  Estimated quality score: {quality_score:.1f}%")

    print("\n[Recommendations]")
    if tutorial_issues['missing_overview']:
        print(f"  1. Add Overview section to {len(tutorial_issues['missing_overview'])} lessons")
    if tutorial_issues['missing_key_concepts']:
        print(f"  2. Add Key Concepts to {len(tutorial_issues['missing_key_concepts'])} lessons")
    if tutorial_issues['missing_best_practices']:
        print(f"  3. Add Best Practices to {len(tutorial_issues['missing_best_practices'])} lessons")
    if tag_analysis['no_tags']:
        print(f"  4. Add tags to {len(tag_analysis['no_tags'])} untagged lessons")
    if tag_analysis['few_tags']:
        print(f"  5. Enhance tagging on {len(tag_analysis['few_tags'])} sparsely-tagged lessons")

    # Save detailed report
    report = {
        'tutorial_issues': {k: v for k, v in tutorial_issues.items()},
        'tag_analysis': {
            'total_unique_tags': tag_analysis['total_unique_tags'],
            'no_tags': tag_analysis['no_tags'],
            'few_tags': [(lid, count, tags) for lid, count, tags in tag_analysis['few_tags']],
            'tag_frequency': tag_analysis['tag_frequency'][:50]
        }
    }

    with open('lesson_analysis_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f"\n[SAVED] Detailed report saved to: lesson_analysis_report.json")
    print("="*80)

if __name__ == "__main__":
    main()
