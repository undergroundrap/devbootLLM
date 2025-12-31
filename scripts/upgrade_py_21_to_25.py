#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 21: Catching Specific Exceptions
lesson21 = next(l for l in lessons if l['id'] == 21)
lesson21['fullSolution'] = '''"""
Catching Specific Exceptions - Error Handling

Master catching specific exception types for precise error handling.
Essential for robust code and graceful error recovery.

**Zero Package Installation Required**
"""

# Example 1: Catch Specific Exception
print("="*70)
print("Example 1: Catch ValueError")
print("="*70)

def convert_to_int(value):
    try:
        result = int(value)
        print(f"Successfully converted '{value}' to {result}")
        return result
    except ValueError:
        print(f"Error: '{value}' is not a valid integer")
        return None

convert_to_int("42")
convert_to_int("not a number")
convert_to_int("100")

# Example 2: Multiple Exception Types
print("\\n" + "="*70)
print("Example 2: Catch Multiple Exceptions")
print("="*70)

def safe_divide(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid types for division")
        return None

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)

# Example 3: Separate Handlers
print("\\n" + "="*70)
print("Example 3: Different Error Messages")
print("="*70)

def access_list(items, index):
    try:
        value = items[index]
        print(f"items[{index}] = {value}")
        return value
    except IndexError:
        print(f"Error: Index {index} out of range")
        return None
    except TypeError:
        print("Error: Invalid index type")
        return None

numbers = [10, 20, 30]
access_list(numbers, 1)
access_list(numbers, 10)
access_list(numbers, "bad")

# Example 4: KeyError Handling
print("\\n" + "="*70)
print("Example 4: Dictionary Key Errors")
print("="*70)

def get_user_info(user_dict, key):
    try:
        value = user_dict[key]
        print(f"{key}: {value}")
        return value
    except KeyError:
        print(f"Error: Key '{key}' not found")
        return None

user = {"name": "Alice", "age": 25}
get_user_info(user, "name")
get_user_info(user, "email")

# Example 5: File Operation Errors
print("\\n" + "="*70)
print("Example 5: FileNotFoundError")
print("="*70)

def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Read {len(content)} characters")
            return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None

# Will fail gracefully
read_file_safe("nonexistent.txt")

# Example 6: Multiple Exceptions Same Handler
print("\\n" + "="*70)
print("Example 6: Group Similar Exceptions")
print("="*70)

def calculate(a, b, operation):
    try:
        if operation == "divide":
            return a / b
        elif operation == "int":
            return int(a)
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"Calculation error: {type(e).__name__}")
        return None

calculate(10, 2, "divide")
calculate(10, 0, "divide")
calculate("bad", None, "int")

# Example 7: Exception with Details
print("\\n" + "="*70)
print("Example 7: Access Exception Details")
print("="*70)

def parse_number(text):
    try:
        return int(text)
    except ValueError as e:
        print(f"ValueError: {e}")
        print(f"Could not parse: '{text}'")
        return 0

parse_number("42")
parse_number("not_a_number")

print("\\n" + "="*70)
print("Catching Specific Exceptions Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Catch specific exceptions")
print("  - Multiple except blocks for different errors")
print("  - Use 'except Type as e' for details")
print("  - Group similar exceptions with tuple")
print("  - More precise than bare except")
'''

