#!/usr/bin/env python3
"""
Upgrade Python lessons 151-160 with comprehensive content.
- Lesson 151: Writing Text Files
- Lesson 152: Dead Letter Queues - Error Handling
- Lesson 153: IndexError Handling
- Lesson 154: KeyError Handling
- Lesson 155: Raise Exceptions
- Lesson 156: Raising Exceptions
- Lesson 157: Try-Except Basics
- Lesson 158: Try/Except
- Lesson 159: TypeError Handling
- Lesson 160: ValueError Handling
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 151-160
lesson151 = next(l for l in lessons if l['id'] == 151)
lesson152 = next(l for l in lessons if l['id'] == 152)
lesson153 = next(l for l in lessons if l['id'] == 153)
lesson154 = next(l for l in lessons if l['id'] == 154)
lesson155 = next(l for l in lessons if l['id'] == 155)
lesson156 = next(l for l in lessons if l['id'] == 156)
lesson157 = next(l for l in lessons if l['id'] == 157)
lesson158 = next(l for l in lessons if l['id'] == 158)
lesson159 = next(l for l in lessons if l['id'] == 159)
lesson160 = next(l for l in lessons if l['id'] == 160)

# Upgrade Lesson 151: Writing Text Files
lesson151['fullSolution'] = '''"""
Writing Text Files

Master file writing operations in Python. Learn to create files, write text,
append content, handle write modes, manage file buffering, and implement
safe file writing practices. Essential for data persistence and logging.

**Zero Package Installation Required**
"""

# Example 1: Basic File Writing
print("="*70)
print("Example 1: Writing to a Text File")
print("="*70)

# Write to a file
with open('example1.txt', 'w') as f:
    f.write('Hello, World!\\n')
    f.write('This is a test file.\\n')
    f.write('Python file I/O is easy!\\n')

# Read back to verify
with open('example1.txt', 'r') as f:
    content = f.read()

print("File content:")
print(content)
print()

# Example 2: Write Mode vs Append Mode
print("="*70)
print("Example 2: Write Mode ('w') vs Append Mode ('a')")
print("="*70)

# Write mode - overwrites existing content
with open('example2.txt', 'w') as f:
    f.write('First write\\n')

with open('example2.txt', 'w') as f:
    f.write('Second write (overwrites first)\\n')

print("After write mode:")
with open('example2.txt', 'r') as f:
    print(f.read())

# Append mode - adds to existing content
with open('example2.txt', 'a') as f:
    f.write('Third write (appended)\\n')
    f.write('Fourth write (also appended)\\n')

print("After append mode:")
with open('example2.txt', 'r') as f:
    print(f.read())
print()

# Example 3: Writing Multiple Lines at Once
print("="*70)
print("Example 3: Writing Multiple Lines with writelines()")
print("="*70)

lines = [
    'Line 1: Introduction\\n',
    'Line 2: Body paragraph\\n',
    'Line 3: Conclusion\\n'
]

# Write all lines at once
with open('example3.txt', 'w') as f:
    f.writelines(lines)

print("Wrote 3 lines to file:")
with open('example3.txt', 'r') as f:
    print(f.read())
print()

# Example 4: Writing Formatted Text
print("="*70)
print("Example 4: Writing Formatted Data")
print("="*70)

# Prepare data
students = [
    {'name': 'Alice', 'grade': 95},
    {'name': 'Bob', 'grade': 87},
    {'name': 'Charlie', 'grade': 92}
]

# Write formatted report
with open('example4.txt', 'w') as f:
    f.write('STUDENT GRADE REPORT\\n')
    f.write('=' * 40 + '\\n')
    for student in students:
        f.write(f"{student['name']:15} {student['grade']:>3}\\n")
    f.write('=' * 40 + '\\n')

print("Student report written:")
with open('example4.txt', 'r') as f:
    print(f.read())
print()

# Example 5: Writing with Print Function
print("="*70)
print("Example 5: Using print() to Write to Files")
print("="*70)

with open('example5.txt', 'w') as f:
    print('Using print function', file=f)
    print('No need for \\\\n', file=f)
    print('Print adds newlines automatically', file=f)
    print(f'Can use f-strings: {2 + 2}', file=f)

print("Content written with print():")
with open('example5.txt', 'r') as f:
    print(f.read())
print()

# Example 6: Writing Binary Data
print("="*70)
print("Example 6: Writing Binary Data")
print("="*70)

# Write binary data
binary_data = bytes([72, 101, 108, 108, 111])  # "Hello" in ASCII

with open('example6.bin', 'wb') as f:
    f.write(binary_data)

# Read back as binary
with open('example6.bin', 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")
    print(f"Decoded: {data.decode('ascii')}")
print()

# Example 7: Safe File Writing with Error Handling
print("="*70)
print("Example 7: Safe File Writing with Exception Handling")
print("="*70)

def safe_write_file(filename, content):
    """Safely write to a file with error handling"""
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully wrote to {filename}")
        return True
    except PermissionError:
        print(f"Error: Permission denied for {filename}")
        return False
    except OSError as e:
        print(f"Error writing file: {e}")
        return False

# Test safe writing
safe_write_file('example7.txt', 'Safe write test\\n')

# Try to write to invalid location
safe_write_file('/root/invalid.txt', 'This will fail\\n')
print()

# Example 8: Writing Log Files
print("="*70)
print("Example 8: Creating a Simple Log File")
print("="*70)

import datetime

def log_message(message, log_file='example8.log'):
    """Append a timestamped message to log file"""
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\\n")

# Write some log entries
log_message('Application started')
log_message('User logged in: alice')
log_message('Processing data...')
log_message('Task completed successfully')
log_message('Application shutdown')

print("Log file content:")
with open('example8.log', 'r') as f:
    print(f.read())
print()

# Example 9: Buffering Control
print("="*70)
print("Example 9: File Buffering")
print("="*70)

# Unbuffered writing (buffering=0 only works in binary mode)
print("Writing with flush for immediate disk write:")
with open('example9.txt', 'w') as f:
    f.write('Line 1\\n')
    f.flush()  # Force write to disk
    print("  Line 1 written and flushed")
    f.write('Line 2\\n')
    f.flush()
    print("  Line 2 written and flushed")

with open('example9.txt', 'r') as f:
    print(f"\\nFile content:\\n{f.read()}")
print()

# Example 10: Practical Application - Configuration File Writer
print("="*70)
print("Example 10: Real-World Use Case - Configuration Manager")
print("="*70)

class ConfigManager:
    """Simple configuration file manager"""

    def __init__(self, config_file='config.txt'):
        self.config_file = config_file
        self.config = {}

    def set(self, key, value):
        """Set a configuration value"""
        self.config[key] = str(value)

    def save(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                f.write('# Configuration File\\n')
                f.write(f'# Generated: {datetime.datetime.now()}\\n')
                f.write('\\n')

                for key, value in sorted(self.config.items()):
                    f.write(f'{key}={value}\\n')

            print(f"Configuration saved to {self.config_file}")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def load(self):
        """Load configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            self.config[key] = value
            print(f"Configuration loaded from {self.config_file}")
            return True
        except FileNotFoundError:
            print(f"Config file not found: {self.config_file}")
            return False

    def display(self):
        """Display current configuration"""
        print("\\nCurrent Configuration:")
        print("=" * 40)
        for key, value in sorted(self.config.items()):
            print(f"  {key:20} = {value}")
        print("=" * 40)

# Use the configuration manager
config = ConfigManager('app_config.txt')

# Set configuration values
config.set('app_name', 'MyApplication')
config.set('version', '1.0.0')
config.set('debug_mode', 'False')
config.set('max_connections', '100')
config.set('timeout_seconds', '30')

# Display and save
config.display()
config.save()

# Show file content
print("\\nConfiguration file content:")
with open('app_config.txt', 'r') as f:
    print(f.read())

# Load configuration into new instance
config2 = ConfigManager('app_config.txt')
config2.load()
config2.display()

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. open(file, 'w') - Write mode (overwrites file)")
print("2. open(file, 'a') - Append mode (adds to end)")
print("3. f.write(string) - Write a string to file")
print("4. f.writelines(list) - Write multiple lines at once")
print("5. print(..., file=f) - Use print() to write to file")
print("6. Always use 'with' statement for automatic closing")
print("7. f.flush() - Force write to disk immediately")
print("8. Use 'wb' mode for binary data writing")
print("9. Handle exceptions for safe file operations")
print("10. Add timestamps for log files")
print("="*70)
'''

# Upgrade Lesson 152: Dead Letter Queues - Error Handling
lesson152['fullSolution'] = '''"""
Dead Letter Queues - Error Handling

Master dead letter queue (DLQ) pattern for handling failed message processing.
Learn to implement retry logic, failure isolation, message routing, and error
recovery strategies. Critical for building resilient distributed systems.

**Zero Package Installation Required**
"""

# Example 1: Basic Dead Letter Queue Concept
print("="*70)
print("Example 1: Understanding Dead Letter Queues")
print("="*70)

class SimpleQueue:
    """Simple queue for demonstration"""
    def __init__(self, name):
        self.name = name
        self.messages = []

    def enqueue(self, message):
        self.messages.append(message)
        print(f"  [{self.name}] Enqueued: {message}")

    def dequeue(self):
        if self.messages:
            msg = self.messages.pop(0)
            print(f"  [{self.name}] Dequeued: {msg}")
            return msg
        return None

    def size(self):
        return len(self.messages)

# Create main queue and dead letter queue
main_queue = SimpleQueue("Main")
dlq = SimpleQueue("DLQ")

# Add messages
main_queue.enqueue("Message 1")
main_queue.enqueue("Message 2")
main_queue.enqueue("Message 3")

print(f"\\nMain queue size: {main_queue.size()}")
print(f"DLQ size: {dlq.size()}")
print()

# Example 2: Processing with Failure Routing
print("="*70)
print("Example 2: Route Failed Messages to DLQ")
print("="*70)

def process_message(message):
    """Simulate message processing that might fail"""
    if "error" in message.lower():
        raise ValueError(f"Processing failed for: {message}")
    print(f"  Successfully processed: {message}")

class QueueWithDLQ:
    def __init__(self):
        self.main_queue = []
        self.dlq = []

    def add_message(self, message):
        self.main_queue.append(message)

    def process_all(self):
        """Process all messages, route failures to DLQ"""
        while self.main_queue:
            message = self.main_queue.pop(0)
            try:
                process_message(message)
            except Exception as e:
                print(f"  ERROR: {e}")
                print(f"  Routing to DLQ: {message}")
                self.dlq.append({"message": message, "error": str(e)})

# Test processing
queue = QueueWithDLQ()
queue.add_message("Valid message 1")
queue.add_message("Error message")
queue.add_message("Valid message 2")
queue.add_message("Another error")

print("Processing messages...")
queue.process_all()

print(f"\\nMessages in DLQ: {len(queue.dlq)}")
for item in queue.dlq:
    print(f"  - {item['message']}: {item['error']}")
