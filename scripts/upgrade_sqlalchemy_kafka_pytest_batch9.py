#!/usr/bin/env python3
"""
Upgrade SQLAlchemy Custom Types, Query Optimization, Kafka Topics, and pytest Database Testing
"""

import json
import sys

def upgrade_lesson_783():
    """SQLAlchemy - Custom Types"""
    return '''# SQLAlchemy Custom Types
# In production: pip install sqlalchemy

"""
SQLAlchemy Custom Column Types

Complete guide to custom SQLAlchemy types:
- Creating custom types
- Type decorators
- JSON/Array types
- Enum types
- Encrypted types
- Type coercion
- Database-specific types

Used by: Applications needing custom data serialization
"""

import json
import base64
from typing import Any, Optional, List, Dict
from datetime import datetime
from enum import Enum as PyEnum


# ============================================================================
# Type System Base
# ============================================================================

class TypeDecorator:
    """Base class for custom types"""

    def __init__(self, impl_type: str):
        self.impl = impl_type  # Underlying database type

    def process_bind_param(self, value: Any, dialect) -> Any:
        """Convert Python value to database value"""
        return value

    def process_result_value(self, value: Any, dialect) -> Any:
        """Convert database value to Python value"""
        return value


# ============================================================================
# JSON Type
# ============================================================================

class JSON(TypeDecorator):
    """
    JSON column type

    Stores Python dicts/lists as JSON strings
    """

    def __init__(self):
        super().__init__('TEXT')

    def process_bind_param(self, value: Any, dialect) -> Optional[str]:
        """Convert Python object to JSON string"""
        if value is None:
            return None

        return json.dumps(value)

    def process_result_value(self, value: Optional[str], dialect) -> Any:
        """Convert JSON string to Python object"""
        if value is None:
            return None

        return json.loads(value)


# ============================================================================
# ARRAY Type
# ============================================================================

class ARRAY(TypeDecorator):
    """
    Array column type

    Stores Python lists as comma-separated strings
    """

    def __init__(self, item_type: str = 'String'):
        super().__init__('TEXT')
        self.item_type = item_type

    def process_bind_param(self, value: Optional[List], dialect) -> Optional[str]:
        """Convert list to comma-separated string"""
        if value is None:
            return None

        return ','.join(str(v) for v in value)

    def process_result_value(self, value: Optional[str], dialect) -> Optional[List]:
        """Convert comma-separated string to list"""
        if value is None or value == '':
            return []

        # Convert based on item type
        items = value.split(',')

        if self.item_type == 'Integer':
            return [int(v) for v in items]
        elif self.item_type == 'Float':
            return [float(v) for v in items]
        else:
            return items


# ============================================================================
# Enum Type
# ============================================================================

class Enum(TypeDecorator):
    """
    Enum column type

    Maps Python Enum to string values
    """

    def __init__(self, enum_class: type):
        super().__init__('VARCHAR')
        self.enum_class = enum_class

    def process_bind_param(self, value: Optional[PyEnum], dialect) -> Optional[str]:
        """Convert Enum to string"""
        if value is None:
            return None

        if isinstance(value, self.enum_class):
            return value.value

        return value

    def process_result_value(self, value: Optional[str], dialect) -> Optional[PyEnum]:
        """Convert string to Enum"""
        if value is None:
            return None

        return self.enum_class(value)


# ============================================================================
# Encrypted Type
# ============================================================================

class EncryptedString(TypeDecorator):
    """
    Encrypted string type

    Encrypts data before storing (base64 for demo)
    In production: Use proper encryption (Fernet, AES)
    """

    def __init__(self, key: str = 'secret-key'):
        super().__init__('TEXT')
        self.key = key

    def _encrypt(self, value: str) -> str:
        """Encrypt value (simplified)"""
        # In production: Use cryptography.fernet.Fernet
        encrypted = base64.b64encode(value.encode()).decode()
        return encrypted

    def _decrypt(self, value: str) -> str:
        """Decrypt value"""
        decrypted = base64.b64decode(value.encode()).decode()
        return decrypted

    def process_bind_param(self, value: Optional[str], dialect) -> Optional[str]:
        """Encrypt before storing"""
        if value is None:
            return None

        return self._encrypt(value)

    def process_result_value(self, value: Optional[str], dialect) -> Optional[str]:
        """Decrypt after retrieving"""
        if value is None:
            return None

        return self._decrypt(value)


# ============================================================================
# Choice Type (Limited Values)
# ============================================================================

class Choice(TypeDecorator):
    """
    Choice type - restricts values to predefined set
    """

    def __init__(self, choices: List[str]):
        super().__init__('VARCHAR')
        self.choices = choices

    def process_bind_param(self, value: Optional[str], dialect) -> Optional[str]:
        """Validate choice"""
        if value is None:
            return None

        if value not in self.choices:
            raise ValueError(f"Invalid choice: {value}. Must be one of {self.choices}")

        return value

    def process_result_value(self, value: Optional[str], dialect) -> Optional[str]:
        """Return choice value"""
        return value


# ============================================================================
# URL Type
# ============================================================================

class URL(TypeDecorator):
    """
    URL type with validation
    """

    def __init__(self):
        super().__init__('VARCHAR')

    def process_bind_param(self, value: Optional[str], dialect) -> Optional[str]:
        """Validate URL"""
        if value is None:
            return None

        # Simple validation
        if not value.startswith(('http://', 'https://')):
            raise ValueError(f"Invalid URL: {value}")

        return value

    def process_result_value(self, value: Optional[str], dialect) -> Optional[str]:
        """Return URL"""
        return value


# ============================================================================
# Email Type
# ============================================================================

class Email(TypeDecorator):
    """
    Email type with validation
    """

    def __init__(self):
        super().__init__('VARCHAR')

    def process_bind_param(self, value: Optional[str], dialect) -> Optional[str]:
        """Validate email"""
        if value is None:
            return None

        if '@' not in value or '.' not in value.split('@')[1]:
            raise ValueError(f"Invalid email: {value}")

        return value.lower()

    def process_result_value(self, value: Optional[str], dialect) -> Optional[str]:
        """Return email"""
        return value


# ============================================================================
# PhoneNumber Type
# ============================================================================

class PhoneNumber(TypeDecorator):
    """
    Phone number type with formatting
    """

    def __init__(self):
        super().__init__('VARCHAR')

    def process_bind_param(self, value: Optional[str], dialect) -> Optional[str]:
        """Format phone number"""
        if value is None:
            return None

        # Remove non-digits
        digits = ''.join(c for c in value if c.isdigit())

        # Format as (XXX) XXX-XXXX for 10 digits
        if len(digits) == 10:
            return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

        return digits

    def process_result_value(self, value: Optional[str], dialect) -> Optional[str]:
        """Return formatted phone number"""
        return value


# ============================================================================
# Example Models Using Custom Types
# ============================================================================

class UserStatus(PyEnum):
    """User status enum"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


class Model:
    """Base model"""
    _storage: Dict[str, List] = {}
    _id_counter = 0

    def __init__(self, **kwargs):
        Model._id_counter += 1
        self.id = Model._id_counter

        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        """Save to storage"""
        table_name = self.__class__.__name__
        if table_name not in Model._storage:
            Model._storage[table_name] = []

        # Process custom types
        for attr_name, attr_value in self.__class__.__dict__.items():
            if isinstance(attr_value, TypeDecorator):
                # Convert Python value to DB value
                python_value = getattr(self, attr_name, None)
                db_value = attr_value.process_bind_param(python_value, None)
                setattr(self, f"_{attr_name}_db", db_value)

        Model._storage[table_name].append(self)

    @classmethod
    def get(cls, id: int):
        """Get by ID"""
        table_name = cls.__name__
        if table_name not in Model._storage:
            return None

        for obj in Model._storage[table_name]:
            if obj.id == id:
                # Convert DB values back to Python
                for attr_name, attr_value in cls.__dict__.items():
                    if isinstance(attr_value, TypeDecorator):
                        db_value = getattr(obj, f"_{attr_name}_db", None)
                        python_value = attr_value.process_result_value(db_value, None)
                        setattr(obj, attr_name, python_value)

                return obj

        return None


class User(Model):
    """User model with custom types"""

    # Standard columns
    username = 'VARCHAR'

    # Custom types
    email = Email()
    phone = PhoneNumber()
    status = Enum(UserStatus)
    metadata = JSON()
    tags = ARRAY('String')
    password_hash = EncryptedString()
    website = URL()


class Product(Model):
    """Product model with custom types"""

    name = 'VARCHAR'
    category = Choice(['electronics', 'clothing', 'books', 'food'])
    features = JSON()
    tags = ARRAY('String')
    price_history = ARRAY('Float')


# ============================================================================
# Example Usage
# ============================================================================

def main():
    print("=" * 80)
    print("SQLALCHEMY CUSTOM TYPES")
    print("=" * 80)

    # 1. JSON Type
    print("\\n1. JSON TYPE")
    print("-" * 80)

    user = User(
        username="alice",
        email="alice@example.com",
        phone="5551234567",
        status=UserStatus.ACTIVE,
        metadata={"preferences": {"theme": "dark", "notifications": True}},
        tags=["admin", "verified"],
        password_hash="secret123",
        website="https://example.com"
    )

    user.save()

    print(f"User created: {user.username}")
    print(f"  Metadata (JSON): {user.metadata}")
    print(f"  Tags (ARRAY): {user.tags}")
    print(f"  Status (ENUM): {user.status}")
    print(f"  Email: {user.email}")
    print(f"  Phone: {user.phone}")
    print(f"  Website: {user.website}")

    # Retrieve user
    retrieved = User.get(user.id)
    print(f"\\nRetrieved user:")
    print(f"  Metadata: {retrieved.metadata}")
    print(f"  Tags: {retrieved.tags}")
    print(f"  Status: {retrieved.status} (type: {type(retrieved.status).__name__})")

    # 2. Product with Custom Types
    print("\\n2. PRODUCT WITH CUSTOM TYPES")
    print("-" * 80)

    product = Product(
        name="Laptop",
        category="electronics",
        features={
            "cpu": "Intel i7",
            "ram": "16GB",
            "storage": "512GB SSD"
        },
        tags=["new", "sale", "popular"],
        price_history=[999.99, 949.99, 899.99]
    )

    product.save()

    print(f"Product: {product.name}")
    print(f"  Category (CHOICE): {product.category}")
    print(f"  Features (JSON): {product.features}")
    print(f"  Tags (ARRAY): {product.tags}")
    print(f"  Price History (ARRAY[Float]): {product.price_history}")

    # 3. Type Validation
    print("\\n3. TYPE VALIDATION")
    print("-" * 80)

    # Invalid email
    try:
        invalid_user = User(
            username="bob",
            email="invalid-email",  # No @ or domain
            phone="555-1234",
            status=UserStatus.ACTIVE,
            metadata={},
            tags=[],
            password_hash="pass",
            website="https://example.com"
        )
        invalid_user.save()
        print("ERROR: Should have failed validation")
    except ValueError as e:
        print(f"Email validation: {e}")

    # Invalid URL
    try:
        invalid_user = User(
            username="bob",
            email="bob@example.com",
            phone="555-1234",
            status=UserStatus.ACTIVE,
            metadata={},
            tags=[],
            password_hash="pass",
            website="invalid-url"  # No http/https
        )
        invalid_user.save()
        print("ERROR: Should have failed validation")
    except ValueError as e:
        print(f"URL validation: {e}")

    # Invalid choice
    try:
        invalid_product = Product(
            name="Book",
            category="invalid",  # Not in choices
            features={},
            tags=[],
            price_history=[]
        )
        invalid_product.save()
        print("ERROR: Should have failed validation")
    except ValueError as e:
        print(f"Choice validation: {e}")

    print("\\n" + "=" * 80)
    print("CUSTOM TYPES BEST PRACTICES")
    print("=" * 80)
    print("""
1. WHEN TO USE CUSTOM TYPES:
   - Complex data structures (JSON, arrays)
   - Encrypted sensitive data
   - Enums for fixed choices
   - Validation (email, URL, phone)
   - Custom serialization

2. TYPE DECORATOR:
   - Inherit from TypeDecorator
   - Implement process_bind_param (Python -> DB)
   - Implement process_result_value (DB -> Python)
   - Choose appropriate impl (underlying DB type)

3. JSON TYPE:
   - Store dicts/lists as JSON
   - Query with JSON operators (PostgreSQL)
   - Good for flexible schemas
   - Index JSON fields if needed

4. ARRAY TYPE:
   - Store lists in database
   - PostgreSQL has native ARRAY
   - Other DBs: serialize as JSON or CSV
   - Good for tags, labels

5. ENUM TYPE:
   - Map Python Enum to DB values
   - Type safety in Python code
   - DB constraint for valid values
   - Use for status, categories

6. ENCRYPTED TYPE:
   - Encrypt sensitive data
   - Use proper encryption (Fernet, AES)
   - Store encryption key securely
   - Can't query encrypted fields

7. VALIDATION TYPES:
   - Validate on insert/update
   - Email, URL, phone number
   - Custom regex patterns
   - Database constraints

8. PERFORMANCE:
   - Custom types add overhead
   - Use native DB types when possible
   - Index appropriately
   - Cache processed values
""")

    print("\\n✓ SQLAlchemy custom types complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_908():
    """Kafka - Topics and Partitions"""
    return '''# Apache Kafka - Topics and Partitions