# Lesson 22: Compound Conditions
lesson22 = next(l for l in lessons if l['id'] == 22)
lesson22['fullSolution'] = '''"""
Compound Conditions - Complex Logic

Master combining multiple conditions with AND, OR, NOT.
Essential for complex decision making in programs.

**Zero Package Installation Required**
"""

# Example 1: AND Conditions
print("="*70)
print("Example 1: Multiple Requirements (AND)")
print("="*70)

age = 25
has_license = True

can_drive = age >= 18 and has_license

print(f"Age: {age}")
print(f"Has license: {has_license}")
print(f"Can drive: {can_drive}")

# Example 2: OR Conditions
print("\\n" + "="*70)
print("Example 2: Alternative Options (OR)")
print("="*70)

is_weekend = False
is_holiday = True

is_day_off = is_weekend or is_holiday

print(f"Weekend: {is_weekend}")
print(f"Holiday: {is_holiday}")
print(f"Day off: {is_day_off}")

# Example 3: NOT Conditions
print("\\n" + "="*70)
print("Example 3: Negation (NOT)")
print("="*70)

is_raining = False
can_go_outside = not is_raining

print(f"Is raining: {is_raining}")
print(f"Can go outside: {can_go_outside}")

# Example 4: Complex Combinations
print("\\n" + "="*70)
print("Example 4: AND with OR")
print("="*70)

age = 15
with_parent = True
has_ticket = True

can_enter = (age >= 18 or with_parent) and has_ticket

print(f"Age: {age}")
print(f"With parent: {with_parent}")
print(f"Has ticket: {has_ticket}")
print(f"Can enter: {can_enter}")

# Example 5: Grade Evaluation
print("\\n" + "="*70)
print("Example 5: Grade Range Check")
print("="*70)

score = 85

is_excellent = score >= 90 and score <= 100
is_good = score >= 80 and score < 90
is_passing = score >= 60 and score < 80

print(f"Score: {score}")
print(f"Excellent (90-100): {is_excellent}")
print(f"Good (80-89): {is_good}")
print(f"Passing (60-79): {is_passing}")

# Example 6: Access Control
print("\\n" + "="*70)
print("Example 6: User Access Logic")
print("="*70)

is_admin = False
is_moderator = True
is_owner = False

has_access = is_admin or is_moderator or is_owner

print(f"Admin: {is_admin}")
print(f"Moderator: {is_moderator}")
print(f"Owner: {is_owner}")
print(f"Has access: {has_access}")

# Example 7: Eligibility Check
print("\\n" + "="*70)
print("Example 7: Multiple Criteria")
print("="*70)

age = 22
is_student = True
has_id = True

gets_discount = (age < 18 or is_student) and has_id

print(f"Age: {age}")
print(f"Student: {is_student}")
print(f"Has ID: {has_id}")
print(f"Gets discount: {gets_discount}")

print("\\n" + "="*70)
print("Compound Conditions Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - AND: all conditions must be True")
print("  - OR: at least one must be True")
print("  - NOT: inverts the value")
print("  - Use parentheses for clarity")
print("  - Combine for complex logic")
'''

# Lesson 23: If / Else
lesson23 = next(l for l in lessons if l['id'] == 23)
lesson23['fullSolution'] = '''"""
If / Else Statements - Decision Making

Master basic conditional logic with if/else statements.
Foundation for all decision-making in programming.

**Zero Package Installation Required**
"""

# Example 1: Basic If/Else
print("="*70)
print("Example 1: Simple Decision")
print("="*70)

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 2: Positive/Negative Check
print("\\n" + "="*70)
print("Example 2: Number Sign")
print("="*70)

number = -5

if number >= 0:
    print(f"{number} is positive or zero")
else:
    print(f"{number} is negative")

# Example 3: Password Validation
print("\\n" + "="*70)
print("Example 3: Password Length")
print("="*70)

password = "secret"
min_length = 8

if len(password) >= min_length:
    print("Password is strong enough")
else:
    print(f"Password too short. Need {min_length} characters")

# Example 4: Grade Pass/Fail
print("\\n" + "="*70)
print("Example 4: Passing Grade")
print("="*70)

score = 75
passing_score = 60

if score >= passing_score:
    print(f"Congratulations! You passed with {score}")
else:
    print(f"Sorry, you need {passing_score} to pass")

# Example 5: Even/Odd Check
print("\\n" + "="*70)
print("Example 5: Even or Odd")
print("="*70)

number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Example 6: Stock Availability
print("\\n" + "="*70)
print("Example 6: In Stock Check")
print("="*70)

stock_quantity = 0

if stock_quantity > 0:
    print(f"In stock! {stock_quantity} available")
else:
    print("Out of stock")

# Example 7: Temperature Warning
print("\\n" + "="*70)
print("Example 7: Temperature Alert")
print("="*70)

temperature = 95

if temperature > 90:
    print("Heat warning! Stay hydrated")
else:
    print("Temperature is comfortable")

print("\\n" + "="*70)
print("If / Else Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - if: runs when condition is True")
print("  - else: runs when condition is False")
print("  - Indent code blocks with 4 spaces")
print("  - Colon (:) required after if and else")
print("  - Foundation of program logic")
'''

