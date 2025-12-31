#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 61: List Methods
lesson61 = next(l for l in lessons if l['id'] == 61)
lesson61['fullSolution'] = '''"""
List Methods - Built-in Operations

Master essential list methods for manipulation.
Complete toolkit for list operations.

**Zero Package Installation Required**
"""

# Example 1: append() - Add to End
print("="*70)
print("Example 1: Append Items")
print("="*70)

fruits = ["apple", "banana"]
print(f"Initial: {fruits}")

fruits.append("cherry")
print(f"After append: {fruits}")

fruits.append("date")
print(f"After another: {fruits}")

# Example 2: insert() - Add at Position
print("\\n" + "="*70)
print("Example 2: Insert at Index")
print("="*70)

numbers = [1, 2, 4, 5]
print(f"Original: {numbers}")

numbers.insert(2, 3)  # Insert 3 at index 2
print(f"After insert(2, 3): {numbers}")

# Example 3: extend() - Add Multiple Items
print("\\n" + "="*70)
print("Example 3: Extend with Another List")
print("="*70)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

list1.extend(list2)
print(f"After extend: {list1}")

# Example 4: remove() - Delete First Match
print("\\n" + "="*70)
print("Example 4: Remove by Value")
print("="*70)

colors = ["red", "green", "blue", "green"]
print(f"Original: {colors}")

colors.remove("green")  # Removes first "green"
print(f"After remove('green'): {colors}")

# Example 5: pop() - Remove and Return
print("\\n" + "="*70)
print("Example 5: Pop Items")
print("="*70)

stack = [1, 2, 3, 4, 5]
print(f"Stack: {stack}")

last = stack.pop()
print(f"Popped: {last}")
print(f"Remaining: {stack}")

second = stack.pop(1)  # Pop at index 1
print(f"Popped index 1: {second}")
print(f"Remaining: {stack}")

# Example 6: clear() - Remove All
print("\\n" + "="*70)
print("Example 6: Clear List")
print("="*70)

items = [1, 2, 3, 4, 5]
print(f"Before clear: {items}")

items.clear()
print(f"After clear: {items}")

# Example 7: index() - Find Position
print("\\n" + "="*70)
print("Example 7: Find Index of Value")
print("="*70)

values = [10, 20, 30, 40, 50]
print(f"Values: {values}")

index = values.index(30)
print(f"Index of 30: {index}")

# Example 8: count() - Count Occurrences
print("\\n" + "="*70)
print("Example 8: Count Items")
print("="*70)

data = [1, 2, 2, 3, 2, 4, 2, 5]
print(f"Data: {data}")

count_2 = data.count(2)
print(f"Count of 2: {count_2}")

# Example 9: sort() - Sort in Place
print("\\n" + "="*70)
print("Example 9: Sort List")
print("="*70)

numbers = [5, 2, 8, 1, 9]
print(f"Before sort: {numbers}")

numbers.sort()
print(f"After sort: {numbers}")

numbers.sort(reverse=True)
print(f"After reverse sort: {numbers}")

# Example 10: reverse() - Reverse in Place
print("\\n" + "="*70)
print("Example 10: Reverse Order")
print("="*70)

items = [1, 2, 3, 4, 5]
print(f"Original: {items}")

items.reverse()
print(f"After reverse: {items}")

# Example 11: copy() - Shallow Copy
print("\\n" + "="*70)
print("Example 11: Copy List")
print("="*70)

original = [1, 2, 3]
copied = original.copy()

original[0] = 999

print(f"Original: {original}")
print(f"Copy: {copied}")

print("\\n" + "="*70)
print("List Methods Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - append(x) adds to end")
print("  - insert(i, x) adds at position")
print("  - remove(x) deletes first match")
print("  - pop() removes and returns")
print("  - sort() orders in place")
print("  - Many powerful methods available")
'''

