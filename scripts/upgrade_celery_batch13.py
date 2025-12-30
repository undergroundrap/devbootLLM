#!/usr/bin/env python3
"""
Upgrade Celery lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 13: Celery Basics, Task Scheduling, and Periodic Tasks
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 815: Celery Basics
    lesson_815 = next(l for l in lessons if l['id'] == 815)
    lesson_815['fullSolution'] = '''# Celery Basics - Complete Simulation
# In production: pip install celery redis
# This lesson simulates Celery distributed task queue fundamentals

import time
import json
import uuid
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import random

class TaskState(Enum):
    """Celery task states."""
    PENDING = "PENDING"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    RETRY = "RETRY"
    REVOKED = "REVOKED"

@dataclass
class TaskResult:
    """Task execution result."""
    task_id: str
    state: TaskState
    result: Any = None
    traceback: Optional[str] = None
    retries: int = 0

@dataclass
class Task:
    """Task definition."""
    name: str
    func: Callable
    bind: bool = False
    max_retries: int = 3
    default_retry_delay: int = 10

    def apply_async(self, args: tuple = (), kwargs: dict = None, countdown: int = None):
        """
        Execute task asynchronously.

        Parameters:
        - args: Positional arguments
        - kwargs: Keyword arguments
        - countdown: Delay in seconds before execution
        - eta: Explicit time to run
        - expires: Task expiration time
        - retry: Whether to retry on failure
        """
        kwargs = kwargs or {}
        task_id = str(uuid.uuid4())

        # Create task message
        message = {
            "id": task_id,
            "task": self.name,
            "args": args,
            "kwargs": kwargs,
            "countdown": countdown,
            "created_at": time.time()
        }

        # Send to broker
        broker.publish(message)

        return AsyncResult(task_id)

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async with args."""
        return self.apply_async(args=args, kwargs=kwargs)

    def __call__(self, *args, **kwargs):
        """Execute task synchronously (for testing)."""
        return self.func(*args, **kwargs)

class AsyncResult:
    """Represents task execution result (like a Future)."""

    def __init__(self, task_id: str):
        self.task_id = task_id

    def get(self, timeout: Optional[float] = None, interval: float = 0.5) -> Any:
        """
        Wait for task to complete and return result.

        Parameters:
        - timeout: Max time to wait
        - interval: Polling interval
        """
        start = time.time()

        while True:
            # Check if task completed
            result = result_backend.get(self.task_id)

            if result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]:
                if result.state == TaskState.FAILURE:
                    raise Exception(f"Task failed: {result.traceback}")
                return result.result

            # Check timeout
            if timeout and (time.time() - start) > timeout:
                raise TimeoutError(f"Task {self.task_id} did not complete within {timeout}s")

            time.sleep(interval)

    def ready(self) -> bool:
        """Check if task has completed."""
        result = result_backend.get(self.task_id)
        return result and result.state in [TaskState.SUCCESS, TaskState.FAILURE]

    def successful(self) -> bool:
        """Check if task completed successfully."""
        result = result_backend.get(self.task_id)
        return result and result.state == TaskState.SUCCESS

    def failed(self) -> bool:
        """Check if task failed."""
        result = result_backend.get(self.task_id)
        return result and result.state == TaskState.FAILURE

    def state(self) -> str:
        """Get current task state."""
        result = result_backend.get(self.task_id)
        return result.state.value if result else TaskState.PENDING.value

class MessageBroker:
    """
    Simulated message broker (RabbitMQ/Redis).

    In production:
    - RabbitMQ: Full-featured message broker with AMQP
    - Redis: Lightweight, fast, good for simple queues
    - Amazon SQS: Managed cloud queue
    """

    def __init__(self):
        self.queues: Dict[str, List[Dict]] = {"celery": []}

    def publish(self, message: Dict):
        """Publish task to queue."""
        self.queues["celery"].append(message)
        print(f"[BROKER] Task {message['id'][:8]} queued: {message['task']}")

    def consume(self, queue: str = "celery") -> Optional[Dict]:
        """Consume message from queue (FIFO)."""
        if self.queues[queue]:
            return self.queues[queue].pop(0)
        return None

    def queue_length(self, queue: str = "celery") -> int:
        """Get queue length."""
        return len(self.queues[queue])

class ResultBackend:
    """
    Simulated result backend (Redis/database).

    Stores task results for later retrieval.
    """

    def __init__(self):
        self.results: Dict[str, TaskResult] = {}

    def store(self, task_id: str, state: TaskState, result: Any = None, traceback: str = None):
        """Store task result."""
        self.results[task_id] = TaskResult(
            task_id=task_id,
            state=state,
            result=result,
            traceback=traceback
        )

    def get(self, task_id: str) -> Optional[TaskResult]:
        """Retrieve task result."""
        return self.results.get(task_id)

