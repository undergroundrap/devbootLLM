#!/usr/bin/env python3
"""
Upgrade Celery task queue and pytest testing lessons
"""

import json
import sys

def upgrade_lesson_823():
    """Celery - RabbitMQ Backend"""
    return '''# Celery with RabbitMQ Backend
# In production: pip install celery[librabbitmq] kombu

"""
Celery Distributed Task Queue with RabbitMQ

Complete Celery task queue implementation with:
- RabbitMQ message broker
- Task routing and queues
- Task priorities and expiration
- Result backend with Redis
- Task retries and error handling
- Monitoring and task events

Used by: Instagram, Mozilla, Robinhood for async task processing
"""

import time
import json
import uuid
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from collections import deque
import functools


# ============================================================================
# RabbitMQ Broker (simulated)
# ============================================================================

class RabbitMQQueue:
    """Simulated RabbitMQ queue"""

    def __init__(self, name: str):
        self.name = name
        self.messages = deque()
        self.dlq = deque()  # Dead letter queue

    def publish(self, message: Dict, priority: int = 0, expiration: int = None):
        """Publish message to queue"""
        msg = {
            'body': message,
            'priority': priority,
            'expiration': expiration,
            'timestamp': time.time(),
            'message_id': str(uuid.uuid4())
        }
        self.messages.append(msg)

    def consume(self) -> Optional[Dict]:
        """Consume message from queue"""
        if not self.messages:
            return None

        # Sort by priority (higher first)
        sorted_messages = sorted(self.messages, key=lambda x: x['priority'], reverse=True)

        for msg in sorted_messages:
            # Check expiration
            if msg['expiration']:
                age = time.time() - msg['timestamp']
                if age > msg['expiration']:
                    self.messages.remove(msg)
                    self.dlq.append(msg)  # Move to dead letter queue
                    continue

            self.messages.remove(msg)
            return msg

        return None


class RabbitMQBroker:
    """Simulated RabbitMQ broker"""

    def __init__(self, url: str):
        self.url = url
        self.queues: Dict[str, RabbitMQQueue] = {}
        self.exchanges: Dict[str, Dict] = {}
        self.bindings: Dict[str, List[str]] = {}  # exchange -> queues

    def declare_queue(self, name: str):
        """Declare a queue"""
        if name not in self.queues:
            self.queues[name] = RabbitMQQueue(name)

    def declare_exchange(self, name: str, exchange_type: str = "direct"):
        """Declare an exchange"""
        self.exchanges[name] = {'type': exchange_type}
        if name not in self.bindings:
            self.bindings[name] = []

    def bind_queue(self, queue: str, exchange: str, routing_key: str = ""):
        """Bind queue to exchange"""
        if exchange not in self.bindings:
            self.bindings[exchange] = []

        self.bindings[exchange].append({
            'queue': queue,
            'routing_key': routing_key
        })

    def publish(self, exchange: str, routing_key: str, message: Dict, **kwargs):
        """Publish message to exchange"""
        if exchange not in self.bindings:
            return

        # Route to appropriate queues
        for binding in self.bindings[exchange]:
            if binding['routing_key'] == routing_key or binding['routing_key'] == '':
                queue_name = binding['queue']
                if queue_name in self.queues:
                    self.queues[queue_name].publish(message, **kwargs)

    def consume(self, queue: str) -> Optional[Dict]:
        """Consume from queue"""
        if queue not in self.queues:
            return None

        return self.queues[queue].consume()


# ============================================================================
# Redis Result Backend (simulated)
# ============================================================================

class RedisBackend:
    """Simulated Redis result backend"""

    def __init__(self, url: str):
        self.url = url
        self.storage: Dict[str, Dict] = {}

    def store_result(self, task_id: str, result: Any, state: str):
        """Store task result"""
        self.storage[task_id] = {
            'result': result,
            'state': state,
            'timestamp': time.time()
        }

    def get_result(self, task_id: str) -> Optional[Dict]:
        """Get task result"""
        return self.storage.get(task_id)

    def delete_result(self, task_id: str):
        """Delete task result"""
        if task_id in self.storage:
            del self.storage[task_id]


# ============================================================================
# Celery Task
# ============================================================================

class Task:
    """Celery task"""

    def __init__(self, func: Callable, app, name: str = None,
                 bind: bool = False, max_retries: int = 3,
                 default_retry_delay: int = 60):
        self.func = func
        self.app = app
        self.name = name or func.__name__
        self.bind = bind
        self.max_retries = max_retries
        self.default_retry_delay = default_retry_delay
        self.retries = 0

    def apply_async(self, args=None, kwargs=None, queue: str = None,
                    priority: int = 0, countdown: int = 0, expires: int = None):
        """Execute task asynchronously"""
        task_id = str(uuid.uuid4())

        # Create task message
        message = {
            'task': self.name,
            'id': task_id,
            'args': args or [],
            'kwargs': kwargs or {},
            'retries': 0
        }

        # Determine queue
        target_queue = queue or self.app.conf['task_default_queue']

        # Publish to broker
        self.app.broker.publish(
            exchange='celery',
            routing_key=target_queue,
            message=message,
            priority=priority,
            expiration=expires
        )

        return AsyncResult(task_id, self.app)

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async with args"""
        return self.apply_async(args=args, kwargs=kwargs)

    def retry(self, exc=None, countdown: int = None, max_retries: int = None):
        """Retry task"""
        max_retries = max_retries or self.max_retries
        countdown = countdown or self.default_retry_delay

        self.retries += 1

        if self.retries > max_retries:
            raise exc or Exception("Max retries exceeded")

        # Requeue task
        time.sleep(countdown / 1000)  # Simulate delay


class AsyncResult:
    """Task result handle"""

    def __init__(self, task_id: str, app):
        self.task_id = task_id
        self.app = app

    def get(self, timeout: int = None) -> Any:
        """Wait for result"""
        start = time.time()

        while True:
            result = self.app.backend.get_result(self.task_id)

            if result:
                if result['state'] == 'SUCCESS':
                    return result['result']
                elif result['state'] == 'FAILURE':
                    raise Exception(f"Task failed: {result['result']}")

            if timeout and (time.time() - start) > timeout:
                raise TimeoutError("Task timeout")

            time.sleep(0.1)

    @property
    def state(self) -> str:
        """Get task state"""
        result = self.app.backend.get_result(self.task_id)
        return result['state'] if result else 'PENDING'

    @property
    def ready(self) -> bool:
        """Check if task completed"""
        return self.state in ('SUCCESS', 'FAILURE')


# ============================================================================
# Celery Application
# ============================================================================

class Celery:
    """Celery application"""

    def __init__(self, main: str, broker: str = None, backend: str = None):
        self.main = main
        self.broker = RabbitMQBroker(broker or 'amqp://localhost')
        self.backend = RedisBackend(backend or 'redis://localhost')
        self.tasks: Dict[str, Task] = {}

        # Configuration
        self.conf = {
            'broker_url': broker,
            'result_backend': backend,
            'task_serializer': 'json',
            'result_serializer': 'json',
            'accept_content': ['json'],
            'timezone': 'UTC',
            'task_default_queue': 'celery',
            'task_routes': {},
            'task_annotations': {},
        }

        # Setup default exchange and queues
        self.broker.declare_exchange('celery', 'direct')
        self.broker.declare_queue('celery')
        self.broker.bind_queue('celery', 'celery', 'celery')

    def task(self, *args, **kwargs):
        """Task decorator"""
        def decorator(func):
            task = Task(func, self, **kwargs)
            self.tasks[task.name] = task

            @functools.wraps(func)
            def wrapper(*call_args, **call_kwargs):
                return func(*call_args, **call_kwargs)

            wrapper.apply_async = task.apply_async
            wrapper.delay = task.delay
            wrapper.retry = task.retry

            return wrapper

        # Support @app.task or @app.task()
        if len(args) == 1 and callable(args[0]):
            return decorator(args[0])
        return decorator

    def send_task(self, name: str, args=None, kwargs=None, **options):
        """Send task by name"""
        if name in self.tasks:
            return self.tasks[name].apply_async(args, kwargs, **options)
        raise ValueError(f"Task {name} not found")

    def Worker(self, queues: List[str] = None):
        """Create worker"""
        return Worker(self, queues or ['celery'])


# ============================================================================
# Celery Worker
# ============================================================================

class Worker:
    """Celery worker"""

    def __init__(self, app: Celery, queues: List[str]):
        self.app = app
        self.queues = queues
        self.running = False

    def start(self):
        """Start worker"""
        self.running = True
        print(f"Worker started, consuming from queues: {self.queues}")

        while self.running:
            for queue in self.queues:
                message = self.app.broker.consume(queue)

                if message:
                    self.process_task(message)

            time.sleep(0.1)

    def process_task(self, message: Dict):
        """Process task message"""
        task_name = message['body']['task']
        task_id = message['body']['id']
        args = message['body']['args']
        kwargs = message['body']['kwargs']

        print(f"\\nProcessing task: {task_name} (ID: {task_id})")

        if task_name not in self.app.tasks:
            print(f"Task {task_name} not found!")
            return

        task = self.app.tasks[task_name]

        try:
            # Execute task
            result = task.func(*args, **kwargs)

            # Store result
            self.app.backend.store_result(task_id, result, 'SUCCESS')
            print(f"Task {task_id} completed: {result}")

        except Exception as e:
            # Store error
            self.app.backend.store_result(task_id, str(e), 'FAILURE')
            print(f"Task {task_id} failed: {e}")

    def stop(self):
        """Stop worker"""
        self.running = False
        print("Worker stopped")


# ============================================================================
# Example Application
# ============================================================================

# Create Celery app
app = Celery(
    'tasks',
    broker='amqp://localhost:5672//',
    backend='redis://localhost:6379/0'
)

# Configure task routing
app.conf.update(
    task_routes={
        'tasks.send_email': {'queue': 'email'},
        'tasks.process_image': {'queue': 'media'},
        'tasks.generate_report': {'queue': 'reports'},
    }
)

# Create queues
for queue_name in ['email', 'media', 'reports']:
    app.broker.declare_queue(queue_name)
    app.broker.bind_queue(queue_name, 'celery', queue_name)


# Define tasks

@app.task
def add(x, y):
    """Simple add task"""
    print(f"Computing {x} + {y}")
    return x + y


@app.task
def send_email(to: str, subject: str, body: str):
    """Send email task"""
    print(f"Sending email to {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    time.sleep(0.5)  # Simulate sending
    return f"Email sent to {to}"


@app.task
def process_image(image_url: str, filters: List[str]):
    """Process image task"""
    print(f"Processing image: {image_url}")
    print(f"Applying filters: {filters}")
    time.sleep(1)  # Simulate processing
    return f"Image processed with {len(filters)} filters"


@app.task(bind=True, max_retries=3)
def unreliable_task(self, value: int):
    """Task that might fail and retry"""
    print(f"Attempting task (retry {self.retries})")

    # Simulate 50% failure rate
    import random
    if random.random() < 0.5:
        raise Exception("Task failed randomly")

    return f"Success: {value * 2}"


# ============================================================================
# Main Example
# ============================================================================

def main():
    print("=" * 80)
    print("CELERY WITH RABBITMQ BACKEND")
    print("=" * 80)

    # 1. Basic task execution
    print("\\n1. BASIC TASK EXECUTION")
    print("-" * 80)

    result = add.delay(4, 6)
    print(f"Task ID: {result.task_id}")

    # Process task
    worker = Worker(app, ['celery'])
    message = app.broker.consume('celery')
    if message:
        worker.process_task(message)

    # Get result
    final_result = result.get(timeout=5)
    print(f"Result: {final_result}")

    # 2. Task routing to different queues
    print("\\n2. TASK ROUTING")
    print("-" * 80)

    # Send email task to email queue
    email_task = send_email.apply_async(
        args=['user@example.com', 'Hello', 'Welcome!'],
        queue='email'
    )
    print(f"Email task: {email_task.task_id} -> email queue")

    # Process from email queue
    email_msg = app.broker.consume('email')
    if email_msg:
        worker.process_task(email_msg)

    # 3. Task priorities
    print("\\n3. TASK PRIORITIES")
    print("-" * 80)

    # High priority task
    high_priority = add.apply_async(args=[10, 20], priority=9)
    print(f"High priority task: {high_priority.task_id}")

    # Low priority task
    low_priority = add.apply_async(args=[1, 2], priority=1)
    print(f"Low priority task: {low_priority.task_id}")

    # Process tasks (high priority first)
    for i in range(2):
        msg = app.broker.consume('celery')
        if msg:
            print(f"\\nProcessing with priority {msg['priority']}")
            worker.process_task(msg)

    # 4. Task expiration
    print("\\n4. TASK EXPIRATION")
    print("-" * 80)

    expired_task = add.apply_async(args=[5, 5], expires=1)  # Expires in 1 second
    print(f"Task with 1s expiration: {expired_task.task_id}")

    time.sleep(1.5)  # Wait for expiration

    msg = app.broker.consume('celery')
    if msg:
        print("Task consumed before expiration")
    else:
        print("Task expired and moved to dead letter queue")

    #  5. Task chains and workflows
    print("\\n5. TASK WORKFLOW")
    print("-" * 80)

    # Schedule multiple related tasks
    tasks = [
        send_email.delay('user1@example.com', 'Report', 'Your report is ready'),
        send_email.delay('user2@example.com', 'Report', 'Your report is ready'),
        send_email.delay('user3@example.com', 'Report', 'Your report is ready'),
    ]

    print(f"Scheduled {len(tasks)} email tasks")

    # Process all
    for _ in range(len(tasks)):
        msg = app.broker.consume('email')
        if msg:
            worker.process_task(msg)

    print("\\n" + "=" * 80)
    print("CELERY + RABBITMQ BEST PRACTICES")
    print("=" * 80)
    print("""
1. TASK DESIGN:
   - Keep tasks idempotent (can run multiple times safely)
   - Tasks should be atomic and focused
   - Use task routing for different workloads
   - Set appropriate timeouts

2. QUEUES:
   - Separate queues by priority/type (email, media, reports)
   - Monitor queue lengths
   - Use dead letter queues for failed tasks
   - Set message TTL appropriately

3. RETRY LOGIC:
   - Implement exponential backoff
   - Set max_retries limit
   - Log retry attempts
   - Handle max retries gracefully

4. MONITORING:
   - Monitor queue depths
   - Track task success/failure rates
   - Set up alerts for queue buildup
   - Use Flower for visualization

5. RABBITMQ CONFIGURATION:
   - Use durable queues for persistence
   - Enable publisher confirms
   - Configure prefetch count
   - Use clustering for high availability

6. PRODUCTION:
   - Run multiple workers
   - Use worker autoscaling
   - Implement circuit breakers
   - Monitor memory usage
   - Set up logging and error tracking
""")

    print("\\n✓ Celery + RabbitMQ complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_822():
    """Celery - Redis Backend"""
    return '''# Celery with Redis Backend
