import json

# Kafka simulation templates based on lesson 907 pattern

def generate_kafka_simulation_python(lesson_id, title):
    """Generate realistic Kafka simulation for Python based on lesson topic"""

    title_lower = title.lower()

    # Base template - producer/consumer classes
    base = '''# Simulated Apache Kafka implementation
import time
from collections import defaultdict, deque

'''

    if 'topic' in title_lower and 'partition' in title_lower:
        # Lesson 908: Topics and Partitions
        return base + '''class KafkaTopic:
    """Simulated Kafka topic with partitions"""
    def __init__(self, name, num_partitions=3):
        self.name = name
        self.partitions = [deque() for _ in range(num_partitions)]
        self.num_partitions = num_partitions

    def get_partition(self, key=None):
        """Determine partition for a message"""
        if key is None:
            # Round-robin if no key
            return hash(time.time()) % self.num_partitions
        else:
            # Hash-based partitioning
            return hash(key) % self.num_partitions

    def send_to_partition(self, partition_id, message):
        """Send message to specific partition"""
        if 0 <= partition_id < self.num_partitions:
            self.partitions[partition_id].append(message)
            return True
        return False

    def read_from_partition(self, partition_id, offset=0):
        """Read messages from partition"""
        if 0 <= partition_id < self.num_partitions:
            partition_data = list(self.partitions[partition_id])
            return partition_data[offset:] if offset < len(partition_data) else []
        return []

# Demo
topic = KafkaTopic("user-events", num_partitions=3)

# Send messages with keys
messages = [
    ("user-1", "login"),
    ("user-2", "logout"),
    ("user-1", "purchase"),
    ("user-3", "view"),
    ("user-1", "logout")
]

print("Kafka Topics and Partitions Demo")
print("=" * 50)

for key, event in messages:
    partition = topic.get_partition(key)
    topic.send_to_partition(partition, f"{key}:{event}")
    print(f"Sent '{event}' from {key} to partition {partition}")

print()
print("Partition contents:")
for i in range(topic.num_partitions):
    messages_in_partition = topic.read_from_partition(i)
    print(f"Partition {i}: {messages_in_partition}")

print()
print("Key insight: Same key always goes to same partition!")
print("user-1 messages are all in the same partition")
'''

    elif 'consumer group' in title_lower:
        # Lesson 909: Consumer Groups
        return base + '''class KafkaConsumerGroup:
    """Simulated Kafka consumer group with partition assignment"""
    def __init__(self, group_id, topic_partitions):
        self.group_id = group_id
        self.consumers = []
        self.topic_partitions = topic_partitions
        self.assignments = {}  # consumer_id -> [partition_ids]

    def add_consumer(self, consumer_id):
        """Add consumer and rebalance partitions"""
        self.consumers.append(consumer_id)
        self._rebalance()

    def remove_consumer(self, consumer_id):
        """Remove consumer and rebalance partitions"""
        if consumer_id in self.consumers:
            self.consumers.remove(consumer_id)
            self._rebalance()

    def _rebalance(self):
        """Redistribute partitions among consumers"""
        self.assignments = {}
        if not self.consumers:
            return

        partitions_per_consumer = self.topic_partitions // len(self.consumers)
        remainder = self.topic_partitions % len(self.consumers)

        partition_id = 0
        for i, consumer in enumerate(self.consumers):
            # Assign base partitions
            count = partitions_per_consumer + (1 if i < remainder else 0)
            self.assignments[consumer] = list(range(partition_id, partition_id + count))
            partition_id += count

    def get_assignment(self, consumer_id):
        """Get partitions assigned to a consumer"""
        return self.assignments.get(consumer_id, [])

# Demo
print("Kafka Consumer Groups Demo")
print("=" * 50)

group = KafkaConsumerGroup("my-group", topic_partitions=6)

# Add consumers and see rebalancing
print("Adding consumer-1:")
group.add_consumer("consumer-1")
print(f"  Partitions: {group.get_assignment('consumer-1')}")

print("\\nAdding consumer-2:")
group.add_consumer("consumer-2")
for consumer in group.consumers:
    print(f"  {consumer}: {group.get_assignment(consumer)}")

print("\\nAdding consumer-3:")
group.add_consumer("consumer-3")
for consumer in group.consumers:
    print(f"  {consumer}: {group.get_assignment(consumer)}")

print("\\nRemoving consumer-2 (rebalance):")
group.remove_consumer("consumer-2")
for consumer in group.consumers:
    print(f"  {consumer}: {group.get_assignment(consumer)}")

print("\\nKey insight: Partitions automatically redistribute")
print("when consumers join or leave the group!")
'''

    elif 'exactly-once' in title_lower or 'semantic' in title_lower:
        # Lesson 910: Exactly-Once Semantics
        return base + '''class KafkaExactlyOnceProducer:
    """Simulated Kafka producer with exactly-once semantics"""
    def __init__(self):
        self.messages = []
        self.transaction_messages = []
        self.in_transaction = False
        self.committed_transactions = set()
        self.transaction_id = 0

    def begin_transaction(self):
        """Start a transaction"""
        self.in_transaction = True
        self.transaction_id += 1
        self.transaction_messages = []
        print(f"Transaction {self.transaction_id} started")

    def send(self, message):
        """Send message (buffered if in transaction)"""
        if self.in_transaction:
            self.transaction_messages.append(message)
            print(f"  Buffered: {message}")
        else:
            self.messages.append(message)
            print(f"  Sent: {message}")

    def commit_transaction(self):
        """Commit transaction - all messages atomic"""
        if not self.in_transaction:
            print("No active transaction")
            return False

        # Atomic commit - all or nothing
        self.messages.extend(self.transaction_messages)
        self.committed_transactions.add(self.transaction_id)
        print(f"Transaction {self.transaction_id} committed")
        print(f"  {len(self.transaction_messages)} messages written")

        self.transaction_messages = []
        self.in_transaction = False
        return True

    def abort_transaction(self):
        """Abort transaction - discard buffered messages"""
        if not self.in_transaction:
            print("No active transaction")
            return False

        print(f"Transaction {self.transaction_id} aborted")
        print(f"  {len(self.transaction_messages)} messages discarded")

        self.transaction_messages = []
        self.in_transaction = False
        return True

# Demo
print("Kafka Exactly-Once Semantics Demo")
print("=" * 50)

producer = KafkaExactlyOnceProducer()

# Transaction 1: Success
producer.begin_transaction()
producer.send("user-1: login")
producer.send("user-1: purchase")
producer.commit_transaction()

print()
print(f"Messages in Kafka: {producer.messages}")

# Transaction 2: Failure (aborted)
print("\\n" + "=" * 50)
producer.begin_transaction()
producer.send("user-2: login")
producer.send("user-2: INVALID_ACTION")
print("  Error detected! Aborting...")
producer.abort_transaction()

print()
print(f"Messages in Kafka: {producer.messages}")
print()
print("Key insight: Transaction 2 messages never appeared!")
print("Exactly-once semantics ensures all-or-nothing delivery")
'''

    else:
        # Generic Kafka simulation
        return base + '''class SimpleKafkaProducer:
    """Simulated Kafka producer"""
    def __init__(self, topic):
        self.topic = topic
        self.messages = []

    def send(self, key, value):
        """Send message to topic"""
        message = {"key": key, "value": value, "timestamp": time.time()}
        self.messages.append(message)
        return message

class SimpleKafkaConsumer:
    """Simulated Kafka consumer"""
    def __init__(self, topic, group_id):
        self.topic = topic
        self.group_id = group_id
        self.offset = 0

    def poll(self, producer_messages, max_messages=10):
        """Poll for new messages"""
        available = producer_messages[self.offset:self.offset + max_messages]
        self.offset += len(available)
        return available

# Demo
print(f"{title}")
print("=" * 50)

producer = SimpleKafkaProducer("events")
consumer = SimpleKafkaConsumer("events", "group-1")

# Producer sends messages
for i in range(5):
    msg = producer.send(f"key-{i}", f"event-{i}")
    print(f"Produced: {msg['key']} -> {msg['value']}")

print()

# Consumer polls messages
messages = consumer.poll(producer.messages)
print(f"Consumed {len(messages)} messages:")
for msg in messages:
    print(f"  {msg['key']}: {msg['value']}")
'''


def main():
    """Generate simulations for all Kafka stubs"""
    # Load current lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Load stub list
    with open('framework_stubs_to_upgrade.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    kafka_stubs = [s for s in data['stubs'] if s['framework'] == 'Kafka' and s['language'] == 'python']

    print(f"Generating simulations for {len(kafka_stubs)} Kafka Python lessons...")

    for stub in kafka_stubs:
        lesson_id = stub['id']
        title = stub['title']

        # Find lesson in array
        for i, lesson in enumerate(lessons):
            if lesson['id'] == lesson_id:
                # Generate simulation
                new_solution = generate_kafka_simulation_python(lesson_id, title)

                # Update lesson
                lessons[i]['fullSolution'] = new_solution

                print(f"  Updated lesson {lesson_id}: {title}")
                break

    # Save updated lessons
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"\nUpgraded {len(kafka_stubs)} Kafka Python lessons to realistic simulations")

if __name__ == '__main__':
    main()