class Worker:
    """
    Celery worker that executes tasks.

    In production:
    - Multiple workers for parallelism
    - Prefetch settings for optimization
    - Concurrency models: prefork, eventlet, gevent
    """

    def __init__(self, broker: MessageBroker, backend: ResultBackend):
        self.broker = broker
        self.backend = backend
        self.tasks: Dict[str, Task] = {}
        self.running = False

    def register_task(self, task: Task):
        """Register a task."""
        self.tasks[task.name] = task

    def start(self, num_tasks: int = None):
        """
        Start worker to process tasks.

        Parameters:
        - num_tasks: Process N tasks then stop (for testing)
        """
        self.running = True
        processed = 0

        print(f"[WORKER] Starting worker...")

        while self.running:
            # Check if should stop
            if num_tasks and processed >= num_tasks:
                break

            # Consume message
            message = self.broker.consume()

            if not message:
                # No tasks in queue
                time.sleep(0.1)
                continue

            # Process task
            self._execute_task(message)
            processed += 1

        print(f"[WORKER] Stopped after processing {processed} tasks")

    def _execute_task(self, message: Dict):
        """Execute a single task."""
        task_id = message["id"]
        task_name = message["task"]
        args = message["args"]
        kwargs = message["kwargs"]
        countdown = message.get("countdown")

        # Wait for countdown
        if countdown:
            print(f"[WORKER] Task {task_id[:8]} delayed {countdown}s")
            time.sleep(countdown)

        # Get task function
        task = self.tasks.get(task_name)
        if not task:
            self.backend.store(task_id, TaskState.FAILURE, traceback=f"Task {task_name} not found")
            return

        # Mark as started
        self.backend.store(task_id, TaskState.STARTED)
        print(f"[WORKER] Executing task {task_id[:8]}: {task_name}")

        try:
            # Execute task
            result = task.func(*args, **kwargs)

            # Store success
            self.backend.store(task_id, TaskState.SUCCESS, result=result)
            print(f"[WORKER] Task {task_id[:8]} completed: {result}")

        except Exception as e:
            # Store failure
            self.backend.store(task_id, TaskState.FAILURE, traceback=str(e))
            print(f"[WORKER] Task {task_id[:8]} failed: {e}")

    def stop(self):
        """Stop worker."""
        self.running = False

# Global broker and backend
broker = MessageBroker()
result_backend = ResultBackend()

# Create Celery app
class Celery:
    """Simulated Celery application."""

    def __init__(self, name: str):
        self.name = name
        self.tasks: Dict[str, Task] = {}

    def task(self, bind: bool = False, max_retries: int = 3):
        """
        Decorator to create a task.

        Usage:
        @app.task
        def add(x, y):
            return x + y
        """
        def decorator(func: Callable) -> Task:
            task_name = f"{self.name}.{func.__name__}"
            task = Task(
                name=task_name,
                func=func,
                bind=bind,
                max_retries=max_retries
            )
            self.tasks[task_name] = task
            return task

        return decorator

# Create app instance
app = Celery("myapp")

# Example 1: Basic Task Definition and Execution
print("Example 1: Basic Task Definition and Execution")
print("=" * 60)

@app.task
def add(x, y):
    """Simple addition task."""
    return x + y

@app.task
def multiply(x, y):
    """Simple multiplication task."""
    return x * y

print("Tasks registered:")
for task_name in app.tasks:
    print(f"  - {task_name}")
print()

# Execute synchronously (for testing)
print("Synchronous execution:")
result = add(5, 3)
print(f"  add(5, 3) = {result}")
print()

# Execute asynchronously
print("Asynchronous execution:")
async_result = add.delay(10, 20)
print(f"  Task submitted: {async_result.task_id[:8]}...")
print(f"  State: {async_result.state()}")

# Start worker to process tasks
worker = Worker(broker, result_backend)
for task_name, task in app.tasks.items():
    worker.register_task(task)

worker.start(num_tasks=1)

# Get result
result = async_result.get(timeout=5)
print(f"  Result: {result}")
print()

# Example 2: Multiple Tasks in Parallel
print("Example 2: Multiple Tasks in Parallel")
print("=" * 60)

@app.task
def process_data(data_id):
    """Simulate data processing."""
    print(f"    Processing data {data_id}...")
    time.sleep(0.2)  # Simulate work
    return f"processed_{data_id}"

# Submit multiple tasks
print("Submitting 5 tasks:")
results = []
for i in range(5):
    result = process_data.delay(i)
    results.append(result)
    print(f"  Task {i} submitted: {result.task_id[:8]}...")

print()

# Process all tasks
worker.start(num_tasks=5)

# Wait for all results
print("\\nResults:")
for i, result in enumerate(results):
    value = result.get(timeout=5)
    print(f"  Task {i}: {value}")

print()

# Example 3: Task with Countdown (Delayed Execution)
print("Example 3: Task with Countdown (Delayed Execution)")
print("=" * 60)

@app.task
def send_email(to: str, subject: str):
    """Simulate sending email."""
    print(f"    Sending email to {to}: {subject}")
    return f"Email sent to {to}"

# Schedule task to run in 2 seconds
print("Scheduling email to send in 2 seconds...")
result = send_email.apply_async(
    args=("user@example.com", "Welcome!"),
    countdown=2
)

print(f"Task scheduled: {result.task_id[:8]}...")
print("Waiting for execution...")

# Process task (worker will wait 2 seconds)
start_time = time.time()
worker.start(num_tasks=1)
elapsed = time.time() - start_time

value = result.get(timeout=5)
print(f"Result: {value}")
print(f"Actual delay: {elapsed:.1f}s")
print()

# Example 4: Task Chaining (Workflow)
print("Example 4: Task Chaining (Workflow)")
print("=" * 60)

@app.task
def download_file(url: str):
    """Step 1: Download file."""
    print(f"    Downloading {url}...")
    return f"file_from_{url}"

@app.task
def process_file(filename: str):
    """Step 2: Process file."""
    print(f"    Processing {filename}...")
    return f"processed_{filename}"

@app.task
def upload_result(filename: str):
    """Step 3: Upload result."""
    print(f"    Uploading {filename}...")
    return f"uploaded_{filename}"

# Manual chaining (in production, use celery.chain)
print("Workflow: Download -> Process -> Upload")

# Step 1
result1 = download_file.delay("http://example.com/data.csv")
worker.start(num_tasks=1)
file1 = result1.get()
print(f"Step 1 complete: {file1}")

