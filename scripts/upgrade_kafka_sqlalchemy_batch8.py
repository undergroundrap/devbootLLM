#!/usr/bin/env python3
"""
Upgrade more Kafka and SQLAlchemy lessons
"""

import json
import sys

def upgrade_lesson_909():
    """Kafka - Consumer Groups"""
    return '''# Apache Kafka - Consumer Groups
# In production: pip install kafka-python

"""
Apache Kafka Consumer Groups

Complete guide to Kafka consumer groups:
- Consumer group coordination
- Partition assignment strategies
- Rebalancing protocols
- Offset management
- Consumer lag monitoring
- Scalability patterns

Used by: All Kafka consumers for distributed message processing
"""

import time
import uuid
from typing import Dict, List, Set, Optional
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict


# ============================================================================
# Partition Assignment Strategies
# ============================================================================

class AssignmentStrategy(Enum):
    """Partition assignment strategies"""
    RANGE = "range"
    ROUND_ROBIN = "roundrobin"
    STICKY = "sticky"
    COOPERATIVE_STICKY = "cooperative-sticky"


# ============================================================================
# Consumer Metadata
# ============================================================================

@dataclass
class ConsumerMetadata:
    """Consumer metadata"""
    consumer_id: str
    group_id: str
    client_id: str
    host: str
    subscribed_topics: List[str]
    assigned_partitions: Set[tuple]  # (topic, partition)
    last_heartbeat: float


@dataclass
class Partition:
    """Topic partition"""
    topic: str
    partition: int
    leader_broker: int

    def __hash__(self):
        return hash((self.topic, self.partition))

    def __eq__(self, other):
        return self.topic == other.topic and self.partition == other.partition


# ============================================================================
# Group Coordinator
# ============================================================================

class GroupCoordinator:
    """
    Manages consumer groups

    Coordinates partition assignment and rebalancing
    """

    def __init__(self):
        self.groups: Dict[str, Dict[str, ConsumerMetadata]] = defaultdict(dict)
        self.partition_ownership: Dict[tuple, str] = {}  # (topic, partition) -> consumer_id
        self.rebalance_listeners: List = []

    def join_group(self, group_id: str, consumer_id: str, client_id: str,
                   topics: List[str]) -> ConsumerMetadata:
        """Consumer joins group"""
        consumer = ConsumerMetadata(
            consumer_id=consumer_id,
            group_id=group_id,
            client_id=client_id,
            host="localhost",
            subscribed_topics=topics,
            assigned_partitions=set(),
            last_heartbeat=time.time()
        )

        self.groups[group_id][consumer_id] = consumer

        print(f"  [Consumer {consumer_id} joined group {group_id}]")

        # Trigger rebalance
        self.rebalance(group_id)

        return consumer

    def leave_group(self, group_id: str, consumer_id: str):
        """Consumer leaves group"""
        if group_id in self.groups and consumer_id in self.groups[group_id]:
            # Remove consumer
            consumer = self.groups[group_id][consumer_id]

            # Release partitions
            for partition in consumer.assigned_partitions:
                if partition in self.partition_ownership:
                    del self.partition_ownership[partition]

            del self.groups[group_id][consumer_id]

            print(f"  [Consumer {consumer_id} left group {group_id}]")

            # Trigger rebalance if group not empty
            if self.groups[group_id]:
                self.rebalance(group_id)

    def heartbeat(self, group_id: str, consumer_id: str):
        """Update consumer heartbeat"""
        if group_id in self.groups and consumer_id in self.groups[group_id]:
            self.groups[group_id][consumer_id].last_heartbeat = time.time()

    def rebalance(self, group_id: str, strategy: AssignmentStrategy = AssignmentStrategy.RANGE):
        """
        Rebalance partition assignment

        Redistributes partitions among consumers
        """
        if group_id not in self.groups or not self.groups[group_id]:
            return

        print(f"\\n  [REBALANCING group {group_id}...]")

        consumers = list(self.groups[group_id].values())

        # Get all topics subscribed by group
        all_topics = set()
        for consumer in consumers:
            all_topics.update(consumer.subscribed_topics)

        # Get all partitions for these topics
        # Simulated - in production, fetch from broker metadata
        all_partitions = []
        for topic in all_topics:
            # Assume 3 partitions per topic
            for partition_num in range(3):
                all_partitions.append(Partition(topic, partition_num, 0))

        # Clear existing assignments
        for consumer in consumers:
            consumer.assigned_partitions.clear()

        # Assign partitions based on strategy
        if strategy == AssignmentStrategy.RANGE:
            self._assign_range(consumers, all_partitions)
        elif strategy == AssignmentStrategy.ROUND_ROBIN:
            self._assign_round_robin(consumers, all_partitions)
        elif strategy == AssignmentStrategy.STICKY:
            self._assign_sticky(consumers, all_partitions)

        # Update partition ownership
        self.partition_ownership.clear()
        for consumer in consumers:
            for partition in consumer.assigned_partitions:
                self.partition_ownership[(partition.topic, partition.partition)] = consumer.consumer_id

        print(f"  [Rebalance complete]")

        # Show assignments
        for consumer in consumers:
            print(f"    {consumer.consumer_id}: {len(consumer.assigned_partitions)} partitions")

    def _assign_range(self, consumers: List[ConsumerMetadata], partitions: List[Partition]):
        """Range assignment strategy"""
        # Group partitions by topic
        topic_partitions: Dict[str, List[Partition]] = defaultdict(list)
        for partition in partitions:
            topic_partitions[partition.topic].append(partition)

        # Sort consumers for deterministic assignment
        sorted_consumers = sorted(consumers, key=lambda c: c.consumer_id)

        # Assign partitions per topic
        for topic, topic_parts in topic_partitions.items():
            sorted_partitions = sorted(topic_parts, key=lambda p: p.partition)

            # Divide partitions among consumers
            partitions_per_consumer = len(sorted_partitions) // len(sorted_consumers)
            extra_partitions = len(sorted_partitions) % len(sorted_consumers)

            partition_idx = 0
            for consumer_idx, consumer in enumerate(sorted_consumers):
                # Calculate partition count for this consumer
                count = partitions_per_consumer + (1 if consumer_idx < extra_partitions else 0)

                # Assign partitions
                for _ in range(count):
                    if partition_idx < len(sorted_partitions):
                        consumer.assigned_partitions.add(
                            (sorted_partitions[partition_idx].topic,
                             sorted_partitions[partition_idx].partition)
                        )
                        partition_idx += 1

    def _assign_round_robin(self, consumers: List[ConsumerMetadata], partitions: List[Partition]):
        """Round-robin assignment strategy"""
        sorted_consumers = sorted(consumers, key=lambda c: c.consumer_id)
        sorted_partitions = sorted(partitions, key=lambda p: (p.topic, p.partition))

        for idx, partition in enumerate(sorted_partitions):
            consumer = sorted_consumers[idx % len(sorted_consumers)]
            consumer.assigned_partitions.add((partition.topic, partition.partition))

    def _assign_sticky(self, consumers: List[ConsumerMetadata], partitions: List[Partition]):
        """
        Sticky assignment strategy

        Tries to keep existing assignments during rebalance
        """
        # For simplicity, use round-robin
        # In production: Track previous assignments and minimize movement
        self._assign_round_robin(consumers, partitions)


# ============================================================================
# Consumer
# ============================================================================

class KafkaConsumer:
    """
    Kafka consumer with group support

    Automatically handles group coordination and rebalancing
    """

    def __init__(self, group_id: str, topics: List[str],
                 coordinator: GroupCoordinator,
                 auto_offset_reset: str = 'latest'):
        self.group_id = group_id
        self.topics = topics
        self.coordinator = coordinator
        self.auto_offset_reset = auto_offset_reset

        # Consumer metadata
        self.consumer_id = f"consumer-{uuid.uuid4().hex[:8]}"
        self.client_id = f"client-{uuid.uuid4().hex[:8]}"

        # Offset tracking
        self.committed_offsets: Dict[tuple, int] = {}  # (topic, partition) -> offset
        self.current_offsets: Dict[tuple, int] = {}

        # State
        self.metadata: Optional[ConsumerMetadata] = None
        self.running = False

    def subscribe(self):
        """Subscribe to topics and join group"""
        self.metadata = self.coordinator.join_group(
            self.group_id,
            self.consumer_id,
            self.client_id,
            self.topics
        )

        print(f"\\nConsumer {self.consumer_id} subscribed to {self.topics}")

    def poll(self, timeout: float = 1.0) -> List:
        """
        Poll for messages

        Returns messages from assigned partitions
        """
        if not self.metadata:
            raise Exception("Consumer not subscribed")

        # Send heartbeat
        self.coordinator.heartbeat(self.group_id, self.consumer_id)

        # Simulate fetching messages from assigned partitions
        messages = []

        for topic, partition in self.metadata.assigned_partitions:
            # Get current offset
            offset = self.current_offsets.get((topic, partition), 0)

            # Simulate message
            message = {
                'topic': topic,
                'partition': partition,
                'offset': offset,
                'key': f'key-{offset}',
                'value': f'message-{offset}'
            }

            messages.append(message)

            # Update current offset
            self.current_offsets[(topic, partition)] = offset + 1

        return messages

    def commit(self):
        """Commit current offsets"""
        for partition_key, offset in self.current_offsets.items():
            self.committed_offsets[partition_key] = offset

        print(f"  [Committed offsets: {len(self.committed_offsets)} partitions]")

    def close(self):
        """Close consumer and leave group"""
        if self.metadata:
            self.coordinator.leave_group(self.group_id, self.consumer_id)

        print(f"Consumer {self.consumer_id} closed")


# ============================================================================
# Example Usage
# ============================================================================

def example_consumer_group():
    """Example: Consumer group with multiple consumers"""
    print("\\n1. CONSUMER GROUP - BASIC")
    print("-" * 80)

    coordinator = GroupCoordinator()

    # Create 3 consumers in same group
    consumer1 = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer2 = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer3 = KafkaConsumer("my-group", ["orders"], coordinator)

    # Subscribe (triggers rebalance)
    consumer1.subscribe()
    consumer2.subscribe()
    consumer3.subscribe()

    # Show assignments
    print("\\nAssignments after rebalance:")
    for consumer in [consumer1, consumer2, consumer3]:
        print(f"  {consumer.consumer_id}: {consumer.metadata.assigned_partitions}")

    # Poll messages
    print("\\nPolling messages:")
    for consumer in [consumer1, consumer2, consumer3]:
        messages = consumer.poll()
        print(f"  {consumer.consumer_id} received {len(messages)} messages")

    # Clean up
    consumer1.close()
    consumer2.close()
    consumer3.close()


def example_rebalancing():
    """Example: Rebalancing when consumer joins/leaves"""
    print("\\n2. REBALANCING")
    print("-" * 80)

    coordinator = GroupCoordinator()

    # Start with 2 consumers
    print("Starting with 2 consumers:")
    consumer1 = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer2 = KafkaConsumer("my-group", ["orders"], coordinator)

    consumer1.subscribe()
    consumer2.subscribe()

    # Add 3rd consumer (triggers rebalance)
    print("\\nAdding 3rd consumer (triggers rebalance):")
    consumer3 = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer3.subscribe()

    # Remove consumer (triggers rebalance)
    print("\\nRemoving consumer 2 (triggers rebalance):")
    consumer2.close()

    # Clean up
    consumer1.close()
    consumer3.close()


def example_offset_management():
    """Example: Offset commit and management"""
    print("\\n3. OFFSET MANAGEMENT")
    print("-" * 80)

    coordinator = GroupCoordinator()
    consumer = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer.subscribe()

    # Poll and process messages
    print("\\nProcessing messages:")
    for i in range(3):
        messages = consumer.poll()
        print(f"  Batch {i + 1}: {len(messages)} messages")

        # Process messages...

        # Commit offsets
        consumer.commit()

    consumer.close()


def example_consumer_lag():
    """Example: Monitoring consumer lag"""
    print("\\n4. CONSUMER LAG MONITORING")
    print("-" * 80)

    coordinator = GroupCoordinator()
    consumer = KafkaConsumer("my-group", ["orders"], coordinator)
    consumer.subscribe()

    # Simulate processing lag
    print("\\nSimulating consumer lag:")

    # Latest offset (from broker)
    latest_offsets = {
        ("orders", 0): 1000,
        ("orders", 1): 950,
        ("orders", 2): 1100
    }

    # Consumer committed offsets
    consumer.committed_offsets = {
        ("orders", 0): 850,
        ("orders", 1): 900,
        ("orders", 2): 1050
    }

    # Calculate lag
    print("\\nConsumer lag per partition:")
    for partition_key, latest_offset in latest_offsets.items():
        committed = consumer.committed_offsets.get(partition_key, 0)
        lag = latest_offset - committed
        print(f"  {partition_key}: lag = {lag} messages")

    consumer.close()


# ============================================================================
# Main Example
# ============================================================================

def main():
    print("=" * 80)
    print("KAFKA CONSUMER GROUPS")
    print("=" * 80)

    example_consumer_group()
    example_rebalancing()
    example_offset_management()
    example_consumer_lag()

    print("\\n" + "=" * 80)
    print("CONSUMER GROUP BEST PRACTICES")
    print("=" * 80)
    print("""
1. GROUP COORDINATION:
   - Use same group.id for related consumers
   - Consumers auto-balance partitions
   - Rebalancing happens on join/leave
   - One partition per consumer in group

2. PARTITION ASSIGNMENT:
   - Range: Default, assigns ranges per topic
   - RoundRobin: Even distribution across topics
   - Sticky: Minimizes partition movement
   - CooperativeSticky: Incremental rebalancing

3. OFFSET MANAGEMENT:
   - Commit offsets regularly
   - enable.auto.commit=false for manual control
   - Commit after processing (at-least-once)
   - Use transactions for exactly-once

4. REBALANCING:
   - Happens when consumer joins/leaves
   - All consumers pause during rebalance
   - Keep rebalances fast (<3s)
   - Monitor rebalance frequency

5. CONSUMER LAG:
   - Monitor lag per partition
   - Lag = latest_offset - committed_offset
   - Alert on high lag (>1000 messages)
   - Scale consumers if lag growing

6. SCALING:
   - Max consumers = partition count
   - Add partitions to scale beyond consumer count
   - Monitor partition distribution
   - Balance partition load

7. SESSION MANAGEMENT:
   - Send heartbeats regularly
   - session.timeout.ms = 10000 (10s)
   - max.poll.interval.ms = 300000 (5min)
   - Keep poll loop active

8. ERROR HANDLING:
   - Handle rebalance events
   - Retry transient failures
   - Use dead letter queue for poison pills
   - Monitor failed message count
""")

    print("\\n✓ Kafka consumer groups complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_907():
    """Apache Kafka - Producer and Consumer"""
    return '''# Apache Kafka - Producer and Consumer
