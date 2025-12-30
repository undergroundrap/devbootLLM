#!/usr/bin/env python3
"""
Upgrade Redis lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 15: Redis Pub/Sub and Caching Strategies
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 852: Redis Pub/Sub Messaging
    lesson_852 = next(l for l in lessons if l['id'] == 852)
    lesson_852['fullSolution'] = '''# Redis Pub/Sub Messaging - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis Pub/Sub for real-time messaging patterns

import time
import threading
from typing import Any, Callable, Dict, List, Set
from dataclasses import dataclass, field
from collections import defaultdict
import uuid

@dataclass
class Message:
    """Published message."""
    channel: str
    data: str
    pattern: str = None  # For pattern subscriptions
    timestamp: float = field(default_factory=time.time)

class PubSub:
    """
    Redis Pub/Sub simulation.

    Pub/Sub provides:
    - One-to-many messaging
    - Fire-and-forget delivery
    - Pattern-based subscriptions
    - Real-time notifications
    """

    def __init__(self):
        # Channel -> subscribers
        self.subscribers: Dict[str, Set[str]] = defaultdict(set)

        # Pattern -> subscribers
        self.pattern_subscribers: Dict[str, Set[str]] = defaultdict(set)

        # Subscriber ID -> callback
        self.callbacks: Dict[str, Callable] = {}

        # Active subscriptions
        self.active = True

    def subscribe(self, *channels: str) -> 'Subscriber':
        """
        Subscribe to channels.

        Returns Subscriber object for receiving messages.
        """
        subscriber_id = str(uuid.uuid4())
        subscriber = Subscriber(subscriber_id, self)

        for channel in channels:
            self.subscribers[channel].add(subscriber_id)
            print(f"[PUBSUB] Subscribed to channel '{channel}'")

        return subscriber

    def psubscribe(self, *patterns: str) -> 'Subscriber':
        """
        Subscribe to channel patterns.

        Patterns support wildcards:
        - news.* : matches news.sports, news.tech, etc.
        - user:*:notifications : matches user:123:notifications
        """
        subscriber_id = str(uuid.uuid4())
        subscriber = Subscriber(subscriber_id, self)

        for pattern in patterns:
            self.pattern_subscribers[pattern].add(subscriber_id)
            print(f"[PUBSUB] Subscribed to pattern '{pattern}'")

        return subscriber

    def publish(self, channel: str, message: str) -> int:
        """
        Publish message to channel.

        Returns: number of subscribers that received the message
        """
        count = 0

        # Send to direct channel subscribers
        if channel in self.subscribers:
            msg = Message(channel=channel, data=message)
            for subscriber_id in self.subscribers[channel]:
                if subscriber_id in self.callbacks:
                    self.callbacks[subscriber_id](msg)
                    count += 1

        # Send to pattern subscribers
        for pattern, subscriber_ids in self.pattern_subscribers.items():
            if self._matches_pattern(channel, pattern):
                msg = Message(channel=channel, data=message, pattern=pattern)
                for subscriber_id in subscriber_ids:
                    if subscriber_id in self.callbacks:
                        self.callbacks[subscriber_id](msg)
                        count += 1

        if count > 0:
            print(f"[PUBSUB] Published to '{channel}': {message} ({count} subscribers)")

        return count

    def _matches_pattern(self, channel: str, pattern: str) -> bool:
        """Check if channel matches pattern."""
        # Simple wildcard matching
        if pattern == "*":
            return True

        # Handle suffix wildcard (news.*)
        if pattern.endswith("*"):
            prefix = pattern[:-1]
            return channel.startswith(prefix)

        # Handle middle wildcard (user:*:notifications)
        if "*" in pattern:
            parts = pattern.split("*")
            pos = 0
            for part in parts:
                if part:
                    idx = channel.find(part, pos)
                    if idx == -1:
                        return False
                    pos = idx + len(part)
            return True

        return channel == pattern

    def unsubscribe(self, subscriber_id: str, *channels: str):
        """Unsubscribe from channels."""
        for channel in channels:
            if channel in self.subscribers:
                self.subscribers[channel].discard(subscriber_id)
                print(f"[PUBSUB] Unsubscribed from '{channel}'")

    def punsubscribe(self, subscriber_id: str, *patterns: str):
        """Unsubscribe from patterns."""
        for pattern in patterns:
            if pattern in self.pattern_subscribers:
                self.pattern_subscribers[pattern].discard(subscriber_id)
                print(f"[PUBSUB] Unsubscribed from pattern '{pattern}'")

    def register_callback(self, subscriber_id: str, callback: Callable):
        """Register message handler."""
        self.callbacks[subscriber_id] = callback

class Subscriber:
    """Subscriber for receiving messages."""

    def __init__(self, subscriber_id: str, pubsub: PubSub):
        self.subscriber_id = subscriber_id
        self.pubsub = pubsub
        self.messages: List[Message] = []

    def listen(self) -> List[Message]:
        """
        Listen for messages (blocking).

        In production, this would be a generator that yields messages.
        """
        def callback(message: Message):
            self.messages.append(message)

        self.pubsub.register_callback(self.subscriber_id, callback)
        return self.messages

    def get_message(self, timeout: float = None) -> Message:
        """Get next message (non-blocking with timeout)."""
        start = time.time()

        while True:
            if self.messages:
                return self.messages.pop(0)

            if timeout and (time.time() - start) > timeout:
                return None

            time.sleep(0.01)

# Example 1: Basic Pub/Sub
print("Example 1: Basic Pub/Sub")
print("=" * 60)

pubsub = PubSub()

# Subscribe to channel
subscriber1 = pubsub.subscribe("news")
subscriber1.listen()

# Publish message
print("\\nPublishing message:")
pubsub.publish("news", "Breaking: New Python release!")

# Receive message
msg = subscriber1.get_message(timeout=1)
if msg:
    print(f"\\nReceived: [{msg.channel}] {msg.data}")

print()

# Example 2: Multiple Subscribers
print("Example 2: Multiple Subscribers (Fan-out)")
print("=" * 60)

pubsub2 = PubSub()

# Multiple subscribers to same channel
subscriber_a = pubsub2.subscribe("alerts")
subscriber_a.listen()

subscriber_b = pubsub2.subscribe("alerts")
subscriber_b.listen()

subscriber_c = pubsub2.subscribe("alerts")
subscriber_c.listen()

# Publish once, all receive
print("\\nPublishing alert to 3 subscribers:")
count = pubsub2.publish("alerts", "System maintenance at 2 AM")

print(f"\\nSubscribers notified: {count}")

# All receive the same message
for i, sub in enumerate([subscriber_a, subscriber_b, subscriber_c], 1):
    msg = sub.get_message(timeout=1)
    if msg:
        print(f"  Subscriber {i} received: {msg.data}")

print()

# Example 3: Pattern Subscriptions
print("Example 3: Pattern Subscriptions")
print("=" * 60)

pubsub3 = PubSub()

# Subscribe to all news channels
subscriber = pubsub3.psubscribe("news.*")
subscriber.listen()

# Publish to different news channels
print("\\nPublishing to multiple news channels:")
pubsub3.publish("news.sports", "Lakers win championship!")
pubsub3.publish("news.tech", "New AI breakthrough announced")
pubsub3.publish("news.world", "Climate summit concludes")
pubsub3.publish("weather", "Sunny tomorrow")  # Won't match pattern

print("\\nReceived messages (pattern: news.*):")
for i in range(3):
    msg = subscriber.get_message(timeout=1)
    if msg:
        print(f"  [{msg.channel}] {msg.data}")

print()

# Example 4: Chat Room Simulation
print("Example 4: Chat Room Simulation")
print("=" * 60)

pubsub4 = PubSub()

class ChatUser:
    """Chat user with Pub/Sub."""

    def __init__(self, username: str, room: str):
        self.username = username
        self.room = room
        self.subscriber = pubsub4.subscribe(f"chat:{room}")
        self.messages = []

        # Setup message handler
        def on_message(msg: Message):
            self.messages.append(msg.data)
            print(f"  [{self.username}] received: {msg.data}")

        self.subscriber.listen()
        pubsub4.register_callback(self.subscriber.subscriber_id, on_message)

    def send(self, message: str):
        """Send message to room."""
        formatted = f"{self.username}: {message}"
        pubsub4.publish(f"chat:{self.room}", formatted)

# Create chat users
print("Creating chat room 'general' with 3 users:")
alice = ChatUser("Alice", "general")
bob = ChatUser("Bob", "general")
charlie = ChatUser("Charlie", "general")

print("\\nChat conversation:")
alice.send("Hello everyone!")
time.sleep(0.1)

bob.send("Hi Alice!")
time.sleep(0.1)

charlie.send("Hey team!")
time.sleep(0.1)

print()

# Example 5: Real-time Notifications
print("Example 5: Real-time Notifications System")
print("=" * 60)

pubsub5 = PubSub()

class NotificationService:
    """User notification service."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.notifications = []

        # Subscribe to user-specific notifications
        self.subscriber = pubsub5.subscribe(f"user:{user_id}:notifications")

        def on_notification(msg: Message):
            self.notifications.append({
                'timestamp': msg.timestamp,
                'message': msg.data
            })
            print(f"  [User {self.user_id}] 🔔 {msg.data}")

        self.subscriber.listen()
        pubsub5.register_callback(self.subscriber.subscriber_id, on_notification)

    def get_notifications(self) -> List[Dict]:
        """Get all notifications."""
        return self.notifications

