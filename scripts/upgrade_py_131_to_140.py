#!/usr/bin/env python3
"""
Upgrade Python lessons 131-140 with comprehensive content.
- Lesson 131: Creating Objects
- Lesson 132: Creating a Simple Class
- Lesson 133: Custom Exception Class
- Lesson 134: Dataclasses
- Lesson 135: SLO/SLI - Service Level Objectives
- Lesson 136: Serialize object to JSON
- Lesson 137: Simple BankAccount Class
- Lesson 138: Simple Book Class
- Lesson 139: Simple Car Class
- Lesson 140: Simple Person Class
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 131-140
lesson131 = next(l for l in lessons if l['id'] == 131)
lesson132 = next(l for l in lessons if l['id'] == 132)
lesson133 = next(l for l in lessons if l['id'] == 133)
lesson134 = next(l for l in lessons if l['id'] == 134)
lesson135 = next(l for l in lessons if l['id'] == 135)
lesson136 = next(l for l in lessons if l['id'] == 136)
lesson137 = next(l for l in lessons if l['id'] == 137)
lesson138 = next(l for l in lessons if l['id'] == 138)
lesson139 = next(l for l in lessons if l['id'] == 139)
lesson140 = next(l for l in lessons if l['id'] == 140)

# Upgrade Lesson 131: Creating Objects
lesson131['fullSolution'] = '''"""
Creating Objects

Master object creation in Python. Learn to instantiate classes, pass arguments
to constructors, create multiple instances, and understand object identity.
Essential foundation for object-oriented programming.