# In production: pip install kafka-python

"""
Apache Kafka Producer and Consumer

Complete guide to Kafka producers and consumers:
- Producer API and configuration
- Consumer API and polling
- Message serialization
- Acknowledgements and durability
- Error handling and retries
- Performance tuning

Used by: LinkedIn, Uber, Netflix for event streaming
"""

import time
import json
import uuid
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass
from collections import deque, defaultdict


# ============================================================================
# Message and Record
# ============================================================================

@dataclass
class ProducerRecord:
    """Producer record to send"""
    topic: str
    value: str
    key: Optional[str] = None
    partition: Optional[int] = None
    headers: Optional[Dict[str, str]] = None


@dataclass
class ConsumerRecord:
    """Consumer record received"""
    topic: str
    partition: int
    offset: int
    key: Optional[str]
    value: str
    timestamp: float
    headers: Dict[str, str]


# ============================================================================
# Topic and Partition
# ============================================================================

class TopicPartition:
    """Simulated Kafka topic partition"""

    def __init__(self, topic: str, partition: int):
        self.topic = topic
        self.partition = partition
        self.messages: deque = deque()
        self.high_water_mark = 0  # Latest offset

    def append(self, key: Optional[str], value: str, headers: Dict = None) -> int:
        """Append message and return offset"""
        offset = self.high_water_mark
        timestamp = time.time()

        record = ConsumerRecord(
            topic=self.topic,
            partition=self.partition,
            offset=offset,
            key=key,
            value=value,
            timestamp=timestamp,
            headers=headers or {}
        )

        self.messages.append(record)
        self.high_water_mark += 1

        return offset

    def read(self, offset: int, max_messages: int = 100) -> List[ConsumerRecord]:
        """Read messages from offset"""
        results = []

        for record in self.messages:
            if record.offset >= offset and len(results) < max_messages:
                results.append(record)

        return results