# Step 2
result2 = process_file.delay(file1)
worker.start(num_tasks=1)
file2 = result2.get()
print(f"Step 2 complete: {file2}")

# Step 3
result3 = upload_result.delay(file2)
worker.start(num_tasks=1)
file3 = result3.get()
print(f"Step 3 complete: {file3}")

print()

# Example 5: Error Handling
print("Example 5: Error Handling")
print("=" * 60)

@app.task
def risky_task(value: int):
    """Task that may fail."""
    if value < 0:
        raise ValueError("Value must be positive!")
    return value * 2

# Successful execution
print("Task with valid input:")
result = risky_task.delay(10)
worker.start(num_tasks=1)
print(f"  Result: {result.get()}")
print()

# Failed execution
print("Task with invalid input:")
result = risky_task.delay(-5)
worker.start(num_tasks=1)

try:
    result.get()
except Exception as e:
    print(f"  Task failed: {e}")
    print(f"  State: {result.state()}")

print()

# Example 6: Task Monitoring
print("Example 6: Task Monitoring")
print("=" * 60)

@app.task
def long_running_task(duration: int):
    """Simulate long-running task."""
    for i in range(duration):
        print(f"    Progress: {i+1}/{duration}")
        time.sleep(0.1)
    return f"Completed {duration} steps"

print("Submitting long-running task...")
result = long_running_task.delay(5)

print(f"Initial state: {result.state()}")

# Start worker in background (simulation)
print("Worker processing...")
worker.start(num_tasks=1)

# Check status
print(f"Final state: {result.state()}")
if result.ready():
    print(f"Result: {result.get()}")

print()
print("=" * 60)
print("CELERY BASICS - BEST PRACTICES")
print("=" * 60)
print("""
TASK DESIGN PRINCIPLES:
  1. IDEMPOTENT
     - Tasks should produce same result if executed multiple times
     - Important for retries and fault tolerance

  2. ATOMIC
     - Each task should be a single unit of work
     - Break large jobs into smaller tasks

  3. STATELESS
     - Don't rely on shared state
     - Pass all required data as arguments

  4. SMALL PAYLOADS
     - Keep arguments small (< 1MB)
     - Use references (IDs) instead of large objects

BROKER SELECTION:
  RabbitMQ:
    ✓ Full-featured, reliable
    ✓ Advanced routing
    ✓ Message priorities
    - Higher memory usage

  Redis:
    ✓ Fast, simple
    ✓ Good for simple queues
    ✓ Lower latency
    - Less durable (can lose messages)

  Amazon SQS:
    ✓ Managed, scalable
    ✓ No infrastructure
    - Higher latency
    - Limited features

RESULT BACKEND SELECTION:
  - Redis: Fast, good for short-lived results
  - Database: Persistent, queryable
  - No backend: Fire-and-forget tasks

WORKER CONFIGURATION:
  Concurrency models:
    - prefork: Multiprocessing (CPU-bound)
    - eventlet/gevent: Coroutines (I/O-bound)
    - solo: Single process (debugging)

  Settings:
    - worker_concurrency: Number of worker processes
    - task_acks_late: Acknowledge after execution
    - worker_prefetch_multiplier: Tasks to prefetch

MONITORING:
  - Flower: Web-based monitoring tool
  - celery events: Event stream
  - celery inspect: Query workers

COMMON PATTERNS:
  1. Fan-out: Distribute work to many workers
  2. Map-reduce: Process data in parallel, combine results
  3. Callbacks: Chain tasks together
  4. Retries: Automatic retry on failure
  5. Rate limiting: Control task execution rate

PRODUCTION TIPS:
  - Use task_reject_on_worker_lost=True
  - Set task timeouts (task_soft_time_limit)
  - Monitor queue lengths
  - Use dedicated queues for priorities
  - Enable task result expiration
  - Configure proper logging

Production note: Real Celery provides:
  - Task routing to different queues
  - Priority queues
  - Task expiration and ETA
  - Canvas: Workflows (chain, group, chord)
  - Retry with exponential backoff
  - Task revocation
  - Result compression
  - Beat scheduler for periodic tasks
""")
'''

    # Lesson 816: Celery Task Scheduling
    lesson_816 = next(l for l in lessons if l['id'] == 816)
    lesson_816['fullSolution'] = '''# Celery Task Scheduling - Complete Simulation
# In production: pip install celery redis
# This lesson simulates Celery task scheduling with ETA, countdown, and priorities

import time
import uuid
from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
import heapq

class Priority(Enum):
    """Task priority levels."""
    LOW = 0
    NORMAL = 5
    HIGH = 10

@dataclass
class ScheduledTask:
    """Task scheduled for future execution."""
    execute_at: float  # Unix timestamp
    priority: int
    message: Dict
    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __lt__(self, other):
        """Compare for priority queue (earlier time or higher priority first)."""
        if abs(self.execute_at - other.execute_at) < 0.001:
            return self.priority > other.priority  # Higher priority first
        return self.execute_at < other.execute_at

class PriorityQueue:
    """
    Priority queue with time-based scheduling.

    In production:
    - RabbitMQ supports priority queues natively
    - Redis uses sorted sets for scheduled tasks
    """

    def __init__(self, name: str):
        self.name = name
        self.heap: List[ScheduledTask] = []

    def push(self, task: ScheduledTask):
        """Add task to priority queue."""
        heapq.heappush(self.heap, task)

    def pop_ready(self, current_time: float) -> Optional[ScheduledTask]:
        """Pop next ready task (time has come and highest priority)."""
        if not self.heap:
            return None

        # Peek at next task
        if self.heap[0].execute_at <= current_time:
            return heapq.heappop(self.heap)

        return None

    def peek_next_time(self) -> Optional[float]:
        """Get execution time of next task."""
        return self.heap[0].execute_at if self.heap else None

    def __len__(self):
        return len(self.heap)

