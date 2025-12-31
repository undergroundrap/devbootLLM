#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 26: Nested If
lesson26 = next(l for l in lessons if l['id'] == 26)
lesson26['fullSolution'] = '''"""
Nested If Statements - Complex Logic Trees

Master nested conditionals for multi-level decision making.
Essential for complex business logic and validation.

**Zero Package Installation Required**
"""

# Example 1: Basic Nested If
print("="*70)
print("Example 1: Two-Level Check")
print("="*70)

age = 25
has_license = True

if age >= 18:
    print("Age requirement met")
    if has_license:
        print("Can drive!")
    else:
        print("Need license")
else:
    print("Too young to drive")

# Example 2: Grade and Attendance
print("\\n" + "="*70)
print("Example 2: Multiple Criteria")
print("="*70)

grade = 85
attendance = 92

if grade >= 60:
    print("Passing grade")
    if attendance >= 90:
        print("Excellent attendance!")
        print("Gets certificate")
    else:
        print("Needs better attendance")
else:
    print("Failing grade")

# Example 3: Access Levels
print("\\n" + "="*70)
print("Example 3: Tiered Permissions")
print("="*70)

is_logged_in = True
is_admin = False
is_premium = True

if is_logged_in:
    print("Access granted")
    if is_admin:
        print("Admin dashboard available")
    else:
        print("Regular user")
        if is_premium:
            print("Premium features unlocked")
        else:
            print("Basic features only")
else:
    print("Please log in")

# Example 4: Number Range Classification
print("\\n" + "="*70)
print("Example 4: Range Validation")
print("="*70)

score = 75

if score >= 0:
    if score <= 100:
        print(f"Valid score: {score}")
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        else:
            print("Grade: C or below")
    else:
        print("Score too high")
else:
    print("Score cannot be negative")

# Example 5: Shopping Cart Discount
print("\\n" + "="*70)
print("Example 5: Nested Discount Logic")
print("="*70)

total = 150
is_member = True
coupon_code = "SAVE10"

discount = 0

if total >= 100:
    if is_member:
        discount += 0.10
        print("Member discount: 10%")
    if coupon_code == "SAVE10":
        discount += 0.10
        print("Coupon discount: 10%")

final_total = total * (1 - discount)
print(f"Total: ${total}")
print(f"Final: ${final_total:.2f}")

# Example 6: Weather Advisory
print("\\n" + "="*70)
print("Example 6: Nested Weather Logic")
print("="*70)

temperature = 95
humidity = 75

if temperature > 90:
    print("Heat warning!")
    if humidity > 70:
        print("High humidity - heat index dangerous")
        print("Stay indoors")
    else:
        print("Low humidity - stay hydrated")
else:
    print("Temperature comfortable")

# Example 7: Login Validation
print("\\n" + "="*70)
print("Example 7: Multi-Step Validation")
print("="*70)

username = "alice"
password = "secret123"
account_active = True

if len(username) >= 3:
    if len(password) >= 8:
        if account_active:
            print("Login successful!")
        else:
            print("Account is inactive")
    else:
        print("Password too short")
else:
    print("Username too short")

print("\\n" + "="*70)
print("Nested If Statements Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Indent each level further")
print("  - Check outer condition first")
print("  - Can mix if/elif/else at any level")
print("  - Keep nesting depth reasonable")
print("  - Consider using elif when possible")
'''