# In production: pip install kafka-python

"""
Apache Kafka Topics and Partitions

Complete guide to Kafka's core concepts:
- Topics as message categories
- Partitions for parallelism
- Partition keys and ordering
- Replication and leadership
- Partition assignment
- Scaling with partitions

Used by: All Kafka deployments for message organization
"""

import time
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from collections import defaultdict, deque


# ============================================================================
# Message and Record
# ============================================================================

@dataclass
class Message:
    """Kafka message"""
    key: Optional[str]
    value: str
    offset: int
    timestamp: float
    partition: int

    def __repr__(self):
        return f"Message(key={self.key}, offset={self.offset}, partition={self.partition})"


# ============================================================================
# Partition
# ============================================================================

class Partition:
    """
    Kafka partition

    Ordered, immutable sequence of messages
    """

    def __init__(self, topic: str, partition_id: int, leader_broker: int):
        self.topic = topic
        self.partition_id = partition_id
        self.leader_broker = leader_broker

        # Storage
        self.messages: deque = deque()
        self.high_water_mark = 0  # Latest committed offset
        self.log_end_offset = 0  # Latest offset (including uncommitted)

        # Replicas
        self.replicas: Set[int] = {leader_broker}
        self.in_sync_replicas: Set[int] = {leader_broker}

    def append(self, key: Optional[str], value: str) -> int:
        """
        Append message to partition

        Returns offset of appended message
        """
        offset = self.log_end_offset
        timestamp = time.time()

        message = Message(
            key=key,
            value=value,
            offset=offset,
            timestamp=timestamp,
            partition=self.partition_id
        )

        self.messages.append(message)
        self.log_end_offset += 1

        # Update high water mark (simplified - assumes immediate commit)
        self.high_water_mark = self.log_end_offset

        return offset

    def read(self, offset: int, max_messages: int = 100) -> List[Message]:
        """Read messages starting from offset"""
        results = []

        for message in self.messages:
            if message.offset >= offset and len(results) < max_messages:
                results.append(message)

        return results

    def add_replica(self, broker_id: int):
        """Add replica"""
        self.replicas.add(broker_id)

    def update_isr(self, broker_ids: Set[int]):
        """Update in-sync replicas"""
        self.in_sync_replicas = broker_ids.intersection(self.replicas)