print()

# Example 3: Retry Logic with DLQ
print("="*70)
print("Example 3: Retry Before Moving to DLQ")
print("="*70)

class RetryableQueue:
    def __init__(self, max_retries=3):
        self.queue = []
        self.dlq = []
        self.max_retries = max_retries

    def add(self, message):
        self.queue.append({"message": message, "attempts": 0})

    def process_with_retry(self):
        """Process with retry logic"""
        processed = []

        while self.queue:
            item = self.queue.pop(0)
            message = item["message"]
            attempts = item["attempts"]

            try:
                # Simulate processing (fails on messages with "flaky")
                if "flaky" in message.lower() and attempts < 2:
                    raise Exception("Temporary failure")

                print(f"  Processed: {message} (attempt {attempts + 1})")
                processed.append(message)

            except Exception as e:
                item["attempts"] += 1

                if item["attempts"] < self.max_retries:
                    print(f"  Retry {item['attempts']}/{self.max_retries}: {message}")
                    self.queue.append(item)
                else:
                    print(f"  Max retries exceeded: {message} -> DLQ")
                    self.dlq.append({
                        "message": message,
                        "error": str(e),
                        "attempts": item["attempts"]
                    })

        return processed

# Test retry logic
retry_queue = RetryableQueue(max_retries=3)
retry_queue.add("Good message 1")
retry_queue.add("Flaky message")
retry_queue.add("Good message 2")
retry_queue.add("Bad message")

print("Processing with retry:")
processed = retry_queue.process_with_retry()

print(f"\\nSuccessfully processed: {len(processed)}")
print(f"Moved to DLQ: {len(retry_queue.dlq)}")
for item in retry_queue.dlq:
    print(f"  - {item['message']} ({item['attempts']} attempts)")
print()

# Example 4: Message Priority and DLQ
print("="*70)
print("Example 4: Priority Queue with DLQ")
print("="*70)

class PriorityQueueWithDLQ:
    def __init__(self):
        self.high_priority = []
        self.normal_priority = []
        self.dlq = []

    def add(self, message, priority="normal"):
        item = {"message": message, "priority": priority}
        if priority == "high":
            self.high_priority.append(item)
        else:
            self.normal_priority.append(item)

    def process_all(self):
        """Process high priority first"""
        # Process high priority
        while self.high_priority:
            self._process_item(self.high_priority.pop(0))

        # Then normal priority
        while self.normal_priority:
            self._process_item(self.normal_priority.pop(0))

    def _process_item(self, item):
        try:
            if "critical_error" in item["message"]:
                raise Exception("Critical error")
            print(f"  [{item['priority'].upper()}] Processed: {item['message']}")
        except Exception as e:
            print(f"  [{item['priority'].upper()}] Failed: {item['message']} -> DLQ")
            self.dlq.append({"message": item["message"], "error": str(e)})

# Test priority processing
pq = PriorityQueueWithDLQ()
pq.add("Normal task 1", "normal")
pq.add("Critical task 1", "high")
pq.add("Normal critical_error", "normal")
pq.add("Critical task 2", "high")

print("Processing by priority:")
pq.process_all()
print(f"\\nDLQ size: {len(pq.dlq)}")
print()

# Example 5: DLQ with Metadata
print("="*70)
print("Example 5: Dead Letter Queue with Rich Metadata")
print("="*70)

import datetime

class MetadataQueue:
    def __init__(self):
        self.queue = []
        self.dlq = []

    def add(self, message, metadata=None):
        self.queue.append({
            "message": message,
            "metadata": metadata or {},
            "enqueued_at": datetime.datetime.now()
        })

    def process(self):
        while self.queue:
            item = self.queue.pop(0)
            try:
                # Simulate processing
                if item["message"].startswith("FAIL"):
                    raise ValueError("Message marked to fail")
                print(f"  Processed: {item['message']}")
            except Exception as e:
                # Add to DLQ with full metadata
                self.dlq.append({
                    "message": item["message"],
                    "error": str(e),
                    "error_type": type(e).__name__,
                    "original_metadata": item["metadata"],
                    "enqueued_at": item["enqueued_at"],
                    "failed_at": datetime.datetime.now()
                })

# Test metadata tracking
mq = MetadataQueue()
mq.add("Message 1", {"user_id": 123, "type": "order"})
mq.add("FAIL Message", {"user_id": 456, "type": "payment"})
mq.add("Message 2", {"user_id": 789, "type": "order"})

print("Processing messages:")
mq.process()

print("\\nDLQ entries:")
for entry in mq.dlq:
    print(f"  Message: {entry['message']}")
    print(f"    Error: {entry['error']}")
    print(f"    Original metadata: {entry['original_metadata']}")
    print(f"    Failed at: {entry['failed_at']}")
print()

# Example 6: DLQ Inspection and Replay
print("="*70)
print("Example 6: Inspect and Replay Failed Messages")
print("="*70)

class ReplayableQueue:
    def __init__(self):
        self.queue = []
        self.dlq = []
        self.processed = []

    def add(self, message):
        self.queue.append(message)

    def process(self):
        """Process messages, route failures to DLQ"""
        while self.queue:
            message = self.queue.pop(0)
            try:
                if "transient_error" in message:
                    raise Exception("Transient error - can be retried")
                if "permanent_error" in message:
                    raise Exception("Permanent error - cannot recover")

                self.processed.append(message)
                print(f"  Processed: {message}")
            except Exception as e:
                error_type = "transient" if "transient" in str(e) else "permanent"
                self.dlq.append({
                    "message": message,
                    "error": str(e),
                    "retry_possible": error_type == "transient"
                })
                print(f"  Failed: {message} -> DLQ ({error_type})")

    def replay_retryable(self):
        """Replay messages that can be retried"""
        retryable = [item for item in self.dlq if item["retry_possible"]]
        permanent = [item for item in self.dlq if not item["retry_possible"]]

        print(f"\\nReplaying {len(retryable)} retryable messages:")
        self.dlq = permanent

        for item in retryable:
            # Remove error condition for replay simulation
            clean_message = item["message"].replace("transient_error", "fixed")
            self.queue.append(clean_message)

# Test replay functionality
rq = ReplayableQueue()
rq.add("Good message 1")
rq.add("Message with transient_error")
rq.add("Message with permanent_error")
rq.add("Good message 2")

print("Initial processing:")
rq.process()

print(f"\\nDLQ status:")
print(f"  Total in DLQ: {len(rq.dlq)}")
print(f"  Retryable: {sum(1 for item in rq.dlq if item['retry_possible'])}")

# Replay retryable messages
rq.replay_retryable()
print("\\nAfter replay:")
rq.process()

print(f"\\nFinal stats:")
print(f"  Processed: {len(rq.processed)}")
print(f"  Permanent failures in DLQ: {len(rq.dlq)}")
print()

# Example 7: DLQ with Alerting
print("="*70)
print("Example 7: DLQ with Alert Thresholds")
print("="*70)

class AlertingQueue:
    def __init__(self, alert_threshold=3):
        self.queue = []
        self.dlq = []
        self.alert_threshold = alert_threshold

    def add(self, message):
        self.queue.append(message)

    def process(self):
        while self.queue:
            message = self.queue.pop(0)
            try:
                if "ERROR" in message:
                    raise Exception(f"Failed to process: {message}")
                print(f"  Processed: {message}")
            except Exception as e:
                self.dlq.append({"message": message, "error": str(e)})
                print(f"  Failed: {message} -> DLQ")

                # Check if alert needed
                if len(self.dlq) >= self.alert_threshold:
                    self._send_alert()

    def _send_alert(self):
        """Simulate sending an alert"""
        print(f"\\n  *** ALERT: DLQ threshold reached! ***")
        print(f"  *** {len(self.dlq)} messages in DLQ ***\\n")

# Test alerting
aq = AlertingQueue(alert_threshold=3)
for i in range(5):
    aq.add(f"Message {i}")
    if i % 2 == 0:
        aq.add(f"ERROR Message {i}")

aq.process()
print()

# Example 8: Batch DLQ Processing
print("="*70)
print("Example 8: Batch Processing with DLQ")
print("="*70)

class BatchQueue:
    def __init__(self, batch_size=3):
        self.queue = []
        self.dlq = []
        self.batch_size = batch_size

    def add_batch(self, messages):
        self.queue.extend(messages)

    def process_batches(self):
        """Process messages in batches"""
        batch_num = 1

        while self.queue:
            # Get next batch
            batch = []
            for _ in range(min(self.batch_size, len(self.queue))):
                batch.append(self.queue.pop(0))

            print(f"Processing batch {batch_num} ({len(batch)} messages):")

            # Process batch
            for message in batch:
                try:
                    if "fail" in message.lower():
                        raise Exception("Batch item failed")
                    print(f"  OK: {message}")
                except Exception as e:
                    print(f"  FAIL: {message} -> DLQ")
                    self.dlq.append({"message": message, "batch": batch_num, "error": str(e)})

            batch_num += 1
            print()

# Test batch processing
bq = BatchQueue(batch_size=3)
messages = [
    "Item 1", "Item 2 FAIL", "Item 3",
    "Item 4", "Item 5", "Item 6 FAIL",
    "Item 7", "Item 8"
]
bq.add_batch(messages)
bq.process_batches()

print(f"DLQ summary: {len(bq.dlq)} failed items")
for item in bq.dlq:
    print(f"  Batch {item['batch']}: {item['message']}")
print()

# Example 9: DLQ Expiration
print("="*70)
print("Example 9: DLQ with Message Expiration")
print("="*70)

class ExpiringDLQ:
    def __init__(self, ttl_seconds=5):
        self.dlq = []
        self.ttl_seconds = ttl_seconds

    def add_to_dlq(self, message, error):
        """Add message to DLQ with timestamp"""
        self.dlq.append({
            "message": message,
            "error": error,
            "timestamp": datetime.datetime.now()
        })

    def cleanup_expired(self):
        """Remove expired messages from DLQ"""
        now = datetime.datetime.now()
        expired = []
        active = []

        for item in self.dlq:
            age = (now - item["timestamp"]).total_seconds()
            if age > self.ttl_seconds:
                expired.append(item)
            else:
                active.append(item)

        self.dlq = active
        return expired

# Test expiration
import time

edlq = ExpiringDLQ(ttl_seconds=2)
edlq.add_to_dlq("Old message 1", "Error 1")
time.sleep(1)
edlq.add_to_dlq("Old message 2", "Error 2")
time.sleep(1.5)
edlq.add_to_dlq("New message", "Error 3")

print(f"DLQ size before cleanup: {len(edlq.dlq)}")
expired = edlq.cleanup_expired()
print(f"Expired messages: {len(expired)}")
print(f"DLQ size after cleanup: {len(edlq.dlq)}")
for item in expired:
    print(f"  Expired: {item['message']}")
print()

# Example 10: Practical Application - Task Queue System
print("="*70)
print("Example 10: Real-World Use Case - Task Processing System")
print("="*70)