# ============================================================================
# Kafka Cluster (simulated)
# ============================================================================

class KafkaCluster:
    """Simulated Kafka cluster"""

    def __init__(self):
        self.topics: Dict[str, List[TopicPartition]] = defaultdict(list)

    def create_topic(self, topic: str, num_partitions: int = 3):
        """Create topic with partitions"""
        if topic not in self.topics:
            for partition_num in range(num_partitions):
                self.topics[topic].append(TopicPartition(topic, partition_num))

            print(f"  [Topic '{topic}' created with {num_partitions} partitions]")

    def get_partition(self, topic: str, partition: int) -> TopicPartition:
        """Get specific partition"""
        if topic in self.topics and partition < len(self.topics[topic]):
            return self.topics[topic][partition]

        raise ValueError(f"Partition {partition} not found for topic {topic}")

    def partition_for_key(self, topic: str, key: Optional[str]) -> int:
        """Determine partition for key using hash"""
        if topic not in self.topics:
            raise ValueError(f"Topic {topic} not found")

        num_partitions = len(self.topics[topic])

        if key is None:
            # Round-robin for null keys
            return 0

        # Hash key to partition
        return hash(key) % num_partitions


# ============================================================================
# Kafka Producer
# ============================================================================

class KafkaProducer:
    """
    Kafka Producer

    Sends messages to Kafka topics with reliability guarantees
    """

    def __init__(self, cluster: KafkaCluster,
                 acks: str = 'all',
                 retries: int = 3,
                 batch_size: int = 16384):
        self.cluster = cluster
        self.acks = acks  # 0, 1, or 'all'
        self.retries = retries
        self.batch_size = batch_size

        # Metrics
        self.messages_sent = 0
        self.bytes_sent = 0
        self.errors = 0

    def send(self, record: ProducerRecord, callback: Callable = None) -> 'Future':
        """
        Send message asynchronously

        Returns Future that can be used to get result
        """
        try:
            # Determine partition
            if record.partition is None:
                partition = self.cluster.partition_for_key(record.topic, record.key)
            else:
                partition = record.partition

            # Get partition
            topic_partition = self.cluster.get_partition(record.topic, partition)

            # Write to partition
            offset = topic_partition.append(record.key, record.value, record.headers)

            # Update metrics
            self.messages_sent += 1
            self.bytes_sent += len(record.value.encode())

            # Create metadata
            metadata = RecordMetadata(
                topic=record.topic,
                partition=partition,
                offset=offset,
                timestamp=time.time()
            )

            # Call callback if provided
            if callback:
                callback(metadata, None)

            # Return future
            future = Future()
            future.set_result(metadata)
            return future

        except Exception as e:
            self.errors += 1

            if callback:
                callback(None, e)

            future = Future()
            future.set_exception(e)
            return future

    def flush(self):
        """Flush any buffered messages"""
        # In real implementation, flush batched messages
        print("  [Producer flushed]")

    def close(self):
        """Close producer"""
        self.flush()
        print(f"Producer closed ({self.messages_sent} messages sent)")


