#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 16: Reading Files
lesson16 = next(l for l in lessons if l['id'] == 16)
lesson16['fullSolution'] = '''"""
Reading Files - The Basics

Master file reading operations in Python.
Essential for data processing, configuration, and file manipulation.

**Zero Package Installation Required**
"""

import io

# Example 1: Read Entire File
print("="*70)
print("Example 1: Read Complete File")
print("="*70)

# Simulate a file using StringIO
file_content = """Line 1: Hello
Line 2: World
Line 3: Python"""

file_obj = io.StringIO(file_content)
content = file_obj.read()

print("File contents:")
print(content)

# Example 2: Read Line by Line
print("\\n" + "="*70)
print("Example 2: Read Each Line")
print("="*70)

file_obj = io.StringIO(file_content)

print("Reading line by line:")
for line in file_obj:
    print(f"  {line.strip()}")

# Example 3: Read into List
print("\\n" + "="*70)
print("Example 3: All Lines as List")
print("="*70)

file_obj = io.StringIO(file_content)
lines = file_obj.readlines()

print(f"Total lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  Line {i}: {line.strip()}")

# Example 4: Process Configuration File
print("\\n" + "="*70)
print("Example 4: Read Configuration")
print("="*70)

config_content = """host=localhost
port=8080
debug=true
timeout=30"""

file_obj = io.StringIO(config_content)
config = {}

for line in file_obj:
    line = line.strip()
    if '=' in line:
        key, value = line.split('=')
        config[key] = value

print("Configuration loaded:")
for key, value in config.items():
    print(f"  {key}: {value}")

# Example 5: Count Lines and Words
print("\\n" + "="*70)
print("Example 5: File Statistics")
print("="*70)

text_content = """Python is awesome.
It is easy to learn.
Great for beginners."""

file_obj = io.StringIO(text_content)

line_count = 0
word_count = 0

for line in file_obj:
    line_count += 1
    word_count += len(line.split())

print(f"Lines: {line_count}")
print(f"Words: {word_count}")

# Example 6: Find Specific Content
print("\\n" + "="*70)
print("Example 6: Search for Pattern")
print("="*70)

log_content = """INFO: Server started
ERROR: Connection failed
INFO: Request received
ERROR: Timeout occurred
INFO: Response sent"""

file_obj = io.StringIO(log_content)

print("Error messages:")
for line in file_obj:
    if 'ERROR' in line:
        print(f"  {line.strip()}")

# Example 7: Skip Empty Lines
print("\\n" + "="*70)
print("Example 7: Ignore Empty Lines")
print("="*70)

sparse_content = """Line 1

Line 2

Line 3"""

file_obj = io.StringIO(sparse_content)

print("Non-empty lines:")
for line in file_obj:
    line = line.strip()
    if line:
        print(f"  {line}")

print("\\n" + "="*70)
print("Reading Files Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Use open() to open files")
print("  - .read() reads entire file")
print("  - .readlines() returns list")
print("  - Iterate with for line in file")
print("  - Use 'with' for automatic closing")
'''

# Lesson 17: Reading JSON Files
lesson17 = next(l for l in lessons if l['id'] == 17)
lesson17['fullSolution'] = '''"""
Reading JSON Files - Structured Data

Master JSON parsing and data extraction in Python.
Essential for APIs, configuration files, and data exchange.

**Zero Package Installation Required**
"""

import json

# Example 1: Basic JSON Parsing
print("="*70)
print("Example 1: Parse JSON String")
print("="*70)

json_string = '{"name": "Alice", "age": 25, "city": "NYC"}'

data = json.loads(json_string)

print(f"Parsed data: {data}")
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"City: {data['city']}")

# Example 2: JSON Array
print("\\n" + "="*70)
print("Example 2: Parse JSON Array")
print("="*70)

json_array = '[1, 2, 3, 4, 5]'

numbers = json.loads(json_array)

print(f"Numbers: {numbers}")
print(f"First: {numbers[0]}")
print(f"Last: {numbers[-1]}")
print(f"Sum: {sum(numbers)}")

# Example 3: List of Objects
print("\\n" + "="*70)
print("Example 3: JSON Array of Objects")
print("="*70)

users_json = '[{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]'

users = json.loads(users_json)

print("Users:")
for user in users:
    print(f"  {user['name']}: {user['score']}")

# Example 4: Convert Python to JSON
print("\\n" + "="*70)
print("Example 4: Python to JSON String")
print("="*70)

person = {
    "name": "David",
    "age": 30,
    "skills": ["Python", "JavaScript", "SQL"]
}

json_output = json.dumps(person)
print("JSON string:")
print(json_output)

# Pretty print
json_pretty = json.dumps(person, indent=2)
print("\\nPretty JSON:")
print(json_pretty)

# Example 5: Error Handling
print("\\n" + "="*70)
print("Example 5: Handle Invalid JSON")
print("="*70)

invalid_json = '{"name": "Alice", "age": }'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    data = {"name": "Unknown", "age": 0}

print(f"Name: {data['name']}")

print("\\n" + "="*70)
print("Reading JSON Files Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - json.loads() parses JSON strings")
print("  - json.dumps() converts to JSON")
print("  - Access data like dictionaries")
print("  - Handle JSONDecodeError for safety")
print("  - Use indent for pretty printing")
'''

