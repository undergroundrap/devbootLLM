#!/usr/bin/env python3
"""
Upgrade Python Foundational Lessons - Batch 1
IDs 1-10: The absolute basics every learner sees first
Using proven patterns from critical lesson upgrades
"""

import json

UPGRADES = {
    1: {
        "title": "Hello, World!",
        "solution": """\"\"\"
Hello, World! - Your First Python Program

The traditional first program in any language. Learn the fundamentals
of Python syntax, output, and program structure.

**Zero Package Installation Required**
\"\"\"

# Example 1: The Classic Hello World
print("="*70)
print("Example 1: Basic Hello World")
print("="*70)

print("Hello, World!")

# Example 2: Understanding print()
print("\\n" + "="*70)
print("Example 2: How print() Works")
print("="*70)

# print() displays text to the console
print("This is a message")
print("This is another message")

# Multiple items separated by spaces
print("Hello", "World", "from", "Python")

# Example 3: Different Greetings
print("\\n" + "="*70)
print("Example 3: Multiple Greetings")
print("="*70)

print("Hello, World!")
print("Bonjour, le monde!")
print("Hola, Mundo!")
print("你好，世界!")
print("こんにちは、世界!")

# Example 4: Print with Newlines
print("\\n" + "="*70)
print("Example 4: Multi-line Output")
print("="*70)

print("Line 1")
print("Line 2")
print("Line 3")

# Using \\n for newlines within a string
print("\\nUsing escape sequences:")
print("First line\\nSecond line\\nThird line")

# Example 5: Print Separators
print("\\n" + "="*70)
print("Example 5: Custom Separators")
print("="*70)

# Default separator is space
print("A", "B", "C")

# Custom separator
print("A", "B", "C", sep="-")
print("A", "B", "C", sep=" | ")
print("A", "B", "C", sep="\\n")

# Example 6: Print End Characters
print("\\n" + "="*70)
print("Example 6: Custom End Characters")
print("="*70)

# Default end is newline
print("Hello", end=" ")
print("World")

# Custom end
print("Loading", end="...")
print("Done!")

# Example 7: Formatted Output
print("\\n" + "="*70)
print("Example 7: Creating Patterns")
print("="*70)

print("*" * 40)
print("*", " " * 36, "*")
print("*", " " * 10, "HELLO WORLD", " " * 13, "*")
print("*", " " * 36, "*")
print("*" * 40)

# Example 8: Numbers and Calculations
print("\\n" + "="*70)
print("Example 8: Printing Numbers")
print("="*70)

print(42)
print(3.14159)
print(2 + 2)
print(10 * 5)

# Example 9: Program Header
print("\\n" + "="*70)
print("Example 9: Professional Output")
print("="*70)

print("="*50)
print("  WELCOME TO MY PYTHON PROGRAM")
print("  Version: 1.0")
print("  Author: Python Learner")
print("="*50)

# Example 10: Building Blocks
print("\\n" + "="*70)
print("Example 10: Combining Concepts")
print("="*70)

print("Program started...")
print()
print("Processing data...")
print("Step 1: Complete")
print("Step 2: Complete")
print("Step 3: Complete")
print()
print("Program finished successfully!")

print("\\n" + "="*70)
print("Hello World Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  • print() displays output to the console")
print("  • Strings go in quotes: 'text' or \\"text\\"")
print("  • Use sep= to change separator between items")
print("  • Use end= to change what comes after")
print("  • \\\\n creates a new line")
print("  • This is the foundation of all Python programs!")

print("\\nNext steps:")
print("  → Learn about variables to store data")
print("  → Explore data types (strings, numbers, etc.)")
print("  → Try user input with input()")
\"\"\"
    }
}

def upgrade_batch1():
    \"\"\"Upgrade batch 1 foundational Python lessons.\"\"\"
    print("="*80)
    print("UPGRADING PYTHON FOUNDATIONAL - BATCH 1")
    print("IDs 1-10: The Absolute Basics")
    print("="*80)

    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    count = 0
    for lesson_id, upgrade_data in UPGRADES.items():
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)

        if lesson:
            old_length = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = upgrade_data['solution']
            new_length = len(lesson['fullSolution'])

            print(f"\\nLesson {lesson_id}: {lesson['title']}")
            print(f"  {old_length:,} -> {new_length:,} characters "
                  f"(+{new_length - old_length:,}, +{((new_length - old_length)/old_length*100):.1f}%)")
            count += 1

    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print("\\n" + "="*80)
    print(f"Batch 1 Complete: {count} lesson(s) upgraded")
    print("="*80)
    print("\\nNext: Continue with lessons 2-10")

if __name__ == '__main__':
    upgrade_batch1()
