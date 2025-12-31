#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

upgrades = {
    7: '''"""
Boolean Logic - AND Operator

Master the AND operator for combining conditions.
Both conditions must be True for the result to be True.

**Zero Package Installation Required**
"""

# Example 1: Basic AND Logic
print("="*70)
print("Example 1: AND Truth Table")
print("="*70)

print("AND operator (both must be True):")
print(f"  True and True = {True and True}")
print(f"  True and False = {True and False}")
print(f"  False and True = {False and True}")
print(f"  False and False = {False and False}")

# Example 2: Age and License Check
print("\\n" + "="*70)
print("Example 2: Driving Eligibility")
print("="*70)

age = 25
has_license = True

can_drive = age >= 16 and has_license

print(f"Age: {age}")
print(f"Has license: {has_license}")
print(f"Can drive: {can_drive}")

# Example 3: Multiple Conditions
print("\\n" + "="*70)
print("Example 3: Three Conditions")
print("="*70)

is_authenticated = True
has_permission = True
account_active = True

can_access = is_authenticated and has_permission and account_active

print(f"Authenticated: {is_authenticated}")
print(f"Has permission: {has_permission}")
print(f"Account active: {account_active}")
print(f"Can access: {can_access}")

# Example 4: Range Checking
print("\\n" + "="*70)
print("Example 4: Check if in Range")
print("="*70)

score = 85
passing = score >= 60 and score <= 100

print(f"Score: {score}")
print(f"Passing (60-100): {passing}")

# Better way using chained comparison
passing2 = 60 <= score <= 100
print(f"Using chained: {passing2}")

# Example 5: Input Validation
print("\\n" + "="*70)
print("Example 5: Validate User Input")
print("="*70)

username = "alice"
password = "secret123"

username_valid = len(username) >= 3 and len(username) <= 20
password_valid = len(password) >= 8

credentials_ok = username_valid and password_valid

print(f"Username length: {len(username)} (3-20 required)")
print(f"Password length: {len(password)} (8+ required)")
print(f"Credentials valid: {credentials_ok}")

# Example 6: Business Hours
print("\\n" + "="*70)
print("Example 6: Check Business Hours")
print("="*70)

hour = 14  # 2 PM
is_weekday = True

is_open = (9 <= hour < 17) and is_weekday

print(f"Current hour: {hour}")
print(f"Is weekday: {is_weekday}")
print(f"Store open: {is_open}")

# Example 7: Combining with OR
print("\\n" + "="*70)
print("Example 7: AND with OR")
print("="*70)

age = 15
has_adult = True
has_ticket = True

can_enter = (age >= 18 or has_adult) and has_ticket

print(f"Age: {age}")
print(f"With adult: {has_adult}")
print(f"Has ticket: {has_ticket}")
print(f"Can enter: {can_enter}")

# Example 8: Short-Circuit Evaluation
print("\\n" + "="*70)
print("Example 8: Short-Circuit Behavior")
print("="*70)

def check1():
    print("  Checking condition 1...")
    return False

def check2():
    print("  Checking condition 2...")
    return True

print("With AND, if first is False, second not evaluated:")
result = check1() and check2()
print(f"Result: {result}")

print("\\n" + "="*70)
print("Boolean AND Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Both conditions must be True")
print("  - Returns False if any is False")
print("  - Short-circuits on first False")
print("  - Perfect for multi-requirement checks")
''',

    8: '''"""
Boolean Logic - NOT Operator

Master the NOT operator for inverting boolean values.
Flips True to False and False to True.

**Zero Package Installation Required**
"""

# Example 1: Basic NOT Logic
print("="*70)
print("Example 1: NOT Truth Table")
print("="*70)

print("NOT operator (inverts the value):")
print(f"  not True = {not True}")
print(f"  not False = {not False}")

# Example 2: Inverting Conditions
print("\\n" + "="*70)
print("Example 2: Opposite Conditions")
print("="*70)

is_open = True
is_closed = not is_open

print(f"Store open: {is_open}")
print(f"Store closed: {is_closed}")

is_raining = False
is_sunny = not is_raining

print(f"\\nIs raining: {is_raining}")
print(f"Is sunny: {is_sunny}")

# Example 3: NOT with Comparisons
print("\\n" + "="*70)
print("Example 3: Negate Comparisons")
print("="*70)

age = 15

is_adult = age >= 18
is_minor = not is_adult

print(f"Age: {age}")
print(f"Is adult: {is_adult}")
print(f"Is minor: {is_minor}")

# Example 4: NOT with AND/OR
print("\\n" + "="*70)
print("Example 4: Combining with AND/OR")
print("="*70)

logged_in = True
is_admin = False

is_guest = not logged_in
is_regular_user = logged_in and not is_admin

print(f"Logged in: {logged_in}")
print(f"Is admin: {is_admin}")
print(f"Is guest: {is_guest}")
print(f"Is regular user: {is_regular_user}")

# Example 5: Double Negation
print("\\n" + "="*70)
print("Example 5: Double NOT")
print("="*70)

value = True
result = not not value

print(f"Original: {value}")
print(f"not value: {not value}")
print(f"not not value: {result}")

# Example 6: Validation with NOT
print("\\n" + "="*70)
print("Example 6: Error Detection")
print("="*70)

username = ""
password = "abc"

username_invalid = not username  # Empty string is falsy
password_too_short = not (len(password) >= 8)

print(f"Username: '{username}'")
print(f"Username invalid (empty): {username_invalid}")
print(f"\\nPassword: '{password}'")
print(f"Password too short: {password_too_short}")

# Example 7: Access Control
print("\\n" + "="*70)
print("Example 7: Deny Access")
print("="*70)

is_banned = False
account_active = True

can_login = not is_banned and account_active

print(f"User banned: {is_banned}")
print(f"Account active: {account_active}")
print(f"Can login: {can_login}")

# Example 8: Toggle Pattern
print("\\n" + "="*70)
print("Example 8: Toggle Boolean")
print("="*70)

light_on = False
print(f"Light initially: {light_on}")

# Toggle
light_on = not light_on
print(f"After toggle: {light_on}")

# Toggle again
light_on = not light_on
print(f"After toggle again: {light_on}")

# Example 9: NOT with Empty Collections
print("\\n" + "="*70)
print("Example 9: Check if Not Empty")
print("="*70)

list1 = []
list2 = [1, 2, 3]

print(f"list1: {list1}")
print(f"list1 is empty: {not list1}")

print(f"\\nlist2: {list2}")
print(f"list2 is empty: {not list2}")

# Example 10: NOT in Conditions
print("\\n" + "="*70)
print("Example 10: IF with NOT")
print("="*70)

has_errors = False

if not has_errors:
    print("Processing successful!")
else:
    print("Errors found!")

is_complete = True

if not is_complete:
    print("Task still in progress")
else:
    print("Task finished!")

print("\\n" + "="*70)
print("Boolean NOT Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - NOT inverts boolean values")
print("  - not True = False")
print("  - not False = True")
print("  - Useful for opposite conditions")
print("  - Can toggle states")
''',

    9: '''"""
Boolean Logic - OR Operator

Master the OR operator for alternative conditions.
Only one condition needs to be True for the result to be True.

**Zero Package Installation Required**
"""

# Example 1: Basic OR Logic
print("="*70)
print("Example 1: OR Truth Table")
print("="*70)

print("OR operator (at least one must be True):")
print(f"  True or True = {True or True}")
print(f"  True or False = {True or False}")
print(f"  False or True = {False or True}")
print(f"  False or False = {False or False}")

# Example 2: Weekend Check
print("\\n" + "="*70)
print("Example 2: Is it the Weekend?")
print("="*70)

day = "Saturday"

is_weekend = (day == "Saturday") or (day == "Sunday")

print(f"Day: {day}")
print(f"Is weekend: {is_weekend}")

# Example 3: Multiple Payment Methods
print("\\n" + "="*70)
print("Example 3: Accept Multiple Options")
print("="*70)

has_cash = False
has_card = True
has_mobile_pay = False

can_pay = has_cash or has_card or has_mobile_pay

print(f"Has cash: {has_cash}")
print(f"Has card: {has_card}")
print(f"Has mobile pay: {has_mobile_pay}")
print(f"Can pay: {can_pay}")

# Example 4: Entry Requirements
print("\\n" + "="*70)
print("Example 4: Flexible Requirements")
print("="*70)

age = 15
with_parent = True

can_enter = (age >= 18) or with_parent

print(f"Age: {age}")
print(f"With parent: {with_parent}")
print(f"Can enter: {can_enter}")

# Example 5: Emergency Override
print("\\n" + "="*70)
print("Example 5: Emergency Access")
print("="*70)

is_authorized = False
is_emergency = True

allow_access = is_authorized or is_emergency

print(f"Authorized: {is_authorized}")
print(f"Emergency: {is_emergency}")
print(f"Access allowed: {allow_access}")

# Example 6: Valid File Types
print("\\n" + "="*70)
print("Example 6: Check File Type")
print("="*70)

filename = "document.pdf"

is_pdf = filename.endswith(".pdf")
is_doc = filename.endswith(".doc")
is_txt = filename.endswith(".txt")

is_valid = is_pdf or is_doc or is_txt

print(f"Filename: {filename}")
print(f"Valid file type: {is_valid}")

# Example 7: Combining OR with AND
print("\\n" + "="*70)
print("Example 7: OR with AND")
print("="*70)

age = 65
is_student = False

gets_discount = (age < 18 or age >= 65) or is_student

print(f"Age: {age}")
print(f"Is student: {is_student}")
print(f"Gets discount: {gets_discount}")

# Example 8: Short-Circuit Evaluation
print("\\n" + "="*70)
print("Example 8: Short-Circuit Behavior")
print("="*70)

def check1():
    print("  Checking condition 1...")
    return True

def check2():
    print("  Checking condition 2...")
    return False

print("With OR, if first is True, second not evaluated:")
result = check1() or check2()
print(f"Result: {result}")

# Example 9: Default Values
print("\\n" + "="*70)
print("Example 9: OR for Default Values")
print("="*70)

user_name = ""
display_name = user_name or "Guest"

print(f"User name: '{user_name}'")
print(f"Display name: '{display_name}'")

user_name2 = "Alice"
display_name2 = user_name2 or "Guest"

print(f"\\nUser name: '{user_name2}'")
print(f"Display name: '{display_name2}'")

# Example 10: Multiple Conditions
print("\\n" + "="*70)
print("Example 10: Complex Conditions")
print("="*70)

role = "admin"

has_access = (role == "admin") or (role == "moderator") or (role == "editor")

print(f"Role: {role}")
print(f"Has access: {has_access}")

print("\\n" + "="*70)
print("Boolean OR Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - At least one must be True")
print("  - Returns True if any is True")
print("  - Short-circuits on first True")
print("  - Perfect for alternative options")
print("  - Can provide default values")
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

print("\\nBatch 7-9 complete!")