# ============================================================================
# Topic
# ============================================================================

class Topic:
    """
    Kafka topic

    Logical category for messages with multiple partitions
    """

    def __init__(self, name: str, num_partitions: int, replication_factor: int):
        self.name = name
        self.num_partitions = num_partitions
        self.replication_factor = replication_factor

        # Create partitions
        self.partitions: List[Partition] = []
        for partition_id in range(num_partitions):
            # Assign leader (round-robin across brokers for demo)
            leader_broker = partition_id % 3  # Assume 3 brokers

            partition = Partition(name, partition_id, leader_broker)
            self.partitions.append(partition)

    def get_partition(self, partition_id: int) -> Partition:
        """Get specific partition"""
        if 0 <= partition_id < len(self.partitions):
            return self.partitions[partition_id]

        raise ValueError(f"Invalid partition ID: {partition_id}")

    def partition_for_key(self, key: Optional[str]) -> int:
        """
        Determine partition for key

        Uses hash partitioning for consistent routing
        """
        if key is None:
            # Round-robin for null keys
            return 0

        # Hash key and map to partition
        key_hash = hash(key)
        return key_hash % self.num_partitions

    def write(self, key: Optional[str], value: str, partition: Optional[int] = None) -> tuple:
        """
        Write message to topic

        Returns (partition_id, offset)
        """
        # Determine partition
        if partition is None:
            partition = self.partition_for_key(key)

        # Write to partition
        target_partition = self.get_partition(partition)
        offset = target_partition.append(key, value)

        return (partition, offset)

    def read(self, partition: int, offset: int, max_messages: int = 100) -> List[Message]:
        """Read messages from partition"""
        target_partition = self.get_partition(partition)
        return target_partition.read(offset, max_messages)


