#!/usr/bin/env python3
"""
Upgrade Python lessons 66-70 with comprehensive content.
- Lesson 66: Reverse a List
- Lesson 67: Sorting Lists
- Lesson 68: Sum of List Elements
- Lesson 69: Working with Multiple Arrays: Merging and Intersection
- Lesson 70: String Concatenation
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 66-70
lesson66 = next(l for l in lessons if l['id'] == 66)
lesson67 = next(l for l in lessons if l['id'] == 67)
lesson68 = next(l for l in lessons if l['id'] == 68)
lesson69 = next(l for l in lessons if l['id'] == 69)
lesson70 = next(l for l in lessons if l['id'] == 70)

# Upgrade Lesson 66: Reverse a List
lesson66['fullSolution'] = '''"""
Reverse a List

Master techniques to reverse lists in Python—from in-place modifications
to creating reversed copies. Essential for data processing, algorithms,
and sequence manipulation.

**Zero Package Installation Required**
"""

# Example 1: Built-in reverse() Method (In-Place)
print("="*70)
print("Example 1: In-Place Reversal with reverse()")
print("="*70)

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")
print(f"Memory ID: {id(numbers)}")

numbers.reverse()  # Modifies the list in-place
print(f"After reverse(): {numbers}")
print(f"Memory ID: {id(numbers)}")  # Same ID - modified in place
print()

# Example 2: Slicing to Create Reversed Copy
print("="*70)
print("Example 2: Creating Reversed Copy with Slicing")
print("="*70)

fruits = ["apple", "banana", "cherry", "date"]
print(f"Original list: {fruits}")
print(f"Original ID: {id(fruits)}")

reversed_fruits = fruits[::-1]  # Creates new list
print(f"Reversed copy: {reversed_fruits}")
print(f"Copy ID: {id(reversed_fruits)}")  # Different ID - new list
print(f"Original unchanged: {fruits}")
print()

# Example 3: reversed() Function with list()
print("="*70)
print("Example 3: reversed() Function (Returns Iterator)")
print("="*70)

colors = ["red", "green", "blue", "yellow"]
print(f"Original: {colors}")

rev_iterator = reversed(colors)
print(f"reversed() returns: {rev_iterator}")  # Iterator object
print(f"Iterator type: {type(rev_iterator)}")

rev_list = list(rev_iterator)
print(f"Converted to list: {rev_list}")
print(f"Original unchanged: {colors}")
print()

# Example 4: Manual Reversal with Loop
print("="*70)
print("Example 4: Manual Reversal Algorithm")
print("="*70)

values = [10, 20, 30, 40, 50]
print(f"Original: {values}")

reversed_values = []
for i in range(len(values) - 1, -1, -1):
    reversed_values.append(values[i])
    print(f"  Step {len(values) - i}: Added {values[i]} → {reversed_values}")

print(f"Final result: {reversed_values}")
print()

# Example 5: Reversing Strings (Convert to List)
print("="*70)
print("Example 5: Reversing Strings via List Conversion")
print("="*70)

text = "Python"
print(f"Original string: '{text}'")

# Convert to list, reverse, join back
char_list = list(text)
print(f"As list: {char_list}")

char_list.reverse()
print(f"Reversed list: {char_list}")

reversed_text = ''.join(char_list)
print(f"Reversed string: '{reversed_text}'")

# Shorter way
print(f"One-liner: '{text[::-1]}'")
print()

# Example 6: Reversing Nested Lists
print("="*70)
print("Example 6: Reversing Lists with Nested Elements")
print("="*70)

matrix = [[1, 2], [3, 4], [5, 6]]
print(f"Original matrix: {matrix}")

# Reverse outer list
reversed_matrix = matrix[::-1]
print(f"Reversed outer: {reversed_matrix}")

# Reverse each inner list too
fully_reversed = [row[::-1] for row in matrix[::-1]]
print(f"Reversed both levels: {fully_reversed}")
print()

# Example 7: Conditional Reversal
print("="*70)
print("Example 7: Reverse Based on Condition")
print("="*70)

def smart_reverse(lst, condition):
    """Reverse list only if condition is met"""
    if condition:
        return lst[::-1]
    return lst

data = [1, 2, 3, 4, 5]
print(f"Original: {data}")
print(f"Reverse if sum > 10: {smart_reverse(data, sum(data) > 10)}")
print(f"Reverse if sum > 20: {smart_reverse(data, sum(data) > 20)}")
print()

# Example 8: Reversing with Index Swapping
print("="*70)
print("Example 8: In-Place Reversal with Two Pointers")
print("="*70)

nums = [1, 2, 3, 4, 5, 6]
print(f"Original: {nums}")

left = 0
right = len(nums) - 1

while left < right:
    # Swap elements
    nums[left], nums[right] = nums[right], nums[left]
    print(f"  Swap positions {left} and {right}: {nums}")
    left += 1
    right -= 1

print(f"Final result: {nums}")
print()

# Example 9: Performance Comparison
print("="*70)
print("Example 9: Performance Characteristics")
print("="*70)

import time

test_list = list(range(100000))

# Time reverse() method
start = time.perf_counter()
test_list.reverse()
reverse_time = time.perf_counter() - start
test_list.reverse()  # Restore

# Time slicing
start = time.perf_counter()
_ = test_list[::-1]
slice_time = time.perf_counter() - start

# Time reversed() with list()
start = time.perf_counter()
_ = list(reversed(test_list))
reversed_time = time.perf_counter() - start

print(f"List size: {len(test_list):,} elements")
print(f"reverse() method: {reverse_time*1000:.4f}ms (in-place)")
print(f"[::-1] slicing: {slice_time*1000:.4f}ms (new list)")
print(f"list(reversed()): {reversed_time*1000:.4f}ms (new list)")
print()

# Example 10: Practical Application - Recent Items
print("="*70)
print("Example 10: Real-World Use Case - Recent Activity")
print("="*70)

activity_log = [
    "User logged in",
    "Viewed dashboard",
    "Updated profile",
    "Uploaded file",
    "Logged out"
]

print("Activity Log (chronological):")
for i, activity in enumerate(activity_log, 1):
    print(f"  {i}. {activity}")

print("\\nRecent Activity (reverse chronological):")
for i, activity in enumerate(reversed(activity_log), 1):
    print(f"  {i}. {activity}")

# Last 3 activities
recent_3 = activity_log[::-1][:3]
print(f"\\nLast 3 activities: {recent_3}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. reverse() - In-place modification, no return value")
print("2. [::-1] - Creates new reversed list, original unchanged")
print("3. reversed() - Returns iterator, memory efficient")
print("4. list(reversed()) - Convert iterator to list")
print("5. reverse() is fastest for in-place reversal")
print("6. [::-1] is most readable for creating copies")
print("7. Manual loops useful for understanding algorithm")
print("8. Works on any sequence (lists, tuples, strings)")
print("="*70)
'''

# Upgrade Lesson 67: Sorting Lists
lesson67['fullSolution'] = '''"""
Sorting Lists

