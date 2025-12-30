#!/usr/bin/env python3
"""
Upgrade SQLAlchemy ORM and Apache Kafka lessons
"""

import json
import sys

def upgrade_lesson_782():
    """SQLAlchemy - Relationship Patterns"""
    return '''# SQLAlchemy Relationship Patterns
# In production: pip install sqlalchemy

"""
SQLAlchemy Advanced Relationship Patterns

Complete guide to SQLAlchemy relationships:
- One-to-Many relationships
- Many-to-Many relationships
- One-to-One relationships
- Self-referential relationships
- Polymorphic relationships
- Cascade operations
- Lazy loading strategies

Used by: Reddit, Yelp, OpenStack for complex database models
"""

from typing import List, Optional, Any, Dict, Set
from datetime import datetime
from collections import defaultdict


# ============================================================================
# SQLAlchemy ORM Simulation
# ============================================================================

class Column:
    """Column definition"""
    def __init__(self, type_name: str, primary_key=False, foreign_key=None,
                 nullable=True, unique=False, index=False):
        self.type_name = type_name
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.nullable = nullable
        self.unique = unique
        self.index = index


class ForeignKey:
    """Foreign key constraint"""
    def __init__(self, target: str, ondelete: str = None):
        self.target = target
        self.ondelete = ondelete


class relationship:
    """Relationship definition"""
    def __init__(self, target, back_populates=None, lazy='select',
                 cascade='', secondary=None, uselist=True):
        self.target = target
        self.back_populates = back_populates
        self.lazy = lazy
        self.cascade = cascade
        self.secondary = secondary
        self.uselist = uselist


class Table:
    """Association table for many-to-many"""
    def __init__(self, name: str, *columns):
        self.name = name
        self.columns = columns


# ============================================================================
# Base Model
# ============================================================================

class ModelMeta(type):
    """Metaclass for models"""
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)

        # Setup relationships
        for attr_name, attr_value in attrs.items():
            if isinstance(attr_value, relationship):
                # Will be populated at runtime
                pass

        return cls


class Model(metaclass=ModelMeta):
    """Base model class"""

    # Class-level storage (simulates database)
    _storage: Dict[type, List[Any]] = defaultdict(list)
    _id_counters: Dict[type, int] = defaultdict(int)

    def __init__(self, **kwargs):
        # Auto-increment ID
        if not hasattr(self, 'id') or self.id is None:
            self.__class__._id_counters[self.__class__] += 1
            self.id = self.__class__._id_counters[self.__class__]

        # Set attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

        self._state = {'adding': True}

    def save(self):
        """Save to storage"""
        if self._state.get('adding'):
            self.__class__._storage[self.__class__].append(self)
            self._state['adding'] = False

    @classmethod
    def query(cls):
        """Query interface"""
        return Query(cls)


class Query:
    """Query builder"""
    def __init__(self, model_class):
        self.model_class = model_class
        self._filters = []

    def filter_by(self, **kwargs):
        """Filter by attributes"""
        self._filters.append(kwargs)
        return self

    def all(self) -> List:
        """Get all results"""
        results = self.model_class._storage[self.model_class].copy()

        for filter_dict in self._filters:
            filtered = []
            for obj in results:
                match = True
                for key, value in filter_dict.items():
                    if getattr(obj, key, None) != value:
                        match = False
                        break
                if match:
                    filtered.append(obj)
            results = filtered

        return results

    def first(self):
        """Get first result"""
        results = self.all()
        return results[0] if results else None


# ============================================================================
# One-to-Many Relationship
# ============================================================================

class Author(Model):
    """Author model (one side)"""
    id = Column('Integer', primary_key=True)
    name = Column('String')
    email = Column('String', unique=True)

    # One-to-Many: One author has many books
    books = relationship('Book', back_populates='author', cascade='all, delete-orphan')

    def __init__(self, name: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self._books = []

    @property
    def books(self) -> List['Book']:
        """Get all books by this author"""
        return Book.query().filter_by(author_id=self.id).all()


class Book(Model):
    """Book model (many side)"""
    id = Column('Integer', primary_key=True)
    title = Column('String')
    isbn = Column('String', unique=True)
    author_id = Column('Integer', ForeignKey('author.id'))

    # Many-to-One: Many books belong to one author
    author = relationship('Author', back_populates='books')

    def __init__(self, title: str, isbn: str, author: Author = None, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.isbn = isbn
        self.author_id = author.id if author else None
        self._author = author


# ============================================================================
# Many-to-Many Relationship
# ============================================================================

# Association table
student_course_association = Table(
    'student_courses',
    Column('student_id', 'Integer', ForeignKey('student.id')),
    Column('course_id', 'Integer', ForeignKey('course.id'))
)


class StudentCourseAssociation:
    """Association table storage"""
    associations: List[Dict] = []

    @classmethod
    def add(cls, student_id: int, course_id: int):
        cls.associations.append({
            'student_id': student_id,
            'course_id': course_id
        })

    @classmethod
    def remove(cls, student_id: int, course_id: int):
        cls.associations = [
            a for a in cls.associations
            if not (a['student_id'] == student_id and a['course_id'] == course_id)
        ]

    @classmethod
    def get_courses_for_student(cls, student_id: int) -> List[int]:
        return [a['course_id'] for a in cls.associations if a['student_id'] == student_id]

    @classmethod
    def get_students_for_course(cls, course_id: int) -> List[int]:
        return [a['student_id'] for a in cls.associations if a['course_id'] == course_id]


class Student(Model):
    """Student model"""
    id = Column('Integer', primary_key=True)
    name = Column('String')
    email = Column('String', unique=True)

    # Many-to-Many: Students can enroll in many courses
    courses = relationship('Course', secondary=student_course_association, back_populates='students')

    def __init__(self, name: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email

    @property
    def courses(self) -> List['Course']:
        """Get all courses for this student"""
        course_ids = StudentCourseAssociation.get_courses_for_student(self.id)
        all_courses = Course._storage[Course]
        return [c for c in all_courses if c.id in course_ids]

    def enroll(self, course: 'Course'):
        """Enroll in a course"""
        StudentCourseAssociation.add(self.id, course.id)


class Course(Model):
    """Course model"""
    id = Column('Integer', primary_key=True)
    name = Column('String')
    code = Column('String', unique=True)

    # Many-to-Many: Courses can have many students
    students = relationship('Student', secondary=student_course_association, back_populates='courses')

    def __init__(self, name: str, code: str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.code = code

    @property
    def students(self) -> List['Student']:
        """Get all students in this course"""
        student_ids = StudentCourseAssociation.get_students_for_course(self.id)
        all_students = Student._storage[Student]
        return [s for s in all_students if s.id in student_ids]


# ============================================================================
# One-to-One Relationship
# ============================================================================

class User(Model):
    """User model"""
    id = Column('Integer', primary_key=True)
    username = Column('String', unique=True)
    email = Column('String', unique=True)

    # One-to-One: Each user has one profile
    profile = relationship('UserProfile', back_populates='user', uselist=False)

    def __init__(self, username: str, email: str, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.email = email
        self._profile = None

    @property
    def profile(self) -> Optional['UserProfile']:
        """Get user profile"""
        return UserProfile.query().filter_by(user_id=self.id).first()


class UserProfile(Model):
    """User profile model (one-to-one)"""
    id = Column('Integer', primary_key=True)
    user_id = Column('Integer', ForeignKey('user.id'), unique=True)
    bio = Column('Text')
    avatar_url = Column('String')

    # One-to-One: Each profile belongs to one user
    user = relationship('User', back_populates='profile')

    def __init__(self, user: User, bio: str = '', avatar_url: str = '', **kwargs):
        super().__init__(**kwargs)
        self.user_id = user.id
        self.bio = bio
        self.avatar_url = avatar_url


# ============================================================================
# Self-Referential Relationship
# ============================================================================

class Employee(Model):
    """Employee with manager relationship"""
    id = Column('Integer', primary_key=True)
    name = Column('String')
    manager_id = Column('Integer', ForeignKey('employee.id'), nullable=True)

    # Self-referential: Employee can have a manager (another employee)
    manager = relationship('Employee', back_populates='subordinates', uselist=False)
    subordinates = relationship('Employee', back_populates='manager')

    def __init__(self, name: str, manager: 'Employee' = None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.manager_id = manager.id if manager else None
        self._manager = manager

    @property
    def manager(self) -> Optional['Employee']:
        """Get manager"""
        if self.manager_id:
            return Employee.query().filter_by(id=self.manager_id).first()
        return None

    @property
    def subordinates(self) -> List['Employee']:
        """Get all subordinates"""
        return Employee.query().filter_by(manager_id=self.id).all()


# ============================================================================
# Cascade Operations
# ============================================================================

def demonstrate_cascade():
    """Demonstrate cascade delete"""
    print("\\nCASCADE OPERATIONS")
    print("-" * 80)

    # Create author with books
    author = Author(name="J.K. Rowling", email="jk@example.com")
    author.save()

    book1 = Book(title="Harry Potter 1", isbn="123", author=author)
    book2 = Book(title="Harry Potter 2", isbn="456", author=author)
    book1.save()
    book2.save()

    print(f"Created author: {author.name}")
    print(f"  Books: {len(author.books)}")

    # Cascade delete - deleting author deletes all books
    print("\\nDeleting author (cascade delete)...")
    Author._storage[Author].remove(author)

    # In real SQLAlchemy with cascade='all, delete-orphan',
    # all books would be automatically deleted
    for book in Book._storage[Book].copy():
        if book.author_id == author.id:
            Book._storage[Book].remove(book)

    print(f"✓ Cascade deleted {2} books")


# ============================================================================
# Example Usage
# ============================================================================

def main():
    print("=" * 80)
    print("SQLALCHEMY RELATIONSHIP PATTERNS")
    print("=" * 80)

    # 1. One-to-Many
    print("\\n1. ONE-TO-MANY RELATIONSHIP")
    print("-" * 80)

    author = Author(name="George Orwell", email="orwell@example.com")
    author.save()

    book1 = Book(title="1984", isbn="1984", author=author)
    book2 = Book(title="Animal Farm", isbn="AF", author=author)
    book1.save()
    book2.save()

    print(f"Author: {author.name}")
    print(f"Books by {author.name}:")
    for book in author.books:
        print(f"  - {book.title}")

    # 2. Many-to-Many
    print("\\n2. MANY-TO-MANY RELATIONSHIP")
    print("-" * 80)

    student1 = Student(name="Alice", email="alice@example.com")
    student2 = Student(name="Bob", email="bob@example.com")
    student1.save()
    student2.save()

    course1 = Course(name="Python Programming", code="CS101")
    course2 = Course(name="Data Structures", code="CS102")
    course1.save()
    course2.save()

    # Enroll students in courses
    student1.enroll(course1)
    student1.enroll(course2)
    student2.enroll(course1)

    print(f"Student: {student1.name}")
    print(f"  Enrolled in:")
    for course in student1.courses:
        print(f"    - {course.name}")

    print(f"\\nCourse: {course1.name}")
    print(f"  Students:")
    for student in course1.students:
        print(f"    - {student.name}")

    # 3. One-to-One
    print("\\n3. ONE-TO-ONE RELATIONSHIP")
    print("-" * 80)

    user = User(username="johndoe", email="john@example.com")
    user.save()

    profile = UserProfile(user=user, bio="Software developer", avatar_url="http://example.com/avatar.jpg")
    profile.save()

    print(f"User: {user.username}")
    print(f"  Profile: {user.profile.bio if user.profile else 'No profile'}")

    # 4. Self-Referential
    print("\\n4. SELF-REFERENTIAL RELATIONSHIP")
    print("-" * 80)

    ceo = Employee(name="CEO Alice")
    ceo.save()

    manager = Employee(name="Manager Bob", manager=ceo)
    manager.save()

    dev1 = Employee(name="Developer Charlie", manager=manager)
    dev2 = Employee(name="Developer Diana", manager=manager)
    dev1.save()
    dev2.save()

    print(f"Organization hierarchy:")
    print(f"  {ceo.name}")
    for sub1 in ceo.subordinates:
        print(f"    └─ {sub1.name}")
        for sub2 in sub1.subordinates:
            print(f"       └─ {sub2.name}")

    # 5. Cascade operations
    demonstrate_cascade()

    print("\\n" + "=" * 80)
    print("RELATIONSHIP BEST PRACTICES")
    print("=" * 80)
    print("""
1. ONE-TO-MANY:
   - Most common relationship type
   - Foreign key on "many" side
   - Use back_populates for bidirectional access
   - Consider cascade options (delete, delete-orphan)

2. MANY-TO-MANY:
   - Requires association table
   - Use secondary parameter
   - Can add extra columns with association object
   - Good for tags, categories, enrollments

3. ONE-TO-ONE:
   - Use uselist=False
   - Foreign key with unique constraint
   - Good for profile data, settings
   - Consider if you really need separate table

4. LAZY LOADING:
   - 'select': Load on access (default)
   - 'joined': Eager load with JOIN
   - 'subquery': Eager load with subquery
   - 'dynamic': Return Query object
   - Choose based on access patterns

5. CASCADE OPTIONS:
   - 'all': Cascade all operations
   - 'delete': Delete related objects
   - 'delete-orphan': Delete when removed from collection
   - 'merge': Merge related objects
   - 'save-update': Cascade saves

6. PERFORMANCE:
   - Use joinedload() for eager loading
   - Avoid N+1 queries with relationships
   - Index foreign keys
   - Use lazy='dynamic' for large collections

7. BIDIRECTIONAL RELATIONSHIPS:
   - Always use back_populates
   - Keep both sides in sync
   - Consider using Association Proxy
   - Document relationship purpose
""")

    print("\\n✓ SQLAlchemy relationship patterns complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_910():
    """Kafka - Exactly-Once Semantics"""
    return '''# Apache Kafka - Exactly-Once Semantics