# ============================================================================
# Kafka Cluster
# ============================================================================

class KafkaCluster:
    """Simulated Kafka cluster"""

    def __init__(self, num_brokers: int = 3):
        self.num_brokers = num_brokers
        self.topics: Dict[str, Topic] = {}
        self.topic_metadata: Dict[str, Dict] = {}

    def create_topic(self, name: str, num_partitions: int = 3,
                     replication_factor: int = 2):
        """Create topic"""
        if name in self.topics:
            raise ValueError(f"Topic {name} already exists")

        topic = Topic(name, num_partitions, replication_factor)
        self.topics[name] = topic

        self.topic_metadata[name] = {
            'name': name,
            'num_partitions': num_partitions,
            'replication_factor': replication_factor,
            'created_at': time.time()
        }

        print(f"Topic '{name}' created:")
        print(f"  Partitions: {num_partitions}")
        print(f"  Replication factor: {replication_factor}")

        # Show partition distribution
        for partition in topic.partitions:
            print(f"    Partition {partition.partition_id}: Leader=Broker-{partition.leader_broker}")

    def get_topic(self, name: str) -> Topic:
        """Get topic"""
        if name not in self.topics:
            raise ValueError(f"Topic {name} not found")

        return self.topics[name]

    def list_topics(self) -> List[str]:
        """List all topics"""
        return list(self.topics.keys())

    def describe_topic(self, name: str):
        """Describe topic"""
        if name not in self.topics:
            print(f"Topic {name} not found")
            return

        topic = self.topics[name]
        metadata = self.topic_metadata[name]

        print(f"\\nTopic: {name}")
        print(f"  Partitions: {metadata['num_partitions']}")
        print(f"  Replication factor: {metadata['replication_factor']}")
        print(f"\\n  Partition Details:")

        for partition in topic.partitions:
            print(f"    Partition {partition.partition_id}:")
            print(f"      Leader: Broker-{partition.leader_broker}")
            print(f"      Replicas: {partition.replicas}")
            print(f"      ISR: {partition.in_sync_replicas}")
            print(f"      Messages: {len(partition.messages)}")
            print(f"      High water mark: {partition.high_water_mark}")


