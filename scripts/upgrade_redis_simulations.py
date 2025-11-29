"""
Upgrade Redis framework lesson stubs to realistic simulations
"""
import json
import sys

def create_redis_basics_simulation():
    """Lesson 850: Redis - Redis Basics"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# This is a simulation for learning without installing redis-py

import time

class RedisSimulation:
    """Simulates Redis in-memory data store for learning purposes"""
    def __init__(self):
        # Real: TCP connection to Redis server
        # Simulation: in-memory Python dict
        self.data = {}
        self.expiry = {}

    def set(self, key, value, ex=None):
        """
        Set key to hold string value
        Args:
            key: The key name
            value: The value to store
            ex: Expiration time in seconds (optional)
        Real: Sends SET command to Redis server via RESP protocol
        Simulation: Stores in local dictionary
        """
        self.data[key] = str(value)
        if ex:
            self.expiry[key] = time.time() + ex
        return True

    def get(self, key):
        """Get value of key"""
        # Check if expired
        if key in self.expiry and time.time() > self.expiry[key]:
            del self.data[key]
            del self.expiry[key]
            return None
        return self.data.get(key)

    def incr(self, key):
        """Increment integer value of key by 1"""
        # Real: Atomic operation on Redis server
        # Simulation: Convert, increment, store
        current = self.data.get(key, '0')
        new_value = int(current) + 1
        self.data[key] = str(new_value)
        return new_value

    def delete(self, key):
        """Delete a key"""
        if key in self.data:
            del self.data[key]
            if key in self.expiry:
                del self.expiry[key]
            return 1
        return 0

    def exists(self, key):
        """Check if key exists"""
        return 1 if key in self.data else 0

# Usage demonstration
redis = RedisSimulation()

# String operations
redis.set('user:1000:name', 'Alice')
redis.set('user:1000:email', 'alice@example.com')
print(f"Name: {redis.get('user:1000:name')}")
print(f"Email: {redis.get('user:1000:email')}")

# Counter operations
redis.set('page:views', '0')
for _ in range(5):
    views = redis.incr('page:views')
print(f"Page views: {views}")

# Expiration (TTL)
redis.set('session:abc123', 'user_data', ex=2)
print(f"Session exists: {redis.exists('session:abc123')}")
time.sleep(2.1)
print(f"Session after expiry: {redis.get('session:abc123')}")

# Key management
redis.delete('user:1000:name')
print(f"Name after delete: {redis.get('user:1000:name')}")
'''

def create_redis_data_structures_simulation():
    """Lesson 851: Redis - Data Structures"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

import time

class RedisDataStructures:
    """Simulates Redis data structures: Hashes, Lists, Sets, Sorted Sets"""
    def __init__(self):
        self.hashes = {}  # Hash data structure
        self.lists = {}   # List data structure
        self.sets = {}    # Set data structure
        self.zsets = {}   # Sorted set data structure

    # Hash operations (like a dictionary within Redis)
    def hset(self, name, key, value):
        """Set field in hash"""
        # Real: Redis hash is optimized memory structure
        if name not in self.hashes:
            self.hashes[name] = {}
        self.hashes[name][key] = str(value)
        return 1

    def hget(self, name, key):
        """Get field from hash"""
        return self.hashes.get(name, {}).get(key)

    def hgetall(self, name):
        """Get all fields and values from hash"""
        return self.hashes.get(name, {})

    # List operations (ordered collection)
    def lpush(self, name, *values):
        """Push values to head of list"""
        if name not in self.lists:
            self.lists[name] = []
        for value in reversed(values):
            self.lists[name].insert(0, str(value))
        return len(self.lists[name])

    def rpush(self, name, *values):
        """Push values to tail of list"""
        if name not in self.lists:
            self.lists[name] = []
        for value in values:
            self.lists[name].append(str(value))
        return len(self.lists[name])

    def lrange(self, name, start, end):
        """Get range of elements from list"""
        lst = self.lists.get(name, [])
        if end == -1:
            return lst[start:]
        return lst[start:end+1]

    # Set operations (unique unordered collection)
    def sadd(self, name, *values):
        """Add members to set"""
        if name not in self.sets:
            self.sets[name] = set()
        before = len(self.sets[name])
        self.sets[name].update(str(v) for v in values)
        return len(self.sets[name]) - before

    def smembers(self, name):
        """Get all members of set"""
        return self.sets.get(name, set())

    # Sorted set operations (scored members)
    def zadd(self, name, mapping):
        """Add members with scores to sorted set"""
        if name not in self.zsets:
            self.zsets[name] = {}
        self.zsets[name].update(mapping)
        return len(mapping)

    def zrange(self, name, start, end, withscores=False):
        """Get range from sorted set by index"""
        if name not in self.zsets:
            return []
        sorted_items = sorted(self.zsets[name].items(), key=lambda x: x[1])
        if end == -1:
            items = sorted_items[start:]
        else:
            items = sorted_items[start:end+1]

        if withscores:
            return [(k, v) for k, v in items]
        return [k for k, v in items]

# Demonstration
redis = RedisDataStructures()

# Hash: Store user profile
redis.hset('user:2000', 'name', 'Bob')
redis.hset('user:2000', 'age', '25')
redis.hset('user:2000', 'city', 'NYC')
print(f"User profile: {redis.hgetall('user:2000')}")

# List: Activity log
redis.rpush('activity:log', 'login', 'view_page', 'logout')
print(f"Activity log: {redis.lrange('activity:log', 0, -1)}")

# Set: Tags
redis.sadd('article:tags', 'python', 'redis', 'database')
print(f"Tags: {redis.smembers('article:tags')}")

# Sorted Set: Leaderboard
redis.zadd('leaderboard', {'Alice': 100, 'Bob': 85, 'Carol': 92})
print(f"Top players: {redis.zrange('leaderboard', 0, -1, withscores=True)}")
'''

def create_redis_pubsub_simulation():
    """Lesson 852: Redis - Pub/Sub Messaging"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379)
# pubsub = r.pubsub()

class RedisPubSubSimulation:
    """Simulates Redis Pub/Sub for real-time messaging"""
    def __init__(self):
        # Real: Redis manages pub/sub channels in memory
        # Simulation: Track subscribers per channel
        self.channels = {}
        self.patterns = {}

    def subscribe(self, subscriber_id, *channels):
        """Subscribe to one or more channels"""
        for channel in channels:
            if channel not in self.channels:
                self.channels[channel] = []
            if subscriber_id not in self.channels[channel]:
                self.channels[channel].append(subscriber_id)
        return True

    def publish(self, channel, message):
        """
        Publish message to channel
        Real: Redis broadcasts to all subscribers via TCP connections
        Simulation: Returns subscriber count
        """
        subscribers = self.channels.get(channel, [])
        print(f"Publishing to '{channel}': {message}")
        print(f"  Delivered to {len(subscribers)} subscriber(s)")
        return len(subscribers)

    def unsubscribe(self, subscriber_id, *channels):
        """Unsubscribe from channels"""
        for channel in channels:
            if channel in self.channels and subscriber_id in self.channels[channel]:
                self.channels[channel].remove(subscriber_id)
        return True

    def psubscribe(self, subscriber_id, *patterns):
        """Subscribe to channel patterns"""
        # Real: Redis supports glob-style patterns like 'news.*'
        for pattern in patterns:
            if pattern not in self.patterns:
                self.patterns[pattern] = []
            if subscriber_id not in self.patterns[pattern]:
                self.patterns[pattern].append(subscriber_id)
        return True

    def get_subscribers(self, channel):
        """Get subscriber count for channel"""
        return len(self.channels.get(channel, []))

# Demonstration
pubsub = RedisPubSubSimulation()

# Subscribe users to channels
pubsub.subscribe('user:alice', 'news', 'updates')
pubsub.subscribe('user:bob', 'news')
pubsub.subscribe('user:carol', 'alerts')

print("=== Publishing Messages ===")
pubsub.publish('news', 'Breaking: New Python release!')
pubsub.publish('updates', 'System will be down at 2am')
pubsub.publish('alerts', 'Security warning')

print(f"\\nNews channel has {pubsub.get_subscribers('news')} subscribers")

# Pattern subscription
pubsub.psubscribe('user:david', 'news.*', 'alert.*')
print("\\nUser David subscribed to patterns: news.*, alert.*")
'''