class ScheduledMessageBroker:
    """Message broker with scheduling support."""

    def __init__(self):
        self.queues: Dict[str, PriorityQueue] = {
            "celery": PriorityQueue("celery"),
            "high_priority": PriorityQueue("high_priority"),
            "low_priority": PriorityQueue("low_priority")
        }

    def publish(
        self,
        message: Dict,
        queue: str = "celery",
        countdown: Optional[int] = None,
        eta: Optional[datetime] = None,
        priority: Priority = Priority.NORMAL
    ):
        """
        Publish task with scheduling options.

        Parameters:
        - countdown: Execute after N seconds
        - eta: Execute at specific time
        - priority: Task priority (LOW, NORMAL, HIGH)
        """
        # Calculate execution time
        if eta:
            execute_at = eta.timestamp()
        elif countdown:
            execute_at = time.time() + countdown
        else:
            execute_at = time.time()

        task = ScheduledTask(
            execute_at=execute_at,
            priority=priority.value,
            message=message
        )

        self.queues[queue].push(task)

        if countdown:
            print(f"[BROKER] Task {task.task_id[:8]} scheduled in {countdown}s on queue '{queue}'")
        elif eta:
            print(f"[BROKER] Task {task.task_id[:8]} scheduled for {eta.strftime('%H:%M:%S')} on queue '{queue}'")
        else:
            print(f"[BROKER] Task {task.task_id[:8]} queued on '{queue}' (priority: {priority.name})")

    def consume(self, queue: str = "celery") -> Optional[Dict]:
        """Consume next ready task from queue."""
        current_time = time.time()
        scheduled_task = self.queues[queue].pop_ready(current_time)

        if scheduled_task:
            return scheduled_task.message

        return None

    def queue_length(self, queue: str = "celery") -> int:
        """Get queue length."""
        return len(self.queues[queue])

    def next_task_eta(self, queue: str = "celery") -> Optional[str]:
        """Get ETA of next task."""
        next_time = self.queues[queue].peek_next_time()
        if next_time:
            dt = datetime.fromtimestamp(next_time)
            return dt.strftime('%H:%M:%S')
        return None