# Setup notification services for users
print("Setting up notification services:")
user_123 = NotificationService(123)
user_456 = NotificationService(456)

print("\\nSending notifications:")
pubsub5.publish("user:123:notifications", "New message from Bob")
time.sleep(0.05)

pubsub5.publish("user:456:notifications", "Your order has shipped")
time.sleep(0.05)

pubsub5.publish("user:123:notifications", "Comment on your post")
time.sleep(0.05)

print(f"\\nUser 123 has {len(user_123.get_notifications())} notifications")
print(f"User 456 has {len(user_456.get_notifications())} notifications")

print()

# Example 6: Event Broadcasting
print("Example 6: Event Broadcasting")
print("=" * 60)

pubsub6 = PubSub()

# Multiple services subscribe to system events
class EventListener:
    def __init__(self, name: str, event_pattern: str):
        self.name = name
        self.events = []
        self.subscriber = pubsub6.psubscribe(event_pattern)

        def on_event(msg: Message):
            self.events.append(msg)
            print(f"  [{self.name}] Event: {msg.channel} -> {msg.data}")

        self.subscriber.listen()
        pubsub6.register_callback(self.subscriber.subscriber_id, on_event)

print("Setting up event listeners:")
logger = EventListener("Logger", "events.*")
analytics = EventListener("Analytics", "events.user.*")
alerting = EventListener("Alerting", "events.error.*")

print("\\nBroadcasting events:")
pubsub6.publish("events.user.login", "user_id=123")
time.sleep(0.05)

pubsub6.publish("events.user.logout", "user_id=123")
time.sleep(0.05)

pubsub6.publish("events.error.500", "Internal server error")
time.sleep(0.05)

pubsub6.publish("events.system.startup", "System started")
time.sleep(0.05)

print(f"\\nLogger captured {len(logger.events)} events (all events)")
print(f"Analytics captured {len(analytics.events)} events (user events only)")
print(f"Alerting captured {len(alerting.events)} events (errors only)")

