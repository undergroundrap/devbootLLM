#!/usr/bin/env python3
"""
Upgrade 5 CRITICAL Python lessons with comprehensive content
"""

import json

# Critical lesson upgrades
UPGRADES = {
    331: {
        "title": "decimal for Precision",
        "solution": '''"""
Decimal for Precision - Comprehensive Guide

The decimal module provides arbitrary-precision decimal arithmetic,
essential for financial calculations, scientific computing, and any
scenario where floating-point errors are unacceptable.

**Zero Package Installation Required**
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP
from typing import List

# Example 1: Why Use Decimal Instead of Float?
print("="*70)
print("Example 1: Float vs Decimal - The Precision Problem")
print("="*70)

# Float precision issues
float_result = 0.1 + 0.2
print(f"\\nFloat calculation:")
print(f"  0.1 + 0.2 = {float_result}")
print(f"  Expected: 0.3, Got: {float_result} ❌")
print(f"  Are they equal? {float_result == 0.3}")

# Decimal precision
decimal_result = Decimal('0.1') + Decimal('0.2')
print(f"\\nDecimal calculation:")
print(f"  Decimal('0.1') + Decimal('0.2') = {decimal_result}")
print(f"  Are they equal to 0.3? {decimal_result == Decimal('0.3')} ✓")

# Example 2: Financial Calculations
print("\\n" + "="*70)
print("Example 2: Financial Calculations (Money)")
print("="*70)

def calculate_tax(price: Decimal, tax_rate: Decimal) -> Decimal:
    """Calculate tax with precision."""
    return price * tax_rate

def calculate_total(price: Decimal, tax_rate: Decimal) -> Decimal:
    """Calculate total with tax."""
    tax = calculate_tax(price, tax_rate)
    return price + tax

# Product prices
products = [
    ("Laptop", Decimal("999.99")),
    ("Mouse", Decimal("24.50")),
    ("Keyboard", Decimal("79.99"))
]

tax_rate = Decimal("0.0825")  # 8.25% tax

print(f"\\nTax Rate: {tax_rate * 100}%")
print("\\nProduct Pricing:")

total_sum = Decimal("0")
for name, price in products:
    tax = calculate_tax(price, tax_rate)
    total = calculate_total(price, tax_rate)
    total_sum += total

    print(f"\\n{name}:")
    print(f"  Price:    ${price:>8}")
    print(f"  Tax:      ${tax:>8.2f}")
    print(f"  Total:    ${total:>8.2f}")

print(f"\\nGrand Total: ${total_sum:.2f}")

# Example 3: Rounding Modes
print("\\n" + "="*70)
print("Example 3: Decimal Rounding Modes")
print("="*70)

value = Decimal("10.555")
print(f"\\nOriginal value: {value}")

# Different rounding modes
print(f"\\nRounding to 2 decimal places:")
print(f"  ROUND_HALF_UP:   {value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
print(f"  ROUND_DOWN:      {value.quantize(Decimal('0.01'), rounding=ROUND_DOWN)}")
print(f"  ROUND_UP:        {value.quantize(Decimal('0.01'), rounding=ROUND_UP)}")

# Example 4: Setting Precision Context
print("\\n" + "="*70)
print("Example 4: Precision Context")
print("="*70)

# Default context
print(f"\\nDefault precision: {getcontext().prec}")

# Calculate pi with different precisions
def calculate_pi_approximation(precision: int) -> Decimal:
    """Simple pi approximation using Leibniz formula (limited iterations)."""
    getcontext().prec = precision

    result = Decimal(0)
    for i in range(1000):
        sign = Decimal(-1) ** i
        term = sign / (2 * i + 1)
        result += term

    return result * 4

print("\\nPi approximations with different precisions:")
for prec in [10, 20, 30]:
    pi_approx = calculate_pi_approximation(prec)
    print(f"  Precision {prec:2d}: {pi_approx}")

# Reset to default
getcontext().prec = 28

# Example 5: Currency Conversion
print("\\n" + "="*70)
print("Example 5: Currency Conversion")
print("="*70)

class CurrencyConverter:
    """Precise currency converter."""

    def __init__(self):
        self.rates = {
            'USD': Decimal('1.00'),
            'EUR': Decimal('0.85'),
            'GBP': Decimal('0.73'),
            'JPY': Decimal('110.50')
        }

    def convert(self, amount: Decimal, from_currency: str, to_currency: str) -> Decimal:
        """Convert between currencies."""
        # Convert to USD first, then to target
        usd_amount = amount / self.rates[from_currency]
        return usd_amount * self.rates[to_currency]

converter = CurrencyConverter()

amount = Decimal("1000.00")
print(f"\\nConverting ${amount} USD:")

for currency in ['EUR', 'GBP', 'JPY']:
    converted = converter.convert(amount, 'USD', currency)
    print(f"  {currency}: {converted:.2f}")

# Example 6: Percentage Calculations
print("\\n" + "="*70)
print("Example 6: Percentage Calculations")
print("="*70)

def calculate_percentage(value: Decimal, percentage: Decimal) -> Decimal:
    """Calculate percentage of a value."""
    return value * (percentage / Decimal('100'))

def apply_discount(price: Decimal, discount_percent: Decimal) -> Decimal:
    """Apply discount to price."""
    discount = calculate_percentage(price, discount_percent)
    return price - discount

original_price = Decimal("199.99")
discounts = [Decimal("10"), Decimal("15"), Decimal("20"), Decimal("25")]

print(f"\\nOriginal Price: ${original_price}")
print("\\nDiscount Analysis:")

for discount in discounts:
    final_price = apply_discount(original_price, discount)
    saved = original_price - final_price
    print(f"  {discount}% off: ${final_price:.2f} (Save ${saved:.2f})")

# Example 7: Investment Returns
print("\\n" + "="*70)
print("Example 7: Compound Interest Calculation")
print("="*70)

def compound_interest(principal: Decimal, rate: Decimal, time: int,
                     compounds_per_year: int = 12) -> Decimal:
    """Calculate compound interest."""
    rate_decimal = rate / Decimal('100')
    n = Decimal(compounds_per_year)
    t = Decimal(time)

    # A = P(1 + r/n)^(nt)
    amount = principal * (Decimal('1') + rate_decimal / n) ** (n * t)
    return amount

principal = Decimal("10000.00")
annual_rate = Decimal("5.5")
years = 10

final_amount = compound_interest(principal, annual_rate, years)
interest_earned = final_amount - principal

print(f"\\nInvestment Analysis:")
print(f"  Principal:        ${principal:>12}")
print(f"  Annual Rate:      {annual_rate}%")
print(f"  Time Period:      {years} years")
print(f"  Final Amount:     ${final_amount:>12.2f}")
print(f"  Interest Earned:  ${interest_earned:>12.2f}")

print("\\n" + "="*70)
print("Decimal precision examples complete!")
print("="*70)
print("\\nKey Takeaways:")
print("  • Use Decimal for financial calculations")
print("  • Always use string initialization: Decimal('0.1')")
print("  • Never use float initialization: Decimal(0.1) ❌")
print("  • Set precision context when needed")
print("  • Use appropriate rounding modes")
'''
    },

    316: {
        "title": "decimal",
        "solution": '''"""
Decimal Module - Comprehensive Guide

Python's decimal module provides support for decimal floating point
arithmetic with user-controllable precision, essential for financial
and scientific applications.

**Zero Package Installation Required**
"""

from decimal import Decimal, getcontext, InvalidOperation, DivisionByZero
from decimal import ROUND_HALF_UP, ROUND_DOWN, ROUND_CEILING, ROUND_FLOOR
from typing import List, Tuple

# Example 1: Basic Decimal Operations
print("="*70)
print("Example 1: Basic Decimal Arithmetic")
print("="*70)

# Creating Decimals - ALWAYS use strings
a = Decimal('10.5')
b = Decimal('5.25')
c = Decimal('2.0')

print(f"\\na = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Basic operations
print(f"\\nBasic Operations:")
print(f"  a + b = {a + b}")
print(f"  a - b = {a - b}")
print(f"  a * b = {a * b}")
print(f"  a / b = {a / b}")
print(f"  a // b = {a // b}  (floor division)")
print(f"  a % b = {a % b}   (modulo)")
print(f"  a ** c = {a ** c}  (power)")

# Example 2: Why String Initialization Matters
print("\\n" + "="*70)
print("Example 2: String vs Float Initialization")
print("="*70)

# Wrong way - using float
decimal_from_float = Decimal(0.1)
print(f"\\nDecimal(0.1) = {decimal_from_float}")
print(f"  ❌ Float representation errors carried over!")

# Right way - using string
decimal_from_string = Decimal('0.1')
print(f"\\nDecimal('0.1') = {decimal_from_string}")
print(f"  ✓ Exact representation!")

# Example 3: Comparison and Equality
print("\\n" + "="*70)
print("Example 3: Decimal Comparisons")
print("="*70)

x = Decimal('10.50')
y = Decimal('10.5')
z = Decimal('10.500')

print(f"\\nx = {x}")
print(f"y = {y}")
print(f"z = {z}")

print(f"\\nComparisons:")
print(f"  x == y: {x == y}")
print(f"  x == z: {x == z}")
print(f"  x > Decimal('10'): {x > Decimal('10')}")
print(f"  x < Decimal('11'): {x < Decimal('11')}")

# Example 4: Quantize - Rounding to Decimal Places
print("\\n" + "="*70)
print("Example 4: Quantize and Rounding")
print("="*70)

value = Decimal('123.456789')
print(f"\\nOriginal: {value}")

# Round to different decimal places
print(f"\\nRounding:")
print(f"  2 decimals: {value.quantize(Decimal('0.01'))}")
print(f"  1 decimal:  {value.quantize(Decimal('0.1'))}")
print(f"  0 decimals: {value.quantize(Decimal('1'))}")

# Different rounding modes
value2 = Decimal('2.5')
print(f"\\nRounding {value2} with different modes:")
print(f"  ROUND_HALF_UP:   {value2.quantize(Decimal('1'), rounding=ROUND_HALF_UP)}")
print(f"  ROUND_DOWN:      {value2.quantize(Decimal('1'), rounding=ROUND_DOWN)}")
print(f"  ROUND_CEILING:   {value2.quantize(Decimal('1'), rounding=ROUND_CEILING)}")
print(f"  ROUND_FLOOR:     {value2.quantize(Decimal('1'), rounding=ROUND_FLOOR)}")

# Example 5: Shopping Cart with Precise Totals
print("\\n" + "="*70)
print("Example 5: Shopping Cart Calculator")
print("="*70)

class ShoppingCart:
    """Shopping cart with precise decimal calculations."""

    def __init__(self):
        self.items: List[Tuple[str, Decimal, int]] = []

    def add_item(self, name: str, price: Decimal, quantity: int):
        """Add item to cart."""
        self.items.append((name, price, quantity))

    def calculate_subtotal(self) -> Decimal:
        """Calculate subtotal."""
        total = Decimal('0')
        for name, price, qty in self.items:
            total += price * Decimal(str(qty))
        return total

    def calculate_tax(self, tax_rate: Decimal) -> Decimal:
        """Calculate tax."""
        return self.calculate_subtotal() * tax_rate

    def calculate_total(self, tax_rate: Decimal) -> Decimal:
        """Calculate total with tax."""
        return self.calculate_subtotal() + self.calculate_tax(tax_rate)

    def display_receipt(self, tax_rate: Decimal):
        """Display formatted receipt."""
        print("\\n" + "="*50)
        print("RECEIPT")
        print("="*50)

        for name, price, qty in self.items:
            line_total = price * Decimal(str(qty))
            print(f"{name:30s} x{qty}  ${line_total:>8.2f}")

        print("-"*50)
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        total = self.calculate_total(tax_rate)

        print(f"{'Subtotal:':<30s}     ${subtotal:>8.2f}")
        print(f"{'Tax (' + str(tax_rate * 100) + '%):':<30s}     ${tax:>8.2f}")
        print("="*50)
        print(f"{'TOTAL:':<30s}     ${total:>8.2f}")
        print("="*50)

# Create cart and add items
cart = ShoppingCart()
cart.add_item("Laptop", Decimal("999.99"), 1)
cart.add_item("USB Cable", Decimal("12.50"), 2)
cart.add_item("Mouse", Decimal("24.99"), 1)
cart.add_item("Keyboard", Decimal("79.99"), 1)

tax_rate = Decimal("0.0825")  # 8.25%
cart.display_receipt(tax_rate)

# Example 6: Precision Control
print("\\n" + "="*70)
print("Example 6: Controlling Precision")
print("="*70)

# Get current context
ctx = getcontext()
print(f"\\nDefault precision: {ctx.prec} digits")

# Perform division
a = Decimal('1')
b = Decimal('3')
result = a / b

print(f"\\n1 / 3 = {result}")

# Change precision
getcontext().prec = 10
result_10 = Decimal('1') / Decimal('3')
print(f"\\nWith precision=10: {result_10}")

getcontext().prec = 50
result_50 = Decimal('1') / Decimal('3')
print(f"With precision=50: {result_50}")

# Reset to default
getcontext().prec = 28

# Example 7: Error Handling
print("\\n" + "="*70)
print("Example 7: Error Handling")
print("="*70)

# Invalid operations
print("\\nHandling invalid operations:")

try:
    invalid = Decimal('abc')
except InvalidOperation as e:
    print(f"  InvalidOperation: Cannot create Decimal from 'abc'")

try:
    result = Decimal('10') / Decimal('0')
except DivisionByZero as e:
    print(f"  DivisionByZero: Cannot divide by zero")

# Example 8: Salary and Payroll Calculations
print("\\n" + "="*70)
print("Example 8: Payroll Calculator")
print("="*70)

def calculate_payroll(hourly_rate: Decimal, hours: Decimal,
                     overtime_hours: Decimal = Decimal('0')) -> dict:
    """Calculate payroll with overtime."""
    regular_pay = hourly_rate * hours
    overtime_rate = hourly_rate * Decimal('1.5')
    overtime_pay = overtime_rate * overtime_hours
    gross_pay = regular_pay + overtime_pay

    # Deductions
    tax_rate = Decimal('0.20')  # 20%
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax

    return {
        'regular_pay': regular_pay,
        'overtime_pay': overtime_pay,
        'gross_pay': gross_pay,
        'tax': tax,
        'net_pay': net_pay
    }

# Calculate employee payroll
hourly_rate = Decimal('25.50')
regular_hours = Decimal('40')
overtime_hours = Decimal('5')

payroll = calculate_payroll(hourly_rate, regular_hours, overtime_hours)

print(f"\\nEmployee Payroll:")
print(f"  Hourly Rate:    ${hourly_rate}")
print(f"  Regular Hours:  {regular_hours}")
print(f"  Overtime Hours: {overtime_hours}")
print(f"\\nPayroll Breakdown:")
print(f"  Regular Pay:    ${payroll['regular_pay']:>10.2f}")
print(f"  Overtime Pay:   ${payroll['overtime_pay']:>10.2f}")
print(f"  Gross Pay:      ${payroll['gross_pay']:>10.2f}")
print(f"  Tax (20%):      ${payroll['tax']:>10.2f}")
print(f"  Net Pay:        ${payroll['net_pay']:>10.2f}")

print("\\n" + "="*70)
print("Decimal module examples complete!")
print("="*70)
print("\\nBest Practices:")
print("  • Always initialize with strings: Decimal('10.5')")
print("  • Use quantize() for rounding")
print("  • Handle InvalidOperation and DivisionByZero")
print("  • Set precision context when needed")
print("  • Perfect for financial calculations!")
'''
    },

    357: {
        "title": "bisect_left",
        "solution": '''"""
bisect_left - Binary Search for Insertion Index

The bisect module provides support for maintaining sorted lists using
binary search algorithms. bisect_left finds the leftmost insertion point.

**Zero Package Installation Required**
"""

import bisect
from typing import List, Any

# Example 1: Basic bisect_left Usage
print("="*70)
print("Example 1: Finding Insertion Index")
print("="*70)

# Sorted list
data = [10, 20, 30, 40, 50]
print(f"\\nSorted list: {data}")

# Find insertion points
values_to_insert = [15, 25, 35, 45]

print("\\nInsertion indices:")
for value in values_to_insert:
    idx = bisect.bisect_left(data, value)
    print(f"  bisect_left({value}): index {idx}")

    # Show what it would look like
    preview = data[:idx] + [value] + data[idx:]
    print(f"    After insert: {preview}")

# Example 2: bisect_left vs bisect_right
print("\\n" + "="*70)
print("Example 2: bisect_left vs bisect_right")
print("="*70)

scores = [65, 75, 75, 75, 85, 95]
print(f"\\nScores: {scores}")

value = 75
left_idx = bisect.bisect_left(scores, value)
right_idx = bisect.bisect_right(scores, value)

print(f"\\nSearching for value: {value}")
print(f"  bisect_left:  index {left_idx} (insert before existing)")
print(f"  bisect_right: index {right_idx} (insert after existing)")

print(f"\\nVisual representation:")
print(f"  {scores}")
print(f"  {'  '*left_idx}↑ bisect_left({value})")
print(f"  {'  '*right_idx}↑ bisect_right({value})")

# Example 3: Maintaining Sorted Order
print("\\n" + "="*70)
print("Example 3: Maintaining a Sorted List")
print("="*70)

class SortedList:
    """Maintain a sorted list using bisect."""

    def __init__(self):
        self.data: List[int] = []

    def insert(self, value: int):
        """Insert value in sorted position."""
        idx = bisect.bisect_left(self.data, value)
        self.data.insert(idx, value)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

# Build sorted list
sorted_list = SortedList()
values = [50, 20, 80, 10, 90, 30, 70, 40, 60]

print(f"\\nInserting values: {values}")
print("\\nStep-by-step insertion:")

for value in values:
    sorted_list.insert(value)
    print(f"  Insert {value}: {sorted_list}")

# Example 4: Grade Lookup System
print("\\n" + "="*70)
print("Example 4: Grade Lookup System")
print("="*70)

class GradeCalculator:
    """Calculate letter grades using bisect_left."""

    def __init__(self):
        # Breakpoints for grades (sorted ascending)
        self.breakpoints = [60, 70, 80, 90]
        self.grades = ['F', 'D', 'C', 'B', 'A']

    def get_grade(self, score: int) -> str:
        """Get letter grade for numeric score."""
        idx = bisect.bisect_left(self.breakpoints, score)
        return self.grades[idx]

grader = GradeCalculator()

# Test scores
test_scores = [95, 87, 76, 82, 65, 58, 92, 71]

print(f"\\nGrade Scale:")
print(f"  A: 90+")
print(f"  B: 80-89")
print(f"  C: 70-79")
print(f"  D: 60-69")
print(f"  F: <60")

print(f"\\nStudent Scores:")
for score in test_scores:
    grade = grader.get_grade(score)
    print(f"  Score {score:3d} = Grade {grade}")

# Example 5: Finding Ranges
print("\\n" + "="*70)
print("Example 5: Finding Value Ranges")
print("="*70)

def count_in_range(data: List[int], low: int, high: int) -> int:
    """Count how many values are in [low, high) range."""
    left = bisect.bisect_left(data, low)
    right = bisect.bisect_left(data, high)
    return right - left

numbers = [10, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90]
print(f"\\nData: {numbers}")

ranges = [(20, 50), (30, 70), (0, 40), (50, 100)]

print(f"\\nCounting values in ranges:")
for low, high in ranges:
    count = count_in_range(numbers, low, high)
    print(f"  [{low}, {high}): {count} values")

# Example 6: Time-based Event Scheduling
print("\\n" + "="*70)
print("Example 6: Event Scheduler")
print("="*70)

class EventScheduler:
    """Schedule events in chronological order."""

    def __init__(self):
        self.times: List[int] = []
        self.events: List[str] = []

    def add_event(self, time: int, event: str):
        """Add event at specific time."""
        idx = bisect.bisect_left(self.times, time)
        self.times.insert(idx, time)
        self.events.insert(idx, event)

    def show_schedule(self):
        """Display all events in order."""
        print("\\n  Time | Event")
        print("  " + "-"*40)
        for time, event in zip(self.times, self.events):
            print(f"  {time:4d} | {event}")

scheduler = EventScheduler()

# Add events (not in order)
scheduler.add_event(1000, "Team Meeting")
scheduler.add_event(900, "Morning Standup")
scheduler.add_event(1400, "Code Review")
scheduler.add_event(1200, "Lunch Break")
scheduler.add_event(1600, "Deploy to Production")

print("\\nDaily Schedule:")
scheduler.show_schedule()

# Example 7: Binary Search for Existing Values
print("\\n" + "="*70)
print("Example 7: Checking if Value Exists")
print("="*70)

def contains(data: List[int], value: int) -> bool:
    """Check if value exists in sorted list."""
    idx = bisect.bisect_left(data, value)
    return idx < len(data) and data[idx] == value

inventory = [100, 200, 300, 400, 500, 600, 700, 800, 900]
print(f"\\nInventory IDs: {inventory}")

search_ids = [250, 300, 450, 500, 850, 900]

print(f"\\nSearching for IDs:")
for search_id in search_ids:
    found = contains(inventory, search_id)
    status = "✓ Found" if found else "✗ Not found"
    print(f"  ID {search_id}: {status}")

# Example 8: Percentile Calculation
print("\\n" + "="*70)
print("Example 8: Percentile Rankings")
print("="*70)

def calculate_percentile(scores: List[int], score: int) -> float:
    """Calculate percentile rank of a score."""
    idx = bisect.bisect_left(scores, score)
    percentile = (idx / len(scores)) * 100
    return percentile

test_scores_sorted = sorted([72, 85, 90, 78, 95, 88, 76, 82, 91, 87,
                             79, 84, 92, 75, 89, 86, 93, 77, 83, 94])

print(f"\\nTest scores (sorted): {test_scores_sorted}")
print(f"Total students: {len(test_scores_sorted)}")

my_scores = [75, 85, 90, 95]

print(f"\\nPercentile rankings:")
for score in my_scores:
    percentile = calculate_percentile(test_scores_sorted, score)
    print(f"  Score {score}: {percentile:.1f}th percentile")

# Example 9: Custom Comparison with Key Functions
print("\\n" + "="*70)
print("Example 9: Advanced - Custom Key Functions")
print("="*70)

class Student:
    """Student with name and GPA."""

    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def __repr__(self):
        return f"{self.name}({self.gpa})"

# Sort students by GPA
students = [
    Student("Alice", 3.5),
    Student("Bob", 3.8),
    Student("Charlie", 3.2),
    Student("Diana", 3.9)
]

# Extract GPAs for binary search
gpas = [s.gpa for s in students]
gpas.sort()

new_gpa = 3.6
idx = bisect.bisect_left(gpas, new_gpa)

print(f"\\nStudent GPAs (sorted): {gpas}")
print(f"\\nNew student with GPA {new_gpa}")
print(f"  Would be inserted at index {idx}")
print(f"  Better than {idx} students")
print(f"  Percentile: {(idx/len(gpas)*100):.1f}%")

print("\\n" + "="*70)
print("bisect_left examples complete!")
print("="*70)
print("\\nKey Points:")
print("  • bisect_left finds the leftmost insertion point")
print("  • Maintains sorted order with O(log n) search")
print("  • Use for: grade lookups, scheduling, rankings")
print("  • Requires data to be sorted!")
'''
    },

    318: {
        "title": "bisect_left",  # Duplicate of 357, create variation
        "solution": '''"""
bisect_left - Insertion Point for Sorted Sequences

Binary search to find where to insert an item in a sorted list
to maintain sorted order. Returns the leftmost position.

**Zero Package Installation Required**
"""

import bisect
from typing import List, Tuple

# Example 1: Understanding bisect_left
print("="*70)
print("Example 1: bisect_left Fundamentals")
print("="*70)

scores = [65, 75, 85, 95]
print(f"\\nSorted scores: {scores}")

# Find where to insert 80
insert_value = 80
position = bisect.bisect_left(scores, insert_value)

print(f"\\nInserting {insert_value}:")
print(f"  Position from bisect_left: {position}")
print(f"  Before: {scores}")

# Actually insert it
scores_copy = scores.copy()
scores_copy.insert(position, insert_value)
print(f"  After:  {scores_copy}")

# Example 2: insort_left - Insert and Maintain Order
print("\\n" + "="*70)
print("Example 2: insort_left - Automatic Insertion")
print("="*70)

numbers = [10, 30, 50, 70, 90]
print(f"\\nStarting list: {numbers}")

values_to_add = [20, 40, 60, 80]

print(f"\\nAdding values: {values_to_add}")
for value in values_to_add:
    bisect.insort_left(numbers, value)
    print(f"  After adding {value}: {numbers}")

# Example 3: Duplicate Handling
print("\\n" + "="*70)
print("Example 3: Handling Duplicates")
print("="*70)

data = [10, 20, 30, 30, 30, 40, 50]
print(f"\\nData with duplicates: {data}")

duplicate_value = 30
left_pos = bisect.bisect_left(data, duplicate_value)
right_pos = bisect.bisect_right(data, duplicate_value)

print(f"\\nSearching for {duplicate_value}:")
print(f"  bisect_left position:  {left_pos} (before duplicates)")
print(f"  bisect_right position: {right_pos} (after duplicates)")
print(f"  Count of {duplicate_value}: {right_pos - left_pos}")

# Example 4: Student Ranking System
print("\\n" + "="*70)
print("Example 4: Student Ranking System")
print("="*70)

class StudentRankings:
    """Track student rankings using bisect."""

    def __init__(self):
        self.scores: List[int] = []
        self.names: List[str] = []

    def add_student(self, name: str, score: int):
        """Add student maintaining sorted order by score."""
        # Use bisect_left to find position
        idx = bisect.bisect_left(self.scores, score)
        self.scores.insert(idx, score)
        self.names.insert(idx, name)

    def get_rank(self, name: str) -> int:
        """Get student's rank (1-based)."""
        try:
            idx = self.names.index(name)
            # Rank is from the end (highest score = rank 1)
            return len(self.scores) - idx
        except ValueError:
            return -1

    def show_rankings(self):
        """Display all rankings."""
        print("\\n  Rank | Score | Name")
        print("  " + "-"*35)
        for i in range(len(self.scores) - 1, -1, -1):
            rank = len(self.scores) - i
            print(f"  {rank:4d} | {self.scores[i]:5d} | {self.names[i]}")

rankings = StudentRankings()

# Add students
students = [
    ("Alice", 850),
    ("Bob", 920),
    ("Charlie", 780),
    ("Diana", 950),
    ("Eve", 890),
    ("Frank", 810)
]

print("\\nAdding students...")
for name, score in students:
    rankings.add_student(name, score)
    print(f"  Added {name} (score: {score})")

rankings.show_rankings()

# Example 5: Price Comparison Tool
print("\\n" + "="*70)
print("Example 5: Price Comparison Tool")
print("="*70)

class PriceTracker:
    """Track prices and find position in market."""

    def __init__(self, product: str):
        self.product = product
        self.prices: List[float] = []
        self.stores: List[str] = []

    def add_price(self, store: str, price: float):
        """Add price maintaining sorted order."""
        idx = bisect.bisect_left(self.prices, price)
        self.prices.insert(idx, price)
        self.stores.insert(idx, store)

    def get_price_position(self, price: float) -> dict:
        """Analyze where a price falls in the market."""
        idx = bisect.bisect_left(self.prices, price)
        total = len(self.prices)

        cheaper = idx
        more_expensive = total - idx
        percentile = (idx / total * 100) if total > 0 else 0

        return {
            'position': idx + 1,
            'total': total,
            'cheaper': cheaper,
            'more_expensive': more_expensive,
            'percentile': percentile
        }

    def show_prices(self):
        """Display all prices."""
        print(f"\\n  {'Store':<20s} | Price")
        print("  " + "-"*35)
        for store, price in zip(self.stores, self.prices):
            print(f"  {store:<20s} | ${price:6.2f}")

tracker = PriceTracker("Laptop")

# Add prices from different stores
prices = [
    ("Store A", 899.99),
    ("Store B", 949.99),
    ("Store C", 849.99),
    ("Store D", 999.99),
    ("Store E", 879.99),
    ("Store F", 929.99)
]

print(f"\\nTracking prices for: {tracker.product}")
for store, price in prices:
    tracker.add_price(store, price)

tracker.show_prices()

# Analyze a potential price
my_price = 920.00
analysis = tracker.get_price_position(my_price)

print(f"\\nAnalyzing price: ${my_price:.2f}")
print(f"  Position: {analysis['position']} out of {analysis['total']}")
print(f"  Cheaper than: {analysis['more_expensive']} stores")
print(f"  More expensive than: {analysis['cheaper']} stores")
print(f"  Percentile: {analysis['percentile']:.1f}%")

# Example 6: Timeline Event Insertion
print("\\n" + "="*70)
print("Example 6: Historical Timeline")
print("="*70)

class Timeline:
    """Maintain chronological timeline of events."""

    def __init__(self):
        self.years: List[int] = []
        self.events: List[str] = []

    def add_event(self, year: int, event: str):
        """Add event in chronological order."""
        idx = bisect.bisect_left(self.years, year)
        self.years.insert(idx, year)
        self.events.insert(idx, event)

    def show_timeline(self):
        """Display chronological timeline."""
        print("\\n  Year | Event")
        print("  " + "-"*50)
        for year, event in zip(self.years, self.events):
            print(f"  {year} | {event}")

    def events_between(self, start_year: int, end_year: int) -> List[Tuple[int, str]]:
        """Get events between two years."""
        start_idx = bisect.bisect_left(self.years, start_year)
        end_idx = bisect.bisect_left(self.years, end_year)
        return list(zip(self.years[start_idx:end_idx],
                       self.events[start_idx:end_idx]))

timeline = Timeline()

# Add historical events (not in order)
events = [
    (1969, "Moon Landing"),
    (1945, "End of WWII"),
    (1989, "Fall of Berlin Wall"),
    (1991, "World Wide Web launched"),
    (2001, "9/11 Attacks"),
    (1955, "Disneyland Opens"),
    (2008, "iPhone 3G Released")
]

print("\\nAdding historical events...")
for year, event in events:
    timeline.add_event(year, event)

timeline.show_timeline()

# Find events in a range
start, end = 1960, 2000
print(f"\\nEvents between {start} and {end}:")
range_events = timeline.events_between(start, end)
for year, event in range_events:
    print(f"  {year}: {event}")

# Example 7: Priority Queue Implementation
print("\\n" + "="*70)
print("Example 7: Simple Priority Queue")
print("="*70)

class PriorityQueue:
    """Simple priority queue using bisect."""

    def __init__(self):
        self.priorities: List[int] = []
        self.tasks: List[str] = []

    def add_task(self, task: str, priority: int):
        """Add task with priority (lower number = higher priority)."""
        idx = bisect.bisect_left(self.priorities, priority)
        self.priorities.insert(idx, priority)
        self.tasks.insert(idx, task)

    def get_next_task(self) -> str:
        """Get highest priority task."""
        if self.tasks:
            self.priorities.pop(0)
            return self.tasks.pop(0)
        return None

    def show_queue(self):
        """Display all tasks."""
        print("\\n  Priority | Task")
        print("  " + "-"*40)
        for priority, task in zip(self.priorities, self.tasks):
            print(f"  {priority:8d} | {task}")

pq = PriorityQueue()

# Add tasks
print("\\nAdding tasks to priority queue:")
tasks = [
    ("Fix critical bug", 1),
    ("Update documentation", 5),
    ("Code review", 3),
    ("Deploy to staging", 2),
    ("Team meeting", 4)
]

for task, priority in tasks:
    pq.add_task(task, priority)
    print(f"  Added: {task} (priority {priority})")

pq.show_queue()

print("\\nProcessing tasks by priority:")
while True:
    task = pq.get_next_task()
    if task is None:
        break
    print(f"  → {task}")

print("\\n" + "="*70)
print("bisect_left examples complete!")
print("="*70)
print("\\nKey Takeaways:")
print("  • Use bisect_left to find insertion point")
print("  • Use insort_left to insert and maintain order")
print("  • O(log n) search time - very efficient!")
print("  • Perfect for rankings, timelines, priority queues")
'''
    },

    355: {
        "title": "decimal.Decimal",
        "solution": '''"""
decimal.Decimal - Arbitrary Precision Decimal Numbers

The Decimal class provides exact decimal representation, essential
for financial calculations and any application requiring precision.

**Zero Package Installation Required**
"""

from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP
from typing import List, Dict

# Example 1: Creating Decimal Numbers
print("="*70)
print("Example 1: Creating Decimal Objects")
print("="*70)

# Different ways to create Decimals
print("\\nCreating Decimals:")

# From string (RECOMMENDED)
d1 = Decimal('123.45')
print(f"  From string: Decimal('123.45') = {d1}")

# From integer
d2 = Decimal(100)
print(f"  From int: Decimal(100) = {d2}")

# From float (NOT RECOMMENDED - see why)
d3 = Decimal(0.1)
print(f"  From float: Decimal(0.1) = {d3}")
print(f"    ⚠️ Note the precision errors!")

# Correct way for 0.1
d4 = Decimal('0.1')
print(f"  From string: Decimal('0.1') = {d4}")
print(f"    ✓ Exact representation!")

# Example 2: Sales Tax Calculator
print("\\n" + "="*70)
print("Example 2: Sales Tax Calculator")
print("="*70)

def calculate_sales_tax(price: Decimal, tax_rate: Decimal) -> Dict[str, Decimal]:
    """Calculate price with tax."""
    tax = price * tax_rate
    total = price + tax

    # Round to 2 decimal places
    tax = tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    return {
        'price': price,
        'tax': tax,
        'total': total
    }

# Calculate tax for products
tax_rate = Decimal('0.0825')  # 8.25%
products = [
    ("Laptop", Decimal("999.99")),
    ("Mouse", Decimal("29.95")),
    ("Keyboard", Decimal("89.50")),
    ("Monitor", Decimal("299.99"))
]

print(f"\\nTax Rate: {tax_rate * 100}%")
print("\\nProduct Pricing:")

grand_total = Decimal('0')
for name, price in products:
    result = calculate_sales_tax(price, tax_rate)
    grand_total += result['total']

    print(f"\\n{name}:")
    print(f"  Price:  ${result['price']:>8.2f}")
    print(f"  Tax:    ${result['tax']:>8.2f}")
    print(f"  Total:  ${result['total']:>8.2f}")

print(f"\\nGrand Total: ${grand_total:.2f}")

# Example 3: Interest Calculator
print("\\n" + "="*70)
print("Example 3: Interest Calculations")
print("="*70)

def calculate_simple_interest(principal: Decimal, rate: Decimal,
                             time: Decimal) -> Decimal:
    """Calculate simple interest: I = P * R * T"""
    interest = principal * (rate / Decimal('100')) * time
    return interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calculate_compound_interest(principal: Decimal, rate: Decimal,
                               time: int, compounds_per_year: int = 1) -> Decimal:
    """Calculate compound interest: A = P(1 + r/n)^(nt)"""
    rate_decimal = rate / Decimal('100')
    n = Decimal(str(compounds_per_year))
    t = Decimal(str(time))

    amount = principal * (Decimal('1') + rate_decimal / n) ** (n * t)
    interest = amount - principal
    return interest.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

principal = Decimal('10000.00')
rate = Decimal('5.5')
years = Decimal('5')

simple = calculate_simple_interest(principal, rate, years)
compound = calculate_compound_interest(principal, rate, int(years), 12)

print(f"\\nInvestment: ${principal}")
print(f"Rate: {rate}% per year")
print(f"Time: {years} years")

print(f"\\nSimple Interest:")
print(f"  Interest earned: ${simple}")
print(f"  Final amount: ${principal + simple}")

print(f"\\nCompound Interest (monthly):")
print(f"  Interest earned: ${compound}")
print(f"  Final amount: ${principal + compound}")

# Example 4: Invoice Calculator
print("\\n" + "="*70)
print("Example 4: Professional Invoice")
print("="*70)

class InvoiceItem:
    """Single item on an invoice."""

    def __init__(self, description: str, quantity: int,
                 unit_price: Decimal):
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total(self) -> Decimal:
        """Calculate line total."""
        return self.unit_price * Decimal(str(self.quantity))

class Invoice:
    """Professional invoice with tax."""

    def __init__(self, invoice_number: str):
        self.invoice_number = invoice_number
        self.items: List[InvoiceItem] = []

    def add_item(self, description: str, quantity: int, unit_price: Decimal):
        """Add item to invoice."""
        item = InvoiceItem(description, quantity, unit_price)
        self.items.append(item)

    def get_subtotal(self) -> Decimal:
        """Calculate subtotal."""
        total = Decimal('0')
        for item in self.items:
            total += item.get_total()
        return total

    def get_tax(self, tax_rate: Decimal) -> Decimal:
        """Calculate tax."""
        return (self.get_subtotal() * tax_rate).quantize(
            Decimal('0.01'), rounding=ROUND_HALF_UP)

    def get_total(self, tax_rate: Decimal) -> Decimal:
        """Calculate total with tax."""
        return self.get_subtotal() + self.get_tax(tax_rate)

    def print_invoice(self, tax_rate: Decimal):
        """Print formatted invoice."""
        print("\\n" + "="*60)
        print(f"INVOICE #{self.invoice_number}")
        print("="*60)

        print(f"\\n{'Description':<30s} {'Qty':>5s} {'Price':>10s} {'Total':>10s}")
        print("-"*60)

        for item in self.items:
            total = item.get_total()
            print(f"{item.description:<30s} {item.quantity:5d} "
                  f"${item.unit_price:>9.2f} ${total:>9.2f}")

        print("-"*60)
        subtotal = self.get_subtotal()
        tax = self.get_tax(tax_rate)
        total = self.get_total(tax_rate)

        print(f"{'Subtotal:':<48s} ${subtotal:>9.2f}")
        print(f"{'Tax (' + str(tax_rate * 100) + '%):':<48s} ${tax:>9.2f}")
        print("="*60)
        print(f"{'TOTAL:':<48s} ${total:>9.2f}")
        print("="*60)

# Create invoice
invoice = Invoice("INV-2025-001")
invoice.add_item("Web Development (10 hrs)", 10, Decimal("125.00"))
invoice.add_item("Logo Design", 1, Decimal("450.00"))
invoice.add_item("Hosting Setup", 1, Decimal("75.00"))
invoice.add_item("Domain Registration", 1, Decimal("12.99"))

tax_rate = Decimal("0.0825")
invoice.print_invoice(tax_rate)

# Example 5: Currency Exchange
print("\\n" + "="*70)
print("Example 5: Currency Exchange Rates")
print("="*70)

class CurrencyConverter:
    """Convert between currencies with precision."""

    def __init__(self):
        # Exchange rates to USD
        self.rates = {
            'USD': Decimal('1.00'),
            'EUR': Decimal('0.85'),
            'GBP': Decimal('0.73'),
            'JPY': Decimal('110.50'),
            'CAD': Decimal('1.25'),
            'AUD': Decimal('1.35')
        }

    def convert(self, amount: Decimal, from_currency: str,
                to_currency: str) -> Decimal:
        """Convert amount between currencies."""
        # Convert to USD first
        usd_amount = amount / self.rates[from_currency]
        # Then to target currency
        result = usd_amount * self.rates[to_currency]
        return result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

converter = CurrencyConverter()

amount = Decimal("1000.00")
from_curr = "USD"

print(f"\\nConverting ${amount} {from_curr}:")

for currency in ['EUR', 'GBP', 'JPY', 'CAD', 'AUD']:
    converted = converter.convert(amount, from_curr, currency)
    print(f"  {currency}: {converted:>10}")

# Example 6: Discount Calculator
print("\\n" + "="*70)
print("Example 6: Multi-tier Discount System")
print("="*70)

def apply_discounts(price: Decimal, discounts: List[Decimal]) -> Decimal:
    """Apply multiple sequential discounts."""
    final_price = price

    for discount in discounts:
        reduction = final_price * (discount / Decimal('100'))
        final_price -= reduction

    return final_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

original = Decimal("500.00")
discounts = [Decimal('20'), Decimal('10'), Decimal('5')]

print(f"\\nOriginal Price: ${original}")
print(f"Discounts: {', '.join(str(d) + '%' for d in discounts)}")

# Calculate step by step
current_price = original
print(f"\\nCalculation:")
print(f"  Start: ${current_price:.2f}")

for discount in discounts:
    reduction = current_price * (discount / Decimal('100'))
    current_price -= reduction
    print(f"  After {discount}% off: ${current_price:.2f}")

final = apply_discounts(original, discounts)
total_saved = original - final
percent_saved = (total_saved / original) * Decimal('100')

print(f"\\nFinal Price: ${final:.2f}")
print(f"Total Saved: ${total_saved:.2f} ({percent_saved:.1f}%)")

# Example 7: Tip Calculator
print("\\n" + "="*70)
print("Example 7: Tip Calculator with Splitting")
print("="*70)

def calculate_tip(bill: Decimal, tip_percent: Decimal,
                 split_ways: int = 1) -> Dict[str, Decimal]:
    """Calculate tip and split bill."""
    tip_amount = bill * (tip_percent / Decimal('100'))
    total = bill + tip_amount
    per_person = total / Decimal(str(split_ways))

    return {
        'bill': bill,
        'tip': tip_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'total': total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        'per_person': per_person.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    }

bill = Decimal("147.50")
tip_percentages = [Decimal('15'), Decimal('18'), Decimal('20')]
split = 4

print(f"\\nBill: ${bill}")
print(f"Split {split} ways")

print(f"\\nTip Options:")
for tip_pct in tip_percentages:
    result = calculate_tip(bill, tip_pct, split)
    print(f"\\n  {tip_pct}% Tip:")
    print(f"    Tip amount:  ${result['tip']}")
    print(f"    Total:       ${result['total']}")
    print(f"    Per person:  ${result['per_person']}")

print("\\n" + "="*70)
print("decimal.Decimal examples complete!")
print("="*70)
print("\\nBest Practices:")
print("  • Use string initialization: Decimal('10.50')")
print("  • Use quantize() for rounding")
print("  • Essential for money calculations")
print("  • Avoid float conversion")
'''
    }
}

def upgrade_lessons():
    """Upgrade all critical lessons."""
    print("="*80)
    print("UPGRADING 5 CRITICAL PYTHON LESSONS")
    print("="*80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Track changes
    for lesson_id, upgrade_data in UPGRADES.items():
        # Find lesson
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)

        if lesson:
            old_length = len(lesson.get('fullSolution', ''))
            lesson['fullSolution'] = upgrade_data['solution']
            new_length = len(lesson['fullSolution'])

            print(f"\nLesson {lesson_id}: {lesson['title']}")
            print(f"  {old_length:,} -> {new_length:,} characters "
                  f"(+{new_length - old_length:,}, +{((new_length - old_length)/old_length*100):.1f}%)")

    # Save
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    print("\n" + "="*80)
    print("CRITICAL LESSONS UPGRADED!")
    print("="*80)
    print(f"\nUpgraded {len(UPGRADES)} critical lessons")
    print("All lessons now have comprehensive examples and explanations")

if __name__ == '__main__':
    upgrade_lessons()