class Task:
    """Task with scheduling capabilities."""

    def __init__(self, name: str, func: Callable):
        self.name = name
        self.func = func

    def apply_async(
        self,
        args: tuple = (),
        kwargs: dict = None,
        countdown: int = None,
        eta: datetime = None,
        priority: Priority = Priority.NORMAL,
        queue: str = "celery"
    ):
        """
        Execute task asynchronously with scheduling.

        Parameters:
        - countdown: Delay in seconds
        - eta: Explicit execution time
        - priority: Task priority
        - queue: Target queue
        - expires: Task expiration
        """
        kwargs = kwargs or {}
        task_id = str(uuid.uuid4())

        message = {
            "id": task_id,
            "task": self.name,
            "args": args,
            "kwargs": kwargs,
        }

        # Publish to broker
        broker.publish(message, queue=queue, countdown=countdown, eta=eta, priority=priority)

        return {"task_id": task_id}

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async."""
        return self.apply_async(args=args, kwargs=kwargs)

class ScheduledWorker:
    """Worker that processes scheduled tasks."""

    def __init__(self, broker: ScheduledMessageBroker, queues: List[str] = None):
        self.broker = broker
        self.queues = queues or ["celery"]
        self.tasks: Dict[str, Task] = {}
        self.running = False

    def register_task(self, task: Task):
        """Register task."""
        self.tasks[task.name] = task

    def start(self, duration: float = None):
        """
        Start worker to process tasks.

        Parameters:
        - duration: Run for N seconds then stop
        """
        self.running = True
        start_time = time.time()

        print(f"[WORKER] Starting worker (queues: {', '.join(self.queues)})...")

        while self.running:
            # Check duration
            if duration and (time.time() - start_time) > duration:
                break

            # Try each queue in order (priority)
            task_found = False
            for queue_name in self.queues:
                message = self.broker.consume(queue_name)

                if message:
                    self._execute_task(message)
                    task_found = True
                    break

            if not task_found:
                # No tasks ready
                time.sleep(0.1)

        print(f"[WORKER] Stopped")

    def _execute_task(self, message: Dict):
        """Execute task."""
        task_id = message["id"]
        task_name = message["task"]
        args = message["args"]
        kwargs = message["kwargs"]

        task = self.tasks.get(task_name)
        if not task:
            print(f"[WORKER] Task {task_name} not found")
            return

        print(f"[WORKER] Executing {task_id[:8]}: {task_name}")

        try:
            result = task.func(*args, **kwargs)
            print(f"[WORKER] Task {task_id[:8]} completed: {result}")
        except Exception as e:
            print(f"[WORKER] Task {task_id[:8]} failed: {e}")

class Celery:
    """Celery app with scheduling."""

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

# Global instances
broker = ScheduledMessageBroker()
app = Celery("scheduling_app")

# Example 1: Countdown (Delayed Execution)
print("Example 1: Countdown (Delayed Execution)")
print("=" * 60)

@app.task()
def send_notification(user_id: int, message: str):
    """Send notification to user."""
    print(f"    Notification to user {user_id}: {message}")
    return f"Sent to {user_id}"

# Schedule task to run in 3 seconds
print("Scheduling notification to send in 3 seconds...")
result = send_notification.apply_async(
    args=(123, "Your order has shipped!"),
    countdown=3
)

# Create worker
worker = ScheduledWorker(broker)
for task in app.tasks.values():
    worker.register_task(task)

# Process (worker will wait)
start = time.time()
worker.start(duration=5)
elapsed = time.time() - start

print(f"Execution took {elapsed:.1f}s (waited for countdown)")
print()

# Example 2: ETA (Exact Time)
print("Example 2: ETA (Exact Time)")
print("=" * 60)

@app.task()
def generate_report(report_type: str):
    """Generate report."""
    print(f"    Generating {report_type} report...")
    return f"{report_type}_report.pdf"

# Schedule for specific time (5 seconds from now)
eta_time = datetime.now() + timedelta(seconds=5)

print(f"Scheduling report generation for {eta_time.strftime('%H:%M:%S')}...")
result = generate_report.apply_async(
    args=("monthly",),
    eta=eta_time
)

print(f"Current time: {datetime.now().strftime('%H:%M:%S')}")
print(f"Next task ETA: {broker.next_task_eta('celery')}")
print()

# Process (worker will wait until ETA)
print("Worker waiting for ETA...")
start = time.time()
worker.start(duration=7)
elapsed = time.time() - start

print(f"Task executed after {elapsed:.1f}s")
print()

# Example 3: Priority Queues
print("Example 3: Priority Queues")
print("=" * 60)

@app.task()
def process_job(job_id: int, job_type: str):
    """Process job."""
    print(f"    Processing {job_type} job {job_id}")
    time.sleep(0.1)
    return f"Job {job_id} complete"

# Submit tasks with different priorities
print("Submitting 6 tasks with mixed priorities:")

tasks_submitted = [
    (1, Priority.LOW, "background task"),
    (2, Priority.NORMAL, "regular task"),
    (3, Priority.HIGH, "urgent task"),
    (4, Priority.LOW, "background task"),
    (5, Priority.HIGH, "urgent task"),
    (6, Priority.NORMAL, "regular task"),
]

for job_id, priority, job_type in tasks_submitted:
    process_job.apply_async(
        args=(job_id, job_type),
        priority=priority
    )

print()

# Process all tasks - high priority first
print("Worker processing tasks (high priority first):")
worker.start(duration=3)

print()

# Example 4: Multiple Queues
print("Example 4: Multiple Queues (Queue Routing)")
print("=" * 60)

@app.task()
def critical_task(task_id: int):
    """Critical task for high-priority queue."""
    print(f"    CRITICAL: Processing task {task_id}")
    return f"Critical task {task_id} done"

@app.task()
def background_task(task_id: int):
    """Background task for low-priority queue."""
    print(f"    BACKGROUND: Processing task {task_id}")
    return f"Background task {task_id} done"

# Submit to different queues
print("Submitting tasks to different queues:")

critical_task.apply_async(args=(1,), queue="high_priority")
background_task.apply_async(args=(2,), queue="low_priority")
critical_task.apply_async(args=(3,), queue="high_priority")
background_task.apply_async(args=(4,), queue="low_priority")

print()

# Worker 1: High priority queue only
print("Worker 1: Processing high_priority queue:")
worker1 = ScheduledWorker(broker, queues=["high_priority"])
for task in app.tasks.values():
    worker1.register_task(task)

worker1.start(duration=1)

print()

# Worker 2: Low priority queue only
print("Worker 2: Processing low_priority queue:")
worker2 = ScheduledWorker(broker, queues=["low_priority"])
for task in app.tasks.values():
    worker2.register_task(task)

worker2.start(duration=1)

print()

# Example 5: Mixed Scheduling
print("Example 5: Mixed Scheduling (Countdown + Priority)")
print("=" * 60)

@app.task()
def send_email(to: str, subject: str, urgency: str):
    """Send email with urgency level."""
    print(f"    Sending {urgency} email to {to}: {subject}")
    return f"Email sent to {to}"

# Schedule emails with different timings and priorities
print("Scheduling emails:")

# Immediate, high priority
send_email.apply_async(
    args=("admin@example.com", "Server Alert", "URGENT"),
    priority=Priority.HIGH
)

# 2 seconds delay, normal priority
send_email.apply_async(
    args=("user@example.com", "Daily Digest", "NORMAL"),
    countdown=2,
    priority=Priority.NORMAL
)

# 4 seconds delay, low priority
send_email.apply_async(
    args=("newsletter@example.com", "Weekly Update", "LOW"),
    countdown=4,
    priority=Priority.LOW
)

print()

# Process all
print("Worker processing all scheduled emails:")
worker.start(duration=6)

print()
print("=" * 60)
print("TASK SCHEDULING BEST PRACTICES")
print("=" * 60)
print("""
COUNTDOWN vs ETA:
  countdown: Relative delay (e.g., "in 5 seconds")
    - Simple, works across timezones
    - Good for: retries, rate limiting

  eta: Absolute time (e.g., "at 2:00 PM")
    - Precise scheduling
    - Good for: scheduled reports, daily tasks

PRIORITY LEVELS:
  Design considerations:
    - Use 3-5 priority levels max
    - HIGH: User-facing, time-sensitive
    - NORMAL: Regular background tasks
    - LOW: Cleanup, analytics, non-urgent

  Implementation:
    - RabbitMQ: Native priority queues (0-10)
    - Redis: Use separate queues + worker routing

