#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

upgrades = {
    11: '''"""
Arithmetic & Assignment Operators

Master arithmetic operations and assignment shortcuts in Python.
Essential for calculations, counters, and data manipulation.

**Zero Package Installation Required**
"""

# Example 1: Basic Arithmetic
print("="*70)
print("Example 1: Fundamental Operations")
print("="*70)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Example 2: Assignment Shortcuts
print("\\n" + "="*70)
print("Example 2: Compound Assignment")
print("="*70)

counter = 0
print(f"Initial: counter = {counter}")

counter += 5  # Same as: counter = counter + 5
print(f"After += 5: counter = {counter}")

counter -= 2  # Same as: counter = counter - 2
print(f"After -= 2: counter = {counter}")

counter *= 3  # Same as: counter = counter * 3
print(f"After *= 3: counter = {counter}")

counter //= 2  # Same as: counter = counter // 2
print(f"After //= 2: counter = {counter}")

# Example 3: Accumulator Pattern
print("\\n" + "="*70)
print("Example 3: Running Total")
print("="*70)

total = 0
prices = [19.99, 34.50, 12.25, 45.00]

print("Adding prices to total:")
for price in prices:
    total += price
    print(f"  Added ${price:.2f}, total now: ${total:.2f}")

print(f"\\nFinal total: ${total:.2f}")

# Example 4: Counter Pattern
print("\\n" + "="*70)
print("Example 4: Counting Items")
print("="*70)

count = 0
items = ["apple", "banana", "apple", "orange", "apple"]

print("Counting apples:")
for item in items:
    if item == "apple":
        count += 1
        print(f"  Found apple, count = {count}")

print(f"\\nTotal apples: {count}")

# Example 5: Multiple Operations
print("\\n" + "="*70)
print("Example 5: Complex Calculations")
print("="*70)

principal = 1000
rate = 0.05
years = 3

# Compound interest: A = P(1 + r)^t
amount = principal * (1 + rate) ** years

print(f"Principal: ${principal}")
print(f"Rate: {rate * 100}%")
print(f"Years: {years}")
print(f"Final amount: ${amount:.2f}")
print(f"Interest earned: ${amount - principal:.2f}")

# Example 6: Score Calculation
print("\\n" + "="*70)
print("Example 6: Average Score")
print("="*70)

score_sum = 0
scores = [85, 92, 78, 95, 88]

print("Scores:", scores)
for score in scores:
    score_sum += score

average = score_sum / len(scores)
print(f"Total: {score_sum}")
print(f"Average: {average:.1f}")

# Example 7: Inventory Management
print("\\n" + "="*70)
print("Example 7: Stock Updates")
print("="*70)

stock = 50
print(f"Initial stock: {stock}")

# Receive shipment
stock += 30
print(f"After receiving 30: {stock}")

# Sell items
stock -= 15
print(f"After selling 15: {stock}")

# Sell more
stock -= 20
print(f"After selling 20: {stock}")

# Example 8: All Assignment Operators
print("\\n" + "="*70)
print("Example 8: All Compound Operators")
print("="*70)

x = 100

print(f"Start: x = {x}")
x += 10
print(f"x += 10: x = {x}")
x -= 5
print(f"x -= 5: x = {x}")
x *= 2
print(f"x *= 2: x = {x}")
x //= 3
print(f"x //= 3: x = {x}")
x %= 7
print(f"x %= 7: x = {x}")
x **= 2
print(f"x **= 2: x = {x}")

# Example 9: Temperature Conversion
print("\\n" + "="*70)
print("Example 9: Celsius to Fahrenheit")
print("="*70)

celsius = 25
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C = {fahrenheit}°F")

celsius = 0
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

celsius = 100
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Example 10: Distance Calculation
print("\\n" + "="*70)
print("Example 10: Speed, Time, Distance")
print("="*70)

speed = 60  # mph
time = 2.5  # hours

distance = speed * time

print(f"Speed: {speed} mph")
print(f"Time: {time} hours")
print(f"Distance: {distance} miles")

print("\\n" + "="*70)
print("Arithmetic & Assignment Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use +, -, *, /, //, %, ** for math")
print("  - Shortcuts: +=, -=, *=, /=, //=, %=, **=")
print("  - += adds to existing value")
print("  - Use for counters and accumulators")
print("  - Order of operations: PEMDAS")
''',

    12: '''"""
Comparison Operators

Master comparison operators to compare values and make decisions.
Foundation for conditionals, loops, and program logic.

**Zero Package Installation Required**
"""

# Example 1: Basic Comparisons
print("="*70)
print("Example 1: All Comparison Operators")
print("="*70)

a = 10
b = 5

print(f"a = {a}, b = {b}")
print(f"a == b (equal): {a == b}")
print(f"a != b (not equal): {a != b}")
print(f"a > b (greater): {a > b}")
print(f"a < b (less): {a < b}")
print(f"a >= b (greater or equal): {a >= b}")
print(f"a <= b (less or equal): {a <= b}")

# Example 2: String Comparisons
print("\\n" + "="*70)
print("Example 2: Compare Strings")
print("="*70)

name1 = "Alice"
name2 = "Bob"
name3 = "Alice"

print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' == '{name3}': {name1 == name3}")
print(f"'{name1}' != '{name2}': {name1 != name2}")

# Alphabetical comparison
print(f"\\n'{name1}' < '{name2}': {name1 < name2}")
print(f"'{name2}' > '{name1}': {name2 > name1}")

# Example 3: Age Validation
print("\\n" + "="*70)
print("Example 3: Age Requirements")
print("="*70)

age = 25
min_age = 18
max_age = 65

print(f"Age: {age}")
print(f"Is adult (>= 18)? {age >= min_age}")
print(f"Is senior (>= 65)? {age >= max_age}")
print(f"Is working age (18-64)? {age >= min_age and age < max_age}")

# Example 4: Price Comparison
print("\\n" + "="*70)
print("Example 4: Find Best Price")
print("="*70)

price1 = 99.99
price2 = 89.99
price3 = 94.99

print(f"Store A: ${price1}")
print(f"Store B: ${price2}")
print(f"Store C: ${price3}")

print(f"\\nStore B cheaper than A? {price2 < price1}")
print(f"Store B cheapest? {price2 < price1 and price2 < price3}")

# Example 5: Score Grading
print("\\n" + "="*70)
print("Example 5: Grade Determination")
print("="*70)

score = 85

print(f"Score: {score}")
print(f"Is A (>= 90)? {score >= 90}")
print(f"Is B (>= 80)? {score >= 80}")
print(f"Is C (>= 70)? {score >= 70}")
print(f"Is passing (>= 60)? {score >= 60}")

# Example 6: Range Checking
print("\\n" + "="*70)
print("Example 6: Value in Range")
print("="*70)

temperature = 72
min_temp = 68
max_temp = 78

print(f"Temperature: {temperature}°F")
print(f"Above minimum ({min_temp})? {temperature >= min_temp}")
print(f"Below maximum ({max_temp})? {temperature <= max_temp}")
print(f"In comfortable range? {temperature >= min_temp and temperature <= max_temp}")

# Alternative: Chained comparison
in_range = min_temp <= temperature <= max_temp
print(f"Using chained comparison: {in_range}")

# Example 7: Password Validation
print("\\n" + "="*70)
print("Example 7: Password Length Check")
print("="*70)

password1 = "abc"
password2 = "secret123"
min_length = 8

print(f"Password: '{password1}'")
print(f"Length: {len(password1)}")
print(f"Valid (>= {min_length} chars)? {len(password1) >= min_length}")

print(f"\\nPassword: '{password2}'")
print(f"Length: {len(password2)}")
print(f"Valid (>= {min_length} chars)? {len(password2) >= min_length}")

# Example 8: Inventory Status
print("\\n" + "="*70)
print("Example 8: Stock Levels")
print("="*70)

stock = 5
reorder_point = 10

print(f"Current stock: {stock}")
print(f"Reorder point: {reorder_point}")
print(f"Need to reorder? {stock <= reorder_point}")
print(f"Out of stock? {stock == 0}")
print(f"In stock? {stock > 0}")

# Example 9: Multiple Conditions
print("\\n" + "="*70)
print("Example 9: Eligibility Check")
print("="*70)

age = 22
has_license = True
has_car = False

print(f"Age: {age}")
print(f"Has license: {has_license}")
print(f"Has car: {has_car}")

can_drive = age >= 16 and has_license
print(f"\\nCan legally drive? {can_drive}")
can_drive_own_car = age >= 16 and has_license and has_car
print(f"Can drive own car? {can_drive_own_car}")

# Example 10: Finding Maximum
print("\\n" + "="*70)
print("Example 10: Compare Multiple Values")
print("="*70)

score1 = 85
score2 = 92
score3 = 78

print(f"Scores: {score1}, {score2}, {score3}")
print(f"\\nscore1 is highest? {score1 > score2 and score1 > score3}")
print(f"score2 is highest? {score2 > score1 and score2 > score3}")
print(f"score3 is highest? {score3 > score1 and score3 > score2}")

print("\\n" + "="*70)
print("Comparison Operators Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - == checks equality")
print("  - != checks inequality")
print("  - <, >, <=, >= compare values")
print("  - Returns True or False")
print("  - Can chain: a < b < c")
print("  - Essential for if statements")
''',

    13: '''"""
Date Arithmetic - Working with Dates and Times

Master date calculations and time operations using Python's datetime module.
Essential for scheduling, age calculation, and time-based logic.

**Zero Package Installation Required**
"""

from datetime import datetime, timedelta

# Example 1: Current Date and Time
print("="*70)
print("Example 1: Get Current Date/Time")
print("="*70)

now = datetime.now()
print(f"Current date and time: {now}")
print(f"Just date: {now.date()}")
print(f"Just time: {now.time()}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")

# Example 2: Create Specific Dates
print("\\n" + "="*70)
print("Example 2: Create Custom Dates")
print("="*70)

birthday = datetime(1990, 5, 15)
print(f"Birthday: {birthday}")

new_year = datetime(2024, 1, 1)
print(f"New Year 2024: {new_year}")

meeting = datetime(2024, 3, 15, 14, 30)
print(f"Meeting: {meeting}")

# Example 3: Date Differences
print("\\n" + "="*70)
print("Example 3: Calculate Age")
print("="*70)

birth_date = datetime(1990, 6, 15)
today = datetime.now()

age_delta = today - birth_date
days_old = age_delta.days
years_old = days_old // 365

print(f"Born: {birth_date.date()}")
print(f"Today: {today.date()}")
print(f"Days old: {days_old:,}")
print(f"Approximate age: {years_old} years")

# Example 4: Adding Days
print("\\n" + "="*70)
print("Example 4: Future Dates")
print("="*70)

start_date = datetime(2024, 1, 1)
print(f"Start: {start_date.date()}")

# Add 7 days
week_later = start_date + timedelta(days=7)
print(f"One week later: {week_later.date()}")

# Add 30 days
month_later = start_date + timedelta(days=30)
print(f"30 days later: {month_later.date()}")

# Add 365 days
year_later = start_date + timedelta(days=365)
print(f"One year later: {year_later.date()}")

# Example 5: Subtracting Days
print("\\n" + "="*70)
print("Example 5: Past Dates")
print("="*70)

today = datetime(2024, 3, 15)
print(f"Today: {today.date()}")

yesterday = today - timedelta(days=1)
print(f"Yesterday: {yesterday.date()}")

week_ago = today - timedelta(days=7)
print(f"Week ago: {week_ago.date()}")

month_ago = today - timedelta(days=30)
print(f"30 days ago: {month_ago.date()}")

# Example 6: Due Date Calculation
print("\\n" + "="*70)
print("Example 6: Project Deadline")
print("="*70)

project_start = datetime(2024, 1, 15)
project_duration = timedelta(days=45)
deadline = project_start + project_duration

print(f"Project starts: {project_start.date()}")
print(f"Duration: {project_duration.days} days")
print(f"Deadline: {deadline.date()}")

# Example 7: Days Until Event
print("\\n" + "="*70)
print("Example 7: Countdown to Event")
print("="*70)

today = datetime(2024, 1, 1)
event_date = datetime(2024, 7, 4)

days_until = (event_date - today).days
weeks_until = days_until // 7

print(f"Today: {today.date()}")
print(f"Event: {event_date.date()}")
print(f"Days until event: {days_until}")
print(f"Weeks until event: {weeks_until}")

# Example 8: Working with Hours
print("\\n" + "="*70)
print("Example 8: Time Addition")
print("="*70)

start_time = datetime(2024, 1, 1, 9, 0)  # 9:00 AM
print(f"Start: {start_time}")

# Add 4 hours
end_time = start_time + timedelta(hours=4)
print(f"After 4 hours: {end_time}")

# Add 90 minutes
meeting_end = start_time + timedelta(minutes=90)
print(f"After 90 minutes: {meeting_end}")

# Example 9: Business Days
print("\\n" + "="*70)
print("Example 9: 5 Business Days")
print("="*70)

order_date = datetime(2024, 1, 1)  # Monday
shipping_days = 5

delivery_date = order_date + timedelta(days=shipping_days)

print(f"Order placed: {order_date.date()}")
print(f"Estimated delivery: {delivery_date.date()}")
print(f"Days to wait: {shipping_days}")

# Example 10: Date Comparison
print("\\n" + "="*70)
print("Example 10: Check if Date Passed")
print("="*70)

today = datetime(2024, 3, 15)
deadline1 = datetime(2024, 3, 10)
deadline2 = datetime(2024, 3, 20)

print(f"Today: {today.date()}")
print(f"\\nDeadline 1: {deadline1.date()}")
print(f"Has passed? {today > deadline1}")

print(f"\\nDeadline 2: {deadline2.date()}")
print(f"Has passed? {today > deadline2}")
print(f"Days remaining: {(deadline2 - today).days}")

print("\\n" + "="*70)
print("Date Arithmetic Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use datetime.now() for current time")
print("  - datetime(year, month, day) creates dates")
print("  - timedelta() for time differences")
print("  - Add/subtract with + and -")
print("  - .days gets total days")
print("  - Compare dates with <, >, ==")
''',

    14: '''"""
Reading CSV Files - Data Processing

Master CSV file reading and processing using Python's csv module.
Essential for working with spreadsheet data and tabular information.

**Zero Package Installation Required**
"""

import csv
import io

# Example 1: Basic CSV Reading
print("="*70)
print("Example 1: Read CSV File")
print("="*70)

# Simulate CSV file
csv_data = """name,age,city
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago"""

csv_file = io.StringIO(csv_data)
reader = csv.reader(csv_file)

print("Reading CSV data:")
for row in reader:
    print(f"  {row}")

# Example 2: With Headers
print("\\n" + "="*70)
print("Example 2: CSV with Headers")
print("="*70)

csv_file = io.StringIO(csv_data)
reader = csv.reader(csv_file)

headers = next(reader)  # Get first row as headers
print(f"Headers: {headers}")

print("\\nData rows:")
for row in reader:
    print(f"  {row}")

# Example 3: Dictionary Reader
print("\\n" + "="*70)
print("Example 3: Read as Dictionaries")
print("="*70)

csv_file = io.StringIO(csv_data)
reader = csv.DictReader(csv_file)

print("Each row as dictionary:")
for row in reader:
    print(f"  Name: {row['name']}, Age: {row['age']}, City: {row['city']}")

# Example 4: Processing Sales Data
print("\\n" + "="*70)
print("Example 4: Sales Report")
print("="*70)

sales_csv = """product,quantity,price
Laptop,5,999.99
Mouse,20,24.99
Keyboard,15,79.99"""

csv_file = io.StringIO(sales_csv)
reader = csv.DictReader(csv_file)

total_revenue = 0
print("Sales:")
for row in reader:
    quantity = int(row['quantity'])
    price = float(row['price'])
    revenue = quantity * price
    total_revenue += revenue
    print(f"  {row['product']}: {quantity} x ${price} = ${revenue:.2f}")

print(f"\\nTotal Revenue: ${total_revenue:.2f}")

# Example 5: Filtering Data
print("\\n" + "="*70)
print("Example 5: Filter by Condition")
print("="*70)

students_csv = """name,grade,score
Alice,A,95
Bob,B,82
Charlie,A,91
David,C,75"""

csv_file = io.StringIO(students_csv)
reader = csv.DictReader(csv_file)

print("Students with A grade:")
for row in reader:
    if row['grade'] == 'A':
        print(f"  {row['name']}: {row['score']}")

# Example 6: Counting Rows
print("\\n" + "="*70)
print("Example 6: Count Records")
print("="*70)

csv_file = io.StringIO(csv_data)
reader = csv.reader(csv_file)

next(reader)  # Skip header
count = sum(1 for row in reader)

print(f"Total records: {count}")

# Example 7: Find Maximum
print("\\n" + "="*70)
print("Example 7: Find Highest Score")
print("="*70)

csv_file = io.StringIO(students_csv)
reader = csv.DictReader(csv_file)

max_score = 0
top_student = ""

for row in reader:
    score = int(row['score'])
    if score > max_score:
        max_score = score
        top_student = row['name']

print(f"Top student: {top_student}")
print(f"Highest score: {max_score}")

# Example 8: Calculate Average
print("\\n" + "="*70)
print("Example 8: Average Age")
print("="*70)

csv_file = io.StringIO(csv_data)
reader = csv.DictReader(csv_file)

ages = []
for row in reader:
    ages.append(int(row['age']))

average_age = sum(ages) / len(ages)

print(f"Ages: {ages}")
print(f"Average age: {average_age:.1f}")

# Example 9: Group and Count
print("\\n" + "="*70)
print("Example 9: Count by Category")
print("="*70)

inventory_csv = """item,category,quantity
Apple,Fruit,50
Banana,Fruit,30
Carrot,Vegetable,20
Broccoli,Vegetable,15"""

csv_file = io.StringIO(inventory_csv)
reader = csv.DictReader(csv_file)

category_counts = {}
for row in reader:
    category = row['category']
    quantity = int(row['quantity'])

    if category in category_counts:
        category_counts[category] += quantity
    else:
        category_counts[category] = quantity

print("Total by category:")
for category, total in category_counts.items():
    print(f"  {category}: {total}")

# Example 10: Different Delimiter
print("\\n" + "="*70)
print("Example 10: Tab-Separated Values")
print("="*70)

tsv_data = """name\\tage\\tsalary
Alice\\t25\\t50000
Bob\\t30\\t60000"""

csv_file = io.StringIO(tsv_data)
reader = csv.reader(csv_file, delimiter='\\t')

print("Tab-separated data:")
for row in reader:
    print(f"  {row}")

print("\\n" + "="*70)
print("Reading CSV Files Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - csv.reader() reads CSV line by line")
print("  - csv.DictReader() reads as dictionaries")
print("  - First row often contains headers")
print("  - Use next() to skip header row")
print("  - Can specify delimiter for TSV, etc.")
print("  - Perfect for spreadsheet data")
''',

    15: '''"""
Reading Error Messages - Debugging Skills

Master the art of reading and understanding Python error messages.
Essential skill for debugging and fixing code problems.

**Zero Package Installation Required**
"""

# Example 1: NameError
print("="*70)
print("Example 1: NameError - Undefined Variable")
print("="*70)

print("This error occurs when using undefined variables:")
print("Error: NameError: name 'undefined_var' is not defined")
print("\\nHow to fix:")

# Wrong:
# print(undefined_var)  # Would raise NameError

# Right:
undefined_var = "Now it's defined"
print(f"Fixed: {undefined_var}")

# Example 2: TypeError
print("\\n" + "="*70)
print("Example 2: TypeError - Wrong Type")
print("="*70)

print("This error occurs with incompatible types:")
print("Error: TypeError: can only concatenate str (not 'int') to str")
print("\\nHow to fix:")

# Wrong approach would be:
# result = "Age: " + 25  # TypeError

# Right:
age = 25
result = "Age: " + str(age)  # Convert to string
print(f"Fixed: {result}")

# Or use f-string:
result2 = f"Age: {age}"
print(f"Better: {result2}")

# Example 3: IndexError
print("\\n" + "="*70)
print("Example 3: IndexError - Index Out of Range")
print("="*70)

print("This error occurs accessing invalid list index:")
print("Error: IndexError: list index out of range")
print("\\nHow to fix:")

numbers = [10, 20, 30]
print(f"List: {numbers}")
print(f"Length: {len(numbers)}")

# Wrong:
# value = numbers[5]  # IndexError

# Right:
if len(numbers) > 2:
    value = numbers[2]
    print(f"Fixed: numbers[2] = {value}")

# Example 4: KeyError
print("\\n" + "="*70)
print("Example 4: KeyError - Missing Dictionary Key")
print("="*70)

print("This error occurs with missing dict keys:")
print("Error: KeyError: 'age'")
print("\\nHow to fix:")

person = {"name": "Alice", "city": "NYC"}
print(f"Dictionary: {person}")

# Wrong:
# age = person['age']  # KeyError

# Right:
age = person.get('age', 'Not found')
print(f"Fixed with .get(): {age}")

# Or check first:
if 'age' in person:
    age = person['age']
else:
    print("Fixed with check: age key not found")

# Example 5: ValueError
print("\\n" + "="*70)
print("Example 5: ValueError - Invalid Value")
print("="*70)

print("This error occurs converting invalid values:")
print("Error: ValueError: invalid literal for int()")
print("\\nHow to fix:")

# Wrong:
# number = int("not a number")  # ValueError

# Right:
text = "not a number"
try:
    number = int(text)
except ValueError:
    print(f"Fixed: '{text}' is not a valid number")
    number = 0

print(f"Using default: {number}")

# Example 6: ZeroDivisionError
print("\\n" + "="*70)
print("Example 6: ZeroDivisionError")
print("="*70)

print("This error occurs dividing by zero:")
print("Error: ZeroDivisionError: division by zero")
print("\\nHow to fix:")

numerator = 10
denominator = 0

# Wrong:
# result = numerator / denominator  # ZeroDivisionError

# Right:
if denominator != 0:
    result = numerator / denominator
    print(f"Fixed: {result}")
else:
    print("Fixed: Cannot divide by zero")

# Example 7: IndentationError
print("\\n" + "="*70)
print("Example 7: IndentationError")
print("="*70)

print("This error occurs with wrong indentation:")
print("Error: IndentationError: unexpected indent")
print("\\nHow to fix:")
print("\\nWrong:")
print("  if True:")
print("print('Hello')  # Not indented")

print("\\nRight:")
print("  if True:")
print("      print('Hello')  # Properly indented")

# Example 8: AttributeError
print("\\n" + "="*70)
print("Example 8: AttributeError - No Such Attribute")
print("="*70)

print("This error occurs accessing non-existent attributes:")
print("Error: AttributeError: 'str' object has no attribute 'append'")
print("\\nHow to fix:")

# Wrong:
# text = "Hello"
# text.append("!")  # AttributeError

# Right:
text = "Hello"
text = text + "!"  # Use + for strings
print(f"Fixed: {text}")

# Lists have append:
items = ["Hello"]
items.append("!")
print(f"List with append: {items}")

# Example 9: SyntaxError
print("\\n" + "="*70)
print("Example 9: SyntaxError - Invalid Syntax")
print("="*70)

print("This error occurs with syntax mistakes:")
print("Error: SyntaxError: invalid syntax")
print("\\nCommon causes:")
print("  - Missing colons after if/for/def")
print("  - Unmatched parentheses")
print("  - Missing quotes")
print("\\nAlways check the line indicated!")

# Example 10: Reading Stack Traces
print("\\n" + "="*70)
print("Example 10: Understanding Stack Traces")
print("="*70)

print("Stack trace shows error location:")
print("\\nExample trace:")
print("  File 'script.py', line 10, in <module>")
print("    result = divide(10, 0)")
print("  File 'script.py', line 5, in divide")
print("    return a / b")
print("  ZeroDivisionError: division by zero")

print("\\nReading tips:")
print("  1. Start from the bottom (actual error)")
print("  2. Look at line numbers")
print("  3. Read the error message")
print("  4. Check the code at that line")

print("\\n" + "="*70)
print("Reading Error Messages Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Read error messages carefully")
print("  - Check line numbers indicated")
print("  - Understand common error types")
print("  - NameError: undefined variable")
print("  - TypeError: wrong type")
print("  - IndexError: invalid index")
print("  - Practice makes perfect!")
'''
}

for lesson_id, new_solution in upgrades.items():
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)
    if lesson:
        old_len = len(lesson['fullSolution'])
        lesson['fullSolution'] = new_solution
        new_len = len(lesson['fullSolution'])
        print(f"Lesson {lesson_id}: {lesson['title']}")
        print(f"  {old_len} -> {new_len} chars (+{((new_len-old_len)/old_len*100):.1f}%)")

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("\\nBatch 11-15 complete!")