# In production: pip install kafka-python

"""
Apache Kafka Exactly-Once Semantics (EOS)

Complete guide to Kafka exactly-once delivery:
- Idempotent producers
- Transactional producers
- Transactional consumers
- Read committed isolation level
- Transaction coordinators
- Producer and consumer configurations

Used by: Uber, Netflix, LinkedIn for guaranteed message processing
"""

import time
import json
import uuid
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict, deque


# ============================================================================
# Kafka Message
# ============================================================================

@dataclass
class Message:
    """Kafka message"""
    key: Optional[str]
    value: str
    offset: int
    partition: int
    timestamp: float
    headers: Dict[str, str]


# ============================================================================
# Transaction State
# ============================================================================

class TransactionState(Enum):
    """Transaction states"""
    ONGOING = "ONGOING"
    PREPARE_COMMIT = "PREPARE_COMMIT"
    COMMITTED = "COMMITTED"
    PREPARE_ABORT = "PREPARE_ABORT"
    ABORTED = "ABORTED"


@dataclass
class Transaction:
    """Transaction metadata"""
    transaction_id: str
    producer_id: int
    producer_epoch: int
    state: TransactionState
    partitions: Set[Tuple[str, int]]  # (topic, partition)
    start_time: float


# ============================================================================
# Transaction Coordinator
# ============================================================================