class TaskProcessor:
    """Production-like task processor with DLQ"""

    def __init__(self, max_retries=3):
        self.pending = []
        self.processing = []
        self.completed = []
        self.dlq = []
        self.max_retries = max_retries

    def submit_task(self, task_id, task_type, data):
        """Submit a new task"""
        task = {
            "id": task_id,
            "type": task_type,
            "data": data,
            "attempts": 0,
            "submitted_at": datetime.datetime.now()
        }
        self.pending.append(task)
        print(f"Task {task_id} submitted")

    def process_tasks(self):
        """Process all pending tasks"""
        while self.pending:
            task = self.pending.pop(0)
            self.processing.append(task)

            try:
                # Simulate task processing
                self._execute_task(task)

                # Success
                self.processing.remove(task)
                task["completed_at"] = datetime.datetime.now()
                self.completed.append(task)
                print(f"  Task {task['id']} completed successfully")

            except Exception as e:
                task["attempts"] += 1
                self.processing.remove(task)

                if task["attempts"] < self.max_retries:
                    # Retry
                    print(f"  Task {task['id']} failed (attempt {task['attempts']}), retrying...")
                    self.pending.append(task)
                else:
                    # Move to DLQ
                    task["error"] = str(e)
                    task["failed_at"] = datetime.datetime.now()
                    self.dlq.append(task)
                    print(f"  Task {task['id']} failed permanently -> DLQ")

    def _execute_task(self, task):
        """Execute a single task"""
        # Simulate different task types
        if task["type"] == "email":
            if "invalid" in task["data"]:
                raise ValueError("Invalid email address")
        elif task["type"] == "payment":
            if task["data"] < 0:
                raise ValueError("Invalid payment amount")
        elif task["type"] == "api_call":
            if task["attempts"] < 2:  # Fail first 2 attempts
                raise Exception("API temporarily unavailable")

    def get_stats(self):
        """Get processing statistics"""
        return {
            "pending": len(self.pending),
            "processing": len(self.processing),
            "completed": len(self.completed),
            "failed": len(self.dlq)
        }

    def inspect_dlq(self):
        """Show DLQ contents"""
        print("\\nDead Letter Queue Contents:")
        print("=" * 70)
        for task in self.dlq:
            print(f"Task ID: {task['id']}")
            print(f"  Type: {task['type']}")
            print(f"  Data: {task['data']}")
            print(f"  Attempts: {task['attempts']}")
            print(f"  Error: {task['error']}")
            print(f"  Submitted: {task['submitted_at']}")
            print(f"  Failed: {task['failed_at']}")
            print()

# Create and test task processor
processor = TaskProcessor(max_retries=3)

# Submit various tasks
processor.submit_task(1, "email", "user@example.com")
processor.submit_task(2, "email", "invalid_email")
processor.submit_task(3, "payment", 100.0)
processor.submit_task(4, "payment", -50.0)
processor.submit_task(5, "api_call", {"endpoint": "/users"})

print("\\nProcessing tasks...")
processor.process_tasks()

# Show statistics
print("\\n" + "=" * 70)
print("PROCESSING STATISTICS")
print("=" * 70)
stats = processor.get_stats()
for key, value in stats.items():
    print(f"{key.capitalize():15} {value:>3}")

# Inspect DLQ
processor.inspect_dlq()

