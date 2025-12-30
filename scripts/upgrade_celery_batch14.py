#!/usr/bin/env python3
"""
Upgrade Celery lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 14: Celery Task Chains and Task Groups
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 818: Celery Task Chains
    lesson_818 = next(l for l in lessons if l['id'] == 818)
    lesson_818['fullSolution'] = '''# Celery Task Chains - Complete Simulation
# In production: pip install celery redis
# This lesson simulates Celery task workflows with chains, callbacks, and error handling

import time
import uuid
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class TaskState(Enum):
    """Task execution states."""
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

@dataclass
class TaskResult:
    """Task execution result."""
    task_id: str
    state: TaskState
    result: Any = None
    error: Optional[str] = None

class Task:
    """Task definition with chaining support."""

    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def apply_async(self, args: tuple = (), kwargs: dict = None, link: 'Task' = None, link_error: 'Task' = None):
        """
        Execute task asynchronously with callbacks.

        Parameters:
        - link: Task to call on success (receives result as first arg)
        - link_error: Task to call on failure (receives exception)
        """
        kwargs = kwargs or {}
        task_id = str(uuid.uuid4())

        message = {
            "id": task_id,
            "task": self.name,
            "args": args,
            "kwargs": kwargs,
            "link": link,
            "link_error": link_error
        }

        broker.publish(message)
        return AsyncResult(task_id)

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async."""
        return self.apply_async(args=args, kwargs=kwargs)

    def __or__(self, other: 'Task') -> 'Chain':
        """
        Pipe operator for chaining: task1 | task2

        Example:
        chain = download | process | upload
        """
        return Chain([self, other])

    def __call__(self, *args, **kwargs):
        """Execute synchronously."""
        return self.func(*args, **kwargs)

