#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 41: Terraform - Modules and Reusability
lesson41 = next(l for l in lessons if l['id'] == 41)
lesson41['fullSolution'] = '''"""
Terraform - Modules and Reusability

Master Terraform module patterns for reusable infrastructure.
Simulated examples showing modular infrastructure design.

**Zero Package Installation Required**
"""

# Example 1: Basic Module Concept
print("="*70)
print("Example 1: Simple Module")
print("="*70)

class TerraformModule:
    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.variables = {}
        self.outputs = {}
        self.resources = []

    def set_variable(self, key, value):
        self.variables[key] = value

    def add_resource(self, resource):
        self.resources.append(resource)

    def show(self):
        print(f"Module: {self.name}")
        print(f"  Source: {self.source}")
        print(f"  Variables: {len(self.variables)}")
        print(f"  Resources: {len(self.resources)}")

vpc_module = TerraformModule("network", "./modules/vpc")
vpc_module.set_variable("cidr_block", "10.0.0.0/16")
vpc_module.set_variable("region", "us-east-1")
vpc_module.show()

# Example 2: Module with Inputs
print("\\n" + "="*70)
print("Example 2: Module Variables")
print("="*70)

web_module = TerraformModule("web_server", "terraform-aws-modules/ec2")

# Input variables
inputs = {
    "instance_type": "t2.micro",
    "ami": "ami-12345678",
    "subnet_id": "${module.network.subnet_id}",
    "key_name": "my-key"
}

for key, value in inputs.items():
    web_module.set_variable(key, value)

print("Module inputs:")
for key, value in web_module.variables.items():
    print(f"  {key} = {value}")

# Example 3: Module Outputs
print("\\n" + "="*70)
print("Example 3: Module Outputs")
print("="*70)

class ModuleOutput:
    def __init__(self, name, value, description=""):
        self.name = name
        self.value = value
        self.description = description

vpc_module.outputs["vpc_id"] = ModuleOutput(
    "vpc_id",
    "vpc-12345",
    "ID of the VPC"
)
vpc_module.outputs["subnet_ids"] = ModuleOutput(
    "subnet_ids",
    ["subnet-1", "subnet-2"],
    "List of subnet IDs"
)

print("Module outputs:")
for name, output in vpc_module.outputs.items():
    print(f"  {name}:")
    print(f"    value: {output.value}")
    print(f"    description: {output.description}")

# Example 4: Nested Modules
print("\\n" + "="*70)
print("Example 4: Module Composition")
print("="*70)

class Infrastructure:
    def __init__(self):
        self.modules = {}

    def add_module(self, module):
        self.modules[module.name] = module

    def plan(self):
        print("Infrastructure plan:")
        for name, module in self.modules.items():
            print(f"  module.{name}:")
            print(f"    source: {module.source}")

infra = Infrastructure()
infra.add_module(vpc_module)
infra.add_module(web_module)
infra.plan()

# Example 5: Module Versioning
print("\\n" + "="*70)
print("Example 5: Module Versions")
print("="*70)

class VersionedModule(TerraformModule):
    def __init__(self, name, source, version):
        super().__init__(name, source)
        self.version = version

    def show(self):
        print(f"Module: {self.name}")
        print(f"  Source: {self.source}")
        print(f"  Version: {self.version}")

rds_module = VersionedModule(
    "database",
    "terraform-aws-modules/rds",
    "5.1.0"
)
rds_module.show()

# Example 6: Reusable Web Server Module
print("\\n" + "="*70)
print("Example 6: Reuse Module Multiple Times")
print("="*70)

def create_web_server(name, instance_type):
    module = TerraformModule(f"web_{name}", "./modules/web")
    module.set_variable("name", name)
    module.set_variable("instance_type", instance_type)
    return module

web_prod = create_web_server("production", "t3.large")
web_staging = create_web_server("staging", "t3.small")

print("Production:")
web_prod.show()
print("\\nStaging:")
web_staging.show()

# Example 7: Module Registry
print("\\n" + "="*70)
print("Example 7: Public Module Registry")
print("="*70)

registry_modules = [
    {"name": "vpc", "source": "terraform-aws-modules/vpc/aws", "version": "3.14.0"},
    {"name": "ec2", "source": "terraform-aws-modules/ec2-instance/aws", "version": "4.0.0"},
    {"name": "rds", "source": "terraform-aws-modules/rds/aws", "version": "5.1.0"}
]

print("Available registry modules:")
for mod in registry_modules:
    print(f"  {mod['name']}: {mod['source']} (v{mod['version']})")

# Example 8: Local vs Remote Modules
print("\\n" + "="*70)
print("Example 8: Module Sources")
print("="*70)

modules = {
    "local": "./modules/custom",
    "git": "git::https://github.com/org/terraform-modules.git//vpc",
    "registry": "terraform-aws-modules/vpc/aws",
    "s3": "s3::https://s3.amazonaws.com/bucket/modules.zip"
}

print("Module source types:")
for source_type, path in modules.items():
    print(f"  {source_type}: {path}")

print("\\n" + "="*70)
print("Terraform Modules Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Modules enable code reuse")
print("  - Define inputs with variables")
print("  - Expose outputs for other modules")
print("  - Version modules for stability")
print("  - Use registry for common patterns")
print("  - Compose modules to build infrastructure")
'''

