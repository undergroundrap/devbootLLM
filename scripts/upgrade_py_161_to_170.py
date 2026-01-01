#!/usr/bin/env python3
"""
Upgrade Python lessons 161-170 with comprehensive content.
- Lesson 161: Basic Math Operations
- Lesson 162: Break Statement
- Lesson 163: Break and Continue Statements
- Lesson 164: Build a Calculator
- Lesson 165: Build a Contact Book
- Lesson 166: Build a Grade Calculator
- Lesson 167: Build a Guessing Game
- Lesson 168: Comparing Dates
- Lesson 169: Continue Statement
- Lesson 170: Counting Characters
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 161-170
lesson161 = next(l for l in lessons if l['id'] == 161)
lesson162 = next(l for l in lessons if l['id'] == 162)
lesson163 = next(l for l in lessons if l['id'] == 163)
lesson164 = next(l for l in lessons if l['id'] == 164)
lesson165 = next(l for l in lessons if l['id'] == 165)
lesson166 = next(l for l in lessons if l['id'] == 166)
lesson167 = next(l for l in lessons if l['id'] == 167)
lesson168 = next(l for l in lessons if l['id'] == 168)
lesson169 = next(l for l in lessons if l['id'] == 169)
lesson170 = next(l for l in lessons if l['id'] == 170)

# Upgrade Lesson 161: Basic Math Operations
lesson161['fullSolution'] = '''"""
Basic Math Operations

Master fundamental mathematical operations in Python. Learn addition, subtraction,
multiplication, division, modulo, exponentiation, and floor division. Understand
operator precedence, integer vs float division, and common math patterns.

