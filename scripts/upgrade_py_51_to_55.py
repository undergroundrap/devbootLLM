#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 51: Average of a List
lesson51 = next(l for l in lessons if l['id'] == 51)
lesson51['fullSolution'] = '''"""
Average of a List - Statistical Calculations

Master calculating the average (mean) of list values.
Essential for data analysis and statistics.

**Zero Package Installation Required**
"""

# Example 1: Basic Average
print("="*70)
print("Example 1: Calculate Mean")
print("="*70)

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)

print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Count: {len(numbers)}")
print(f"Average: {average}")

# Example 2: Test Scores Average
print("\\n" + "="*70)
print("Example 2: Grade Point Average")
print("="*70)

scores = [85, 92, 78, 95, 88]
avg_score = sum(scores) / len(scores)

print(f"Test scores: {scores}")
print(f"Average score: {avg_score:.1f}")

# Example 3: Average Function
print("\\n" + "="*70)
print("Example 3: Reusable Function")
print("="*70)

def calculate_average(values):
    if not values:
        return 0
    return sum(values) / len(values)

data1 = [10, 20, 30]
data2 = [5, 10, 15, 20, 25]

print(f"Data 1: {data1}")
print(f"Average: {calculate_average(data1):.2f}")
print(f"\\nData 2: {data2}")
print(f"Average: {calculate_average(data2):.2f}")

# Example 4: Temperature Average
print("\\n" + "="*70)
print("Example 4: Weekly Temperature")
print("="*70)

temps = [72, 75, 68, 71, 73, 70, 74]
avg_temp = sum(temps) / len(temps)

print(f"Daily temperatures: {temps}")
print(f"Average temperature: {avg_temp:.1f}°F")

# Example 5: Price Average
print("\\n" + "="*70)
print("Example 5: Average Price")
print("="*70)

prices = [19.99, 24.99, 14.99, 29.99, 34.99]
avg_price = sum(prices) / len(prices)

print(f"Prices: {prices}")
print(f"Average price: ${avg_price:.2f}")

# Example 6: Manual Calculation
print("\\n" + "="*70)
print("Example 6: Calculate Without sum()")
print("="*70)

values = [5, 10, 15, 20, 25]
total = 0

for value in values:
    total += value

average = total / len(values)

print(f"Values: {values}")
print(f"Total: {total}")
print(f"Average: {average}")

# Example 7: Floating Point Precision
print("\\n" + "="*70)
print("Example 7: Round Results")
print("="*70)

measurements = [10.3, 20.7, 15.2, 18.9]
avg = sum(measurements) / len(measurements)

print(f"Measurements: {measurements}")
print(f"Average (raw): {avg}")
print(f"Average (1 decimal): {avg:.1f}")
print(f"Average (2 decimals): {avg:.2f}")

# Example 8: Above/Below Average
print("\\n" + "="*70)
print("Example 8: Compare to Average")
print("="*70)

salaries = [50000, 60000, 55000, 65000, 45000]
avg_salary = sum(salaries) / len(salaries)

print(f"Salaries: {salaries}")
print(f"Average: ${avg_salary:,.2f}")
print("\\nComparison:")

for salary in salaries:
    if salary > avg_salary:
        print(f"  ${salary:,} - Above average")
    elif salary < avg_salary:
        print(f"  ${salary:,} - Below average")
    else:
        print(f"  ${salary:,} - At average")

# Example 9: Empty List Handling
print("\\n" + "="*70)
print("Example 9: Handle Empty Lists")
print("="*70)

def safe_average(numbers):
    if len(numbers) == 0:
        print("  Warning: Empty list, returning 0")
        return 0
    return sum(numbers) / len(numbers)

print(f"Average of [1,2,3]: {safe_average([1,2,3])}")
print(f"Average of []: {safe_average([])}")

# Example 10: Multiple Averages
print("\\n" + "="*70)
print("Example 10: Compare Multiple Datasets")
print("="*70)

jan_sales = [1000, 1200, 1100, 1300]
feb_sales = [1500, 1400, 1600, 1700]

jan_avg = sum(jan_sales) / len(jan_sales)
feb_avg = sum(feb_sales) / len(feb_sales)

print(f"January average: ${jan_avg:.2f}")
print(f"February average: ${feb_avg:.2f}")
print(f"Improvement: ${feb_avg - jan_avg:.2f}")

print("\\n" + "="*70)
print("Average of a List Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Average = sum(list) / len(list)")
print("  - Use sum() for total")
print("  - Check for empty lists")
print("  - Round for display")
print("  - Essential for data analysis")
'''

