#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

upgrades = {
    6: '''"""
Boolean Logic - True and False

Master boolean values and logical operations.
Foundation for all conditional logic in programming.

**Zero Package Installation Required**
"""

# Example 1: Boolean Values
print("="*70)
print("Example 1: True and False")
print("="*70)

is_sunny = True
is_raining = False

print(f"Is sunny? {is_sunny}")
print(f"Is raining? {is_raining}")

# Example 2: Comparison Operators
print("\\n" + "="*70)
print("Example 2: Comparisons Return Booleans")
print("="*70)

age = 25
print(f"age = {age}")
print(f"age > 18: {age > 18}")
print(f"age < 30: {age < 30}")
print(f"age == 25: {age == 25}")
print(f"age != 30: {age != 30}")

# Example 3: Boolean in Conditionals
print("\\n" + "="*70)
print("Example 3: Using Booleans in If Statements")
print("="*70)

has_ticket = True
is_vip = False

if has_ticket:
    print("Welcome to the event!")
else:
    print("Please purchase a ticket")

if is_vip:
    print("VIP access granted")
else:
    print("Standard access")

# Example 4: Boolean Variables
print("\\n" + "="*70)
print("Example 4: Storing Boolean State")
print("="*70)

is_logged_in = False
is_admin = False

print(f"User logged in? {is_logged_in}")
print(f"User is admin? {is_admin}")

# Simulate login
is_logged_in = True
print(f"\\nAfter login: {is_logged_in}")

# Example 5: Boolean Functions
print("\\n" + "="*70)
print("Example 5: Functions Returning Booleans")
print("="*70)

def is_even(number):
    return number % 2 == 0

def is_positive(number):
    return number > 0

print(f"Is 10 even? {is_even(10)}")
print(f"Is 7 even? {is_even(7)}")
print(f"Is 5 positive? {is_positive(5)}")
print(f"Is -3 positive? {is_positive(-3)}")

# Example 6: Truthy and Falsy
print("\\n" + "="*70)
print("Example 6: Truthy and Falsy Values")
print("="*70)

# Falsy values
print("Falsy values:")
print(f"  bool(0) = {bool(0)}")
print(f"  bool('') = {bool('')}")
print(f"  bool(None) = {bool(None)}")
print(f"  bool([]) = {bool([])}")

# Truthy values
print("\\nTruthy values:")
print(f"  bool(1) = {bool(1)}")
print(f"  bool('text') = {bool('text')}")
print(f"  bool([1, 2]) = {bool([1, 2])}")

# Example 7: Boolean in Loops
print("\\n" + "="*70)
print("Example 7: Booleans Control Loops")
print("="*70)

running = True
count = 0

while running:
    print(f"Count: {count}")
    count += 1
    if count >= 5:
        running = False

print("Loop stopped")

# Example 8: Multiple Conditions
print("\\n" + "="*70)
print("Example 8: Combining with AND/OR")
print("="*70)

age = 25
has_license = True

can_drive = age >= 16 and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive? {can_drive}")

# Example 9: Negation
print("\\n" + "="*70)
print("Example 9: NOT Operator")
print("="*70)

is_open = True
is_closed = not is_open

print(f"Store open: {is_open}")
print(f"Store closed: {is_closed}")

# Example 10: Practical Application
print("\\n" + "="*70)
print("Example 10: User Access Control")
print("="*70)

is_authenticated = True
has_permission = True
account_active = True

can_access = is_authenticated and has_permission and account_active

print(f"Authenticated: {is_authenticated}")
print(f"Has permission: {has_permission}")
print(f"Account active: {account_active}")
print(f"\\nAccess granted: {can_access}")

print("\\n" + "="*70)
print("Boolean Logic Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Only two values: True and False")
print("  - Comparisons return booleans")
print("  - Used in if/while statements")
print("  - Can combine with and/or/not")
print("  - Foundation of program logic")
''',

    10: '''"""
Integer Division and Modulo

Master integer division (//) and modulo (%) operators.
Essential for math operations, loops, and algorithms.

**Zero Package Installation Required**
"""

# Example 1: Regular vs Integer Division
print("="*70)
print("Example 1: Division Operators")
print("="*70)

# Regular division (/)
print("Regular division (/):")
print(f"  10 / 3 = {10 / 3}")
print(f"  20 / 4 = {20 / 4}")

# Integer division (//)
print("\\nInteger division (//):")
print(f"  10 // 3 = {10 // 3}")
print(f"  20 // 4 = {20 // 4}")

# Example 2: Modulo Operator
print("\\n" + "="*70)
print("Example 2: Modulo (Remainder)")
print("="*70)

print("Modulo (%):")
print(f"  10 % 3 = {10 % 3}")
print(f"  20 % 4 = {20 % 4}")
print(f"  15 % 5 = {15 % 5}")
print(f"  7 % 2 = {7 % 2}")

# Example 3: Even/Odd Detection
print("\\n" + "="*70)
print("Example 3: Check Even or Odd")
print("="*70)

numbers = [10, 15, 22, 37, 44]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Example 4: Dividing Items into Groups
print("\\n" + "="*70)
print("Example 4: Divide into Groups")
print("="*70)

total_items = 25
items_per_box = 6

boxes_needed = total_items // items_per_box
items_remaining = total_items % items_per_box

print(f"Total items: {total_items}")
print(f"Items per box: {items_per_box}")
print(f"Boxes needed: {boxes_needed}")
print(f"Items remaining: {items_remaining}")

# Example 5: Time Calculations
print("\\n" + "="*70)
print("Example 5: Convert Minutes to Hours")
print("="*70)

total_minutes = 185

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"Total: {total_minutes} minutes")
print(f"Equals: {hours} hours and {minutes} minutes")

# Example 6: Cycling Through Values
print("\\n" + "="*70)
print("Example 6: Wrap Around with Modulo")
print("="*70)

# Days of week cycle
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(10):
    day_index = i % 7
    print(f"Day {i}: {days[day_index]}")

# Example 7: Splitting Money
print("\\n" + "="*70)
print("Example 7: Distribute Money Evenly")
print("="*70)

total_money = 100
people = 3

per_person = total_money // people
leftover = total_money % people

print(f"Total: ${total_money}")
print(f"People: {people}")
print(f"Each gets: ${per_person}")
print(f"Leftover: ${leftover}")

# Example 8: Digit Extraction
print("\\n" + "="*70)
print("Example 8: Extract Last Digit")
print("="*70)

number = 12345

last_digit = number % 10
remaining = number // 10

print(f"Number: {number}")
print(f"Last digit: {last_digit}")
print(f"Remaining: {remaining}")

# Example 9: Check Divisibility
print("\\n" + "="*70)
print("Example 9: Check if Divisible")
print("="*70)

def is_divisible_by(number, divisor):
    return number % divisor == 0

num = 30
print(f"Is {num} divisible by:")
print(f"  2? {is_divisible_by(num, 2)}")
print(f"  3? {is_divisible_by(num, 3)}")
print(f"  5? {is_divisible_by(num, 5)}")
print(f"  7? {is_divisible_by(num, 7)}")

# Example 10: Array Index Wrapping
print("\\n" + "="*70)
print("Example 10: Circular Array Access")
print("="*70)

colors = ["Red", "Green", "Blue"]

for i in range(8):
    index = i % len(colors)
    print(f"Position {i}: {colors[index]}")

print("\\n" + "="*70)
print("Integer Division & Modulo Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - // gives whole number result")
print("  - % gives remainder")
print("  - Perfect for even/odd checks")
print("  - Useful for grouping items")
print("  - Essential for cycling/wrapping")
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

print("\\nBatch complete!")