# Lesson 62: List Slicing
lesson62 = next(l for l in lessons if l['id'] == 62)
lesson62['fullSolution'] = '''"""
List Slicing - Extract Sublists

Master slicing to extract portions of lists.
Powerful technique for working with sequences.

**Zero Package Installation Required**
"""

# Example 1: Basic Slicing
print("="*70)
print("Example 1: Get Sublist")
print("="*70)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Full list: {numbers}")
print(f"[2:5]: {numbers[2:5]}")  # Index 2 to 4
print(f"[0:3]: {numbers[0:3]}")  # First 3
print(f"[5:8]: {numbers[5:8]}")  # Index 5 to 7

# Example 2: Omitting Start/Stop
print("\\n" + "="*70)
print("Example 2: Default Indices")
print("="*70)

items = [10, 20, 30, 40, 50]

print(f"List: {items}")
print(f"[:3] (first 3): {items[:3]}")
print(f"[2:] (from 2 to end): {items[2:]}")
print(f"[:] (full copy): {items[:]}")

# Example 3: Negative Indices
print("\\n" + "="*70)
print("Example 3: Slice with Negatives")
print("="*70)

data = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"Data: {data}")
print(f"[-3:] (last 3): {data[-3:]}")
print(f"[:-2] (all but last 2): {data[:-2]}")
print(f"[-5:-2] (middle): {data[-5:-2]}")

# Example 4: Step Parameter
print("\\n" + "="*70)
print("Example 4: Slice with Step")
print("="*70)

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"Values: {values}")
print(f"[::2] (every 2nd): {values[::2]}")
print(f"[1::2] (every 2nd from 1): {values[1::2]}")
print(f"[::3] (every 3rd): {values[::3]}")

# Example 5: Reverse with Slicing
print("\\n" + "="*70)
print("Example 5: Reverse List")
print("="*70)

nums = [1, 2, 3, 4, 5]

print(f"Original: {nums}")
print(f"[::-1] (reversed): {nums[::-1]}")

# Example 6: Extract First/Last N
print("\\n" + "="*70)
print("Example 6: First and Last Elements")
print("="*70)

items = [10, 20, 30, 40, 50, 60, 70, 80]

first_3 = items[:3]
last_3 = items[-3:]

print(f"Items: {items}")
print(f"First 3: {first_3}")
print(f"Last 3: {last_3}")

# Example 7: Remove First/Last
print("\\n" + "="*70)
print("Example 7: Skip Elements")
print("="*70)

data = [1, 2, 3, 4, 5, 6]

without_first = data[1:]
without_last = data[:-1]
without_both = data[1:-1]

print(f"Data: {data}")
print(f"Without first: {without_first}")
print(f"Without last: {without_last}")
print(f"Without both: {without_both}")

# Example 8: Split in Half
print("\\n" + "="*70)
print("Example 8: Divide List")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
mid = len(numbers) // 2

left = numbers[:mid]
right = numbers[mid:]

print(f"Numbers: {numbers}")
print(f"Left half: {left}")
print(f"Right half: {right}")

# Example 9: Replace Slice
print("\\n" + "="*70)
print("Example 9: Replace Section")
print("="*70)

values = [1, 2, 3, 4, 5]
print(f"Original: {values}")

values[1:4] = [20, 30, 40]
print(f"After replace [1:4]: {values}")

# Example 10: Delete with Slicing
print("\\n" + "="*70)
print("Example 10: Delete Section")
print("="*70)

items = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Original: {items}")

del items[2:5]
print(f"After del [2:5]: {items}")

print("\\n" + "="*70)
print("List Slicing Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - [start:stop] gets sublist")
print("  - [:n] gets first n items")
print("  - [n:] gets from n to end")
print("  - [::step] for every nth item")
print("  - [::-1] reverses list")
print("  - Very powerful and Pythonic")
'''

