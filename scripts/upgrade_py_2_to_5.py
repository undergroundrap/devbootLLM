#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 2: Print Debugging
lesson2 = next(l for l in lessons if l['id'] == 2)
lesson2['fullSolution'] = '''"""
Print Debugging - Finding and Fixing Bugs

Learn to use print() to debug code and track program flow.
Essential skill for understanding what your code is doing.

**Zero Package Installation Required**
"""

# Example 1: Tracking Variable Values
print("="*70)
print("Example 1: Track Variable Changes")
print("="*70)

x = 10
print(f"Debug: x = {x}")

x = x + 5
print(f"Debug: After adding 5, x = {x}")

x = x * 2
print(f"Debug: After multiplying by 2, x = {x}")

# Example 2: Debugging Calculations
print("\\n" + "="*70)
print("Example 2: Debug Complex Calculations")
print("="*70)

price = 100
quantity = 3
tax_rate = 0.08

print(f"Debug: price = {price}")
print(f"Debug: quantity = {quantity}")
print(f"Debug: tax_rate = {tax_rate}")

subtotal = price * quantity
print(f"Debug: subtotal = {subtotal}")

tax = subtotal * tax_rate
print(f"Debug: tax = {tax}")

total = subtotal + tax
print(f"Debug: total = {total}")

# Example 3: Debugging Loops
print("\\n" + "="*70)
print("Example 3: Debug Loop Execution")
print("="*70)

print("Debug: Starting loop...")
for i in range(5):
    print(f"  Debug: iteration {i}, value = {i * 2}")
print("Debug: Loop finished")

# Example 4: Debugging Conditionals
print("\\n" + "="*70)
print("Example 4: Debug If Statements")
print("="*70)

score = 85
print(f"Debug: Checking score {score}")

if score >= 90:
    print("Debug: In >= 90 branch")
    grade = "A"
elif score >= 80:
    print("Debug: In >= 80 branch")
    grade = "B"
else:
    print("Debug: In else branch")
    grade = "C"

print(f"Debug: Final grade = {grade}")

# Example 5: Debugging Functions
print("\\n" + "="*70)
print("Example 5: Debug Function Calls")
print("="*70)

def calculate_discount(price, percent):
    print(f"  Debug: Function called with price={price}, percent={percent}")
    discount = price * (percent / 100)
    print(f"  Debug: Calculated discount = {discount}")
    return discount

original_price = 200
discount_percent = 15

print("Debug: Calling function...")
discount_amount = calculate_discount(original_price, discount_percent)
print(f"Debug: Function returned {discount_amount}")

final_price = original_price - discount_amount
print(f"Debug: Final price = {final_price}")

# Example 6: Debugging Data Structures
print("\\n" + "="*70)
print("Example 6: Debug Lists and Dicts")
print("="*70)

numbers = [10, 20, 30, 40, 50]
print(f"Debug: numbers = {numbers}")
print(f"Debug: First element = {numbers[0]}")
print(f"Debug: Last element = {numbers[-1]}")
print(f"Debug: Length = {len(numbers)}")

person = {"name": "Alice", "age": 25}
print(f"\\nDebug: person = {person}")
print(f"Debug: name = {person['name']}")

# Example 7: Finding Errors
print("\\n" + "="*70)
print("Example 7: Debug to Find Errors")
print("="*70)

numerator = 100
denominator = 5

print(f"Debug: numerator = {numerator}")
print(f"Debug: denominator = {denominator}")

if denominator != 0:
    print("Debug: Safe to divide")
    result = numerator / denominator
    print(f"Debug: result = {result}")
else:
    print("Debug: ERROR - Cannot divide by zero!")

print("\\n" + "="*70)
print("Print Debugging Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Add print() to see variable values")
print("  - Print before and after operations")
print("  - Use descriptive messages")
print("  - Remove debug prints in production")
print("  - Essential for understanding code flow")
'''

# Lesson 3: Writing Good Comments
lesson3 = next(l for l in lessons if l['id'] == 3)
lesson3['fullSolution'] = '''"""
Writing Good Comments - Code Documentation

Learn to write clear, helpful comments that explain WHY, not WHAT.
Essential for maintainability and team collaboration.

**Zero Package Installation Required**
"""

# Example 1: Bad vs Good Comments
print("="*70)
print("Example 1: Bad vs Good Comments")
print("="*70)

# BAD: States the obvious
x = 5  # Set x to 5

# GOOD: Explains why
max_retries = 5  # Retry up to 5 times before failing

# BAD: Redundant
price = price * 0.9  # Multiply price by 0.9

# GOOD: Explains business logic
price = price * 0.9  # Apply 10% loyalty discount

print("Good comments explain WHY, not WHAT")

# Example 2: Document Complex Logic
print("\\n" + "="*70)
print("Example 2: Explain Complex Logic")
print("="*70)

# Calculate shipping: base + (weight * $0.50/lb) + (distance * $0.10/mi)
weight = 10  # pounds
distance = 100  # miles

shipping = 5.00 + (weight * 0.50) + (distance * 0.10)
print(f"Shipping cost: ${shipping}")

# Example 3: Function Documentation
print("\\n" + "="*70)
print("Example 3: Document Functions")
print("="*70)

def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters

    Returns:
        BMI value (float)

    Formula: weight / (height^2)
    """
    return weight_kg / (height_m ** 2)

bmi = calculate_bmi(70, 1.75)
print(f"BMI: {bmi:.1f}")

# Example 4: TODO and FIXME
print("\\n" + "="*70)
print("Example 4: TODO Comments")
print("="*70)

# TODO: Add error handling for negative prices
# FIXME: This fails when price is 0
# NOTE: Assumes USD currency

price = 100
discount = 0.2
final_price = price * (1 - discount)

print(f"Price after discount: ${final_price}")

# Example 5: Section Headers
print("\\n" + "="*70)
print("Example 5: Organize with Headers")
print("="*70)

# ============================================
# DATA LOADING
# ============================================

data = [1, 2, 3, 4, 5]
print(f"Loaded {len(data)} items")

# ============================================
# CALCULATIONS
# ============================================

total = sum(data)
average = total / len(data)

print(f"Total: {total}, Average: {average}")

# Example 6: When NOT to Comment
print("\\n" + "="*70)
print("Example 6: Don't Comment Obvious Code")
print("="*70)

# DON'T DO THIS:
# Loop from 0 to 4
# for i in range(5):
#     print(i)

# DO THIS: Only comment non-obvious parts
# Process users by priority (sorted by join date)
users = ["Alice", "Bob", "Charlie"]
for user in users:
    print(f"Processing {user}")

# Example 7: Inline vs Block Comments
print("\\n" + "="*70)
print("Example 7: Comment Types")
print("="*70)

# Block comment: Explain larger sections
# Compound interest formula: A = P(1 + r/n)^(nt)
# P=principal, r=rate, n=compounds/year, t=years

principal = 1000
rate = 0.05  # Inline: Quick explanation
years = 5

amount = principal * (1 + rate/12) ** (12 * years)
print(f"Future value: ${amount:.2f}")

print("\\n" + "="*70)
print("Good Comments Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Explain WHY, not WHAT")
print("  - Comment complex logic")
print("  - Use docstrings for functions")
print("  - Keep comments updated")
print("  - Don't comment obvious code")
'''

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 2-3:")
print(f"  2: Print Debugging (153 -> {len(lesson2['fullSolution'])} chars)")
print(f"  3: Comments (169 -> {len(lesson3['fullSolution'])} chars)")