class Chain:
    """
    Task chain - execute tasks sequentially.

    Each task receives the result of the previous task as input.

    Example:
    chain = download_file.s() | process_data.s() | upload_result.s()
    chain.apply_async()
    """

    def __init__(self, tasks: List[Task]):
        self.tasks = tasks
        self.task_id = str(uuid.uuid4())

    def __or__(self, other):
        """Add another task to chain."""
        if isinstance(other, Task):
            self.tasks.append(other)
        elif isinstance(other, Chain):
            self.tasks.extend(other.tasks)
        return self

    def apply_async(self, args: tuple = (), kwargs: dict = None):
        """Execute chain asynchronously."""
        kwargs = kwargs or {}

        message = {
            "id": self.task_id,
            "type": "chain",
            "tasks": self.tasks,
            "args": args,
            "kwargs": kwargs
        }

        broker.publish(message)
        return AsyncResult(self.task_id)

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async."""
        return self.apply_async(args=args, kwargs=kwargs)

class AsyncResult:
    """Represents async task result."""

    def __init__(self, task_id: str):
        self.task_id = task_id

    def get(self, timeout: float = None) -> Any:
        """Wait for result."""
        start = time.time()

        while True:
            result = result_backend.get(self.task_id)

            if result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]:
                if result.state == TaskState.FAILURE:
                    raise Exception(f"Task failed: {result.error}")
                return result.result

            if timeout and (time.time() - start) > timeout:
                raise TimeoutError("Task did not complete in time")

            time.sleep(0.1)

    def ready(self) -> bool:
        """Check if complete."""
        result = result_backend.get(self.task_id)
        return result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]

class SimpleBroker:
    """Message broker."""

    def __init__(self):
        self.queue: List[Dict] = []

    def publish(self, message: Dict):
        """Publish task."""
        self.queue.append(message)
        print(f"[BROKER] Queued: {message.get('task', 'chain')}")

    def consume(self) -> Optional[Dict]:
        """Consume task."""
        return self.queue.pop(0) if self.queue else None

class ResultBackend:
    """Result storage."""

    def __init__(self):
        self.results: Dict[str, TaskResult] = {}

    def store(self, task_id: str, state: TaskState, result: Any = None, error: str = None):
        """Store result."""
        self.results[task_id] = TaskResult(
            task_id=task_id,
            state=state,
            result=result,
            error=error
        )

    def get(self, task_id: str) -> Optional[TaskResult]:
        """Get result."""
        return self.results.get(task_id)

class Worker:
    """Worker that executes tasks and chains."""

    def __init__(self, broker, backend):
        self.broker = broker
        self.backend = backend
        self.tasks: Dict[str, Task] = {}

    def register_task(self, task: Task):
        """Register task."""
        self.tasks[task.name] = task

    def start(self, num_messages: int = None):
        """Process messages."""
        processed = 0

        while True:
            if num_messages and processed >= num_messages:
                break

            message = self.broker.consume()
            if not message:
                break

            if message.get("type") == "chain":
                self._execute_chain(message)
            else:
                self._execute_task(message)

            processed += 1

    def _execute_task(self, message: Dict):
        """Execute single task."""
        task_id = message["id"]
        task_name = message["task"]
        args = message["args"]
        kwargs = message["kwargs"]
        link = message.get("link")
        link_error = message.get("link_error")

        task = self.tasks.get(task_name)
        if not task:
            self.backend.store(task_id, TaskState.FAILURE, error=f"Task {task_name} not found")
            return

        self.backend.store(task_id, TaskState.STARTED)
        print(f"[WORKER] Executing: {task_name}")

        try:
            result = task.func(*args, **kwargs)
            self.backend.store(task_id, TaskState.SUCCESS, result=result)
            print(f"[WORKER] Success: {task_name} -> {result}")

            # Execute linked task on success
            if link:
                print(f"[WORKER] Triggering success callback")
                link.apply_async(args=(result,))

        except Exception as e:
            self.backend.store(task_id, TaskState.FAILURE, error=str(e))
            print(f"[WORKER] Failure: {task_name} -> {e}")

            # Execute error callback
            if link_error:
                print(f"[WORKER] Triggering error callback")
                link_error.apply_async(args=(str(e),))

    def _execute_chain(self, message: Dict):
        """Execute task chain."""
        chain_id = message["id"]
        tasks = message["tasks"]
        args = message["args"]
        kwargs = message["kwargs"]

        print(f"[WORKER] Executing chain: {len(tasks)} tasks")

        result = None
        try:
            for i, task in enumerate(tasks):
                print(f"[WORKER] Chain step {i+1}/{len(tasks)}: {task.name}")

                # First task uses provided args, rest use previous result
                if i == 0:
                    result = task.func(*args, **kwargs)
                else:
                    # Pass previous result as first argument
                    result = task.func(result)

                print(f"[WORKER] Step {i+1} result: {result}")

            self.backend.store(chain_id, TaskState.SUCCESS, result=result)
            print(f"[WORKER] Chain complete: {result}")

        except Exception as e:
            self.backend.store(chain_id, TaskState.FAILURE, error=str(e))
            print(f"[WORKER] Chain failed at step {i+1}: {e}")

# Global instances
broker = SimpleBroker()
result_backend = ResultBackend()

class Celery:
    """Celery app."""

    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}

    def task(self):
        """Task decorator."""
        def decorator(func: Callable) -> Task:
            task_name = f"{self.name}.{func.__name__}"
            task = Task(task_name, func)
            self.tasks[task_name] = task
            return task
        return decorator

app = Celery("chain_app")

# Example 1: Basic Task Chain
print("Example 1: Basic Task Chain")
print("=" * 60)

@app.task()
def step1_download(url: str):
    """Step 1: Download data."""
    print(f"    Downloading from {url}...")
    time.sleep(0.1)
    return f"data_from_{url}"

@app.task()
def step2_process(data: str):
    """Step 2: Process data."""
    print(f"    Processing {data}...")
    time.sleep(0.1)
    return f"processed_{data}"

@app.task()
def step3_upload(data: str):
    """Step 3: Upload result."""
    print(f"    Uploading {data}...")
    time.sleep(0.1)
    return f"uploaded_{data}"

# Create chain using pipe operator
print("Creating chain: download | process | upload")
workflow = step1_download | step2_process | step3_upload

# Execute chain
print("\\nExecuting chain...")
result = workflow.apply_async(args=("http://example.com/data.csv",))

# Process chain
worker = Worker(broker, result_backend)
for task in app.tasks.values():
    worker.register_task(task)

worker.start(num_messages=1)

# Get final result
final_result = result.get(timeout=5)
print(f"\\nFinal result: {final_result}")
print()

# Example 2: Task with Callbacks (Link)
print("Example 2: Task with Callbacks (Success/Error Handlers)")
print("=" * 60)

@app.task()
def send_email(to: str, subject: str):
    """Send email."""
    print(f"    Sending email to {to}: {subject}")
    return f"Email sent to {to}"

@app.task()
def log_success(result: str):
    """Success callback."""
    print(f"    ✓ SUCCESS logged: {result}")
    return f"Success logged: {result}"

@app.task()
def log_error(error: str):
    """Error callback."""
    print(f"    ✗ ERROR logged: {error}")
    return f"Error logged: {error}"

# Task with success callback
print("Task with success callback:")
result = send_email.apply_async(
    args=("user@example.com", "Welcome!"),
    link=log_success
)

worker.start(num_messages=2)  # Process task + callback
print()

# Example 3: Error Handling in Chains
print("Example 3: Error Handling in Chains")
print("=" * 60)

@app.task()
def risky_step(data: str):
    """Task that may fail."""
    print(f"    Processing {data}...")

    if "bad" in data:
        raise ValueError(f"Invalid data: {data}")

    return f"processed_{data}"

@app.task()
def cleanup_on_error(error: str):
    """Cleanup on error."""
    print(f"    Cleaning up after error: {error}")
    return "Cleanup complete"

# Chain that will fail
print("Executing chain with failing task:")
failing_chain = step1_download | risky_step | step3_upload
result = failing_chain.apply_async(args=("http://example.com/bad_data.csv",))

try:
    worker.start(num_messages=1)
    result.get(timeout=5)
except Exception as e:
    print(f"\\nChain failed as expected: {e}")

print()

# Example 4: Data Transformation Pipeline
print("Example 4: Data Transformation Pipeline")
print("=" * 60)

@app.task()
def extract_data(source: str):
    """Extract data from source."""
    print(f"    Extracting from {source}...")
    return {"records": [1, 2, 3, 4, 5], "source": source}

@app.task()
def transform_data(data: dict):
    """Transform data."""
    print(f"    Transforming {len(data['records'])} records...")
    transformed = [x * 2 for x in data["records"]]
    return {"records": transformed, "source": data["source"]}

@app.task()
def load_data(data: dict):
    """Load data to destination."""
    print(f"    Loading {len(data['records'])} records to database...")
    return f"Loaded {len(data['records'])} records from {data['source']}"

# ETL pipeline
print("ETL Pipeline: Extract -> Transform -> Load")
etl_pipeline = extract_data | transform_data | load_data

result = etl_pipeline.apply_async(args=("api.example.com",))
worker.start(num_messages=1)

final_result = result.get(timeout=5)
print(f"\\nPipeline result: {final_result}")
print()

# Example 5: Complex Workflow with Branching
print("Example 5: Complex Workflow Simulation")
print("=" * 60)

@app.task()
def fetch_user_data(user_id: int):
    """Fetch user data."""
    print(f"    Fetching user {user_id}...")
    return {"id": user_id, "name": f"User{user_id}", "score": 85}

@app.task()
def calculate_rank(user_data: dict):
    """Calculate user rank."""
    print(f"    Calculating rank for {user_data['name']}...")
    rank = 100 - user_data["score"]
    return {**user_data, "rank": rank}

@app.task()
def generate_certificate(user_data: dict):
    """Generate certificate."""
    print(f"    Generating certificate for {user_data['name']} (Rank: {user_data['rank']})...")
    return f"Certificate for {user_data['name']}"

@app.task()
def send_notification(result: str):
    """Send notification."""
    print(f"    Sending notification: {result}")
    return f"Notification sent: {result}"

# Workflow: fetch -> rank -> certificate -> notify
print("Workflow: Fetch User -> Calculate Rank -> Generate Certificate -> Notify")
user_workflow = fetch_user_data | calculate_rank | generate_certificate | send_notification

result = user_workflow.apply_async(args=(1234,))
worker.start(num_messages=1)

final_result = result.get(timeout=5)
print(f"\\nWorkflow result: {final_result}")
print()

# Example 6: Partial Application (Signatures)
print("Example 6: Task Signatures (Partial Application)")
print("=" * 60)

@app.task()
def multiply(x: int, y: int):
    """Multiply two numbers."""
    print(f"    {x} * {y} = {x * y}")
    return x * y

@app.task()
def add(x: int, y: int):
    """Add two numbers."""
    print(f"    {x} + {y} = {x + y}")
    return x + y

# In real Celery, you'd use .s() for signatures
# Here we simulate with a simple chain

@app.task()
def double(x: int):
    """Double a number."""
    print(f"    {x} * 2 = {x * 2}")
    return x * 2

@app.task()
def square(x: int):
    """Square a number."""
    print(f"    {x}² = {x * x}")
    return x * x

# Chain: double -> square
print("Mathematical pipeline: double(5) -> square(result)")
math_chain = double | square

result = math_chain.apply_async(args=(5,))
worker.start(num_messages=1)

final_result = result.get(timeout=5)
print(f"\\nResult: double(5) -> square = {final_result}")
print(f"Verification: (5*2)² = 10² = 100")
print()

print("=" * 60)
print("TASK CHAINS BEST PRACTICES")
print("=" * 60)
print("""
CHAIN PATTERNS:

1. BASIC CHAIN (Sequential Execution):
   chain = task1.s() | task2.s() | task3.s()
   chain.apply_async()

   - Each task receives previous result
   - Fails if any task fails
   - Linear data flow

2. CALLBACKS (Success/Error Handlers):
   task.apply_async(
       link=success_handler.s(),
       link_error=error_handler.s()
   )

   - Execute on success/failure
   - Good for logging, cleanup
   - Don't affect main workflow

3. ETL PIPELINE:
   pipeline = extract | transform | load

   - Classic data processing pattern
   - Each stage transforms data
   - Idempotent operations recommended

4. ERROR HANDLING:
   chain = (
       fetch_data.s() |
       process.s() |
       save.s()
   ).on_error(cleanup.s())

   - Cleanup on failure
   - Retry failed steps
   - Graceful degradation

DESIGN PRINCIPLES:

1. SINGLE RESPONSIBILITY:
   ✓ Each task does one thing well
   ✗ Avoid monolithic tasks

2. IDEMPOTENCY:
   - Same input -> same output
   - Safe to retry
   - No side effects

3. SMALL DATA:
   - Pass IDs, not objects
   - Use references
   - Keep payloads < 1MB

4. ERROR RECOVERY:
   - Handle failures gracefully
   - Use error callbacks
   - Implement retries

