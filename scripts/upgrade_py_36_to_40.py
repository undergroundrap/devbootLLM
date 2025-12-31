#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 36: Nested Loops
lesson36 = next(l for l in lessons if l['id'] == 36)
lesson36['fullSolution'] = '''"""
Nested Loops - Multi-Level Iteration

Master loops within loops for multi-dimensional processing.
Essential for tables, grids, and complex iterations.

**Zero Package Installation Required**
"""

# Example 1: Basic Nested Loop
print("="*70)
print("Example 1: Simple 2D Iteration")
print("="*70)

for i in range(3):
    for j in range(3):
        print(f"  i={i}, j={j}")

# Example 2: Multiplication Table
print("\\n" + "="*70)
print("Example 2: Times Table")
print("="*70)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")

# Example 3: Pattern Printing
print("\\n" + "="*70)
print("Example 3: Print Rectangle")
print("="*70)

for i in range(3):
    for j in range(5):
        print("*", end="")
    print()

# Example 4: Nested List Iteration
print("\\n" + "="*70)
print("Example 4: 2D List Processing")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(f"{value} ", end="")
    print()

# Example 5: Find All Pairs
print("\\n" + "="*70)
print("Example 5: Generate Pairs")
print("="*70)

list1 = ["a", "b"]
list2 = [1, 2]

for letter in list1:
    for number in list2:
        print(f"  ({letter}, {number})")

# Example 6: Triangle Pattern
print("\\n" + "="*70)
print("Example 6: Print Triangle")
print("="*70)

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Example 7: Search 2D Array
print("\\n" + "="*70)
print("Example 7: Find Value in Matrix")
print("="*70)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

for row in grid:
    for value in row:
        if value == target:
            print(f"Found {target}!")
            found = True
            break
    if found:
        break

# Example 8: Sum 2D Array
print("\\n" + "="*70)
print("Example 8: Total All Values")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0
for row in matrix:
    for value in row:
        total += value

print(f"Sum: {total}")

print("\\n" + "="*70)
print("Nested Loops Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Loop inside another loop")
print("  - Outer loop runs, inner completes each time")
print("  - Use for tables and grids")
print("  - Watch performance with large data")
print("  - Can nest 3+ levels but keep simple")
'''

# Lesson 37: Nested Loops Fundamentals
lesson37 = next(l for l in lessons if l['id'] == 37)
lesson37['fullSolution'] = '''"""
Nested Loops Fundamentals - Understanding Iteration

Master the fundamentals of nested iteration patterns.
Essential for multi-dimensional data structures.

**Zero Package Installation Required**
"""

# Example 1: Understanding Execution Order
print("="*70)
print("Example 1: How Nested Loops Work")
print("="*70)

print("Outer loop i, Inner loop j:")
for i in range(3):
    print(f"Outer: i = {i}")
    for j in range(2):
        print(f"  Inner: j = {j}")

# Example 2: Row and Column Concept
print("\\n" + "="*70)
print("Example 2: Rows and Columns")
print("="*70)

rows = 3
cols = 4

for row in range(rows):
    for col in range(cols):
        print(f"({row},{col})", end=" ")
    print()

# Example 3: Counting Iterations
print("\\n" + "="*70)
print("Example 3: Total Iterations")
print("="*70)

count = 0
for i in range(3):
    for j in range(4):
        count += 1

print(f"Total iterations: {count}")
print(f"Formula: 3 x 4 = {3 * 4}")

# Example 4: Building Tables
print("\\n" + "="*70)
print("Example 4: Create Number Table")
print("="*70)

for i in range(1, 4):
    for j in range(1, 4):
        value = i * 10 + j
        print(f"{value:3}", end=" ")
    print()

# Example 5: Nested List Creation
print("\\n" + "="*70)
print("Example 5: Build 2D List")
print("="*70)

matrix = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(i + j)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Example 6: Break in Nested Loops
print("\\n" + "="*70)
print("Example 6: Break Only Breaks Inner")
print("="*70)

for i in range(3):
    print(f"Outer: {i}")
    for j in range(3):
        if j == 1:
            break
        print(f"  Inner: {j}")

# Example 7: Common Pattern - Grid Initialization
print("\\n" + "="*70)
print("Example 7: Initialize Grid with Zeros")
print("="*70)

grid = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(0)
    grid.append(row)

print("Zero grid:")
for row in grid:
    print(f"  {row}")

print("\\n" + "="*70)
print("Nested Loops Fundamentals Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Inner loop completes fully each outer iteration")
print("  - Total iterations = outer * inner")
print("  - Good for 2D arrays and grids")
print("  - break only exits innermost loop")
print("  - Essential for matrix operations")
'''