print()
print("=" * 60)
print("REDIS PUB/SUB BEST PRACTICES")
print("=" * 60)
print("""
WHEN TO USE PUB/SUB:

✓ Real-time notifications
✓ Chat applications
✓ Live updates (dashboards, feeds)
✓ Event broadcasting
✓ Cache invalidation
✓ Microservice coordination
✓ Log aggregation

WHEN NOT TO USE:

✗ Guaranteed delivery needed (use queues)
✗ Message persistence required (use streams)
✗ Work distribution (use task queues)
✗ Request/response pattern (use RPC)

KEY CHARACTERISTICS:

Fire-and-forget:
  - No message persistence
  - Subscribers must be active
  - Missed messages are lost

Fan-out:
  - One message -> many subscribers
  - All subscribers get copy
  - No message acknowledgment

Pattern matching:
  - Subscribe to wildcards
  - news.* matches news.sports, news.tech
  - Efficient routing

COMMON PATTERNS:

1. Chat Rooms:
   SUBSCRIBE chat:room:123
   PUBLISH chat:room:123 "message"

2. User Notifications:
   SUBSCRIBE user:${user_id}:notifications
   PUBLISH user:123:notifications "alert"

3. System Events:
   PSUBSCRIBE events.*
   PUBLISH events.user.login "data"

4. Cache Invalidation:
   SUBSCRIBE cache:invalidate
   PUBLISH cache:invalidate "user:123"

5. Real-time Analytics:
   PSUBSCRIBE metrics.*
   PUBLISH metrics.page_views "100"

PERFORMANCE TIPS:

  - Use patterns wisely (overhead)
  - Keep messages small (< 1KB)
  - Limit subscribers per channel
  - Monitor memory usage
  - Use connection pooling

SCALING CONSIDERATIONS:

  Single Redis:
    - All messages through one node
    - Limited by network bandwidth
    - Good for 1000s msgs/sec

  Redis Cluster:
    - Pub/Sub is global (all nodes)
    - Messages replicated cluster-wide
    - Watch for network amplification

  Sharding:
    - Separate Redis instances
    - Partition by channel prefix
    - Application-level routing

RELIABILITY:

  No guarantees:
    - Messages may be lost
    - No delivery confirmation
    - No replay capability

  Improve reliability:
    - Combine with persistence
    - Use Redis Streams for history
    - Implement heartbeats
    - Add application-level ACKs

MONITORING:

  Commands:
    PUBSUB CHANNELS - List active channels
    PUBSUB NUMSUB channel - Subscriber count
    PUBSUB NUMPAT - Pattern subscriptions

  Metrics:
    - Messages per second
    - Subscriber counts
    - Pattern overhead
    - Connection count

ALTERNATIVES:

  Redis Streams:
    + Message persistence
    + Consumer groups
    + Message replay
    - More complex

  Message Queues (RabbitMQ, Kafka):
    + Guaranteed delivery
    + Persistence
    + Acknowledgments
    - Higher latency
    - More resources

  WebSockets:
    + Bidirectional
    + Browser support
    - Connection overhead

Production note: Real Redis Pub/Sub provides:
  - SUBSCRIBE/PSUBSCRIBE commands
  - PUBLISH returns subscriber count
  - Cluster-wide message propagation
  - Pattern-based subscriptions
  - Low-latency messaging (< 1ms)
  - CLIENT KILL for cleanup
  - Connection monitoring
  - Max message size: 512MB
""")
'''

    # Lesson 1003: Redis Pub/Sub Real-time Messaging
    lesson_1003 = next(l for l in lessons if l['id'] == 1003)
    lesson_1003['fullSolution'] = '''# Redis Pub/Sub Real-time Messaging - Complete Simulation
# In production: pip install redis
# This lesson simulates advanced Redis Pub/Sub patterns for real-time applications

import time
import threading
from typing import Any, Callable, Dict, List, Optional, Set
from dataclasses import dataclass, field
from collections import defaultdict, deque
import json
import uuid

@dataclass
class RealtimeMessage:
    """Real-time message with metadata."""
    id: str
    channel: str
    event_type: str
    data: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    sender: Optional[str] = None

class RealtimePubSub:
    """Enhanced Pub/Sub with real-time features."""

    def __init__(self):
        self.subscribers: Dict[str, Set[str]] = defaultdict(set)
        self.callbacks: Dict[str, Callable] = {}
        self.message_history: Dict[str, deque] = defaultdict(lambda: deque(maxlen=100))
        self.presence: Dict[str, Set[str]] = defaultdict(set)  # Channel -> active users

    def subscribe(self, channel: str, user_id: str = None) -> 'RealtimeSubscriber':
        """Subscribe with presence tracking."""
        subscriber_id = str(uuid.uuid4())
        subscriber = RealtimeSubscriber(subscriber_id, channel, self)

        self.subscribers[channel].add(subscriber_id)

        # Track presence
        if user_id:
            self.presence[channel].add(user_id)
            self._broadcast_presence(channel, user_id, "joined")

        return subscriber

    def publish(self, channel: str, event_type: str, data: Dict, sender: str = None) -> int:
        """Publish real-time message."""
        message = RealtimeMessage(
            id=str(uuid.uuid4()),
            channel=channel,
            event_type=event_type,
            data=data,
            sender=sender
        )

        # Store in history
        self.message_history[channel].append(message)

        # Deliver to subscribers
        count = 0
        if channel in self.subscribers:
            for subscriber_id in self.subscribers[channel]:
                if subscriber_id in self.callbacks:
                    self.callbacks[subscriber_id](message)
                    count += 1

        return count

    def _broadcast_presence(self, channel: str, user_id: str, action: str):
        """Broadcast presence change."""
        self.publish(channel, "presence", {
            "user_id": user_id,
            "action": action,
            "online_users": list(self.presence[channel])
        })

    def get_history(self, channel: str, limit: int = 10) -> List[RealtimeMessage]:
        """Get recent message history."""
        history = list(self.message_history[channel])
        return history[-limit:] if len(history) > limit else history

    def get_presence(self, channel: str) -> List[str]:
        """Get online users in channel."""
        return list(self.presence[channel])