COMMON PATTERNS:

1. Data Processing:
   download | validate | transform | load

2. User Workflow:
   register | send_email | activate_account

3. Report Generation:
   collect_data | analyze | generate_pdf | email_report

4. Image Processing:
   upload | resize | watermark | publish

5. Order Processing:
   validate_order | charge_payment | ship_items | send_confirmation

PERFORMANCE:

  - Keep tasks small (< 1 minute)
  - Avoid heavy computation in chains
  - Use groups for parallel work
  - Consider task priorities

MONITORING:

  - Log each step
  - Track chain progress
  - Alert on failures
  - Measure step durations

TESTING:

  # Test individual tasks
  result = task1("input")
  assert result == "expected"

  # Test chains
  chain = task1.s() | task2.s()
  result = chain.apply().get()

COMMON PITFALLS:

  ✗ Long chains (> 5 tasks)
  ✗ Large data in chain
  ✗ No error handling
  ✗ Non-idempotent tasks
  ✗ Missing timeouts

ALTERNATIVES:

  Chains: Sequential (A -> B -> C)
  Groups: Parallel (A + B + C)
  Chords: Parallel then reduce (A + B + C -> D)
  Maps: Apply to list (map(task, items))

Production note: Real Celery chains provide:
  - Automatic retry on failure
  - Task result expiration
  - Chain immutability
  - Signature objects (.s())
  - Advanced workflows (chord, map, starmap)
  - Result backend optimization
  - Chain introspection
  - Partial application
