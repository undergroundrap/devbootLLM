"""
Improve tutorials to college-level quality standards.
Batch 1: 10 sample lessons
"""
import json
import re

# Tutorial improvements with actual technical content and code examples
IMPROVEMENTS = {
    714: {  # Netflix CDN
        "tutorial": """<div style="background: rgba(107, 114, 128, 0.1); border-left: 4px solid #6b7280; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">📋 Overview</h4>
  <p class="mb-4 text-gray-300">Design a Content Delivery Network (CDN) architecture similar to Netflix's Open Connect CDN. A CDN reduces latency and bandwidth costs by caching content at edge locations close to users, rather than serving everything from a central origin server.</p>
</div>

<div style="background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🏗️ CDN Architecture Components</h4>
  <p class="mb-4 text-gray-300">A production CDN system consists of:</p>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-blue-400">Origin Server:</strong> Stores master copies of content</li>
    <li><strong class="text-blue-400">Edge Servers:</strong> Distributed cache servers near users (POPs - Points of Presence)</li>
    <li><strong class="text-blue-400">Cache Layer:</strong> In-memory cache (Redis/Memcached) for hot content</li>
    <li><strong class="text-blue-400">Routing Logic:</strong> Directs users to nearest edge server</li>
    <li><strong class="text-blue-400">Cache Invalidation:</strong> Updates or removes stale content</li>
  </ul>
</div>

<div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">💡 Example: Edge Server with Cache</h4>
  <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>class EdgeServer:
    def __init__(self, location):
        self.location = location
        self.cache = {}  # In-memory cache
        self.cache_hits = 0
        self.cache_misses = 0

    def get_content(self, content_id, origin):
        # Check cache first (fast)
        if content_id in self.cache:
            self.cache_hits += 1
            return self.cache[content_id]

        # Cache miss - fetch from origin (slow)
        self.cache_misses += 1
        content = origin.fetch(content_id)
        self.cache[content_id] = content
        return content

    def invalidate(self, content_id):
        if content_id in self.cache:
            del self.cache[content_id]</code></pre>
  <p class="mt-4 text-gray-300">Edge servers maintain a local cache. On cache hit, content is served immediately (~5-10ms). On cache miss, content is fetched from origin (~100-200ms) and cached for future requests.</p>
</div>

<div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🔄 Cache Invalidation Strategies</h4>
  <p class="mb-4 text-gray-300">When content updates, caches must be invalidated. Three common strategies:</p>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-purple-400">TTL (Time To Live):</strong> Content expires after fixed duration (e.g., 24 hours)</li>
    <li><strong class="text-purple-400">Purge API:</strong> Manually invalidate specific content via API call</li>
    <li><strong class="text-purple-400">Versioned URLs:</strong> Each version gets unique URL (e.g., /video-v2.mp4)</li>
  </ul>
  <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code># TTL-based caching
import time

class CacheEntry:
    def __init__(self, data, ttl=3600):
        self.data = data
        self.expiry = time.time() + ttl

    def is_valid(self):
        return time.time() < self.expiry</code></pre>
</div>

<div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">📊 Performance Metrics</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-amber-400">Cache Hit Ratio:</strong> Percentage of requests served from cache (target: >90%)</li>
    <li><strong class="text-amber-400">P50/P95/P99 Latency:</strong> Response time percentiles (target: P95 < 50ms)</li>
    <li><strong class="text-amber-400">Bandwidth Savings:</strong> Reduced origin traffic (can save 70-90% bandwidth costs)</li>
    <li><strong class="text-amber-400">Edge Server Load:</strong> Request distribution across edge nodes</li>
  </ul>
</div>

<div style="background: rgba(20, 83, 45, 0.2); border-left: 4px solid #22c55e; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">✅ Production Best Practices</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Use geographical routing to direct users to nearest edge server (DNS-based or Anycast)</li>
    <li>Implement cache warming for popular content before traffic spikes</li>
    <li>Monitor cache hit ratios and adjust TTL/cache size accordingly</li>
    <li>Use compression (gzip/brotli) to reduce bandwidth by 60-80%</li>
    <li>Implement rate limiting and DDoS protection at edge</li>
    <li>Handle cache stampede with request coalescing</li>
  </ul>
</div>

<div style="background: rgba(30, 58, 138, 0.2); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🎓 Real-World Application</h4>
  <p class="mb-4 text-gray-300">Netflix's Open Connect CDN serves over 200 million subscribers globally. They place edge servers (Open Connect Appliances) in ISP data centers to serve content as close to users as possible. During peak hours, over 90% of content is served from cache, dramatically reducing their origin server load and bandwidth costs.</p>
  <p class="mb-4 text-gray-300">Similar systems: Cloudflare CDN, AWS CloudFront, Akamai, Fastly</p>
</div>""",
        "fullSolution": """# Netflix CDN Architecture Simulation
import time
import random

class OriginServer:
    \"\"\"Master content server (single location)\"\"\"
    def __init__(self):
        self.content_store = {
            'video_1': 'Netflix Original Series - Episode 1',
            'video_2': 'Action Movie 2024',
            'video_3': 'Documentary Special'
        }
        self.fetch_count = 0

    def fetch(self, content_id):
        \"\"\"Simulate origin fetch (slow, ~200ms)\"\"\"
        self.fetch_count += 1
        time.sleep(0.01)  # Simulate network latency
        return self.content_store.get(content_id, 'Content not found')

class EdgeServer:
    \"\"\"CDN edge server with caching\"\"\"
    def __init__(self, location):
        self.location = location
        self.cache = {}
        self.cache_hits = 0
        self.cache_misses = 0

    def get_content(self, content_id, origin):
        \"\"\"Get content from cache or origin\"\"\"
        if content_id in self.cache:
            self.cache_hits += 1
            print(f"  [{self.location}] Cache HIT for {content_id}")
            return self.cache[content_id]

        # Cache miss - fetch from origin
        self.cache_misses += 1
        print(f"  [{self.location}] Cache MISS for {content_id} - fetching from origin...")
        content = origin.fetch(content_id)
        self.cache[content_id] = content
        return content

    def get_stats(self):
        total = self.cache_hits + self.cache_misses
        hit_ratio = (self.cache_hits / total * 100) if total > 0 else 0
        return f"Hits: {self.cache_hits}, Misses: {self.cache_misses}, Hit Ratio: {hit_ratio:.1f}%"

# Initialize CDN
origin = OriginServer()
edge_us = EdgeServer("US-East")
edge_eu = EdgeServer("EU-West")

# Simulate user requests
print("=== Simulating CDN Requests ===\\n")

# User 1 (US) - First request
print("User 1 (US): Requesting video_1")
content = edge_us.get_content('video_1', origin)
print(f"  Delivered: {content[:30]}...\\n")

# User 2 (US) - Cache hit
print("User 2 (US): Requesting video_1")
content = edge_us.get_content('video_1', origin)
print(f"  Delivered: {content[:30]}...\\n")

# User 3 (EU) - Cache miss (different edge)
print("User 3 (EU): Requesting video_1")
content = edge_eu.get_content('video_1', origin)
print(f"  Delivered: {content[:30]}...\\n")

# User 4 (EU) - Cache hit
print("User 4 (EU): Requesting video_1")
content = edge_eu.get_content('video_1', origin)
print(f"  Delivered: {content[:30]}...\\n")

# Performance stats
print("=== CDN Performance Stats ===")
print(f"Origin fetches: {origin.fetch_count}")
print(f"US Edge: {edge_us.get_stats()}")
print(f"EU Edge: {edge_eu.get_stats()}")
print(f"\\nBandwidth savings: Served 4 requests with only {origin.fetch_count} origin fetches!")
"""
    },

    715: {  # WhatsApp Chat
        "tutorial": """<div style="background: rgba(107, 114, 128, 0.1); border-left: 4px solid #6b7280; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">📋 Overview</h4>
  <p class="mb-4 text-gray-300">Design a real-time chat messaging system like WhatsApp with user-to-user messaging, group chats, message delivery tracking, and online status indicators. Focus on scalability, low latency, and reliability for billions of messages per day.</p>
</div>

<div style="background: rgba(59, 130, 246, 0.1); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🏗️ System Architecture</h4>
  <p class="mb-4 text-gray-300">Key components of a chat system:</p>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-blue-400">WebSocket Server:</strong> Persistent connections for real-time message delivery</li>
    <li><strong class="text-blue-400">Message Queue:</strong> Kafka/RabbitMQ for reliable message delivery</li>
    <li><strong class="text-blue-400">Database:</strong> Cassandra/MongoDB for message storage (billions of messages)</li>
    <li><strong class="text-blue-400">Presence Service:</strong> Redis for tracking online/offline status</li>
    <li><strong class="text-blue-400">Media Storage:</strong> S3/CDN for images/videos</li>
  </ul>
</div>

<div style="background: rgba(16, 185, 129, 0.1); border-left: 4px solid #10b981; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">💡 Example: Message Delivery System</h4>
  <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>class ChatServer:
    def __init__(self):
        self.connections = {}  # user_id -> websocket
        self.message_queue = []

    def send_message(self, from_user, to_user, message):
        msg = {
            'id': generate_id(),
            'from': from_user,
            'to': to_user,
            'text': message,
            'timestamp': time.time(),
            'status': 'sent'
        }

        # Store in database
        db.save_message(msg)

        # Try to deliver immediately if online
        if to_user in self.connections:
            self.connections[to_user].send(msg)
            msg['status'] = 'delivered'
        else:
            # Queue for later delivery
            self.message_queue.append(msg)

        return msg['id']</code></pre>
  <p class="mt-4 text-gray-300">Messages are persisted to database first, then delivered via WebSocket if the recipient is online. If offline, messages are queued for delivery when the user reconnects.</p>
</div>

<div style="background: rgba(139, 92, 246, 0.1); border-left: 4px solid #8b5cf6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">✓ Message Status Tracking</h4>
  <p class="mb-4 text-gray-300">WhatsApp-style delivery indicators:</p>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-purple-400">Single checkmark (✓):</strong> Sent to server</li>
    <li><strong class="text-purple-400">Double checkmark (✓✓):</strong> Delivered to recipient's device</li>
    <li><strong class="text-purple-400">Blue checkmarks:</strong> Read by recipient</li>
  </ul>
  <pre class="bg-gray-900 text-gray-100 p-4 rounded-lg overflow-x-auto"><code>class MessageStatus:
    SENT = 'sent'         # ✓ Received by server
    DELIVERED = 'delivered'  # ✓✓ Received by client
    READ = 'read'         # Blue ✓✓ Opened by user

    def mark_delivered(self, message_id, user_id):
        db.update(message_id, status='delivered')
        # Notify sender
        self.notify_sender(message_id, 'delivered')

    def mark_read(self, message_id, user_id):
        db.update(message_id, status='read',
                  read_at=time.time())
        self.notify_sender(message_id, 'read')</code></pre>
</div>

<div style="background: rgba(245, 158, 11, 0.1); border-left: 4px solid #f59e0b; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🔐 Security & Privacy</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li><strong class="text-amber-400">End-to-End Encryption:</strong> Messages encrypted on sender device, decrypted on recipient device (Signal Protocol)</li>
    <li><strong class="text-amber-400">TLS/SSL:</strong> Encrypt data in transit between client and server</li>
    <li><strong class="text-amber-400">Message Expiration:</strong> Delete messages after 30/90 days to save storage</li>
    <li><strong class="text-amber-400">Authentication:</strong> JWT tokens for API access, refresh tokens for long sessions</li>
  </ul>
</div>

<div style="background: rgba(20, 83, 45, 0.2); border-left: 4px solid #22c55e; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">✅ Scalability Considerations</h4>
  <ul class="list-disc list-inside mb-4 text-gray-300 space-y-2">
    <li>Use connection pooling and load balancing across multiple WebSocket servers</li>
    <li>Partition users across databases by user_id (consistent hashing)</li>
    <li>Cache recent messages in Redis for fast retrieval (last 100 messages)</li>
    <li>Use message queues (Kafka) to handle traffic spikes</li>
    <li>Compress media before uploading, store in CDN for fast delivery</li>
    <li>Implement back-pressure to prevent server overload</li>
  </ul>
</div>

<div style="background: rgba(30, 58, 138, 0.2); border-left: 4px solid #3b82f6; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
  <h4 class="font-semibold text-gray-200" style="margin-bottom: 0.75rem;">🎓 Real-World Scale</h4>
  <p class="mb-4 text-gray-300">WhatsApp handles over 100 billion messages per day with 2 billion active users. They use Erlang for their messaging servers (lightweight processes for each connection), FreeBSD for OS, and custom-built infrastructure. Average message latency is <200ms globally.</p>
</div>""",
        "fullSolution": """# WhatsApp-style Chat System Simulation
import time
from datetime import datetime

class Message:
    \"\"\"Represents a chat message\"\"\"
    def __init__(self, msg_id, sender, recipient, text):
        self.id = msg_id
        self.sender = sender
        self.recipient = recipient
        self.text = text
        self.timestamp = datetime.now().strftime("%H:%M")
        self.status = 'sent'  # sent -> delivered -> read

    def __repr__(self):
        status_icons = {
            'sent': '✓',
            'delivered': '✓✓',
            'read': '✓✓ (blue)'
        }
        return f"[{self.timestamp}] {self.sender} -> {self.recipient}: {self.text} {status_icons[self.status]}"

class ChatServer:
    \"\"\"Simplified chat server\"\"\"
    def __init__(self):
        self.users_online = set()
        self.messages = []
        self.undelivered_messages = {}

    def user_connect(self, user_id):
        \"\"\"User comes online\"\"\"
        self.users_online.add(user_id)
        print(f"✓ {user_id} is now online")

        # Deliver pending messages
        if user_id in self.undelivered_messages:
            pending = self.undelivered_messages[user_id]
            print(f"  Delivering {len(pending)} pending messages to {user_id}")
            for msg in pending:
                msg.status = 'delivered'
                print(f"  {msg}")
            del self.undelivered_messages[user_id]

    def user_disconnect(self, user_id):
        \"\"\"User goes offline\"\"\"
        self.users_online.discard(user_id)
        print(f"✗ {user_id} is now offline")

    def send_message(self, sender, recipient, text):
        \"\"\"Send message from sender to recipient\"\"\"
        msg_id = len(self.messages) + 1
        msg = Message(msg_id, sender, recipient, text)
        self.messages.append(msg)

        print(f"\\n{sender} sends: \\\"{text}\\\"")

        # Check if recipient is online
        if recipient in self.users_online:
            msg.status = 'delivered'
            print(f"  ✓✓ Delivered to {recipient} immediately")
        else:
            # Queue for later delivery
            if recipient not in self.undelivered_messages:
                self.undelivered_messages[recipient] = []
            self.undelivered_messages[recipient].append(msg)
            print(f"  ✓ Sent to server ({recipient} is offline)")

        return msg

    def mark_read(self, message_id):
        \"\"\"Mark message as read\"\"\"
        msg = self.messages[message_id - 1]
        msg.status = 'read'
        print(f"  ✓✓ Message {message_id} read by {msg.recipient}")

# Simulate chat system
print("=== WhatsApp-style Chat System ===\\n")

server = ChatServer()

# Alice comes online
server.user_connect("Alice")

# Bob is offline, Alice sends message
msg1 = server.send_message("Alice", "Bob", "Hey Bob! Are you there?")

# Alice sends another message
msg2 = server.send_message("Alice", "Bob", "Let me know when you're free")

# Bob comes online - receives pending messages
print()
server.user_connect("Bob")

# Bob reads the messages
print()
server.mark_read(msg1.id)
server.mark_read(msg2.id)

# Bob replies
print()
msg3 = server.send_message("Bob", "Alice", "Hi Alice! Just saw your messages")

# Alice reads Bob's reply
print()
server.mark_read(msg3.id)

# Show final message history
print("\\n=== Message History ===")
for msg in server.messages:
    print(msg)
"""
    }
}