# Lesson 52: Build a Todo List
lesson52 = next(l for l in lessons if l['id'] == 52)
lesson52['fullSolution'] = '''"""
Build a Todo List - List Application

Master building a practical todo list application.
Learn CRUD operations with lists.

**Zero Package Installation Required**
"""

# Example 1: Basic Todo List
print("="*70)
print("Example 1: Simple Todo List")
print("="*70)

todos = []

# Add items
todos.append("Buy groceries")
todos.append("Call dentist")
todos.append("Finish homework")

print("Todo List:")
for i, todo in enumerate(todos, 1):
    print(f"  {i}. {todo}")

# Example 2: Add and Remove
print("\\n" + "="*70)
print("Example 2: Manage Items")
print("="*70)

tasks = ["Task 1", "Task 2", "Task 3"]
print(f"Initial: {tasks}")

# Add new task
tasks.append("Task 4")
print(f"After add: {tasks}")

# Remove completed task
tasks.remove("Task 2")
print(f"After remove: {tasks}")

# Example 3: Mark as Complete
print("\\n" + "="*70)
print("Example 3: Track Completion")
print("="*70)

class Todo:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.description}"

todos = [
    Todo("Buy milk"),
    Todo("Read book"),
    Todo("Exercise")
]

print("Todo list:")
for todo in todos:
    print(f"  {todo}")

# Mark one complete
todos[0].mark_complete()

print("\\nAfter completing first:")
for todo in todos:
    print(f"  {todo}")

# Example 4: Dictionary-Based Todos
print("\\n" + "="*70)
print("Example 4: Structured Todos")
print("="*70)

todo_list = [
    {"task": "Clean room", "done": False},
    {"task": "Study Python", "done": True},
    {"task": "Make dinner", "done": False}
]

print("Tasks:")
for todo in todo_list:
    status = "DONE" if todo["done"] else "TODO"
    print(f"  [{status}] {todo['task']}")

# Example 5: Priority Levels
print("\\n" + "="*70)
print("Example 5: Todo with Priority")
print("="*70)

tasks = [
    {"task": "Fix bug", "priority": "high"},
    {"task": "Write docs", "priority": "low"},
    {"task": "Code review", "priority": "medium"}
]

print("High priority tasks:")
for task in tasks:
    if task["priority"] == "high":
        print(f"  - {task['task']}")

# Example 6: Add Todo Function
print("\\n" + "="*70)
print("Example 6: Helper Functions")
print("="*70)

todos = []

def add_todo(description):
    todos.append(description)
    print(f"  Added: {description}")

def show_todos():
    print("  Current todos:")
    for i, todo in enumerate(todos, 1):
        print(f"    {i}. {todo}")

add_todo("Buy coffee")
add_todo("Reply to email")
show_todos()

# Example 7: Remove by Index
print("\\n" + "="*70)
print("Example 7: Remove Specific Item")
print("="*70)

tasks = ["Task A", "Task B", "Task C", "Task D"]
print(f"Tasks: {tasks}")

# Remove by index
index_to_remove = 1
removed = tasks.pop(index_to_remove)

print(f"Removed: {removed}")
print(f"Remaining: {tasks}")

# Example 8: Count Incomplete
print("\\n" + "="*70)
print("Example 8: Statistics")
print("="*70)

todos = [
    {"task": "Task 1", "done": True},
    {"task": "Task 2", "done": False},
    {"task": "Task 3", "done": False},
    {"task": "Task 4", "done": True}
]

total = len(todos)
completed = sum(1 for t in todos if t["done"])
remaining = total - completed

print(f"Total tasks: {total}")
print(f"Completed: {completed}")
print(f"Remaining: {remaining}")

# Example 9: Clear All
print("\\n" + "="*70)
print("Example 9: Clear Todo List")
print("="*70)

todos = ["Task 1", "Task 2", "Task 3"]
print(f"Before: {todos}")

todos.clear()
print(f"After clear: {todos}")
print(f"List is empty: {len(todos) == 0}")

# Example 10: Complete Todo Manager
print("\\n" + "="*70)
print("Example 10: Full Todo Manager")
print("="*70)

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, task):
        self.todos.append({"task": task, "done": False})

    def complete(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["done"] = True

    def show(self):
        for i, todo in enumerate(self.todos):
            status = "✓" if todo["done"] else " "
            print(f"  {i}. [{status}] {todo['task']}")

manager = TodoManager()
manager.add("Learn Python")
manager.add("Build project")
manager.add("Deploy app")

print("Todo list:")
manager.show()

print("\\nCompleting first task:")
manager.complete(0)
manager.show()

print("\\n" + "="*70)
print("Build a Todo List Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use lists to store tasks")
print("  - append() to add")
print("  - remove() or pop() to delete")
print("  - Track completion with flags")
print("  - Build practical applications")
'''