def create_redis_caching_simulation():
    """Lesson 853: Redis - Caching Strategies"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

import time
import hashlib

class RedisCachingSimulation:
    """Simulates Redis caching with TTL and eviction"""
    def __init__(self, max_memory_mb=100):
        self.cache = {}
        self.expiry = {}
        self.access_time = {}  # For LRU
        self.max_memory = max_memory_mb * 1024 * 1024

    def set(self, key, value, ex=None):
        """
        Cache a value with optional expiration
        Real: Redis handles memory limits with eviction policies
        """
        self.cache[key] = str(value)
        self.access_time[key] = time.time()

        if ex:
            self.expiry[key] = time.time() + ex
        return True

    def get(self, key):
        """Get from cache, respecting TTL"""
        # Check expiration
        if key in self.expiry and time.time() > self.expiry[key]:
            self._evict(key)
            return None

        if key in self.cache:
            self.access_time[key] = time.time()  # Update for LRU
            return self.cache[key]
        return None

    def _evict(self, key):
        """Remove key from cache"""
        if key in self.cache:
            del self.cache[key]
        if key in self.expiry:
            del self.expiry[key]
        if key in self.access_time:
            del self.access_time[key]

    def setex(self, key, seconds, value):
        """Set with expiration time"""
        return self.set(key, value, ex=seconds)

    def ttl(self, key):
        """Get remaining TTL in seconds"""
        if key not in self.expiry:
            return -1
        remaining = self.expiry[key] - time.time()
        return int(remaining) if remaining > 0 else -2

# Simulated database for cache-aside pattern
DATABASE = {
    'user:1': {'name': 'Alice', 'email': 'alice@example.com'},
    'user:2': {'name': 'Bob', 'email': 'bob@example.com'},
}

def get_user_with_cache(user_id, cache):
    """Cache-Aside pattern implementation"""
    cache_key = f'user:{user_id}'

    # 1. Try cache first
    cached = cache.get(cache_key)
    if cached:
        print(f"Cache HIT for {cache_key}")
        return cached

    print(f"Cache MISS for {cache_key}")

    # 2. Fetch from database
    user_data = DATABASE.get(cache_key)
    if user_data:
        # 3. Store in cache with 60s TTL
        cache.set(cache_key, str(user_data), ex=60)
        return str(user_data)

    return None

# Demonstration
redis = RedisCachingSimulation()

print("=== Cache-Aside Pattern ===")
# First call: cache miss
result1 = get_user_with_cache('1', redis)
print(f"Result: {result1}\\n")

# Second call: cache hit
result2 = get_user_with_cache('1', redis)
print(f"Result: {result2}\\n")

print("=== TTL Management ===")
redis.setex('session:xyz', 5, 'session_data')
print(f"Session TTL: {redis.ttl('session:xyz')} seconds")
time.sleep(2)
print(f"Session TTL after 2s: {redis.ttl('session:xyz')} seconds")
'''

def create_redis_transactions_simulation():
    """Lesson 854: Redis - Redis Transactions"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# pipe = r.pipeline()

class RedisTransactionSimulation:
    """Simulates Redis MULTI/EXEC transactions"""
    def __init__(self):
        self.data = {}
        self.pipeline_commands = []
        self.in_transaction = False

    def set(self, key, value):
        """Set key-value pair"""
        if self.in_transaction:
            self.pipeline_commands.append(('set', key, value))
            return 'QUEUED'
        else:
            self.data[key] = str(value)
            return True

    def get(self, key):
        """Get value by key"""
        if self.in_transaction:
            self.pipeline_commands.append(('get', key))
            return 'QUEUED'
        return self.data.get(key)

    def incr(self, key):
        """Increment key"""
        if self.in_transaction:
            self.pipeline_commands.append(('incr', key))
            return 'QUEUED'
        current = int(self.data.get(key, '0'))
        self.data[key] = str(current + 1)
        return current + 1

    def multi(self):
        """
        Start transaction
        Real: Redis queues all commands until EXEC
        """
        self.in_transaction = True
        self.pipeline_commands = []
        print("Transaction started (MULTI)")
        return True

    def exec(self):
        """
        Execute all queued commands atomically
        Real: Redis executes all commands in a transaction atomically
        Simulation: Execute commands sequentially
        """
        if not self.in_transaction:
            raise Exception("No transaction in progress")

        print(f"Executing {len(self.pipeline_commands)} queued commands...")
        results = []

        # Execute all commands
        for cmd in self.pipeline_commands:
            operation = cmd[0]

            if operation == 'set':
                self.data[cmd[1]] = str(cmd[2])
                results.append(True)
            elif operation == 'get':
                results.append(self.data.get(cmd[1]))
            elif operation == 'incr':
                current = int(self.data.get(cmd[1], '0'))
                self.data[cmd[1]] = str(current + 1)
                results.append(current + 1)

        self.in_transaction = False
        self.pipeline_commands = []
        print("Transaction executed (EXEC)")
        return results

    def discard(self):
        """Discard transaction"""
        self.in_transaction = False
        self.pipeline_commands = []
        print("Transaction discarded (DISCARD)")
        return True

# Demonstration
redis = RedisTransactionSimulation()

print("=== Single Operations ===")
redis.set('balance:alice', '100')
redis.set('balance:bob', '50')
print(f"Alice balance: {redis.get('balance:alice')}")
print(f"Bob balance: {redis.get('balance:bob')}")

print("\\n=== Transfer Money with Transaction ===")
# Real: All commands execute atomically or not at all
redis.multi()
print(redis.set('balance:alice', '80'))  # Alice sends 20
print(redis.set('balance:bob', '70'))    # Bob receives 20
results = redis.exec()
print(f"Transaction results: {results}")

print(f"\\nAfter transaction:")
print(f"Alice balance: {redis.get('balance:alice')}")
print(f"Bob balance: {redis.get('balance:bob')}")

