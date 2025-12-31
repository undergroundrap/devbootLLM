#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 46: ArrayDeque as Stack (Basic)
lesson46 = next(l for l in lessons if l['id'] == 46)
lesson46['fullSolution'] = '''"""
ArrayDeque as Stack (Basic) - Stack Operations

Master stack data structure using collections.deque.
Essential for Last-In-First-Out (LIFO) operations.

**Zero Package Installation Required**
"""

from collections import deque

# Example 1: Basic Stack Operations
print("="*70)
print("Example 1: Push and Pop")
print("="*70)

stack = deque()

# Push items
stack.append(10)
stack.append(20)
stack.append(30)

print(f"Stack after pushes: {list(stack)}")

# Pop items
top = stack.pop()
print(f"Popped: {top}")
print(f"Stack after pop: {list(stack)}")

# Example 2: Stack as Function Call History
print("\\n" + "="*70)
print("Example 2: Function Call Stack")
print("="*70)

call_stack = deque()

def function_a():
    call_stack.append("function_a")
    print(f"  Called: function_a")
    function_b()
    call_stack.pop()

def function_b():
    call_stack.append("function_b")
    print(f"  Called: function_b")
    print(f"  Call stack: {list(call_stack)}")
    call_stack.pop()

function_a()

# Example 3: Check if Empty
print("\\n" + "="*70)
print("Example 3: Empty Stack Check")
print("="*70)

stack = deque()

if not stack:
    print("Stack is empty")

stack.append(1)
if stack:
    print(f"Stack has items: {list(stack)}")

# Example 4: Peek at Top
print("\\n" + "="*70)
print("Example 4: Peek Without Removing")
print("="*70)

stack = deque([1, 2, 3, 4, 5])

print(f"Stack: {list(stack)}")
if stack:
    top = stack[-1]
    print(f"Top element: {top}")
    print(f"Stack unchanged: {list(stack)}")

# Example 5: Stack Size
print("\\n" + "="*70)
print("Example 5: Get Stack Size")
print("="*70)

stack = deque([10, 20, 30])

print(f"Stack: {list(stack)}")
print(f"Size: {len(stack)}")

stack.append(40)
print(f"After push, size: {len(stack)}")

# Example 6: Reverse String
print("\\n" + "="*70)
print("Example 6: Reverse with Stack")
print("="*70)

text = "hello"
stack = deque()

# Push all characters
for char in text:
    stack.append(char)

# Pop to reverse
reversed_text = ""
while stack:
    reversed_text += stack.pop()

print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# Example 7: Undo Operations
print("\\n" + "="*70)
print("Example 7: Undo Stack")
print("="*70)

undo_stack = deque()
current_state = 0

def perform_action(change):
    global current_state
    undo_stack.append(current_state)
    current_state += change
    print(f"  Action: +{change}, State: {current_state}")

def undo():
    global current_state
    if undo_stack:
        current_state = undo_stack.pop()
        print(f"  Undo -> State: {current_state}")
    else:
        print("  Nothing to undo")

perform_action(10)
perform_action(5)
perform_action(-3)
undo()
undo()

# Example 8: Balanced Parentheses
print("\\n" + "="*70)
print("Example 8: Check Balanced Brackets")
print("="*70)

def is_balanced(expression):
    stack = deque()

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0

test1 = "((()))"
test2 = "(()"

print(f"'{test1}' balanced: {is_balanced(test1)}")
print(f"'{test2}' balanced: {is_balanced(test2)}")

# Example 9: Clear Stack
print("\\n" + "="*70)
print("Example 9: Clear All Items")
print("="*70)

stack = deque([1, 2, 3, 4, 5])
print(f"Stack: {list(stack)}")

stack.clear()
print(f"After clear: {list(stack)}")
print(f"Is empty: {len(stack) == 0}")

# Example 10: Stack from List
print("\\n" + "="*70)
print("Example 10: Initialize from List")
print("="*70)

items = [1, 2, 3, 4, 5]
stack = deque(items)

print(f"Created stack: {list(stack)}")
print(f"Pop order:")
while stack:
    print(f"  {stack.pop()}")

print("\\n" + "="*70)
print("ArrayDeque Stack Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use deque for efficient stack")
print("  - append() to push")
print("  - pop() to pop (from right)")
print("  - Last-In-First-Out (LIFO)")
print("  - O(1) push and pop operations")
'''

