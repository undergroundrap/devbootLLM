#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 56: Iterating Through Lists
lesson56 = next(l for l in lessons if l['id'] == 56)
lesson56['fullSolution'] = '''"""
Iterating Through Lists - Loop Over Elements

Master different ways to loop through list elements.
Essential for processing collections.

**Zero Package Installation Required**
"""

# Example 1: Basic For Loop
print("="*70)
print("Example 1: Simple Iteration")
print("="*70)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"  {fruit}")

# Example 2: With Index (enumerate)
print("\\n" + "="*70)
print("Example 2: Iterate with Index")
print("="*70)

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# Example 3: Start Index at 1
print("\\n" + "="*70)
print("Example 3: Custom Start Index")
print("="*70)

tasks = ["Task A", "Task B", "Task C"]

for i, task in enumerate(tasks, start=1):
    print(f"  {i}. {task}")

# Example 4: Index-Based Loop
print("\\n" + "="*70)
print("Example 4: Loop with range()")
print("="*70)

numbers = [10, 20, 30, 40, 50]

for i in range(len(numbers)):
    print(f"  Index {i}: {numbers[i]}")

# Example 5: Process Each Element
print("\\n" + "="*70)
print("Example 5: Transform While Iterating")
print("="*70)

values = [1, 2, 3, 4, 5]

print("Doubling each value:")
for value in values:
    doubled = value * 2
    print(f"  {value} * 2 = {doubled}")

# Example 6: Accumulate While Iterating
print("\\n" + "="*70)
print("Example 6: Running Total")
print("="*70)

prices = [10.99, 5.99, 15.99, 8.99]
total = 0

print("Adding prices:")
for price in prices:
    total += price
    print(f"  +${price:.2f} = ${total:.2f}")

# Example 7: Conditional Processing
print("\\n" + "="*70)
print("Example 7: Filter While Iterating")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(f"  {num}")

# Example 8: Iterate Backwards
print("\\n" + "="*70)
print("Example 8: Reverse Iteration")
print("="*70)

items = ["first", "second", "third"]

print("Reverse order:")
for item in reversed(items):
    print(f"  {item}")

# Example 9: Nested Iteration
print("\\n" + "="*70)
print("Example 9: Iterate 2D List")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix values:")
for row in matrix:
    for value in row:
        print(f"  {value}", end=" ")
    print()

# Example 10: Iterate Multiple Lists
print("\\n" + "="*70)
print("Example 10: Zip Multiple Lists")
print("="*70)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("People:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

print("\\n" + "="*70)
print("Iterating Through Lists Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - for item in list: is simplest")
print("  - enumerate() for index + value")
print("  - range(len()) for index-based")
print("  - reversed() for backwards")
print("  - zip() for parallel iteration")
'''

# Lesson 57: List Comprehensions
lesson57 = next(l for l in lessons if l['id'] == 57)
lesson57['fullSolution'] = '''"""
List Comprehensions - Advanced

Master advanced list comprehension patterns.
Powerful technique for concise data transformation.

**Zero Package Installation Required**
"""

# Example 1: Basic Comprehension
print("="*70)
print("Example 1: Transform List")
print("="*70)

numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Example 2: With Filter
print("\\n" + "="*70)
print("Example 2: Filter and Transform")
print("="*70)

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [n**2 for n in values if n % 2 == 0]

print(f"Values: {values}")
print(f"Even squares: {even_squares}")

# Example 3: String Operations
print("\\n" + "="*70)
print("Example 3: Process Strings")
print("="*70)

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
lengths = [len(word) for word in words]

print(f"Words: {words}")
print(f"Uppercase: {upper_words}")
print(f"Lengths: {lengths}")

# Example 4: Conditional Expression
print("\\n" + "="*70)
print("Example 4: If-Else in Comprehension")
print("="*70)

numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Example 5: Nested Comprehension
print("\\n" + "="*70)
print("Example 5: Flatten Matrix")
print("="*70)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]

print(f"Matrix: {matrix}")
print(f"Flattened: {flat}")

# Example 6: Generate Pairs
print("\\n" + "="*70)
print("Example 6: Cartesian Product")
print("="*70)

colors = ["red", "green"]
sizes = ["S", "M", "L"]
combinations = [f"{color}-{size}" for color in colors for size in sizes]

print(f"Colors: {colors}")
print(f"Sizes: {sizes}")
print(f"Combinations: {combinations}")

# Example 7: Parse Data
print("\\n" + "="*70)
print("Example 7: Extract Values")
print("="*70)

data = ["10", "20", "30", "40"]
numbers = [int(x) for x in data]

print(f"Strings: {data}")
print(f"Integers: {numbers}")

# Example 8: Dictionary to List
print("\\n" + "="*70)
print("Example 8: Extract Dict Values")
print("="*70)

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]

names = [user["name"] for user in users]
ages = [user["age"] for user in users]

print("Users:", users)
print(f"Names: {names}")
print(f"Ages: {ages}")

# Example 9: Complex Filter
print("\\n" + "="*70)
print("Example 9: Multiple Conditions")
print("="*70)

numbers = range(1, 21)
filtered = [n for n in numbers if n % 2 == 0 if n > 10]

print(f"Range: 1-20")
print(f"Even and >10: {filtered}")

# Example 10: Function in Comprehension
print("\\n" + "="*70)
print("Example 10: Apply Function")
print("="*70)

def square_if_even(n):
    return n**2 if n % 2 == 0 else n

numbers = [1, 2, 3, 4, 5]
result = [square_if_even(n) for n in numbers]

print(f"Numbers: {numbers}")
print(f"Result: {result}")

print("\\n" + "="*70)
print("List Comprehensions Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - [expr for item in list]")
print("  - Add if for filtering")
print("  - Use if-else for mapping")
print("  - Can nest comprehensions")
print("  - More concise than loops")
'''