print("\\n=== Counter with Transaction ===")
redis.set('page:views', '0')
redis.multi()
redis.incr('page:views')
redis.incr('page:views')
redis.incr('page:views')
results = redis.exec()
print(f"Increments: {results}")
print(f"Final count: {redis.get('page:views')}")
'''

def create_redis_persistence_simulation():
    """Lesson 855: Redis - Persistence"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379)
# Real Redis has RDB snapshots and AOF (Append-Only File)

import json
import time
from pathlib import Path

class RedisPersistenceSimulation:
    """
    Simulates Redis persistence mechanisms
    Real: Redis uses RDB (snapshots) and AOF (append-only file)
    """
    def __init__(self, data_dir='./redis_data'):
        self.data = {}
        self.data_dir = Path(data_dir)
        self.aof_log = []  # Append-only file log
        self.last_save_time = time.time()

    def set(self, key, value):
        """Set key with AOF logging"""
        self.data[key] = str(value)
        # Real: AOF logs every write command
        self.aof_log.append({
            'cmd': 'SET',
            'key': key,
            'value': str(value),
            'timestamp': time.time()
        })
        return True

    def get(self, key):
        """Get value (reads don't affect persistence)"""
        return self.data.get(key)

    def save(self):
        """
        RDB: Save snapshot to disk (SAVE command)
        Real: Redis creates binary RDB file with entire dataset
        Simulation: Save to JSON
        """
        print("Saving RDB snapshot...")
        snapshot = {
            'timestamp': time.time(),
            'data': self.data,
            'keys': len(self.data)
        }

        # Simulate saving to disk
        print(f"  Saved {len(self.data)} keys to dump.rdb")
        self.last_save_time = time.time()
        return True

    def bgsave(self):
        """
        Background save (non-blocking)
        Real: Redis forks process to save without blocking
        Simulation: Same as save() but simulate background
        """
        print("Background save started (fork)")
        self.save()
        print("Background save completed")
        return True

    def bgrewriteaof(self):
        """
        Rewrite AOF file to compact it
        Real: Redis recreates AOF with minimal commands
        """
        print("Rewriting AOF...")
        # Compact: Instead of many SETs, create one per key
        self.aof_log = [
            {'cmd': 'SET', 'key': k, 'value': v, 'timestamp': time.time()}
            for k, v in self.data.items()
        ]
        print(f"  AOF compacted to {len(self.aof_log)} commands")
        return True

    def info_persistence(self):
        """Get persistence statistics"""
        return {
            'rdb_last_save_time': int(self.last_save_time),
            'rdb_changes_since_last_save': len(self.aof_log),
            'aof_size': len(self.aof_log),
            'keys_count': len(self.data)
        }

# Demonstration
redis = RedisPersistenceSimulation()

print("=== Writing Data ===")
redis.set('user:1', 'Alice')
redis.set('user:2', 'Bob')
redis.set('user:3', 'Carol')
redis.set('counter', '42')

print("\\n=== RDB Snapshot (SAVE) ===")
redis.save()

print("\\n=== More Writes ===")
redis.set('user:4', 'Dave')
redis.set('user:5', 'Eve')

print("\\n=== Background Save (BGSAVE) ===")
redis.bgsave()

print("\\n=== AOF Rewrite ===")
redis.bgrewriteaof()

print("\\n=== Persistence Info ===")
info = redis.info_persistence()
for key, value in info.items():
    print(f"  {key}: {value}")

print("\\n=== How Redis Persistence Works ===")
print("1. RDB: Periodic snapshots of entire dataset")
print("   - Fast recovery, larger files")
print("   - Can lose data between snapshots")
print("\\n2. AOF: Log of every write operation")
print("   - Better durability, can replay operations")
print("   - Larger files, slower recovery")
print("\\n3. Both: Use RDB for backups + AOF for durability")
'''

def create_redis_cluster_simulation():
    """Lesson 856: Redis - Redis Cluster"""
    return '''# In production: from rediscluster import RedisCluster
# startup_nodes = [{"host": "127.0.0.1", "port": "7000"}]
# rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

import hashlib

class RedisClusterSimulation:
    """
    Simulates Redis Cluster for horizontal scaling
    Real: Redis Cluster shards data across multiple nodes using hash slots
    """
    def __init__(self, num_nodes=3):
        self.num_nodes = num_nodes
        self.nodes = {}

        # Real: Redis Cluster has 16384 hash slots
        self.hash_slots = 16384

        # Initialize nodes with their slot ranges
        slots_per_node = self.hash_slots // num_nodes
        for i in range(num_nodes):
            start_slot = i * slots_per_node
            end_slot = start_slot + slots_per_node - 1
            if i == num_nodes - 1:
                end_slot = self.hash_slots - 1

            self.nodes[f'node_{i}'] = {
                'data': {},
                'slot_range': (start_slot, end_slot),
                'host': f'127.0.0.1:{7000 + i}'
            }

    def _calculate_slot(self, key):
        """
        Calculate hash slot for key
        Real: CRC16(key) mod 16384
        Simulation: Simple hash mod
        """
        # Redis uses CRC16 for hash slot calculation
        hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
        return hash_value % self.hash_slots

    def _get_node_for_slot(self, slot):
        """Determine which node owns this slot"""
        for node_name, node_info in self.nodes.items():
            start, end = node_info['slot_range']
            if start <= slot <= end:
                return node_name
        return None

    def set(self, key, value):
        """
        Set key-value, automatically routing to correct node
        Real: Client library handles routing via MOVED redirects
        """
        slot = self._calculate_slot(key)
        node = self._get_node_for_slot(slot)

        print(f"Key '{key}' -> slot {slot} -> {node}")
        self.nodes[node]['data'][key] = str(value)
        return True

    def get(self, key):
        """Get value, routing to correct node"""
        slot = self._calculate_slot(key)
        node = self._get_node_for_slot(slot)
        return self.nodes[node]['data'].get(key)

    def cluster_info(self):
        """Get cluster information"""
        info = {
            'cluster_state': 'ok',
            'cluster_slots_assigned': self.hash_slots,
            'cluster_known_nodes': self.num_nodes,
            'cluster_size': self.num_nodes
        }
        return info

    def cluster_nodes(self):
        """List all nodes and their slot ranges"""
        nodes_info = []
        for node_name, node_data in self.nodes.items():
            start, end = node_data['slot_range']
            keys_count = len(node_data['data'])
            nodes_info.append({
                'name': node_name,
                'host': node_data['host'],
                'slots': f'{start}-{end}',
                'keys': keys_count
            })
        return nodes_info

# Demonstration
cluster = RedisClusterSimulation(num_nodes=3)

print("=== Redis Cluster Setup ===")
info = cluster.cluster_info()
print(f"Cluster state: {info['cluster_state']}")
print(f"Nodes: {info['cluster_known_nodes']}")
print(f"Hash slots: {info['cluster_slots_assigned']}")

print("\\n=== Writing Data (automatic sharding) ===")
keys = ['user:1', 'user:2', 'user:3', 'order:100', 'order:101', 'session:abc']
for key in keys:
    cluster.set(key, f'value_of_{key}')

print("\\n=== Cluster Node Distribution ===")
nodes = cluster.cluster_nodes()
for node in nodes:
    print(f"{node['name']} ({node['host']})")
    print(f"  Slots: {node['slots']}")
    print(f"  Keys: {node['keys']}")

print("\\n=== Reading Data ===")
print(f"user:1 = {cluster.get('user:1')}")
print(f"order:100 = {cluster.get('order:100')}")

print("\\n=== Cluster Benefits ===")
print("1. Horizontal scaling: Add nodes to increase capacity")
print("2. Automatic sharding: Data distributed via hash slots")
print("3. High availability: Master-slave replication per shard")
print("4. No single point of failure")
'''