# Lesson 47: List Comprehensions Basics
lesson47 = next(l for l in lessons if l['id'] == 47)
lesson47['fullSolution'] = '''"""
List Comprehensions Basics - Elegant List Creation

Master list comprehensions for concise list creation.
Modern Pythonic way to transform and filter sequences.

**Zero Package Installation Required**
"""

# Example 1: Basic List Comprehension
print("="*70)
print("Example 1: Square Numbers")
print("="*70)

# Traditional way
squares_old = []
for i in range(5):
    squares_old.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(5)]

print(f"Traditional: {squares_old}")
print(f"Comprehension: {squares}")

# Example 2: Transform Strings
print("\\n" + "="*70)
print("Example 2: Uppercase Names")
print("="*70)

names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]

print(f"Original: {names}")
print(f"Uppercase: {upper_names}")

# Example 3: With Condition (Filter)
print("\\n" + "="*70)
print("Example 3: Filter Even Numbers")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]

print(f"Numbers: {numbers}")
print(f"Evens: {evens}")

# Example 4: Multiple Operations
print("\\n" + "="*70)
print("Example 4: Double and Filter")
print("="*70)

values = [1, 2, 3, 4, 5]
doubled_evens = [n * 2 for n in values if n % 2 == 0]

print(f"Values: {values}")
print(f"Doubled evens: {doubled_evens}")

# Example 5: String Operations
print("\\n" + "="*70)
print("Example 5: Extract First Letters")
print("="*70)

words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]

print(f"Words: {words}")
print(f"First letters: {first_letters}")

# Example 6: Range with Transformation
print("\\n" + "="*70)
print("Example 6: Create Custom Range")
print("="*70)

# Multiples of 5
multiples = [i * 5 for i in range(1, 6)]

print(f"Multiples of 5: {multiples}")

# Example 7: Filter Strings by Length
print("\\n" + "="*70)
print("Example 7: Long Words Only")
print("="*70)

words = ["hi", "hello", "hey", "greetings"]
long_words = [word for word in words if len(word) >= 5]

print(f"All words: {words}")
print(f"Long words (>=5): {long_words}")

# Example 8: Nested Comprehension
print("\\n" + "="*70)
print("Example 8: Flatten 2D List")
print("="*70)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]

print(f"Matrix: {matrix}")
print(f"Flattened: {flat}")

# Example 9: Conditional Expression
print("\\n" + "="*70)
print("Example 9: Map Values")
print("="*70)

numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(f"Numbers: {numbers}")
print(f"Labels: {labels}")

# Example 10: Combine Lists
print("\\n" + "="*70)
print("Example 10: Pair Elements")
print("="*70)

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
pairs = [f"{letter}{num}" for letter, num in zip(letters, numbers)]

print(f"Letters: {letters}")
print(f"Numbers: {numbers}")
print(f"Pairs: {pairs}")

print("\\n" + "="*70)
print("List Comprehensions Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - [expr for item in iterable]")
print("  - [expr for item in iterable if condition]")
print("  - More concise than loops")
print("  - Faster for simple transformations")
print("  - Pythonic and readable")
'''

# Lesson 48: Lists Basics
lesson48 = next(l for l in lessons if l['id'] == 48)
lesson48['fullSolution'] = '''"""
Lists Basics - Python List Fundamentals

Master the fundamentals of Python lists.
Essential data structure for ordered collections.

**Zero Package Installation Required**
"""

# Example 1: Creating Lists
print("="*70)
print("Example 1: Different Ways to Create Lists")
print("="*70)

# Empty list
empty = []
print(f"Empty: {empty}")

# List with items
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Mixed types
mixed = [1, "hello", 3.14, True]
print(f"Mixed types: {mixed}")

# Example 2: List Length
print("\\n" + "="*70)
print("Example 2: Get List Size")
print("="*70)

fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")
print(f"Length: {len(fruits)}")

# Example 3: Check if Item Exists
print("\\n" + "="*70)
print("Example 3: Membership Test")
print("="*70)

colors = ["red", "green", "blue"]

print(f"Colors: {colors}")
print(f"'red' in list: {'red' in colors}")
print(f"'yellow' in list: {'yellow' in colors}")

# Example 4: List Methods Overview
print("\\n" + "="*70)
print("Example 4: Common List Methods")
print("="*70)

items = [1, 2, 3]
print(f"Original: {items}")

items.append(4)
print(f"After append(4): {items}")

items.insert(0, 0)
print(f"After insert(0, 0): {items}")

items.remove(2)
print(f"After remove(2): {items}")

# Example 5: List Slicing Basics
print("\\n" + "="*70)
print("Example 5: Get Sublist")
print("="*70)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Full list: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle: {numbers[3:7]}")

# Example 6: List Concatenation
print("\\n" + "="*70)
print("Example 6: Combine Lists")
print("="*70)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Combined: {combined}")

# Example 7: List Repetition
print("\\n" + "="*70)
print("Example 7: Repeat List")
print("="*70)

pattern = [0, 1]
repeated = pattern * 3

print(f"Pattern: {pattern}")
print(f"Repeated x3: {repeated}")

# Example 8: List Copying
print("\\n" + "="*70)
print("Example 8: Copy vs Reference")
print("="*70)

original = [1, 2, 3]
reference = original  # Same object
copy = original.copy()  # New object

original[0] = 999

print(f"Original: {original}")
print(f"Reference: {reference}")  # Changed!
print(f"Copy: {copy}")  # Unchanged

# Example 9: Count Occurrences
print("\\n" + "="*70)
print("Example 9: Count Items")
print("="*70)

items = [1, 2, 2, 3, 2, 4, 2]

print(f"Items: {items}")
print(f"Count of 2: {items.count(2)}")
print(f"Count of 5: {items.count(5)}")

# Example 10: Clear List
print("\\n" + "="*70)
print("Example 10: Remove All Items")
print("="*70)

data = [1, 2, 3, 4, 5]
print(f"Before clear: {data}")

data.clear()
print(f"After clear: {data}")
print(f"Is empty: {len(data) == 0}")

print("\\n" + "="*70)
print("Lists Basics Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Lists are ordered and mutable")
print("  - Created with []")
print("  - Can hold any type")
print("  - Many built-in methods")
print("  - Zero-indexed")
print("  - Most versatile data structure")
'''