print("="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. DLQ isolates failed messages for separate handling")
print("2. Implement retry logic before moving to DLQ")
print("3. Track metadata: attempts, timestamps, error details")
print("4. Set alert thresholds for DLQ size monitoring")
print("5. Use DLQ for transient vs permanent error analysis")
print("6. Implement message expiration to prevent DLQ bloat")
print("7. Enable DLQ inspection and manual replay")
print("8. Process by priority: high priority first")
print("9. Batch processing can improve throughput")
print("10. Essential pattern for resilient distributed systems")
print("="*70)
'''

# Upgrade Lesson 153: IndexError Handling
lesson153['fullSolution'] = '''"""
IndexError Handling

Master IndexError exception handling in Python. Learn to safely access list
elements, handle out-of-bounds indices, validate ranges, and implement
defensive programming techniques for sequence operations.

**Zero Package Installation Required**
"""

# Example 1: Understanding IndexError
print("="*70)
print("Example 1: What Causes IndexError")
print("="*70)

numbers = [10, 20, 30, 40, 50]
print(f"List: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Valid indices: 0 to {len(numbers) - 1}")

# Valid access
print(f"\\nValid access - numbers[2]: {numbers[2]}")

# Invalid access
try:
    value = numbers[10]
    print(f"numbers[10]: {value}")
except IndexError as e:
    print(f"\\nIndexError caught: {e}")
    print("Attempted to access index 10, but list only has 5 elements")
print()

# Example 2: Handling IndexError with Try-Except
print("="*70)
print("Example 2: Safe List Access with Exception Handling")
print("="*70)

def safe_get(lst, index, default=None):
    """Safely get element from list"""
    try:
        return lst[index]
    except IndexError:
        print(f"  Index {index} out of range, returning default: {default}")
        return default

fruits = ["apple", "banana", "cherry"]

# Test safe access
print(f"List: {fruits}")
print(f"safe_get(fruits, 1): {safe_get(fruits, 1)}")
print(f"safe_get(fruits, 5): {safe_get(fruits, 5)}")
print(f"safe_get(fruits, 10, 'N/A'): {safe_get(fruits, 10, 'N/A')}")
print()

# Example 3: Preventing IndexError with Validation
print("="*70)
print("Example 3: Validate Index Before Access")
print("="*70)

def get_element(lst, index):
    """Get element with validation"""
    if not lst:
        print("  Error: List is empty")
        return None

    if index < 0 or index >= len(lst):
        print(f"  Error: Index {index} out of range [0, {len(lst)-1}]")
        return None

    return lst[index]

data = [100, 200, 300]

# Test validation
print(f"Data: {data}")
print(f"get_element(data, 1): {get_element(data, 1)}")
print(f"get_element(data, 5): {get_element(data, 5)}")
print(f"get_element([], 0): {get_element([], 0)}")
print()

# Example 4: Negative Index Handling
print("="*70)
print("Example 4: Handling Negative Indices")
print("="*70)

items = ['a', 'b', 'c', 'd', 'e']

print(f"List: {items}")
print("Valid negative indices: -1 to -5")

# Valid negative indices
print(f"items[-1]: {items[-1]}")  # Last element
print(f"items[-2]: {items[-2]}")  # Second to last

# Invalid negative index
try:
    value = items[-10]
except IndexError as e:
    print(f"\\nIndexError: {e}")
    print("items[-10] is out of range")
print()

# Example 5: IndexError in Loops
print("="*70)
print("Example 5: Avoiding IndexError in Loops")
print("="*70)

numbers = [10, 20, 30, 40, 50]

# Dangerous: Hardcoded range
print("Dangerous approach (hardcoded range):")
try:
    for i in range(10):  # Goes beyond list length
        print(f"  numbers[{i}] = {numbers[i]}")
except IndexError as e:
    print(f"  ERROR: {e}")

# Safe: Use len()
print("\\nSafe approach (using len()):")
for i in range(len(numbers)):
    print(f"  numbers[{i}] = {numbers[i]}")

# Best: Enumerate
print("\\nBest approach (using enumerate):")
for i, value in enumerate(numbers):
    print(f"  numbers[{i}] = {value}")
print()

# Example 6: IndexError in String Slicing
print("="*70)
print("Example 6: IndexError vs Slicing Behavior")
print("="*70)

text = "Hello"
print(f"String: '{text}'")

# Index access raises error
try:
    char = text[10]
except IndexError as e:
    print(f"text[10] raises IndexError: {e}")

# Slicing doesn't raise error
print(f"text[10:15] returns empty string: '{text[10:15]}'")
print(f"text[:100] returns full string: '{text[:100]}'")
print()

# Example 7: Multi-dimensional List IndexError
print("="*70)
print("Example 7: IndexError in Nested Lists")
print("="*70)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def safe_matrix_get(matrix, row, col):
    """Safely access matrix element"""
    try:
        return matrix[row][col]
    except IndexError:
        print(f"  Invalid position ({row}, {col})")
        return None

print("Matrix:")
for row in matrix:
    print(f"  {row}")

print("\\nAccessing elements:")
print(f"safe_matrix_get(matrix, 1, 1): {safe_matrix_get(matrix, 1, 1)}")
print(f"safe_matrix_get(matrix, 0, 5): {safe_matrix_get(matrix, 0, 5)}")
print(f"safe_matrix_get(matrix, 5, 0): {safe_matrix_get(matrix, 5, 0)}")
print()

# Example 8: IndexError with Pop and Remove
print("="*70)
print("Example 8: IndexError with List Methods")
print("="*70)

items = ['x', 'y', 'z']

print(f"List: {items}")

# Pop with invalid index
try:
    removed = items.pop(10)
except IndexError as e:
    print(f"items.pop(10) raised IndexError: {e}")

# Pop without index (safe, removes last item)
if items:
    removed = items.pop()
    print(f"items.pop() removed: {removed}")
    print(f"List now: {items}")

# Pop from empty list
empty = []
try:
    empty.pop()
except IndexError as e:
    print(f"\\nempty.pop() raised IndexError: {e}")
print()

# Example 9: IndexError Recovery Strategies
print("="*70)
print("Example 9: Different Recovery Strategies")
print("="*70)

data = [10, 20, 30]

# Strategy 1: Return None
def strategy_return_none(lst, idx):
    try:
        return lst[idx]
    except IndexError:
        return None

# Strategy 2: Return default value
def strategy_default(lst, idx, default=0):
    try:
        return lst[idx]
    except IndexError:
        return default

# Strategy 3: Clamp index to valid range
def strategy_clamp(lst, idx):
    if not lst:
        return None
    if idx < 0:
        return lst[0]
    if idx >= len(lst):
        return lst[-1]
    return lst[idx]

# Strategy 4: Use modulo to wrap around
def strategy_wrap(lst, idx):
    if not lst:
        return None
    return lst[idx % len(lst)]

print(f"Data: {data}")
print(f"\\nAccessing index 10:")
print(f"  Return None: {strategy_return_none(data, 10)}")
print(f"  Return default (0): {strategy_default(data, 10, 0)}")
print(f"  Clamp to range: {strategy_clamp(data, 10)}")
print(f"  Wrap around: {strategy_wrap(data, 10)}")
print()

# Example 10: Practical Application - Safe Data Processor
print("="*70)
print("Example 10: Real-World Use Case - CSV Row Processor")
print("="*70)

class CSVRowProcessor:
    """Process CSV-like data with robust error handling"""

    def __init__(self, expected_columns):
        self.expected_columns = expected_columns
        self.errors = []

    def process_row(self, row, row_number):
        """Process a single row with IndexError handling"""
        result = {}

        try:
            # Expected: [name, age, city, salary]
            result['name'] = row[0]
            result['age'] = int(row[1])
            result['city'] = row[2]
            result['salary'] = float(row[3])

            print(f"  Row {row_number}: {result['name']:15} {result['city']:12} ${result['salary']:>10,.2f}")
            return result

        except IndexError as e:
            error_msg = f"Row {row_number}: Missing columns (expected {self.expected_columns}, got {len(row)})"
            print(f"  ERROR - {error_msg}")
            self.errors.append({
                "row": row_number,
                "error": error_msg,
                "data": row
            })
            return None

        except ValueError as e:
            error_msg = f"Row {row_number}: Invalid data format - {e}"
            print(f"  ERROR - {error_msg}")
            self.errors.append({
                "row": row_number,
                "error": error_msg,
                "data": row
            })
            return None

    def process_all(self, rows):
        """Process all rows"""
        results = []

        print("Processing CSV data:")
        print("  " + "-" * 60)

        for i, row in enumerate(rows, start=1):
            result = self.process_row(row, i)
            if result:
                results.append(result)

        print("  " + "-" * 60)
        return results

    def report_errors(self):
        """Report all errors"""
        if not self.errors:
            print("\\nNo errors encountered!")
            return

        print(f"\\nERROR REPORT - {len(self.errors)} errors found:")
        print("=" * 70)
        for error in self.errors:
            print(f"Row {error['row']}: {error['error']}")
            print(f"  Data: {error['data']}")
            print()

# Test CSV processor
processor = CSVRowProcessor(expected_columns=4)

# Sample data with various issues
csv_data = [
    ['Alice', '30', 'New York', '75000'],      # Valid
    ['Bob', '25', 'LA'],                        # Missing column
    ['Charlie', '35', 'Chicago', '90000'],      # Valid
    ['David'],                                  # Missing multiple columns
    ['Eve', 'invalid', 'Boston', '65000'],      # Invalid age format
    ['Frank', '40', 'Seattle', '85000'],        # Valid
]

results = processor.process_all(csv_data)

print(f"\\nSuccessfully processed: {len(results)} rows")
print(f"Failed: {len(processor.errors)} rows")

processor.report_errors()

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. IndexError occurs when accessing invalid list index")
print("2. Valid indices: 0 to len(list)-1 (or -1 to -len(list))")
print("3. Use try-except to handle IndexError gracefully")
print("4. Validate index before access: 0 <= index < len(list)")
print("5. Use len() in loops instead of hardcoded ranges")
print("6. enumerate() prevents IndexError in iterations")
print("7. Slicing doesn't raise IndexError (returns empty)")
print("8. pop() on empty list raises IndexError")
print("9. Implement recovery strategies: default, clamp, wrap")
print("10. Log errors for debugging and monitoring")
print("="*70)
'''

# Save progress
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Upgrade Lesson 154: KeyError Handling
lesson154['fullSolution'] = '''"""
KeyError Handling

Master KeyError exception handling in Python. Learn to safely access dictionary
keys, implement fallback values, use get() method, validate keys, and build
robust data access patterns for production applications.

**Zero Package Installation Required**
"""

# Example 1: Understanding KeyError
print("="*70)
print("Example 1: What Causes KeyError")
print("="*70)

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Dictionary: {person}")

# Valid access
print(f"person['name']: {person['name']}")

# Invalid access
try:
    email = person['email']
except KeyError as e:
    print(f"\\nKeyError caught: {e}")
    print("Key 'email' does not exist in dictionary")
print()

# Example 2: Safe Dictionary Access with get()
print("="*70)
print("Example 2: Using get() Method to Avoid KeyError")
print("="*70)

config = {"host": "localhost", "port": 8080, "debug": True}
print(f"Config: {config}")

# get() returns None if key doesn't exist
print(f"\\nconfig.get('host'): {config.get('host')}")
print(f"config.get('timeout'): {config.get('timeout')}")
print(f"config.get('timeout', 30): {config.get('timeout', 30)}")  # Default value
print()

# Example 3: Try-Except for KeyError
print("="*70)
print("Example 3: Handling KeyError with Try-Except")
print("="*70)

def safe_get(dictionary, key):
    """Safely get value with error handling"""
    try:
        return dictionary[key]
    except KeyError:
        print(f"  Warning: Key '{key}' not found, returning None")
        return None

data = {"a": 1, "b": 2, "c": 3}

print(f"Data: {data}")
print(f"safe_get(data, 'b'): {safe_get(data, 'b')}")
print(f"safe_get(data, 'x'): {safe_get(data, 'x')}")
print()

# Example 4: Validating Keys Before Access
print("="*70)
print("Example 4: Check if Key Exists Before Accessing")
print("="*70)

user = {"username": "john_doe", "email": "john@example.com"}

# Check with 'in' operator
if "username" in user:
    print(f"Username: {user['username']}")

if "phone" in user:
    print(f"Phone: {user['phone']}")
else:
    print("Phone number not available")

# Using keys() method
print(f"\\nAvailable keys: {list(user.keys())}")
print()

# Example 5: setdefault() Method
print("="*70)
print("Example 5: Using setdefault() for Safe Access")
print("="*70)

scores = {"math": 95, "science": 88}
print(f"Scores: {scores}")

# setdefault() returns value if exists, sets and returns default if not
math_score = scores.setdefault("math", 0)
print(f"\\nMath score: {math_score}")
print(f"Scores after: {scores}")

english_score = scores.setdefault("english", 0)
print(f"\\nEnglish score (new): {english_score}")
print(f"Scores after: {scores}")
print()

# Example 6: Nested Dictionary KeyError
print("="*70)
print("Example 6: KeyError in Nested Dictionaries")
print("="*70)

data = {
    "users": {
        "alice": {"age": 30, "city": "NYC"},
        "bob": {"age": 25, "city": "LA"}
    }
}

def safe_nested_get(dictionary, *keys, default=None):
    """Safely access nested dictionary values"""
    result = dictionary
    try:
        for key in keys:
            result = result[key]
        return result
    except (KeyError, TypeError):
        return default

print(f"Data structure: {data}")
print(f"\\nAlice's city: {safe_nested_get(data, 'users', 'alice', 'city')}")
print(f"Charlie's age: {safe_nested_get(data, 'users', 'charlie', 'age', default='N/A')}")
print(f"Bob's phone: {safe_nested_get(data, 'users', 'bob', 'phone', default='N/A')}")
print()

# Example 7: KeyError with Dictionary Methods
print("="*70)
print("Example 7: KeyError with pop() and del")
print("="*70)

items = {"x": 10, "y": 20, "z": 30}
print(f"Items: {items}")

# pop() with default (safe)
value = items.pop("x", None)
print(f"\\nPopped 'x': {value}")
print(f"Items: {items}")

# pop() without default (can raise KeyError)
try:
    value = items.pop("missing")
except KeyError as e:
    print(f"\\nKeyError on pop: {e}")

# pop() with default avoids error
value = items.pop("missing", "default")
print(f"Pop with default: {value}")

# del statement can raise KeyError
try:
    del items["nonexistent"]
except KeyError as e:
    print(f"\\nKeyError on del: {e}")
print()

# Example 8: defaultdict to Prevent KeyError
print("="*70)
print("Example 8: Using defaultdict from collections")
print("="*70)

from collections import defaultdict

# Regular dict raises KeyError
regular_dict = {}
try:
    regular_dict["count"] += 1
except KeyError:
    print("Regular dict: KeyError on missing key")

# defaultdict provides default value
counter = defaultdict(int)  # int() returns 0
counter["count"] += 1
counter["count"] += 1
print(f"\\ndefaultdict counter: {dict(counter)}")

# defaultdict with list
groups = defaultdict(list)
groups["team_a"].append("Alice")
groups["team_a"].append("Bob")
groups["team_b"].append("Charlie")
print(f"defaultdict groups: {dict(groups)}")
print()

# Example 9: Multiple Key Access Strategies
print("="*70)
print("Example 9: Different Key Access Patterns")
print("="*70)

config = {
    "database": "postgres",
    "host": "localhost",
    "port": 5432
}

# Strategy 1: Try-except
try:
    user = config["user"]
except KeyError:
    user = "default_user"
print(f"Strategy 1 (try-except): user = {user}")

# Strategy 2: get() with default
password = config.get("password", "default_pass")
print(f"Strategy 2 (get): password = {password}")

# Strategy 3: Check then access
if "timeout" in config:
    timeout = config["timeout"]
else:
    timeout = 30
print(f"Strategy 3 (check first): timeout = {timeout}")

# Strategy 4: setdefault()
ssl = config.setdefault("ssl", True)
print(f"Strategy 4 (setdefault): ssl = {ssl}")
print(f"Config now: {config}")
print()

# Example 10: Practical Application - Configuration Manager
print("="*70)
print("Example 10: Real-World Use Case - Robust Config Manager")
print("="*70)

class ConfigManager:
    """Configuration manager with KeyError handling"""

    def __init__(self, config_dict=None):
        self.config = config_dict or {}
        self.access_log = []
        self.missing_keys = set()

    def get(self, key, default=None, required=False):
        """
        Get configuration value with error handling

        Args:
            key: Configuration key
            default: Default value if key not found
            required: If True, raise error for missing key
        """
        self.access_log.append(key)

        try:
            value = self.config[key]
            print(f"  Config '{key}': {value}")
            return value

        except KeyError:
            if required:
                self.missing_keys.add(key)
                raise KeyError(f"Required configuration '{key}' is missing")

            self.missing_keys.add(key)
            print(f"  Config '{key}': not found, using default: {default}")
            return default

    def get_nested(self, *keys, default=None):
        """Get nested configuration value"""
        result = self.config
        path = ".".join(keys)

        try:
            for key in keys:
                result = result[key]
            print(f"  Nested config '{path}': {result}")
            return result

        except (KeyError, TypeError):
            print(f"  Nested config '{path}': not found, using default: {default}")
            self.missing_keys.add(path)
            return default

    def require(self, *keys):
        """Validate that required keys exist"""
        missing = []
        for key in keys:
            if key not in self.config:
                missing.append(key)

        if missing:
            raise KeyError(f"Required configuration keys missing: {missing}")

    def report(self):
        """Generate access report"""
        print("\\nConfiguration Access Report:")
        print("=" * 70)
        print(f"Total accesses: {len(self.access_log)}")
        print(f"Unique keys accessed: {len(set(self.access_log))}")
        print(f"Missing keys: {len(self.missing_keys)}")
        if self.missing_keys:
            print(f"Missing key list: {sorted(self.missing_keys)}")

# Test configuration manager
app_config = {
    "app": {
        "name": "MyApp",
        "version": "1.0.0"
    },
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "debug": True
}

manager = ConfigManager(app_config)

print("Accessing configuration values:")
print("-" * 70)

# Get simple values
manager.get("debug")
manager.get("timeout", default=30)

# Get nested values
manager.get_nested("app", "name")
manager.get_nested("app", "author", default="Unknown")
manager.get_nested("database", "host")
manager.get_nested("database", "user", default="postgres")

# Try to get missing nested value
manager.get_nested("cache", "ttl", default=300)

# Validate required keys
try:
    manager.require("debug", "app")
    print("\\nRequired keys validation: PASSED")
except KeyError as e:
    print(f"\\nRequired keys validation: FAILED - {e}")

# Try to require missing key
try:
    manager.require("secret_key")
except KeyError as e:
    print(f"Required key check failed: {e}")

# Generate report
manager.report()

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. KeyError occurs when accessing non-existent dictionary key")
print("2. Use dict.get(key, default) for safe access with fallback")
print("3. Check key existence: if key in dict")
print("4. Try-except KeyError for error handling")
print("5. setdefault(key, default) gets or sets value")
print("6. pop(key, default) safely removes and returns value")
print("7. defaultdict provides automatic default values")
print("8. For nested dicts, handle KeyError and TypeError")
print("9. Validate required keys at application startup")
print("10. Log missing keys for debugging and monitoring")
print("="*70)
'''

# Upgrade Lesson 155: Raise Exceptions
lesson155['fullSolution'] = '''"""
Raise Exceptions

Master raising exceptions in Python. Learn to throw built-in exceptions,
create custom error messages, re-raise exceptions, and implement proper
error signaling in your code. Essential for robust error handling.

**Zero Package Installation Required**
"""

# Example 1: Basic Exception Raising
print("="*70)
print("Example 1: Raising Built-in Exceptions")
print("="*70)

def divide(a, b):
    """Divide with error checking"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test the function
try:
    result = divide(10, 2)
    print(f"10 / 2 = {result}")
except ValueError as e:
    print(f"Error: {e}")

try:
    result = divide(10, 0)
    print(f"10 / 0 = {result}")
except ValueError as e:
    print(f"Error: {e}")
print()

# Example 2: Different Exception Types
print("="*70)
print("Example 2: Raising Different Exception Types")
print("="*70)

def process_age(age):
    """Process age with validation"""
    if not isinstance(age, int):
        raise TypeError(f"Age must be integer, got {type(age).__name__}")

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 150:
        raise ValueError("Age is unrealistically high")

    print(f"  Processing age: {age}")
    return age

# Test with valid age
try:
    process_age(25)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Test with invalid type
try:
    process_age("25")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Test with negative age
try:
    process_age(-5)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
print()

# Example 3: Raising with Custom Messages
print("="*70)
print("Example 3: Custom Error Messages")
print("="*70)

def withdraw(balance, amount):
    """Withdraw money with validation"""
    if amount <= 0:
        raise ValueError(f"Withdrawal amount must be positive, got {amount}")

    if amount > balance:
        raise ValueError(
            f"Insufficient funds: tried to withdraw ${amount:.2f}, "
            f"but balance is only ${balance:.2f}"
        )

    return balance - amount

balance = 1000.0

try:
    balance = withdraw(balance, 200)
    print(f"Withdrew $200, new balance: ${balance:.2f}")
except ValueError as e:
    print(f"Withdrawal failed: {e}")

try:
    balance = withdraw(balance, 2000)
except ValueError as e:
    print(f"Withdrawal failed: {e}")

try:
    balance = withdraw(balance, -50)
except ValueError as e:
    print(f"Withdrawal failed: {e}")
print()

# Example 4: Re-raising Exceptions
print("="*70)
print("Example 4: Re-raising Exceptions with Additional Context")
print("="*70)

def read_config(filename):
    """Read configuration file"""
    try:
        with open(filename, 'r') as f:
            data = f.read()
            return data
    except FileNotFoundError:
        print(f"  Logging error: Config file {filename} not found")
        raise  # Re-raise the same exception

def load_app_config():
    """Load application configuration"""
    try:
        config = read_config("missing_config.txt")
        return config
    except FileNotFoundError as e:
        print(f"  Application startup failed due to missing config")
        raise RuntimeError("Cannot start application without config file") from e

try:
    load_app_config()
except RuntimeError as e:
    print(f"\\nFatal error: {e}")
    if e.__cause__:
        print(f"Caused by: {e.__cause__}")
print()

# Example 5: Conditional Exception Raising
print("="*70)
print("Example 5: Raise Exceptions Based on Conditions")
print("="*70)

def validate_username(username):
    """Validate username with multiple checks"""
    if not username:
        raise ValueError("Username cannot be empty")

    if len(username) < 3:
        raise ValueError(f"Username too short: {len(username)} chars (minimum 3)")

    if len(username) > 20:
        raise ValueError(f"Username too long: {len(username)} chars (maximum 20)")

    if not username.isalnum():
        raise ValueError("Username must contain only letters and numbers")

    print(f"  Username '{username}' is valid")
    return True

# Test various usernames
usernames = ["alice", "ab", "this_is_a_very_long_username_that_exceeds_limit", "user@123", ""]

for username in usernames:
    try:
        validate_username(username)
    except ValueError as e:
        print(f"  Invalid username '{username}': {e}")
print()

# Example 6: Raising in Assertions
print("="*70)
print("Example 6: Using raise vs assert")
print("="*70)

def calculate_discount(price, discount_percent):
    """Calculate discounted price"""
    # Use raise for expected validation
    if price < 0:
        raise ValueError(f"Price cannot be negative: {price}")

    if discount_percent < 0 or discount_percent > 100:
        raise ValueError(f"Discount must be 0-100, got {discount_percent}")

    # Assertions for internal checks (can be disabled with -O flag)
    assert isinstance(price, (int, float)), "Price must be numeric"
    assert isinstance(discount_percent, (int, float)), "Discount must be numeric"

    return price * (1 - discount_percent / 100)

try:
    print(f"$100 with 20% discount: ${calculate_discount(100, 20):.2f}")
except ValueError as e:
    print(f"Error: {e}")

try:
    print(f"$100 with 150% discount: ${calculate_discount(100, 150):.2f}")
except ValueError as e:
    print(f"Error: {e}")
print()

# Example 7: Raising in Property Setters
print("="*70)
print("Example 7: Raising Exceptions in Property Setters")
print("="*70)

class Temperature:
    """Temperature class with validation"""

    def __init__(self, celsius):
        self._celsius = None
        self.celsius = celsius  # Use setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(
                f"Temperature {value}°C is below absolute zero (-273.15°C)"
            )
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

# Test temperature class
try:
    temp1 = Temperature(25)
    print(f"Temperature: {temp1.celsius}°C = {temp1.fahrenheit:.1f}°F")
except ValueError as e:
    print(f"Error: {e}")

try:
    temp2 = Temperature(-300)
except ValueError as e:
    print(f"Error: {e}")

try:
    temp3 = Temperature(0)
    temp3.celsius = -280  # Try to set invalid temperature
except ValueError as e:
    print(f"Error: {e}")
print()

# Example 8: Exception Chains
print("="*70)
print("Example 8: Exception Chaining with 'from'")
print("="*70)

def parse_int(value):
    """Parse integer from string"""
    try:
        return int(value)
    except ValueError as e:
        raise ValueError(f"Could not parse '{value}' as integer") from e

def process_input(data):
    """Process user input"""
    try:
        number = parse_int(data)
        return number * 2
    except ValueError as e:
        print(f"Processing error: {e}")
        if e.__cause__:
            print(f"  Original error: {e.__cause__}")
        raise

# Test exception chaining
try:
    result = process_input("123")
    print(f"Result: {result}")
except ValueError:
    pass

try:
    result = process_input("abc")
except ValueError:
    print("Failed to process input")
print()

# Example 9: Raising Exceptions in Loops
print("="*70)
print("Example 9: Raising Exceptions to Break Out of Loops")
print("="*70)

def find_divisor(number, divisors):
    """Find first divisor that divides evenly"""
    for divisor in divisors:
        if divisor == 0:
            raise ValueError("Cannot test divisibility by zero")

        if number % divisor == 0:
            return divisor

    raise ValueError(f"No divisor found for {number} in {divisors}")

try:
    divisor = find_divisor(100, [3, 5, 7, 10, 13])
    print(f"Found divisor: {divisor}")
except ValueError as e:
    print(f"Error: {e}")

try:
    divisor = find_divisor(100, [3, 7, 13])
    print(f"Found divisor: {divisor}")
except ValueError as e:
    print(f"Error: {e}")

try:
    divisor = find_divisor(100, [3, 0, 7])
except ValueError as e:
    print(f"Error: {e}")
print()

# Example 10: Practical Application - Input Validator
print("="*70)
print("Example 10: Real-World Use Case - Form Validation System")
print("="*70)

class ValidationError(Exception):
    """Custom validation error"""
    pass

class FormValidator:
    """Form validator that raises exceptions for invalid data"""

    @staticmethod
    def validate_email(email):
        """Validate email address"""
        if not email:
            raise ValidationError("Email is required")

        if '@' not in email:
            raise ValidationError(f"Invalid email format: {email}")

        parts = email.split('@')
        if len(parts) != 2:
            raise ValidationError(f"Invalid email format: {email}")

        if not parts[0] or not parts[1]:
            raise ValidationError(f"Invalid email format: {email}")

        if '.' not in parts[1]:
            raise ValidationError(f"Email domain must contain a dot: {email}")

        return True

    @staticmethod
    def validate_password(password):
        """Validate password strength"""
        if not password:
            raise ValidationError("Password is required")

        if len(password) < 8:
            raise ValidationError(
                f"Password too short: {len(password)} chars (minimum 8)"
            )

        if not any(c.isupper() for c in password):
            raise ValidationError("Password must contain at least one uppercase letter")

        if not any(c.isdigit() for c in password):
            raise ValidationError("Password must contain at least one digit")

        return True

    @staticmethod
    def validate_age(age):
        """Validate age"""
        try:
            age_int = int(age)
        except (ValueError, TypeError):
            raise ValidationError(f"Age must be a number, got: {age}")

        if age_int < 0:
            raise ValidationError(f"Age cannot be negative: {age_int}")

        if age_int < 13:
            raise ValidationError("Must be at least 13 years old to register")

        if age_int > 120:
            raise ValidationError(f"Age seems invalid: {age_int}")

        return True

    def validate_form(self, email, password, age):
        """Validate entire form"""
        errors = []

        # Validate each field
        try:
            self.validate_email(email)
        except ValidationError as e:
            errors.append(str(e))

        try:
            self.validate_password(password)
        except ValidationError as e:
            errors.append(str(e))

        try:
            self.validate_age(age)
        except ValidationError as e:
            errors.append(str(e))

        # If any errors, raise with all messages
        if errors:
            raise ValidationError("Form validation failed:\\n  - " + "\\n  - ".join(errors))

        return True

# Test form validator
validator = FormValidator()

# Test individual validations
print("Individual field validations:")
print("-" * 70)

test_cases = [
    ("email", "user@example.com", validator.validate_email),
    ("email", "invalid-email", validator.validate_email),
    ("password", "SecurePass123", validator.validate_password),
    ("password", "weak", validator.validate_password),
    ("age", 25, validator.validate_age),
    ("age", 10, validator.validate_age),
]

for field, value, validate_func in test_cases:
    try:
        validate_func(value)
        print(f"  {field} '{value}': VALID")
    except ValidationError as e:
        print(f"  {field} '{value}': INVALID - {e}")

# Test full form validation
print("\\nFull form validations:")
print("-" * 70)

forms = [
    ("alice@example.com", "SecurePass123", 25),
    ("bad-email", "weak", 10),
    ("bob@test.com", "GoodPass456", 30),
]

for email, password, age in forms:
    try:
        validator.validate_form(email, password, age)
        print(f"  Form VALID: {email}, {age} years old")
    except ValidationError as e:
        print(f"  Form INVALID: {email}")
        print(f"    {e}")

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. raise ExceptionType('message') - Throw an exception")
print("2. Use ValueError for invalid values")
print("3. Use TypeError for wrong types")
print("4. raise - Re-raise current exception")
print("5. raise NewException() from original - Chain exceptions")
print("6. Provide clear, descriptive error messages")
print("7. Raise early when validation fails")
print("8. Use custom exception classes for domain errors")
print("9. Don't raise exceptions for normal control flow")
print("10. Document what exceptions your functions raise")
print("="*70)
'''

# Upgrade Lesson 156: Raising Exceptions (Alternative)
lesson156['fullSolution'] = lesson155['fullSolution']  # Similar content, use same comprehensive solution

# Upgrade Lesson 157: Try-Except Basics
lesson157['fullSolution'] = '''"""
Try-Except Basics

Master try-except blocks for exception handling in Python. Learn to catch
exceptions, handle multiple exception types, use else and finally clauses,
and implement robust error handling patterns.

**Zero Package Installation Required**
"""

# Example 1: Basic Try-Except
print("="*70)
print("Example 1: Basic Try-Except Block")
print("="*70)

# Without exception handling
print("Without try-except:")
# This would crash: result = 10 / 0

# With exception handling
print("\\nWith try-except:")
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

print("Program continues after exception")
print()

# Example 2: Catching Exception Details
print("="*70)
print("Example 2: Accessing Exception Information")
print("="*70)

try:
    numbers = [1, 2, 3]
    print(f"Accessing numbers[10]...")
    value = numbers[10]
except IndexError as e:
    print(f"Caught IndexError: {e}")
    print(f"Exception type: {type(e).__name__}")

try:
    result = int("not a number")
except ValueError as e:
    print(f"\\nCaught ValueError: {e}")
    print(f"Exception type: {type(e).__name__}")
print()

# Example 3: Multiple Except Blocks
print("="*70)
print("Example 3: Handling Different Exception Types")
print("="*70)

def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"  Error: Cannot divide {a} by zero")
        return None
    except TypeError:
        print(f"  Error: Invalid types for division: {type(a).__name__}, {type(b).__name__}")
        return None

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / '2' = {safe_divide(10, '2')}")
print()

# Example 4: Catching Multiple Exceptions
print("="*70)
print("Example 4: Single Except for Multiple Exception Types")
print("="*70)

def process_data(data, index):
    """Process data element at index"""
    try:
        value = int(data[index])
        return value * 2
    except (IndexError, ValueError, TypeError) as e:
        print(f"  Processing error: {type(e).__name__} - {e}")
        return None

data = ["10", "20", "thirty", "40"]

print(f"Process index 0: {process_data(data, 0)}")
print(f"Process index 2: {process_data(data, 2)}")  # ValueError
print(f"Process index 10: {process_data(data, 10)}")  # IndexError
print()

# Example 5: Try-Except-Else
print("="*70)
print("Example 5: Using Else Clause")
print("="*70)

def read_number(text):
    """Convert text to number"""
    try:
        number = int(text)
    except ValueError:
        print(f"  '{text}' is not a valid number")
    else:
        # Executes only if no exception occurred
        print(f"  Successfully converted '{text}' to {number}")
        return number

read_number("42")
read_number("hello")
read_number("100")
print()

# Example 6: Try-Except-Finally
print("="*70)
print("Example 6: Using Finally Clause")
print("="*70)

def process_file(filename):
    """Process file with guaranteed cleanup"""
    file = None
    try:
        print(f"  Opening {filename}...")
        file = open(filename, 'r')
        data = file.read()
        print(f"  Read {len(data)} characters")
        return data
    except FileNotFoundError:
        print(f"  Error: {filename} not found")
        return None
    finally:
        # Always executes, even if exception occurred
        if file:
            file.close()
            print(f"  File closed")
        else:
            print(f"  No file to close")

process_file("nonexistent.txt")
print()

# Create a test file
with open("test.txt", "w") as f:
    f.write("Hello, World!")

process_file("test.txt")
print()

# Example 7: Nested Try-Except
print("="*70)
print("Example 7: Nested Exception Handling")
print("="*70)

def complex_operation(data):
    """Perform operation with nested error handling"""
    try:
        print(f"  Processing: {data}")

        # Outer try block
        try:
            # Inner operation that might fail
            value = int(data)
            result = 100 / value
            print(f"    Result: {result}")
        except ValueError:
            print(f"    Inner error: Invalid number format")
            raise  # Re-raise to outer handler

    except ZeroDivisionError:
        print(f"    Outer error: Division by zero")
    except ValueError:
        print(f"    Outer error: Could not convert to number")

complex_operation("50")
complex_operation("0")
complex_operation("abc")
print()

# Example 8: Try-Except in Loops
print("="*70)
print("Example 8: Exception Handling in Loops")
print("="*70)

data = ["10", "20", "invalid", "30", "0", "40"]

print("Processing data with exception handling:")
results = []

for item in data:
    try:
        # Try to process each item
        number = int(item)
        result = 100 / number
        results.append(result)
        print(f"  {item}: {result:.2f}")
    except ValueError:
        print(f"  {item}: Skipped (invalid format)")
    except ZeroDivisionError:
        print(f"  {item}: Skipped (zero division)")
    # Loop continues even after exception

print(f"\\nSuccessfully processed {len(results)} items")
print()

# Example 9: Generic Exception Handling
print("="*70)
print("Example 9: Catching All Exceptions")
print("="*70)

def risky_operation(value):
    """Operation that might fail in various ways"""
    try:
        # Various operations that might fail
        if value < 0:
            raise ValueError("Negative value")
        if value == 0:
            return 100 / value
        if value > 100:
            return [][value]  # IndexError
        return value * 2

    except ValueError as e:
        print(f"  ValueError: {e}")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: Division by zero")
    except Exception as e:
        # Catch-all for any other exception
        print(f"  Unexpected error: {type(e).__name__} - {e}")

risky_operation(50)
risky_operation(-10)
risky_operation(0)
risky_operation(200)
print()

# Example 10: Practical Application - Data Processor
print("="*70)
print("Example 10: Real-World Use Case - Robust Data Processor")
print("="*70)

class DataProcessor:
    """Process data with comprehensive error handling"""

    def __init__(self):
        self.processed = []
        self.errors = []

    def process_record(self, record, record_num):
        """Process a single record"""
        try:
            # Validate record structure
            if not isinstance(record, dict):
                raise TypeError(f"Record must be dict, got {type(record).__name__}")

            # Extract fields
            name = record["name"]
            age = int(record["age"])
            score = float(record["score"])

            # Validate values
            if age < 0 or age > 120:
                raise ValueError(f"Invalid age: {age}")

            if score < 0 or score > 100:
                raise ValueError(f"Invalid score: {score}")

            # Process successfully
            result = {
                "name": name,
                "age": age,
                "score": score,
                "grade": self._calculate_grade(score)
            }

            self.processed.append(result)
            print(f"  Record {record_num}: {name} - PROCESSED")
            return result

        except KeyError as e:
            error = f"Record {record_num}: Missing field {e}"
            print(f"  {error}")
            self.errors.append({"record": record_num, "error": error})

        except ValueError as e:
            error = f"Record {record_num}: Invalid value - {e}"
            print(f"  {error}")
            self.errors.append({"record": record_num, "error": error})

        except TypeError as e:
            error = f"Record {record_num}: Type error - {e}"
            print(f"  {error}")
            self.errors.append({"record": record_num, "error": error})

        except Exception as e:
            error = f"Record {record_num}: Unexpected error - {type(e).__name__}: {e}"
            print(f"  {error}")
            self.errors.append({"record": record_num, "error": error})

        return None

    def _calculate_grade(self, score):
        """Calculate letter grade from score"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def process_all(self, records):
        """Process all records"""
        print("Processing records:")
        print("-" * 70)

        for i, record in enumerate(records, start=1):
            self.process_record(record, i)

        print("-" * 70)

    def summary(self):
        """Print processing summary"""
        print("\\nPROCESSING SUMMARY")
        print("=" * 70)
        print(f"Total records: {len(self.processed) + len(self.errors)}")
        print(f"Successfully processed: {len(self.processed)}")
        print(f"Errors: {len(self.errors)}")

        if self.processed:
            print("\\nProcessed records:")
            for record in self.processed:
                print(f"  {record['name']:15} Age: {record['age']:>3}  Score: {record['score']:>5.1f}  Grade: {record['grade']}")

        if self.errors:
            print("\\nError details:")
            for error in self.errors:
                print(f"  {error['error']}")

# Test data processor
processor = DataProcessor()

test_records = [
    {"name": "Alice", "age": "25", "score": "95.5"},      # Valid
    {"name": "Bob", "age": "invalid", "score": "87.0"},   # Invalid age
    {"name": "Charlie", "score": "92.0"},                  # Missing age
    {"name": "David", "age": "30", "score": "78.5"},      # Valid
    "Invalid record",                                      # Wrong type
    {"name": "Eve", "age": "28", "score": "150"},         # Invalid score
    {"name": "Frank", "age": "35", "score": "88.0"},      # Valid
]

processor.process_all(test_records)
processor.summary()

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. try-except catches and handles exceptions")
print("2. Use specific exception types when possible")
print("3. except ExceptionType as e - Capture exception details")
print("4. Multiple except blocks for different errors")
print("5. except (Type1, Type2) - Handle multiple types together")
print("6. else clause runs if no exception occurred")
print("7. finally clause always runs (cleanup code)")
print("8. Nested try-except for complex error handling")
print("9. Continue execution after handling exception")
print("10. Log errors for debugging and monitoring")
print("="*70)
'''

# Upgrade Lesson 158: Try/Except (Alternative)
lesson158['fullSolution'] = lesson157['fullSolution']  # Similar content, use same comprehensive solution

# Upgrade Lesson 159: TypeError Handling
lesson159['fullSolution'] = '''"""
TypeError Handling

Master TypeError exception handling in Python. Learn to handle type mismatches,
validate function arguments, implement type checking, and create type-safe
functions. Essential for robust Python code.

**Zero Package Installation Required**
"""

# Example 1: Understanding TypeError
print("="*70)
print("Example 1: What Causes TypeError")
print("="*70)

# Type mismatch in operations
try:
    result = "10" + 5
except TypeError as e:
    print(f"TypeError: {e}")

# Type mismatch in function calls
try:
    result = len(123)
except TypeError as e:
    print(f"TypeError: {e}")

# Incorrect number of arguments
try:
    result = int("10", "20", "30")
except TypeError as e:
    print(f"TypeError: {e}")
print()

# Example 2: Handling TypeError in Functions
print("="*70)
print("Example 2: Safe Type Handling in Functions")
print("="*70)

def safe_add(a, b):
    """Safely add two values"""
    try:
        return a + b
    except TypeError as e:
        print(f"  Cannot add {type(a).__name__} and {type(b).__name__}: {e}")
        return None

print(f"5 + 10 = {safe_add(5, 10)}")
print(f"'hello' + ' world' = {safe_add('hello', ' world')}")
print(f"5 + 'hello' = {safe_add(5, 'hello')}")
print(f"[1, 2] + [3, 4] = {safe_add([1, 2], [3, 4])}")
print(f"5 + None = {safe_add(5, None)}")
print()

# Example 3: Type Validation
print("="*70)
print("Example 3: Explicit Type Checking")
print("="*70)

def multiply(a, b):
    """Multiply two numbers with type checking"""
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be numeric, got {type(a).__name__}")

    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be numeric, got {type(b).__name__}")

    return a * b

# Valid calls
try:
    print(f"5 * 10 = {multiply(5, 10)}")
    print(f"2.5 * 4 = {multiply(2.5, 4)}")
except TypeError as e:
    print(f"Error: {e}")

# Invalid calls
try:
    result = multiply("5", 10)
except TypeError as e:
    print(f"Error: {e}")

try:
    result = multiply(5, [1, 2, 3])
except TypeError as e:
    print(f"Error: {e}")
print()

# Example 4: TypeError with Containers
print("="*70)
print("Example 4: TypeError in Container Operations")
print("="*70)

def safe_index(container, item):
    """Safely find index of item"""
    try:
        index = container.index(item)
        print(f"  Found '{item}' at index {index}")
        return index
    except TypeError as e:
        print(f"  TypeError: {e}")
        print(f"  Container type {type(container).__name__} doesn't support indexing")
        return None
    except ValueError:
        print(f"  Item '{item}' not found in container")
        return None

safe_index([1, 2, 3, 4], 3)
safe_index("hello", "l")
safe_index(123, 2)  # TypeError: integers don't have index method
print()

# Example 5: TypeError with Unpacking
print("="*70)
print("Example 5: TypeError in Sequence Unpacking")
print("="*70)

def safe_unpack(data):
    """Safely unpack data"""
    try:
        a, b, c = data
        print(f"  Unpacked: a={a}, b={b}, c={c}")
        return (a, b, c)
    except TypeError as e:
        print(f"  Cannot unpack {type(data).__name__}: {e}")
        return None
    except ValueError as e:
        print(f"  Wrong number of values: {e}")
        return None

safe_unpack([1, 2, 3])
safe_unpack("abc")
safe_unpack(123)  # TypeError: int is not iterable
safe_unpack([1, 2])  # ValueError: not enough values
print()

# Example 6: TypeError with String Formatting
print("="*70)
print("Example 6: TypeError in String Operations")
print("="*70)

def format_message(template, value):
    """Format message with type handling"""
    try:
        message = template % value
        print(f"  Formatted: {message}")
        return message
    except TypeError as e:
        print(f"  Format error: {e}")
        # Try alternative formatting
        try:
            message = str(template) + " " + str(value)
            print(f"  Fallback: {message}")
            return message
        except:
            return None

format_message("Value is %d", 42)
format_message("Value is %s", "hello")
format_message("Value is %d", "not a number")  # TypeError
print()

# Example 7: TypeError with Comparisons
print("="*70)
print("Example 7: TypeError in Comparisons")
print("="*70)

def safe_compare(a, b):
    """Safely compare two values"""
    try:
        if a < b:
            result = f"{a} < {b}"
        elif a > b:
            result = f"{a} > {b}"
        else:
            result = f"{a} == {b}"
        print(f"  {result}")
        return result
    except TypeError as e:
        print(f"  Cannot compare {type(a).__name__} and {type(b).__name__}: {e}")
        return None

safe_compare(5, 10)
safe_compare("apple", "banana")
safe_compare(5, "hello")  # TypeError: can't compare int and str
safe_compare([1, 2], {"a": 1})  # TypeError: can't compare list and dict
print()

# Example 8: TypeError with Dictionary Operations
print("="*70)
print("Example 8: TypeError in Dictionary Operations")
print("="*70)

def safe_dict_get(data, key):
    """Safely get value from dict-like object"""
    try:
        value = data[key]
        print(f"  data[{key}] = {value}")
        return value
    except TypeError as e:
        print(f"  TypeError: {type(data).__name__} is not subscriptable - {e}")
        return None
    except KeyError:
        print(f"  Key {key} not found")
        return None

safe_dict_get({"a": 1, "b": 2}, "a")
safe_dict_get([10, 20, 30], 1)
safe_dict_get("hello", 0)
safe_dict_get(123, "key")  # TypeError: int is not subscriptable
print()

# Example 9: TypeError with JSON Operations
print("="*70)
print("Example 9: TypeError in JSON Serialization")
print("="*70)

import json

def safe_json_dumps(data):
    """Safely serialize to JSON"""
    try:
        json_str = json.dumps(data)
        print(f"  JSON: {json_str}")
        return json_str
    except TypeError as e:
        print(f"  Cannot serialize {type(data).__name__} to JSON: {e}")
        # Try converting to string representation
        try:
            json_str = json.dumps(str(data))
            print(f"  Converted to string: {json_str}")
            return json_str
        except:
            return None

safe_json_dumps({"name": "Alice", "age": 30})
safe_json_dumps([1, 2, 3, 4])
safe_json_dumps("hello")

# Complex object that's not JSON serializable
class Person:
    def __init__(self, name):
        self.name = name

safe_json_dumps(Person("Bob"))
print()

# Example 10: Practical Application - Type-Safe Calculator
print("="*70)
print("Example 10: Real-World Use Case - Type-Safe Calculator")
print("="*70)

class TypeSafeCalculator:
    """Calculator with comprehensive type checking"""

    def __init__(self):
        self.history = []

    def _validate_numeric(self, value, name="value"):
        """Validate that value is numeric"""
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"{name} must be int or float, got {type(value).__name__}"
            )

        if isinstance(value, bool):
            raise TypeError(
                f"{name} cannot be bool (even though bool is subclass of int)"
            )

    def add(self, a, b):
        """Add two numbers"""
        try:
            self._validate_numeric(a, "first argument")
            self._validate_numeric(b, "second argument")

            result = a + b
            self.history.append(f"{a} + {b} = {result}")
            print(f"  {a} + {b} = {result}")
            return result

        except TypeError as e:
            print(f"  Addition error: {e}")
            self.history.append(f"ERROR: {e}")
            return None

    def divide(self, a, b):
        """Divide two numbers"""
        try:
            self._validate_numeric(a, "dividend")
            self._validate_numeric(b, "divisor")

            if b == 0:
                raise ValueError("Cannot divide by zero")

            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            print(f"  {a} / {b} = {result}")
            return result

        except TypeError as e:
            print(f"  Division error: {e}")
            self.history.append(f"ERROR: {e}")
            return None
        except ValueError as e:
            print(f"  Division error: {e}")
            self.history.append(f"ERROR: {e}")
            return None

    def power(self, base, exponent):
        """Raise base to exponent"""
        try:
            self._validate_numeric(base, "base")
            self._validate_numeric(exponent, "exponent")

            result = base ** exponent
            self.history.append(f"{base} ** {exponent} = {result}")
            print(f"  {base} ** {exponent} = {result}")
            return result

        except TypeError as e:
            print(f"  Power error: {e}")
            self.history.append(f"ERROR: {e}")
            return None

    def average(self, *numbers):
        """Calculate average of numbers"""
        try:
            if not numbers:
                raise ValueError("Need at least one number")

            # Validate all arguments
            for i, num in enumerate(numbers):
                self._validate_numeric(num, f"argument {i+1}")

            result = sum(numbers) / len(numbers)
            nums_str = ", ".join(str(n) for n in numbers)
            self.history.append(f"average({nums_str}) = {result}")
            print(f"  average({nums_str}) = {result}")
            return result

        except TypeError as e:
            print(f"  Average error: {e}")
            self.history.append(f"ERROR: {e}")
            return None
        except ValueError as e:
            print(f"  Average error: {e}")
            self.history.append(f"ERROR: {e}")
            return None

    def show_history(self):
        """Display calculation history"""
        print("\\nCalculation History:")
        print("=" * 70)
        for i, entry in enumerate(self.history, start=1):
            print(f"  {i}. {entry}")