""")
'''

    # Lesson 819: Celery Task Groups
    lesson_819 = next(l for l in lessons if l['id'] == 819)
    lesson_819['fullSolution'] = '''# Celery Task Groups - Complete Simulation
# In production: pip install celery redis
# This lesson simulates Celery groups, chords, and parallel task execution

import time
import uuid
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import threading

class TaskState(Enum):
    """Task states."""
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

@dataclass
class TaskResult:
    """Task result."""
    task_id: str
    state: TaskState
    result: Any = None
    error: Optional[str] = None

class Task:
    """Task definition."""

    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def apply_async(self, args: tuple = (), kwargs: dict = None):
        """Execute async."""
        kwargs = kwargs or {}
        task_id = str(uuid.uuid4())

        message = {
            "id": task_id,
            "task": self.name,
            "args": args,
            "kwargs": kwargs
        }

        broker.publish(message)
        return AsyncResult(task_id)

    def delay(self, *args, **kwargs):
        """Shortcut."""
        return self.apply_async(args=args, kwargs=kwargs)

    def s(self, *args, **kwargs):
        """
        Create signature (partial application).

        Signature = task + arguments, ready to execute later.
        """
        return Signature(self, args, kwargs)

    def __call__(self, *args, **kwargs):
        """Execute synchronously."""
        return self.func(*args, **kwargs)

class Signature:
    """Task signature - task with bound arguments."""

    def __init__(self, task: Task, args: tuple, kwargs: dict):
        self.task = task
        self.args = args
        self.kwargs = kwargs

    def apply_async(self):
        """Execute signature."""
        return self.task.apply_async(self.args, self.kwargs)

    def delay(self):
        """Execute signature."""
        return self.apply_async()

class Group:
    """
    Execute tasks in parallel.

    Example:
    group = Group([
        task1.s(arg1),
        task2.s(arg2),
        task3.s(arg3)
    ])

    Results are returned as list in same order.
    """

    def __init__(self, signatures: List[Signature]):
        self.signatures = signatures
        self.group_id = str(uuid.uuid4())

    def apply_async(self):
        """Execute all tasks in parallel."""
        message = {
            "id": self.group_id,
            "type": "group",
            "signatures": self.signatures
        }

        broker.publish(message)
        return GroupResult(self.group_id, len(self.signatures))

    def delay(self):
        """Shortcut."""
        return self.apply_async()

class Chord:
    """
    Execute tasks in parallel, then callback with results.

    chord = chord([task1.s(), task2.s(), task3.s()])(callback.s())

    Callback receives list of results from group.
    """

    def __init__(self, group: Group):
        self.group = group
        self.chord_id = str(uuid.uuid4())

    def __call__(self, callback: Signature):
        """Set callback."""
        self.callback = callback

        message = {
            "id": self.chord_id,
            "type": "chord",
            "group": self.group,
            "callback": callback
        }

        broker.publish(message)
        return AsyncResult(self.chord_id)

class AsyncResult:
    """Single task result."""

    def __init__(self, task_id: str):
        self.task_id = task_id

    def get(self, timeout: float = None) -> Any:
        """Wait for result."""
        start = time.time()

        while True:
            result = result_backend.get(self.task_id)

            if result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]:
                if result.state == TaskState.FAILURE:
                    raise Exception(f"Task failed: {result.error}")
                return result.result

            if timeout and (time.time() - start) > timeout:
                raise TimeoutError()

            time.sleep(0.1)

    def ready(self) -> bool:
        """Check if ready."""
        result = result_backend.get(self.task_id)
        return result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]

class GroupResult:
    """Group result - multiple tasks."""

    def __init__(self, group_id: str, count: int):
        self.group_id = group_id
        self.count = count

    def get(self, timeout: float = None) -> List[Any]:
        """Wait for all results."""
        start = time.time()

        while True:
            result = result_backend.get(self.group_id)

            if result and result.state == TaskState.SUCCESS:
                return result.result

            if timeout and (time.time() - start) > timeout:
                raise TimeoutError()

            time.sleep(0.1)

    def ready(self) -> bool:
        """Check if all tasks complete."""
        result = result_backend.get(self.group_id)
        return result and result.state == TaskState.SUCCESS

class SimpleBroker:
    """Message broker."""

    def __init__(self):
        self.queue: List[Dict] = []

    def publish(self, message: Dict):
        """Publish message."""
        self.queue.append(message)
        msg_type = message.get("type", "task")
        print(f"[BROKER] Queued {msg_type}: {message.get('task', message['id'][:8])}")

    def consume(self) -> Optional[Dict]:
        """Consume message."""
        return self.queue.pop(0) if self.queue else None

class ResultBackend:
    """Result storage."""

    def __init__(self):
        self.results: Dict[str, TaskResult] = {}

    def store(self, task_id: str, state: TaskState, result: Any = None, error: str = None):
        """Store result."""
        self.results[task_id] = TaskResult(task_id, state, result, error)

    def get(self, task_id: str) -> Optional[TaskResult]:
        """Get result."""
        return self.results.get(task_id)

class Worker:
    """Worker for tasks, groups, and chords."""

    def __init__(self, broker, backend):
        self.broker = broker
        self.backend = backend
        self.tasks: Dict[str, Task] = {}

    def register_task(self, task: Task):
        """Register task."""
        self.tasks[task.name] = task

    def start(self, num_messages: int = None):
        """Process messages."""
        processed = 0

        while True:
            if num_messages and processed >= num_messages:
                break

            message = self.broker.consume()
            if not message:
                break

            msg_type = message.get("type")

            if msg_type == "group":
                self._execute_group(message)
            elif msg_type == "chord":
                self._execute_chord(message)
            else:
                self._execute_task(message)

            processed += 1

    def _execute_task(self, message: Dict):
        """Execute single task."""
        task_id = message["id"]
        task_name = message["task"]
        args = message["args"]
        kwargs = message["kwargs"]

        task = self.tasks.get(task_name)
        if not task:
            self.backend.store(task_id, TaskState.FAILURE, error="Task not found")
            return

        print(f"[WORKER] Executing: {task_name}")

        try:
            result = task.func(*args, **kwargs)
            self.backend.store(task_id, TaskState.SUCCESS, result=result)
            print(f"[WORKER] Success: {task_name} -> {result}")
        except Exception as e:
            self.backend.store(task_id, TaskState.FAILURE, error=str(e))
            print(f"[WORKER] Failure: {task_name} -> {e}")

    def _execute_group(self, message: Dict):
        """Execute group in parallel (simulated with threads)."""
        group_id = message["id"]
        signatures = message["signatures"]

        print(f"[WORKER] Executing group: {len(signatures)} tasks")

        results = [None] * len(signatures)
        threads = []

        def run_task(index, signature):
            """Run task and store result."""
            try:
                result = signature.task.func(*signature.args, **signature.kwargs)
                results[index] = result
                print(f"[WORKER]   Task {index+1} complete: {result}")
            except Exception as e:
                results[index] = f"ERROR: {e}"
                print(f"[WORKER]   Task {index+1} failed: {e}")

        # Start threads
        for i, sig in enumerate(signatures):
            thread = threading.Thread(target=run_task, args=(i, sig))
            threads.append(thread)
            thread.start()

        # Wait for all
        for thread in threads:
            thread.join()

        self.backend.store(group_id, TaskState.SUCCESS, result=results)
        print(f"[WORKER] Group complete: {results}")

    def _execute_chord(self, message: Dict):
        """Execute chord: group then callback."""
        chord_id = message["id"]
        group = message["group"]
        callback = message["callback"]

        print(f"[WORKER] Executing chord: {len(group.signatures)} tasks + callback")

        # Execute group
        self._execute_group({
            "id": group.group_id,
            "type": "group",
            "signatures": group.signatures
        })

        # Get group results
        group_result = self.backend.get(group.group_id)

        # Execute callback with group results
        print(f"[WORKER] Executing chord callback with results: {group_result.result}")

        try:
            final_result = callback.task.func(group_result.result)
            self.backend.store(chord_id, TaskState.SUCCESS, result=final_result)
            print(f"[WORKER] Chord complete: {final_result}")
        except Exception as e:
            self.backend.store(chord_id, TaskState.FAILURE, error=str(e))
            print(f"[WORKER] Chord callback failed: {e}")

# Global instances
broker = SimpleBroker()
result_backend = ResultBackend()

class Celery:
    """Celery app."""

    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}

    def task(self):
        """Decorator."""
        def decorator(func: Callable) -> Task:
            task_name = f"{self.name}.{func.__name__}"
            task = Task(task_name, func)
            self.tasks[task_name] = task
            return task
        return decorator

app = Celery("group_app")

# Example 1: Basic Group (Parallel Execution)
print("Example 1: Basic Group (Parallel Execution)")
print("=" * 60)

@app.task()
def process_item(item_id: int):
    """Process single item."""
    print(f"    Processing item {item_id}...")
    time.sleep(0.1)  # Simulate work
    return f"processed_{item_id}"

# Create group - process items in parallel
print("Creating group to process 5 items in parallel:")
job = Group([
    process_item.s(1),
    process_item.s(2),
    process_item.s(3),
    process_item.s(4),
    process_item.s(5),
])

result = job.apply_async()

# Execute group
worker = Worker(broker, result_backend)
for task in app.tasks.values():
    worker.register_task(task)

worker.start(num_messages=1)

# Get results
results = result.get(timeout=5)
print(f"\\nAll results: {results}")
print()

# Example 2: Map-Reduce with Chord
print("Example 2: Map-Reduce with Chord")
print("=" * 60)

@app.task()
def calculate_square(n: int):
    """Calculate square."""
    print(f"    Calculating {n}² = {n*n}")
    time.sleep(0.05)
    return n * n

@app.task()
def sum_results(numbers: List[int]):
    """Sum all results."""
    total = sum(numbers)
    print(f"    Summing {numbers} = {total}")
    return total

# Map: Calculate squares in parallel
# Reduce: Sum all results
print("Map-Reduce: Calculate squares [1-5] then sum")

chord_job = Chord(Group([
    calculate_square.s(1),
    calculate_square.s(2),
    calculate_square.s(3),
    calculate_square.s(4),
    calculate_square.s(5),
]))(sum_results.s())

worker.start(num_messages=1)

final_result = chord_job.get(timeout=5)
print(f"\\nFinal result: {final_result}")
print(f"Verification: 1² + 2² + 3² + 4² + 5² = 1+4+9+16+25 = 55")
print()

# Example 3: Parallel Data Processing
print("Example 3: Parallel Data Processing")
print("=" * 60)

@app.task()
def fetch_user_score(user_id: int):
    """Fetch user score."""
    print(f"    Fetching score for user {user_id}...")
    time.sleep(0.05)
    # Simulate scores
    scores = {1: 95, 2: 87, 3: 92, 4: 78, 5: 88}
    return {"user_id": user_id, "score": scores.get(user_id, 0)}

@app.task()
def calculate_average(results: List[Dict]):
    """Calculate average score."""
    scores = [r["score"] for r in results]
    avg = sum(scores) / len(scores) if scores else 0
    print(f"    Scores: {scores}, Average: {avg:.1f}")
    return avg

# Fetch scores in parallel, then average
print("Fetching scores for 5 users in parallel, then calculating average:")

job = Chord(Group([
    fetch_user_score.s(1),
    fetch_user_score.s(2),
    fetch_user_score.s(3),
    fetch_user_score.s(4),
    fetch_user_score.s(5),
]))(calculate_average.s())

worker.start(num_messages=1)

avg_score = job.get(timeout=5)
print(f"\\nAverage score: {avg_score:.1f}")
print()

# Example 4: Batch Processing
print("Example 4: Batch Processing")
print("=" * 60)

@app.task()
def resize_image(image_id: int):
    """Resize image."""
    print(f"    Resizing image {image_id}...")
    time.sleep(0.05)
    return f"resized_{image_id}.jpg"

@app.task()
def create_thumbnails(image_id: int):
    """Create thumbnails."""
    print(f"    Creating thumbnails for image {image_id}...")
    time.sleep(0.05)
    return f"thumb_{image_id}.jpg"

# Process multiple images in parallel
print("Processing 3 images in parallel (resize + thumbnails):")

batch_job = Group([
    Group([resize_image.s(1), create_thumbnails.s(1)]),
    Group([resize_image.s(2), create_thumbnails.s(2)]),
    Group([resize_image.s(3), create_thumbnails.s(3)]),
])

# Note: Nested groups in real Celery need special handling
# Here we simplify to show the concept

job = Group([
    resize_image.s(1),
    create_thumbnails.s(1),
    resize_image.s(2),
    create_thumbnails.s(2),
    resize_image.s(3),
    create_thumbnails.s(3),
])

result = job.apply_async()
worker.start(num_messages=1)

results = result.get(timeout=5)
print(f"\\nBatch results: {results}")
print()

# Example 5: Fan-out/Fan-in Pattern
print("Example 5: Fan-out/Fan-in Pattern")
print("=" * 60)

@app.task()
def analyze_segment(segment_id: int, data: str):
    """Analyze data segment."""
    print(f"    Analyzing segment {segment_id}: {data}")
    time.sleep(0.05)
    return {"segment": segment_id, "word_count": len(data.split())}

@app.task()
def merge_analysis(results: List[Dict]):
    """Merge analysis results."""
    total_words = sum(r["word_count"] for r in results)
    segments = len(results)
    print(f"    Merging {segments} segments: {total_words} total words")
    return {"segments": segments, "total_words": total_words}

# Fan-out: Analyze segments in parallel
# Fan-in: Merge results
print("Fan-out: Analyze text segments -> Fan-in: Merge results")

text_segments = [
    "Hello world this is segment one",
    "Segment two has different content",
    "Third segment with more words here",
]

job = Chord(Group([
    analyze_segment.s(i, seg) for i, seg in enumerate(text_segments)
]))(merge_analysis.s())

worker.start(num_messages=1)

final_analysis = job.get(timeout=5)
print(f"\\nFinal analysis: {final_analysis}")
print()

print("=" * 60)
print("TASK GROUPS & CHORDS BEST PRACTICES")
print("=" * 60)
print("""
GROUP - Parallel Execution:

  group = Group([
      task1.s(arg1),
      task2.s(arg2),
      task3.s(arg3)
  ])
  results = group.apply_async().get()

  Use cases:
  - Independent tasks
  - Batch processing
  - Fan-out pattern
  - Performance optimization

  Returns: [result1, result2, result3]

