import json

# REPOSITIONING PLAN:
# Insert bridging lessons between levels to smooth transitions
# This requires shifting existing lesson IDs to make room

repositioning_plan = {
    # Beginner Bridges: Insert after lesson 100 (between Beginner and Intermediate)
    # 697-700 → 101-104, shift old 101-696 → 105-700
    697: 101,  # String Manipulation Mastery
    698: 102,  # Array Searching: Linear vs Binary
    699: 103,  # Working with Multiple Arrays
    700: 104,  # Input Validation

    # Intermediate Bridges: Insert after old lesson 200 (now 204)
    # 701-710 → 205-214, shift old 201-696 → 215-710
    701: 205,  # HashMap Deep Dive
    702: 206,  # ArrayList vs LinkedList
    703: 207,  # TreeSet and TreeMap
    704: 208,  # Queue and Deque
    705: 209,  # Stack Applications
    706: 210,  # Set Operations
    707: 211,  # Sorting Algorithms Comparison
    708: 212,  # Recursion Patterns
    709: 213,  # StringBuilder Performance
    710: 214,  # Wrapper Classes

    # Advanced Bridges: Insert after old lesson 350 (now 364 after shifts)
    # 711-720 → 365-374, shift old 351-696 → 375-720
    711: 365,  # Abstract Classes vs Interfaces
    712: 366,  # Composition over Inheritance
    713: 367,  # Immutable Objects
    714: 368,  # Builder Pattern
    715: 369,  # Strategy Pattern
    716: 370,  # Observer Pattern
    717: 371,  # Factory Pattern
    718: 372,  # Singleton Pattern
    719: 373,  # Decorator Pattern
    720: 374,  # Template Method Pattern

    # Expert Bridges: Insert after old lesson 500 (now 524 after shifts)
    # 721-728 → 525-532, shift old 501-696 → 533-728
    721: 525,  # Thread Synchronization
    722: 526,  # Concurrent Collections
    723: 527,  # Executor Framework
    724: 528,  # CompletableFuture
    725: 529,  # Memory Management
    726: 530,  # Garbage Collection Tuning
    727: 531,  # JVM Performance Monitoring
    728: 532,  # Caching Strategies

    # Enterprise Bridges: Insert after old lesson 600 (now 632 after shifts)
    # 729-735 → 633-639, shift old 601-696 → 640-735
    729: 633,  # RESTful API Design
    730: 634,  # Database Connection Pooling
    731: 635,  # Logging Best Practices
    732: 636,  # Configuration Management
    733: 637,  # Health Checks and Monitoring
    734: 638,  # Rate Limiting
    735: 639,  # Circuit Breaker Pattern
}

def calculate_new_id(old_id):
    """Calculate new ID for a lesson based on how many bridges come before it"""

    # Lessons 1-100 stay the same
    if old_id <= 100:
        return old_id

    # Lessons 101-200 shift by +4 (for beginner bridges 101-104)
    elif old_id <= 200:
        return old_id + 4

    # Lessons 201-350 shift by +14 (4 beginner + 10 intermediate)
    elif old_id <= 350:
        return old_id + 14

    # Lessons 351-500 shift by +24 (4 + 10 + 10 advanced)
    elif old_id <= 500:
        return old_id + 24

    # Lessons 501-600 shift by +32 (4 + 10 + 10 + 8 expert)
    elif old_id <= 600:
        return old_id + 32

    # Lessons 601+ shift by +39 (4 + 10 + 10 + 8 + 7 enterprise)
    else:
        return old_id + 39