def create_redis_pipelining_simulation():
    """Lesson 857: Redis - Pipelining"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# pipe = r.pipeline()

import time

class RedisPipelineSimulation:
    """
    Simulates Redis pipelining for performance
    Real: Pipelines send multiple commands without waiting for responses
    """
    def __init__(self):
        self.data = {}
        self.pipeline_commands = []
        self.in_pipeline = False
        self.network_latency_ms = 1  # Simulated RTT

    def set(self, key, value):
        """Set command"""
        if self.in_pipeline:
            self.pipeline_commands.append(('SET', key, value))
            return self
        else:
            # Simulate network round-trip
            time.sleep(self.network_latency_ms / 1000)
            self.data[key] = str(value)
            return True

    def get(self, key):
        """Get command"""
        if self.in_pipeline:
            self.pipeline_commands.append(('GET', key))
            return self
        else:
            time.sleep(self.network_latency_ms / 1000)
            return self.data.get(key)

    def incr(self, key):
        """Increment command"""
        if self.in_pipeline:
            self.pipeline_commands.append(('INCR', key))
            return self
        else:
            time.sleep(self.network_latency_ms / 1000)
            current = int(self.data.get(key, '0'))
            self.data[key] = str(current + 1)
            return current + 1

    def pipeline(self):
        """
        Create pipeline context
        Real: Redis pipeline buffers commands client-side
        """
        self.in_pipeline = True
        self.pipeline_commands = []
        return self

    def execute(self):
        """
        Execute all pipelined commands
        Real: Single network round-trip for all commands
        Simulation: Execute all at once
        """
        if not self.in_pipeline:
            raise Exception("No pipeline active")

        # Simulate single network round-trip
        time.sleep(self.network_latency_ms / 1000)

        results = []
        for cmd in self.pipeline_commands:
            operation = cmd[0]

            if operation == 'SET':
                self.data[cmd[1]] = str(cmd[2])
                results.append(True)
            elif operation == 'GET':
                results.append(self.data.get(cmd[1]))
            elif operation == 'INCR':
                current = int(self.data.get(cmd[1], '0'))
                self.data[cmd[1]] = str(current + 1)
                results.append(current + 1)

        self.in_pipeline = False
        commands_count = len(self.pipeline_commands)
        self.pipeline_commands = []

        print(f"Executed {commands_count} commands in 1 network round-trip")
        return results

# Demonstration
redis = RedisPipelineSimulation()

print("=== Without Pipeline (slow) ===")
start = time.time()
for i in range(100):
    redis.set(f'key:{i}', f'value{i}')
elapsed_no_pipeline = (time.time() - start) * 1000
print(f"100 SETs: {elapsed_no_pipeline:.1f}ms")

print("\\n=== With Pipeline (fast) ===")
start = time.time()
pipe = redis.pipeline()
for i in range(100):
    pipe.set(f'pkey:{i}', f'pvalue{i}')
pipe.execute()
elapsed_pipeline = (time.time() - start) * 1000
print(f"100 SETs: {elapsed_pipeline:.1f}ms")

speedup = elapsed_no_pipeline / elapsed_pipeline
print(f"\\nSpeedup: {speedup:.1f}x faster")

print("\\n=== Pipeline with Multiple Operations ===")
pipe = redis.pipeline()
pipe.set('counter', '0')
pipe.incr('counter')
pipe.incr('counter')
pipe.incr('counter')
pipe.get('counter')
results = pipe.execute()
print(f"Results: {results}")
print(f"Final counter: {results[-1]}")

print("\\n=== Why Pipelining Helps ===")
print("Without: 100 commands = 100 network round-trips")
print("With: 100 commands = 1 network round-trip")
print("Critical for high-latency networks or many operations")
'''

def create_redis_lua_scripting_simulation():
    """Lesson 858: Redis - Lua Scripting"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# script = r.register_script(lua_script)

class RedisLuaSimulation:
    """
    Simulates Redis Lua scripting for atomic operations
    Real: Redis executes Lua scripts atomically on the server
    """
    def __init__(self):
        self.data = {}
        self.scripts = {}

    def set(self, key, value):
        """Set key-value"""
        self.data[key] = str(value)
        return True

    def get(self, key):
        """Get value"""
        return self.data.get(key)

    def eval(self, script, num_keys, *args):
        """
        Execute Lua script
        Real: Redis runs Lua interpreter server-side
        Simulation: Python implementation of common patterns
        """
        # Script 1: Atomic increment with max value
        if 'incr_max' in script:
            key = args[0]
            max_val = int(args[1])
            current = int(self.data.get(key, '0'))

            if current < max_val:
                new_val = current + 1
                self.data[key] = str(new_val)
                return new_val
            else:
                return current

        # Script 2: Conditional set (set only if value matches)
        elif 'cas' in script:  # Compare-and-swap
            key = args[0]
            expected = args[1]
            new_value = args[2]
            current = self.data.get(key)

            if current == expected:
                self.data[key] = str(new_value)
                return 1
            return 0

        # Script 3: Get and delete atomically
        elif 'getdel' in script:
            key = args[0]
            value = self.data.get(key)
            if key in self.data:
                del self.data[key]
            return value

        return None

    def register_script(self, script):
        """Register Lua script (returns SHA)"""
        import hashlib
        sha = hashlib.sha1(script.encode()).hexdigest()
        self.scripts[sha] = script
        return sha

    def evalsha(self, sha, num_keys, *args):
        """Execute registered script by SHA"""
        if sha in self.scripts:
            return self.eval(self.scripts[sha], num_keys, *args)
        raise Exception(f"Script {sha} not found")

# Demonstration
redis = RedisLuaSimulation()

print("=== Atomic Increment with Max (Lua) ===")
# This is atomic in Redis - no race conditions
redis.set('tickets:available', '0')

lua_incr_max = """
-- incr_max: Increment but don't exceed max
local current = redis.call('GET', KEYS[1]) or '0'
local max = tonumber(ARGV[1])
current = tonumber(current)

if current < max then
    redis.call('SET', KEYS[1], current + 1)
    return current + 1
else
    return current
end
"""

# Try to increment (should work)
result = redis.eval(lua_incr_max, 1, 'tickets:available', '5')
print(f"Increment to max 5: {result}")

for i in range(6):
    result = redis.eval(lua_incr_max, 1, 'tickets:available', '5')
    print(f"  Attempt {i+1}: {result}")

print("\\n=== Compare-and-Swap (CAS) ===")
redis.set('lock:resource', 'unlocked')

lua_cas = """
-- cas: Compare and swap
local current = redis.call('GET', KEYS[1])
if current == ARGV[1] then
    redis.call('SET', KEYS[1], ARGV[2])
    return 1
end
return 0
"""

# Try to acquire lock
success = redis.eval(lua_cas, 1, 'lock:resource', 'unlocked', 'locked')
print(f"Acquire lock: {'Success' if success else 'Failed'}")

# Try again (should fail)
success = redis.eval(lua_cas, 1, 'lock:resource', 'unlocked', 'locked')
print(f"Acquire again: {'Success' if success else 'Failed'}")

print("\\n=== Get and Delete Atomically ===")
redis.set('temp:data', 'important_value')

lua_getdel = """
-- getdel: Get and delete in one operation
local value = redis.call('GET', KEYS[1])
redis.call('DEL', KEYS[1])
return value
"""

value = redis.eval(lua_getdel, 1, 'temp:data')
print(f"Got and deleted: {value}")
print(f"Key exists after: {redis.get('temp:data')}")