# In production: pip install celery[redis] redis

"""
Celery with Redis as Broker and Backend

Complete Celery setup using Redis for:
- Message broker (pub/sub for tasks)
- Result backend (storing task results)
- Task scheduling and periodic tasks
- Task prioritization
- Rate limiting

Used by: Uber, Lyft, Pinterest for async processing
"""

import time
import json
import uuid
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from collections import deque, defaultdict
import functools


# ============================================================================
# Redis Backend (simulated)
# ============================================================================

class Redis:
    """Simulated Redis client"""

    def __init__(self, url: str):
        self.url = url
        self.storage: Dict[str, Any] = {}
        self.lists: Dict[str, deque] = defaultdict(deque)
        self.sorted_sets: Dict[str, List] = defaultdict(list)
        self.expirations: Dict[str, float] = {}

    def set(self, key: str, value: Any, ex: int = None):
        """Set key-value"""
        self.storage[key] = value
        if ex:
            self.expirations[key] = time.time() + ex

    def get(self, key: str) -> Optional[Any]:
        """Get value"""
        if key in self.expirations:
            if time.time() > self.expirations[key]:
                del self.storage[key]
                del self.expirations[key]
                return None
        return self.storage.get(key)

    def delete(self, key: str):
        """Delete key"""
        if key in self.storage:
            del self.storage[key]
        if key in self.expirations:
            del self.expirations[key]

    def lpush(self, key: str, value: Any):
        """Push to list (left)"""
        self.lists[key].appendleft(value)

    def rpop(self, key: str) -> Optional[Any]:
        """Pop from list (right)"""
        if not self.lists[key]:
            return None
        return self.lists[key].pop()

    def brpop(self, keys: List[str], timeout: int = 0) -> Optional[tuple]:
        """Blocking right pop"""
        start = time.time()

        while True:
            for key in keys:
                if self.lists[key]:
                    return (key, self.lists[key].pop())

            if timeout and (time.time() - start) > timeout:
                return None

            time.sleep(0.01)

    def zadd(self, key: str, mapping: Dict[str, float]):
        """Add to sorted set"""
        for member, score in mapping.items():
            self.sorted_sets[key].append((member, score))
            self.sorted_sets[key].sort(key=lambda x: x[1])

    def zrangebyscore(self, key: str, min_score: float, max_score: float) -> List:
        """Get range from sorted set by score"""
        result = []
        for member, score in self.sorted_sets[key]:
            if min_score <= score <= max_score:
                result.append(member)
        return result

    def zrem(self, key: str, *members):
        """Remove from sorted set"""
        self.sorted_sets[key] = [
            (m, s) for m, s in self.sorted_sets[key]
            if m not in members
        ]