class RealtimeSubscriber:
    """Subscriber with message buffering."""

    def __init__(self, subscriber_id: str, channel: str, pubsub: RealtimePubSub):
        self.subscriber_id = subscriber_id
        self.channel = channel
        self.pubsub = pubsub
        self.messages: deque = deque(maxlen=1000)

    def on_message(self, callback: Callable):
        """Register message handler."""
        def wrapper(msg: RealtimeMessage):
            self.messages.append(msg)
            callback(msg)

        self.pubsub.callbacks[self.subscriber_id] = wrapper
        return self

# Example 1: Live Dashboard with Real-time Updates
print("Example 1: Live Dashboard with Real-time Updates")
print("=" * 60)

pubsub = RealtimePubSub()

class Dashboard:
    """Real-time dashboard."""

    def __init__(self, name: str):
        self.name = name
        self.metrics = {}
        self.subscriber = pubsub.subscribe("metrics:live")

        def on_metric(msg: RealtimeMessage):
            if msg.event_type == "metric_update":
                metric_name = msg.data["metric"]
                value = msg.data["value"]
                self.metrics[metric_name] = value
                print(f"  [{self.name}] {metric_name}: {value}")

        self.subscriber.on_message(on_metric)

print("Setting up real-time dashboard:")
dashboard = Dashboard("Admin Dashboard")

print("\\nPublishing real-time metrics:")
pubsub.publish("metrics:live", "metric_update", {
    "metric": "active_users",
    "value": 1523
})

pubsub.publish("metrics:live", "metric_update", {
    "metric": "requests_per_sec",
    "value": 850
})

pubsub.publish("metrics:live", "metric_update", {
    "metric": "cpu_usage",
    "value": "45%"
})

print(f"\\nDashboard metrics: {dashboard.metrics}")
print()

# Example 2: Collaborative Editing (Google Docs-style)
print("Example 2: Collaborative Editing")
print("=" * 60)

pubsub2 = RealtimePubSub()

class CollaborativeEditor:
    """Real-time collaborative text editor."""

    def __init__(self, user_id: str, document_id: str):
        self.user_id = user_id
        self.document_id = document_id
        self.content = ""
        self.cursors = {}  # user_id -> cursor position

        channel = f"doc:{document_id}"
        self.subscriber = pubsub2.subscribe(channel, user_id)

        def on_change(msg: RealtimeMessage):
            if msg.event_type == "edit" and msg.sender != self.user_id:
                self._apply_edit(msg.data)
                print(f"  [{self.user_id}] Applied edit from {msg.sender}")

            elif msg.event_type == "cursor_move" and msg.sender != self.user_id:
                self.cursors[msg.sender] = msg.data["position"]
                print(f"  [{self.user_id}] {msg.sender} cursor at {msg.data['position']}")

            elif msg.event_type == "presence":
                if msg.data["action"] == "joined":
                    print(f"  [{self.user_id}] 👤 {msg.data['user_id']} joined")

        self.subscriber.on_message(on_change)

    def edit(self, operation: str, position: int, text: str):
        """Make edit and broadcast."""
        if operation == "insert":
            self.content = self.content[:position] + text + self.content[position:]
        elif operation == "delete":
            self.content = self.content[:position] + self.content[position + len(text):]

        pubsub2.publish(f"doc:{self.document_id}", "edit", {
            "operation": operation,
            "position": position,
            "text": text
        }, sender=self.user_id)

    def _apply_edit(self, edit_data: Dict):
        """Apply remote edit."""
        operation = edit_data["operation"]
        position = edit_data["position"]
        text = edit_data["text"]

        if operation == "insert":
            self.content = self.content[:position] + text + self.content[position:]
        elif operation == "delete":
            self.content = self.content[:position] + self.content[position + len(text):]

    def move_cursor(self, position: int):
        """Move cursor and broadcast."""
        pubsub2.publish(f"doc:{self.document_id}", "cursor_move", {
            "position": position
        }, sender=self.user_id)

print("Setting up collaborative editing session:")
alice_editor = CollaborativeEditor("Alice", "doc123")
bob_editor = CollaborativeEditor("Bob", "doc123")
charlie_editor = CollaborativeEditor("Charlie", "doc123")

print("\\nCollaborative editing:")
alice_editor.edit("insert", 0, "Hello ")
time.sleep(0.05)

bob_editor.edit("insert", 6, "World!")
time.sleep(0.05)

charlie_editor.move_cursor(11)
time.sleep(0.05)

print(f"\\nFinal content (Alice): '{alice_editor.content}'")
print(f"Final content (Bob): '{bob_editor.content}'")
print(f"Final content (Charlie): '{charlie_editor.content}'")
print()

# Example 3: Live Gaming Leaderboard
print("Example 3: Live Gaming Leaderboard")
print("=" * 60)

pubsub3 = RealtimePubSub()

class LiveLeaderboard:
    """Real-time game leaderboard."""

    def __init__(self):
        self.scores = {}
        self.subscriber = pubsub3.subscribe("game:leaderboard")

        def on_score_update(msg: RealtimeMessage):
            if msg.event_type == "score_update":
                player = msg.data["player"]
                score = msg.data["score"]
                self.scores[player] = score
                self._display()

        self.subscriber.on_message(on_score_update)

    def _display(self):
        """Display top 3."""
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        print(f"  Leaderboard: {', '.join(f'{p}:{s}' for p, s in sorted_scores[:3])}")

print("Setting up live leaderboard:")
leaderboard = LiveLeaderboard()

print("\\nGame events (score updates):")
pubsub3.publish("game:leaderboard", "score_update", {"player": "Alice", "score": 100})
time.sleep(0.05)

pubsub3.publish("game:leaderboard", "score_update", {"player": "Bob", "score": 150})
time.sleep(0.05)

pubsub3.publish("game:leaderboard", "score_update", {"player": "Charlie", "score": 120})
time.sleep(0.05)