CHORD - Parallel + Callback:

  chord = chord([
      task1.s(),
      task2.s(),
      task3.s()
  ])(callback.s())

  Use cases:
  - Map-reduce
  - Aggregate results
  - Fan-out/fan-in
  - Parallel processing with reduction

  Callback receives: [result1, result2, result3]

COMMON PATTERNS:

1. Batch Processing:
   Group([process_item.s(i) for i in items])

2. Map-Reduce:
   chord([map_task.s(i) for i in items])(reduce_task.s())

3. Parallel APIs:
   Group([fetch_api1.s(), fetch_api2.s(), fetch_api3.s()])

4. Image Processing:
   chord([resize.s(img) for img in images])(create_gallery.s())

5. Data Aggregation:
   chord([query_db1.s(), query_db2.s()])(merge_results.s())

PERFORMANCE:

  Sequential: 5 tasks × 10s = 50s
  Parallel:   5 tasks || = 10s (5x speedup!)

  - Use workers >= group size
  - Balance task duration
  - Monitor resource usage
  - Set appropriate timeouts

ERROR HANDLING:

  # Individual task failure
  group = Group([task.s() for _ in range(10)])
  results = group.apply_async().get()
  # Some may be errors

  # Chord callback only runs if ALL succeed
  chord([tasks...])(callback.s())

  Strategies:
  - Use link_error on tasks
  - Implement fallbacks
  - Retry failed tasks
  - Log failures