# Lesson 53: Creating Lists
lesson53 = next(l for l in lessons if l['id'] == 53)
lesson53['fullSolution'] = '''"""
Creating Lists - List Initialization

Master different ways to create and initialize lists.
Foundation for working with collections.

**Zero Package Installation Required**
"""

# Example 1: Empty List
print("="*70)
print("Example 1: Create Empty List")
print("="*70)

# Method 1: Square brackets
list1 = []
print(f"Empty list: {list1}")

# Method 2: list() constructor
list2 = list()
print(f"Using list(): {list2}")

# Example 2: List with Values
print("\\n" + "="*70)
print("Example 2: Initialize with Items")
print("="*70)

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Fruits: {fruits}")
print(f"Mixed types: {mixed}")

# Example 3: List from Range
print("\\n" + "="*70)
print("Example 3: Create from Range")
print("="*70)

# Numbers 0 to 9
nums1 = list(range(10))
print(f"0 to 9: {nums1}")

# Numbers 1 to 10
nums2 = list(range(1, 11))
print(f"1 to 10: {nums2}")

# Even numbers
evens = list(range(0, 11, 2))
print(f"Evens: {evens}")

# Example 4: Repeated Values
print("\\n" + "="*70)
print("Example 4: Lists with Repetition")
print("="*70)

# Ten zeros
zeros = [0] * 10
print(f"Ten zeros: {zeros}")

# Five "hello"s
greetings = ["hello"] * 5
print(f"Five hellos: {greetings}")

# Pattern repetition
pattern = [1, 2, 3] * 3
print(f"Pattern x3: {pattern}")

# Example 5: List from String
print("\\n" + "="*70)
print("Example 5: String to List")
print("="*70)

# Characters
text = "Python"
chars = list(text)
print(f"String: {text}")
print(f"Characters: {chars}")

# Split into words
sentence = "Hello World Python"
words = sentence.split()
print(f"\\nSentence: {sentence}")
print(f"Words: {words}")

# Example 6: Nested Lists
print("\\n" + "="*70)
print("Example 6: 2D Lists")
print("="*70)

# Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Example 7: List Comprehension Creation
print("\\n" + "="*70)
print("Example 7: Create with Comprehension")
print("="*70)

# Squares
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# Example 8: Copy Lists
print("\\n" + "="*70)
print("Example 8: Create Copies")
print("="*70)

original = [1, 2, 3, 4, 5]

# Shallow copy
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

print(f"Original: {original}")
print(f"Copy 1: {copy1}")
print(f"Copy 2: {copy2}")
print(f"Copy 3: {copy3}")

# Example 9: From Other Collections
print("\\n" + "="*70)
print("Example 9: Convert to List")
print("="*70)

# From tuple
tuple_data = (1, 2, 3, 4, 5)
list_data = list(tuple_data)
print(f"Tuple: {tuple_data}")
print(f"List: {list_data}")

# From set
set_data = {3, 1, 4, 1, 5}
list_from_set = list(set_data)
print(f"\\nSet: {set_data}")
print(f"List: {list_from_set}")

# Example 10: Pre-sized Lists
print("\\n" + "="*70)
print("Example 10: Initialize with Size")
print("="*70)

# List of None values
size = 5
empty_slots = [None] * size
print(f"Empty slots: {empty_slots}")

# Fill later
data = [0] * 10
data[0] = 100
data[5] = 500
print(f"Partially filled: {data}")

print("\\n" + "="*70)
print("Creating Lists Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - [] creates empty list")
print("  - [values] initializes with items")
print("  - list(range(n)) creates sequence")
print("  - [value] * n creates repetition")
print("  - Many ways to create lists")
'''