**Zero Package Installation Required**
"""

# Example 1: Basic Arithmetic Operations
print("="*70)
print("Example 1: Basic Arithmetic Operators")
print("="*70)

a = 10
b = 3

print(f"Numbers: a = {a}, b = {b}")
print()
print(f"Addition:       a + b = {a + b}")
print(f"Subtraction:    a - b = {a - b}")
print(f"Multiplication: a * b = {a * b}")
print(f"Division:       a / b = {a / b}")  # Always returns float
print(f"Floor Division: a // b = {a // b}")  # Returns integer part
print(f"Modulo:         a % b = {a % b}")  # Returns remainder
print(f"Exponentiation: a ** b = {a ** b}")  # Power operation
print()

# Example 2: Integer vs Float Division
print("="*70)
print("Example 2: Division Operators - / vs //")
print("="*70)

numbers = [(10, 3), (15, 4), (20, 6), (7, 2)]

print(f"{'a':>5} {'b':>5} {'a / b':>10} {'a // b':>10} {'a % b':>10}")
print("-" * 45)

for a, b in numbers:
    print(f"{a:>5} {b:>5} {a / b:>10.2f} {a // b:>10} {a % b:>10}")
print()

# Example 3: Operator Precedence
print("="*70)
print("Example 3: Operator Precedence (PEMDAS)")
print("="*70)

# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

expr1 = "2 + 3 * 4"
result1 = 2 + 3 * 4
print(f"{expr1:30} = {result1}")

expr2 = "(2 + 3) * 4"
result2 = (2 + 3) * 4
print(f"{expr2:30} = {result2}")

expr3 = "2 ** 3 + 4"
result3 = 2 ** 3 + 4
print(f"{expr3:30} = {result3}")

expr4 = "2 ** (3 + 4)"
result4 = 2 ** (3 + 4)
print(f"{expr4:30} = {result4}")

expr5 = "10 + 20 / 5 * 2 - 3"
result5 = 10 + 20 / 5 * 2 - 3
print(f"{expr5:30} = {result5}")

expr6 = "((10 + 20) / 5) * 2 - 3"
result6 = ((10 + 20) / 5) * 2 - 3
print(f"{expr6:30} = {result6}")
print()

# Example 4: Modulo Operator Applications
print("="*70)
print("Example 4: Modulo Operator - Finding Remainders")
print("="*70)

# Check if number is even or odd
numbers = [10, 15, 22, 33, 44, 57]

print("Even or Odd:")
for num in numbers:
    result = "even" if num % 2 == 0 else "odd"
    print(f"  {num} is {result}")

print()

# Check divisibility
number = 100
divisors = [2, 3, 5, 7, 10]

print(f"Divisibility of {number}:")
for divisor in divisors:
    if number % divisor == 0:
        print(f"  {number} is divisible by {divisor}")
    else:
        remainder = number % divisor
        print(f"  {number} % {divisor} = {remainder}")
print()

# Example 5: Exponentiation - Powers and Roots
print("="*70)
print("Example 5: Exponentiation and Roots")
print("="*70)

# Powers
print("Powers:")
print(f"  2^3 = {2 ** 3}")
print(f"  3^4 = {3 ** 4}")
print(f"  10^2 = {10 ** 2}")
print(f"  5^0 = {5 ** 0}")  # Any number to the power 0 is 1

# Roots using fractional exponents
print()
print("Roots (using fractional exponents):")
print(f"  Square root of 16: 16^0.5 = {16 ** 0.5}")
print(f"  Square root of 25: 25^0.5 = {25 ** 0.5}")
print(f"  Cube root of 27:   27^(1/3) = {27 ** (1/3)}")
print(f"  Cube root of 64:   64^(1/3) = {64 ** (1/3)}")
print()

# Example 6: Negative Numbers
print("="*70)
print("Example 6: Operations with Negative Numbers")
print("="*70)

a = -10
b = 3

print(f"a = {a}, b = {b}")
print()
print(f"  {a} + {b} = {a + b}")
print(f"  {a} - {b} = {a - b}")
print(f"  {a} * {b} = {a * b}")
print(f"  {a} / {b} = {a / b:.2f}")
print(f"  {a} // {b} = {a // b}")
print(f"  {a} % {b} = {a % b}")
print(f"  {a} ** {b} = {a ** b}")

# Modulo with negative numbers
print()
print("Modulo with negative numbers:")
print(f"  -10 % 3 = {-10 % 3}")  # Result has sign of divisor in Python
print(f"  10 % -3 = {10 % -3}")
print(f"  -10 % -3 = {-10 % -3}")
print()

# Example 7: Floating Point Precision
print("="*70)
print("Example 7: Floating Point Arithmetic")
print("="*70)

# Basic float operations
print("Basic floating point operations:")
print(f"  3.14 + 2.86 = {3.14 + 2.86}")
print(f"  10.5 - 3.2 = {10.5 - 3.2}")
print(f"  2.5 * 4.0 = {2.5 * 4.0}")
print(f"  15.0 / 4.0 = {15.0 / 4.0}")

# Precision issues
print()
print("Floating point precision:")
result = 0.1 + 0.2
print(f"  0.1 + 0.2 = {result}")
print(f"  Exact: {result:.20f}")  # Shows precision issues

# Rounding
print()
print("Rounding to handle precision:")
print(f"  round(0.1 + 0.2, 2) = {round(0.1 + 0.2, 2)}")
print(f"  round(3.14159, 2) = {round(3.14159, 2)}")
print(f"  round(10.6) = {round(10.6)}")
print()

# Example 8: Compound Assignment Operators
print("="*70)
print("Example 8: Compound Assignment Operators")
print("="*70)

x = 10
print(f"Initial value: x = {x}")

x += 5  # x = x + 5
print(f"After x += 5:  x = {x}")

x -= 3  # x = x - 3
print(f"After x -= 3:  x = {x}")

x *= 2  # x = x * 2
print(f"After x *= 2:  x = {x}")

x //= 4  # x = x // 4
print(f"After x //= 4: x = {x}")

x **= 2  # x = x ** 2
print(f"After x **= 2: x = {x}")

x %= 7  # x = x % 7
print(f"After x %= 7:  x = {x}")
print()

# Example 9: Common Math Patterns
print("="*70)
print("Example 9: Common Mathematical Patterns")
print("="*70)

# Calculate average
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Numbers: {numbers}")
print(f"Average: {average}")

# Calculate percentage
score = 85
total = 100
percentage = (score / total) * 100
print(f"\\nScore: {score}/{total}")
print(f"Percentage: {percentage}%")

# Calculate tip
bill = 75.50
tip_percent = 15
tip = bill * (tip_percent / 100)
total_bill = bill + tip
print(f"\\nBill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip:.2f}")
print(f"Total: ${total_bill:.2f}")

# Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"\\nTemperature: {celsius}°C = {fahrenheit}°F")

# Calculate area and perimeter of rectangle
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print(f"\\nRectangle: {length} x {width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print()

# Example 10: Practical Application - Mathematical Calculator
print("="*70)
print("Example 10: Real-World Use Case - Basic Calculator")
print("="*70)

class Calculator:
    """Basic calculator with mathematical operations"""

    @staticmethod
    def add(a, b):
        """Add two numbers"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract b from a"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers"""
        return a * b

    @staticmethod
    def divide(a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def floor_divide(a, b):
        """Floor division of a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a // b

    @staticmethod
    def modulo(a, b):
        """Calculate a modulo b"""
        if b == 0:
            raise ValueError("Cannot perform modulo by zero")
        return a % b

    @staticmethod
    def power(base, exponent):
        """Raise base to exponent"""
        return base ** exponent

    @staticmethod
    def percentage(value, total):
        """Calculate percentage"""
        if total == 0:
            raise ValueError("Total cannot be zero")
        return (value / total) * 100

    @staticmethod
    def average(numbers):
        """Calculate average of numbers"""
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)