Master Python's powerful sorting capabilities—from basic sorted() and sort()
to custom key functions and multi-level sorting. Essential for data organization,
search optimization, and algorithm implementation.

**Zero Package Installation Required**
"""

# Example 1: sorted() Function (Creates New List)
print("="*70)
print("Example 1: sorted() - Returns New Sorted List")
print("="*70)

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {numbers}")
print(f"Original ID: {id(numbers)}")

sorted_numbers = sorted(numbers)
print(f"Sorted result: {sorted_numbers}")
print(f"Sorted ID: {id(sorted_numbers)}")  # Different ID
print(f"Original unchanged: {numbers}")
print()

# Example 2: sort() Method (In-Place)
print("="*70)
print("Example 2: sort() - In-Place Sorting")
print("="*70)

values = [5, 2, 9, 1, 7, 3]
print(f"Original: {values}")
print(f"Memory ID: {id(values)}")

result = values.sort()  # Returns None!
print(f"sort() returns: {result}")
print(f"List after sort(): {values}")
print(f"Memory ID: {id(values)}")  # Same ID - modified in place
print()

# Example 3: Reverse Sorting
print("="*70)
print("Example 3: Sorting in Descending Order")
print("="*70)

scores = [85, 92, 78, 95, 88]
print(f"Original scores: {scores}")

ascending = sorted(scores)
descending = sorted(scores, reverse=True)

print(f"Ascending: {ascending}")
print(f"Descending: {descending}")

# In-place reverse sort
scores.sort(reverse=True)
print(f"In-place descending: {scores}")
print()

# Example 4: Sorting Strings
print("="*70)
print("Example 4: String Sorting (Lexicographic)")
print("="*70)

fruits = ["banana", "apple", "Cherry", "date", "Elderberry"]
print(f"Original: {fruits}")

# Case-sensitive (default)
sorted_default = sorted(fruits)
print(f"Default sort: {sorted_default}")  # Uppercase first

# Case-insensitive
sorted_case_insensitive = sorted(fruits, key=str.lower)
print(f"Case-insensitive: {sorted_case_insensitive}")

# By length
sorted_by_length = sorted(fruits, key=len)
print(f"By length: {sorted_by_length}")
print()

# Example 5: Custom Key Functions
print("="*70)
print("Example 5: Sorting with Custom Key Functions")
print("="*70)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 95}
]

print("Original order:")
for s in students:
    print(f"  {s['name']}: {s['grade']}")

# Sort by grade
by_grade = sorted(students, key=lambda s: s['grade'])
print("\\nSorted by grade:")
for s in by_grade:
    print(f"  {s['name']}: {s['grade']}")

# Sort by name
by_name = sorted(students, key=lambda s: s['name'])
print("\\nSorted by name:")
for s in by_name:
    print(f"  {s['name']}: {s['grade']}")
print()

# Example 6: Multi-Level Sorting
print("="*70)
print("Example 6: Sorting by Multiple Criteria")
print("="*70)

employees = [
    ("Alice", "Engineering", 85000),
    ("Bob", "Engineering", 92000),
    ("Charlie", "Sales", 78000),
    ("David", "Sales", 78000),
    ("Eve", "Engineering", 92000)
]

# Sort by department, then by salary (descending)
sorted_emp = sorted(employees, key=lambda e: (e[1], -e[2]))

print("Sorted by dept (asc), then salary (desc):")
for name, dept, salary in sorted_emp:
    print(f"  {name:10} | {dept:12} | ${salary:,}")
print()

# Example 7: Sorting Tuples
print("="*70)
print("Example 7: Tuple Sorting (Element-by-Element)")
print("="*70)

coordinates = [(3, 4), (1, 2), (3, 1), (2, 5), (1, 9)]
print(f"Original coordinates: {coordinates}")

sorted_coords = sorted(coordinates)  # Sorts by first element, then second
print(f"Sorted: {sorted_coords}")

# Sort by second element
by_y = sorted(coordinates, key=lambda c: c[1])
print(f"Sorted by Y: {by_y}")

# Sort by distance from origin
from math import sqrt
by_distance = sorted(coordinates, key=lambda c: sqrt(c[0]**2 + c[1]**2))
print(f"By distance from origin: {by_distance}")
print()

# Example 8: Stability of Python's Sort
print("="*70)
print("Example 8: Sort Stability (Preserves Original Order)")
print("="*70)

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 25),
    ("David", 30),
    ("Eve", 25)
]

print("Original order:")
for name, age in data:
    print(f"  {name}: {age}")

# Sort by age - stable sort preserves order of equal elements
sorted_data = sorted(data, key=lambda x: x[1])
print("\\nSorted by age (note preserved order for same age):")
for name, age in sorted_data:
    print(f"  {name}: {age}")
print()

# Example 9: Sorting with None Values
print("="*70)
print("Example 9: Handling None Values in Sorting")
print("="*70)

values_with_none = [5, None, 2, None, 8, 1]
print(f"List with None: {values_with_none}")

# Custom key to handle None (put None at end)
sorted_safe = sorted(values_with_none, key=lambda x: (x is None, x or 0))
print(f"Sorted (None at end): {sorted_safe}")

# Separate None and sort
non_none = sorted([x for x in values_with_none if x is not None])
none_count = values_with_none.count(None)
result = non_none + [None] * none_count
print(f"Manual approach: {result}")
print()

# Example 10: Performance and Algorithm
print("="*70)
print("Example 10: Timsort Algorithm Characteristics")
print("="*70)

import time

# Best case: already sorted
already_sorted = list(range(10000))
start = time.perf_counter()
sorted(already_sorted)
best_time = time.perf_counter() - start

# Worst case: reverse sorted
reverse_sorted = list(range(10000, 0, -1))
start = time.perf_counter()
sorted(reverse_sorted)
worst_time = time.perf_counter() - start

# Random case
import random
random_list = list(range(10000))
random.shuffle(random_list)
start = time.perf_counter()
sorted(random_list)
random_time = time.perf_counter() - start

print("Timsort Performance (10,000 elements):")
print(f"  Already sorted: {best_time*1000:.4f}ms")
print(f"  Reverse sorted: {worst_time*1000:.4f}ms")
print(f"  Random order: {random_time*1000:.4f}ms")
print("\\nTimsort is adaptive - faster on partially sorted data!")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. sorted() - Returns new sorted list, original unchanged")
print("2. sort() - In-place sorting, returns None, modifies original")
print("3. reverse=True - Sort in descending order")
print("4. key=function - Custom sorting criterion")
print("5. Timsort algorithm - O(n log n), stable, adaptive")
print("6. Stable sort - Preserves order of equal elements")
print("7. Can sort any comparable types (numbers, strings, tuples)")
print("8. Use lambda for complex key functions")
print("="*70)
'''

# Upgrade Lesson 68: Sum of List Elements
lesson68['fullSolution'] = '''"""
Sum of List Elements