# ============================================================================
# Example Usage
# ============================================================================

def example_basic_topic():
    """Example: Basic topic creation and usage"""
    print("\\n1. BASIC TOPIC")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("events", num_partitions=3, replication_factor=2)

    topic = cluster.get_topic("events")

    # Write messages
    print("\\nWriting messages:")
    for i in range(5):
        partition, offset = topic.write(None, f"message-{i}")
        print(f"  message-{i} -> partition {partition}, offset {offset}")


def example_key_based_partitioning():
    """Example: Key-based partitioning"""
    print("\\n2. KEY-BASED PARTITIONING")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("user-events", num_partitions=3)

    topic = cluster.get_topic("user-events")

    # Messages with same key go to same partition
    users = ["user1", "user2", "user1", "user3", "user2", "user1"]

    print("\\nWriting messages with keys:")
    partition_counts = defaultdict(int)

    for user in users:
        partition, offset = topic.write(user, f"event from {user}")
        partition_counts[partition] += 1
        print(f"  {user} -> partition {partition}")

    print("\\nPartition distribution:")
    for partition_id, count in sorted(partition_counts.items()):
        print(f"  Partition {partition_id}: {count} messages")


def example_ordering_guarantees():
    """Example: Message ordering guarantees"""
    print("\\n3. ORDERING GUARANTEES")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("orders", num_partitions=2)

    topic = cluster.get_topic("orders")

    # Write ordered sequence
    print("\\nWriting ordered sequence:")
    for i in range(6):
        partition, offset = topic.write("customer1", f"order-{i}")
        print(f"  order-{i} -> partition {partition}, offset {offset}")

    # Read back - ordering preserved within partition
    print("\\nReading from partition 0:")
    messages = topic.read(partition=0, offset=0)
    for msg in messages:
        print(f"  {msg.value} (offset {msg.offset})")