# Test calculator
calc = Calculator()

print("CALCULATOR OPERATIONS")
print("=" * 70)

# Basic operations
a, b = 15, 4
print(f"Numbers: a = {a}, b = {b}")
print(f"  Add:           {a} + {b} = {calc.add(a, b)}")
print(f"  Subtract:      {a} - {b} = {calc.subtract(a, b)}")
print(f"  Multiply:      {a} * {b} = {calc.multiply(a, b)}")
print(f"  Divide:        {a} / {b} = {calc.divide(a, b):.2f}")
print(f"  Floor Divide:  {a} // {b} = {calc.floor_divide(a, b)}")
print(f"  Modulo:        {a} % {b} = {calc.modulo(a, b)}")
print(f"  Power:         {a} ** {b} = {calc.power(a, b)}")

# Advanced calculations
print()
print("PRACTICAL CALCULATIONS")
print("=" * 70)

# Percentage calculation
score = 42
total_questions = 50
percentage = calc.percentage(score, total_questions)
print(f"Test Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.1f}%")

# Average calculation
grades = [85, 92, 78, 90, 88]
avg = calc.average(grades)
print(f"\\nGrades: {grades}")
print(f"Average: {avg:.2f}")

# Sales tax calculation
price = 49.99
tax_rate = 8.5  # 8.5%
tax = price * (tax_rate / 100)
final_price = price + tax
print(f"\\nPrice: ${price:.2f}")
print(f"Tax ({tax_rate}%): ${tax:.2f}")
print(f"Final Price: ${final_price:.2f}")

# Currency conversion
usd = 100
exchange_rate = 1.25  # USD to EUR
eur = usd * exchange_rate
print(f"\\nCurrency Conversion:")
print(f"  ${usd:.2f} USD = €{eur:.2f} EUR")
print(f"  (Rate: 1 USD = {exchange_rate} EUR)")

# Distance calculation
speed = 60  # mph
time = 2.5  # hours
distance = speed * time
print(f"\\nDistance Calculation:")
print(f"  Speed: {speed} mph")
print(f"  Time: {time} hours")
print(f"  Distance: {distance} miles")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. + (addition), - (subtraction), * (multiplication)")
print("2. / (division - always returns float)")
print("3. // (floor division - returns integer part)")
print("4. % (modulo - returns remainder)")
print("5. ** (exponentiation - power operation)")
print("6. Operator precedence: PEMDAS (Parentheses, Exponents, Mult/Div, Add/Sub)")
print("7. Use // for integer division, / for float division")
print("8. Modulo useful for: even/odd, divisibility, cycling")
print("9. Compound operators: +=, -=, *=, /=, //=, %=, **=")
print("10. round() handles floating point precision issues")
print("="*70)
'''

# Save progress
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Upgrade Lesson 162: Break Statement
lesson162['fullSolution'] = '''"""
Break Statement

Master the break statement for controlling loop execution in Python. Learn to
exit loops early, implement search algorithms, handle user input, and create
conditional loop termination. Essential for efficient loop control.

**Zero Package Installation Required**
"""