# Lesson 63: Lists and Arrays Fundamentals
lesson63 = next(l for l in lessons if l['id'] == 63)
lesson63['fullSolution'] = '''"""
Lists and Arrays Fundamentals

Master Python lists as dynamic arrays.
Understanding list behavior and performance.

**Zero Package Installation Required**
"""

# Example 1: Lists as Dynamic Arrays
print("="*70)
print("Example 1: List Basics")
print("="*70)

# Python lists are dynamic arrays
numbers = [1, 2, 3]
print(f"Initial: {numbers}")

# Can grow dynamically
numbers.append(4)
numbers.append(5)
print(f"After appends: {numbers}")

# Example 2: Heterogeneous Types
print("\\n" + "="*70)
print("Example 2: Mixed Types (Unlike Arrays)")
print("="*70)

# Lists can hold different types
mixed = [1, "hello", 3.14, True, [1, 2]]
print(f"Mixed list: {mixed}")
print(f"Types: {[type(x).__name__ for x in mixed]}")

# Example 3: List vs Array Concept
print("\\n" + "="*70)
print("Example 3: List Memory Model")
print("="*70)

values = [10, 20, 30]
print(f"Values: {values}")
print(f"Size: {len(values)}")
print(f"Memory efficient for Python objects")

# Example 4: Indexing Like Arrays
print("\\n" + "="*70)
print("Example 4: Array-Like Access")
print("="*70)

data = [100, 200, 300, 400, 500]

print("Index access:")
print(f"  data[0] = {data[0]}")
print(f"  data[2] = {data[2]}")
print(f"  data[-1] = {data[-1]}")

# Example 5: Contiguous but Dynamic
print("\\n" + "="*70)
print("Example 5: Growth Behavior")
print("="*70)

arr = []
print(f"Start: {arr}")

for i in range(5):
    arr.append(i)
    print(f"  Appended {i}: {arr}")

# Example 6: List Capacity Concept
print("\\n" + "="*70)
print("Example 6: Efficient Appending")
print("="*70)

# Lists over-allocate for efficiency
nums = []
for i in range(10):
    nums.append(i)

print(f"Built list: {nums}")
print("Append is O(1) amortized")

# Example 7: Sequential Access
print("\\n" + "="*70)
print("Example 7: Iterate Like Array")
print("="*70)

items = [1, 2, 3, 4, 5]

print("Sequential access:")
for i in range(len(items)):
    print(f"  items[{i}] = {items[i]}")

# Example 8: Bounds Checking
print("\\n" + "="*70)
print("Example 8: Safe vs Unsafe Access")
print("="*70)

data = [10, 20, 30]

# Safe access
if 5 < len(data):
    print(f"Index 5: {data[5]}")
else:
    print("Index 5 out of bounds")

# Example 9: List Operations
print("\\n" + "="*70)
print("Example 9: Common Operations")
print("="*70)

arr = [1, 2, 3, 4, 5]

print(f"Array: {arr}")
print(f"Length: {len(arr)}")
print(f"Sum: {sum(arr)}")
print(f"Max: {max(arr)}")
print(f"Min: {min(arr)}")

# Example 10: Performance Characteristics
print("\\n" + "="*70)
print("Example 10: Time Complexity")
print("="*70)

print("List operations:")
print("  Access by index: O(1)")
print("  Append to end: O(1) amortized")
print("  Insert at start: O(n)")
print("  Search: O(n)")
print("  Sort: O(n log n)")

print("\\n" + "="*70)
print("Lists and Arrays Fundamentals Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Lists are dynamic arrays")
print("  - Can hold any type")
print("  - Zero-indexed")
print("  - Dynamic sizing")
print("  - Efficient for most operations")
'''