# Lesson 42: Terraform - State Management
lesson42 = next(l for l in lessons if l['id'] == 42)
lesson42['fullSolution'] = '''"""
Terraform - State Management

Master Terraform state concepts and management.
Understand how Terraform tracks infrastructure.

**Zero Package Installation Required**
"""

# Example 1: State File Concept
print("="*70)
print("Example 1: Terraform State Basics")
print("="*70)

class TerraformState:
    def __init__(self):
        self.version = 4
        self.terraform_version = "1.0.0"
        self.resources = []

    def add_resource(self, resource_type, name, attributes):
        resource = {
            "type": resource_type,
            "name": name,
            "attributes": attributes,
            "id": f"{resource_type}.{name}"
        }
        self.resources.append(resource)
        print(f"Added to state: {resource['id']}")

    def list_resources(self):
        print("Current state resources:")
        for res in self.resources:
            print(f"  {res['id']}")

state = TerraformState()
state.add_resource("aws_vpc", "main", {"cidr_block": "10.0.0.0/16"})
state.add_resource("aws_subnet", "public", {"cidr_block": "10.0.1.0/24"})
state.list_resources()

# Example 2: Remote State
print("\\n" + "="*70)
print("Example 2: Remote State Backend")
print("="*70)

class RemoteBackend:
    def __init__(self, backend_type, config):
        self.type = backend_type
        self.config = config

    def configure(self):
        print(f"Backend: {self.type}")
        for key, value in self.config.items():
            print(f"  {key} = {value}")

s3_backend = RemoteBackend("s3", {
    "bucket": "my-terraform-state",
    "key": "prod/terraform.tfstate",
    "region": "us-east-1",
    "encrypt": True
})

s3_backend.configure()

# Example 3: State Locking
print("\\n" + "="*70)
print("Example 3: State Lock Mechanism")
print("="*70)

class StateLock:
    def __init__(self):
        self.locked = False
        self.lock_id = None
        self.locked_by = None

    def acquire(self, user):
        if self.locked:
            print(f"State locked by {self.locked_by}")
            return False
        else:
            self.locked = True
            self.locked_by = user
            self.lock_id = "lock-12345"
            print(f"Lock acquired by {user}")
            return True

    def release(self):
        if self.locked:
            print(f"Lock released by {self.locked_by}")
            self.locked = False
            self.locked_by = None

lock = StateLock()
lock.acquire("user1")
lock.acquire("user2")  # Will fail
lock.release()
lock.acquire("user2")  # Now succeeds

# Example 4: State Operations
print("\\n" + "="*70)
print("Example 4: Common State Commands")
print("="*70)

class StateManager:
    def __init__(self, state):
        self.state = state

    def show(self):
        print("terraform state list:")
        self.state.list_resources()

    def pull(self):
        print("Pulling remote state...")
        print("State downloaded successfully")

    def push(self):
        print("Pushing local state to remote...")
        print("State uploaded successfully")

manager = StateManager(state)
manager.show()
manager.pull()
manager.push()

# Example 5: Resource Drift Detection
print("\\n" + "="*70)
print("Example 5: Detect Configuration Drift")
print("="*70)

class DriftDetector:
    def __init__(self, state, actual):
        self.state = state
        self.actual = actual

    def check_drift(self):
        print("Checking for drift...")
        if self.state != self.actual:
            print("  DRIFT DETECTED!")
            print(f"  State: {self.state}")
            print(f"  Actual: {self.actual}")
        else:
            print("  No drift detected")

detector = DriftDetector(
    {"instance_type": "t2.micro"},
    {"instance_type": "t2.small"}
)
detector.check_drift()

# Example 6: State File Structure
print("\\n" + "="*70)
print("Example 6: State File Contents")
print("="*70)

state_example = {
    "version": 4,
    "terraform_version": "1.0.0",
    "serial": 5,
    "lineage": "abc-123",
    "resources": [
        {
            "type": "aws_instance",
            "name": "web",
            "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
            "instances": [
                {
                    "attributes": {
                        "id": "i-12345",
                        "instance_type": "t2.micro"
                    }
                }
            ]
        }
    ]
}

print("State structure:")
print(f"  Version: {state_example['version']}")
print(f"  Terraform: {state_example['terraform_version']}")
print(f"  Resources: {len(state_example['resources'])}")

# Example 7: State Backup
print("\\n" + "="*70)
print("Example 7: State Backup & Restore")
print("="*70)

class StateBackup:
    def __init__(self):
        self.backups = []

    def create(self, state):
        backup = {
            "timestamp": "2024-03-15T10:30:00Z",
            "state": state
        }
        self.backups.append(backup)
        print(f"Backup created at {backup['timestamp']}")

    def list_backups(self):
        print("Available backups:")
        for i, backup in enumerate(self.backups):
            print(f"  {i+1}. {backup['timestamp']}")

backup_manager = StateBackup()
backup_manager.create(state)
backup_manager.list_backups()

# Example 8: State Migration
print("\\n" + "="*70)
print("Example 8: Migrate State Between Backends")
print("="*70)

def migrate_state(source, destination):
    print(f"Migrating state:")
    print(f"  From: {source.type}")
    print(f"  To: {destination.type}")
    print("Migration steps:")
    print("  1. Pull state from source")
    print("  2. Push state to destination")
    print("  3. Update backend configuration")
    print("Migration complete!")

local_backend = RemoteBackend("local", {"path": "terraform.tfstate"})
migrate_state(local_backend, s3_backend)

print("\\n" + "="*70)
print("Terraform State Management Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - State tracks infrastructure")
print("  - Use remote backends for teams")
print("  - State locking prevents conflicts")
print("  - Regular backups are critical")
print("  - Detect drift with plan")
print("  - Never manually edit state")
'''