# Lesson 27: Simple If
lesson27 = next(l for l in lessons if l['id'] == 27)
lesson27['fullSolution'] = '''"""
Simple If Statements - Basic Conditionals

Master the simplest form of conditional logic.
Foundation for all decision-making in programming.

**Zero Package Installation Required**
"""

# Example 1: Single Condition
print("="*70)
print("Example 1: Basic If Statement")
print("="*70)

temperature = 85

if temperature > 80:
    print("It's hot outside!")

print("Program continues...")

# Example 2: Age Check
print("\\n" + "="*70)
print("Example 2: Adult Check")
print("="*70)

age = 25

if age >= 18:
    print("You are an adult")

# Example 3: Positive Number
print("\\n" + "="*70)
print("Example 3: Number Check")
print("="*70)

number = 42

if number > 0:
    print(f"{number} is positive")

# Example 4: String Length
print("\\n" + "="*70)
print("Example 4: Password Strength")
print("="*70)

password = "mysecretpassword"

if len(password) >= 8:
    print("Password meets minimum length")

# Example 5: List Not Empty
print("\\n" + "="*70)
print("Example 5: Check List Has Items")
print("="*70)

items = ["apple", "banana", "cherry"]

if len(items) > 0:
    print(f"Found {len(items)} items")

# Example 6: Even Number
print("\\n" + "="*70)
print("Example 6: Even Check")
print("="*70)

num = 10

if num % 2 == 0:
    print(f"{num} is even")

# Example 7: Stock Warning
print("\\n" + "="*70)
print("Example 7: Low Stock Alert")
print("="*70)

stock = 3

if stock <= 5:
    print(f"Warning: Only {stock} items left!")

# Example 8: Multiple Simple Ifs
print("\\n" + "="*70)
print("Example 8: Independent Checks")
print("="*70)

score = 95

if score >= 90:
    print("Excellent performance!")

if score >= 80:
    print("Good job!")

if score >= 60:
    print("You passed!")

# Example 9: String Contains
print("\\n" + "="*70)
print("Example 9: Search for Text")
print("="*70)

message = "Hello, World!"

if "World" in message:
    print("Found 'World' in message")

# Example 10: Boolean Flag
print("\\n" + "="*70)
print("Example 10: Flag Check")
print("="*70)

is_logged_in = True

if is_logged_in:
    print("Welcome back!")

print("\\n" + "="*70)
print("Simple If Statements Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Runs code block if condition is True")
print("  - No else needed")
print("  - Colon (:) required")
print("  - Indent with 4 spaces")
print("  - Simplest form of conditional")
'''

# Lesson 28: Try-except with specific exception
lesson28 = next(l for l in lessons if l['id'] == 28)
lesson28['fullSolution'] = '''"""
Try-Except with Specific Exceptions

Master handling specific error types for robust code.
Essential for graceful error handling and recovery.

**Zero Package Installation Required**
"""

# Example 1: Catch ValueError
print("="*70)
print("Example 1: Handle ValueError")
print("="*70)

user_input = "not a number"

try:
    number = int(user_input)
    print(f"Converted to: {number}")
except ValueError:
    print("Error: Invalid number format")

# Example 2: Catch ZeroDivisionError
print("\\n" + "="*70)
print("Example 2: Handle Division by Zero")
print("="*70)

def safe_divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None

safe_divide(10, 2)
safe_divide(10, 0)

# Example 3: Catch IndexError
print("\\n" + "="*70)
print("Example 3: Handle List Index Errors")
print("="*70)

numbers = [1, 2, 3]

try:
    value = numbers[5]
    print(f"Value: {value}")
except IndexError:
    print("Error: Index out of range")

# Example 4: Catch KeyError
print("\\n" + "="*70)
print("Example 4: Handle Missing Dictionary Key")
print("="*70)

user = {"name": "Alice", "age": 25}

try:
    email = user["email"]
    print(f"Email: {email}")
except KeyError:
    print("Error: Email not found")

# Example 5: Catch TypeError
print("\\n" + "="*70)
print("Example 5: Handle Type Errors")
print("="*70)

try:
    result = "hello" + 5
    print(result)
except TypeError:
    print("Error: Cannot add string and int")

# Example 6: Multiple Try-Except
print("\\n" + "="*70)
print("Example 6: Different Operations")
print("="*70)

def process_data(data):
    try:
        num = int(data)
        print(f"Processed: {num}")
    except ValueError:
        print(f"'{data}' is not a valid number")

process_data("42")
process_data("abc")

# Example 7: With Error Message
print("\\n" + "="*70)
print("Example 7: Show Error Details")
print("="*70)

try:
    value = int("bad")
except ValueError as e:
    print(f"Error details: {e}")

print("\\n" + "="*70)
print("Try-Except Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - try: code that might fail")
print("  - except ExceptionType: error handler")
print("  - Specify exact exception type")
print("  - Use 'as e' for error details")
print("  - Program continues after handling")
'''