# Lesson 58: List Helper Functions
lesson58 = next(l for l in lessons if l['id'] == 58)
lesson58['fullSolution'] = '''"""
List Helper Functions - Built-in Utilities

Master Python's built-in list functions.
Essential tools for list manipulation.

**Zero Package Installation Required**
"""

# Example 1: len() - List Length
print("="*70)
print("Example 1: Get Length")
print("="*70)

fruits = ["apple", "banana", "cherry"]
count = len(fruits)

print(f"Fruits: {fruits}")
print(f"Count: {count}")

# Example 2: sum() - Add Numbers
print("\\n" + "="*70)
print("Example 2: Sum Values")
print("="*70)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)

print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 3: max() and min()
print("\\n" + "="*70)
print("Example 3: Maximum and Minimum")
print("="*70)

scores = [85, 92, 78, 95, 88]
highest = max(scores)
lowest = min(scores)

print(f"Scores: {scores}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Example 4: sorted() - Sort List
print("\\n" + "="*70)
print("Example 4: Sort List")
print("="*70)

numbers = [5, 2, 8, 1, 9]
sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)

print(f"Original: {numbers}")
print(f"Ascending: {sorted_asc}")
print(f"Descending: {sorted_desc}")

# Example 5: reversed() - Reverse Order
print("\\n" + "="*70)
print("Example 5: Reverse List")
print("="*70)

items = [1, 2, 3, 4, 5]
reversed_items = list(reversed(items))

print(f"Original: {items}")
print(f"Reversed: {reversed_items}")

# Example 6: enumerate() - Index + Value
print("\\n" + "="*70)
print("Example 6: Enumerate Items")
print("="*70)

colors = ["red", "green", "blue"]

print("With indices:")
for i, color in enumerate(colors):
    print(f"  {i}: {color}")

# Example 7: zip() - Combine Lists
print("\\n" + "="*70)
print("Example 7: Zip Multiple Lists")
print("="*70)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("Combined:")
for name, age in zip(names, ages):
    print(f"  {name}: {age}")

# Example 8: all() and any()
print("\\n" + "="*70)
print("Example 8: Boolean Checks")
print("="*70)

all_positive = [1, 2, 3, 4, 5]
has_negative = [1, -2, 3, 4, 5]

print(f"All positive? {all(n > 0 for n in all_positive)}")
print(f"Has negative? {any(n < 0 for n in has_negative)}")

# Example 9: filter() - Filter Items
print("\\n" + "="*70)
print("Example 9: Filter Function")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Numbers: {numbers}")
print(f"Evens: {evens}")

# Example 10: map() - Transform Items
print("\\n" + "="*70)
print("Example 10: Map Function")
print("="*70)

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

print("\\n" + "="*70)
print("List Helper Functions Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - len() for size")
print("  - sum() for total")
print("  - max()/min() for extremes")
print("  - sorted() for ordering")
print("  - enumerate(), zip() for iteration")
print("  - filter(), map() for transformation")
'''