# Example 1: Basic Break in While Loop
print("="*70)
print("Example 1: Using break in While Loop")
print("="*70)

count = 0
while True:  # Infinite loop
    print(f"  Count: {count}")
    count += 1

    if count >= 5:
        print("  Breaking out of loop!")
        break

print("Loop finished")
print()

# Example 2: Break in For Loop
print("="*70)
print("Example 2: Using break in For Loop")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Searching for first number greater than 5 in {numbers}")

for num in numbers:
    print(f"  Checking: {num}")
    if num > 5:
        print(f"  Found it: {num}!")
        break

print()

# Example 3: Search with Break
print("="*70)
print("Example 3: Searching for Element")
print("="*70)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search_term = "cherry"

print(f"Fruits: {fruits}")
print(f"Searching for: '{search_term}'")

found = False
for i, fruit in enumerate(fruits):
    print(f"  Checking position {i}: {fruit}")
    if fruit == search_term:
        print(f"  Found '{search_term}' at index {i}!")
        found = True
        break

if not found:
    print(f"  '{search_term}' not found")
print()

# Example 4: Break with User Input
print("="*70)
print("Example 4: Break on User Command (Simulated)")
print("="*70)

# Simulate user inputs
simulated_inputs = ["hello", "world", "python", "quit", "never reached"]

print("Chat simulation (type 'quit' to exit):")
for user_input in simulated_inputs:
    print(f"  User: {user_input}")

    if user_input.lower() == "quit":
        print("  Exiting chat...")
        break

    print(f"  Echo: {user_input}")

print()

# Example 5: Break in Nested Loops
print("="*70)
print("Example 5: Break in Nested Loops")
print("="*70)

print("Searching for number 7 in 2D grid:")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

found = False
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        print(f"  Checking [{i}][{j}]: {value}")
        if value == 7:
            print(f"  Found 7 at position [{i}][{j}]!")
            found = True
            break
    if found:
        break  # Break outer loop too

print()

# Example 6: Break vs Return
print("="*70)
print("Example 6: Break in Function")
print("="*70)

def find_first_even(numbers):
    """Find first even number in list"""
    print(f"  Searching in: {numbers}")
    for num in numbers:
        print(f"    Checking: {num}")
        if num % 2 == 0:
            print(f"    Found even number: {num}")
            return num  # Return exits function
    print("    No even number found")
    return None

result = find_first_even([1, 3, 5, 8, 9, 10])
print(f"  Result: {result}")
print()

# Example 7: Break with Conditional
print("="*70)
print("Example 7: Multiple Break Conditions")
print("="*70)

max_attempts = 10
threshold = 50

print(f"Finding number > {threshold} (max {max_attempts} attempts):")

for i in range(max_attempts):
    value = i * 6
    print(f"  Attempt {i + 1}: {value}")

    if value > threshold:
        print(f"  Reached threshold!")
        break

    if i == max_attempts - 1:
        print(f"  Max attempts reached!")
print()

# Example 8: Break in While with Counter
print("="*70)
print("Example 8: Break with Counter")
print("="*70)

count = 0
max_count = 100

print("Counting until we hit a number divisible by 17:")

while count < max_count:
    count += 1

    if count % 17 == 0:
        print(f"  Found: {count} is divisible by 17!")
        break

if count < max_count:
    print(f"  Stopped early at count = {count}")
else:
    print(f"  Reached max count: {max_count}")
print()

# Example 9: Break for Validation
print("="*70)
print("Example 9: Input Validation with Break")
print("="*70)

# Simulate user attempting to enter valid PIN
attempts = ["1111", "2222", "5555", "1234", "9999"]
correct_pin = "1234"
max_attempts = 5