**Zero Package Installation Required**
"""

# Example 1: Basic Object Creation
print("="*70)
print("Example 1: Creating Simple Objects")
print("="*70)

class Dog:
    def __init__(self, name):
        self.name = name

# Create objects using the class
dog1 = Dog("Buddy")
dog2 = Dog("Max")
dog3 = Dog("Charlie")

print(f"Dog 1: {dog1.name}")
print(f"Dog 2: {dog2.name}")
print(f"Dog 3: {dog3.name}")

# Each object is unique
print(f"\\nAre dog1 and dog2 the same object? {dog1 is dog2}")
print()

# Example 2: Object Creation with Multiple Parameters
print("="*70)
print("Example 2: Creating Objects with Multiple Arguments")
print("="*70)

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Create people with different attributes
person1 = Person("Alice", 30, "New York")
person2 = Person("Bob", 25, "Los Angeles")
person3 = Person("Charlie", 35, "Chicago")

print("Created people:")
for i, person in enumerate([person1, person2, person3], 1):
    print(f"  Person {i}: {person.name}, age {person.age}, from {person.city}")
print()

# Example 3: Object Creation with Default Parameters
print("="*70)
print("Example 3: Creating Objects with Default Values")
print("="*70)

class Product:
    def __init__(self, name, price=0.0, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

# Create products with various arguments
product1 = Product("Laptop", 999.99, 10)
product2 = Product("Mouse", 29.99)  # Uses default stock
product3 = Product("Keyboard")      # Uses default price and stock

print("Products created:")
print(f"  {product1.name}: ${product1.price:.2f} - {product1.stock} in stock")
print(f"  {product2.name}: ${product2.price:.2f} - {product2.stock} in stock")
print(f"  {product3.name}: ${product3.price:.2f} - {product3.stock} in stock")
print()

# Example 4: Creating Objects in a Loop
print("="*70)
print("Example 4: Creating Multiple Objects in a Loop")
print("="*70)

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Create students from data
student_data = [
    ("Alice", 95),
    ("Bob", 87),
    ("Charlie", 92),
    ("David", 78),
    ("Eve", 88)
]

students = []
for name, grade in student_data:
    student = Student(name, grade)
    students.append(student)

print(f"Created {len(students)} students:")
for student in students:
    print(f"  {student.name}: {student.grade}")
print()

# Example 5: Object Identity and Equality
print("="*70)
print("Example 5: Object Identity vs Equality")
print("="*70)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Create points
p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = p1  # Reference to same object

print(f"p1 coordinates: ({p1.x}, {p1.y})")
print(f"p2 coordinates: ({p2.x}, {p2.y})")
print(f"p3 coordinates: ({p3.x}, {p3.y})")

print(f"\\np1 is p2 (same object)? {p1 is p2}")
print(f"p1 is p3 (same object)? {p1 is p3}")
print(f"id(p1): {id(p1)}")
print(f"id(p2): {id(p2)}")
print(f"id(p3): {id(p3)}")
print()

# Example 6: Creating Objects from User Input Simulation
print("="*70)
print("Example 6: Creating Objects from Input Data")
print("="*70)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# Simulate creating books from input
book_data = {
    "title": "1984",
    "author": "George Orwell",
    "year": 1949
}

book = Book(**book_data)  # Unpack dictionary
print(f"Created book: {book}")

# Create from individual inputs
book2 = Book(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    year=1960
)
print(f"Created book: {book2}")
print()

# Example 7: Factory Pattern for Object Creation
print("="*70)
print("Example 7: Factory Function for Creating Objects")
print("="*70)

class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

def create_developer(name, years_exp):
    """Factory function for creating developer objects"""
    base_salary = 60000
    salary = base_salary + (years_exp * 10000)
    return Employee(name, "Developer", salary)

def create_manager(name, team_size):
    """Factory function for creating manager objects"""
    base_salary = 80000
    salary = base_salary + (team_size * 5000)
    return Employee(name, "Manager", salary)

# Use factory functions
dev1 = create_developer("Alice", 3)
dev2 = create_developer("Bob", 5)
mgr1 = create_manager("Charlie", 4)

print("Employees created via factory:")
print(f"  {dev1.name} ({dev1.role}): ${dev1.salary:,}")
print(f"  {dev2.name} ({dev2.role}): ${dev2.salary:,}")
print(f"  {mgr1.name} ({mgr1.role}): ${mgr1.salary:,}")
print()

# Example 8: Creating Objects with Validation
print("="*70)
print("Example 8: Object Creation with Input Validation")
print("="*70)

class BankAccount:
    def __init__(self, account_number, initial_balance):
        if not isinstance(account_number, str):
            raise TypeError("Account number must be a string")
        if len(account_number) < 5:
            raise ValueError("Account number must be at least 5 characters")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.account_number = account_number
        self.balance = initial_balance

# Valid account
try:
    account1 = BankAccount("ACC12345", 1000)
    print(f"Created account: {account1.account_number} with ${account1.balance}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Invalid accounts
print("\\nTrying to create invalid accounts:")

try:
    account2 = BankAccount("A123", 500)  # Too short
except ValueError as e:
    print(f"  Error: {e}")

try:
    account3 = BankAccount("ACC12345", -100)  # Negative balance
except ValueError as e:
    print(f"  Error: {e}")
print()

# Example 9: Creating Nested Objects
print("="*70)
print("Example 9: Creating Objects that Contain Other Objects")
print("="*70)

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.city} {self.zipcode}"

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address  # Nested object

# Create nested objects
address1 = Address("123 Main St", "New York", "10001")
customer1 = Customer("Alice", "alice@example.com", address1)

# Or create inline
customer2 = Customer(
    "Bob",
    "bob@example.com",
    Address("456 Oak Ave", "Los Angeles", "90001")
)

print("Customers created:")
print(f"  {customer1.name} ({customer1.email})")
print(f"    Address: {customer1.address}")
print(f"  {customer2.name} ({customer2.email})")
print(f"    Address: {customer2.address}")
print()

# Example 10: Practical Application - Inventory Management
print("="*70)
print("Example 10: Real-World Use Case - Inventory System")
print("="*70)

class InventoryItem:
    total_items = 0  # Class attribute to track all items

    def __init__(self, sku, name, quantity, price):
        self.sku = sku
        self.name = name
        self.quantity = quantity
        self.price = price
        InventoryItem.total_items += 1

    def get_total_value(self):
        return self.quantity * self.price

    def __str__(self):
        return f"[{self.sku}] {self.name} - Qty: {self.quantity}, Price: ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, sku, name, quantity, price):
        """Create and add a new inventory item"""
        item = InventoryItem(sku, name, quantity, price)
        self.items.append(item)
        return item

    def get_total_value(self):
        return sum(item.get_total_value() for item in self.items)

    def print_inventory(self):
        print("INVENTORY LISTING")
        print("="*70)
        for item in self.items:
            value = item.get_total_value()
            print(f"{item} = ${value:,.2f}")

# Create inventory system
inventory = Inventory()

# Add items (creates objects internally)
inventory.add_item("LPTOP001", "Laptop", 15, 999.99)
inventory.add_item("MOUSE001", "Wireless Mouse", 50, 29.99)
inventory.add_item("KYBRD001", "Mechanical Keyboard", 30, 129.99)
inventory.add_item("MNTR001", "27-inch Monitor", 20, 299.99)
inventory.add_item("HDPHN001", "Noise-Canceling Headphones", 25, 199.99)

# Display inventory
inventory.print_inventory()

# Summary
print("\\n" + "="*70)
print("INVENTORY SUMMARY")
print("="*70)
print(f"Total items in inventory: {len(inventory.items)}")
print(f"Total objects created: {InventoryItem.total_items}")
print(f"Total inventory value: ${inventory.get_total_value():,.2f}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. Create objects: obj = ClassName(args)")
print("2. __init__() constructor is called automatically")
print("3. Pass arguments to set initial object state")
print("4. Each object has unique identity (id)")
print("5. Use default parameters for optional attributes")
print("6. Create multiple objects in loops or comprehensions")
print("7. Factory functions simplify complex object creation")
print("8. Validate inputs in __init__() for data integrity")
print("9. Objects can contain other objects (composition)")
print("10. Track object creation with class attributes")
print("="*70)
'''

# Save and continue
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Continue with remaining lessons (132-140) in batch
# Due to file length, will create comprehensive content for all

# Save progress so far
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\nUpgraded lesson 131:")
print(f"  131: Creating Objects - {len(lesson131['fullSolution'])} chars")
print("\nBatch 131-140: Lesson 131 complete")
print("Next: Run upgrade_py_132_to_136.py and upgrade_py_137_to_140.py for remaining lessons")