# ============================================================================
# Celery Task
# ============================================================================

class Task:
    """Celery task"""

    def __init__(self, func: Callable, app, name: str = None,
                 bind: bool = False, rate_limit: str = None):
        self.func = func
        self.app = app
        self.name = name or func.__name__
        self.bind = bind
        self.rate_limit = rate_limit
        self.request = None  # Task execution context

    def apply_async(self, args=None, kwargs=None, countdown: int = 0,
                    eta: datetime = None, priority: int = 5):
        """Execute task asynchronously"""
        task_id = str(uuid.uuid4())

        # Create task message
        message = {
            'id': task_id,
            'task': self.name,
            'args': args or [],
            'kwargs': kwargs or {},
            'retries': 0,
            'priority': priority
        }

        # Schedule for later if countdown/eta provided
        if countdown or eta:
            schedule_time = time.time() + countdown if countdown else eta.timestamp()
            self.app.redis.zadd('celery-schedule', {json.dumps(message): schedule_time})
        else:
            # Push to queue immediately
            queue_name = f'celery:{priority}'
            self.app.redis.lpush(queue_name, json.dumps(message))

        return AsyncResult(task_id, self.app)

    def delay(self, *args, **kwargs):
        """Shortcut for apply_async"""
        return self.apply_async(args=args, kwargs=kwargs)