QUEUE ROUTING:
  Patterns:
    1. By priority: high_priority, default, low_priority
    2. By function: emails, reports, uploads
    3. By resource: cpu_intensive, io_intensive
    4. By customer: customer_A, customer_B (multi-tenancy)

  Worker configuration:
    celery -A app worker -Q high_priority,default
    celery -A app worker -Q low_priority

TASK EXPIRATION:
  Set expires to prevent stale task execution:
    task.apply_async(expires=300)  # 5 minutes

  Use cases:
    - Real-time notifications
    - Time-sensitive offers
    - Temporary tokens

SCHEDULING PATTERNS:
  1. Throttling:
     countdown = calculate_backoff(attempt)
     task.apply_async(countdown=countdown)

  2. Batching:
     # Wait 60s, batch all pending items
     process_batch.apply_async(countdown=60)

  3. Cascading:
     # Chain with delays
     task1.apply_async() -> (wait) -> task2.apply_async()

MONITORING:
  - Track queue lengths by priority
  - Monitor scheduled task counts
  - Alert on growing queues
  - Measure time-to-execution variance

COMMON PITFALLS:
  ✗ Too many priority levels (confusing)
  ✗ Scheduling far future tasks (use Beat instead)
  ✗ No expiration on scheduled tasks
  ✗ Priority inversion (low priority blocking high)

PRODUCTION PATTERNS:
  Email service:
    - Immediate: High priority, no delay
    - Marketing: Low priority, rate limited
    - Digests: Scheduled via ETA

  Report generation:
    - Ad-hoc: High priority
    - Scheduled: Normal priority with ETA
    - Batch: Low priority

  Data processing:
    - Real-time: High priority, separate queue
    - Batch: Low priority, scheduled
    - Cleanup: Lowest priority, daily ETA

Production note: Real Celery provides:
  - Task expiration (expires parameter)
  - Soft/hard time limits
  - Task replacement (replace=True)
  - Queue binding and routing keys
  - Delayed task execution with Beat
  - Task rate limiting
  - ETA precision based on clock skew