Master techniques for summing list elements in Python—from built-in sum()
to custom aggregations with conditions, transformations, and nested structures.
Essential for data analysis, statistics, and numerical computations.

**Zero Package Installation Required**
"""

# Example 1: Built-in sum() Function
print("="*70)
print("Example 1: Basic sum() Function")
print("="*70)

numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")

total = sum(numbers)
print(f"Sum: {total}")
print(f"Type: {type(total)}")

# With start value
total_with_start = sum(numbers, 100)
print(f"Sum with start=100: {total_with_start}")
print()

# Example 2: Manual Summation with Loop
print("="*70)
print("Example 2: Manual Summation Algorithm")
print("="*70)

values = [10, 20, 30, 40, 50]
print(f"Values: {values}")

total = 0
for value in values:
    total += value
    print(f"  After adding {value}: total = {total}")

print(f"Final sum: {total}")
print()

# Example 3: Conditional Summation
print("="*70)
print("Example 3: Sum with Conditions (Filtering)")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")

# Sum only even numbers
even_sum = sum(n for n in numbers if n % 2 == 0)
print(f"Sum of evens: {even_sum}")

# Sum only odd numbers
odd_sum = sum(n for n in numbers if n % 2 != 0)
print(f"Sum of odds: {odd_sum}")

# Sum numbers > 5
greater_than_5 = sum(n for n in numbers if n > 5)
print(f"Sum of numbers > 5: {greater_than_5}")
print()

# Example 4: Transforming Before Summing
print("="*70)
print("Example 4: Sum with Transformations")
print("="*70)

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Sum of squares
sum_of_squares = sum(n**2 for n in numbers)
print(f"Sum of squares: {sum_of_squares}")
print(f"Calculation: 1² + 2² + 3² + 4² + 5² = {sum_of_squares}")

# Sum of absolute values
negatives = [-5, -3, 2, -1, 4]
print(f"\\nWith negatives: {negatives}")
sum_abs = sum(abs(n) for n in negatives)
print(f"Sum of absolute values: {sum_abs}")

# Sum of doubled values
sum_doubled = sum(n * 2 for n in numbers)
print(f"\\nSum of doubled values: {sum_doubled}")
print()

# Example 5: Summing Floating Point Numbers
print("="*70)
print("Example 5: Floating Point Arithmetic")
print("="*70)

prices = [19.99, 29.99, 9.99, 49.99]
print(f"Prices: {prices}")

total = sum(prices)
print(f"Total: ${total}")
print(f"Total (rounded): ${total:.2f}")

# Tax calculation
tax_rate = 0.08
subtotal = sum(prices)
tax = subtotal * tax_rate
total_with_tax = subtotal + tax

print(f"\\nSubtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total_with_tax:.2f}")
print()

# Example 6: Summing List of Lists (Nested)
print("="*70)
print("Example 6: Summing Nested Lists (Flattening)")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Sum all elements
total = sum(sum(row) for row in matrix)
print(f"\\nSum of all elements: {total}")

# Sum by rows
row_sums = [sum(row) for row in matrix]
print(f"Row sums: {row_sums}")

# Sum by columns
col_sums = [sum(matrix[row][col] for row in range(len(matrix)))
            for col in range(len(matrix[0]))]
print(f"Column sums: {col_sums}")
print()

# Example 7: Summing Dictionary Values
print("="*70)
print("Example 7: Summing from Dictionaries")
print("="*70)

sales = {
    "Monday": 1200,
    "Tuesday": 1500,
    "Wednesday": 980,
    "Thursday": 1750,
    "Friday": 2100
}

print("Daily sales:")
for day, amount in sales.items():
    print(f"  {day}: ${amount}")

total_sales = sum(sales.values())
print(f"\\nTotal sales: ${total_sales}")

average = total_sales / len(sales)
print(f"Average daily sales: ${average:.2f}")
print()

# Example 8: Weighted Sum
print("="*70)
print("Example 8: Weighted Sum (Dot Product)")
print("="*70)

scores = [85, 90, 78, 92]
weights = [0.2, 0.3, 0.2, 0.3]  # Must sum to 1.0

print(f"Scores: {scores}")
print(f"Weights: {weights}")

weighted_sum = sum(score * weight for score, weight in zip(scores, weights))
print(f"\\nWeighted average: {weighted_sum:.2f}")

# Show calculation
print("\\nCalculation:")
for score, weight in zip(scores, weights):
    print(f"  {score} × {weight} = {score * weight}")
print(f"  Total: {weighted_sum:.2f}")
print()

# Example 9: Cumulative Sum (Running Total)
print("="*70)
print("Example 9: Cumulative Sum / Running Total")
print("="*70)

monthly_revenue = [5000, 5500, 6200, 5800, 6500, 7000]
print("Monthly revenue:")

cumulative = []
running_total = 0

for month, revenue in enumerate(monthly_revenue, 1):
    running_total += revenue
    cumulative.append(running_total)
    print(f"  Month {month}: ${revenue:,} | Cumulative: ${running_total:,}")

print(f"\\nCumulative totals: {cumulative}")
print()

# Example 10: Practical Application - Shopping Cart
print("="*70)
print("Example 10: Real-World Application - Shopping Cart")
print("="*70)

cart = [
    {"item": "Laptop", "price": 899.99, "quantity": 1},
    {"item": "Mouse", "price": 29.99, "quantity": 2},
    {"item": "Keyboard", "price": 79.99, "quantity": 1},
    {"item": "Monitor", "price": 249.99, "quantity": 2},
]

print("Shopping Cart:")
print(f"{'Item':<15} {'Price':>10} {'Qty':>5} {'Subtotal':>12}")
print("-" * 45)

item_totals = []
for item in cart:
    subtotal = item['price'] * item['quantity']
    item_totals.append(subtotal)
    print(f"{item['item']:<15} ${item['price']:>9.2f} {item['quantity']:>5} ${subtotal:>11.2f}")

cart_total = sum(item_totals)
print("-" * 45)
print(f"{'Total:':<32} ${cart_total:>11.2f}")

# Alternative: one-liner
total = sum(item['price'] * item['quantity'] for item in cart)
print(f"\\nVerification: ${total:.2f}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. sum(iterable) - Built-in function for summing sequences")
print("2. sum(iterable, start) - Specify starting value (default 0)")
print("3. Generator expressions - Memory-efficient conditional sums")
print("4. sum(n for n in list if condition) - Filter while summing")
print("5. sum(transform(n) for n in list) - Transform then sum")
print("6. Works with any numeric type (int, float, complex)")
print("7. Nested sums - sum(sum(row) for row in matrix)")
print("8. Weighted sums - sum(a*b for a,b in zip(list1, list2))")
print("="*70)
'''

# Upgrade Lesson 69: Working with Multiple Arrays
lesson69['fullSolution'] = '''"""
Working with Multiple Arrays: Merging and Intersection

