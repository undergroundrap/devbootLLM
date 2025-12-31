#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 31: Continue in Loops
lesson31 = next(l for l in lessons if l['id'] == 31)
lesson31['fullSolution'] = '''"""
Continue in Loops - Skip Iterations

Master skipping loop iterations with continue statement.
Essential for filtering and conditional processing.

**Zero Package Installation Required**
"""

# Example 1: Basic Continue
print("="*70)
print("Example 1: Skip Even Numbers")
print("="*70)

for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  Odd: {i}")

# Example 2: Skip Specific Value
print("\\n" + "="*70)
print("Example 2: Skip Number 5")
print("="*70)

for i in range(10):
    if i == 5:
        continue
    print(f"  Processing: {i}")

# Example 3: Filter List
print("\\n" + "="*70)
print("Example 3: Process Only Positives")
print("="*70)

numbers = [5, -2, 8, -1, 3, 0, -7]

for num in numbers:
    if num <= 0:
        continue
    print(f"  Positive: {num}")

# Example 4: Skip Empty Strings
print("\\n" + "="*70)
print("Example 4: Ignore Empty Values")
print("="*70)

items = ["apple", "", "banana", "", "cherry"]

for item in items:
    if not item:
        continue
    print(f"  Item: {item}")

# Example 5: Skip Errors
print("\\n" + "="*70)
print("Example 5: Skip Invalid Data")
print("="*70)

data = ["10", "20", "bad", "30", "wrong"]

for value in data:
    try:
        number = int(value)
    except ValueError:
        continue
    print(f"  Valid number: {number}")

# Example 6: Process Valid Scores
print("\\n" + "="*70)
print("Example 6: Skip Out of Range")
print("="*70)

scores = [85, 105, 72, -5, 90, 110]

for score in scores:
    if score < 0 or score > 100:
        print(f"  Skipping invalid: {score}")
        continue
    print(f"  Valid score: {score}")

# Example 7: Skip Comments
print("\\n" + "="*70)
print("Example 7: Ignore Comment Lines")
print("="*70)

lines = [
    "x = 10",
    "# This is a comment",
    "y = 20",
    "# Another comment",
    "z = 30"
]

for line in lines:
    if line.startswith("#"):
        continue
    print(f"  Code: {line}")

# Example 8: Sum Positive Numbers
print("\\n" + "="*70)
print("Example 8: Calculate Sum of Positives")
print("="*70)

numbers = [5, -2, 8, -1, 3, -4, 7]
total = 0

for num in numbers:
    if num < 0:
        continue
    total += num

print(f"Sum of positives: {total}")

# Example 9: While with Continue
print("\\n" + "="*70)
print("Example 9: Continue in While Loop")
print("="*70)

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(f"  Not divisible by 3: {i}")

# Example 10: Multiple Conditions
print("\\n" + "="*70)
print("Example 10: Complex Filtering")
print("="*70)

values = [12, 5, 18, 3, 21, 8, 25]

for val in values:
    if val < 10:
        continue
    if val % 2 != 0:
        continue
    print(f"  Value >= 10 and even: {val}")

print("\\n" + "="*70)
print("Continue in Loops Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - continue skips to next iteration")
print("  - Skips remaining code in loop body")
print("  - Useful for filtering")
print("  - Works with for and while")
print("  - Loop continues normally")
'''