@dataclass
class RecordMetadata:
    """Metadata for sent record"""
    topic: str
    partition: int
    offset: int
    timestamp: float


class Future:
    """Future for async operations"""

    def __init__(self):
        self._result = None
        self._exception = None
        self._done = False

    def set_result(self, result):
        self._result = result
        self._done = True

    def set_exception(self, exception):
        self._exception = exception
        self._done = True

    def get(self, timeout: float = None) -> RecordMetadata:
        """Wait for and return result"""
        if self._exception:
            raise self._exception
        return self._result


# ============================================================================
# Kafka Consumer
# ============================================================================

class KafkaConsumer:
    """
    Kafka Consumer

    Reads messages from Kafka topics
    """

    def __init__(self, topics: List[str], cluster: KafkaCluster,
                 group_id: str = None,
                 auto_offset_reset: str = 'latest',
                 enable_auto_commit: bool = True):
        self.topics = topics
        self.cluster = cluster
        self.group_id = group_id or f"group-{uuid.uuid4().hex[:8]}"
        self.auto_offset_reset = auto_offset_reset
        self.enable_auto_commit = enable_auto_commit

        # Offset tracking
        self.offsets: Dict[tuple, int] = {}  # (topic, partition) -> offset
        self.committed_offsets: Dict[tuple, int] = {}

        # Subscribe to topics
        self._subscribe()

    def _subscribe(self):
        """Subscribe to topics"""
        for topic in self.topics:
            if topic not in self.cluster.topics:
                self.cluster.create_topic(topic)

            # Initialize offsets
            for partition in range(len(self.cluster.topics[topic])):
                partition_key = (topic, partition)

                if self.auto_offset_reset == 'earliest':
                    self.offsets[partition_key] = 0
                else:  # latest
                    topic_partition = self.cluster.get_partition(topic, partition)
                    self.offsets[partition_key] = topic_partition.high_water_mark

    def poll(self, timeout_ms: int = 1000, max_records: int = 100) -> List[ConsumerRecord]:
        """
        Poll for messages

        Returns list of ConsumerRecords
        """
        records = []

        for topic in self.topics:
            for partition_num in range(len(self.cluster.topics[topic])):
                partition_key = (topic, partition_num)
                offset = self.offsets.get(partition_key, 0)

                # Read messages
                topic_partition = self.cluster.get_partition(topic, partition_num)
                partition_records = topic_partition.read(offset, max_records)

                records.extend(partition_records)

                # Update offset
                if partition_records:
                    last_offset = partition_records[-1].offset
                    self.offsets[partition_key] = last_offset + 1

        # Auto-commit if enabled
        if self.enable_auto_commit and records:
            self.commit()

        return records

    def commit(self):
        """Commit current offsets"""
        self.committed_offsets = self.offsets.copy()
        # print(f"  [Offsets committed]")

    def seek(self, topic: str, partition: int, offset: int):
        """Seek to specific offset"""
        self.offsets[(topic, partition)] = offset

    def close(self):
        """Close consumer"""
        self.commit()
        print(f"Consumer closed (group: {self.group_id})")