Master techniques for combining and comparing multiple lists in Python—from
simple concatenation to set operations, merging sorted arrays, and finding
common elements. Essential for data integration, deduplication, and analysis.

**Zero Package Installation Required**
"""

# Example 1: Simple List Concatenation
print("="*70)
print("Example 1: Basic List Merging with + Operator")
print("="*70)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")

merged = list1 + list2 + list3
print(f"\\nMerged: {merged}")
print(f"Length: {len(merged)}")

# Original lists unchanged
print(f"\\nList 1 unchanged: {list1}")
print()

# Example 2: extend() Method (In-Place)
print("="*70)
print("Example 2: In-Place Merging with extend()")
print("="*70)

fruits = ["apple", "banana"]
more_fruits = ["cherry", "date"]
even_more = ["elderberry", "fig"]

print(f"Original fruits: {fruits}")
print(f"Memory ID: {id(fruits)}")

fruits.extend(more_fruits)
print(f"After extend(more_fruits): {fruits}")

fruits.extend(even_more)
print(f"After extend(even_more): {fruits}")
print(f"Memory ID: {id(fruits)}")  # Same ID - modified in place
print()

# Example 3: Unpacking Operator *
print("="*70)
print("Example 3: Merging with Unpacking Operator")
print("="*70)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

# Modern Python approach
merged = [*a, *b, *c]
print(f"List a: {a}")
print(f"List b: {b}")
print(f"List c: {c}")
print(f"Merged with [*a, *b, *c]: {merged}")

# Can add extra elements too
custom_merge = [0, *a, 99, *b, *c, 100]
print(f"Custom merge: {custom_merge}")
print()

# Example 4: Set Intersection (Common Elements)
print("="*70)
print("Example 4: Finding Common Elements with Sets")
print("="*70)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = [3, 4, 5, 9, 10]

print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")

# Intersection of two lists
common_1_2 = list(set(list1) & set(list2))
print(f"\\nCommon in 1 and 2: {sorted(common_1_2)}")

# Intersection of all three
common_all = list(set(list1) & set(list2) & set(list3))
print(f"Common in all three: {sorted(common_all)}")

# Using set.intersection()
common_method = sorted(set(list1).intersection(list2, list3))
print(f"Using intersection(): {common_method}")
print()

# Example 5: List Comprehension Intersection
print("="*70)
print("Example 5: Intersection Preserving Order and Duplicates")
print("="*70)

list1 = [1, 2, 3, 2, 4, 5]
list2 = [2, 3, 4, 4, 6]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Keep duplicates from list1
intersection_with_dups = [x for x in list1 if x in list2]
print(f"\\nIntersection (with duplicates): {intersection_with_dups}")

# Unique intersection preserving order
seen = set()
intersection_ordered = []
for x in list1:
    if x in list2 and x not in seen:
        intersection_ordered.append(x)
        seen.add(x)

print(f"Intersection (unique, ordered): {intersection_ordered}")
print()

# Example 6: Union (All Unique Elements)
print("="*70)
print("Example 6: Union - All Elements from Multiple Lists")
print("="*70)

team_a = ["Alice", "Bob", "Charlie"]
team_b = ["Bob", "David", "Eve"]
team_c = ["Charlie", "Frank", "Alice"]

print(f"Team A: {team_a}")
print(f"Team B: {team_b}")
print(f"Team C: {team_c}")

# Set union
all_members = set(team_a) | set(team_b) | set(team_c)
print(f"\\nAll unique members (set): {sorted(all_members)}")

# Union preserving order
all_ordered = []
for person in team_a + team_b + team_c:
    if person not in all_ordered:
        all_ordered.append(person)
print(f"All members (ordered): {all_ordered}")
print()

# Example 7: Difference (Elements in A but not B)
print("="*70)
print("Example 7: Set Difference")
print("="*70)

all_items = [1, 2, 3, 4, 5, 6, 7, 8]
sold_items = [2, 4, 6, 8]

print(f"All items: {all_items}")
print(f"Sold items: {sold_items}")

# Items not sold
remaining = list(set(all_items) - set(sold_items))
print(f"\\nRemaining items: {sorted(remaining)}")

# Using list comprehension
remaining_lc = [x for x in all_items if x not in sold_items]
print(f"Remaining (list comp): {remaining_lc}")
print()

# Example 8: Symmetric Difference (XOR)
print("="*70)
print("Example 8: Symmetric Difference (Elements in A or B, not Both)")
print("="*70)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"List 1: {list1}")
print(f"List 2: {list2}")

# Elements in either list but not both
sym_diff = list(set(list1) ^ set(list2))
print(f"\\nSymmetric difference: {sorted(sym_diff)}")

# Using set operations
sym_diff_alt = list((set(list1) - set(list2)) | (set(list2) - set(list1)))
print(f"Alternative calculation: {sorted(sym_diff_alt)}")
print()

# Example 9: Merging Sorted Lists
print("="*70)
print("Example 9: Merging Sorted Arrays Efficiently")
print("="*70)

sorted1 = [1, 3, 5, 7, 9]
sorted2 = [2, 4, 6, 8, 10]

print(f"Sorted list 1: {sorted1}")
print(f"Sorted list 2: {sorted2}")

# Two-pointer merge algorithm
merged = []
i, j = 0, 0

while i < len(sorted1) and j < len(sorted2):
    if sorted1[i] <= sorted2[j]:
        merged.append(sorted1[i])
        i += 1
    else:
        merged.append(sorted2[j])
        j += 1

# Add remaining elements
merged.extend(sorted1[i:])
merged.extend(sorted2[j:])

print(f"\\nMerged (maintaining sort): {merged}")

# Simple approach (less efficient)
simple_merge = sorted(sorted1 + sorted2)
print(f"Simple approach: {simple_merge}")
print()

# Example 10: Practical Application - Data Reconciliation
print("="*70)
print("Example 10: Real-World Use Case - Database Sync")
print("="*70)

database_a = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

database_b = [
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "David"},
    {"id": 5, "name": "Eve"}
]

ids_a = {record['id'] for record in database_a}
ids_b = {record['id'] for record in database_b}

print(f"Database A IDs: {sorted(ids_a)}")
print(f"Database B IDs: {sorted(ids_b)}")

# Records in both databases
common_ids = ids_a & ids_b
print(f"\\nCommon records: {sorted(common_ids)}")

# Records only in A
only_a = ids_a - ids_b
print(f"Only in A: {sorted(only_a)}")

# Records only in B
only_b = ids_b - ids_a
print(f"Only in B: {sorted(only_b)}")

# All unique records
all_ids = ids_a | ids_b
print(f"All unique IDs: {sorted(all_ids)}")

print("\\nReconciliation summary:")
print(f"  Total unique records: {len(all_ids)}")
print(f"  Need to add to A: {len(only_b)} records")
print(f"  Need to add to B: {len(only_a)} records")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Concatenation: list1 + list2 (creates new list)")
print("2. extend(): In-place merging, modifies original list")
print("3. Unpacking: [*list1, *list2, *list3] (modern Python)")
print("4. Intersection: set(list1) & set(list2) (common elements)")
print("5. Union: set(list1) | set(list2) (all unique elements)")
print("6. Difference: set(list1) - set(list2) (in A, not in B)")
print("7. Symmetric diff: set(list1) ^ set(list2) (in A or B, not both)")
print("8. Set operations remove duplicates and lose order")
print("9. List comprehensions preserve order and duplicates")
print("10. Use two-pointer merge for sorted lists")
print("="*70)
'''

# Upgrade Lesson 70: String Concatenation
lesson70['fullSolution'] = '''"""
String Concatenation