# Lesson 18: Reading Text Files
lesson18 = next(l for l in lessons if l['id'] == 18)
lesson18['fullSolution'] = '''"""
Reading Text Files - String Processing

Master text file reading and string manipulation in Python.
Essential for log processing, data analysis, and text parsing.

**Zero Package Installation Required**
"""

import io

# Example 1: Read as Single String
print("="*70)
print("Example 1: Read Complete Text")
print("="*70)

text_content = """Python is a powerful language.
It is used for web development.
Also great for data science."""

file_obj = io.StringIO(text_content)
content = file_obj.read()

print("File contents:")
print(content)
print(f"\\nTotal characters: {len(content)}")

# Example 2: Process Line by Line
print("\\n" + "="*70)
print("Example 2: Line-by-Line Processing")
print("="*70)

file_obj = io.StringIO(text_content)

line_num = 1
for line in file_obj:
    print(f"Line {line_num}: {line.strip()}")
    line_num += 1

# Example 3: Count Occurrences
print("\\n" + "="*70)
print("Example 3: Count Word Occurrences")
print("="*70)

file_obj = io.StringIO(text_content)
content = file_obj.read()

word_to_find = "is"
count = content.lower().count(word_to_find.lower())

print(f"The word '{word_to_find}' appears {count} times")

# Example 4: Extract Lines with Keyword
print("\\n" + "="*70)
print("Example 4: Filter Lines")
print("="*70)

log_content = """2024-01-01 INFO Server started
2024-01-01 ERROR Database connection failed
2024-01-01 INFO Request processed
2024-01-01 ERROR Timeout occurred"""

file_obj = io.StringIO(log_content)

print("Error lines only:")
for line in file_obj:
    if "ERROR" in line:
        print(f"  {line.strip()}")

# Example 5: Word Statistics
print("\\n" + "="*70)
print("Example 5: Text Analysis")
print("="*70)

file_obj = io.StringIO(text_content)
content = file_obj.read()

words = content.split()
unique_words = set(word.lower().strip('.,!?') for word in words)

print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")

print("\\n" + "="*70)
print("Reading Text Files Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - .read() for entire content")
print("  - Iterate for line-by-line")
print("  - .strip() removes whitespace")
print("  - .split() breaks into words")
print("  - .count() finds occurrences")
'''

# Lesson 19: Threading + Lock
lesson19 = next(l for l in lessons if l['id'] == 19)
lesson19['fullSolution'] = '''"""
Threading + Lock - Concurrent Programming

Master thread synchronization and race condition prevention.
Essential for concurrent programming and shared resource access.

**Zero Package Installation Required**
"""

import threading
import time

# Example 1: Basic Thread Creation
print("="*70)
print("Example 1: Simple Threading")
print("="*70)

def worker(name):
    print(f"  Thread {name} starting")
    time.sleep(0.1)
    print(f"  Thread {name} finished")

print("Creating threads:")
thread1 = threading.Thread(target=worker, args=("A",))
thread2 = threading.Thread(target=worker, args=("B",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("All threads completed")

# Example 2: Race Condition Problem
print("\\n" + "="*70)
print("Example 2: Race Condition Without Lock")
print("="*70)

counter = 0

def increment_unsafe():
    global counter
    for _ in range(100):
        temp = counter
        temp += 1
        counter = temp

print(f"Initial counter: {counter}")

threads = []
for i in range(5):
    t = threading.Thread(target=increment_unsafe)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter (expected 500): {counter}")
print("May be wrong due to race condition!")

# Example 3: Using Lock
print("\\n" + "="*70)
print("Example 3: Protected with Lock")
print("="*70)

counter = 0
lock = threading.Lock()

def increment_safe():
    global counter
    for _ in range(100):
        with lock:
            temp = counter
            temp += 1
            counter = temp

print(f"Initial counter: {counter}")

threads = []
for i in range(5):
    t = threading.Thread(target=increment_safe)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final counter (expected 500): {counter}")
print("Correct! Lock prevented race condition")

# Example 4: Bank Account Example
print("\\n" + "="*70)
print("Example 4: Thread-Safe Bank Account")
print("="*70)

balance = 1000
balance_lock = threading.Lock()

def deposit(amount):
    global balance
    with balance_lock:
        current = balance
        time.sleep(0.001)
        balance = current + amount
        print(f"  Deposited ${amount}, balance: ${balance}")

print(f"Starting balance: ${balance}")

threads = [
    threading.Thread(target=deposit, args=(100,)),
    threading.Thread(target=deposit, args=(200,))
]

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Final balance: ${balance}")

print("\\n" + "="*70)
print("Threading + Lock Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - Threads run concurrently")
print("  - Lock prevents race conditions")
print("  - Use 'with lock:' for safety")
print("  - Lock automatically released")
print("  - Protects shared resources")
'''