# Lesson 32: Date Formatting
lesson32 = next(l for l in lessons if l['id'] == 32)
lesson32['fullSolution'] = '''"""
Date Formatting - Display Dates and Times

Master formatting dates and times for display.
Essential for user interfaces and reports.

**Zero Package Installation Required**
"""

from datetime import datetime

# Example 1: Basic Date Formatting
print("="*70)
print("Example 1: Format Current Date")
print("="*70)

now = datetime.now()

print(f"Default: {now}")
print(f"Date only: {now.date()}")
print(f"Time only: {now.time()}")

# Example 2: Custom Format Strings
print("\\n" + "="*70)
print("Example 2: strftime Formatting")
print("="*70)

date = datetime(2024, 3, 15, 14, 30, 45)

print(f"Full: {date.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"US Format: {date.strftime('%m/%d/%Y')}")
print(f"EU Format: {date.strftime('%d/%m/%Y')}")
print(f"12-hour: {date.strftime('%I:%M %p')}")

# Example 3: Common Formats
print("\\n" + "="*70)
print("Example 3: Popular Date Formats")
print("="*70)

dt = datetime(2024, 12, 25, 18, 30)

print(f"ISO 8601: {dt.strftime('%Y-%m-%d')}")
print(f"Long date: {dt.strftime('%B %d, %Y')}")
print(f"Short date: {dt.strftime('%b %d, %Y')}")
print(f"Weekday: {dt.strftime('%A, %B %d, %Y')}")

# Example 4: Time Formatting
print("\\n" + "="*70)
print("Example 4: Time Format Options")
print("="*70)

time = datetime(2024, 1, 1, 14, 30, 45)

print(f"24-hour: {time.strftime('%H:%M:%S')}")
print(f"12-hour: {time.strftime('%I:%M:%S %p')}")
print(f"Hour only: {time.strftime('%I %p')}")

# Example 5: Custom Text in Format
print("\\n" + "="*70)
print("Example 5: Include Custom Text")
print("="*70)

date = datetime(2024, 7, 4)

print(date.strftime("Date: %Y-%m-%d"))
print(date.strftime("Month: %B"))
print(date.strftime("It is %A"))

# Example 6: Format for Logging
print("\\n" + "="*70)
print("Example 6: Log Timestamp Format")
print("="*70)

now = datetime.now()
log_format = now.strftime("[%Y-%m-%d %H:%M:%S]")

print(f"{log_format} Application started")
print(f"{log_format} User logged in")

# Example 7: File Name with Date
print("\\n" + "="*70)
print("Example 7: Date in Filename")
print("="*70)

now = datetime.now()
filename = now.strftime("backup_%Y%m%d_%H%M%S.sql")

print(f"Backup file: {filename}")

# Example 8: Birthday Display
print("\\n" + "="*70)
print("Example 8: Human-Readable Date")
print("="*70)

birthday = datetime(1990, 5, 15)

format1 = birthday.strftime("%B %d, %Y")
format2 = birthday.strftime("%A, %B %d, %Y")

print(f"Short: {format1}")
print(f"Long: {format2}")

# Example 9: Format Components
print("\\n" + "="*70)
print("Example 9: Format Codes Reference")
print("="*70)

dt = datetime(2024, 3, 15, 14, 30, 45)

print("Common format codes:")
print(f"  %Y (year): {dt.strftime('%Y')}")
print(f"  %m (month): {dt.strftime('%m')}")
print(f"  %d (day): {dt.strftime('%d')}")
print(f"  %H (hour 24): {dt.strftime('%H')}")
print(f"  %M (minute): {dt.strftime('%M')}")
print(f"  %S (second): {dt.strftime('%S')}")

# Example 10: Parse and Reformat
print("\\n" + "="*70)
print("Example 10: Convert Date Format")
print("="*70)

date_str = "2024-03-15"
dt = datetime.strptime(date_str, "%Y-%m-%d")
new_format = dt.strftime("%B %d, %Y")

print(f"Original: {date_str}")
print(f"Reformatted: {new_format}")

print("\\n" + "="*70)
print("Date Formatting Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - strftime() formats datetime objects")
print("  - %Y for year, %m for month, %d for day")
print("  - %H for 24-hour, %I for 12-hour time")
print("  - %B for full month, %b for short")
print("  - Build custom formats easily")
'''

