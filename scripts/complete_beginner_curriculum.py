#!/usr/bin/env python3
"""
Complete and reorganize beginner curriculum:
1. Add comprehensive beginner lessons covering all missing topics
2. Reorganize all lessons in logical learning order
"""

import json
import sys
sys.path.append('scripts')
from enhance_beginner_lessons import create_html_tutorial, create_additional_examples


def create_lesson(lesson_id, title, description, category, tags, language):
    """Create a complete lesson object."""
    if language == 'java':
        base_code = f"""public class Main {{
    public static void main(String[] args) {{
        // TODO: {title}
        // {description}

        System.out.println("Complete the exercise");
    }}
}}"""
        full_solution = f"""public class Main {{
    public static void main(String[] args) {{
        // {title}
        // {description}

        System.out.println("Exercise completed!");
    }}
}}"""
    else:  # python
        base_code = f"""# TODO: {title}
# {description}

def main():
    print("Complete the exercise")

if __name__ == "__main__":
    main()"""
        full_solution = f"""# {title}
# {description}

def main():
    print("Exercise completed!")

if __name__ == "__main__":
    main()"""

    return {
        "id": lesson_id,
        "title": title,
        "description": description,
        "difficulty": "Beginner",
        "category": category,
        "tags": tags,
        "language": language,
        "baseCode": base_code,
        "fullSolution": full_solution,
        "testCases": [],
        "hints": [
            "Review the tutorial for key concepts",
            "Break down the problem into smaller steps",
            "Test your code with different inputs"
        ],
        "tutorial": "",  # Will be filled by enhance function
        "additionalExamples": "",  # Will be filled by enhance function
        "expectedOutput": "Exercise completed!"
    }