# Lesson 20: AWS SNS
lesson20 = next(l for l in lessons if l['id'] == 20)
lesson20['fullSolution'] = '''"""
AWS SNS - Notification Service

Master AWS Simple Notification Service patterns.
Simulated examples showing pub/sub messaging without AWS account.

**Zero Package Installation Required**
"""

# Example 1: Simulated Topic
print("="*70)
print("Example 1: Create Notification Topic")
print("="*70)

class SimulatedSNSTopic:
    def __init__(self, name):
        self.name = name
        self.arn = f"arn:aws:sns:us-east-1:123456789:{name}"
        self.subscriptions = []

topic = SimulatedSNSTopic("OrderNotifications")
print(f"Created topic: {topic.name}")
print(f"ARN: {topic.arn}")

# Example 2: Subscribe to Topic
print("\\n" + "="*70)
print("Example 2: Add Subscriptions")
print("="*70)

class Subscription:
    def __init__(self, protocol, endpoint):
        self.protocol = protocol
        self.endpoint = endpoint

topic.subscriptions.append(Subscription("email", "admin@example.com"))
topic.subscriptions.append(Subscription("sms", "+1-555-0100"))

print(f"Subscriptions for {topic.name}:")
for sub in topic.subscriptions:
    print(f"  {sub.protocol}: {sub.endpoint}")

# Example 3: Publish Message
print("\\n" + "="*70)
print("Example 3: Send Notification")
print("="*70)

def publish_message(topic, subject, message):
    print(f"Publishing to {topic.name}:")
    print(f"  Subject: {subject}")
    print(f"  Message: {message}")
    print(f"\\nDelivering to {len(topic.subscriptions)} subscribers:")

    for sub in topic.subscriptions:
        print(f"  -> Sent via {sub.protocol} to {sub.endpoint}")

    return {"MessageId": "msg-12345", "Status": "Success"}

result = publish_message(
    topic,
    "New Order Received",
    "Order #12345 has been placed"
)

print(f"\\nResult: {result}")

# Example 4: Fan-Out Pattern
print("\\n" + "="*70)
print("Example 4: Fan-Out to Multiple Services")
print("="*70)

fanout_topic = SimulatedSNSTopic("OrderProcessing")

services = [
    "InventoryService",
    "ShippingService",
    "BillingService"
]

for service in services:
    fanout_topic.subscriptions.append(
        Subscription("https", f"https://{service.lower()}.example.com")
    )

print(f"Fan-out topic: {fanout_topic.name}")
print(f"Subscribers: {len(fanout_topic.subscriptions)}")

print("\\n" + "="*70)
print("AWS SNS Complete!")
print("="*70)

print("\\nKey Takeaways:")
print("  - SNS enables pub/sub messaging")
print("  - Topics distribute to subscribers")
print("  - Supports email, SMS, HTTPS")
print("  - Fan-out to multiple services")
print("  - Decouples publishers/subscribers")
'''

# Save all changes
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, ensure_ascii=False, indent=2)

print("Upgraded lessons 16-20:")
print(f"  16: Reading Files - {len(lesson16['fullSolution'])} chars")
print(f"  17: Reading JSON Files - {len(lesson17['fullSolution'])} chars")
print(f"  18: Reading Text Files - {len(lesson18['fullSolution'])} chars")
print(f"  19: Threading + Lock - {len(lesson19['fullSolution'])} chars")
print(f"  20: AWS SNS - {len(lesson20['fullSolution'])} chars")
print("\\nBatch 16-20 complete!")