print(f"PIN entry system (max {max_attempts} attempts):")

for attempt_num, pin in enumerate(attempts, 1):
    print(f"  Attempt {attempt_num}: Entered {pin}")

    if pin == correct_pin:
        print(f"  Access granted!")
        break

    if attempt_num >= max_attempts:
        print(f"  Maximum attempts reached. Access denied.")
        break

    print(f"  Incorrect PIN. {max_attempts - attempt_num} attempts remaining.")
print()

# Example 10: Practical Application - Menu System
print("="*70)
print("Example 10: Real-World Use Case - Interactive Menu")
print("="*70)

class MenuSystem:
    """Simple menu system with break for exit"""

    def __init__(self):
        self.running = True
        self.items = []

    def display_menu(self):
        """Display menu options"""
        print("\\n" + "="*50)
        print("TODO LIST MENU")
        print("="*50)
        print("1. Add item")
        print("2. View items")
        print("3. Remove item")
        print("4. Clear all")
        print("5. Exit")
        print("="*50)

    def add_item(self, item):
        """Add item to list"""
        self.items.append(item)
        print(f"  Added: '{item}'")

    def view_items(self):
        """View all items"""
        if not self.items:
            print("  No items in list")
        else:
            print("  TODO Items:")
            for i, item in enumerate(self.items, 1):
                print(f"    {i}. {item}")

    def remove_item(self, index):
        """Remove item by index"""
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"  Removed: '{removed}'")
        else:
            print(f"  Invalid index: {index}")

    def clear_all(self):
        """Clear all items"""
        count = len(self.items)
        self.items.clear()
        print(f"  Cleared {count} items")

    def run(self, simulated_choices):
        """Run menu with simulated user choices"""
        print("Starting menu system simulation...")

        for choice_data in simulated_choices:
            if not self.running:
                break

            choice = choice_data["choice"]
            self.display_menu()
            print(f"User selects: {choice}")

            if choice == "1":
                # Add item
                item = choice_data.get("item", "New task")
                self.add_item(item)

            elif choice == "2":
                # View items
                self.view_items()

            elif choice == "3":
                # Remove item
                index = choice_data.get("index", 0)
                self.remove_item(index)

            elif choice == "4":
                # Clear all
                self.clear_all()

            elif choice == "5":
                # Exit
                print("  Exiting menu...")
                break  # Exit the loop

            else:
                print("  Invalid choice!")

        print("\\nMenu system closed")

# Test menu system with simulated inputs
menu = MenuSystem()

simulated_inputs = [
    {"choice": "1", "item": "Buy groceries"},
    {"choice": "1", "item": "Call dentist"},
    {"choice": "2"},  # View items
    {"choice": "1", "item": "Finish project"},
    {"choice": "2"},  # View items
    {"choice": "3", "index": 1},  # Remove middle item
    {"choice": "2"},  # View items
    {"choice": "5"},  # Exit
    {"choice": "1", "item": "This won't be added"}  # After exit
]

menu.run(simulated_inputs)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. break exits the nearest enclosing loop immediately")
print("2. Use break to exit infinite loops (while True)")
print("3. break is useful for searching (stop when found)")
print("4. break only exits one loop (innermost)")
print("5. Combine with if for conditional exit")
print("6. Use flags to break nested loops")
print("7. break vs return: break exits loop, return exits function")
print("8. Common pattern: while True with break condition")
print("9. Good for user input loops (quit command)")
print("10. Improves efficiency by stopping early")
print("="*70)
'''

# Upgrade Lesson 163: Break and Continue Statements
lesson163['fullSolution'] = '''"""
Break and Continue Statements

Master break and continue for advanced loop control in Python. Learn when to
use each, combine them effectively, and implement complex loop logic patterns.
Understand the difference and best practices for loop control flow.

**Zero Package Installation Required**
"""

# Example 1: Understanding break vs continue
print("="*70)
print("Example 1: Break vs Continue Comparison")
print("="*70)

print("With break (exits loop):")
for i in range(10):
    if i == 5:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")