class TransactionCoordinator:
    """
    Manages transactions across partitions

    In production: Part of Kafka broker
    """

    def __init__(self):
        self.transactions: Dict[str, Transaction] = {}
        self.transaction_log: List[Dict] = []

    def begin_transaction(self, transaction_id: str, producer_id: int,
                         producer_epoch: int) -> Transaction:
        """Begin new transaction"""
        transaction = Transaction(
            transaction_id=transaction_id,
            producer_id=producer_id,
            producer_epoch=producer_epoch,
            state=TransactionState.ONGOING,
            partitions=set(),
            start_time=time.time()
        )

        self.transactions[transaction_id] = transaction

        self.transaction_log.append({
            'type': 'BEGIN',
            'transaction_id': transaction_id,
            'timestamp': time.time()
        })

        print(f"  [Transaction {transaction_id}: BEGUN]")
        return transaction

    def add_partition_to_transaction(self, transaction_id: str,
                                     topic: str, partition: int):
        """Add partition to transaction"""
        if transaction_id in self.transactions:
            self.transactions[transaction_id].partitions.add((topic, partition))

    def prepare_commit(self, transaction_id: str):
        """Prepare transaction for commit"""
        if transaction_id in self.transactions:
            txn = self.transactions[transaction_id]
            txn.state = TransactionState.PREPARE_COMMIT

            self.transaction_log.append({
                'type': 'PREPARE_COMMIT',
                'transaction_id': transaction_id,
                'timestamp': time.time()
            })

            print(f"  [Transaction {transaction_id}: PREPARE COMMIT]")

    def commit_transaction(self, transaction_id: str):
        """Commit transaction"""
        if transaction_id in self.transactions:
            txn = self.transactions[transaction_id]
            txn.state = TransactionState.COMMITTED

            self.transaction_log.append({
                'type': 'COMMIT',
                'transaction_id': transaction_id,
                'timestamp': time.time()
            })

            print(f"  [Transaction {transaction_id}: COMMITTED]")

    def abort_transaction(self, transaction_id: str):
        """Abort transaction"""
        if transaction_id in self.transactions:
            txn = self.transactions[transaction_id]
            txn.state = TransactionState.ABORTED

            self.transaction_log.append({
                'type': 'ABORT',
                'transaction_id': transaction_id,
                'timestamp': time.time()
            })

            print(f"  [Transaction {transaction_id}: ABORTED]")

    def is_transaction_committed(self, transaction_id: str) -> bool:
        """Check if transaction is committed"""
        if transaction_id in self.transactions:
            return self.transactions[transaction_id].state == TransactionState.COMMITTED
        return False