print("\\n=== Why Lua Scripts ===")
print("1. Atomicity: Script executes without interruption")
print("2. Performance: No network round-trips for logic")
print("3. Complex operations: Multi-step logic server-side")
print("4. Race condition prevention")
'''

def create_cache_aside_writethrough_simulation():
    """Lesson 1004: Redis - Caching Strategies (Cache-Aside, Write-Through)"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

import time
import json

class CachingStrategiesSimulation:
    """
    Demonstrates Cache-Aside and Write-Through patterns
    Real: Used with Redis + Database (PostgreSQL, MySQL, etc.)
    """
    def __init__(self):
        self.cache = {}
        self.database = {
            'user:1': {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            'user:2': {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
            'user:3': {'id': 3, 'name': 'Carol', 'email': 'carol@example.com'},
        }
        self.db_queries = 0
        self.cache_hits = 0
        self.cache_misses = 0

    def cache_get(self, key):
        """Get from cache"""
        return self.cache.get(key)

    def cache_set(self, key, value, ttl=300):
        """Set in cache with TTL"""
        self.cache[key] = value
        return True

    def db_query(self, key):
        """Simulate database query (slow)"""
        time.sleep(0.01)  # Simulate DB latency
        self.db_queries += 1
        return self.database.get(key)

    def db_update(self, key, value):
        """Update database"""
        time.sleep(0.01)  # Simulate DB latency
        self.database[key] = value
        return True

    # Pattern 1: Cache-Aside (Lazy Loading)
    def get_user_cache_aside(self, user_id):
        """
        Cache-Aside Pattern:
        1. Check cache first
        2. If miss, query database
        3. Store in cache for next time

        Application manages cache explicitly
        """
        key = f'user:{user_id}'

        # Step 1: Try cache
        cached = self.cache_get(key)
        if cached:
            self.cache_hits += 1
            print(f"[Cache-Aside] CACHE HIT: {key}")
            return json.loads(cached)

        # Step 2: Cache miss - query database
        self.cache_misses += 1
        print(f"[Cache-Aside] CACHE MISS: {key} - querying DB")
        data = self.db_query(key)

        # Step 3: Store in cache
        if data:
            self.cache_set(key, json.dumps(data), ttl=300)
            print(f"[Cache-Aside] Cached {key} for 300s")

        return data

    # Pattern 2: Write-Through
    def update_user_write_through(self, user_id, data):
        """
        Write-Through Pattern:
        1. Write to cache first
        2. Immediately write to database
        3. Return success

        Cache stays consistent with DB
        Slower writes, but cache always fresh
        """
        key = f'user:{user_id}'

        print(f"[Write-Through] Updating {key}")

        # Step 1: Write to cache
        self.cache_set(key, json.dumps(data))
        print(f"  Cache updated")

        # Step 2: Write to database
        self.db_update(key, data)
        print(f"  Database updated")

        return True

    # Pattern 3: Write-Behind (Write-Back)
    def update_user_write_behind(self, user_id, data):
        """
        Write-Behind Pattern:
        1. Write to cache immediately
        2. Queue DB write for later (async)
        3. Return success quickly

        Faster writes, risk of data loss
        """
        key = f'user:{user_id}'

        print(f"[Write-Behind] Updating {key}")

        # Step 1: Write to cache immediately
        self.cache_set(key, json.dumps(data))
        print(f"  Cache updated (instant)")

        # Step 2: Queue for async DB write
        print(f"  DB write queued (background)")
        # Real: Would use Celery, RQ, or async task queue

        return True

    def get_stats(self):
        """Get cache statistics"""
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0

        return {
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'hit_rate': f'{hit_rate:.1f}%',
            'db_queries': self.db_queries
        }

# Demonstration
cache = CachingStrategiesSimulation()

print("=== Cache-Aside Pattern (Lazy Loading) ===")
# First request: cache miss
user1 = cache.get_user_cache_aside(1)
print(f"User: {user1}\\n")

# Second request: cache hit
user1_again = cache.get_user_cache_aside(1)
print(f"User: {user1_again}\\n")

# Third request: different user, cache miss
user2 = cache.get_user_cache_aside(2)
print(f"User: {user2}\\n")

print("=== Write-Through Pattern ===")
updated_user = {'id': 1, 'name': 'Alice Updated', 'email': 'alice.new@example.com'}
cache.update_user_write_through(1, updated_user)
print()

# Verify cache is updated
user1_updated = cache.get_user_cache_aside(1)
print(f"Updated user: {user1_updated}\\n")

print("=== Cache Statistics ===")
stats = cache.get_stats()
for key, value in stats.items():
    print(f"{key}: {value}")

print("\\n=== Pattern Comparison ===")
print("Cache-Aside: App manages cache, good for read-heavy")
print("Write-Through: Always consistent, slower writes")
print("Write-Behind: Fast writes, eventual consistency")
'''

def create_cache_invalidation_simulation():
    """Lesson 1005: Redis - Cache Invalidation Patterns"""
    return '''# In production: import redis
# r = redis.Redis(host='localhost', port=6379, decode_responses=True)

import time
import json

class CacheInvalidationSimulation:
    """
    Demonstrates cache invalidation strategies
    "There are only two hard things in Computer Science: cache invalidation and naming things"
    """
    def __init__(self):
        self.cache = {}
        self.ttl = {}
        self.dependencies = {}  # Track cache dependencies
        self.versions = {}  # For versioned caching

    def set(self, key, value, ex=None):
        """Set with optional expiration"""
        self.cache[key] = value
        if ex:
            self.ttl[key] = time.time() + ex
        return True

    def get(self, key):
        """Get with TTL check"""
        if key in self.ttl and time.time() > self.ttl[key]:
            self.delete(key)
            return None
        return self.cache.get(key)

    def delete(self, key):
        """Delete key"""
        if key in self.cache:
            del self.cache[key]
        if key in self.ttl:
            del self.ttl[key]
        return True

    # Strategy 1: TTL-Based Invalidation
    def cache_with_ttl(self, key, value, seconds=60):
        """
        Time-To-Live: Cache expires after fixed time
        Pros: Simple, prevents stale data
        Cons: May serve stale data before expiry
        """
        self.set(key, value, ex=seconds)
        print(f"[TTL] Cached {key} for {seconds}s")
        return True

    # Strategy 2: Event-Based Invalidation
    def invalidate_on_update(self, entity_type, entity_id):
        """
        Event-Based: Invalidate when data changes
        Pros: Always fresh data
        Cons: Requires update tracking
        """
        # Invalidate all related keys
        patterns = [
            f'{entity_type}:{entity_id}',
            f'{entity_type}:{entity_id}:*',
            f'list:{entity_type}',
        ]

        invalidated = []
        for pattern in patterns:
            for key in list(self.cache.keys()):
                if pattern.replace('*', '') in key:
                    self.delete(key)
                    invalidated.append(key)

        print(f"[Event] Invalidated {len(invalidated)} keys: {invalidated}")
        return invalidated

    # Strategy 3: Versioned Keys
    def set_versioned(self, base_key, value, version=None):
        """
        Versioned Keys: Include version in key name
        Pros: No invalidation needed, atomic updates
        Cons: Old versions accumulate
        """
        if version is None:
            version = self.versions.get(base_key, 0) + 1
            self.versions[base_key] = version

        versioned_key = f'{base_key}:v{version}'
        self.set(versioned_key, value)
        self.set(f'{base_key}:current', str(version))

        print(f"[Versioned] Set {versioned_key}")
        return version

    def get_versioned(self, base_key):
        """Get current version of key"""
        current_version = self.get(f'{base_key}:current')
        if current_version:
            return self.get(f'{base_key}:v{current_version}')
        return None

    # Strategy 4: Cache Tags
    def set_with_tags(self, key, value, tags):
        """
        Tags: Associate cache entries with tags for bulk invalidation
        Pros: Invalidate related items easily
        Cons: Need tag tracking
        """
        self.set(key, value)

        # Track which keys have which tags
        for tag in tags:
            tag_key = f'tag:{tag}'
            if tag_key not in self.dependencies:
                self.dependencies[tag_key] = []
            self.dependencies[tag_key].append(key)

        print(f"[Tags] Cached {key} with tags {tags}")
        return True

    def invalidate_by_tag(self, tag):
        """Invalidate all keys with this tag"""
        tag_key = f'tag:{tag}'
        keys = self.dependencies.get(tag_key, [])

        for key in keys:
            self.delete(key)

        print(f"[Tags] Invalidated {len(keys)} keys with tag '{tag}'")
        return len(keys)

    # Strategy 5: Write-Through Invalidation
    def update_with_invalidation(self, key, new_value):
        """
        Write-Through: Update cache and DB, or invalidate
        Pros: Cache always consistent
        Cons: Extra work on writes
        """
        print(f"[Write-Through] Updating {key}")

        # Option A: Update cache
        self.set(key, new_value)
        print(f"  Cache updated with new value")

        # Option B: Invalidate (simpler, lets next read refresh)
        # self.delete(key)
        # print(f"  Cache invalidated, will refresh on next read")

        return True

# Demonstration
cache = CacheInvalidationSimulation()

print("=== Strategy 1: TTL-Based Invalidation ===")
cache.cache_with_ttl('session:user123', 'session_data', seconds=60)
cache.cache_with_ttl('temp:data', 'temporary', seconds=5)
print()

print("=== Strategy 2: Event-Based Invalidation ===")
cache.set('user:100', '{"name": "Alice"}')
cache.set('user:100:profile', '{"avatar": "pic.jpg"}')
cache.set('list:users', '[100, 101, 102]')
print("Cached user data\\n")

print("User 100 updated - invalidating caches:")
cache.invalidate_on_update('user', '100')
print()

print("=== Strategy 3: Versioned Keys ===")
v1 = cache.set_versioned('product:500', '{"price": 99.99}')
v2 = cache.set_versioned('product:500', '{"price": 89.99}')
print(f"Current product: {cache.get_versioned('product:500')}")
print()

print("=== Strategy 4: Cache Tags ===")
cache.set_with_tags('report:jan', 'data1', tags=['reports', '2024'])
cache.set_with_tags('report:feb', 'data2', tags=['reports', '2024'])
cache.set_with_tags('summary:2024', 'data3', tags=['2024'])
print()

print("Invalidating all '2024' tagged caches:")
cache.invalidate_by_tag('2024')
print()

print("=== Strategy 5: Write-Through ===")
cache.update_with_invalidation('user:200', '{"name": "Bob Updated"}')

print("\\n=== Invalidation Best Practices ===")
print("1. Use TTL as safety net (even with other strategies)")
print("2. Event-based for critical data consistency")
print("3. Versioned keys for immutable data")
print("4. Tags for related data (e.g., user's posts)")
print("5. Monitor hit rates to tune strategy")
'''

