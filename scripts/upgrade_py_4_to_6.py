#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 4: Instance Variables
lesson4 = next(l for l in lessons if l['id'] == 4)
lesson4['fullSolution'] = '''"""
Instance Variables - Object State

Learn how objects store their own data using instance variables.
Essential for object-oriented programming.

**Zero Package Installation Required**
"""

# Example 1: Basic Instance Variables
print("="*70)
print("Example 1: Creating Objects with State")
print("="*70)

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(f"{person1.name} is {person1.age} years old")
print(f"{person2.name} is {person2.age} years old")

# Example 2: Multiple Instance Variables
print("\\n" + "="*70)
print("Example 2: Objects with Multiple Attributes")
print("="*70)

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = 0  # Default value

car1 = Car("Toyota", "Camry", 2020, "Blue")
car2 = Car("Honda", "Civic", 2021, "Red")

print(f"Car 1: {car1.year} {car1.color} {car1.make} {car1.model}")
print(f"Car 2: {car2.year} {car2.color} {car2.make} {car2.model}")

# Example 3: Modifying Instance Variables
print("\\n" + "="*70)
print("Example 3: Changing Object State")
print("="*70)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

account = BankAccount("Alice", 1000)
print(f"Initial balance: ${account.balance}")
account.deposit(500)
account.withdraw(200)

# Example 4: Instance vs Class Variables
print("\\n" + "="*70)
print("Example 4: Instance vs Class Variables")
print("="*70)

class Dog:
    species = "Canis familiaris"  # Class variable (shared)

    def __init__(self, name, breed):
        self.name = name    # Instance variable (unique)
        self.breed = breed  # Instance variable (unique)

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

print(f"{dog1.name} is a {dog1.breed}")
print(f"{dog2.name} is a {dog2.breed}")
print(f"Both are {Dog.species}")

# Example 5: Private Instance Variables
print("\\n" + "="*70)
print("Example 5: Encapsulation with Private Variables")
print("="*70)

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # Convention: _ means private

    def check_password(self, password):
        return self._password == password

user = User("alice", "secret123")
print(f"Username: {user.username}")
print(f"Password correct? {user.check_password('secret123')}")
print(f"Password correct? {user.check_password('wrong')}")

# Example 6: Default Values
print("\\n" + "="*70)
print("Example 6: Default Instance Variable Values")
print("="*70)

class Product:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity  # Default is 0
        self.discount = 0  # Can set in __init__

product1 = Product("Laptop", 999.99, 10)
product2 = Product("Mouse", 24.99)  # quantity defaults to 0

print(f"{product1.name}: ${product1.price}, Qty: {product1.quantity}")
print(f"{product2.name}: ${product2.price}, Qty: {product2.quantity}")

# Example 7: Tracking State Changes
print("\\n" + "="*70)
print("Example 7: Object State Over Time")
print("="*70)

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def reset(self):
        self.count = 0

counter = Counter()
print(f"Initial: {counter.count}")
counter.increment()
print(f"After increment: {counter.count}")
counter.increment()
counter.increment()
print(f"After 2 more increments: {counter.count}")
counter.reset()
print(f"After reset: {counter.count}")

print("\\n" + "="*70)
print("Instance Variables Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Instance variables store object-specific data")
print("  - Use self.variable_name in __init__")
print("  - Each object has its own copy")
print("  - Can be modified after creation")
print("  - Essential for OOP")
'''

# Lesson 5: Variables & Data Types
lesson5 = next(l for l in lessons if l['id'] == 5)
lesson5['fullSolution'] = '''"""
Variables & Data Types - Python Fundamentals

Learn to store and work with different types of data in Python.
Foundation for all programming concepts.

**Zero Package Installation Required**
"""

# Example 1: String Variables
print("="*70)
print("Example 1: String Variables")
print("="*70)

name = "Alice"
city = "New York"
message = "Hello, World!"

print(f"Name: {name}")
print(f"City: {city}")
print(f"Message: {message}")

# Example 2: Number Variables
print("\\n" + "="*70)
print("Example 2: Integer and Float")
print("="*70)

age = 25  # Integer (whole number)
height = 5.6  # Float (decimal number)
temperature = -10  # Negative integer

print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Temperature: {temperature}")

# Example 3: Boolean Variables
print("\\n" + "="*70)
print("Example 3: Boolean (True/False)")
print("="*70)

is_student = True
is_employed = False
has_license = True

print(f"Is student? {is_student}")
print(f"Is employed? {is_employed}")
print(f"Has license? {has_license}")

# Example 4: Variable Assignment
print("\\n" + "="*70)
print("Example 4: Creating and Updating Variables")
print("="*70)

x = 10
print(f"Initial value: x = {x}")

x = 20
print(f"Updated value: x = {x}")

x = x + 5
print(f"After adding 5: x = {x}")

# Example 5: Multiple Assignment
print("\\n" + "="*70)
print("Example 5: Multiple Variables at Once")
print("="*70)

# Assign same value to multiple variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# Assign different values
x, y, z = 1, 2, 3
print(f"x = {x}, y = {y}, z = {z}")

# Example 6: Type Conversion
print("\\n" + "="*70)
print("Example 6: Converting Between Types")
print("="*70)

# String to integer
age_str = "25"
age_int = int(age_str)
print(f"String '{age_str}' -> Integer {age_int}")

# Integer to string
number = 42
text = str(number)
print(f"Integer {number} -> String '{text}'")

# String to float
price_str = "19.99"
price_float = float(price_str)
print(f"String '{price_str}' -> Float {price_float}")

# Example 7: Variable Naming Rules
print("\\n" + "="*70)
print("Example 7: Valid Variable Names")
print("="*70)

# Good variable names
user_name = "Alice"
user_age = 25
total_price = 99.99
is_active = True

# Convention: use snake_case for variables
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"

print(f"Full name: {full_name}")

# Example 8: Working with All Types
print("\\n" + "="*70)
print("Example 8: Complete Example")
print("="*70)

# Product information
product_name = "Laptop"
product_price = 999.99
product_quantity = 5
in_stock = True

print("Product Details:")
print(f"  Name: {product_name}")
print(f"  Price: ${product_price}")
print(f"  Quantity: {product_quantity}")
print(f"  In stock: {in_stock}")

# Calculate total value
total_value = product_price * product_quantity
print(f"  Total value: ${total_value}")

# Example 9: None Type
print("\\n" + "="*70)
print("Example 9: None (No Value)")
print("="*70)

result = None  # Represents "no value"
print(f"Result: {result}")

# Check if None
if result is None:
    print("Result has no value yet")

# Example 10: Checking Types
print("\\n" + "="*70)
print("Example 10: Checking Variable Types")
print("="*70)

value1 = 42
value2 = "Hello"
value3 = 3.14
value4 = True

print(f"{value1} is {type(value1).__name__}")
print(f"{value2} is {type(value2).__name__}")
print(f"{value3} is {type(value3).__name__}")
print(f"{value4} is {type(value4).__name__}")

print("\\n" + "="*70)
print("Variables & Data Types Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Variables store data")
print("  - Main types: str, int, float, bool")
print("  - Use = to assign values")
print("  - Can convert between types")
print("  - Use descriptive names")
'''

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 4-5:")
print(f"  4: Instance Variables (336 -> {len(lesson4['fullSolution'])} chars)")
print(f"  5: Variables & Data Types (184 -> {len(lesson5['fullSolution'])} chars)")