# Lesson 64: Max in a List
lesson64 = next(l for l in lessons if l['id'] == 64)
lesson64['fullSolution'] = '''"""
Max in a List - Maximum Value

Master finding maximum values in lists.
Essential for data analysis and comparisons.

**Zero Package Installation Required**
"""

# Example 1: Using max()
print("="*70)
print("Example 1: Built-in max() Function")
print("="*70)

numbers = [45, 12, 67, 23, 89, 34]
maximum = max(numbers)

print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")

# Example 2: Manual Maximum Search
print("\\n" + "="*70)
print("Example 2: Find Max with Loop")
print("="*70)

values = [15, 42, 8, 91, 27]
max_val = values[0]

for val in values:
    if val > max_val:
        max_val = val

print(f"Values: {values}")
print(f"Maximum: {max_val}")

# Example 3: Max with Position
print("\\n" + "="*70)
print("Example 3: Find Max and Index")
print("="*70)

scores = [85, 92, 78, 95, 88]
max_score = max(scores)
max_index = scores.index(max_score)

print(f"Scores: {scores}")
print(f"Highest: {max_score}")
print(f"Position: {max_index}")

# Example 4: Max of Negative Numbers
print("\\n" + "="*70)
print("Example 4: Maximum of Negatives")
print("="*70)

negatives = [-5, -2, -10, -1, -8]
max_neg = max(negatives)

print(f"Negatives: {negatives}")
print(f"Maximum: {max_neg}")

# Example 5: Max with Tracking
print("\\n" + "="*70)
print("Example 5: Track Max Updates")
print("="*70)

data = [10, 25, 15, 30, 20]
current_max = data[0]

print("Finding maximum:")
for i, val in enumerate(data):
    if val > current_max:
        current_max = val
        print(f"  New max at index {i}: {val}")

print(f"Final max: {current_max}")

# Example 6: Max from Multiple Lists
print("\\n" + "="*70)
print("Example 6: Overall Maximum")
print("="*70)

list1 = [10, 20, 30]
list2 = [15, 25, 35]
list3 = [5, 15, 25]

max1 = max(list1)
max2 = max(list2)
max3 = max(list3)

overall_max = max(max1, max2, max3)

print(f"List 1 max: {max1}")
print(f"List 2 max: {max2}")
print(f"List 3 max: {max3}")
print(f"Overall max: {overall_max}")

# Example 7: Max with Key Function
print("\\n" + "="*70)
print("Example 7: Max by Property")
print("="*70)

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

top_student = max(students, key=lambda s: s["score"])

print("Students:")
for s in students:
    print(f"  {s['name']}: {s['score']}")

print(f"\\nTop student: {top_student['name']}")
print(f"Score: {top_student['score']}")

# Example 8: Max String Length
print("\\n" + "="*70)
print("Example 8: Longest String")
print("="*70)

words = ["hi", "hello", "hey", "greetings"]
longest = max(words, key=len)

print(f"Words: {words}")
print(f"Longest: '{longest}'")
print(f"Length: {len(longest)}")

# Example 9: Empty List Handling
print("\\n" + "="*70)
print("Example 9: Safe Max Function")
print("="*70)

def safe_max(numbers):
    if not numbers:
        return None
    return max(numbers)

print(f"Max of [1,5,3]: {safe_max([1,5,3])}")
print(f"Max of []: {safe_max([])}")

# Example 10: Max with Default
print("\\n" + "="*70)
print("Example 10: Max or Default")
print("="*70)

def max_or_default(numbers, default=0):
    return max(numbers) if numbers else default

print(f"Max of [10,20,30]: {max_or_default([10,20,30])}")
print(f"Max of [] with default: {max_or_default([])}")

print("\\n" + "="*70)
print("Max in a List Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - max(list) finds largest")
print("  - Returns value, not index")
print("  - Use .index() to find position")
print("  - key= for custom comparison")
print("  - Handle empty lists safely")
'''

