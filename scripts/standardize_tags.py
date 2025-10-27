import json

# Tag standardization mapping: old_tag -> new_tag
TAG_STANDARDIZATION = {
    # Capitalize inconsistencies
    'enterprise': 'Enterprise',
    'intermediate': 'Intermediate',
    'beginner': 'Beginner',
    'advanced': 'Advanced',
    'expert': 'Expert',

    # Consolidate similar tags
    'Basics': 'Beginner',
    'basics': 'Beginner',
    'Basic': 'Beginner',

    # Standardize common terms
    'arrays': 'Arrays',
    'strings': 'Strings',
    'loops': 'Loops',
    'functions': 'Functions',
    'methods': 'Methods',

    # Algorithm tags
    'algorithms': 'Algorithms',
    'sorting': 'Sorting',
    'searching': 'Searching',

    # OOP tags
    'oop': 'OOP',
    'classes': 'Classes',
    'objects': 'Objects',
    'inheritance': 'Inheritance',

    # Collections
    'collections': 'Collections',
    'arraylist': 'ArrayList',
    'hashmap': 'HashMap',
    'hashset': 'HashSet',

    # Concurrency
    'concurrency': 'Concurrency',
    'threads': 'Threads',
    'threading': 'Threads',

    # Web & APIs
    'api': 'API',
    'rest': 'REST',
    'http': 'HTTP',
    'json': 'JSON',

    # Testing
    'testing': 'Testing',
    'junit': 'JUnit',
    'tdd': 'TDD',

    # Database
    'database': 'Database',
    'sql': 'SQL',
    'jdbc': 'JDBC',

    # Career
    'career': 'Career',
    'interview': 'Interview Prep',
    'faang': 'FAANG',
    'portfolio': 'Portfolio',

    # Design Patterns - standardize to full names
    'design patterns': 'Design Patterns',
    'singleton': 'Singleton',
    'factory': 'Factory',
    'builder': 'Builder',
    'strategy': 'Strategy',
    'observer': 'Observer',

    # Security
    'security': 'Security',
    'authentication': 'Authentication',
    'authorization': 'Authorization',

    # Performance
    'performance': 'Performance',
    'optimization': 'Optimization',

    # Cloud & DevOps
    'cloud': 'Cloud',
    'aws': 'AWS',
    'docker': 'Docker',
    'kubernetes': 'Kubernetes',
    'git': 'Git',

    # Add proper capitalization
    'spring': 'Spring',
    'spring boot': 'Spring Boot',
    'microservices': 'Microservices',
}

def standardize_tags(tags):
    """Standardize tags according to mapping"""
    standardized = []
    seen = set()

    for tag in tags:
        # Apply standardization
        new_tag = TAG_STANDARDIZATION.get(tag, tag)

        # Remove duplicates (case-insensitive)
        if new_tag.lower() not in seen:
            standardized.append(new_tag)
            seen.add(new_tag.lower())

    return standardized

def main():
    print("="*80)
    print("TAG STANDARDIZATION")
    print("="*80)

    for language in ['java', 'python']:
        print(f"\nProcessing {language.upper()} lessons...")

        filename = f'public/lessons-{language}.json'
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        modified_count = 0
        tag_changes = {}

        for lesson in data['lessons']:
            original_tags = lesson.get('tags', [])
            standardized_tags = standardize_tags(original_tags)

            if original_tags != standardized_tags:
                lesson['tags'] = standardized_tags
                modified_count += 1

                # Track what changed
                for old, new in zip(original_tags, standardized_tags):
                    if old != new:
                        tag_changes[old] = new

        # Save
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"  Modified {modified_count} lessons")

        if tag_changes:
            print(f"\n  Tag changes applied:")
            for old, new in sorted(tag_changes.items())[:20]:
                print(f"    '{old}' -> '{new}'")

    print("\n" + "="*80)
    print("TAG STANDARDIZATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