# Lesson 43: While Loops
lesson43 = next(l for l in lessons if l['id'] == 43)
lesson43['fullSolution'] = '''"""
While Loops - Condition-Based Iteration

Master while loops for condition-based repetition.
Essential for unknown iteration counts and event-driven loops.

**Zero Package Installation Required**
"""

# Example 1: Basic While Loop
print("="*70)
print("Example 1: Count to 5")
print("="*70)

count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1

# Example 2: User Input Simulation
print("\\n" + "="*70)
print("Example 2: Loop Until Condition")
print("="*70)

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts += 1
    print(f"  Attempt {attempts} of {max_attempts}")

print("Max attempts reached")

# Example 3: Sum Until Threshold
print("\\n" + "="*70)
print("Example 3: Accumulate Until Target")
print("="*70)

total = 0
target = 100
number = 1

while total < target:
    total += number
    print(f"  Added {number}, total: {total}")
    number += 1

print(f"Reached target: {total}")

# Example 4: While with Break
print("\\n" + "="*70)
print("Example 4: Early Exit")
print("="*70)

count = 0
while True:
    count += 1
    print(f"  Iteration {count}")
    if count >= 5:
        print("Breaking out!")
        break

# Example 5: Password Validation Loop
print("\\n" + "="*70)
print("Example 5: Retry Logic")
print("="*70)

passwords = ["wrong1", "wrong2", "correct"]
attempts = 0
correct_password = "correct"
authenticated = False

while attempts < len(passwords) and not authenticated:
    password = passwords[attempts]
    attempts += 1
    print(f"  Attempt {attempts}: {password}")

    if password == correct_password:
        authenticated = True
        print("  Access granted!")
    else:
        print("  Wrong password")

# Example 6: Countdown Timer
print("\\n" + "="*70)
print("Example 6: Countdown")
print("="*70)

countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1

print("  Blast off!")

# Example 7: Process List Items
print("\\n" + "="*70)
print("Example 7: While with Index")
print("="*70)

items = ["apple", "banana", "cherry"]
index = 0

while index < len(items):
    print(f"  Item {index}: {items[index]}")
    index += 1

# Example 8: Double Until Overflow
print("\\n" + "="*70)
print("Example 8: Grow Until Limit")
print("="*70)

value = 1
limit = 1000

while value < limit:
    print(f"  Value: {value}")
    value *= 2

print(f"Final value: {value}")

# Example 9: While with Continue
print("\\n" + "="*70)
print("Example 9: Skip Even Numbers")
print("="*70)

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(f"  Odd: {num}")

# Example 10: Infinite Loop Pattern
print("\\n" + "="*70)
print("Example 10: Event Loop Pattern")
print("="*70)

events = ["start", "process", "process", "stop"]
index = 0

while True:
    event = events[index]
    print(f"  Event: {event}")

    if event == "stop":
        print("Stopping event loop")
        break

    index += 1

print("\\n" + "="*70)
print("While Loops Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - while condition: runs while True")
print("  - Check condition before each iteration")
print("  - Must update condition inside loop")
print("  - Use for unknown iteration count")
print("  - while True: needs break")
'''