# Lesson 33: For Loops
lesson33 = next(l for l in lessons if l['id'] == 33)
lesson33['fullSolution'] = '''"""
For Loops - Iteration Fundamentals

Master for loops to iterate over sequences and ranges.
Foundation of repetitive tasks in programming.

**Zero Package Installation Required**
"""

# Example 1: Basic Range Loop
print("="*70)
print("Example 1: Count 0 to 4")
print("="*70)

for i in range(5):
    print(f"  i = {i}")

# Example 2: Start and Stop
print("\\n" + "="*70)
print("Example 2: Count 1 to 10")
print("="*70)

for i in range(1, 11):
    print(f"  Number: {i}")

# Example 3: With Step
print("\\n" + "="*70)
print("Example 3: Count by Twos")
print("="*70)

for i in range(0, 11, 2):
    print(f"  Even: {i}")

# Example 4: Iterate List
print("\\n" + "="*70)
print("Example 4: Loop Through List")
print("="*70)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"  Fruit: {fruit}")

# Example 5: Iterate String
print("\\n" + "="*70)
print("Example 5: Each Character")
print("="*70)

word = "Python"

for char in word:
    print(f"  Char: {char}")

# Example 6: Sum Numbers
print("\\n" + "="*70)
print("Example 6: Calculate Sum")
print("="*70)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 7: Count Items
print("\\n" + "="*70)
print("Example 7: Count Occurrences")
print("="*70)

items = ["a", "b", "a", "c", "a"]
count = 0

for item in items:
    if item == "a":
        count += 1

print(f"Count of 'a': {count}")

# Example 8: Print Table
print("\\n" + "="*70)
print("Example 8: Multiplication Table")
print("="*70)

for i in range(1, 6):
    result = 5 * i
    print(f"  5 x {i} = {result}")

# Example 9: Build List
print("\\n" + "="*70)
print("Example 9: Create Squares List")
print("="*70)

squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(f"Squares: {squares}")

# Example 10: Enumerate for Index
print("\\n" + "="*70)
print("Example 10: Loop with Index")
print("="*70)

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

print("\\n" + "="*70)
print("For Loops Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - for item in sequence:")
print("  - range(n) gives 0 to n-1")
print("  - range(start, stop, step)")
print("  - Iterate lists, strings, ranges")
print("  - Most common loop type")
'''

# Lesson 34: For-Each Over a List
lesson34 = next(l for l in lessons if l['id'] == 34)
lesson34['fullSolution'] = '''"""
For-Each Over a List - List Iteration

Master iterating over list elements directly.
Essential pattern for processing collections.

**Zero Package Installation Required**
"""

# Example 1: Basic For-Each
print("="*70)
print("Example 1: Print Each Item")
print("="*70)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"  {fruit}")

# Example 2: Process Numbers
print("\\n" + "="*70)
print("Example 2: Double Each Number")
print("="*70)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    doubled = num * 2
    print(f"  {num} * 2 = {doubled}")

# Example 3: Calculate Total
print("\\n" + "="*70)
print("Example 3: Sum All Items")
print("="*70)

prices = [19.99, 24.99, 14.99]
total = 0

for price in prices:
    total += price

print(f"Prices: {prices}")
print(f"Total: ${total:.2f}")

# Example 4: Find Maximum
print("\\n" + "="*70)
print("Example 4: Find Highest Score")
print("="*70)

scores = [85, 92, 78, 95, 88]
max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score

print(f"Scores: {scores}")
print(f"Highest: {max_score}")

# Example 5: Filter List
print("\\n" + "="*70)
print("Example 5: Find All Evens")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Original: {numbers}")
print(f"Evens: {evens}")

# Example 6: String Processing
print("\\n" + "="*70)
print("Example 6: Uppercase Names")
print("="*70)

names = ["alice", "bob", "charlie"]

for name in names:
    upper = name.upper()
    print(f"  {name} -> {upper}")

# Example 7: Count Matching
print("\\n" + "="*70)
print("Example 7: Count Long Words")
print("="*70)

words = ["hi", "hello", "hey", "greetings"]
count = 0

for word in words:
    if len(word) >= 5:
        count += 1

print(f"Words >= 5 chars: {count}")

# Example 8: Build New List
print("\\n" + "="*70)
print("Example 8: Square Each Number")
print("="*70)

numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# Example 9: Search for Item
print("\\n" + "="*70)
print("Example 9: Find Target")
print("="*70)

items = ["a", "b", "c", "d"]
target = "c"
found = False

for item in items:
    if item == target:
        found = True
        break

print(f"Looking for '{target}': {'Found' if found else 'Not found'}")

# Example 10: Multi-Line Processing
print("\\n" + "="*70)
print("Example 10: Format Output")
print("="*70)

users = ["Alice", "Bob", "Charlie"]

for user in users:
    print(f"  User: {user}")
    print(f"    Length: {len(user)}")

print("\\n" + "="*70)
print("For-Each Over List Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - for item in list:")
print("  - Direct access to each element")
print("  - No index needed (usually)")
print("  - Most Pythonic way to iterate")
print("  - Cleaner than index-based loops")
'''