def reposition_lessons(language='java'):
    """Reposition all bridging lessons to their correct locations"""

    filename = f'public/lessons-{language}.json'

    # Load lessons
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"\n{'='*80}")
    print(f"REPOSITIONING {language.upper()} LESSONS")
    print(f"{'='*80}\n")

    # Separate bridge lessons (697-735) from existing lessons
    bridge_lessons = {l['id']: l for l in data['lessons'] if l['id'] >= 697}
    existing_lessons = [l for l in data['lessons'] if l['id'] <= 696]

    print(f"Bridge lessons to reposition: {len(bridge_lessons)}")
    print(f"Existing lessons to shift: {len(existing_lessons)}\n")

    # Create new lesson list
    new_lessons = []

    # Sort existing lessons by ID
    existing_lessons.sort(key=lambda x: x['id'])

    # Apply shifts to existing lessons
    print("STEP 1: Shifting existing lessons to make room for bridges")
    print("-" * 80)

    for lesson in existing_lessons:
        old_id = lesson['id']
        new_id = calculate_new_id(old_id)

        lesson['id'] = new_id
        new_lessons.append(lesson)

        if old_id != new_id and old_id % 50 == 0:  # Show progress
            print(f"  Lesson {old_id} -> {new_id} (+{new_id - old_id})")

    print(f"\nShifted {len(new_lessons)} existing lessons")

    # Insert bridge lessons at new positions
    print("\nSTEP 2: Inserting bridging lessons at correct positions")
    print("-" * 80)

    for old_id, new_id in sorted(repositioning_plan.items(), key=lambda x: x[1]):
        if old_id in bridge_lessons:
            lesson = bridge_lessons[old_id]
            lesson['id'] = new_id
            new_lessons.append(lesson)
            print(f"  Bridge lesson {old_id} -> {new_id}: {lesson['title'][:50]}")

    # Sort by new ID
    new_lessons.sort(key=lambda x: x['id'])

    # Verify we have 700 lessons
    print(f"\nSTEP 3: Validation")
    print("-" * 80)
    print(f"Total lessons: {len(new_lessons)}")
    print(f"Expected: 700")
    print(f"ID range: {new_lessons[0]['id']} to {new_lessons[-1]['id']}")

    # Check for duplicate IDs
    ids = [l['id'] for l in new_lessons]
    duplicates = [id for id in ids if ids.count(id) > 1]
    if duplicates:
        print(f"WARNING: Duplicate IDs found: {set(duplicates)}")
        return False
    else:
        print("[OK] No duplicate IDs")

    # Check for missing IDs in critical ranges
    id_set = set(ids)
    missing = []
    for i in range(1, 101):  # Check beginner range
        if i not in id_set:
            missing.append(i)
    if missing:
        print(f"WARNING: Missing IDs in beginner range: {missing}")

    # Save repositioned lessons
    data['lessons'] = new_lessons

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n[SUCCESS] Saved {len(new_lessons)} lessons to {filename}")
    return True

def show_new_ranges():
    """Show the new lesson ID ranges after repositioning"""
    print("\n" + "="*80)
    print("NEW LESSON RANGES AFTER REPOSITIONING")
    print("="*80 + "\n")

    ranges = [
        ("Level 1: Beginner", "1-100", "Foundation lessons (100 lessons)"),
        ("Beginner Bridges", "101-104", "String, arrays, search, validation (4 lessons)"),
        ("Level 2: Intermediate", "105-204", "Core software engineering (100 lessons)"),
        ("Intermediate Bridges", "205-214", "Collections deep dive (10 lessons)"),
        ("Level 3: Advanced", "215-364", "Professional patterns (150 lessons)"),
        ("Advanced Bridges", "365-374", "Design patterns (10 lessons)"),
        ("Level 4: Expert", "375-524", "Production systems (150 lessons)"),
        ("Expert Bridges", "525-532", "Concurrency & performance (8 lessons)"),
        ("Level 5: Enterprise", "533-632", "FAANG-level topics (100 lessons)"),
        ("Enterprise Bridges", "633-639", "Real-world systems (7 lessons)"),
        ("Level 6: FAANG Prep", "640-689", "Interview preparation (50 lessons)"),
        ("Level 7: Job Ready", "690-700", "Portfolio & career (11 lessons)"),
    ]

    total = 0
    for level, range_str, desc in ranges:
        start, end = map(int, range_str.split('-'))
        count = end - start + 1
        total += count
        print(f"{level:25} {range_str:12} - {desc}")

    print(f"\n{'TOTAL':25} {total} lessons")
    print("="*80)

if __name__ == "__main__":
    print("="*80)
    print("BRIDGING LESSON REPOSITIONING SCRIPT")
    print("="*80)

    # Show the plan
    show_new_ranges()

    # Reposition Java lessons
    success_java = reposition_lessons('java')

    if success_java:
        # Reposition Python lessons
        success_python = reposition_lessons('python')

        if success_python:
            print("\n" + "="*80)
            print("[SUCCESS] All bridging lessons repositioned correctly!")
            print("="*80)
            print("\nBridging lessons are now positioned between their respective levels:")
            print("  - Beginner bridges (101-104) smooth transition to Intermediate")
            print("  - Intermediate bridges (205-214) smooth transition to Advanced")
            print("  - Advanced bridges (365-374) smooth transition to Expert")
            print("  - Expert bridges (525-532) smooth transition to Enterprise")
            print("  - Enterprise bridges (633-639) smooth transition to FAANG Prep")
        else:
            print("\n[ERROR] Failed to reposition Python lessons")
    else:
        print("\n[ERROR] Failed to reposition Java lessons")