pubsub3.publish("game:leaderboard", "score_update", {"player": "Alice", "score": 180})
time.sleep(0.05)

print()

# Example 4: Real-time Stock Ticker
print("Example 4: Real-time Stock Ticker")
print("=" * 60)

pubsub4 = RealtimePubSub()

class StockTicker:
    """Real-time stock price tracker."""

    def __init__(self, symbols: List[str]):
        self.prices = {}
        self.alerts = []

        # Subscribe to all stock updates
        self.subscriber = pubsub4.subscribe("stocks:updates")

        def on_price_update(msg: RealtimeMessage):
            if msg.event_type == "price":
                symbol = msg.data["symbol"]
                price = msg.data["price"]
                change = msg.data.get("change", 0)

                if symbol in symbols:
                    self.prices[symbol] = price
                    indicator = "📈" if change > 0 else "📉" if change < 0 else "➡️"
                    print(f"  {indicator} {symbol}: ${price:.2f} ({change:+.2f}%)")

        self.subscriber.on_message(on_price_update)

print("Setting up stock ticker for AAPL, GOOGL, MSFT:")
ticker = StockTicker(["AAPL", "GOOGL", "MSFT"])

print("\\nLive stock updates:")
stocks = [
    ("AAPL", 175.50, +2.3),
    ("GOOGL", 142.30, -1.2),
    ("MSFT", 380.75, +0.8),
    ("AAPL", 176.20, +2.7),
    ("TSLA", 245.00, +5.0),  # Not subscribed
]

for symbol, price, change in stocks:
    pubsub4.publish("stocks:updates", "price", {
        "symbol": symbol,
        "price": price,
        "change": change
    })
    time.sleep(0.1)

print()

# Example 5: Real-time Notification Center
print("Example 5: Real-time Notification Center")
print("=" * 60)

pubsub5 = RealtimePubSub()

class NotificationCenter:
    """Real-time notification aggregator."""

    def __init__(self, user_id: str):
        self.user_id = user_id
        self.notifications = []
        self.unread_count = 0

        # Subscribe to multiple notification types
        for channel in ["messages", "mentions", "alerts"]:
            subscriber = pubsub5.subscribe(f"user:{user_id}:{channel}")

            def make_handler(notification_type):
                def handler(msg: RealtimeMessage):
                    notification = {
                        "type": notification_type,
                        "message": msg.data.get("message"),
                        "timestamp": msg.timestamp
                    }
                    self.notifications.append(notification)
                    self.unread_count += 1
                    self._display_notification(notification)
                return handler

            subscriber.on_message(make_handler(channel))

    def _display_notification(self, notification: Dict):
        """Display notification."""
        icons = {"messages": "💬", "mentions": "@", "alerts": "🔔"}
        icon = icons.get(notification["type"], "📬")
        print(f"  [{self.user_id}] {icon} {notification['message']}")

    def mark_read(self):
        """Mark all as read."""
        self.unread_count = 0

print("Setting up notification center for Alice:")
alice_notif = NotificationCenter("Alice")

print("\\nSending various notifications:")
pubsub5.publish("user:Alice:messages", "message", {
    "message": "New message from Bob"
})
time.sleep(0.05)

pubsub5.publish("user:Alice:mentions", "mention", {
    "message": "Charlie mentioned you in a comment"
})
time.sleep(0.05)

pubsub5.publish("user:Alice:alerts", "alert", {
    "message": "Your report is ready"
})
time.sleep(0.05)

print(f"\\nUnread notifications: {alice_notif.unread_count}")
print()

# Example 6: Message History and Replay
print("Example 6: Message History and Replay")
print("=" * 60)

pubsub6 = RealtimePubSub()

# Publish some messages
print("Publishing chat messages:")
for i in range(5):
    pubsub6.publish("chat:room1", "message", {
        "user": f"User{i}",
        "text": f"Message {i}"
    })

# New user joins and gets history
print("\\nNew user joins and receives history:")
history = pubsub6.get_history("chat:room1", limit=3)

print(f"Recent messages ({len(history)}):")
for msg in history:
    print(f"  [{msg.data['user']}] {msg.data['text']}")

print()

print("=" * 60)
print("REAL-TIME PUB/SUB PATTERNS")
print("=" * 60)
print("""
COMMON REAL-TIME PATTERNS:

1. LIVE DASHBOARDS:
   - Metrics updates
   - System monitoring
   - Business intelligence
   - Server status

2. COLLABORATIVE EDITING:
   - Google Docs-style
   - Operational Transform (OT)
   - Conflict-free Replicated Data Types (CRDTs)
   - Cursor tracking

3. CHAT & MESSAGING:
   - Direct messages
   - Group chats
   - Typing indicators
   - Read receipts

4. GAMING:
   - Player positions
   - Game state sync
   - Leaderboards
   - Match updates

5. FINANCIAL TICKERS:
   - Stock prices
   - Crypto rates
   - Sports scores
   - Auction bids

6. NOTIFICATIONS:
   - Push notifications
   - Activity feeds
   - Alert systems
   - Status updates

DESIGN PATTERNS:

Presence Tracking:
  - Track online users
  - Heartbeat mechanism
  - Join/leave events
  - Timeout detection

Message History:
  - Buffer recent messages
  - New subscribers get context
  - Implement as circular buffer
  - Set retention limit

Event Sourcing:
  - Store all events
  - Replay to reconstruct state
  - Audit trail
  - Time travel debugging

Fan-out on Write:
  - Precompute updates
  - Push to all subscribers
  - Low read latency
  - Higher write cost

PERFORMANCE OPTIMIZATION:

Message Batching:
  - Group updates together
  - Reduce network overhead
  - Throttle high-frequency updates
  - Debounce rapid changes

Connection Pooling:
  - Reuse connections
  - Reduce overhead
  - Connection limits
  - Load balancing

Compression:
  - Compress large payloads
  - Trade CPU for bandwidth
  - Use for historical data
  - Skip for small messages

RELIABILITY PATTERNS:

Heartbeats:
  - Periodic ping/pong
  - Detect disconnections
  - Automatic reconnect
  - Exponential backoff

Message Acknowledgments:
  - Application-level ACKs
  - Retry on timeout
  - Duplicate detection
  - Ordering guarantees

Circuit Breaker:
  - Detect failures
  - Fallback to polling
  - Prevent cascade
  - Auto-recovery

SCALING STRATEGIES:

Horizontal Scaling:
  - Multiple Redis instances
  - Shard by channel
  - Consistent hashing
  - Client-side routing

Vertical Scaling:
  - More memory/CPU
  - Faster network
  - Redis Cluster
  - Read replicas

Edge Caching:
  - CDN for static data
  - Regional Redis
  - Geo-distribution
  - Lower latency

MONITORING:

Metrics:
  - Messages per second
  - Subscriber count
  - Connection count
  - Message size
  - Latency (p50, p99)

Alerts:
  - Slow subscribers
  - Memory pressure
  - Connection limits
  - Pattern complexity

Production note: Real Redis Pub/Sub provides:
  - Sub-millisecond latency
  - Millions of messages/sec
  - Thousands of channels
  - Pattern subscriptions
  - Cluster-wide propagation
  - Client-side buffering
  - Automatic reconnection
  - Load balancing support
""")
'''

    # Lesson 853: Redis Caching Strategies
    lesson_853 = next(l for l in lessons if l['id'] == 853)
    lesson_853['fullSolution'] = '''# Redis Caching Strategies - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis caching patterns and strategies for performance optimization