# Lesson 65: Removing from Lists
lesson65 = next(l for l in lessons if l['id'] == 65)
lesson65['fullSolution'] = '''"""
Removing from Lists - Delete Elements

Master different methods to remove list elements.
Essential for list maintenance and cleanup.

**Zero Package Installation Required**
"""

# Example 1: remove() - Delete by Value
print("="*70)
print("Example 1: Remove First Match")
print("="*70)

fruits = ["apple", "banana", "cherry", "banana"]
print(f"Original: {fruits}")

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# Example 2: pop() - Remove by Index
print("\\n" + "="*70)
print("Example 2: Pop Elements")
print("="*70)

numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

removed = numbers.pop()
print(f"Popped (last): {removed}")
print(f"Remaining: {numbers}")

removed = numbers.pop(1)
print(f"Popped index 1: {removed}")
print(f"Remaining: {numbers}")

# Example 3: del - Delete by Index/Slice
print("\\n" + "="*70)
print("Example 3: Delete with del")
print("="*70)

items = [1, 2, 3, 4, 5]
print(f"Original: {items}")

del items[2]
print(f"After del items[2]: {items}")

del items[1:3]
print(f"After del items[1:3]: {items}")

# Example 4: clear() - Remove All
print("\\n" + "="*70)
print("Example 4: Clear Entire List")
print("="*70)

data = [1, 2, 3, 4, 5]
print(f"Before clear: {data}")

data.clear()
print(f"After clear: {data}")

# Example 5: Remove All Occurrences
print("\\n" + "="*70)
print("Example 5: Remove All Matches")
print("="*70)

values = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {values}")

while 2 in values:
    values.remove(2)

print(f"After removing all 2's: {values}")

# Example 6: Remove with Condition
print("\\n" + "="*70)
print("Example 6: Filter Out Values")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original: {numbers}")

# Remove evens
numbers = [n for n in numbers if n % 2 != 0]
print(f"Odds only: {numbers}")

# Example 7: Safe Remove
print("\\n" + "="*70)
print("Example 7: Check Before Removing")
print("="*70)

colors = ["red", "green", "blue"]
print(f"Colors: {colors}")

if "yellow" in colors:
    colors.remove("yellow")
    print("Removed yellow")
else:
    print("Yellow not found")

if "red" in colors:
    colors.remove("red")
    print(f"Removed red: {colors}")

# Example 8: Remove from End
print("\\n" + "="*70)
print("Example 8: Pop from End")
print("="*70)

stack = [1, 2, 3, 4, 5]

print("Popping from stack:")
while stack:
    item = stack.pop()
    print(f"  Popped: {item}, remaining: {stack}")

# Example 9: Remove Duplicates
print("\\n" + "="*70)
print("Example 9: Remove Duplicates")
print("="*70)

items = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(f"With duplicates: {items}")

# Method 1: List comprehension
seen = []
unique = []
for item in items:
    if item not in seen:
        seen.append(item)
        unique.append(item)

print(f"Without duplicates: {unique}")

# Method 2: Using set (loses order)
unique2 = list(set(items))
print(f"Using set: {unique2}")

# Example 10: Remove by Multiple Conditions
print("\\n" + "="*70)
print("Example 10: Complex Filtering")
print("="*70)

numbers = [-5, 10, -3, 8, 0, -1, 15, 20]
print(f"Original: {numbers}")

# Keep only positive numbers greater than 5
filtered = [n for n in numbers if n > 5]
print(f"Positive and >5: {filtered}")

print("\\n" + "="*70)
print("Removing from Lists Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - remove(value) deletes first match")
print("  - pop(index) removes and returns")
print("  - del for index or slice")
print("  - clear() removes all")
print("  - List comprehension for filtering")
print("  - Check existence before removing")
'''

# Save all changes
for lesson in [lesson61, lesson62, lesson63, lesson64, lesson65]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 61-65:")
print(f"  61: List Methods - {len(lesson61['fullSolution'])} chars")
print(f"  62: List Slicing - {len(lesson62['fullSolution'])} chars")
print(f"  63: Lists and Arrays Fundamentals - {len(lesson63['fullSolution'])} chars")
print(f"  64: Max in a List - {len(lesson64['fullSolution'])} chars")
print(f"  65: Removing from Lists - {len(lesson65['fullSolution'])} chars")
print("\\nBatch 61-65 complete!")