""")
'''

    # Lesson 817: Celery Periodic Tasks
    lesson_817 = next(l for l in lessons if l['id'] == 817)
    lesson_817['fullSolution'] = '''# Celery Periodic Tasks - Complete Simulation
# In production: pip install celery redis celery-beat
# This lesson simulates Celery Beat for periodic task scheduling

import time
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum

class ScheduleType(Enum):
    """Types of periodic schedules."""
    CRONTAB = "crontab"
    INTERVAL = "interval"
    SOLAR = "solar"

@dataclass
class Schedule:
    """Base schedule class."""
    pass

@dataclass
class IntervalSchedule(Schedule):
    """
    Run task every N seconds/minutes/hours/days.

    Examples:
    - every=60: Every 60 seconds
    - every=timedelta(minutes=5): Every 5 minutes
    - every=timedelta(hours=1): Every 1 hour
    """
    every: int  # seconds

    def is_due(self, last_run: datetime) -> Tuple[bool, float]:
        """
        Check if task is due.

        Returns: (is_due, next_run_in_seconds)
        """
        elapsed = (datetime.now() - last_run).total_seconds()

        if elapsed >= self.every:
            return True, self.every
        else:
            remaining = self.every - elapsed
            return False, remaining

@dataclass
class CrontabSchedule(Schedule):
    """
    Cron-like schedule.

    Fields:
    - minute: 0-59
    - hour: 0-23
    - day_of_week: 0-6 (Monday=0)
    - day_of_month: 1-31
    - month_of_year: 1-12

    Use '*' for "every"
    """
    minute: str = "*"
    hour: str = "*"
    day_of_week: str = "*"
    day_of_month: str = "*"
    month_of_year: str = "*"

    def _matches(self, value: int, pattern: str) -> bool:
        """Check if value matches cron pattern."""
        if pattern == "*":
            return True

        # Handle ranges (e.g., "1-5")
        if "-" in pattern:
            start, end = map(int, pattern.split("-"))
            return start <= value <= end

        # Handle lists (e.g., "1,3,5")
        if "," in pattern:
            values = list(map(int, pattern.split(",")))
            return value in values

        # Exact match
        return value == int(pattern)

    def is_due(self, last_run: datetime) -> Tuple[bool, float]:
        """Check if task is due based on cron schedule."""
        now = datetime.now()

        # Check each field
        is_due = (
            self._matches(now.minute, self.minute) and
            self._matches(now.hour, self.hour) and
            self._matches(now.weekday(), self.day_of_week) and
            self._matches(now.day, self.day_of_month) and
            self._matches(now.month, self.month_of_year)
        )

        # Calculate next run (simplified - assumes every minute)
        next_run_seconds = 60 - now.second

        return is_due, next_run_seconds

@dataclass
class PeriodicTask:
    """Periodic task configuration."""
    name: str
    task: str  # Task name
    schedule: Schedule
    args: tuple = ()
    kwargs: dict = None
    enabled: bool = True
    last_run_at: datetime = None

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}
        if self.last_run_at is None:
            self.last_run_at = datetime.now() - timedelta(days=1)

class Beat:
    """
    Celery Beat scheduler.

    Periodically checks which tasks should run and sends them to broker.
    """

    def __init__(self, broker):
        self.broker = broker
        self.schedule: Dict[str, PeriodicTask] = {}
        self.running = False

    def add_periodic_task(
        self,
        schedule: Schedule,
        task: str,
        name: str = None,
        args: tuple = (),
        kwargs: dict = None
    ):
        """Add a periodic task to the schedule."""
        kwargs = kwargs or {}
        task_name = name or f"{task}_{id(schedule)}"

        periodic_task = PeriodicTask(
            name=task_name,
            task=task,
            schedule=schedule,
            args=args,
            kwargs=kwargs
        )

        self.schedule[task_name] = periodic_task
        print(f"[BEAT] Registered periodic task: {task_name}")

    def start(self, duration: float = None):
        """
        Start beat scheduler.

        Parameters:
        - duration: Run for N seconds then stop
        """
        self.running = True
        start_time = time.time()

        print(f"[BEAT] Starting scheduler with {len(self.schedule)} periodic tasks...")

        while self.running:
            # Check duration
            if duration and (time.time() - start_time) > duration:
                break

            # Check each periodic task
            for task_name, periodic_task in self.schedule.items():
                if not periodic_task.enabled:
                    continue

                # Check if task is due
                is_due, next_run_in = periodic_task.schedule.is_due(periodic_task.last_run_at)

                if is_due:
                    print(f"[BEAT] Scheduling {task_name}")

                    # Send task to broker
                    message = {
                        "id": f"{task_name}_{int(time.time())}",
                        "task": periodic_task.task,
                        "args": periodic_task.args,
                        "kwargs": periodic_task.kwargs
                    }

                    self.broker.publish(message)

                    # Update last run time
                    periodic_task.last_run_at = datetime.now()

            # Sleep for a bit
            time.sleep(1)

        print(f"[BEAT] Stopped")

    def stop(self):
        """Stop beat scheduler."""
        self.running = False

class SimpleBroker:
    """Simple message broker."""

    def __init__(self):
        self.queue: List[Dict] = []

    def publish(self, message: Dict):
        """Publish message to queue."""
        self.queue.append(message)

    def consume(self) -> Optional[Dict]:
        """Consume message from queue."""
        if self.queue:
            return self.queue.pop(0)
        return None

class SimpleWorker:
    """Simple worker."""

    def __init__(self, broker, tasks: Dict[str, Callable]):
        self.broker = broker
        self.tasks = tasks
        self.running = False

    def start(self, duration: float = None):
        """Start worker."""
        self.running = True
        start_time = time.time()

        while self.running:
            if duration and (time.time() - start_time) > duration:
                break

            message = self.broker.consume()
            if message:
                self._execute(message)
            else:
                time.sleep(0.1)

    def _execute(self, message: Dict):
        """Execute task."""
        task_name = message["task"]
        args = message["args"]
        kwargs = message["kwargs"]

        if task_name in self.tasks:
            print(f"[WORKER] Executing {task_name}")
            result = self.tasks[task_name](*args, **kwargs)
            print(f"[WORKER] Result: {result}")

# Example 1: Interval-based Periodic Task
print("Example 1: Interval-based Periodic Task")
print("=" * 60)

broker = SimpleBroker()
beat = Beat(broker)

def cleanup_old_data():
    """Clean up old data."""
    print("    Cleaning up old data...")
    return "Cleaned 150 old records"

def send_heartbeat():
    """Send heartbeat."""
    print("    Sending heartbeat ping...")
    return "Heartbeat sent"

# Schedule cleanup every 5 seconds
beat.add_periodic_task(
    schedule=IntervalSchedule(every=5),
    task="cleanup_old_data",
    name="cleanup_task"
)

# Schedule heartbeat every 3 seconds
beat.add_periodic_task(
    schedule=IntervalSchedule(every=3),
    task="send_heartbeat",
    name="heartbeat_task"
)

print("Periodic tasks registered:")
for name in beat.schedule:
    print(f"  - {name}")
print()

# Start beat scheduler for 12 seconds
print("Running beat scheduler for 12 seconds...")
print("(cleanup runs at: 5s, 10s | heartbeat runs at: 3s, 6s, 9s, 12s)")
print()

import threading

def run_beat():
    beat.start(duration=12)

def run_worker():
    worker = SimpleWorker(broker, {
        "cleanup_old_data": cleanup_old_data,
        "send_heartbeat": send_heartbeat
    })
    worker.start(duration=13)

# Run beat and worker concurrently (simulated)
beat_thread = threading.Thread(target=run_beat)
worker_thread = threading.Thread(target=run_worker)

beat_thread.start()
time.sleep(0.5)  # Let beat start first
worker_thread.start()

beat_thread.join()
worker_thread.join()

print()

# Example 2: Crontab-based Periodic Task
print("Example 2: Crontab-based Periodic Task")
print("=" * 60)

broker2 = SimpleBroker()
beat2 = Beat(broker2)

def generate_daily_report():
    """Generate daily report."""
    print(f"    Generating daily report at {datetime.now().strftime('%H:%M:%S')}")
    return "Daily report generated"

def send_hourly_summary():
    """Send hourly summary."""
    print(f"    Sending hourly summary at {datetime.now().strftime('%H:%M:%S')}")
    return "Hourly summary sent"

# Run every day at 9:00 AM
beat2.add_periodic_task(
    schedule=CrontabSchedule(hour="9", minute="0"),
    task="generate_daily_report",
    name="daily_report"
)

# Run every hour at minute 0
beat2.add_periodic_task(
    schedule=CrontabSchedule(minute="0"),
    task="send_hourly_summary",
    name="hourly_summary"
)

# For demo, use current time
current_minute = datetime.now().minute
current_hour = datetime.now().hour

# Adjust to trigger within next minute
beat2.add_periodic_task(
    schedule=CrontabSchedule(minute=str((current_minute + 1) % 60)),
    task="send_hourly_summary",
    name="demo_minute_task"
)

print("Crontab tasks:")
for name, task in beat2.schedule.items():
    if isinstance(task.schedule, CrontabSchedule):
        s = task.schedule
        print(f"  {name}: {s.minute} {s.hour} * * *")

print()

# Example 3: Real-world Patterns
print("Example 3: Real-world Patterns")
print("=" * 60)

broker3 = SimpleBroker()
beat3 = Beat(broker3)

# Pattern 1: Database cleanup (nightly at 2 AM)
beat3.add_periodic_task(
    schedule=CrontabSchedule(hour="2", minute="0"),
    task="db_cleanup",
    name="nightly_db_cleanup"
)

# Pattern 2: Cache warming (every 15 minutes)
beat3.add_periodic_task(
    schedule=IntervalSchedule(every=15 * 60),
    task="warm_cache",
    name="cache_warming"
)

# Pattern 3: Health checks (every 30 seconds)
beat3.add_periodic_task(
    schedule=IntervalSchedule(every=30),
    task="health_check",
    name="service_health_check"
)

# Pattern 4: Weekly reports (Monday at 9 AM)
beat3.add_periodic_task(
    schedule=CrontabSchedule(day_of_week="0", hour="9", minute="0"),
    task="weekly_report",
    name="monday_weekly_report"
)

# Pattern 5: Hourly analytics (every hour)
beat3.add_periodic_task(
    schedule=CrontabSchedule(minute="0"),
    task="process_analytics",
    name="hourly_analytics"
)

print("Production-ready periodic tasks:")
for name, task in beat3.schedule.items():
    if isinstance(task.schedule, IntervalSchedule):
        print(f"  {name}: Every {task.schedule.every}s")
    elif isinstance(task.schedule, CrontabSchedule):
        s = task.schedule
        print(f"  {name}: Cron({s.minute} {s.hour} {s.day_of_month} {s.month_of_year} {s.day_of_week})")

print()
print("=" * 60)
print("PERIODIC TASKS BEST PRACTICES")
print("=" * 60)
print("""
SCHEDULE TYPES:

1. INTERVAL (time-based):
   Use for:
   - Health checks
   - Cache updates
   - Heartbeat pings
   - Any fixed-interval task

   Examples:
   schedule=IntervalSchedule(every=60)  # Every minute
   schedule=IntervalSchedule(every=3600)  # Every hour

2. CRONTAB (calendar-based):
   Use for:
   - Daily reports
   - Weekly summaries
   - Monthly billing
   - Any calendar-scheduled task

   Examples:
   CrontabSchedule(hour="9", minute="0")  # Daily at 9 AM
   CrontabSchedule(day_of_week="0", hour="9")  # Monday at 9 AM
   CrontabSchedule(day_of_month="1", hour="0")  # 1st of month

3. SOLAR (sunrise/sunset):
   Use for:
   - Location-based scheduling
   - Daylight-dependent tasks

COMMON PATTERNS:

1. Database Maintenance:
   # Run at night when traffic is low
   CrontabSchedule(hour="2", minute="0")

2. Report Generation:
   # Business hours
   CrontabSchedule(hour="9", minute="0")

3. Cache Warming:
   # Before peak hours
   IntervalSchedule(every=900)  # 15 minutes

4. Data Sync:
   # Every 5 minutes
   IntervalSchedule(every=300)

5. Cleanup Tasks:
   # Weekly on Sunday
   CrontabSchedule(day_of_week="6", hour="3")

PRODUCTION CONFIGURATION:

beat_schedule = {
    'cleanup-old-sessions': {
        'task': 'app.cleanup_sessions',
        'schedule': crontab(hour=2, minute=0),
    },
    'send-daily-report': {
        'task': 'app.daily_report',
        'schedule': crontab(hour=9, minute=0),
        'args': (report_type,)
    },
    'refresh-cache': {
        'task': 'app.refresh_cache',
        'schedule': 900.0,  # Every 15 minutes
    },
}

MONITORING:
  - Track task execution times
  - Alert on missed schedules
  - Log periodic task failures
  - Monitor beat scheduler health

FAULT TOLERANCE:
  - Use idempotent tasks
  - Handle missed schedules gracefully
  - Set task expiration
  - Implement locking for critical tasks

SCALING:
  - Run single beat instance (uses locks)
  - Distribute workers horizontally
  - Use timezone-aware scheduling
  - Consider clock skew in clusters

COMMON PITFALLS:
  ✗ Multiple beat instances (duplicate tasks)
  ✗ Long-running periodic tasks (use async)
  ✗ No expiration on scheduled tasks
  ✗ Ignoring timezone configuration

ADVANCED PATTERNS:

1. Dynamic schedules:
   # Load from database
   beat.add_periodic_task(
       schedule=user.preferred_schedule,
       task='send_reminder'
   )

2. Conditional execution:
   @periodic_task(schedule=interval(60))
   def conditional_task():
       if should_run():
           do_work()

3. Chained periodic tasks:
   @periodic_task(schedule=crontab(hour=2))
   def nightly_workflow():
       cleanup.delay()
       process.delay()
       report.delay()

TIMEZONE HANDLING:
  - Set CELERY_TIMEZONE = 'UTC'
  - Use timezone-aware datetimes
  - Document timezone in cron expressions

Production note: Real Celery Beat provides:
  - Persistent schedules (database backend)
  - Task locking (prevent duplicates)
  - Timezone support
  - Solar schedules
  - Dynamic schedule updates
  - Beat scheduler HA with Redis/DB locks
  - Integration with Django/Flask
  - Admin UI for schedule management
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 13 COMPLETE: Celery Basics, Scheduling & Periodic Tasks")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 815: Celery Basics")
    print(f"  - Lesson 816: Celery Task Scheduling")
    print(f"  - Lesson 817: Celery Periodic Tasks")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