import time
import hashlib
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass
from functools import wraps
from enum import Enum

class EvictionPolicy(Enum):
    """Cache eviction policies."""
    LRU = "lru"           # Least Recently Used
    LFU = "lfu"           # Least Frequently Used
    TTL = "ttl"           # Time To Live
    FIFO = "fifo"         # First In First Out

@dataclass
class CacheEntry:
    """Cache entry with metadata."""
    key: str
    value: Any
    created_at: float
    accessed_at: float
    access_count: int = 0
    ttl: Optional[int] = None

    def is_expired(self) -> bool:
        """Check if entry has expired."""
        if self.ttl is None:
            return False
        return (time.time() - self.created_at) > self.ttl

    def touch(self):
        """Update access metadata."""
        self.accessed_at = time.time()
        self.access_count += 1

class RedisCache:
    """
    Redis cache simulation with multiple strategies.

    Caching patterns:
    - Cache-aside (lazy loading)
    - Write-through
    - Write-behind
    - Read-through
    """

    def __init__(self, max_size: int = 100, eviction: EvictionPolicy = EvictionPolicy.LRU):
        self.data: Dict[str, CacheEntry] = {}
        self.max_size = max_size
        self.eviction = eviction
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        # Check if key exists and not expired
        if key in self.data:
            entry = self.data[key]

            if entry.is_expired():
                del self.data[key]
                self.misses += 1
                return None

            entry.touch()
            self.hits += 1
            return entry.value

        self.misses += 1
        return None

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Set value in cache."""
        # Check if we need to evict
        if len(self.data) >= self.max_size and key not in self.data:
            self._evict()

        entry = CacheEntry(
            key=key,
            value=value,
            created_at=time.time(),
            accessed_at=time.time(),
            ttl=ttl
        )

        self.data[key] = entry

    def delete(self, key: str) -> bool:
        """Delete key from cache."""
        if key in self.data:
            del self.data[key]
            return True
        return False

    def _evict(self):
        """Evict entry based on policy."""
        if not self.data:
            return

        if self.eviction == EvictionPolicy.LRU:
            # Evict least recently used
            victim = min(self.data.values(), key=lambda e: e.accessed_at)
        elif self.eviction == EvictionPolicy.LFU:
            # Evict least frequently used
            victim = min(self.data.values(), key=lambda e: e.access_count)
        elif self.eviction == EvictionPolicy.FIFO:
            # Evict oldest
            victim = min(self.data.values(), key=lambda e: e.created_at)
        else:
            victim = next(iter(self.data.values()))

        del self.data[victim.key]
        print(f"  [EVICT] Removed {victim.key} (policy: {self.eviction.value})")

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        return {
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": f"{hit_rate:.1f}%",
            "size": len(self.data),
            "max_size": self.max_size
        }

def cache_aside(cache: RedisCache, database: Dict[str, Any]):
    """
    Cache-Aside pattern (Lazy Loading).

    Pattern:
    1. Check cache
    2. If miss, load from database
    3. Store in cache
    4. Return value
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(key: str):
            # Try cache first
            value = cache.get(key)

            if value is not None:
                print(f"  [CACHE HIT] {key}")
                return value

            # Cache miss - load from database
            print(f"  [CACHE MISS] {key} - loading from database")
            value = database.get(key)

            if value is not None:
                # Store in cache
                cache.set(key, value)
                print(f"  [CACHE SET] {key}")

            return value

        return wrapper
    return decorator

class WriteThrough:
    """
    Write-Through cache.

    Pattern:
    1. Write to cache
    2. Write to database (synchronous)
    3. Return
    """

    def __init__(self, cache: RedisCache, database: Dict[str, Any]):
        self.cache = cache
        self.database = database

    def write(self, key: str, value: Any):
        """Write to cache and database."""
        print(f"  [WRITE-THROUGH] Writing {key}")

        # Write to cache
        self.cache.set(key, value)

        # Write to database (synchronous)
        self.database[key] = value

        print(f"  [WRITE-THROUGH] Completed")

    def read(self, key: str) -> Optional[Any]:
        """Read from cache, fallback to database."""
        value = self.cache.get(key)

        if value is None:
            value = self.database.get(key)
            if value is not None:
                self.cache.set(key, value)

        return value