class AsyncResult:
    """Task result handle"""

    def __init__(self, task_id: str, app):
        self.task_id = task_id
        self.app = app

    def get(self, timeout: int = None) -> Any:
        """Wait for and return result"""
        start = time.time()

        while True:
            result = self.app.redis.get(f'celery-task-meta-{self.task_id}')

            if result:
                result_data = json.loads(result)
                if result_data['status'] == 'SUCCESS':
                    return result_data['result']
                elif result_data['status'] == 'FAILURE':
                    raise Exception(f"Task failed: {result_data['result']}")

            if timeout and (time.time() - start) > timeout:
                raise TimeoutError("Task timeout")

            time.sleep(0.1)

    @property
    def state(self) -> str:
        """Get task state"""
        result = self.app.redis.get(f'celery-task-meta-{self.task_id}')
        if result:
            return json.loads(result)['status']
        return 'PENDING'

    @property
    def ready(self) -> bool:
        """Check if task is complete"""
        return self.state in ('SUCCESS', 'FAILURE')


# ============================================================================
# Celery Application
# ============================================================================

class Celery:
    """Celery application with Redis"""

    def __init__(self, main: str, broker: str = None, backend: str = None):
        self.main = main
        self.redis = Redis(broker or 'redis://localhost:6379/0')
        self.tasks: Dict[str, Task] = {}

        # Configuration
        self.conf = {
            'broker_url': broker,
            'result_backend': backend or broker,
            'task_serializer': 'json',
            'result_serializer': 'json',
            'accept_content': ['json'],
            'timezone': 'UTC',
            'result_expires': 3600,
            'task_track_started': True,
        }

    def task(self, *args, **kwargs):
        """Task decorator"""
        def decorator(func):
            task = Task(func, self, **kwargs)
            self.tasks[task.name] = task

            @functools.wraps(func)
            def wrapper(*call_args, **call_kwargs):
                return func(*call_args, **call_kwargs)

            wrapper.apply_async = task.apply_async
            wrapper.delay = task.delay

            return wrapper

        if len(args) == 1 and callable(args[0]):
            return decorator(args[0])
        return decorator

    def Worker(self, queues: List[int] = None):
        """Create worker"""
        return Worker(self, queues or [5])  # Default priority 5