# Lesson 54: Finding Max in List
lesson54 = next(l for l in lessons if l['id'] == 54)
lesson54['fullSolution'] = '''"""
Finding Max in List - Maximum Value Search

Master finding the largest value in a list.
Essential for data analysis and comparisons.

**Zero Package Installation Required**
"""

# Example 1: Using max() Function
print("="*70)
print("Example 1: Built-in max()")
print("="*70)

numbers = [10, 45, 23, 67, 12, 89, 34]
maximum = max(numbers)

print(f"Numbers: {numbers}")
print(f"Maximum: {maximum}")

# Example 2: Manual Search
print("\\n" + "="*70)
print("Example 2: Find Max Manually")
print("="*70)

values = [15, 42, 8, 91, 27]
max_value = values[0]

for value in values:
    if value > max_value:
        max_value = value

print(f"Values: {values}")
print(f"Maximum: {max_value}")

# Example 3: Max with Index
print("\\n" + "="*70)
print("Example 3: Find Max and Position")
print("="*70)

scores = [85, 92, 78, 95, 88]
max_score = max(scores)
max_index = scores.index(max_score)

print(f"Scores: {scores}")
print(f"Highest score: {max_score}")
print(f"Position: {max_index}")

# Example 4: Max Temperature
print("\\n" + "="*70)
print("Example 4: Highest Temperature")
print("="*70)

temps = [72, 75, 68, 82, 71, 77, 80]
highest_temp = max(temps)

print(f"Daily temps: {temps}")
print(f"Highest: {highest_temp}°F")

# Example 5: Max of Negative Numbers
print("\\n" + "="*70)
print("Example 5: Maximum of Negatives")
print("="*70)

negatives = [-5, -2, -10, -1, -8]
max_neg = max(negatives)

print(f"Negatives: {negatives}")
print(f"Maximum (least negative): {max_neg}")

# Example 6: Max with Tracking
print("\\n" + "="*70)
print("Example 6: Track Max Changes")
print("="*70)

data = [10, 25, 15, 30, 20]
current_max = data[0]

print("Processing:")
for i, value in enumerate(data):
    if value > current_max:
        current_max = value
        print(f"  New max at index {i}: {value}")
    else:
        print(f"  Value {value} <= current max {current_max}")

# Example 7: Max of Prices
print("\\n" + "="*70)
print("Example 7: Most Expensive Item")
print("="*70)

prices = [19.99, 34.99, 12.99, 45.99, 28.99]
most_expensive = max(prices)

print(f"Prices: {prices}")
print(f"Most expensive: ${most_expensive}")

# Example 8: Max Function
print("\\n" + "="*70)
print("Example 8: Reusable Function")
print("="*70)

def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

print(f"Max of [1,5,3]: {find_maximum([1,5,3])}")
print(f"Max of []: {find_maximum([])}")

# Example 9: Multiple Lists
print("\\n" + "="*70)
print("Example 9: Compare Multiple Maximums")
print("="*70)

list1 = [10, 20, 30]
list2 = [15, 25, 35]

max1 = max(list1)
max2 = max(list2)

print(f"List 1 max: {max1}")
print(f"List 2 max: {max2}")
print(f"Overall max: {max(max1, max2)}")

# Example 10: Max of Objects
print("\\n" + "="*70)
print("Example 10: Max by Property")
print("="*70)

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

# Find student with highest score
top_student = max(students, key=lambda s: s["score"])

print("Students:", [s["name"] for s in students])
print(f"Top student: {top_student['name']}")
print(f"Score: {top_student['score']}")

print("\\n" + "="*70)
print("Finding Max Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - max(list) returns largest value")
print("  - Can find max manually with loop")
print("  - Use .index() to find position")
print("  - Works with numbers, strings, etc.")
print("  - Use key= for complex objects")
'''