def create_celery_redis_backend_simulation():
    """Lesson 822: Celery - Redis Backend"""
    return '''# In production:
# from celery import Celery
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/1')

import json
import time
import uuid

class CeleryRedisBackendSimulation:
    """
    Simulates Celery using Redis as message broker and result backend
    Real: Celery uses Redis for task queue and result storage
    """
    def __init__(self):
        # Redis DB 0: Message broker (task queue)
        self.task_queue = []

        # Redis DB 1: Result backend (task results)
        self.results = {}

        # Track task states
        self.task_states = {}

    def send_task(self, task_name, args=None, kwargs=None):
        """
        Queue a task (producer)
        Real: Celery serializes task and pushes to Redis list
        """
        task_id = str(uuid.uuid4())

        task_message = {
            'id': task_id,
            'task': task_name,
            'args': args or [],
            'kwargs': kwargs or {},
            'eta': None,
            'expires': None
        }

        # Push to Redis queue (LPUSH)
        self.task_queue.append(task_message)
        self.task_states[task_id] = 'PENDING'

        print(f"[Producer] Queued task {task_name} with ID {task_id}")
        return task_id

    def execute_task(self, task_message):
        """Execute a task (worker simulation)"""
        task_id = task_message['id']
        task_name = task_message['task']
        args = task_message['args']

        print(f"[Worker] Executing {task_name}({args})")
        self.task_states[task_id] = 'STARTED'

        # Simulate task execution
        try:
            # Example tasks
            if task_name == 'add':
                result = sum(args)
            elif task_name == 'send_email':
                time.sleep(0.1)  # Simulate email sending
                result = f"Email sent to {args[0]}"
            elif task_name == 'process_image':
                time.sleep(0.2)  # Simulate image processing
                result = f"Processed {args[0]}"
            else:
                result = "Task completed"

            # Store result in Redis (SET)
            self.results[task_id] = {
                'status': 'SUCCESS',
                'result': result,
                'traceback': None
            }
            self.task_states[task_id] = 'SUCCESS'

            print(f"[Worker] Task {task_id} completed: {result}")
            return result

        except Exception as e:
            # Store error in Redis
            self.results[task_id] = {
                'status': 'FAILURE',
                'result': None,
                'traceback': str(e)
            }
            self.task_states[task_id] = 'FAILURE'
            print(f"[Worker] Task {task_id} failed: {e}")
            return None

    def get_result(self, task_id, timeout=5):
        """
        Get task result (blocks until ready)
        Real: Polls Redis for result key
        """
        start = time.time()
        while time.time() - start < timeout:
            if task_id in self.results:
                result = self.results[task_id]
                print(f"[Consumer] Got result for {task_id}: {result['status']}")
                return result
            time.sleep(0.1)

        return {'status': 'PENDING', 'result': None}

    def get_state(self, task_id):
        """Get task state"""
        return self.task_states.get(task_id, 'PENDING')

    def worker_run(self, max_tasks=None):
        """
        Worker main loop
        Real: Celery worker blocks on BRPOP (blocking pop from Redis list)
        """
        print("[Worker] Starting worker...")
        processed = 0

        while self.task_queue and (max_tasks is None or processed < max_tasks):
            # Pop task from queue (BRPOP)
            task_message = self.task_queue.pop(0)
            self.execute_task(task_message)
            processed += 1

        print(f"[Worker] Processed {processed} tasks")
        return processed

# Demonstration
app = CeleryRedisBackendSimulation()

print("=== Queueing Tasks ===")
task1_id = app.send_task('add', args=[10, 32])
task2_id = app.send_task('send_email', args=['user@example.com'])
task3_id = app.send_task('process_image', args=['photo.jpg'])
print()

print("=== Worker Processing ===")
app.worker_run(max_tasks=3)
print()

print("=== Getting Results ===")
result1 = app.get_result(task1_id)
print(f"Task 1 result: {result1['result']}")

result2 = app.get_result(task2_id)
print(f"Task 2 result: {result2['result']}")

result3 = app.get_result(task3_id)
print(f"Task 3 result: {result3['result']}")

print("\\n=== Task States ===")
print(f"Task 1: {app.get_state(task1_id)}")
print(f"Task 2: {app.get_state(task2_id)}")
print(f"Task 3: {app.get_state(task3_id)}")

print("\\n=== Redis Data Structures Used ===")
print("Broker (DB 0): LIST for task queue (LPUSH/BRPOP)")
print("Backend (DB 1): STRING for results (SET/GET)")
print("State: STRING with JSON for task metadata")
'''