def improve_lessons():
    """Apply improvements to lessons"""
    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        python_lessons = json.load(f)

    # Apply improvements
    improved_count = 0
    for lesson_id, improvements in IMPROVEMENTS.items():
        # Find lesson (0-indexed)
        lesson = python_lessons[lesson_id - 1]

        if lesson['id'] != lesson_id:
            print(f"ERROR: Lesson ID mismatch at index {lesson_id-1}")
            continue

        # Store old values for comparison
        old_tutorial_len = len(lesson['tutorial'])
        old_solution_len = len(lesson['fullSolution'])

        # Apply improvements
        if 'tutorial' in improvements:
            lesson['tutorial'] = improvements['tutorial']
        if 'fullSolution' in improvements:
            lesson['fullSolution'] = improvements['fullSolution']
        if 'expectedOutput' in improvements:
            lesson['expectedOutput'] = improvements['expectedOutput']

        improved_count += 1
        print(f"[OK] Improved Lesson {lesson_id}: {lesson['title']}")
        print(f"  Tutorial: {old_tutorial_len} -> {len(lesson['tutorial'])} chars")
        print(f"  Solution: {old_solution_len} -> {len(lesson['fullSolution'])} chars")

    # Save improved lessons
    with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(python_lessons, f, indent=2, ensure_ascii=False)

    print(f"\n[DONE] Successfully improved {improved_count} lessons")
    return improved_count

if __name__ == '__main__':
    improve_lessons()