# Test type-safe calculator
calc = TypeSafeCalculator()

print("Valid operations:")
print("-" * 70)
calc.add(10, 20)
calc.divide(100, 4)
calc.power(2, 8)
calc.average(10, 20, 30, 40, 50)

print("\\nInvalid operations (TypeError):")
print("-" * 70)
calc.add("10", 20)
calc.divide(100, "4")
calc.power(2, [1, 2, 3])
calc.average(10, 20, "30", 40)
calc.add(True, False)  # Bools are technically ints, but we reject them

# Show all calculations
calc.show_history()

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. TypeError occurs with incompatible types in operations")
print("2. Use isinstance() for type validation")
print("3. Validate types before operations")
print("4. Handle TypeError separately from other exceptions")
print("5. Provide clear error messages about type mismatches")
print("6. Consider type conversion as fallback strategy")
print("7. TypeError common in: +, -, *, /, [], (), etc.")
print("8. Check for None before operations")
print("9. Use type hints for better code documentation")
print("10. Test with various types to ensure robustness")
print("="*70)
'''

# Upgrade Lesson 160: ValueError Handling
lesson160['fullSolution'] = '''"""
ValueError Handling

Master ValueError exception handling in Python. Learn to handle invalid values,
validate data ranges, implement input validation, and create robust functions
that handle invalid arguments gracefully.

**Zero Package Installation Required**
"""