def create_docker_compose_redis_simulation():
    """Lesson 881: Docker - Docker Compose Multi-Container"""
    return '''# In production: docker-compose.yml defines multi-container apps
# This simulates how Redis works in a Docker Compose environment

class DockerComposeRedisSimulation:
    """
    Simulates Redis in Docker Compose multi-container setup
    Shows networking, volumes, and service dependencies
    """
    def __init__(self):
        self.containers = {}
        self.networks = {'app-network': []}
        self.volumes = {}

    def create_compose_config(self):
        """
        Simulates docker-compose.yml for Redis + App
        Real: Docker Compose orchestrates multiple containers
        """
        compose_config = {
            'version': '3.8',
            'services': {
                'redis': {
                    'image': 'redis:7-alpine',
                    'container_name': 'app-redis',
                    'ports': ['6379:6379'],
                    'volumes': ['redis-data:/data'],
                    'networks': ['app-network'],
                    'command': 'redis-server --appendonly yes',
                    'healthcheck': {
                        'test': ['CMD', 'redis-cli', 'ping'],
                        'interval': '10s',
                        'timeout': '3s',
                        'retries': 3
                    }
                },
                'app': {
                    'build': '.',
                    'container_name': 'python-app',
                    'depends_on': ['redis'],
                    'environment': {
                        'REDIS_HOST': 'redis',  # DNS: service name
                        'REDIS_PORT': '6379'
                    },
                    'networks': ['app-network'],
                    'volumes': ['./app:/app']
                },
                'worker': {
                    'build': '.',
                    'container_name': 'celery-worker',
                    'depends_on': ['redis'],
                    'environment': {
                        'CELERY_BROKER_URL': 'redis://redis:6379/0'
                    },
                    'networks': ['app-network'],
                    'command': 'celery -A tasks worker --loglevel=info'
                }
            },
            'networks': {
                'app-network': {
                    'driver': 'bridge'
                }
            },
            'volumes': {
                'redis-data': {}
            }
        }
        return compose_config

    def start_services(self):
        """
        Simulate docker-compose up
        Real: Starts containers in dependency order
        """
        print("=== Starting Docker Compose Services ===")

        # Start Redis first (no dependencies)
        print("\\n[1/3] Starting redis...")
        self.containers['redis'] = {
            'status': 'running',
            'ip': '172.18.0.2',
            'ports': {'6379/tcp': '6379'},
            'networks': ['app-network']
        }
        self.networks['app-network'].append('redis')
        print("  Container redis started at 172.18.0.2")
        print("  Exposed port: 6379")

        # Start app (depends on redis)
        print("\\n[2/3] Starting app...")
        print("  Waiting for redis to be healthy...")
        self.containers['app'] = {
            'status': 'running',
            'ip': '172.18.0.3',
            'networks': ['app-network'],
            'env': {
                'REDIS_HOST': 'redis',
                'REDIS_PORT': '6379'
            }
        }
        self.networks['app-network'].append('app')
        print("  Container app started at 172.18.0.3")
        print("  Can reach Redis at: redis:6379")

        # Start worker (depends on redis)
        print("\\n[3/3] Starting worker...")
        self.containers['worker'] = {
            'status': 'running',
            'ip': '172.18.0.4',
            'networks': ['app-network'],
            'env': {
                'CELERY_BROKER_URL': 'redis://redis:6379/0'
            }
        }
        self.networks['app-network'].append('worker')
        print("  Container worker started at 172.18.0.4")

        return True

    def show_network(self):
        """Show container networking"""
        print("\\n=== Docker Network: app-network ===")
        for service in self.networks['app-network']:
            container = self.containers[service]
            print(f"{service}")
            print(f"  IP: {container['ip']}")
            print(f"  DNS: {service}.app-network")

    def show_volumes(self):
        """Show volume mounts"""
        print("\\n=== Docker Volumes ===")
        print("redis-data:")
        print("  Mount: /data (inside container)")
        print("  Purpose: Persist Redis data")
        print("  Type: Named volume (managed by Docker)")

    def simulate_app_connection(self):
        """Simulate app connecting to Redis"""
        print("\\n=== App Connecting to Redis ===")
        print("Python app code:")
        print("  import redis")
        print("  import os")
        print("  ")
        print("  # Uses Docker Compose service name as hostname")
        print("  host = os.getenv('REDIS_HOST', 'redis')")
        print("  port = os.getenv('REDIS_PORT', 6379)")
        print("  ")
        print("  r = redis.Redis(host=host, port=port)")
        print("  r.set('app:status', 'connected')")
        print("  ")
        print("Result: ✓ Connected to redis:6379")

    def show_commands(self):
        """Show common Docker Compose commands"""
        print("\\n=== Common Docker Compose Commands ===")
        commands = [
            ("docker-compose up -d", "Start services in background"),
            ("docker-compose ps", "List running services"),
            ("docker-compose logs redis", "View Redis logs"),
            ("docker-compose exec redis redis-cli", "Connect to Redis CLI"),
            ("docker-compose down", "Stop and remove containers"),
            ("docker-compose down -v", "Stop and remove volumes too"),
        ]

        for cmd, desc in commands:
            print(f"  {cmd}")
            print(f"    → {desc}")

# Demonstration
compose = DockerComposeRedisSimulation()

# Show compose config
config = compose.create_compose_config()
print("=== Docker Compose Configuration ===")
print(f"Services: {', '.join(config['services'].keys())}")
print(f"Networks: {', '.join(config['networks'].keys())}")
print(f"Volumes: {', '.join(config['volumes'].keys())}")

# Start services
compose.start_services()

# Show networking
compose.show_network()

# Show volumes
compose.show_volumes()

# Simulate connection
compose.simulate_app_connection()

# Show commands
compose.show_commands()

print("\\n=== Why Docker Compose + Redis ===")
print("1. Consistent environment: Same config dev to prod")
print("2. Service discovery: Use 'redis' hostname, not IP")
print("3. Easy scaling: docker-compose up --scale worker=3")
print("4. Data persistence: Volumes survive container restarts")
'''