print()
print("With continue (skips to next iteration):")
for i in range(10):
    if i == 5:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}")
print()

# Example 2: Continue to Skip Elements
print("="*70)
print("Example 2: Using continue to Filter")
print("="*70)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Processing numbers: {numbers}")
print("Processing only even numbers:")

for num in numbers:
    if num % 2 != 0:
        continue  # Skip odd numbers
    print(f"  Processing even number: {num}")
print()

# Example 3: Break for Early Exit
print("="*70)
print("Example 3: Break for Error Condition")
print("="*70)

data = [10, 20, 30, -5, 40, 50]

print(f"Processing data: {data}")
print("Stopping at first negative number:")

for value in data:
    if value < 0:
        print(f"  Error: Negative value {value} found, stopping!")
        break
    print(f"  Processing: {value}")
print()

# Example 4: Continue for Validation
print("="*70)
print("Example 4: Continue to Skip Invalid Data")
print("="*70)

inputs = ["10", "20", "invalid", "30", "abc", "40", "50"]

print(f"Converting strings to integers: {inputs}")
print("Skipping invalid entries:")

results = []
for item in inputs:
    try:
        value = int(item)
        results.append(value)
        print(f"  Converted: {item} -> {value}")
    except ValueError:
        print(f"  Skipping invalid: {item}")
        continue  # Skip invalid values

print(f"Results: {results}")
print()

# Example 5: Combining Break and Continue
print("="*70)
print("Example 5: Using Both break and continue")
print("="*70)

numbers = [1, 2, 3, 4, 5, -1, 6, 7, 8, 9, 10]

print(f"Numbers: {numbers}")
print("Processing even numbers until we hit -1:")

for num in numbers:
    if num == -1:
        print(f"  Found sentinel value -1, stopping!")
        break

    if num % 2 != 0:
        continue  # Skip odd numbers

    print(f"  Processing even: {num}")
print()

# Example 6: Continue in Nested Loops
print("="*70)
print("Example 6: Continue in Nested Loops")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

print("Processing matrix, skipping zeros:")
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == 0:
            print(f"  Skipping zero at [{i}][{j}]")
            continue
        print(f"  [{i}][{j}] = {value}")
print()

# Example 7: Break in Nested Loops with Flag
print("="*70)
print("Example 7: Breaking Nested Loops with Flag")
print("="*70)

grid = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

target = 7
found = False

print(f"Searching for {target} in grid:")

for i, row in enumerate(grid):
    if found:
        break  # Break outer loop

    for j, value in enumerate(row):
        print(f"  Checking [{i}][{j}] = {value}")
        if value == target:
            print(f"  Found {target} at [{i}][{j}]!")
            found = True
            break  # Break inner loop
print()

# Example 8: Continue for Processing Steps
print("="*70)
print("Example 8: Multi-Step Processing with continue")
print("="*70)

tasks = [
    {"name": "Task 1", "priority": "high", "done": False},
    {"name": "Task 2", "priority": "low", "done": True},
    {"name": "Task 3", "priority": "high", "done": False},
    {"name": "Task 4", "priority": "medium", "done": True},
    {"name": "Task 5", "priority": "high", "done": False},
]

print("Processing only incomplete high-priority tasks:")

for task in tasks:
    # Skip if already done
    if task["done"]:
        print(f"  Skipping completed: {task['name']}")
        continue

    # Skip if not high priority
    if task["priority"] != "high":
        print(f"  Skipping non-high priority: {task['name']}")
        continue

    # Process high-priority incomplete tasks
    print(f"  PROCESSING: {task['name']} (priority: {task['priority']})")
print()

# Example 9: Break for Resource Limits
print("="*70)
print("Example 9: Break on Resource Limit")
print("="*70)

files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
max_size = 1000
current_size = 0
file_sizes = [200, 300, 400, 500, 600]

print(f"Loading files (max {max_size} bytes):")