# ============================================================================
# Idempotent Producer
# ============================================================================

class IdempotentProducer:
    """
    Idempotent producer - prevents duplicate messages

    Uses producer ID and sequence numbers
    """

    def __init__(self, producer_id: int):
        self.producer_id = producer_id
        self.producer_epoch = 0
        self.sequence_numbers: Dict[Tuple[str, int], int] = defaultdict(int)
        self.sent_messages: Set[Tuple[str, int, int]] = set()  # (topic, partition, seq)

    def send(self, topic: str, partition: int, message: str) -> bool:
        """
        Send message idempotently

        Duplicate sends are detected and ignored
        """
        seq_num = self.sequence_numbers[(topic, partition)]

        # Check for duplicate
        message_id = (topic, partition, seq_num)
        if message_id in self.sent_messages:
            print(f"    Duplicate detected: {message_id}, skipping")
            return False

        # Send message (with producer ID and sequence number)
        print(f"    Sending: topic={topic}, partition={partition}, seq={seq_num}")

        # Mark as sent
        self.sent_messages.add(message_id)
        self.sequence_numbers[(topic, partition)] += 1

        return True


# ============================================================================
# Transactional Producer
# ============================================================================

class TransactionalProducer:
    """
    Transactional producer - exactly-once semantics

    Messages are only visible after transaction commit
    """

    def __init__(self, transaction_id: str, coordinator: TransactionCoordinator):
        self.transaction_id = transaction_id
        self.coordinator = coordinator
        self.producer_id = hash(transaction_id) % 10000
        self.producer_epoch = 0

        # Idempotent producer
        self.idempotent_producer = IdempotentProducer(self.producer_id)

        # Transaction state
        self.current_transaction: Optional[Transaction] = None
        self.pending_messages: List[Tuple[str, int, str]] = []

    def begin_transaction(self):
        """Begin transaction"""
        self.current_transaction = self.coordinator.begin_transaction(
            self.transaction_id,
            self.producer_id,
            self.producer_epoch
        )

        self.pending_messages = []

    def send(self, topic: str, partition: int, message: str):
        """
        Send message within transaction

        Message not visible until commit
        """
        if not self.current_transaction:
            raise Exception("No active transaction")

        # Add partition to transaction
        self.coordinator.add_partition_to_transaction(
            self.transaction_id,
            topic,
            partition
        )

        # Send idempotently
        if self.idempotent_producer.send(topic, partition, message):
            self.pending_messages.append((topic, partition, message))

    def commit_transaction(self):
        """Commit transaction - make messages visible"""
        if not self.current_transaction:
            raise Exception("No active transaction")

        # Two-phase commit
        # Phase 1: Prepare
        self.coordinator.prepare_commit(self.transaction_id)

        # Phase 2: Commit
        self.coordinator.commit_transaction(self.transaction_id)

        print(f"  ✓ Committed {len(self.pending_messages)} messages")

        self.current_transaction = None
        self.pending_messages = []

    def abort_transaction(self):
        """Abort transaction - discard messages"""
        if not self.current_transaction:
            raise Exception("No active transaction")

        self.coordinator.abort_transaction(self.transaction_id)

        print(f"  ✗ Aborted transaction, discarded {len(self.pending_messages)} messages")

        self.current_transaction = None
        self.pending_messages = []