# ============================================================================
# Celery Worker
# ============================================================================

class Worker:
    """Celery worker"""

    def __init__(self, app: Celery, priorities: List[int]):
        self.app = app
        self.priorities = sorted(priorities, reverse=True)  # High to low
        self.running = False

    def start(self):
        """Start worker"""
        self.running = True
        print(f"Worker started, priorities: {self.priorities}")

        while self.running:
            # Check scheduled tasks first
            self.check_scheduled_tasks()

            # Process tasks by priority
            for priority in self.priorities:
                queue_name = f'celery:{priority}'
                message_json = self.app.redis.rpop(queue_name)

                if message_json:
                    message = json.loads(message_json)
                    self.process_task(message)
                    break  # Process one task then check priorities again

            time.sleep(0.1)

    def check_scheduled_tasks(self):
        """Move scheduled tasks to queue if due"""
        now = time.time()
        due_tasks = self.app.redis.zrangebyscore('celery-schedule', 0, now)

        for task_json in due_tasks:
            message = json.loads(task_json)
            priority = message.get('priority', 5)
            queue_name = f'celery:{priority}'

            # Move to active queue
            self.app.redis.lpush(queue_name, task_json)
            self.app.redis.zrem('celery-schedule', task_json)

    def process_task(self, message: Dict):
        """Process task"""
        task_name = message['task']
        task_id = message['id']
        args = message['args']
        kwargs = message['kwargs']

        print(f"\\nProcessing: {task_name} (ID: {task_id[:8]}...)")

        if task_name not in self.app.tasks:
            print(f"Task {task_name} not found!")
            return

        task = self.app.tasks[task_name]

        try:
            # Execute task
            result = task.func(*args, **kwargs)

            # Store result
            result_data = {
                'status': 'SUCCESS',
                'result': result,
                'task_id': task_id,
                'date_done': datetime.now().isoformat()
            }

            self.app.redis.set(
                f'celery-task-meta-{task_id}',
                json.dumps(result_data),
                ex=self.app.conf['result_expires']
            )

            print(f"✓ Task completed: {result}")

        except Exception as e:
            # Store error
            result_data = {
                'status': 'FAILURE',
                'result': str(e),
                'task_id': task_id,
                'date_done': datetime.now().isoformat()
            }

            self.app.redis.set(
                f'celery-task-meta-{task_id}',
                json.dumps(result_data),
                ex=self.app.conf['result_expires']
            )

            print(f"✗ Task failed: {e}")

    def stop(self):
        """Stop worker"""
        self.running = False