# Example 1: Understanding ValueError
print("="*70)
print("Example 1: What Causes ValueError")
print("="*70)

# Invalid conversion
try:
    number = int("not a number")
except ValueError as e:
    print(f"ValueError: {e}")

# Invalid base in conversion
try:
    number = int("10", 100)  # Base must be 0 or 2-36
except ValueError as e:
    print(f"ValueError: {e}")

# Invalid unpacking
try:
    a, b, c = [1, 2]  # Too few values
except ValueError as e:
    print(f"ValueError: {e}")
print()

# Example 2: Handling String to Number Conversion
print("="*70)
print("Example 2: Safe String to Number Conversion")
print("="*70)

def safe_int(value, default=0):
    """Safely convert value to integer"""
    try:
        return int(value)
    except ValueError as e:
        print(f"  Cannot convert '{value}' to int: {e}")
        return default

print(f"safe_int('42'): {safe_int('42')}")
print(f"safe_int('3.14'): {safe_int('3.14')}")
print(f"safe_int('hello'): {safe_int('hello')}")
print(f"safe_int('', -1): {safe_int('', -1)}")
print()

# Example 3: ValueError in List Methods
print("="*70)
print("Example 3: ValueError with List Operations")
print("="*70)

def safe_remove(lst, item):
    """Safely remove item from list"""
    try:
        lst.remove(item)
        print(f"  Removed '{item}' from list")
        return True
    except ValueError:
        print(f"  Item '{item}' not found in list")
        return False