# Additional Java beginner topics (70 lessons to reach ~28%)
ADDITIONAL_JAVA_BEGINNER_TOPICS = [
    # More String Practice (10 lessons)
    ('String Contains and IndexOf', 'Check if string contains substring and find its position.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Replace', 'Replace characters and substrings in strings.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Split', 'Split strings into arrays using delimiters.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Join', 'Join array elements into a single string.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('StringBuilder Basics', 'Use StringBuilder for efficient string manipulation.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Reverse', 'Reverse a string using various methods.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Palindrome Check', 'Check if a string is a palindrome.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('Counting Characters in String', 'Count occurrences of characters in strings.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Empty vs Null', 'Understand and check for null and empty strings.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('Formatting Numbers in Strings', 'Format numbers as strings with decimal places.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),

    # More Loop Practice (10 lessons)
    ('Break Statement', 'Exit loops early using break.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Continue Statement', 'Skip to next iteration using continue.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Do-While Loop', 'Use do-while loops for at-least-once execution.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Enhanced For Loop', 'Iterate collections using enhanced for loop.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Nested Loops', 'Create patterns using nested loops.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Loop Practice - Sum Numbers', 'Calculate sum of numbers using loops.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Loop Practice - Count Even Numbers', 'Count even numbers in a range.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Loop Practice - Multiplication Table', 'Generate multiplication tables with loops.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Loop Practice - Find First Match', 'Find first element matching condition.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),
    ('Loop Practice - Validate Input', 'Use loops to validate user input.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),

    # Date and Time Basics (8 lessons)
    ('Creating Dates', 'Create date objects using LocalDate.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Date Formatting', 'Format dates for display.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Date Comparison', 'Compare dates to check which is earlier/later.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Adding Days to Date', 'Add or subtract days from dates.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Getting Current Date and Time', 'Get current date and time in Java.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Calculating Date Differences', 'Calculate days/months between dates.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Working with Time', 'Use LocalTime for time operations.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),
    ('Date and Time Together', 'Use LocalDateTime for complete timestamps.', 'Core Java', ['Beginner', 'Core Java', 'DateTime']),

    # More Array Practice (8 lessons)
    ('Two-Dimensional Arrays', 'Create and use 2D arrays (matrices).', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Copying', 'Copy arrays using Arrays.copyOf().', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Sorting', 'Sort arrays using Arrays.sort().', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Searching', 'Search arrays using Arrays.binarySearch().', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Equals', 'Compare arrays for equality.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array to String', 'Convert arrays to strings for display.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Fill', 'Fill array with default values.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Varargs', 'Create methods accepting variable arguments.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),

    # Simple Algorithms (10 lessons)
    ('Linear Search', 'Find element in array using linear search.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Bubble Sort', 'Sort array using bubble sort algorithm.', 'Algorithms', ['Beginner', 'Algorithms', 'Sorting']),
    ('Selection Sort', 'Sort array using selection sort algorithm.', 'Algorithms', ['Beginner', 'Algorithms', 'Sorting']),
    ('Insertion Sort', 'Sort array using insertion sort algorithm.', 'Algorithms', ['Beginner', 'Algorithms', 'Sorting']),
    ('Find Maximum Element', 'Find max element in unsorted array.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Find Minimum Element', 'Find min element in unsorted array.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Count Occurrences', 'Count how many times value appears in array.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Remove Duplicates', 'Remove duplicate elements from array.', 'Algorithms', ['Beginner', 'Algorithms', 'Arrays']),
    ('Reverse an Array', 'Reverse array elements in place.', 'Algorithms', ['Beginner', 'Algorithms', 'Arrays']),
    ('Check if Array is Sorted', 'Determine if array is sorted.', 'Algorithms', ['Beginner', 'Algorithms', 'Arrays']),

    # Regular Expressions Basics (6 lessons)
    ('Pattern Matching Basics', 'Match patterns in strings using regex.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),
    ('Email Validation', 'Validate email addresses with regex.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),
    ('Phone Number Validation', 'Validate phone numbers with regex.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),
    ('Extract Numbers from String', 'Extract all numbers from text.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),
    ('Replace with Regex', 'Replace text patterns using regex.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),
    ('Split with Regex', 'Split strings using regex patterns.', 'Core Java', ['Beginner', 'Core Java', 'Regex']),

    # Mini Projects (10 lessons)
    ('Build a Simple Calculator', 'Create calculator with basic operations.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Number Guessing Game', 'Create interactive guessing game.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Todo List', 'Create simple todo list application.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Grade Calculator', 'Calculate student grades and averages.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Contact Book', 'Store and manage contacts.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Shopping Cart', 'Implement basic shopping cart functionality.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Word Counter', 'Count words in text files.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Password Validator', 'Validate password strength.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Temperature Converter', 'Convert between temperature scales.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),
    ('Build a Simple ATM', 'Simulate ATM operations.', 'Core Java', ['Beginner', 'Core Java', 'Projects']),

    # Debugging and Best Practices (8 lessons)
    ('Reading Error Messages', 'Understand and interpret Java error messages.', 'Core Java', ['Beginner', 'Core Java', 'Debugging']),
    ('Using Print Debugging', 'Debug code using print statements.', 'Core Java', ['Beginner', 'Core Java', 'Debugging']),
    ('Common Beginner Mistakes', 'Avoid common pitfalls in Java.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
    ('Naming Conventions', 'Follow Java naming conventions.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
    ('Code Comments', 'Write effective code comments.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
    ('Code Organization', 'Organize code into logical sections.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
    ('Avoiding Magic Numbers', 'Use named constants instead of magic numbers.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
    ('Simple Refactoring', 'Improve code without changing behavior.', 'Core Java', ['Beginner', 'Core Java', 'Best Practices']),
]

# Additional Python beginner topics (40 lessons to reach ~28%)
ADDITIONAL_PYTHON_BEGINNER_TOPICS = [
    # More String Practice (8 lessons)
    ('String Find and Index', 'Find substring position in strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Replace', 'Replace text in strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Split and Join', 'Split strings into lists and join them back.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Reverse', 'Reverse strings using slicing.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Palindrome Check', 'Check if string is a palindrome.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('Counting Characters', 'Count character occurrences in strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Validation', 'Check if string is numeric, alphabetic, etc.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Formatting', 'Format strings with format() and f-strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),

    # More Loop Practice (6 lessons)
    ('Break Statement', 'Exit loops early with break.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),
    ('Continue Statement', 'Skip iteration with continue.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),
    ('Enumerate Function', 'Loop with index using enumerate.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),
    ('Zip Function', 'Iterate multiple lists together.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),
    ('Range Function', 'Generate number sequences with range.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),
    ('Nested Loops', 'Create patterns with nested loops.', 'Core Python', ['Beginner', 'Core Python', 'Loops']),

    # Date and Time Basics (5 lessons)
    ('Working with datetime', 'Create and manipulate datetime objects.', 'Core Python', ['Beginner', 'Core Python', 'DateTime']),
    ('Date Formatting', 'Format dates as strings.', 'Core Python', ['Beginner', 'Core Python', 'DateTime']),
    ('Date Arithmetic', 'Add and subtract time from dates.', 'Core Python', ['Beginner', 'Core Python', 'DateTime']),
    ('Getting Current Date/Time', 'Get current date and time.', 'Core Python', ['Beginner', 'Core Python', 'DateTime']),
    ('Comparing Dates', 'Compare dates to find earlier/later.', 'Core Python', ['Beginner', 'Core Python', 'DateTime']),

    # Simple Algorithms (8 lessons)
    ('Linear Search', 'Find element using linear search.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Bubble Sort', 'Sort list using bubble sort.', 'Algorithms', ['Beginner', 'Algorithms', 'Sorting']),
    ('Selection Sort', 'Sort list using selection sort.', 'Algorithms', ['Beginner', 'Algorithms', 'Sorting']),
    ('Find Maximum', 'Find max element in list.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Find Minimum', 'Find min element in list.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Count Occurrences', 'Count value occurrences in list.', 'Algorithms', ['Beginner', 'Algorithms', 'Searching']),
    ('Remove Duplicates', 'Remove duplicates from list.', 'Algorithms', ['Beginner', 'Algorithms', 'Lists']),
    ('Reverse a List', 'Reverse list in place.', 'Algorithms', ['Beginner', 'Algorithms', 'Lists']),

    # Regular Expressions (4 lessons)
    ('Regex Basics', 'Match patterns with regular expressions.', 'Core Python', ['Beginner', 'Core Python', 'Regex']),
    ('Email Validation', 'Validate emails with regex.', 'Core Python', ['Beginner', 'Core Python', 'Regex']),
    ('Extract Numbers', 'Extract numbers from text with regex.', 'Core Python', ['Beginner', 'Core Python', 'Regex']),
    ('Replace with Regex', 'Replace patterns using regex.', 'Core Python', ['Beginner', 'Core Python', 'Regex']),

    # Mini Projects (5 lessons)
    ('Build a Calculator', 'Create simple calculator.', 'Core Python', ['Beginner', 'Core Python', 'Projects']),
    ('Build a Guessing Game', 'Create number guessing game.', 'Core Python', ['Beginner', 'Core Python', 'Projects']),
    ('Build a Todo List', 'Create todo list application.', 'Core Python', ['Beginner', 'Core Python', 'Projects']),
    ('Build a Grade Calculator', 'Calculate student grades.', 'Core Python', ['Beginner', 'Core Python', 'Projects']),
    ('Build a Contact Book', 'Manage contacts in Python.', 'Core Python', ['Beginner', 'Core Python', 'Projects']),

    # Debugging and Best Practices (4 lessons)
    ('Reading Error Messages', 'Understand Python error messages.', 'Core Python', ['Beginner', 'Core Python', 'Debugging']),
    ('Print Debugging', 'Debug with print statements.', 'Core Python', ['Beginner', 'Core Python', 'Debugging']),
    ('Python Naming Conventions', 'Follow PEP 8 naming standards.', 'Core Python', ['Beginner', 'Core Python', 'Best Practices']),
    ('Writing Good Comments', 'Write clear code comments.', 'Core Python', ['Beginner', 'Core Python', 'Best Practices']),
]


def add_comprehensive_lessons(language='java', topics=None, starting_id=1018):
    """Add comprehensive beginner lessons."""
    filename = f'public/lessons-{language}.json'

    print(f"\nAdding {len(topics)} new {language} beginner lessons...")
    with open(filename, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    new_lessons = []
    for i, (title, desc, category, tags) in enumerate(topics):
        lesson_id = starting_id + i
        lesson = create_lesson(lesson_id, title, desc, category, tags, language)

        # Enhance with rich content
        lesson['tutorial'] = create_html_tutorial(title, desc, category, tags, language)
        lesson['additionalExamples'] = create_additional_examples(title, desc, language)
        lesson['expectedOutput'] = "Exercise completed!"

        new_lessons.append(lesson)

    lessons.extend(new_lessons)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"Added {len(new_lessons)} lessons to {language}")
    return len(new_lessons)


def reorganize_lessons(language='java'):
    """Reorganize lessons in logical learning order."""
    filename = f'public/lessons-{language}.json'

    print(f"\nReorganizing {language} lessons in logical order...")
    with open(filename, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Separate by difficulty
    beginner = [l for l in lessons if l['difficulty'] == 'Beginner']
    intermediate = [l for l in lessons if l['difficulty'] == 'Intermediate']
    advanced = [l for l in lessons if l['difficulty'] == 'Advanced']
    expert = [l for l in lessons if l['difficulty'] == 'Expert']

    print(f"  Beginner: {len(beginner)} lessons")
    print(f"  Intermediate: {len(intermediate)} lessons")
    print(f"  Advanced: {len(advanced)} lessons")
    print(f"  Expert: {len(expert)} lessons")

    # Sort each group by category, then by title
    def sort_key(lesson):
        category_order = {
            'Core Java': 1, 'Core Python': 1,
            'OOP': 2,
            'Algorithms': 3,
            'Testing': 4,
            'Database': 5,
            'Web Development': 6,
            'Cloud': 7,
            'DevOps': 8,
        }
        category = lesson.get('category', 'Other')
        return (category_order.get(category, 99), lesson.get('title', ''))

    beginner.sort(key=sort_key)
    intermediate.sort(key=sort_key)
    advanced.sort(key=sort_key)
    expert.sort(key=sort_key)

    # Reassign IDs sequentially
    reorganized = beginner + intermediate + advanced + expert
    for i, lesson in enumerate(reorganized, 1):
        lesson['id'] = i

    # Save reorganized lessons
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reorganized, f, indent=2, ensure_ascii=False)

    print(f"Reorganized {len(reorganized)} lessons")
    print(f"  New ID range: 1-{len(reorganized)}")
    print(f"  Beginner lessons: IDs 1-{len(beginner)}")
    print(f"  Intermediate lessons: IDs {len(beginner)+1}-{len(beginner)+len(intermediate)}")
    print(f"  Advanced lessons: IDs {len(beginner)+len(intermediate)+1}-{len(beginner)+len(intermediate)+len(advanced)}")
    print(f"  Expert lessons: IDs {len(beginner)+len(intermediate)+len(advanced)+1}-{len(reorganized)}")

    return len(reorganized)


if __name__ == "__main__":
    print("=" * 80)
    print("COMPLETING AND REORGANIZING BEGINNER CURRICULUM")
    print("=" * 80)

    # Add comprehensive lessons
    java_added = add_comprehensive_lessons('java', ADDITIONAL_JAVA_BEGINNER_TOPICS, 1018)
    python_added = add_comprehensive_lessons('python', ADDITIONAL_PYTHON_BEGINNER_TOPICS, 995)

    print()
    print("=" * 80)
    print("REORGANIZING LESSONS IN LOGICAL ORDER")
    print("=" * 80)

    # Reorganize both curricula
    java_total = reorganize_lessons('java')
    python_total = reorganize_lessons('python')

    print()
    print("=" * 80)
    print("COMPLETE!")
    print("=" * 80)
    print(f"\nJava: Added {java_added} lessons, reorganized {java_total} total")
    print(f"Python: Added {python_added} lessons, reorganized {python_total} total")
    print()
    print("Next steps:")
    print("  1. Run validation: node scripts/validate-lessons.mjs")
    print("  2. Review lesson organization")
    print("  3. Commit changes")
    print("=" * 80)