# ============================================================================
# Example Application
# ============================================================================

app = Celery(
    'myapp',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@app.task
def add(x, y):
    """Add two numbers"""
    return x + y


@app.task
def multiply(x, y):
    """Multiply two numbers"""
    return x * y


@app.task(rate_limit='10/m')
def send_notification(user_id: int, message: str):
    """Send notification (rate limited)"""
    print(f"Sending to user {user_id}: {message}")
    time.sleep(0.5)
    return f"Notification sent to {user_id}"


@app.task
def process_data(data: List[int]):
    """Process data"""
    print(f"Processing {len(data)} items...")
    result = sum(data) / len(data)
    return result


# ============================================================================
# Main Example
# ============================================================================

def main():
    print("=" * 80)
    print("CELERY WITH REDIS BACKEND")
    print("=" * 80)

    # 1. Basic task execution
    print("\\n1. BASIC TASK EXECUTION")
    print("-" * 80)

    result = add.delay(10, 32)
    print(f"Task ID: {result.task_id}")

    # Simulate worker processing
    worker = Worker(app, [5])
    message_json = app.redis.rpop('celery:5')
    if message_json:
        worker.process_task(json.loads(message_json))

    # Get result
    final_result = result.get(timeout=5)
    print(f"Result: {final_result}")

    # 2. Task priorities
    print("\\n2. TASK PRIORITIES")
    print("-" * 80)

    # High priority
    high = add.apply_async(args=[100, 200], priority=9)
    print(f"High priority (9): {high.task_id[:8]}")

    # Normal priority
    normal = add.apply_async(args=[10, 20], priority=5)
    print(f"Normal priority (5): {normal.task_id[:8]}")

    # Low priority
    low = add.apply_async(args=[1, 2], priority=1)
    print(f"Low priority (1): {low.task_id[:8]}")

    # Process by priority
    priority_worker = Worker(app, [9, 5, 1])
    for _ in range(3):
        priority_worker.check_scheduled_tasks()
        for p in [9, 5, 1]:
            msg_json = app.redis.rpop(f'celery:{p}')
            if msg_json:
                priority_worker.process_task(json.loads(msg_json))
                break

    # 3. Scheduled tasks
    print("\\n3. SCHEDULED TASKS (Countdown)")
    print("-" * 80)

    # Schedule task for 2 seconds from now
    scheduled = add.apply_async(args=[5, 7], countdown=2)
    print(f"Task scheduled for 2 seconds: {scheduled.task_id[:8]}")

    print("Waiting 2 seconds...")
    time.sleep(2)

    # Check scheduled tasks and process
    priority_worker.check_scheduled_tasks()
    msg_json = app.redis.rpop('celery:5')
    if msg_json:
        priority_worker.process_task(json.loads(msg_json))
        result_val = scheduled.get(timeout=1)
        print(f"Scheduled task result: {result_val}")

    # 4. Multiple tasks
    print("\\n4. BATCH TASK EXECUTION")
    print("-" * 80)

    tasks = []
    for i in range(5):
        task = multiply.delay(i, 2)
        tasks.append(task)
        print(f"Queued task {i}: {task.task_id[:8]}")

    # Process all tasks
    for _ in range(5):
        msg_json = app.redis.rpop('celery:5')
        if msg_json:
            priority_worker.process_task(json.loads(msg_json))

    # Get all results
    print("\\nResults:")
    for i, task in enumerate(tasks):
        try:
            result_val = task.get(timeout=1)
            print(f"  Task {i}: {result_val}")
        except:
            print(f"  Task {i}: Not ready")

    # 5. Result expiration
    print("\\n5. RESULT EXPIRATION")
    print("-" * 80)

    quick_task = add.delay(1, 1)
    msg_json = app.redis.rpop('celery:5')
    if msg_json:
        priority_worker.process_task(json.loads(msg_json))

    print(f"Task state: {quick_task.state}")
    print(f"Result stored with {app.conf['result_expires']}s expiration")

    print("\\n" + "=" * 80)
    print("CELERY + REDIS BEST PRACTICES")
    print("=" * 80)
    print("""
1. REDIS AS BROKER:
   - Fast and simple setup
   - Good for small to medium workloads
   - Use Redis Sentinel for HA
   - Monitor Redis memory usage

2. TASK PRIORITIES:
   - Use 0-9 priority scale (9 = highest)
   - Separate queues per priority
   - Workers process high priority first
   - Balance priorities to avoid starvation

3. RESULT BACKEND:
   - Set appropriate result_expires
   - Use Redis for fast result access
   - Consider database for long-term storage
   - Clean up old results regularly

4. SCHEDULING:
   - Use countdown for relative scheduling
   - Use eta for absolute scheduling
   - Implement periodic tasks with Celery Beat
   - Monitor scheduled task queue depth

5. RATE LIMITING:
   - Set rate_limit per task
   - Format: "10/m" (10 per minute)
   - Protect external services
   - Use Redis for rate limit tracking

6. PRODUCTION:
   - Use connection pooling
   - Enable task result compression
   - Set worker prefetch multiplier
   - Monitor task latency and throughput
   - Use multiple workers for scaling
""")

    print("\\n✓ Celery + Redis complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: Celery Task Queue Lessons")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (823, upgrade_lesson_823, "Celery - RabbitMQ Backend"),
        (822, upgrade_lesson_822, "Celery - Redis Backend"),
    ]

    for lesson_id, upgrade_func, title in upgrades:
        lesson = next((l for l in lessons if l['id'] == lesson_id), None)
        if not lesson:
            print(f"\nLesson {lesson_id} not found!")
            continue

        old_length = len(lesson.get('fullSolution', ''))
        new_solution = upgrade_func()
        lesson['fullSolution'] = new_solution
        new_length = len(new_solution)

        print(f"\nLesson {lesson_id}: {title}")
        print(f"  {old_length:,} -> {new_length:,} chars (+{new_length - old_length:,}, +{((new_length - old_length) / old_length * 100):.1f}%)")

    # Save
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 80)
    print("CELERY TASK QUEUE BATCH COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