# Lesson 49: Appending to Lists
lesson49 = next(l for l in lessons if l['id'] == 49)
lesson49['fullSolution'] = '''"""
Appending to Lists - Adding Elements

Master adding elements to lists with append and extend.
Essential for building and growing collections.

**Zero Package Installation Required**
"""

# Example 1: Basic Append
print("="*70)
print("Example 1: Add Single Item")
print("="*70)

fruits = ["apple", "banana"]
print(f"Original: {fruits}")

fruits.append("cherry")
print(f"After append: {fruits}")

fruits.append("date")
print(f"After another: {fruits}")

# Example 2: Append in Loop
print("\\n" + "="*70)
print("Example 2: Build List with Loop")
print("="*70)

squares = []
for i in range(5):
    squares.append(i ** 2)

print(f"Squares: {squares}")

# Example 3: Append vs Extend
print("\\n" + "="*70)
print("Example 3: Append vs Extend")
print("="*70)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

list1.append([4, 5])
list2.extend([4, 5])

print(f"Append [4,5]: {list1}")
print(f"Extend [4,5]: {list2}")

# Example 4: Collect User Data
print("\\n" + "="*70)
print("Example 4: Accumulate Items")
print("="*70)

names = []
inputs = ["Alice", "Bob", "Charlie"]

for name in inputs:
    names.append(name)
    print(f"  Added {name}, list: {names}")

# Example 5: Append Different Types
print("\\n" + "="*70)
print("Example 5: Mixed Type List")
print("="*70)

data = []
data.append(42)
data.append("hello")
data.append(3.14)
data.append(True)

print(f"Mixed data: {data}")

# Example 6: Build List of Dictionaries
print("\\n" + "="*70)
print("Example 6: Append Objects")
print("="*70)

users = []
users.append({"name": "Alice", "age": 25})
users.append({"name": "Bob", "age": 30})

print("Users:")
for user in users:
    print(f"  {user}")

# Example 7: Conditional Append
print("\\n" + "="*70)
print("Example 7: Selective Appending")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Even numbers: {evens}")

# Example 8: Append Multiple Lists
print("\\n" + "="*70)
print("Example 8: Extend with Multiple")
print("="*70)

result = [1, 2, 3]
print(f"Start: {result}")

result.extend([4, 5])
print(f"Extend [4,5]: {result}")

result.extend([6, 7, 8])
print(f"Extend [6,7,8]: {result}")

# Example 9: Chain Appends
print("\\n" + "="*70)
print("Example 9: Multiple Appends")
print("="*70)

items = []
items.append(1)
items.append(2)
items.append(3)

print(f"After 3 appends: {items}")

# Example 10: Performance Tip
print("\\n" + "="*70)
print("Example 10: Append is O(1)")
print("="*70)

# Efficient: append is fast
large_list = []
for i in range(1000):
    large_list.append(i)

print(f"Created list of {len(large_list)} items")
print(f"First 10: {large_list[:10]}")

print("\\n" + "="*70)
print("Appending to Lists Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - append(item) adds one element")
print("  - extend(iterable) adds multiple")
print("  - append is O(1) - very fast")
print("  - Build lists incrementally")
print("  - Can append any type")
'''