numbers = [1, 2, 3, 4, 5]
print(f"List: {numbers}")

safe_remove(numbers, 3)
print(f"After remove: {numbers}")

safe_remove(numbers, 10)
print(f"After failed remove: {numbers}")
print()

# Example 4: ValueError in Range Validation
print("="*70)
print("Example 4: Validating Value Ranges")
print("="*70)

def set_age(age):
    """Set age with validation"""
    try:
        age_int = int(age)

        if age_int < 0:
            raise ValueError(f"Age cannot be negative: {age_int}")

        if age_int > 150:
            raise ValueError(f"Age is unrealistically high: {age_int}")

        print(f"  Age set to: {age_int}")
        return age_int

    except ValueError as e:
        print(f"  Invalid age: {e}")
        return None

set_age(25)
set_age(-5)
set_age(200)
set_age("thirty")
print()

# Example 5: ValueError in Date/Time Parsing
print("="*70)
print("Example 5: ValueError in Date Parsing")
print("="*70)

import datetime

def parse_date(date_string):
    """Parse date string to datetime object"""
    try:
        # Try format: YYYY-MM-DD
        date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        print(f"  Parsed date: {date.strftime('%B %d, %Y')}")
        return date
    except ValueError as e:
        print(f"  Invalid date format '{date_string}': {e}")

        # Try alternative format: MM/DD/YYYY
        try:
            date = datetime.datetime.strptime(date_string, "%m/%d/%Y")
            print(f"  Parsed with alternative format: {date.strftime('%B %d, %Y')}")
            return date
        except ValueError:
            print(f"  Could not parse date '{date_string}' with any known format")
            return None