Master all techniques for combining strings in Python—from basic + operator
to join(), f-strings, and format(). Learn when to use each method for optimal
performance and readability.

**Zero Package Installation Required**
"""

# Example 1: Basic + Operator
print("="*70)
print("Example 1: String Concatenation with + Operator")
print("="*70)

first_name = "John"
last_name = "Doe"

# Simple concatenation
full_name = first_name + " " + last_name
print(f"First name: '{first_name}'")
print(f"Last name: '{last_name}'")
print(f"Full name: '{full_name}'")

# Multiple concatenations
greeting = "Hello, " + first_name + " " + last_name + "!"
print(f"Greeting: '{greeting}'")

# With newlines
multi_line = "Line 1" + "\\n" + "Line 2" + "\\n" + "Line 3"
print(f"\\nMulti-line:\\n{multi_line}")
print()

# Example 2: Using join() Method
print("="*70)
print("Example 2: join() - Most Efficient for Multiple Strings")
print("="*70)

words = ["Python", "is", "awesome"]
print(f"Word list: {words}")

# Join with space
sentence = " ".join(words)
print(f"Joined with space: '{sentence}'")

# Join with different separators
comma_separated = ", ".join(words)
print(f"Comma separated: '{comma_separated}'")

dash_separated = " - ".join(words)
print(f"Dash separated: '{dash_separated}'")

# Join with no separator
mashed = "".join(words)
print(f"No separator: '{mashed}'")
print()

# Example 3: F-Strings (Python 3.6+)
print("="*70)
print("Example 3: F-Strings - Modern String Formatting")
print("="*70)

name = "Alice"
age = 30
city = "New York"

# Basic f-string
intro = f"My name is {name} and I am {age} years old."
print(intro)

# Multiple variables
full_intro = f"{name} is {age} years old and lives in {city}."
print(full_intro)

# Expressions inside f-strings
print(f"{name} will be {age + 1} next year.")

# Formatting numbers
price = 19.99
print(f"Price: ${price:.2f}")

# Multi-line f-string
message = f"""
Name: {name}
Age: {age}
City: {city}
Status: {'Adult' if age >= 18 else 'Minor'}
"""
print(message)
print()

# Example 4: format() Method
print("="*70)
print("Example 4: format() Method - Template-Based")
print("="*70)

template = "Hello, {}! You have {} new messages."
message = template.format("Bob", 5)
print(message)

# Named placeholders
named_template = "Hello, {name}! You have {count} new messages."
named_message = named_template.format(name="Charlie", count=3)
print(named_message)

# Positional arguments
result = "{0} + {1} = {2}".format(5, 3, 5+3)
print(result)

# Reusing arguments
repeated = "{0} {1} {0}".format("Python", "is")
print(repeated)
print()

# Example 5: % Operator (Old Style)
print("="*70)
print("Example 5: % Operator - C-Style Formatting")
print("="*70)

name = "David"
score = 95

# String substitution
message = "Hello, %s!" % name
print(message)

# Multiple substitutions
result = "%s scored %d points." % (name, score)
print(result)

# Formatted numbers
pi = 3.14159265359
formatted_pi = "Pi: %.2f" % pi
print(formatted_pi)

# Width and precision
formatted = "Name: %-10s Score: %3d" % (name, score)
print(formatted)
print()

# Example 6: String Builder Pattern (List + Join)
print("="*70)
print("Example 6: Efficient String Building with List")
print("="*70)

# Inefficient way (creates new string each time)
result = ""
for i in range(5):
    result += f"Item {i}, "
print(f"Inefficient result: '{result}'")

# Efficient way (build list, join once)
parts = []
for i in range(5):
    parts.append(f"Item {i}")
efficient_result = ", ".join(parts)
print(f"Efficient result: '{efficient_result}'")

# Even better: list comprehension + join
best_result = ", ".join([f"Item {i}" for i in range(5)])
print(f"Best result: '{best_result}'")
print()

# Example 7: Concatenating with Non-Strings
print("="*70)
print("Example 7: Mixing Strings with Other Types")
print("="*70)

# Must convert to string first
age = 25
# This would error: message = "Age: " + age

# Correct approaches
message1 = "Age: " + str(age)
print(f"Using str(): '{message1}'")

message2 = f"Age: {age}"
print(f"Using f-string: '{message2}'")

message3 = "Age: {}".format(age)
print(f"Using format(): '{message3}'")

# Multiple types
name = "Eve"
age = 28
height = 5.6
info = f"{name} is {age} years old and {height} feet tall"
print(f"\\nMixed types: '{info}'")
print()

# Example 8: Multiline String Concatenation
print("="*70)
print("Example 8: Building Multiline Strings")
print("="*70)

# Implicit concatenation
multiline1 = ("This is a very long string that "
              "spans multiple lines for "
              "better readability.")
print("Implicit concatenation:")
print(multiline1)

# Triple quotes
multiline2 = """This is a
multiline string using
triple quotes."""
print("\\nTriple quotes:")
print(multiline2)

# Join with newlines
lines = ["First line", "Second line", "Third line"]
multiline3 = "\\n".join(lines)
print("\\nJoin with newlines:")
print(multiline3)
print()

# Example 9: Performance Comparison
print("="*70)
print("Example 9: Performance Characteristics")
print("="*70)

import time

# Test with 1000 concatenations
iterations = 1000

# Using + operator
start = time.perf_counter()
result = ""
for i in range(iterations):
    result = result + "x"
plus_time = time.perf_counter() - start

# Using join
start = time.perf_counter()
result = "".join(["x" for i in range(iterations)])
join_time = time.perf_counter() - start

# Using list append + join
start = time.perf_counter()
parts = []
for i in range(iterations):
    parts.append("x")
result = "".join(parts)
list_join_time = time.perf_counter() - start

print(f"Iterations: {iterations}")
print(f"+ operator: {plus_time*1000:.4f}ms")
print(f"join (list comp): {join_time*1000:.4f}ms")
print(f"append + join: {list_join_time*1000:.4f}ms")
print("\\njoin() is much faster for multiple concatenations!")
print()

# Example 10: Practical Application - Building HTML
print("="*70)
print("Example 10: Real-World Use Case - HTML Generation")
print("="*70)

users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

# Build HTML table
html_parts = ["<table>", "  <tr><th>Name</th><th>Email</th></tr>"]

for user in users:
    row = f"  <tr><td>{user['name']}</td><td>{user['email']}</td></tr>"
    html_parts.append(row)

html_parts.append("</table>")

# Join all parts
html = "\\n".join(html_parts)
print("Generated HTML:")
print(html)

# Alternative: single f-string
print("\\nAlternative with f-string:")
table = f"""<table>
  <tr><th>Name</th><th>Email</th></tr>
{chr(10).join(f'  <tr><td>{u["name"]}</td><td>{u["email"]}</td></tr>' for u in users)}
</table>"""
print(table)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. + operator - Simple but creates new string each time")
print("2. join() - Most efficient for multiple strings")
print("3. f-strings - Most readable, Python 3.6+")
print("4. format() - Template-based, good for reuse")
print("5. % operator - Old style, still works")
print("6. List + join pattern - Best for loops/iterations")
print("7. Must convert non-strings with str()")
print("8. join() is O(n), repeated + is O(n²)")
print("9. Use f-strings for readability, join() for performance")
print("10. Implicit concatenation for long literals")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 66-70:")
print(f"  66: Reverse a List - {len(lesson66['fullSolution'])} chars")
print(f"  67: Sorting Lists - {len(lesson67['fullSolution'])} chars")
print(f"  68: Sum of List Elements - {len(lesson68['fullSolution'])} chars")
print(f"  69: Working with Multiple Arrays: Merging and Intersection - {len(lesson69['fullSolution'])} chars")
print(f"  70: String Concatenation - {len(lesson70['fullSolution'])} chars")
print("\nBatch 66-70 complete!")