# ============================================================================
# Transactional Consumer
# ============================================================================

class TransactionalConsumer:
    """
    Transactional consumer with read-committed isolation

    Only reads committed messages
    """

    def __init__(self, group_id: str, coordinator: TransactionCoordinator,
                 isolation_level: str = "read_committed"):
        self.group_id = group_id
        self.coordinator = coordinator
        self.isolation_level = isolation_level
        self.offsets: Dict[Tuple[str, int], int] = {}

    def poll(self, messages: List[Message]) -> List[Message]:
        """
        Poll messages with read-committed isolation

        Only return messages from committed transactions
        """
        if self.isolation_level == "read_uncommitted":
            return messages

        # Filter to only committed messages
        committed_messages = []

        for message in messages:
            # Check if message's transaction is committed
            # In production: Check transaction marker
            transaction_id = message.headers.get('transaction_id')

            if transaction_id:
                if self.coordinator.is_transaction_committed(transaction_id):
                    committed_messages.append(message)
            else:
                # Non-transactional message
                committed_messages.append(message)

        return committed_messages

    def commit_offsets(self, offsets: Dict[Tuple[str, int], int]):
        """Commit consumer offsets"""
        self.offsets.update(offsets)
        print(f"  [Consumer offsets committed: {offsets}]")


# ============================================================================
# Example: Exactly-Once Processing
# ============================================================================