LIMITATIONS:

  ✗ Results must fit in memory
  ✗ All tasks must complete for chord
  ✗ Network overhead for many tasks
  ✗ No partial results in chord

SCALING:

  # Small groups (< 100 tasks)
  Group([task.s(i) for i in range(50)])

  # Large batches (split into chunks)
  for chunk in chunks(items, 100):
      Group([task.s(i) for i in chunk]).apply_async()

MONITORING:

  - Track group completion time
  - Monitor individual task failures
  - Alert on slow tasks
  - Measure fan-out efficiency

ALTERNATIVES:

  Chains: Sequential (A -> B -> C)
  Groups: Parallel (A + B + C)
  Chords: Parallel + Reduce (A + B + C -> D)
  Map: Apply to items (map(task, [1,2,3]))

ADVANCED:

  # Nested groups
  Group([
      Group([task1.s(), task2.s()]),
      Group([task3.s(), task4.s()])
  ])

  # Multiple chords
  chord([...]) | chord([...])

Production note: Real Celery provides:
  - Result backend optimization for large groups
  - Chunked group execution
  - Group result expiration
  - Chord unlock (manual callback trigger)
  - Map/starmap primitives
  - Nested workflow support
  - Result metadata
  - Progress tracking
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 14 COMPLETE: Celery Task Chains and Task Groups")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 818: Celery Task Chains")
    print(f"  - Lesson 819: Celery Task Groups")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