# Lesson 35: Loop Accumulator Patterns
lesson35 = next(l for l in lessons if l['id'] == 35)
lesson35['fullSolution'] = '''"""
Loop Accumulator Patterns - Aggregate Data

Master accumulator patterns for calculations and aggregations.
Essential for sums, counts, and building collections.

**Zero Package Installation Required**
"""

# Example 1: Sum Accumulator
print("="*70)
print("Example 1: Total Sum")
print("="*70)

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print(f"Numbers: {numbers}")
print(f"Sum: {total}")

# Example 2: Count Accumulator
print("\\n" + "="*70)
print("Example 2: Count Items")
print("="*70)

items = ["a", "b", "a", "c", "a", "b"]
count_a = 0

for item in items:
    if item == "a":
        count_a += 1

print(f"Items: {items}")
print(f"Count of 'a': {count_a}")

# Example 3: Product Accumulator
print("\\n" + "="*70)
print("Example 3: Multiply All")
print("="*70)

numbers = [2, 3, 4, 5]
product = 1

for num in numbers:
    product *= num

print(f"Numbers: {numbers}")
print(f"Product: {product}")

# Example 4: List Accumulator
print("\\n" + "="*70)
print("Example 4: Build Filtered List")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(f"Evens: {evens}")

# Example 5: String Accumulator
print("\\n" + "="*70)
print("Example 5: Concatenate Strings")
print("="*70)

words = ["Hello", "World", "Python"]
sentence = ""

for word in words:
    sentence += word + " "

print(f"Sentence: {sentence.strip()}")

# Example 6: Maximum Accumulator
print("\\n" + "="*70)
print("Example 6: Find Maximum")
print("="*70)

scores = [85, 92, 78, 95, 88]
max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score = score

print(f"Scores: {scores}")
print(f"Maximum: {max_score}")

# Example 7: Average Calculation
print("\\n" + "="*70)
print("Example 7: Calculate Average")
print("="*70)

grades = [85, 90, 78, 92, 88]
total = 0

for grade in grades:
    total += grade

average = total / len(grades)

print(f"Grades: {grades}")
print(f"Average: {average:.1f}")

# Example 8: Dictionary Accumulator
print("\\n" + "="*70)
print("Example 8: Count Frequencies")
print("="*70)

letters = ["a", "b", "a", "c", "b", "a"]
counts = {}

for letter in letters:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

print(f"Frequencies: {counts}")

# Example 9: Running Total
print("\\n" + "="*70)
print("Example 9: Cumulative Sum")
print("="*70)

values = [10, 20, 30, 40]
cumulative = []
total = 0

for value in values:
    total += value
    cumulative.append(total)

print(f"Values: {values}")
print(f"Cumulative: {cumulative}")

# Example 10: Multiple Accumulators
print("\\n" + "="*70)
print("Example 10: Track Multiple Stats")
print("="*70)

numbers = [1, -2, 3, -4, 5, -6]
positives = 0
negatives = 0
sum_all = 0

for num in numbers:
    sum_all += num
    if num > 0:
        positives += 1
    elif num < 0:
        negatives += 1

print(f"Numbers: {numbers}")
print(f"Positives: {positives}")
print(f"Negatives: {negatives}")
print(f"Sum: {sum_all}")

print("\\n" + "="*70)
print("Loop Accumulator Patterns Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Initialize before loop")
print("  - Update inside loop")
print("  - Use after loop")
print("  - Common patterns: sum, count, list")
print("  - Essential for aggregations")
'''

# Save all changes
for lesson in [lesson31, lesson32, lesson33, lesson34, lesson35]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 31-35:")
print(f"  31: Continue in Loops - {len(lesson31['fullSolution'])} chars")
print(f"  32: Date Formatting - {len(lesson32['fullSolution'])} chars")
print(f"  33: For Loops - {len(lesson33['fullSolution'])} chars")
print(f"  34: For-Each Over a List - {len(lesson34['fullSolution'])} chars")
print(f"  35: Loop Accumulator Patterns - {len(lesson35['fullSolution'])} chars")
print("\\nBatch 31-35 complete!")