# Lesson 24: If-Elif-Else
lesson24 = next(l for l in lessons if l['id'] == 24)
lesson24['fullSolution'] = '''"""
If-Elif-Else Statements - Multiple Choices

Master handling multiple conditions with elif chains.
Essential for complex decision trees and multiple outcomes.

**Zero Package Installation Required**
"""

# Example 1: Basic If-Elif-Else
print("="*70)
print("Example 1: Three-Way Decision")
print("="*70)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(f"Score: {score}")
print(f"Grade: {grade}")

# Example 2: Multiple Conditions
print("\\n" + "="*70)
print("Example 2: Complete Grading Scale")
print("="*70)

score = 73

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

# Example 3: Time of Day
print("\\n" + "="*70)
print("Example 3: Greeting by Time")
print("="*70)

hour = 14

if hour < 12:
    greeting = "Good morning"
elif hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

print(f"Hour: {hour}")
print(greeting)

# Example 4: Temperature Classification
print("\\n" + "="*70)
print("Example 4: Weather Description")
print("="*70)

temp = 75

if temp >= 90:
    condition = "Hot"
elif temp >= 70:
    condition = "Warm"
elif temp >= 50:
    condition = "Cool"
else:
    condition = "Cold"

print(f"Temperature: {temp}°F")
print(f"Condition: {condition}")

# Example 5: Age Groups
print("\\n" + "="*70)
print("Example 5: Age Categories")
print("="*70)

age = 35

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"Age: {age}")
print(f"Category: {category}")

# Example 6: Traffic Light
print("\\n" + "="*70)
print("Example 6: Traffic Signal")
print("="*70)

light = "yellow"

if light == "red":
    action = "Stop"
elif light == "yellow":
    action = "Slow down"
elif light == "green":
    action = "Go"
else:
    action = "Signal malfunction"

print(f"Light: {light}")
print(f"Action: {action}")

# Example 7: Discount Calculation
print("\\n" + "="*70)
print("Example 7: Tiered Discounts")
print("="*70)

total = 150

if total >= 200:
    discount = 0.20
elif total >= 100:
    discount = 0.10
elif total >= 50:
    discount = 0.05
else:
    discount = 0

savings = total * discount
final = total - savings

print(f"Total: ${total}")
print(f"Discount: {discount * 100}%")
print(f"Savings: ${savings}")
print(f"Final: ${final}")

print("\\n" + "="*70)
print("If-Elif-Else Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - elif: check additional conditions")
print("  - Evaluates top to bottom")
print("  - First True condition wins")
print("  - else is optional fallback")
print("  - Use for multiple outcomes")
'''

# Lesson 25: Modifying List Elements
lesson25 = next(l for l in lessons if l['id'] == 25)
lesson25['fullSolution'] = '''"""
Modifying List Elements - List Manipulation

Master changing values in lists using indexing and methods.
Essential for data manipulation and list operations.

**Zero Package Installation Required**
"""

# Example 1: Change Single Element
print("="*70)
print("Example 1: Modify by Index")
print("="*70)

numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")

numbers[2] = 99
print(f"After changing index 2: {numbers}")

# Example 2: Update Multiple Elements
print("\\n" + "="*70)
print("Example 2: Change Several Items")
print("="*70)

fruits = ["apple", "banana", "cherry", "date"]
print(f"Original: {fruits}")

fruits[1] = "blueberry"
fruits[3] = "dragon fruit"
print(f"Modified: {fruits}")

# Example 3: Increment Values
print("\\n" + "="*70)
print("Example 3: Increase Numbers")
print("="*70)

scores = [10, 20, 30]
print(f"Original scores: {scores}")

scores[0] = scores[0] + 5
scores[1] = scores[1] + 5
scores[2] = scores[2] + 5

print(f"After +5 bonus: {scores}")

# Example 4: Modify in Loop
print("\\n" + "="*70)
print("Example 4: Double All Values")
print("="*70)

values = [1, 2, 3, 4, 5]
print(f"Original: {values}")

for i in range(len(values)):
    values[i] = values[i] * 2

print(f"Doubled: {values}")

# Example 5: Conditional Modification
print("\\n" + "="*70)
print("Example 5: Modify If Condition")
print("="*70)

numbers = [5, 12, 8, 15, 3]
print(f"Original: {numbers}")

for i in range(len(numbers)):
    if numbers[i] > 10:
        numbers[i] = 10

print(f"Capped at 10: {numbers}")

# Example 6: Replace with Calculation
print("\\n" + "="*70)
print("Example 6: Update Prices")
print("="*70)

prices = [100, 200, 150]
print(f"Original prices: {prices}")

# Apply 10% increase
for i in range(len(prices)):
    prices[i] = prices[i] * 1.10

print(f"After 10% increase: {prices}")

# Example 7: Swap Elements
print("\\n" + "="*70)
print("Example 7: Swap Two Items")
print("="*70)

items = ["first", "second", "third"]
print(f"Original: {items}")

# Swap first and last
temp = items[0]
items[0] = items[2]
items[2] = temp

print(f"After swap: {items}")

print("\\n" + "="*70)
print("Modifying List Elements Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use list[index] = value")
print("  - Modify in place changes original")
print("  - Use loops for multiple changes")
print("  - Can use conditions to filter")
print("  - Essential for data updates")
'''

# Save all changes
for lesson in [lesson21, lesson22, lesson23, lesson24, lesson25]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 21-25:")
print(f"  21: Catching Specific Exceptions - {len(lesson21['fullSolution'])} chars")
print(f"  22: Compound Conditions - {len(lesson22['fullSolution'])} chars")
print(f"  23: If / Else - {len(lesson23['fullSolution'])} chars")
print(f"  24: If-Elif-Else - {len(lesson24['fullSolution'])} chars")
print(f"  25: Modifying List Elements - {len(lesson25['fullSolution'])} chars")
print("\\nBatch 21-25 complete!")