# Lesson 38: String Formatting
lesson38 = next(l for l in lessons if l['id'] == 38)
lesson38['fullSolution'] = '''"""
String Formatting - Classic Methods

Master traditional string formatting techniques.
Foundation for creating formatted output.

**Zero Package Installation Required**
"""

# Example 1: Basic Concatenation
print("="*70)
print("Example 1: Join Strings")
print("="*70)

name = "Alice"
age = 25

message = "Name: " + name + ", Age: " + str(age)
print(message)

# Example 2: format() Method
print("\\n" + "="*70)
print("Example 2: Using .format()")
print("="*70)

text = "Hello, {}!".format("World")
print(text)

text2 = "{} is {} years old".format("Bob", 30)
print(text2)

# Example 3: Numbered Placeholders
print("\\n" + "="*70)
print("Example 3: Positional Arguments")
print("="*70)

text = "{0} {1} {0}".format("Hello", "World")
print(text)

# Example 4: Named Placeholders
print("\\n" + "="*70)
print("Example 4: Named Arguments")
print("="*70)

text = "Name: {name}, Age: {age}".format(name="Alice", age=25)
print(text)

# Example 5: Number Formatting
print("\\n" + "="*70)
print("Example 5: Format Numbers")
print("="*70)

pi = 3.14159
print("Pi: {:.2f}".format(pi))
print("Pi: {:.4f}".format(pi))

price = 19.99
print("Price: ${:.2f}".format(price))

# Example 6: Padding and Alignment
print("\\n" + "="*70)
print("Example 6: Align Text")
print("="*70)

print("{:>10}".format("right"))
print("{:<10}".format("left"))
print("{:^10}".format("center"))

# Example 7: Old-Style % Formatting
print("\\n" + "="*70)
print("Example 7: Printf-Style")
print("="*70)

name = "Alice"
age = 25

print("Name: %s, Age: %d" % (name, age))
print("Price: $%.2f" % 19.99)

# Example 8: Multiple Values
print("\\n" + "="*70)
print("Example 8: Format Table Row")
print("="*70)

name = "Product"
price = 99.99
quantity = 5

print("{:<15} ${:>8.2f} {:>5}".format(name, price, quantity))

print("\\n" + "="*70)
print("String Formatting Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - .format() inserts values")
print("  - {} are placeholders")
print("  - {:.2f} for decimals")
print("  - {:>10} for alignment")
print("  - f-strings are preferred (modern)")
'''

# Lesson 39: String Formatting with f-strings
lesson39 = next(l for l in lessons if l['id'] == 39)
lesson39['fullSolution'] = '''"""
String Formatting with f-strings

Master modern f-string formatting (Python 3.6+).
Best practice for string interpolation in Python.

**Zero Package Installation Required**
"""

# Example 1: Basic f-strings
print("="*70)
print("Example 1: Simple Interpolation")
print("="*70)

name = "Alice"
age = 25

print(f"Name: {name}, Age: {age}")

# Example 2: Expressions in f-strings
print("\\n" + "="*70)
print("Example 2: Calculate Inside")
print("="*70)

x = 10
y = 5

print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")

# Example 3: Method Calls
print("\\n" + "="*70)
print("Example 3: Call Methods")
print("="*70)

text = "hello"
print(f"Uppercase: {text.upper()}")
print(f"Length: {len(text)}")

# Example 4: Number Formatting
print("\\n" + "="*70)
print("Example 4: Format Numbers")
print("="*70)

pi = 3.14159
print(f"Pi: {pi:.2f}")
print(f"Pi: {pi:.4f}")

price = 1234.56
print(f"Price: ${price:,.2f}")

# Example 5: Alignment
print("\\n" + "="*70)
print("Example 5: Align Text")
print("="*70)

left = "left"
center = "center"
right = "right"

print(f"{left:<10}|")
print(f"{center:^10}|")
print(f"{right:>10}|")

# Example 6: Padding with Zeros
print("\\n" + "="*70)
print("Example 6: Zero Padding")
print("="*70)

num = 42
print(f"Number: {num:05d}")

# Example 7: Multi-line f-strings
print("\\n" + "="*70)
print("Example 7: Multi-line Format")
print("="*70)

name = "Bob"
age = 30
city = "NYC"

info = f"""
Name: {name}
Age: {age}
City: {city}
"""
print(info)

# Example 8: Dictionary Values
print("\\n" + "="*70)
print("Example 8: Format Dict Values")
print("="*70)

user = {"name": "Alice", "age": 25}
print(f"User: {user['name']}, Age: {user['age']}")

# Example 9: List Elements
print("\\n" + "="*70)
print("Example 9: Format List Items")
print("="*70)

numbers = [10, 20, 30]
print(f"First: {numbers[0]}, Last: {numbers[-1]}")

# Example 10: Complex Formatting
print("\\n" + "="*70)
print("Example 10: Table with f-strings")
print("="*70)

products = [
    ("Laptop", 999.99, 5),
    ("Mouse", 24.99, 20)
]

for name, price, qty in products:
    print(f"{name:<10} ${price:>8.2f} x{qty:>3}")

print("\\n" + "="*70)
print("f-strings Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - f\"...{variable}...\" syntax")
print("  - Can include expressions")
print("  - {value:.2f} for decimals")
print("  - {value:>10} for alignment")
print("  - Preferred modern method")
'''

