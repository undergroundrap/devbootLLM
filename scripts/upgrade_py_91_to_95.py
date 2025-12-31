#!/usr/bin/env python3
"""
Upgrade Python lessons 91-95 with comprehensive content.
- Lesson 91: Dict Comprehensions
- Lesson 92: Dictionaries
- Lesson 93: Dictionary Fundamentals
- Lesson 94: Dictionary Updates
- Lesson 95: Iterate Dict (keys)
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 91-95
lesson91 = next(l for l in lessons if l['id'] == 91)
lesson92 = next(l for l in lessons if l['id'] == 92)
lesson93 = next(l for l in lessons if l['id'] == 93)
lesson94 = next(l for l in lessons if l['id'] == 94)
lesson95 = next(l for l in lessons if l['id'] == 95)

# Upgrade Lesson 91: Dict Comprehensions
lesson91['fullSolution'] = '''"""
Dict Comprehensions

Master dictionary comprehensions in Python—the concise way to create
dictionaries from iterables. Learn basic patterns, conditional logic,
transformations, and advanced techniques. Essential for data processing.

**Zero Package Installation Required**
"""

# Example 1: Basic Dictionary Comprehension
print("="*70)
print("Example 1: Basic Dictionary Comprehension Syntax")
print("="*70)

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Cube numbers
cubes = {x: x**3 for x in range(1, 6)}
print(f"Cubes: {cubes}")

# Powers of 2
powers = {x: 2**x for x in range(6)}
print(f"Powers of 2: {powers}")

# String lengths
fruits = ["apple", "banana", "cherry"]
lengths = {fruit: len(fruit) for fruit in fruits}
print(f"\\nFruit lengths: {lengths}")
print()

# Example 2: From Two Lists with zip()
print("="*70)
print("Example 2: Create from Parallel Lists")
print("="*70)

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]

# Combine with comprehension
people = {name: age for name, age in zip(names, ages)}
print(f"Names: {names}")
print(f"Ages: {ages}")
print(f"\\nPeople: {people}")

# More complex
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999.99, 29.99, 79.99]
inventory = {product: {"price": price} for product, price in zip(products, prices)}

print(f"\\nInventory:")
for item, details in inventory.items():
    print(f"  {item}: {details}")
print()

# Example 3: With Conditional (if)
print("="*70)
print("Example 3: Comprehension with if Condition")
print("="*70)

# Only even numbers
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {evens}")

# Only odd numbers
odds = {x: x**2 for x in range(10) if x % 2 != 0}
print(f"Odd squares: {odds}")

# Filter by string length
words = ["cat", "elephant", "dog", "hippopotamus", "bee"]
long_words = {word: len(word) for word in words if len(word) > 3}
print(f"\\nWords > 3 chars: {long_words}")

# Filter by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scores = {name: score for name, score in scores.items() if score >= 90}
print(f"\\nHigh scores (>=90): {high_scores}")
print()

# Example 4: Conditional Expression (if-else in value)
print("="*70)
print("Example 4: Conditional Expression in Comprehension")
print("="*70)

# Grade classification
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
grades = {name: "A" if score >= 90 else "B" for name, score in scores.items()}
print(f"Scores: {scores}")
print(f"Grades: {grades}")

# More complex conditional
status = {name: "Pass" if score >= 80 else "Fail"
          for name, score in scores.items()}
print(f"\\nStatus: {status}")

# Multiple conditions
tier = {name: "Gold" if score >= 90 else "Silver" if score >= 80 else "Bronze"
        for name, score in scores.items()}
print(f"Tiers: {tier}")
print()

# Example 5: Transform Keys
print("="*70)
print("Example 5: Transforming Keys in Comprehension")
print("="*70)

# Uppercase keys
data = {"name": "Alice", "age": 30, "city": "NYC"}
upper_keys = {key.upper(): value for key, value in data.items()}
print(f"Original: {data}")
print(f"Upper keys: {upper_keys}")

# Add prefix to keys
prefixed = {f"user_{key}": value for key, value in data.items()}
print(f"Prefixed: {prefixed}")

# Reverse dictionary (swap keys and values)
reversed_dict = {value: key for key, value in data.items()}
print(f"\\nReversed: {reversed_dict}")
print()

# Example 6: Transform Values
print("="*70)
print("Example 6: Transforming Values in Comprehension")
print("="*70)

prices = {"apple": 1.20, "banana": 0.50, "orange": 0.80}
print(f"Prices: {prices}")

# Add tax (10%)
with_tax = {item: price * 1.10 for item, price in prices.items()}
print(f"With 10% tax: {with_tax}")

# Round prices
rounded = {item: round(price, 1) for item, price in prices.items()}
print(f"Rounded: {rounded}")

# Format as strings
formatted = {item: f"${price:.2f}" for item, price in prices.items()}
print(f"Formatted: {formatted}")
print()

# Example 7: Nested Comprehensions
print("="*70)
print("Example 7: Nested Dictionary Comprehension")
print("="*70)

# Create multiplication table
mult_table = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print("Multiplication table:")
for i, row in mult_table.items():
    print(f"  {i}: {row}")

# Nested from lists
teams = ["Red", "Blue", "Green"]
members = ["Alice", "Bob"]
team_members = {team: {member: False for member in members} for team in teams}

print(f"\\nTeam members:")
for team, members_dict in team_members.items():
    print(f"  {team}: {members_dict}")
print()

# Example 8: From Enumerate
print("="*70)
print("Example 8: Comprehension with enumerate()")
print("="*70)

items = ["apple", "banana", "cherry", "date"]

# Index as key
indexed = {i: item for i, item in enumerate(items)}
print(f"Items: {items}")
print(f"Indexed: {indexed}")

# Start from different index
indexed_from_1 = {i: item for i, item in enumerate(items, start=1)}
print(f"Indexed from 1: {indexed_from_1}")

# Item as key, index as value
reverse_indexed = {item: i for i, item in enumerate(items)}
print(f"Reverse indexed: {reverse_indexed}")
print()

# Example 9: Filtering and Transforming Existing Dict
print("="*70)
print("Example 9: Process Existing Dictionary")
print("="*70)

inventory = {
    "laptop": {"price": 999.99, "stock": 5},
    "mouse": {"price": 29.99, "stock": 0},
    "keyboard": {"price": 79.99, "stock": 12},
    "monitor": {"price": 299.99, "stock": 0}
}

# Filter: only items in stock
in_stock = {item: details for item, details in inventory.items()
            if details["stock"] > 0}

print("In stock items:")
for item, details in in_stock.items():
    print(f"  {item}: {details}")

# Extract just prices
prices = {item: details["price"] for item, details in inventory.items()}
print(f"\\nJust prices: {prices}")

# Calculate discounted prices (20% off for in-stock items)
discounted = {item: details["price"] * 0.8
              for item, details in inventory.items()
              if details["stock"] > 0}
print(f"\\nDiscounted prices: {discounted}")
print()

# Example 10: Practical Application - Data Processing
print("="*70)
print("Example 10: Real-World Use Case - Process Survey Data")
print("="*70)

# Simulated survey responses
responses = [
    {"user_id": 1, "question": "satisfaction", "answer": "very_satisfied"},
    {"user_id": 2, "question": "satisfaction", "answer": "satisfied"},
    {"user_id": 3, "question": "satisfaction", "answer": "neutral"},
    {"user_id": 1, "question": "recommend", "answer": "yes"},
    {"user_id": 2, "question": "recommend", "answer": "yes"},
    {"user_id": 3, "question": "recommend", "answer": "no"}
]

print("Survey responses:")
for resp in responses[:3]:
    print(f"  {resp}")
print("  ...")

# Group by question
by_question = {}
for resp in responses:
    question = resp["question"]
    if question not in by_question:
        by_question[question] = []
    by_question[question].append(resp["answer"])

print(f"\\nGrouped by question:")
for q, answers in by_question.items():
    print(f"  {q}: {answers}")

# Count responses per question using comprehension
question_counts = {
    question: len([r for r in responses if r["question"] == question])
    for question in set(r["question"] for r in responses)
}

print(f"\\nResponse counts: {question_counts}")

# Calculate satisfaction score (using comprehension)
score_map = {"very_satisfied": 5, "satisfied": 4, "neutral": 3, "dissatisfied": 2, "very_dissatisfied": 1}

satisfaction_responses = [r["answer"] for r in responses if r["question"] == "satisfaction"]
avg_satisfaction = sum(score_map.get(ans, 0) for ans in satisfaction_responses) / len(satisfaction_responses)

print(f"\\nSatisfaction responses: {satisfaction_responses}")
print(f"Average satisfaction score: {avg_satisfaction:.2f}/5.00")

# Summary report using comprehension
summary = {
    "total_responses": len(responses),
    "unique_users": len(set(r["user_id"] for r in responses)),
    "questions_asked": len(set(r["question"] for r in responses)),
    "avg_satisfaction": round(avg_satisfaction, 2)
}

print("\\n" + "="*70)
print("SURVEY SUMMARY".center(70))
print("="*70)
for key, value in summary.items():
    print(f"  {key.replace('_', ' ').title()}: {value}")
print("="*70)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. {k: v for item in iterable} - Basic syntax")
print("2. {k: v for k, v in zip(keys, values)} - From two lists")
print("3. {k: v for item in iterable if condition} - With filter")
print("4. {k: (v1 if cond else v2) for ...} - Conditional value")
print("5. {k.upper(): v for k, v in dict.items()} - Transform keys")
print("6. {k: v*2 for k, v in dict.items()} - Transform values")
print("7. {i: item for i, item in enumerate(list)} - From enumerate")
print("8. Nested: {i: {j: ... for j in ...} for i in ...}")
print("9. More concise than equivalent for loops")
print("10. Essential for data transformation and filtering")
print("="*70)
'''

# Upgrade Lesson 92-95 will be added in the same file but I need to keep this message short
# Let me save the file and continue in next message...

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lessons 91:")
print(f"  91: Dict Comprehensions - {len(lesson91['fullSolution'])} chars")
print("\nBatch 91-95: Lesson 91 complete, continuing with 92-95...")