class WriteBehind:
    """
    Write-Behind (Write-Back) cache.

    Pattern:
    1. Write to cache immediately
    2. Queue write to database
    3. Flush asynchronously
    """

    def __init__(self, cache: RedisCache, database: Dict[str, Any]):
        self.cache = cache
        self.database = database
        self.write_queue: List[Tuple[str, Any]] = []

    def write(self, key: str, value: Any):
        """Write to cache, queue database write."""
        print(f"  [WRITE-BEHIND] Writing {key} to cache")

        # Immediate cache write
        self.cache.set(key, value)

        # Queue for database
        self.write_queue.append((key, value))

        print(f"  [WRITE-BEHIND] Queued for database ({len(self.write_queue)} pending)")

    def flush(self):
        """Flush pending writes to database."""
        print(f"  [FLUSH] Writing {len(self.write_queue)} entries to database")

        for key, value in self.write_queue:
            self.database[key] = value

        self.write_queue.clear()
        print(f"  [FLUSH] Complete")

# Example 1: Cache-Aside Pattern (Lazy Loading)
print("Example 1: Cache-Aside Pattern (Lazy Loading)")
print("=" * 60)

# Setup
cache1 = RedisCache(max_size=3)
database1 = {
    "user:1": {"name": "Alice", "email": "alice@example.com"},
    "user:2": {"name": "Bob", "email": "bob@example.com"},
    "user:3": {"name": "Charlie", "email": "charlie@example.com"},
}

@cache_aside(cache1, database1)
def get_user(user_id: str):
    """Get user data."""
    pass

print("First access (cache miss, loads from DB):")
user = get_user("user:1")
print(f"Result: {user}")
print()

print("Second access (cache hit):")
user = get_user("user:1")
print(f"Result: {user}")
print()

print("Access another user:")
user = get_user("user:2")
print()

print("Cache stats:", cache1.get_stats())
print()

# Example 2: Write-Through Pattern
print("Example 2: Write-Through Pattern")
print("=" * 60)

cache2 = RedisCache(max_size=10)
database2 = {}

write_through = WriteThrough(cache2, database2)

print("Writing data (cache + database synchronously):")
write_through.write("product:100", {"name": "Laptop", "price": 999})
print()

print("Reading data (from cache):")
product = write_through.read("product:100")
print(f"Result: {product}")
print()

print(f"Database contains: {database2}")
print()

# Example 3: Write-Behind Pattern
print("Example 3: Write-Behind Pattern")
print("=" * 60)

cache3 = RedisCache(max_size=10)
database3 = {}

write_behind = WriteBehind(cache3, database3)

print("Writing multiple values (cache only, database queued):")
write_behind.write("order:1", {"item": "Widget", "qty": 5})
write_behind.write("order:2", {"item": "Gadget", "qty": 3})
write_behind.write("order:3", {"item": "Doodad", "qty": 7})
print()

print(f"Database before flush: {database3}")
print()

print("Flushing writes to database:")
write_behind.flush()
print()

print(f"Database after flush: {database3}")
print()

# Example 4: TTL (Time-To-Live) Expiration
print("Example 4: TTL (Time-To-Live) Expiration")
print("=" * 60)

cache4 = RedisCache()

print("Setting values with TTL:")
cache4.set("session:abc", {"user_id": 123}, ttl=2)  # 2 second TTL
cache4.set("temp:xyz", "temporary data", ttl=1)     # 1 second TTL

print("Immediate read:")
print(f"  session:abc = {cache4.get('session:abc')}")
print(f"  temp:xyz = {cache4.get('temp:xyz')}")
print()

print("Waiting 1.5 seconds...")
time.sleep(1.5)

print("After 1.5 seconds:")
print(f"  session:abc = {cache4.get('session:abc')} (still valid)")
print(f"  temp:xyz = {cache4.get('temp:xyz')} (expired)")
print()

# Example 5: Cache Eviction Policies
print("Example 5: Cache Eviction Policies")
print("=" * 60)

# LRU (Least Recently Used)
print("LRU Policy:")
cache_lru = RedisCache(max_size=3, eviction=EvictionPolicy.LRU)

cache_lru.set("key1", "value1")
cache_lru.set("key2", "value2")
cache_lru.set("key3", "value3")

# Access key1 and key2 (key3 is least recently used)
cache_lru.get("key1")
cache_lru.get("key2")

# This will evict key3 (LRU)
print("  Adding key4 (will evict least recently used):")
cache_lru.set("key4", "value4")
print(f"  Cache keys: {list(cache_lru.data.keys())}")
print()

# LFU (Least Frequently Used)
print("LFU Policy:")
cache_lfu = RedisCache(max_size=3, eviction=EvictionPolicy.LFU)

cache_lfu.set("key1", "value1")
cache_lfu.set("key2", "value2")
cache_lfu.set("key3", "value3")

# Access key1 multiple times
cache_lfu.get("key1")
cache_lfu.get("key1")
cache_lfu.get("key1")

# Access key2 twice
cache_lfu.get("key2")
cache_lfu.get("key2")

# key3 has lowest frequency
print("  Adding key4 (will evict least frequently used):")
cache_lfu.set("key4", "value4")
print(f"  Cache keys: {list(cache_lfu.data.keys())}")
print()

# Example 6: Cache Stampede Prevention
print("Example 6: Cache Stampede Prevention")
print("=" * 60)

cache6 = RedisCache()
database6 = {"expensive_query": "computed result"}
computing_lock = {}

def get_with_lock(key: str) -> Any:
    """Get value with stampede protection."""
    # Try cache
    value = cache6.get(key)
    if value is not None:
        print(f"  [HIT] {key}")
        return value

    # Check if already computing
    if key in computing_lock:
        print(f"  [WAIT] {key} being computed by another request")
        # In production, wait for lock to release
        return None

    # Set lock
    computing_lock[key] = True
    print(f"  [LOCK] Acquired lock for {key}")

    try:
        # Expensive computation
        print(f"  [COMPUTE] Loading {key} from database...")
        time.sleep(0.5)  # Simulate slow query
        value = database6.get(key)

        # Store in cache
        cache6.set(key, value, ttl=60)
        print(f"  [SET] Cached {key}")

        return value
    finally:
        # Release lock
        del computing_lock[key]
        print(f"  [UNLOCK] Released lock for {key}")