# Lesson 44: asyncio.wait_for timeout
lesson44 = next(l for l in lessons if l['id'] == 44)
lesson44['fullSolution'] = '''"""
asyncio.wait_for Timeout - Async Time Limits

Master setting timeouts for async operations.
Essential for preventing hanging operations.

**Zero Package Installation Required**
"""

import asyncio
import time

# Example 1: Basic Timeout
print("="*70)
print("Example 1: Simple Timeout")
print("="*70)

async def slow_task():
    print("  Starting slow task...")
    await asyncio.sleep(5)
    print("  Task completed!")
    return "Done"

async def example1():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Task timed out after 2 seconds!")

asyncio.run(example1())

# Example 2: Fast vs Slow
print("\\n" + "="*70)
print("Example 2: Task Within Timeout")
print("="*70)

async def fast_task():
    print("  Starting fast task...")
    await asyncio.sleep(0.5)
    return "Quick result"

async def example2():
    try:
        result = await asyncio.wait_for(fast_task(), timeout=2.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Timed out")

asyncio.run(example2())

# Example 3: API Request Simulation
print("\\n" + "="*70)
print("Example 3: Simulated API Call")
print("="*70)

async def fetch_data(delay):
    print(f"  Fetching data (will take {delay}s)...")
    await asyncio.sleep(delay)
    return {"status": "success", "data": [1, 2, 3]}

async def example3():
    try:
        data = await asyncio.wait_for(fetch_data(1.0), timeout=2.0)
        print(f"  Data: {data}")
    except asyncio.TimeoutError:
        print("  Request timed out!")

asyncio.run(example3())

# Example 4: Multiple Timeouts
print("\\n" + "="*70)
print("Example 4: Different Timeout Values")
print("="*70)

async def operation(name, duration):
    print(f"  {name} starting...")
    await asyncio.sleep(duration)
    return f"{name} done"

async def example4():
    operations = [
        ("Fast", 0.5, 1.0),
        ("Medium", 1.5, 2.0),
        ("Slow", 3.0, 2.0)
    ]

    for name, duration, timeout in operations:
        try:
            result = await asyncio.wait_for(
                operation(name, duration),
                timeout=timeout
            )
            print(f"  {result}")
        except asyncio.TimeoutError:
            print(f"  {name} timed out!")

asyncio.run(example4())

# Example 5: Cleanup on Timeout
print("\\n" + "="*70)
print("Example 5: Handle Timeout Gracefully")
print("="*70)

async def database_query():
    print("  Querying database...")
    await asyncio.sleep(3)
    return "Query results"

async def example5():
    try:
        result = await asyncio.wait_for(
            database_query(),
            timeout=1.0
        )
        print(f"  Got: {result}")
    except asyncio.TimeoutError:
        print("  Database timeout - using cached data")
        result = "Cached data"
        print(f"  Using: {result}")

asyncio.run(example5())

# Example 6: Retry with Timeout
print("\\n" + "="*70)
print("Example 6: Retry Logic")
print("="*70)

async def unreliable_service():
    await asyncio.sleep(0.5)
    return "Service response"

async def example6():
    max_retries = 3
    timeout = 1.0

    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1}...")
            result = await asyncio.wait_for(
                unreliable_service(),
                timeout=timeout
            )
            print(f"  Success: {result}")
            break
        except asyncio.TimeoutError:
            print(f"  Attempt {attempt + 1} timed out")
            if attempt == max_retries - 1:
                print("  All retries failed")

asyncio.run(example6())

# Example 7: Concurrent with Timeouts
print("\\n" + "="*70)
print("Example 7: Multiple Tasks")
print("="*70)

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"{name} completed"

async def example7():
    tasks = [
        asyncio.wait_for(task("Task1", 0.5), timeout=1.0),
        asyncio.wait_for(task("Task2", 1.5), timeout=1.0),
        asyncio.wait_for(task("Task3", 0.3), timeout=1.0)
    ]

    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i, result in enumerate(results, 1):
        if isinstance(result, asyncio.TimeoutError):
            print(f"  Task{i}: Timed out")
        else:
            print(f"  Task{i}: {result}")

asyncio.run(example7())

print("\\n" + "="*70)
print("asyncio.wait_for Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - await asyncio.wait_for(coro, timeout)")
print("  - Raises TimeoutError if too slow")
print("  - Use try/except to handle timeouts")
print("  - Prevents operations from hanging")
print("  - Essential for network requests")
'''