# Lesson 40: Terraform - Infrastructure Basics
lesson40 = next(l for l in lessons if l['id'] == 40)
lesson40['fullSolution'] = '''"""
Terraform - Infrastructure as Code Basics

Learn Infrastructure as Code concepts with Terraform simulation.
Understand resource provisioning patterns without cloud account.

**Zero Package Installation Required**
"""

# Example 1: Basic Resource Concept
print("="*70)
print("Example 1: Simulated Terraform Resource")
print("="*70)

class TerraformResource:
    def __init__(self, type, name, config):
        self.type = type
        self.name = name
        self.config = config
        self.id = f"{type}.{name}"

    def plan(self):
        print(f"Planning {self.id}:")
        for key, value in self.config.items():
            print(f"  {key} = {value}")

    def apply(self):
        print(f"Creating {self.id}...")
        print(f"  Resource created successfully")

# Create a simulated EC2 instance
instance = TerraformResource("aws_instance", "web_server", {
    "ami": "ami-12345678",
    "instance_type": "t2.micro",
    "tags": {"Name": "WebServer"}
})

instance.plan()
instance.apply()

# Example 2: Multiple Resources
print("\\n" + "="*70)
print("Example 2: Infrastructure with Multiple Resources")
print("="*70)

resources = []

# VPC
vpc = TerraformResource("aws_vpc", "main", {
    "cidr_block": "10.0.0.0/16"
})
resources.append(vpc)

# Subnet
subnet = TerraformResource("aws_subnet", "public", {
    "vpc_id": "${aws_vpc.main.id}",
    "cidr_block": "10.0.1.0/24"
})
resources.append(subnet)

# Security Group
sg = TerraformResource("aws_security_group", "web", {
    "vpc_id": "${aws_vpc.main.id}",
    "ingress": [{"from_port": 80, "to_port": 80}]
})
resources.append(sg)

print("Planning infrastructure:")
for resource in resources:
    print(f"  + {resource.id}")

# Example 3: State Management
print("\\n" + "="*70)
print("Example 3: Terraform State Concept")
print("="*70)

class TerraformState:
    def __init__(self):
        self.resources = {}

    def add(self, resource):
        self.resources[resource.id] = resource
        print(f"State: Added {resource.id}")

    def list_resources(self):
        print("Current state:")
        for res_id in self.resources:
            print(f"  - {res_id}")

state = TerraformState()
state.add(instance)
state.add(vpc)
state.list_resources()

# Example 4: Variables
print("\\n" + "="*70)
print("Example 4: Using Variables")
print("="*70)

variables = {
    "region": "us-east-1",
    "instance_type": "t2.micro",
    "environment": "production"
}

print("Variables:")
for key, value in variables.items():
    print(f"  {key} = {value}")

# Example 5: Outputs
print("\\n" + "="*70)
print("Example 5: Output Values")
print("="*70)

outputs = {
    "instance_ip": "54.123.45.67",
    "vpc_id": "vpc-12345",
    "subnet_id": "subnet-67890"
}

print("Outputs:")
for key, value in outputs.items():
    print(f"  {key} = {value}")

# Example 6: Modules Concept
print("\\n" + "="*70)
print("Example 6: Simulated Module")
print("="*70)

class TerraformModule:
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.resources = []

    def add_resource(self, resource):
        self.resources.append(resource)

    def show(self):
        print(f"Module: {self.name}")
        print(f"  Source: {self.source}")
        print(f"  Resources: {len(self.resources)}")

web_module = TerraformModule("web_infrastructure", "./modules/web")
web_module.add_resource(instance)
web_module.add_resource(vpc)
web_module.show()

# Example 7: Dependency Graph
print("\\n" + "="*70)
print("Example 7: Resource Dependencies")
print("="*70)

dependencies = {
    "aws_instance.web": ["aws_subnet.public", "aws_security_group.web"],
    "aws_subnet.public": ["aws_vpc.main"],
    "aws_security_group.web": ["aws_vpc.main"]
}

print("Resource dependencies:")
for resource, deps in dependencies.items():
    print(f"{resource}:")
    for dep in deps:
        print(f"  depends on: {dep}")

print("\\n" + "="*70)
print("Terraform Basics Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Infrastructure as Code (IaC)")
print("  - Declarative configuration")
print("  - State management is critical")
print("  - Resources have dependencies")
print("  - Modules enable reuse")
print("  - Plan before apply")
'''

# Save all changes
for lesson in [lesson36, lesson37, lesson38, lesson39, lesson40]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 36-40:")
print(f"  36: Nested Loops - {len(lesson36['fullSolution'])} chars")
print(f"  37: Nested Loops Fundamentals - {len(lesson37['fullSolution'])} chars")
print(f"  38: String Formatting - {len(lesson38['fullSolution'])} chars")
print(f"  39: f-strings - {len(lesson39['fullSolution'])} chars")
print(f"  40: Terraform - {len(lesson40['fullSolution'])} chars")
print("\\nBatch 36-40 complete!")