# Lesson 55: Finding Min in List
lesson55 = next(l for l in lessons if l['id'] == 55)
lesson55['fullSolution'] = '''"""
Finding Min in List - Minimum Value Search

Master finding the smallest value in a list.
Essential for data analysis and comparisons.

**Zero Package Installation Required**
"""

# Example 1: Using min() Function
print("="*70)
print("Example 1: Built-in min()")
print("="*70)

numbers = [10, 45, 23, 3, 67, 12, 89, 34]
minimum = min(numbers)

print(f"Numbers: {numbers}")
print(f"Minimum: {minimum}")

# Example 2: Manual Search
print("\\n" + "="*70)
print("Example 2: Find Min Manually")
print("="*70)

values = [15, 42, 8, 91, 27]
min_value = values[0]

for value in values:
    if value < min_value:
        min_value = value

print(f"Values: {values}")
print(f"Minimum: {min_value}")

# Example 3: Min with Index
print("\\n" + "="*70)
print("Example 3: Find Min and Position")
print("="*70)

scores = [85, 92, 78, 95, 88]
min_score = min(scores)
min_index = scores.index(min_score)

print(f"Scores: {scores}")
print(f"Lowest score: {min_score}")
print(f"Position: {min_index}")

# Example 4: Min Temperature
print("\\n" + "="*70)
print("Example 4: Coldest Temperature")
print("="*70)

temps = [72, 75, 68, 82, 71, 77, 80]
coldest = min(temps)

print(f"Daily temps: {temps}")
print(f"Coldest: {coldest}°F")

# Example 5: Min of Negative Numbers
print("\\n" + "="*70)
print("Example 5: Minimum of Negatives")
print("="*70)

negatives = [-5, -2, -10, -1, -8]
min_neg = min(negatives)

print(f"Negatives: {negatives}")
print(f"Minimum (most negative): {min_neg}")

# Example 6: Min Price
print("\\n" + "="*70)
print("Example 6: Cheapest Item")
print("="*70)

prices = [19.99, 34.99, 12.99, 45.99, 28.99]
cheapest = min(prices)

print(f"Prices: {prices}")
print(f"Cheapest: ${cheapest}")

# Example 7: Min and Max Together
print("\\n" + "="*70)
print("Example 7: Range (Min to Max)")
print("="*70)

data = [45, 12, 67, 23, 89, 34]
minimum = min(data)
maximum = max(data)
range_size = maximum - minimum

print(f"Data: {data}")
print(f"Min: {minimum}")
print(f"Max: {maximum}")
print(f"Range: {range_size}")

# Example 8: Min Function
print("\\n" + "="*70)
print("Example 8: Reusable Function")
print("="*70)

def find_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)

print(f"Min of [5,1,3]: {find_minimum([5,1,3])}")
print(f"Min of []: {find_minimum([])}")

# Example 9: Min String Length
print("\\n" + "="*70)
print("Example 9: Shortest String")
print("="*70)

words = ["hi", "hello", "hey", "greetings"]
shortest = min(words, key=len)

print(f"Words: {words}")
print(f"Shortest: '{shortest}'")
print(f"Length: {len(shortest)}")

# Example 10: Min of Objects
print("\\n" + "="*70)
print("Example 10: Min by Property")
print("="*70)

products = [
    {"name": "Laptop", "price": 999},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75}
]

cheapest = min(products, key=lambda p: p["price"])

print("Products:", [p["name"] for p in products])
print(f"Cheapest: {cheapest['name']}")
print(f"Price: ${cheapest['price']}")

print("\\n" + "="*70)
print("Finding Min Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - min(list) returns smallest value")
print("  - Can find min manually with loop")
print("  - Use .index() to find position")
print("  - Works with numbers, strings, etc.")
print("  - Use key= for complex objects")
'''

# Save all changes
for lesson in [lesson51, lesson52, lesson53, lesson54, lesson55]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 51-55:")
print(f"  51: Average of a List - {len(lesson51['fullSolution'])} chars")
print(f"  52: Build a Todo List - {len(lesson52['fullSolution'])} chars")
print(f"  53: Creating Lists - {len(lesson53['fullSolution'])} chars")
print(f"  54: Finding Max in List - {len(lesson54['fullSolution'])} chars")
print(f"  55: Finding Min in List - {len(lesson55['fullSolution'])} chars")
print("\\nBatch 51-55 complete!")