# ============================================================================
# Example Usage
# ============================================================================

def example_basic_producer_consumer():
    """Example: Basic producer and consumer"""
    print("\\n1. BASIC PRODUCER AND CONSUMER")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("orders", num_partitions=3)

    # Producer
    producer = KafkaProducer(cluster)

    print("\\nProducing messages:")
    for i in range(5):
        record = ProducerRecord(
            topic="orders",
            key=f"order-{i}",
            value=json.dumps({"order_id": i, "amount": 100.0 * (i + 1)})
        )

        future = producer.send(record)
        metadata = future.get()
        print(f"  Sent: partition={metadata.partition}, offset={metadata.offset}")

    producer.close()

    # Consumer
    consumer = KafkaConsumer(["orders"], cluster, auto_offset_reset='earliest')

    print("\\nConsuming messages:")
    records = consumer.poll()
    for record in records:
        data = json.loads(record.value)
        print(f"  Received: partition={record.partition}, offset={record.offset}, data={data}")

    consumer.close()


def example_producer_callback():
    """Example: Producer with callback"""
    print("\\n2. PRODUCER WITH CALLBACK")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("events")

    producer = KafkaProducer(cluster)

    def on_send_success(metadata, error):
        """Callback for send completion"""
        if error:
            print(f"  ✗ Send failed: {error}")
        else:
            print(f"  ✓ Sent: partition={metadata.partition}, offset={metadata.offset}")

    # Send with callback
    for i in range(3):
        record = ProducerRecord(
            topic="events",
            value=f"event-{i}"
        )
        producer.send(record, callback=on_send_success)

    producer.close()