print("Simulating cache stampede scenario:")
result = get_with_lock("expensive_query")
print(f"Result: {result}")
print()

print("Second request (from cache):")
result = get_with_lock("expensive_query")
print(f"Result: {result}")
print()

# Example 7: Multi-Layer Caching
print("Example 7: Multi-Layer Caching (L1 + L2)")
print("=" * 60)

class MultiLayerCache:
    """Multi-layer cache (L1: in-memory, L2: Redis)."""

    def __init__(self):
        self.l1_cache = {}  # Small, fast (in-process memory)
        self.l2_cache = RedisCache(max_size=100)  # Larger (Redis)
        self.database = {}

    def get(self, key: str) -> Optional[Any]:
        """Get from L1, then L2, then database."""
        # Try L1 (fastest)
        if key in self.l1_cache:
            print(f"  [L1 HIT] {key}")
            return self.l1_cache[key]

        # Try L2 (Redis)
        value = self.l2_cache.get(key)
        if value is not None:
            print(f"  [L2 HIT] {key}")
            # Promote to L1
            self.l1_cache[key] = value
            return value

        # Load from database
        print(f"  [L1 MISS, L2 MISS] Loading from database")
        value = self.database.get(key)

        if value is not None:
            # Store in both layers
            self.l1_cache[key] = value
            self.l2_cache.set(key, value)

        return value

    def set(self, key: str, value: Any):
        """Set in all layers."""
        self.l1_cache[key] = value
        self.l2_cache.set(key, value)
        self.database[key] = value

multi_cache = MultiLayerCache()

print("Setting value:")
multi_cache.set("data:1", {"value": 42})
print()

# Clear L1 to simulate different server
multi_cache.l1_cache.clear()

print("Getting value (L1 cleared):")
value = multi_cache.get("data:1")
print(f"Result: {value}")
print()

print("Getting value again (now in L1):")
value = multi_cache.get("data:1")
print(f"Result: {value}")
print()

print("=" * 60)
print("CACHING STRATEGIES BEST PRACTICES")
print("=" * 60)
print("""
CACHING PATTERNS:

1. CACHE-ASIDE (Lazy Loading):
   ✓ Simple implementation
   ✓ Only cache what's used
   ✓ Cache failure doesn't break app
   ✗ Cache miss penalty
   ✗ Stale data possible

2. WRITE-THROUGH:
   ✓ Cache always in sync
   ✓ No stale data
   ✗ Write latency
   ✗ Wasted writes

3. WRITE-BEHIND:
   ✓ Fast writes
   ✓ Batch database updates
   ✗ Data loss risk
   ✗ Complexity

4. READ-THROUGH:
   ✓ Transparent caching
   ✓ Simplified application code
   ✗ Cache handles loading
   ✗ Initial load penalty

EVICTION POLICIES:

LRU (Least Recently Used):
  - Evict oldest access
  - Good for time-based access
  - Redis: maxmemory-policy allkeys-lru

LFU (Least Frequently Used):
  - Evict lowest frequency
  - Good for popularity-based
  - Redis: maxmemory-policy allkeys-lfu

TTL (Time To Live):
  - Auto-expire entries
  - Good for session data
  - Redis: EXPIRE command

FIFO (First In First Out):
  - Evict oldest entry
  - Simple implementation
  - Rarely optimal

TTL STRATEGIES:

Session Data: 15-30 minutes
API Responses: 5-60 seconds
Static Content: 1-24 hours
User Profiles: 5-15 minutes
Configuration: 1-60 minutes

CACHE KEY DESIGN:

Good patterns:
  user:{id}:profile
  product:{id}:details
  api:{endpoint}:{params_hash}

Bad patterns:
  userprofile123 (no namespace)
  data (too generic)
  {json_params} (unpredictable)

CACHE INVALIDATION:

Time-based:
  SET key value EX 300

Event-based:
  DEL user:123:profile

Tag-based:
  SET tags:user:123 "profile,orders,cart"

Pattern-based:
  DEL user:123:*

CACHE STAMPEDE PREVENTION:

Problem: Multiple requests compute same value

Solutions:
1. Locking:
   - SETNX lock:key 1 EX 10
   - Compute if lock acquired
   - Others wait or serve stale

2. Probabilistic Early Expiration:
   - Refresh before TTL expires
   - Random jitter
   - Spread load

3. Always serve stale:
   - Return expired value
   - Refresh in background

MONITORING:

Key metrics:
  - Hit rate (target: > 80%)
  - Miss rate
  - Eviction rate
  - Memory usage
  - Latency (p50, p99)

Alerts:
  - Hit rate drops
  - Memory pressure
  - High eviction rate
  - Slow queries

OPTIMIZATION:

Compression:
  - Large values (> 1KB)
  - JSON, HTML, text
  - Trade CPU for memory

Serialization:
  - JSON: human-readable
  - MessagePack: compact
  - Pickle: Python-specific

Connection Pooling:
  - Reuse connections
  - Set pool size
  - Monitor connections

Production note: Real Redis caching provides:
  - Multiple eviction policies
  - TTL per key
  - Atomic operations
  - Transactions (MULTI/EXEC)
  - Pub/Sub for invalidation
  - Cluster support
  - Persistence options
  - Memory optimization
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 15 COMPLETE: Redis Pub/Sub and Caching Strategies")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 852: Redis Pub/Sub Messaging")
    print(f"  - Lesson 1003: Redis Pub/Sub Real-time Messaging")
    print(f"  - Lesson 853: Redis Caching Strategies")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