def create_redis_production_simulation():
    """Lesson 1006: Redis - Redis Production"""
    return '''# In production: import redis
# from redis.sentinel import Sentinel
# from redis.cluster import RedisCluster

import time
import random

class RedisProductionSimulation:
    """
    Simulates Redis production setup with HA and monitoring
    Real: Redis Sentinel, Cluster, monitoring, and best practices
    """
    def __init__(self):
        self.master = {'host': '10.0.1.10', 'port': 6379, 'status': 'online'}
        self.replicas = [
            {'host': '10.0.1.11', 'port': 6379, 'status': 'online'},
            {'host': '10.0.1.12', 'port': 6379, 'status': 'online'}
        ]
        self.sentinels = [
            {'host': '10.0.1.20', 'port': 26379},
            {'host': '10.0.1.21', 'port': 26379},
            {'host': '10.0.1.22', 'port': 26379}
        ]
        self.metrics = {
            'ops_per_sec': 0,
            'connected_clients': 0,
            'used_memory_mb': 0,
            'evicted_keys': 0,
            'hit_rate': 0
        }

    def configure_sentinel(self):
        """
        Redis Sentinel for high availability
        Real: Monitors master, auto-failover if down
        """
        print("=== Redis Sentinel Configuration ===")
        print("sentinel.conf:")
        print("  sentinel monitor mymaster 10.0.1.10 6379 2")
        print("  sentinel down-after-milliseconds mymaster 5000")
        print("  sentinel parallel-syncs mymaster 1")
        print("  sentinel failover-timeout mymaster 10000")
        print()
        print("Setup:")
        for i, s in enumerate(self.sentinels):
            print(f"  Sentinel {i+1}: {s['host']}:{s['port']}")
        print()
        print("Quorum: 2 sentinels must agree for failover")

    def simulate_failover(self):
        """Simulate automatic failover"""
        print("\\n=== Automatic Failover Simulation ===")
        print(f"Master: {self.master['host']} (online)")
        print("Replicas:")
        for r in self.replicas:
            print(f"  - {r['host']} (replicating)")

        print("\\n[!] Master crashes!")
        self.master['status'] = 'down'
        time.sleep(0.1)

        print("[Sentinel] Detected master down")
        print("[Sentinel] Quorum reached (2/3 sentinels agree)")
        print("[Sentinel] Starting failover...")
        time.sleep(0.1)

        # Promote replica to master
        new_master = self.replicas[0]
        print(f"[Sentinel] Promoted {new_master['host']} to master")

        self.master = new_master
        self.replicas = self.replicas[1:] + [{'host': '10.0.1.10', 'port': 6379, 'status': 'replica'}]

        print("[Sentinel] Failover complete")
        print(f"\\nNew master: {self.master['host']}")

    def configure_persistence(self):
        """Production persistence config"""
        print("\\n=== Production Persistence ===")
        print("redis.conf:")
        print("  # RDB Snapshots")
        print("  save 900 1      # Save if 1 key changed in 15 min")
        print("  save 300 10     # Save if 10 keys changed in 5 min")
        print("  save 60 10000   # Save if 10k keys changed in 1 min")
        print()
        print("  # AOF (Append-Only File)")
        print("  appendonly yes")
        print("  appendfsync everysec  # Fsync every second (good balance)")
        print()
        print("  # Memory Management")
        print("  maxmemory 2gb")
        print("  maxmemory-policy allkeys-lru  # Evict least recently used")

    def monitor_metrics(self):
        """Simulate production monitoring"""
        print("\\n=== Production Monitoring ===")

        # Simulate metrics
        self.metrics = {
            'ops_per_sec': random.randint(5000, 15000),
            'connected_clients': random.randint(50, 200),
            'used_memory_mb': random.randint(500, 1800),
            'evicted_keys': random.randint(0, 100),
            'hit_rate': random.uniform(85, 99)
        }

        print("Real-time Metrics (INFO command):")
        print(f"  Operations/sec: {self.metrics['ops_per_sec']:,}")
        print(f"  Connected clients: {self.metrics['connected_clients']}")
        print(f"  Memory used: {self.metrics['used_memory_mb']} MB / 2048 MB")
        print(f"  Cache hit rate: {self.metrics['hit_rate']:.1f}%")
        print(f"  Evicted keys: {self.metrics['evicted_keys']}")

        # Alerts
        print("\\nAlerts:")
        if self.metrics['used_memory_mb'] > 1800:
            print("  ⚠️  HIGH: Memory usage > 90%")
        if self.metrics['hit_rate'] < 90:
            print("  ⚠️  WARNING: Hit rate below 90%")
        if self.metrics['evicted_keys'] > 50:
            print("  ⚠️  WARNING: High eviction rate")

        if all([
            self.metrics['used_memory_mb'] < 1800,
            self.metrics['hit_rate'] >= 90,
            self.metrics['evicted_keys'] < 50
        ]):
            print("  ✓ All metrics healthy")

    def security_config(self):
        """Production security settings"""
        print("\\n=== Production Security ===")
        print("redis.conf:")
        print("  # Authentication")
        print("  requirepass <strong-password>")
        print("  ")
        print("  # Network")
        print("  bind 10.0.1.10  # Only listen on private IP")
        print("  protected-mode yes")
        print("  ")
        print("  # Disable dangerous commands")
        print("  rename-command FLUSHDB \"\"")
        print("  rename-command FLUSHALL \"\"")
        print("  rename-command CONFIG \"CONFIG_abc123\"")
        print()
        print("Firewall: Only allow ports 6379, 26379 from app servers")
        print("SSL/TLS: Use Redis 6+ with TLS for encryption")

    def backup_strategy(self):
        """Production backup strategy"""
        print("\\n=== Backup Strategy ===")
        print("1. RDB snapshots:")
        print("   - Hourly: Keep last 24")
        print("   - Daily: Keep last 30")
        print("   - Weekly: Keep last 12")
        print()
        print("2. AOF persistence:")
        print("   - Real-time write log")
        print("   - Rewrite nightly (compact)")
        print()
        print("3. Remote backups:")
        print("   - Copy RDB to S3/GCS daily")
        print("   - Encrypted and versioned")
        print()
        print("4. Disaster recovery:")
        print("   - Test restore monthly")
        print("   - RTO: 15 minutes")
        print("   - RPO: 1 second (AOF)")

# Demonstration
redis_prod = RedisProductionSimulation()

# Configuration
redis_prod.configure_sentinel()

# Failover
redis_prod.simulate_failover()

# Persistence
redis_prod.configure_persistence()

# Monitoring
redis_prod.monitor_metrics()

# Security
redis_prod.security_config()

# Backup
redis_prod.backup_strategy()

print("\\n=== Production Checklist ===")
print("✓ High availability (Sentinel or Cluster)")
print("✓ Replication (1 master + 2+ replicas)")
print("✓ Persistence (RDB + AOF)")
print("✓ Monitoring (Prometheus, Datadog, CloudWatch)")
print("✓ Security (auth, firewall, TLS)")
print("✓ Backups (automated, tested)")
print("✓ Resource limits (maxmemory, client limits)")
print("✓ Alerting (Slack, PagerDuty)")
'''

# Mapping of lesson IDs to simulation creators
SIMULATIONS = {
    850: create_redis_basics_simulation,
    851: create_redis_data_structures_simulation,
    852: create_redis_pubsub_simulation,
    853: create_redis_caching_simulation,
    854: create_redis_transactions_simulation,
    855: create_redis_persistence_simulation,
    856: create_redis_cluster_simulation,
    857: create_redis_pipelining_simulation,
    858: create_redis_lua_scripting_simulation,
    1004: create_cache_aside_writethrough_simulation,
    1005: create_cache_invalidation_simulation,
    822: create_celery_redis_backend_simulation,
    881: create_docker_compose_redis_simulation,
    1006: create_redis_production_simulation,
}

def main():
    """Main upgrade function"""
    print("Reading lessons-python.json...")
    with open(r'c:\devbootLLM-app\public\lessons-python.json', encoding='utf-8') as f:
        lessons = json.load(f)

    upgraded_count = 0
    upgraded_lessons = []

    for lesson_id, create_simulation in SIMULATIONS.items():
        print(f"\nUpgrading lesson {lesson_id}...")

        # Find lesson
        lesson_index = None
        for i, lesson in enumerate(lessons):
            if lesson['id'] == lesson_id:
                lesson_index = i
                break

        if lesson_index is None:
            print(f"  ERROR: Lesson {lesson_id} not found!")
            continue

        # Create simulation
        new_simulation = create_simulation()

        # Update lesson
        lessons[lesson_index]['fullSolution'] = new_simulation

        upgraded_count += 1
        upgraded_lessons.append({
            'id': lesson_id,
            'title': lessons[lesson_index]['title'],
            'length': len(new_simulation)
        })

        print(f"  [OK] Updated: {lessons[lesson_index]['title']}")
        print(f"    New length: {len(new_simulation)} characters")

    # Write back
    print(f"\nWriting updated lessons to file...")
    with open(r'c:\devbootLLM-app\public\lessons-python.json', 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Successfully upgraded {upgraded_count} lessons")

    # Print report
    print("\n" + "="*60)
    print("UPGRADE REPORT")
    print("="*60)
    for lesson in upgraded_lessons:
        print(f"ID {lesson['id']}: {lesson['title']}")
        print(f"  Length: {lesson['length']} characters")

    return upgraded_count, upgraded_lessons

if __name__ == '__main__':
    count, lessons = main()
    sys.exit(0 if count > 0 else 1)