# Lesson 59: List Indexing & len()
lesson59 = next(l for l in lessons if l['id'] == 59)
lesson59['fullSolution'] = '''"""
List Indexing & len() - Access and Size

Master list indexing and length operations.
Foundation for list manipulation.

**Zero Package Installation Required**
"""

# Example 1: Positive Indexing
print("="*70)
print("Example 1: Access by Index")
print("="*70)

fruits = ["apple", "banana", "cherry", "date"]

print(f"List: {fruits}")
print(f"Index 0: {fruits[0]}")
print(f"Index 1: {fruits[1]}")
print(f"Index 2: {fruits[2]}")
print(f"Index 3: {fruits[3]}")

# Example 2: Negative Indexing
print("\\n" + "="*70)
print("Example 2: Access from End")
print("="*70)

numbers = [10, 20, 30, 40, 50]

print(f"List: {numbers}")
print(f"Last (index -1): {numbers[-1]}")
print(f"Second last (index -2): {numbers[-2]}")
print(f"Third last (index -3): {numbers[-3]}")

# Example 3: len() Function
print("\\n" + "="*70)
print("Example 3: Get List Length")
print("="*70)

colors = ["red", "green", "blue"]
size = len(colors)

print(f"Colors: {colors}")
print(f"Length: {size}")

# Example 4: Last Element with len()
print("\\n" + "="*70)
print("Example 4: Access Last with len()")
print("="*70)

items = ["a", "b", "c", "d", "e"]
last_index = len(items) - 1
last_item = items[last_index]

print(f"Items: {items}")
print(f"Length: {len(items)}")
print(f"Last index: {last_index}")
print(f"Last item: {last_item}")

# Example 5: Valid Index Check
print("\\n" + "="*70)
print("Example 5: Check Index Bounds")
print("="*70)

data = [1, 2, 3, 4, 5]
index = 3

if 0 <= index < len(data):
    print(f"Valid index {index}: {data[index]}")
else:
    print(f"Index {index} out of range")

# Example 6: Middle Element
print("\\n" + "="*70)
print("Example 6: Find Middle")
print("="*70)

values = [10, 20, 30, 40, 50]
middle_index = len(values) // 2
middle = values[middle_index]

print(f"Values: {values}")
print(f"Middle index: {middle_index}")
print(f"Middle value: {middle}")

# Example 7: Loop Using Length
print("\\n" + "="*70)
print("Example 7: Iterate with Indices")
print("="*70)

words = ["hello", "world", "python"]

for i in range(len(words)):
    print(f"  Index {i}: {words[i]}")

# Example 8: Modify by Index
print("\\n" + "="*70)
print("Example 8: Update Elements")
print("="*70)

scores = [70, 80, 90]
print(f"Original: {scores}")

scores[1] = 85  # Change second element
print(f"After update: {scores}")

# Example 9: Empty List Check
print("\\n" + "="*70)
print("Example 9: Check if Empty")
print("="*70)

empty = []
full = [1, 2, 3]

print(f"Empty list length: {len(empty)}")
print(f"Is empty? {len(empty) == 0}")
print(f"\\nFull list length: {len(full)}")
print(f"Is empty? {len(full) == 0}")

# Example 10: Slice with Length
print("\\n" + "="*70)
print("Example 10: Dynamic Slicing")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
half = len(numbers) // 2

first_half = numbers[:half]
second_half = numbers[half:]

print(f"Full list: {numbers}")
print(f"First half: {first_half}")
print(f"Second half: {second_half}")

print("\\n" + "="*70)
print("List Indexing & len() Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - list[i] accesses element at index i")
print("  - Indices start at 0")
print("  - Negative indices count from end")
print("  - len(list) returns size")
print("  - Last index is len(list) - 1")
'''