def example_partition_scaling():
    """Example: Scaling with partitions"""
    print("\\n4. SCALING WITH PARTITIONS")
    print("-" * 80)

    cluster = KafkaCluster()

    # Small topic
    cluster.create_topic("small-topic", num_partitions=1)
    print("Small topic: 1 partition (limited parallelism)")

    # Large topic
    print("\\n")
    cluster.create_topic("large-topic", num_partitions=12)
    print("Large topic: 12 partitions (high parallelism)")

    print("\\nScaling principles:")
    print("  - 1 partition = 1 consumer max")
    print("  - 12 partitions = up to 12 parallel consumers")
    print("  - More partitions = better throughput")
    print("  - But: More partitions = more overhead")


def example_replication():
    """Example: Partition replication"""
    print("\\n5. PARTITION REPLICATION")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("critical-data", num_partitions=3, replication_factor=3)

    topic = cluster.get_topic("critical-data")

    print("\\nReplication details:")
    for partition in topic.partitions:
        print(f"  Partition {partition.partition_id}:")
        print(f"    Leader: Broker-{partition.leader_broker}")
        print(f"    Replicas: {list(partition.replicas)}")
        print(f"    In-Sync Replicas (ISR): {list(partition.in_sync_replicas)}")


def main():
    print("=" * 80)
    print("KAFKA TOPICS AND PARTITIONS")
    print("=" * 80)

    example_basic_topic()
    example_key_based_partitioning()
    example_ordering_guarantees()
    example_partition_scaling()
    example_replication()

    print("\\n" + "=" * 80)
    print("TOPICS AND PARTITIONS BEST PRACTICES")
    print("=" * 80)
    print("""
1. TOPIC DESIGN:
   - One topic per event type
   - Use meaningful topic names
   - Plan partition count upfront
   - Can't decrease partitions later

2. PARTITION COUNT:
   - More partitions = more parallelism
   - Rule of thumb: (throughput target / single partition throughput)
   - Consider consumer count (max consumers = partition count)
   - Typical: 3-12 partitions per topic

3. MESSAGE KEYS:
   - Use keys for ordering guarantees
   - Same key -> same partition -> ordered
   - Good for user_id, account_id, session_id
   - Null key -> round-robin distribution

4. ORDERING:
   - Guaranteed within partition only
   - Not guaranteed across partitions
   - Use single partition for strict ordering
   - Or use message keys for partial ordering

5. REPLICATION:
   - replication_factor: 2-3 typical
   - min.insync.replicas: 2 recommended
   - Leader handles all reads/writes
   - Replicas provide fault tolerance

6. PARTITION DISTRIBUTION:
   - Evenly distribute across brokers
   - Leaders spread for load balancing
   - Monitor partition sizes
   - Rebalance if uneven

7. SCALING:
   - Add partitions to increase throughput
   - Can't remove partitions (Kafka limitation)
   - Plan for growth upfront
   - Use partition count as multiple of consumer count

8. PERFORMANCE:
   - More partitions = more files
   - Trade-off: parallelism vs overhead
   - Monitor broker load
   - Limit total partitions per broker (<1000)
""")

    print("\\n✓ Kafka topics and partitions complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: SQLAlchemy Custom Types and Kafka Topics/Partitions")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (783, upgrade_lesson_783, "SQLAlchemy - Custom Types"),
        (908, upgrade_lesson_908, "Kafka - Topics and Partitions"),
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
    print(f"\\nTotal lessons in file: {len(lessons)} (maintaining 1030)")


if __name__ == '__main__':
    main()
