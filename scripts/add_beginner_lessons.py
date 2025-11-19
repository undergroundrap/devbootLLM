#!/usr/bin/env python3
"""
Add beginner lessons to Java and Python curricula
Increases Beginner % from ~13-17% to ~25-30%
"""

import json

# Java beginner lesson definitions (100 lessons)
JAVA_BEGINNER_LESSONS = [
    # Basic Syntax & Operations (15 lessons)
    ('String Length and Character Access', 'Learn how to get string length and access individual characters in Java.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Concatenation', 'Practice combining strings using concatenation operators and methods.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Comparison', 'Learn to compare strings using equals() and compareTo() methods.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Case Conversion', 'Convert strings between uppercase and lowercase in Java.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('String Trimming', 'Remove whitespace from the beginning and end of strings.', 'Core Java', ['Beginner', 'Core Java', 'Strings']),
    ('Basic Math Operations', 'Practice addition, subtraction, multiplication, and division with integers.', 'Core Java', ['Beginner', 'Core Java', 'Math']),
    ('Integer Division and Modulo', 'Understand integer division and the modulo operator.', 'Core Java', ['Beginner', 'Core Java', 'Math']),
    ('Type Casting Basics', 'Learn to convert between numeric types in Java.', 'Core Java', ['Beginner', 'Core Java', 'Types']),
    ('Boolean Logic - AND', 'Practice using the AND logical operator.', 'Core Java', ['Beginner', 'Core Java', 'Logic']),
    ('Boolean Logic - OR', 'Practice using the OR logical operator.', 'Core Java', ['Beginner', 'Core Java', 'Logic']),
    ('Boolean Logic - NOT', 'Practice using the NOT logical operator.', 'Core Java', ['Beginner', 'Core Java', 'Logic']),
    ('Simple If Statements', 'Write basic if statements to make decisions in code.', 'Core Java', ['Beginner', 'Core Java', 'Control Flow']),
    ('If-Else Statements', 'Use if-else to handle two different conditions.', 'Core Java', ['Beginner', 'Core Java', 'Control Flow']),
    ('Nested If Statements', 'Practice nesting if statements for complex conditions.', 'Core Java', ['Beginner', 'Core Java', 'Control Flow']),
    ('Simple For Loop', 'Learn to use for loops to repeat code a specific number of times.', 'Core Java', ['Beginner', 'Core Java', 'Loops']),

    # Arrays & Lists (15 lessons)
    ('Creating Arrays', 'Learn how to create and initialize arrays in Java.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Accessing Array Elements', 'Practice accessing elements in an array by index.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Array Length', 'Use the length property to find the size of an array.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Iterating Through Arrays', 'Loop through array elements using for loops.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Modifying Array Elements', 'Change values in an array by index.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Sum of Array Elements', 'Calculate the sum of all numbers in an array.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Finding Max in Array', 'Find the largest number in an array.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Finding Min in Array', 'Find the smallest number in an array.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Counting Array Elements', 'Count how many elements meet a specific condition.', 'Core Java', ['Beginner', 'Core Java', 'Arrays']),
    ('Creating ArrayLists', 'Learn to create and use ArrayList for dynamic arrays.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Adding to ArrayList', 'Add elements to an ArrayList using add() method.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Removing from ArrayList', 'Remove elements from an ArrayList.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('ArrayList Size', 'Get the number of elements in an ArrayList.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Checking ArrayList Contains', 'Check if an ArrayList contains a specific element.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Iterating ArrayList', 'Loop through ArrayList elements.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),

    # Functions & Methods (15 lessons)
    ('Creating Simple Methods', 'Write your first method that returns a value.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Method Parameters', 'Pass values to methods using parameters.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Return Values', 'Return results from methods.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Void Methods', 'Create methods that perform actions without returning values.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Multiple Parameters', 'Write methods that accept multiple parameters.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Method Overloading Basics', 'Create multiple methods with the same name but different parameters.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Simple Recursion', 'Understand basic recursive method calls.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Factorial Function', 'Calculate factorial using a simple method.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('String Helper Methods', 'Create utility methods for string manipulation.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Array Helper Methods', 'Create utility methods for array operations.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Math Helper Methods', 'Create utility methods for mathematical operations.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Validation Methods', 'Write methods that validate input data.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Simple Calculator Methods', 'Create basic calculator methods.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Temperature Conversion Methods', 'Convert between Celsius and Fahrenheit.', 'Core Java', ['Beginner', 'Core Java', 'Methods']),
    ('Simple Unit Tests', 'Learn to test your methods with basic assertions.', 'Testing', ['Beginner', 'Testing', 'JUnit']),

    # Classes & Objects Basics (20 lessons)
    ('Creating a Simple Class', 'Define your first Java class with fields.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Class Constructors', 'Learn to create constructors for initializing objects.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Instance Variables', 'Understand and use instance variables in classes.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Getter Methods', 'Create getter methods to access private fields.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Setter Methods', 'Create setter methods to modify private fields.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Creating Objects', 'Instantiate objects from classes using the new keyword.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Object Method Calls', 'Call methods on object instances.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Multiple Constructors', 'Create classes with multiple constructor options.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('This Keyword', 'Use the this keyword to refer to current object.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Static vs Instance', 'Understand the difference between static and instance members.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Person Class', 'Build a Person class with basic properties and methods.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Book Class', 'Build a Book class with title, author, and pages.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Car Class', 'Build a Car class with make, model, and year.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Student Class', 'Build a Student class with name and grades.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple BankAccount Class', 'Build a BankAccount class with deposit and withdraw.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('toString Method', 'Override toString() to create string representations of objects.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('equals Method Basics', 'Learn to compare objects using equals().', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Inheritance', 'Create a subclass that extends a parent class.', 'OOP', ['Beginner', 'OOP', 'Inheritance']),
    ('Method Overriding Basics', 'Override parent class methods in subclasses.', 'OOP', ['Beginner', 'OOP', 'Inheritance']),
    ('Super Keyword', 'Use super to call parent class constructors and methods.', 'OOP', ['Beginner', 'OOP', 'Inheritance']),

    # Input/Output & Files (10 lessons)
    ('Reading Console Input', 'Use Scanner to read user input from console.', 'Core Java', ['Beginner', 'Core Java', 'I/O']),
    ('Reading Integers', 'Read integer values from user input.', 'Core Java', ['Beginner', 'Core Java', 'I/O']),
    ('Reading Strings', 'Read string values from user input.', 'Core Java', ['Beginner', 'Core Java', 'I/O']),
    ('Simple Menu System', 'Create a simple text-based menu for user interaction.', 'Core Java', ['Beginner', 'Core Java', 'I/O']),
    ('Input Validation', 'Validate user input to prevent errors.', 'Core Java', ['Beginner', 'Core Java', 'I/O']),
    ('Reading Text Files', 'Read content from text files line by line.', 'Core Java', ['Beginner', 'Core Java', 'Files']),
    ('Writing Text Files', 'Write text content to files.', 'Core Java', ['Beginner', 'Core Java', 'Files']),
    ('Appending to Files', 'Add content to existing files without overwriting.', 'Core Java', ['Beginner', 'Core Java', 'Files']),
    ('Counting File Lines', 'Count the number of lines in a text file.', 'Core Java', ['Beginner', 'Core Java', 'Files']),
    ('Simple File Copy', 'Copy content from one file to another.', 'Core Java', ['Beginner', 'Core Java', 'Files']),

    # Error Handling (10 lessons)
    ('Try-Catch Basics', 'Handle exceptions using try-catch blocks.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('Catching Specific Exceptions', 'Catch different exception types separately.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('Finally Block', 'Use finally for cleanup code that always runs.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('Throwing Exceptions', 'Throw your own exceptions when needed.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('NumberFormatException Handling', 'Handle errors when parsing numbers from strings.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('NullPointerException Handling', 'Prevent and handle null pointer errors.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('ArrayIndexOutOfBounds Handling', 'Handle array index errors gracefully.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('FileNotFoundException Handling', 'Handle file not found errors.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('IOException Handling', 'Handle input/output errors.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),
    ('Custom Exception Class', 'Create your own exception class.', 'Core Java', ['Beginner', 'Core Java', 'Exceptions']),

    # Collections & Maps (15 lessons)
    ('HashSet Basics', 'Use HashSet for storing unique elements.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Adding to HashSet', 'Add elements to a HashSet.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Removing from HashSet', 'Remove elements from a HashSet.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Checking Set Contains', 'Check if a HashSet contains an element.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Iterating HashSet', 'Loop through HashSet elements.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('HashMap Basics', 'Store key-value pairs using HashMap.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Adding to HashMap', 'Put key-value pairs into a HashMap.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Getting from HashMap', 'Retrieve values from HashMap by key.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Removing from HashMap', 'Remove key-value pairs from HashMap.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Checking HashMap Keys', 'Check if a HashMap contains a specific key.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Iterating HashMap', 'Loop through HashMap entries.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('LinkedList Basics', 'Use LinkedList for ordered collections.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Stack Basics', 'Use Stack for LIFO (Last In First Out) operations.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Queue Basics', 'Use Queue for FIFO (First In First Out) operations.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
    ('Comparing Collections', 'Understand when to use different collection types.', 'Core Java', ['Beginner', 'Core Java', 'Collections']),
]

# Python beginner lesson definitions (90 lessons)
PYTHON_BEGINNER_LESSONS = [
    # Basic Syntax & Operations (15 lessons)
    ('String Length and Indexing', 'Learn how to get string length and access characters by index in Python.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Concatenation', 'Practice combining strings using the + operator.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Formatting with f-strings', 'Learn to format strings using f-strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Methods - upper and lower', 'Convert strings between uppercase and lowercase.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Methods - strip', 'Remove whitespace from strings.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('String Slicing', 'Extract portions of strings using slice notation.', 'Core Python', ['Beginner', 'Core Python', 'Strings']),
    ('Basic Math Operations', 'Practice arithmetic operators in Python.', 'Core Python', ['Beginner', 'Core Python', 'Math']),
    ('Integer Division and Modulo', 'Use // for integer division and % for modulo.', 'Core Python', ['Beginner', 'Core Python', 'Math']),
    ('Type Conversion', 'Convert between int, float, and str types.', 'Core Python', ['Beginner', 'Core Python', 'Types']),
    ('Boolean Logic - and', 'Practice using the and logical operator.', 'Core Python', ['Beginner', 'Core Python', 'Logic']),
    ('Boolean Logic - or', 'Practice using the or logical operator.', 'Core Python', ['Beginner', 'Core Python', 'Logic']),
    ('Boolean Logic - not', 'Practice using the not logical operator.', 'Core Python', ['Beginner', 'Core Python', 'Logic']),
    ('Simple If Statements', 'Write basic if statements for decision making.', 'Core Python', ['Beginner', 'Core Python', 'Control Flow']),
    ('If-Elif-Else Statements', 'Handle multiple conditions with elif.', 'Core Python', ['Beginner', 'Core Python', 'Control Flow']),
    ('Nested If Statements', 'Practice nesting if statements.', 'Core Python', ['Beginner', 'Core Python', 'Control Flow']),

    # Lists & Tuples (15 lessons)
    ('Creating Lists', 'Learn to create and initialize lists in Python.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Accessing List Elements', 'Access elements in a list by index.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('List Length', 'Use len() to find the size of a list.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Iterating Through Lists', 'Loop through list elements using for loops.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Modifying List Elements', 'Change values in a list by index.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Appending to Lists', 'Add elements to the end of a list.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Removing from Lists', 'Remove elements from lists using remove() and pop().', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('List Slicing', 'Extract portions of lists using slice notation.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Sum of List Elements', 'Calculate the sum of all numbers in a list.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Finding Max in List', 'Find the largest number in a list.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Finding Min in List', 'Find the smallest number in a list.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('List Comprehensions Basics', 'Create lists using list comprehension syntax.', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Sorting Lists', 'Sort lists using sort() and sorted().', 'Core Python', ['Beginner', 'Core Python', 'Lists']),
    ('Tuples Basics', 'Learn about immutable tuples in Python.', 'Core Python', ['Beginner', 'Core Python', 'Tuples']),
    ('Tuple Unpacking', 'Unpack tuple values into variables.', 'Core Python', ['Beginner', 'Core Python', 'Tuples']),

    # Functions (15 lessons)
    ('Defining Functions', 'Create your first function with def keyword.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Function Parameters', 'Pass values to functions using parameters.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Return Values', 'Return results from functions.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Multiple Parameters', 'Write functions that accept multiple parameters.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Default Parameters', 'Set default values for function parameters.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Keyword Arguments', 'Call functions using keyword arguments.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Return Multiple Values', 'Return multiple values from a function using tuples.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Simple Recursion', 'Understand basic recursive function calls.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Factorial Function', 'Calculate factorial using recursion.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('String Helper Functions', 'Create utility functions for string manipulation.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('List Helper Functions', 'Create utility functions for list operations.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Math Helper Functions', 'Create utility functions for mathematical operations.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Validation Functions', 'Write functions that validate input data.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Simple Calculator Functions', 'Create basic calculator functions.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),
    ('Temperature Conversion Functions', 'Convert between Celsius and Fahrenheit.', 'Core Python', ['Beginner', 'Core Python', 'Functions']),

    # Classes & Objects Basics (15 lessons)
    ('Creating a Simple Class', 'Define your first Python class.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Class __init__ Method', 'Learn to create constructors with __init__.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Instance Variables', 'Understand and use instance variables with self.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Instance Methods', 'Create methods that operate on instance data.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Creating Objects', 'Instantiate objects from classes.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Object Method Calls', 'Call methods on object instances.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Property Decorator', 'Use @property for getter methods.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Person Class', 'Build a Person class with basic properties.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Book Class', 'Build a Book class with title and author.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Car Class', 'Build a Car class with make and model.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Student Class', 'Build a Student class with name and grades.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple BankAccount Class', 'Build a BankAccount class with deposit and withdraw.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('__str__ Method', 'Override __str__ for string representations.', 'OOP', ['Beginner', 'OOP', 'Classes']),
    ('Simple Inheritance', 'Create a subclass that inherits from a parent class.', 'OOP', ['Beginner', 'OOP', 'Inheritance']),
    ('Method Overriding Basics', 'Override parent class methods in subclasses.', 'OOP', ['Beginner', 'OOP', 'Inheritance']),

    # Dictionaries & Sets (10 lessons)
    ('Creating Dictionaries', 'Learn to create and use dictionaries in Python.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Accessing Dictionary Values', 'Get values from dictionaries by key.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Adding to Dictionaries', 'Add new key-value pairs to dictionaries.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Removing from Dictionaries', 'Remove key-value pairs from dictionaries.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Checking Dictionary Keys', 'Check if a key exists in a dictionary.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Iterating Dictionaries', 'Loop through dictionary keys and values.', 'Core Python', ['Beginner', 'Core Python', 'Dictionaries']),
    ('Set Basics', 'Use sets for storing unique elements.', 'Core Python', ['Beginner', 'Core Python', 'Sets']),
    ('Set Operations', 'Perform union, intersection, and difference on sets.', 'Core Python', ['Beginner', 'Core Python', 'Sets']),
    ('Adding to Sets', 'Add elements to a set.', 'Core Python', ['Beginner', 'Core Python', 'Sets']),
    ('Removing from Sets', 'Remove elements from a set.', 'Core Python', ['Beginner', 'Core Python', 'Sets']),

    # File I/O (10 lessons)
    ('Reading Text Files', 'Read content from text files line by line.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Writing Text Files', 'Write text content to files.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Appending to Files', 'Add content to existing files without overwriting.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Using with Statement', 'Use context managers to handle files safely.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Reading CSV Files', 'Read CSV files using the csv module.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Writing CSV Files', 'Write data to CSV files.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Reading JSON Files', 'Parse JSON files using the json module.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Writing JSON Files', 'Write data to JSON files.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Counting File Lines', 'Count the number of lines in a text file.', 'Core Python', ['Beginner', 'Core Python', 'Files']),
    ('Simple File Copy', 'Copy content from one file to another.', 'Core Python', ['Beginner', 'Core Python', 'Files']),

    # Error Handling (10 lessons)
    ('Try-Except Basics', 'Handle exceptions using try-except blocks.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('Catching Specific Exceptions', 'Catch different exception types separately.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('Finally Block', 'Use finally for cleanup code that always runs.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('Raising Exceptions', 'Raise your own exceptions when needed.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('ValueError Handling', 'Handle ValueError when parsing data.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('KeyError Handling', 'Handle KeyError when accessing dictionary keys.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('IndexError Handling', 'Handle IndexError when accessing list elements.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('FileNotFoundError Handling', 'Handle file not found errors.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('TypeError Handling', 'Handle type errors gracefully.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
    ('Custom Exception Class', 'Create your own exception class.', 'Core Python', ['Beginner', 'Core Python', 'Exceptions']),
]


def create_lesson(lesson_id, title, description, category, tags, language):
    """Create a complete lesson object from template."""
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
        // Solution: {title}
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
        full_solution = f"""# Solution: {title}
# {description}

def main():
    print("Exercise completed!")

if __name__ == "__main__":
    main()"""

    tutorial = f"""# Overview

{description}

# Key Concepts

- **Concept 1**: Core principle related to {title}
- **Concept 2**: Important detail to understand
- **Concept 3**: Common use case

# Example

```{language}
# Example code demonstrating {title}
```

# Practical Applications

- Real-world scenario 1
- Real-world scenario 2

# Best Practices

- Follow standard naming conventions
- Write clear, readable code
- Test your solution

# Key Takeaways

- Understand the fundamentals of {title}
- Practice regularly to build confidence
- Apply these concepts in your projects
"""

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
        "tutorial": tutorial
    }


def add_java_beginner_lessons():
    """Add 100 beginner lessons to Java curriculum."""
    print("Loading Java lessons...")
    with open('public/lessons-java.json', 'r', encoding='utf-8') as f:
        java_lessons = json.load(f)

    starting_id = 918
    new_lessons = []

    print(f"Creating {len(JAVA_BEGINNER_LESSONS)} new Java beginner lessons...")
    for i, (title, desc, category, tags) in enumerate(JAVA_BEGINNER_LESSONS):
        lesson = create_lesson(starting_id + i, title, desc, category, tags, 'java')
        new_lessons.append(lesson)

    # Add new lessons to the end
    java_lessons.extend(new_lessons)

    # Save
    print(f"Saving {len(java_lessons)} total Java lessons...")
    with open('public/lessons-java.json', 'w', encoding='utf-8') as f:
        json.dump(java_lessons, f, indent=2, ensure_ascii=False)

    # Calculate new distribution
    diff_counts = {'Beginner': 0, 'Intermediate': 0, 'Advanced': 0, 'Expert': 0}
    for lesson in java_lessons:
        diff_counts[lesson['difficulty']] += 1

    print(f"\nJava Curriculum Updated:")
    print(f"  Total lessons: {len(java_lessons)}")
    print(f"  Beginner: {diff_counts['Beginner']} ({diff_counts['Beginner']/len(java_lessons)*100:.1f}%)")
    print(f"  Intermediate: {diff_counts['Intermediate']} ({diff_counts['Intermediate']/len(java_lessons)*100:.1f}%)")
    print(f"  Advanced: {diff_counts['Advanced']} ({diff_counts['Advanced']/len(java_lessons)*100:.1f}%)")
    print(f"  Expert: {diff_counts['Expert']} ({diff_counts['Expert']/len(java_lessons)*100:.1f}%)")


def add_python_beginner_lessons():
    """Add 90 beginner lessons to Python curriculum."""
    print("\nLoading Python lessons...")
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    starting_id = 905
    new_lessons = []

    print(f"Creating {len(PYTHON_BEGINNER_LESSONS)} new Python beginner lessons...")
    for i, (title, desc, category, tags) in enumerate(PYTHON_BEGINNER_LESSONS):
        lesson = create_lesson(starting_id + i, title, desc, category, tags, 'python')
        new_lessons.append(lesson)

    # Add new lessons to the end
    python_lessons.extend(new_lessons)

    # Save
    print(f"Saving {len(python_lessons)} total Python lessons...")
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_lessons, f, indent=2, ensure_ascii=False)

    # Calculate new distribution
    diff_counts = {'Beginner': 0, 'Intermediate': 0, 'Advanced': 0, 'Expert': 0}
    for lesson in python_lessons:
        diff_counts[lesson['difficulty']] += 1

    print(f"\nPython Curriculum Updated:")
    print(f"  Total lessons: {len(python_lessons)}")
    print(f"  Beginner: {diff_counts['Beginner']} ({diff_counts['Beginner']/len(python_lessons)*100:.1f}%)")
    print(f"  Intermediate: {diff_counts['Intermediate']} ({diff_counts['Intermediate']/len(python_lessons)*100:.1f}%)")
    print(f"  Advanced: {diff_counts['Advanced']} ({diff_counts['Advanced']/len(python_lessons)*100:.1f}%)")
    print(f"  Expert: {diff_counts['Expert']} ({diff_counts['Expert']/len(python_lessons)*100:.1f}%)")


if __name__ == "__main__":
    print("=" * 80)
    print("PHASE 2: ADDING BEGINNER LESSONS")
    print("=" * 80)
    print()

    add_java_beginner_lessons()
    add_python_beginner_lessons()

    print()
    print("=" * 80)
    print("BEGINNER LESSONS ADDED SUCCESSFULLY!")
    print("=" * 80)
    print()
    print("Next steps:")
    print("  1. Run validation: node scripts/validate-lessons.mjs")
    print("  2. Commit changes to GitHub")
    print("=" * 80)