loaded_files = []
for filename, size in zip(files, file_sizes):
    if current_size + size > max_size:
        print(f"  Limit reached! Cannot load {filename} ({size} bytes)")
        break

    current_size += size
    loaded_files.append(filename)
    print(f"  Loaded: {filename} ({size} bytes) - Total: {current_size} bytes")

print(f"Loaded {len(loaded_files)} files, Total size: {current_size} bytes")
print()

# Example 10: Practical Application - Data Validator
print("="*70)
print("Example 10: Real-World Use Case - Data Validation Pipeline")
print("="*70)

class DataValidator:
    """Validate and process data with break/continue"""

    def __init__(self):
        self.valid_records = []
        self.skipped_records = []
        self.fatal_errors = 0

    def validate_record(self, record, record_num):
        """Validate a single record"""
        # Check for required fields
        if "id" not in record:
            print(f"  Record {record_num}: SKIP - Missing 'id' field")
            self.skipped_records.append((record_num, "missing id"))
            return False

        if "value" not in record:
            print(f"  Record {record_num}: SKIP - Missing 'value' field")
            self.skipped_records.append((record_num, "missing value"))
            return False

        # Validate data types
        if not isinstance(record["value"], (int, float)):
            print(f"  Record {record_num}: SKIP - Invalid value type")
            self.skipped_records.append((record_num, "invalid value type"))
            return False

        # Validate range
        if record["value"] < 0:
            print(f"  Record {record_num}: SKIP - Negative value")
            self.skipped_records.append((record_num, "negative value"))
            return False

        # Check for critical errors
        if record.get("error_flag") == "FATAL":
            print(f"  Record {record_num}: FATAL ERROR - Stopping processing")
            self.fatal_errors += 1
            return "FATAL"

        # Valid record
        print(f"  Record {record_num}: VALID - id={record['id']}, value={record['value']}")
        return True

    def process_batch(self, records):
        """Process batch of records"""
        print("PROCESSING DATA BATCH")
        print("=" * 70)

        for i, record in enumerate(records, 1):
            result = self.validate_record(record, i)

            if result == "FATAL":
                print("  Fatal error encountered, stopping batch processing!")
                break  # Exit on fatal error

            if not result:
                continue  # Skip invalid records

            # Process valid record
            self.valid_records.append(record)

        print("\\n" + "=" * 70)
        print("PROCESSING SUMMARY")
        print("=" * 70)
        print(f"Total records processed: {i}")
        print(f"Valid records: {len(self.valid_records)}")
        print(f"Skipped records: {len(self.skipped_records)}")
        print(f"Fatal errors: {self.fatal_errors}")

        if self.skipped_records:
            print("\\nSkipped record details:")
            for rec_num, reason in self.skipped_records:
                print(f"  Record {rec_num}: {reason}")

# Test data validator
validator = DataValidator()

test_data = [
    {"id": 1, "value": 100},                          # Valid
    {"id": 2},                                         # Missing value
    {"id": 3, "value": "abc"},                        # Invalid type
    {"id": 4, "value": 200},                          # Valid
    {"value": 150},                                    # Missing id
    {"id": 5, "value": -50},                          # Negative value
    {"id": 6, "value": 300},                          # Valid
    {"id": 7, "value": 400, "error_flag": "FATAL"},   # Fatal error
    {"id": 8, "value": 500},                          # Won't be processed
]

validator.process_batch(test_data)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. break exits loop completely")
print("2. continue skips to next iteration")
print("3. break useful for: searches, early exit, errors")
print("4. continue useful for: filtering, skipping invalid data")
print("5. Can combine break and continue in same loop")
print("6. continue is like an if-else without the else block")
print("7. Use flags to break nested loops")
print("8. break saves processing time by stopping early")
print("9. continue improves readability vs nested ifs")
print("10. Both affect only the innermost loop")
print("="*70)
'''

# Save progress
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\nUpgraded lessons 161-163:")
print(f"  161: Basic Math Operations - {len(lesson161['fullSolution'])} chars")
print(f"  162: Break Statement - {len(lesson162['fullSolution'])} chars")
print(f"  163: Break and Continue Statements - {len(lesson163['fullSolution'])} chars")
print("\nContinuing with lessons 164-170...")