# Lesson 29: Match-Case
lesson29 = next(l for l in lessons if l['id'] == 29)
lesson29['fullSolution'] = '''"""
Match-Case Statement (Python 3.10+)

Master pattern matching with match-case statements.
Modern alternative to long if-elif chains.

**Zero Package Installation Required**
**Requires Python 3.10 or later**
"""

# Example 1: Basic Match-Case
print("="*70)
print("Example 1: Simple Pattern Matching")
print("="*70)

status_code = 200

match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

# Example 2: Day of Week
print("\\n" + "="*70)
print("Example 2: Match Days")
print("="*70)

day = "Monday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Invalid day")

# Example 3: HTTP Method
print("\\n" + "="*70)
print("Example 3: Match Request Type")
print("="*70)

method = "GET"

match method:
    case "GET":
        print("Fetching data")
    case "POST":
        print("Creating data")
    case "PUT":
        print("Updating data")
    case "DELETE":
        print("Deleting data")
    case _:
        print("Unknown method")

# Example 4: Grade Conversion
print("\\n" + "="*70)
print("Example 4: Grade to GPA")
print("="*70)

grade = "B"

match grade:
    case "A":
        gpa = 4.0
    case "B":
        gpa = 3.0
    case "C":
        gpa = 2.0
    case "D":
        gpa = 1.0
    case _:
        gpa = 0.0

print(f"Grade {grade} = {gpa} GPA")

# Example 5: Command Router
print("\\n" + "="*70)
print("Example 5: Match Commands")
print("="*70)

command = "start"

match command:
    case "start":
        print("Starting application...")
    case "stop":
        print("Stopping application...")
    case "restart":
        print("Restarting application...")
    case "status":
        print("Application is running")
    case _:
        print(f"Unknown command: {command}")

# Example 6: Multiple Values (OR)
print("\\n" + "="*70)
print("Example 6: Match Multiple Values")
print("="*70)

color = "red"

match color:
    case "red" | "orange" | "yellow":
        print("Warm color")
    case "blue" | "green" | "purple":
        print("Cool color")
    case _:
        print("Neutral color")

# Example 7: Fallthrough with Default
print("\\n" + "="*70)
print("Example 7: Default Case")
print("="*70)

value = 999

match value:
    case 1:
        result = "One"
    case 2:
        result = "Two"
    case 3:
        result = "Three"
    case _:
        result = "Many"

print(f"Value {value} is: {result}")

print("\\n" + "="*70)
print("Match-Case Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Modern alternative to if-elif")
print("  - Use | for multiple patterns")
print("  - _ is the default case")
print("  - More readable than long if chains")
print("  - Requires Python 3.10+")
'''

# Lesson 30: Break in Loops
lesson30 = next(l for l in lessons if l['id'] == 30)
lesson30['fullSolution'] = '''"""
Break in Loops - Early Exit

Master breaking out of loops when a condition is met.
Essential for search operations and early termination.

**Zero Package Installation Required**
"""

# Example 1: Basic Break
print("="*70)
print("Example 1: Stop at 5")
print("="*70)

for i in range(10):
    if i == 5:
        print("Found 5, stopping!")
        break
    print(f"  i = {i}")

# Example 2: Search for Item
print("\\n" + "="*70)
print("Example 2: Find in List")
print("="*70)

fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == target:
        print(f"Found {target}!")
        break

# Example 3: First Even Number
print("\\n" + "="*70)
print("Example 3: Find First Even")
print("="*70)

numbers = [1, 3, 5, 8, 9, 11]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number: {num}")
        break
    print(f"  {num} is odd")

# Example 4: While with Break
print("\\n" + "="*70)
print("Example 4: Input Validation")
print("="*70)

count = 0
while True:
    count += 1
    print(f"  Attempt {count}")
    if count >= 3:
        print("Max attempts reached")
        break

# Example 5: Password Check
print("\\n" + "="*70)
print("Example 5: Find Correct Password")
print("="*70)

attempts = ["wrong1", "wrong2", "correct", "wrong3"]
correct_password = "correct"

for attempt in attempts:
    print(f"Trying: {attempt}")
    if attempt == correct_password:
        print("Access granted!")
        break
    print("  Wrong password")

# Example 6: Negative Number Search
print("\\n" + "="*70)
print("Example 6: First Negative")
print("="*70)

values = [5, 10, -3, 8, -1]

for value in values:
    if value < 0:
        print(f"First negative: {value}")
        break
    print(f"  {value} is positive")

# Example 7: Break in Nested Loop
print("\\n" + "="*70)
print("Example 7: Break from Inner Loop")
print("="*70)

for i in range(3):
    print(f"Outer: {i}")
    for j in range(5):
        if j == 2:
            print("  Breaking inner loop")
            break
        print(f"  Inner: {j}")

print("\\n" + "="*70)
print("Break in Loops Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - break exits the loop immediately")
print("  - Useful for search operations")
print("  - Stops checking remaining items")
print("  - Works with for and while")
print("  - Only exits innermost loop")
'''

# Save all changes
for lesson in [lesson26, lesson27, lesson28, lesson29, lesson30]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 26-30:")
print(f"  26: Nested If - {len(lesson26['fullSolution'])} chars")
print(f"  27: Simple If - {len(lesson27['fullSolution'])} chars")
print(f"  28: Try-except - {len(lesson28['fullSolution'])} chars")
print(f"  29: Match-Case - {len(lesson29['fullSolution'])} chars")
print(f"  30: Break in Loops - {len(lesson30['fullSolution'])} chars")
print("\\nBatch 26-30 complete!")