def example_partitioning():
    """Example: Key-based partitioning"""
    print("\\n3. KEY-BASED PARTITIONING")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("user-events", num_partitions=3)

    producer = KafkaProducer(cluster)

    # Messages with same key go to same partition
    users = ["user1", "user2", "user1", "user3", "user2"]

    print("\\nSending messages with keys:")
    for user in users:
        record = ProducerRecord(
            topic="user-events",
            key=user,
            value=f"event from {user}"
        )

        future = producer.send(record)
        metadata = future.get()
        print(f"  {user} -> partition {metadata.partition}")

    producer.close()


def example_offset_management():
    """Example: Manual offset management"""
    print("\\n4. MANUAL OFFSET MANAGEMENT")
    print("-" * 80)

    cluster = KafkaCluster()
    cluster.create_topic("logs")

    # Produce some messages
    producer = KafkaProducer(cluster)
    for i in range(10):
        producer.send(ProducerRecord("logs", value=f"log-{i}"))
    producer.close()

    # Consumer with manual commit
    consumer = KafkaConsumer(
        ["logs"],
        cluster,
        auto_offset_reset='earliest',
        enable_auto_commit=False
    )

    # Poll and manually commit
    print("\\nProcessing messages:")
    records = consumer.poll(max_records=5)
    print(f"  Batch 1: {len(records)} messages")

    # Process messages...
    consumer.commit()
    print("  Offsets committed")

    # Poll again
    records = consumer.poll(max_records=5)
    print(f"  Batch 2: {len(records)} messages")

    consumer.close()