parse_date("2024-03-15")
parse_date("03/15/2024")
parse_date("2024-13-45")  # Invalid month and day
parse_date("not a date")
print()

# Example 6: ValueError with Math Operations
print("="*70)
print("Example 6: ValueError in Math Domain Errors")
print("="*70)

import math

def safe_sqrt(value):
    """Safely calculate square root"""
    try:
        result = math.sqrt(value)
        print(f"  sqrt({value}) = {result}")
        return result
    except ValueError as e:
        print(f"  Cannot calculate sqrt({value}): {e}")
        return None
    except TypeError as e:
        print(f"  Invalid type for sqrt: {e}")
        return None

safe_sqrt(16)
safe_sqrt(25.5)
safe_sqrt(-4)  # ValueError: negative number
safe_sqrt("16")  # TypeError: string not accepted
print()

# Example 7: ValueError in Data Validation
print("="*70)
print("Example 7: Multi-Field Data Validation")
print("="*70)

def validate_score(score):
    """Validate score is in valid range"""
    try:
        score_float = float(score)

        if score_float < 0:
            raise ValueError(f"Score cannot be negative: {score_float}")

        if score_float > 100:
            raise ValueError(f"Score cannot exceed 100: {score_float}")

        print(f"  Valid score: {score_float}")
        return score_float

    except ValueError as e:
        print(f"  Invalid score: {e}")
        return None

validate_score(85.5)
validate_score(-10)
validate_score(105)
validate_score("ninety")
print()

# Example 8: ValueError with String Methods
print("="*70)
print("Example 8: ValueError in String Operations")
print("="*70)

def safe_split(text, delimiter, expected_parts):
    """Safely split string and validate part count"""
    try:
        parts = text.split(delimiter)

        if len(parts) != expected_parts:
            raise ValueError(
                f"Expected {expected_parts} parts, got {len(parts)}: {parts}"
            )

        print(f"  Split '{text}' into {len(parts)} parts: {parts}")
        return parts

    except ValueError as e:
        print(f"  Split error: {e}")
        return None

safe_split("a,b,c", ",", 3)
safe_split("a,b,c,d", ",", 3)
safe_split("a-b-c", ",", 3)
print()

# Example 9: ValueError Recovery Strategies
print("="*70)
print("Example 9: Different Recovery Strategies")
print("="*70)

def parse_number_with_fallback(text):
    """Try multiple parsing strategies"""
    # Strategy 1: Try as int
    try:
        return int(text)
    except ValueError:
        print(f"  Not an integer: '{text}'")

    # Strategy 2: Try as float
    try:
        return float(text)
    except ValueError:
        print(f"  Not a float: '{text}'")

    # Strategy 3: Try removing common formatting
    try:
        cleaned = text.replace(',', '').replace('$', '').strip()
        return float(cleaned)
    except ValueError:
        print(f"  Cannot parse even after cleaning: '{text}'")

    # Strategy 4: Return None
    return None

print(f"'42': {parse_number_with_fallback('42')}")
print(f"'3.14': {parse_number_with_fallback('3.14')}")
print(f"'$1,234.56': {parse_number_with_fallback('$1,234.56')}")
print(f"'hello': {parse_number_with_fallback('hello')}")
print()

# Example 10: Practical Application - Form Validator
print("="*70)
print("Example 10: Real-World Use Case - Robust Form Validator")
print("="*70)

class FormValidator:
    """Validate form data with comprehensive error handling"""

    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        """Validate email format"""
        try:
            if not email:
                raise ValueError("Email cannot be empty")

            if '@' not in email:
                raise ValueError(f"Email missing @ symbol: {email}")

            parts = email.split('@')
            if len(parts) != 2:
                raise ValueError(f"Email has multiple @ symbols: {email}")

            if not parts[0] or not parts[1]:
                raise ValueError(f"Email has empty parts: {email}")

            print(f"  Email valid: {email}")
            return True

        except ValueError as e:
            print(f"  Email validation error: {e}")
            self.errors.append(str(e))
            return False

    def validate_age(self, age):
        """Validate age value"""
        try:
            age_int = int(age)

            if age_int < 0:
                raise ValueError(f"Age cannot be negative: {age_int}")

            if age_int > 120:
                raise ValueError(f"Age unrealistic: {age_int}")

            if age_int < 18:
                raise ValueError(f"Must be 18 or older: {age_int}")

            print(f"  Age valid: {age_int}")
            return True

        except ValueError as e:
            print(f"  Age validation error: {e}")
            self.errors.append(str(e))
            return False

    def validate_phone(self, phone):
        """Validate phone number format"""
        try:
            # Remove common formatting
            cleaned = phone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')

            # Check if all digits
            if not cleaned.isdigit():
                raise ValueError(f"Phone must contain only digits: {phone}")

            # Check length (US format)
            if len(cleaned) != 10:
                raise ValueError(f"Phone must be 10 digits, got {len(cleaned)}: {phone}")

            formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
            print(f"  Phone valid: {formatted}")
            return True

        except ValueError as e:
            print(f"  Phone validation error: {e}")
            self.errors.append(str(e))
            return False

    def validate_zip_code(self, zip_code):
        """Validate ZIP code"""
        try:
            # Remove dash if present
            cleaned = zip_code.replace('-', '')

            # Check if all digits
            if not cleaned.isdigit():
                raise ValueError(f"ZIP code must be numeric: {zip_code}")

            # Check length
            if len(cleaned) not in [5, 9]:
                raise ValueError(f"ZIP code must be 5 or 9 digits: {zip_code}")

            print(f"  ZIP code valid: {zip_code}")
            return True

        except ValueError as e:
            print(f"  ZIP code validation error: {e}")
            self.errors.append(str(e))
            return False

    def validate_form(self, email, age, phone, zip_code):
        """Validate entire form"""
        print("Validating form data:")
        print("-" * 70)

        self.errors = []  # Reset errors

        email_valid = self.validate_email(email)
        age_valid = self.validate_age(age)
        phone_valid = self.validate_phone(phone)
        zip_valid = self.validate_zip_code(zip_code)

        print("-" * 70)

        if all([email_valid, age_valid, phone_valid, zip_valid]):
            print("Form validation: PASSED")
            return True
        else:
            print(f"Form validation: FAILED ({len(self.errors)} errors)")
            return False

# Test form validator
validator = FormValidator()

# Test case 1: Valid form
print("Test 1: Valid form data")
print("=" * 70)
validator.validate_form(
    email="john@example.com",
    age="25",
    phone="555-123-4567",
    zip_code="12345"
)

# Test case 2: Invalid form
print("\\nTest 2: Invalid form data")
print("=" * 70)
validator.validate_form(
    email="invalid-email",
    age="15",
    phone="123",
    zip_code="abcd"
)

# Test case 3: Mixed valid/invalid
print("\\nTest 3: Mixed form data")
print("=" * 70)
validator.validate_form(
    email="alice@test.com",
    age="thirty",
    phone="(555) 987-6543",
    zip_code="12345-6789"
)

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. ValueError occurs when value is wrong type but correct form")
print("2. int() and float() raise ValueError for invalid strings")
print("3. list.remove() raises ValueError if item not found")
print("4. Validate ranges before operations")
print("5. Use try-except for conversion operations")
print("6. Provide clear error messages about invalid values")
print("7. Consider multiple parsing strategies as fallback")
print("8. datetime parsing commonly raises ValueError")
print("9. math operations raise ValueError for invalid domains")
print("10. Validate early and provide user-friendly errors")
print("="*70)
'''

# Save all upgrades
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\nUpgraded lessons 151-160:")
print(f"  151: Writing Text Files - {len(lesson151['fullSolution'])} chars")
print(f"  152: Dead Letter Queues - {len(lesson152['fullSolution'])} chars")
print(f"  153: IndexError Handling - {len(lesson153['fullSolution'])} chars")
print(f"  154: KeyError Handling - {len(lesson154['fullSolution'])} chars")
print(f"  155: Raise Exceptions - {len(lesson155['fullSolution'])} chars")
print(f"  156: Raising Exceptions - {len(lesson156['fullSolution'])} chars")
print(f"  157: Try-Except Basics - {len(lesson157['fullSolution'])} chars")
print(f"  158: Try/Except - {len(lesson158['fullSolution'])} chars")
print(f"  159: TypeError Handling - {len(lesson159['fullSolution'])} chars")
print(f"  160: ValueError Handling - {len(lesson160['fullSolution'])} chars")
print("\nBatch 151-160: All lessons upgraded successfully!")