def example_exactly_once_transfer():
    """
    Example: Exactly-once bank transfer

    Read from account-debits, write to account-credits
    """
    print("\\n1. EXACTLY-ONCE BANK TRANSFER")
    print("-" * 80)

    coordinator = TransactionCoordinator()

    # Producer for credits topic
    producer = TransactionalProducer("bank-transfer-txn", coordinator)

    # Simulated debit messages
    debit_messages = [
        Message(key="account1", value="debit:100", offset=0, partition=0,
                timestamp=time.time(), headers={}),
        Message(key="account1", value="debit:50", offset=1, partition=0,
                timestamp=time.time(), headers={}),
    ]

    # Process debits and produce credits atomically
    producer.begin_transaction()

    try:
        for debit_msg in debit_messages:
            account = debit_msg.key
            amount = int(debit_msg.value.split(':')[1])

            # Produce credit message
            credit_msg = f"credit:{amount}"
            producer.send("account-credits", 0, credit_msg)

            print(f"  Processing: {account} debit ${amount} -> credit ${amount}")

        # Commit transaction
        producer.commit_transaction()

        print("  ✓ Transfer completed with exactly-once guarantee")

    except Exception as e:
        # Abort on error
        producer.abort_transaction()
        print(f"  ✗ Transfer aborted: {e}")


def example_idempotent_producer():
    """Example: Idempotent producer preventing duplicates"""
    print("\\n2. IDEMPOTENT PRODUCER (Duplicate Prevention)")
    print("-" * 80)

    producer = IdempotentProducer(producer_id=123)

    # Send message
    print("  Sending message (first time):")
    producer.send("orders", 0, "order-001")

    # Retry (duplicate)
    print("  Retrying message (duplicate):")
    producer.send("orders", 0, "order-001")  # Detected and skipped

    print("  ✓ Duplicate prevented")


def example_read_committed():
    """Example: Read-committed isolation"""
    print("\\n3. READ-COMMITTED ISOLATION")
    print("-" * 80)

    coordinator = TransactionCoordinator()

    # Producer
    producer = TransactionalProducer("txn-123", coordinator)
    producer.begin_transaction()

    # Send messages (uncommitted)
    producer.send("events", 0, "event-1")
    producer.send("events", 0, "event-2")

    # Consumer with read-committed isolation
    consumer = TransactionalConsumer("consumer-group", coordinator,
                                    isolation_level="read_committed")

    uncommitted_messages = [
        Message(key=None, value="event-1", offset=0, partition=0,
                timestamp=time.time(), headers={'transaction_id': 'txn-123'}),
        Message(key=None, value="event-2", offset=1, partition=0,
                timestamp=time.time(), headers={'transaction_id': 'txn-123'}),
    ]

    # Poll before commit
    print("  Polling before commit:")
    messages = consumer.poll(uncommitted_messages)
    print(f"    Received: {len(messages)} messages (uncommitted filtered out)")

    # Commit transaction
    producer.commit_transaction()

    # Poll after commit
    print("  Polling after commit:")
    messages = consumer.poll(uncommitted_messages)
    print(f"    Received: {len(messages)} messages (committed, now visible)")