# Lesson 45: Accessing List Elements
lesson45 = next(l for l in lessons if l['id'] == 45)
lesson45['fullSolution'] = '''"""
Accessing List Elements - Indexing Basics

Master accessing list elements by index position.
Foundation for working with sequences in Python.

**Zero Package Installation Required**
"""

# Example 1: Basic Indexing
print("="*70)
print("Example 1: Access by Index")
print("="*70)

fruits = ["apple", "banana", "cherry", "date"]

print(f"List: {fruits}")
print(f"First item (index 0): {fruits[0]}")
print(f"Second item (index 1): {fruits[1]}")
print(f"Third item (index 2): {fruits[2]}")

# Example 2: Negative Indexing
print("\\n" + "="*70)
print("Example 2: Access from End")
print("="*70)

numbers = [10, 20, 30, 40, 50]

print(f"List: {numbers}")
print(f"Last item (index -1): {numbers[-1]}")
print(f"Second to last (index -2): {numbers[-2]}")
print(f"First item (index -5): {numbers[-5]}")

# Example 3: Access in Loop
print("\\n" + "="*70)
print("Example 3: Loop with Index")
print("="*70)

colors = ["red", "green", "blue"]

for i in range(len(colors)):
    print(f"  Index {i}: {colors[i]}")

# Example 4: First and Last
print("\\n" + "="*70)
print("Example 4: Common Patterns")
print("="*70)

items = ["A", "B", "C", "D", "E"]

first = items[0]
last = items[-1]
middle = items[len(items) // 2]

print(f"First: {first}")
print(f"Last: {last}")
print(f"Middle: {middle}")

# Example 5: Check Before Access
print("\\n" + "="*70)
print("Example 5: Safe Access")
print("="*70)

data = [1, 2, 3]
index = 5

if index < len(data):
    print(f"Item at {index}: {data[index]}")
else:
    print(f"Index {index} out of range (length: {len(data)})")

# Example 6: Get Multiple Items
print("\\n" + "="*70)
print("Example 6: Access Several Elements")
print("="*70)

scores = [85, 92, 78, 95, 88]

top_score = scores[0]
second_score = scores[1]
third_score = scores[2]

print(f"Top 3 scores:")
print(f"  1st: {top_score}")
print(f"  2nd: {second_score}")
print(f"  3rd: {third_score}")

# Example 7: Index with Enumerate
print("\\n" + "="*70)
print("Example 7: Enumerate for Index")
print("="*70)

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
    print(f"  Person {index}: {name}")

# Example 8: Find Index of Value
print("\\n" + "="*70)
print("Example 8: Search for Item")
print("="*70)

values = [5, 10, 15, 20, 25]
target = 15

if target in values:
    index = values.index(target)
    print(f"Found {target} at index {index}")
else:
    print(f"{target} not found")

# Example 9: Access Nested Lists
print("\\n" + "="*70)
print("Example 9: 2D List Access")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"First row: {matrix[0]}")
print(f"First row, first col: {matrix[0][0]}")
print(f"Second row, third col: {matrix[1][2]}")

# Example 10: Common Errors
print("\\n" + "="*70)
print("Example 10: Handle Index Errors")
print("="*70)

items = ["a", "b", "c"]

try:
    value = items[10]
    print(value)
except IndexError:
    print("Error: Index 10 out of range")
    print(f"Valid indices: 0 to {len(items)-1}")

print("\\n" + "="*70)
print("Accessing List Elements Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - list[0] is first element")
print("  - list[-1] is last element")
print("  - Indices start at 0")
print("  - Negative indices count from end")
print("  - IndexError if out of range")
print("  - Check length before accessing")
'''

# Save all changes
for lesson in [lesson41, lesson42, lesson43, lesson44, lesson45]:
    target = next(l for l in lessons if l['id'] == lesson['id'])
    target['fullSolution'] = lesson['fullSolution']

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 41-45:")
print(f"  41: Terraform Modules - {len(lesson41['fullSolution'])} chars")
print(f"  42: Terraform State - {len(lesson42['fullSolution'])} chars")
print(f"  43: While Loops - {len(lesson43['fullSolution'])} chars")
print(f"  44: asyncio.wait_for - {len(lesson44['fullSolution'])} chars")
print(f"  45: Accessing List Elements - {len(lesson45['fullSolution'])} chars")
print("\\nBatch 41-45 complete!")