# ============================================================================
# Main Example
# ============================================================================

def main():
    print("=" * 80)
    print("KAFKA PRODUCER AND CONSUMER")
    print("=" * 80)

    example_basic_producer_consumer()
    example_producer_callback()
    example_partitioning()
    example_offset_management()

    print("\\n" + "=" * 80)
    print("PRODUCER/CONSUMER BEST PRACTICES")
    print("=" * 80)
    print("""
1. PRODUCER CONFIGURATION:
   - acks='all': Wait for all replicas (durability)
   - acks=1: Wait for leader only (balance)
   - acks=0: No acknowledgement (speed)
   - retries=3: Retry on transient failures
   - batch.size=16384: Batch messages for efficiency

2. CONSUMER CONFIGURATION:
   - group.id: Consumer group for load balancing
   - auto.offset.reset: earliest or latest
   - enable.auto.commit: false for manual control
   - max.poll.records: Limit messages per poll
   - session.timeout.ms: Heartbeat timeout

3. MESSAGE KEYS:
   - Use keys for partition affinity
   - Messages with same key go to same partition
   - Maintains ordering per key
   - Good for user/account data

4. ERROR HANDLING:
   - Implement retry logic
   - Use callbacks for async errors
   - Monitor send failures
   - Handle deserialization errors

5. OFFSET MANAGEMENT:
   - Commit after processing
   - Don't commit too frequently (overhead)
   - Handle rebalancing
   - Store offsets externally if needed

6. PERFORMANCE:
   - Batch messages when possible
   - Use compression (gzip, snappy)
   - Tune linger.ms for batching
   - Monitor producer/consumer lag

7. SERIALIZATION:
   - Use JSON for human-readable
   - Use Avro/Protobuf for efficiency
   - Include schema version
   - Handle schema evolution

8. MONITORING:
   - Track producer/consumer lag
   - Monitor error rates
   - Alert on high latency
   - Track partition distribution
""")

    print("\\n✓ Kafka producer and consumer complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: More Kafka Lessons")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (909, upgrade_lesson_909, "Kafka - Consumer Groups"),
        (907, upgrade_lesson_907, "Apache Kafka - Producer and Consumer"),
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
    print("MORE KAFKA LESSONS COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