# Lesson 60: List Length
lesson60 = next(l for l in lessons if l['id'] == 60)
lesson60['fullSolution'] = '''"""
List Length - Size Operations

Master working with list length and size.
Essential for bounds checking and iteration.

**Zero Package Installation Required**
"""

# Example 1: Basic len()
print("="*70)
print("Example 1: Get List Size")
print("="*70)

fruits = ["apple", "banana", "cherry"]
length = len(fruits)

print(f"Fruits: {fruits}")
print(f"Length: {length}")

# Example 2: Empty vs Non-Empty
print("\\n" + "="*70)
print("Example 2: Check Empty")
print("="*70)

empty_list = []
full_list = [1, 2, 3]

print(f"Empty list: {empty_list}")
print(f"Length: {len(empty_list)}")
print(f"Is empty? {len(empty_list) == 0}")

print(f"\\nFull list: {full_list}")
print(f"Length: {len(full_list)}")
print(f"Is empty? {len(full_list) == 0}")

# Example 3: Length After Operations
print("\\n" + "="*70)
print("Example 3: Track Size Changes")
print("="*70)

items = []
print(f"Initial length: {len(items)}")

items.append("first")
print(f"After append: {len(items)}")

items.append("second")
print(f"After another append: {len(items)}")

items.remove("first")
print(f"After remove: {len(items)}")

# Example 4: Compare Lengths
print("\\n" + "="*70)
print("Example 4: Compare List Sizes")
print("="*70)

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

print(f"List 1: {list1} (length: {len(list1)})")
print(f"List 2: {list2} (length: {len(list2)})")

if len(list1) < len(list2):
    print("List 1 is shorter")
elif len(list1) > len(list2):
    print("List 1 is longer")
else:
    print("Same length")

# Example 5: Length in Loops
print("\\n" + "="*70)
print("Example 5: Use Length for Iteration")
print("="*70)

colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print(f"  Position {i} of {len(colors)-1}: {colors[i]}")

# Example 6: Capacity Check
print("\\n" + "="*70)
print("Example 6: Check if Room")
print("="*70)

max_size = 5
queue = [1, 2, 3]

print(f"Queue: {queue}")
print(f"Current size: {len(queue)}")
print(f"Max size: {max_size}")
print(f"Has room? {len(queue) < max_size}")

# Example 7: Split at Midpoint
print("\\n" + "="*70)
print("Example 7: Use Length to Split")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6]
mid = len(numbers) // 2

left = numbers[:mid]
right = numbers[mid:]

print(f"Full list: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Midpoint: {mid}")
print(f"Left half: {left}")
print(f"Right half: {right}")

# Example 8: Length-Based Conditions
print("\\n" + "="*70)
print("Example 8: Conditional Logic")
print("="*70)

def describe_list(lst):
    size = len(lst)
    if size == 0:
        return "Empty list"
    elif size == 1:
        return "Single item"
    elif size < 5:
        return "Small list"
    else:
        return "Large list"

print(describe_list([]))
print(describe_list([1]))
print(describe_list([1, 2, 3]))
print(describe_list([1, 2, 3, 4, 5, 6, 7]))

# Example 9: Valid Index Range
print("\\n" + "="*70)
print("Example 9: Index Validation")
print("="*70)

data = [10, 20, 30, 40]

def safe_get(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return None

print(f"Data: {data}")
print(f"Get index 2: {safe_get(data, 2)}")
print(f"Get index 10: {safe_get(data, 10)}")

# Example 10: Count Elements
print("\\n" + "="*70)
print("Example 10: Size Statistics")
print("="*70)

lists = [
    [1, 2],
    [1, 2, 3, 4],
    [1],
    [1, 2, 3]
]

print("List sizes:")
for i, lst in enumerate(lists):
    print(f"  List {i}: {len(lst)} elements")

total_elements = sum(len(lst) for lst in lists)
print(f"\\nTotal elements across all lists: {total_elements}")

print("\\n" + "="*70)
print("List Length Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - len(list) returns element count")
print("  - Returns 0 for empty lists")
print("  - Use for bounds checking")
print("  - Essential for safe indexing")
print("  - Helps with list operations")
'''

# Save all changes
for lesson in [lesson56, lesson57, lesson58, lesson59, lesson60]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 56-60:")
print(f"  56: Iterating Through Lists - {len(lesson56['fullSolution'])} chars")
print(f"  57: List Comprehensions - {len(lesson57['fullSolution'])} chars")
print(f"  58: List Helper Functions - {len(lesson58['fullSolution'])} chars")
print(f"  59: List Indexing & len() - {len(lesson59['fullSolution'])} chars")
print(f"  60: List Length - {len(lesson60['fullSolution'])} chars")
print("\\nBatch 56-60 complete!")