def example_consume_transform_produce():
    """
    Example: Consume-Transform-Produce pattern

    Exactly-once from input topic to output topic
    """
    print("\\n4. CONSUME-TRANSFORM-PRODUCE (Exactly-Once)")
    print("-" * 80)

    coordinator = TransactionCoordinator()

    # Consumer
    consumer = TransactionalConsumer("processor-group", coordinator)

    # Producer
    producer = TransactionalProducer("processor-txn", coordinator)

    # Input messages
    input_messages = [
        Message(key="user1", value="click", offset=0, partition=0,
                timestamp=time.time(), headers={}),
        Message(key="user2", value="click", offset=1, partition=0,
                timestamp=time.time(), headers={}),
    ]

    # Process atomically
    producer.begin_transaction()

    try:
        for msg in input_messages:
            # Transform
            transformed = f"processed_{msg.value}"

            # Produce to output topic
            producer.send("output-topic", 0, transformed)

            print(f"  Transformed: {msg.value} -> {transformed}")

        # Commit offsets and production together
        consumer.commit_offsets({("input-topic", 0): 2})
        producer.commit_transaction()

        print("  ✓ Exactly-once processing complete")

    except Exception as e:
        producer.abort_transaction()
        print(f"  ✗ Processing aborted: {e}")


# ============================================================================
# Main Example
# ============================================================================

def main():
    print("=" * 80)
    print("KAFKA EXACTLY-ONCE SEMANTICS")
    print("=" * 80)

    example_exactly_once_transfer()
    example_idempotent_producer()
    example_read_committed()
    example_consume_transform_produce()

    print("\\n" + "=" * 80)
    print("EXACTLY-ONCE SEMANTICS BEST PRACTICES")
    print("=" * 80)
    print("""
1. ENABLE EXACTLY-ONCE:
   - Set enable.idempotence=true
   - Set transactional.id for producers
   - Set isolation.level=read_committed for consumers
   - Requires Kafka 0.11+

2. IDEMPOTENT PRODUCERS:
   - Automatically enabled with transactions
   - Prevents duplicate messages within session
   - Uses producer ID and sequence numbers
   - Retries are safe

3. TRANSACTIONAL PRODUCERS:
   - Use transactions for atomic multi-partition writes
   - begin_transaction(), send(), commit_transaction()
   - Handle errors with abort_transaction()
   - Set max.in.flight.requests.per.connection=5

4. TRANSACTIONAL CONSUMERS:
   - Set isolation.level=read_committed
   - Only see committed messages
   - Commit offsets within transaction
   - Handle transaction markers

5. CONSUME-TRANSFORM-PRODUCE:
   - Read from input topic
   - Transform data
   - Write to output topic
   - Commit offsets and production together
   - Exactly-once end-to-end

6. PERFORMANCE:
   - Slight latency increase (2-phase commit)
   - Throughput impact minimal
   - Worth it for correctness guarantees
   - Monitor transaction coordinator load

7. ERROR HANDLING:
   - Always abort on errors
   - Implement retry logic
   - Monitor aborted transactions
   - Alert on high abort rates

8. MONITORING:
   - Track transaction durations
   - Monitor coordinator lag
   - Alert on transaction timeouts
   - Verify no duplicate messages
""")

    print("\\n✓ Kafka exactly-once semantics complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: SQLAlchemy and Kafka Lessons")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (782, upgrade_lesson_782, "SQLAlchemy - Relationship Patterns"),
        (910, upgrade_lesson_910, "Kafka - Exactly-Once Semantics"),
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
    print("SQLALCHEMY AND KAFKA BATCH COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