# Lesson 50: Array Searching
lesson50 = next(l for l in lessons if l['id'] == 50)
lesson50['fullSolution'] = '''"""
Array Searching - Linear vs Binary Approaches

Master searching algorithms for finding elements.
Essential for data retrieval and algorithm understanding.

**Zero Package Installation Required**
"""

# Example 1: Linear Search
print("="*70)
print("Example 1: Sequential Search")
print("="*70)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [10, 23, 45, 12, 67, 34]
target = 45

index = linear_search(numbers, target)
print(f"Array: {numbers}")
print(f"Searching for: {target}")
print(f"Found at index: {index}")

# Example 2: Linear Search All Occurrences
print("\\n" + "="*70)
print("Example 2: Find All Matches")
print("="*70)

def find_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

data = [1, 2, 3, 2, 4, 2, 5]
positions = find_all(data, 2)

print(f"Data: {data}")
print(f"All positions of 2: {positions}")

# Example 3: Binary Search (Sorted Array)
print("\\n" + "="*70)
print("Example 3: Binary Search")
print("="*70)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"  Checking index {mid}: {arr[mid]}")

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

sorted_nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

print(f"Sorted array: {sorted_nums}")
print(f"Searching for: {target}")
index = binary_search(sorted_nums, target)
print(f"Found at index: {index}")

# Example 4: Search with in Operator
print("\\n" + "="*70)
print("Example 4: Python's Built-in Search")
print("="*70)

items = ["apple", "banana", "cherry"]

if "banana" in items:
    print("Found banana!")

if "grape" not in items:
    print("Grape not in list")

# Example 5: index() Method
print("\\n" + "="*70)
print("Example 5: Using .index()")
print("="*70)

colors = ["red", "green", "blue", "yellow"]

try:
    index = colors.index("blue")
    print(f"Blue found at index: {index}")
except ValueError:
    print("Color not found")

# Example 6: Search with Condition
print("\\n" + "="*70)
print("Example 6: Find First Match")
print("="*70)

def find_first_even(numbers):
    for i, num in enumerate(numbers):
        if num % 2 == 0:
            return i
    return -1

nums = [1, 3, 5, 8, 9, 11]
index = find_first_even(nums)

print(f"Numbers: {nums}")
print(f"First even at index: {index}")

# Example 7: Performance Comparison
print("\\n" + "="*70)
print("Example 7: Linear vs Binary")
print("="*70)

import time

large_list = list(range(10000))
target = 9999

# Linear
start = time.time()
linear_search(large_list, target)
linear_time = time.time() - start

# Binary
start = time.time()
binary_search(large_list, target)
binary_time = time.time() - start

print(f"Linear search: {linear_time:.6f}s")
print(f"Binary search: {binary_time:.6f}s")
print(f"Binary is faster for sorted data!")

# Example 8: Search in 2D Array
print("\\n" + "="*70)
print("Example 8: Matrix Search")
print("="*70)

def search_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return None

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

position = search_matrix(grid, 5)
print(f"Grid: {grid}")
print(f"Position of 5: {position}")

# Example 9: Custom Comparison
print("\\n" + "="*70)
print("Example 9: Search Objects")
print("="*70)

users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]

def find_user(users, name):
    for i, user in enumerate(users):
        if user["name"] == name:
            return i
    return -1

index = find_user(users, "Bob")
print(f"Bob found at index: {index}")

# Example 10: Early Exit Optimization
print("\\n" + "="*70)
print("Example 10: Stop When Found")
print("="*70)

def search_with_logging(arr, target):
    checks = 0
    for i in range(len(arr)):
        checks += 1
        if arr[i] == target:
            print(f"  Found after {checks} checks")
            return i
    print(f"  Not found after {checks} checks")
    return -1

data = [5, 10, 15, 20, 25, 30]
search_with_logging(data, 15)
search_with_logging(data, 99)

print("\\n" + "="*70)
print("Array Searching Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Linear search: O(n), works on any list")
print("  - Binary search: O(log n), needs sorted list")
print("  - Use 'in' operator for simple checks")
print("  - .index() raises ValueError if not found")
print("  - Choose algorithm based on data")
'''

# Save all changes
for lesson in [lesson46, lesson47, lesson48, lesson49, lesson50]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 46-50:")
print(f"  46: ArrayDeque as Stack - {len(lesson46['fullSolution'])} chars")
print(f"  47: List Comprehensions - {len(lesson47['fullSolution'])} chars")
print(f"  48: Lists Basics - {len(lesson48['fullSolution'])} chars")
print(f"  49: Appending to Lists - {len(lesson49['fullSolution'])} chars")
print(f"  50: Array Searching - {len(lesson50['fullSolution'])} chars")
print("\\nBatch 46-50 complete!")
print("\\nFirst 50 Python lessons now fully upgraded!")
