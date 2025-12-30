#!/usr/bin/env python3
"""
Upgrade Redis lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 12: Redis Data Structures, Persistence, and Transactions
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 851: Redis Data Structures
    lesson_851 = next(l for l in lessons if l['id'] == 851)
    lesson_851['fullSolution'] = '''# Redis Data Structures - Complete Simulation
# In production: pip install redis
# This lesson simulates all core Redis data structures with production patterns

import time
from typing import Any, Dict, List, Optional, Set, Tuple
from collections import OrderedDict
import bisect

class RedisString:
    """Simulated Redis String operations."""

    def __init__(self):
        self.data: Dict[str, str] = {}
        self.expires: Dict[str, float] = {}

    def set(self, key: str, value: str, ex: Optional[int] = None, nx: bool = False, xx: bool = False) -> Optional[str]:
        """
        SET with options:
        - EX: expiration in seconds
        - NX: only set if key doesn't exist
        - XX: only set if key exists
        """
        # Check expiration
        if key in self.expires and time.time() > self.expires[key]:
            del self.data[key]
            del self.expires[key]

        # NX: only if not exists
        if nx and key in self.data:
            return None

        # XX: only if exists
        if xx and key not in self.data:
            return None

        self.data[key] = str(value)

        if ex:
            self.expires[key] = time.time() + ex

        return "OK"

    def get(self, key: str) -> Optional[str]:
        """Get value by key."""
        if key in self.expires and time.time() > self.expires[key]:
            del self.data[key]
            del self.expires[key]
            return None
        return self.data.get(key)

    def incr(self, key: str) -> int:
        """Increment integer value."""
        current = int(self.data.get(key, 0))
        current += 1
        self.data[key] = str(current)
        return current

    def decr(self, key: str) -> int:
        """Decrement integer value."""
        current = int(self.data.get(key, 0))
        current -= 1
        self.data[key] = str(current)
        return current

    def append(self, key: str, value: str) -> int:
        """Append to string value."""
        current = self.data.get(key, "")
        new_value = current + value
        self.data[key] = new_value
        return len(new_value)

    def getrange(self, key: str, start: int, end: int) -> str:
        """Get substring."""
        value = self.data.get(key, "")
        if end == -1:
            return value[start:]
        return value[start:end+1]

class RedisList:
    """Simulated Redis List operations."""

    def __init__(self):
        self.data: Dict[str, List[str]] = {}

    def lpush(self, key: str, *values: str) -> int:
        """Push to left (head) of list."""
        if key not in self.data:
            self.data[key] = []
        for value in reversed(values):
            self.data[key].insert(0, value)
        return len(self.data[key])

    def rpush(self, key: str, *values: str) -> int:
        """Push to right (tail) of list."""
        if key not in self.data:
            self.data[key] = []
        self.data[key].extend(values)
        return len(self.data[key])

    def lpop(self, key: str) -> Optional[str]:
        """Pop from left (head) of list."""
        if key not in self.data or not self.data[key]:
            return None
        return self.data[key].pop(0)

    def rpop(self, key: str) -> Optional[str]:
        """Pop from right (tail) of list."""
        if key not in self.data or not self.data[key]:
            return None
        return self.data[key].pop()

    def lrange(self, key: str, start: int, end: int) -> List[str]:
        """Get range of elements."""
        if key not in self.data:
            return []
        lst = self.data[key]
        if end == -1:
            return lst[start:]
        return lst[start:end+1]

    def llen(self, key: str) -> int:
        """Get list length."""
        return len(self.data.get(key, []))

    def lindex(self, key: str, index: int) -> Optional[str]:
        """Get element at index."""
        if key not in self.data:
            return None
        try:
            return self.data[key][index]
        except IndexError:
            return None

    def lset(self, key: str, index: int, value: str) -> str:
        """Set element at index."""
        if key not in self.data:
            raise Exception("ERR no such key")
        try:
            self.data[key][index] = value
            return "OK"
        except IndexError:
            raise Exception("ERR index out of range")

    def ltrim(self, key: str, start: int, end: int) -> str:
        """Trim list to specified range."""
        if key in self.data:
            if end == -1:
                self.data[key] = self.data[key][start:]
            else:
                self.data[key] = self.data[key][start:end+1]
        return "OK"

class RedisSet:
    """Simulated Redis Set operations."""

    def __init__(self):
        self.data: Dict[str, Set[str]] = {}

    def sadd(self, key: str, *members: str) -> int:
        """Add members to set."""
        if key not in self.data:
            self.data[key] = set()
        before = len(self.data[key])
        self.data[key].update(members)
        return len(self.data[key]) - before

    def srem(self, key: str, *members: str) -> int:
        """Remove members from set."""
        if key not in self.data:
            return 0
        before = len(self.data[key])
        self.data[key].difference_update(members)
        return before - len(self.data[key])

    def smembers(self, key: str) -> Set[str]:
        """Get all members."""
        return self.data.get(key, set()).copy()

    def sismember(self, key: str, member: str) -> bool:
        """Check if member exists."""
        return member in self.data.get(key, set())

    def scard(self, key: str) -> int:
        """Get set cardinality (size)."""
        return len(self.data.get(key, set()))

    def sinter(self, *keys: str) -> Set[str]:
        """Intersection of sets."""
        if not keys:
            return set()

        result = self.data.get(keys[0], set()).copy()
        for key in keys[1:]:
            result &= self.data.get(key, set())
        return result

    def sunion(self, *keys: str) -> Set[str]:
        """Union of sets."""
        result = set()
        for key in keys:
            result |= self.data.get(key, set())
        return result

    def sdiff(self, *keys: str) -> Set[str]:
        """Difference of sets."""
        if not keys:
            return set()

        result = self.data.get(keys[0], set()).copy()
        for key in keys[1:]:
            result -= self.data.get(key, set())
        return result

class RedisSortedSet:
    """Simulated Redis Sorted Set operations."""

    def __init__(self):
        self.data: Dict[str, Dict[str, float]] = {}

    def zadd(self, key: str, mapping: Dict[str, float]) -> int:
        """Add members with scores."""
        if key not in self.data:
            self.data[key] = {}

        count = 0
        for member, score in mapping.items():
            if member not in self.data[key]:
                count += 1
            self.data[key][member] = float(score)
        return count

    def zrem(self, key: str, *members: str) -> int:
        """Remove members."""
        if key not in self.data:
            return 0

        count = 0
        for member in members:
            if member in self.data[key]:
                del self.data[key][member]
                count += 1
        return count

    def zscore(self, key: str, member: str) -> Optional[float]:
        """Get score of member."""
        if key not in self.data or member not in self.data[key]:
            return None
        return self.data[key][member]

    def zrange(self, key: str, start: int, end: int, withscores: bool = False) -> List:
        """Get range by rank (sorted by score)."""
        if key not in self.data:
            return []

        sorted_items = sorted(self.data[key].items(), key=lambda x: (x[1], x[0]))

        if end == -1:
            items = sorted_items[start:]
        else:
            items = sorted_items[start:end+1]

        if withscores:
            return [(member, score) for member, score in items]
        return [member for member, score in items]

    def zrevrange(self, key: str, start: int, end: int, withscores: bool = False) -> List:
        """Get range by rank in reverse order."""
        if key not in self.data:
            return []

        sorted_items = sorted(self.data[key].items(), key=lambda x: (x[1], x[0]), reverse=True)

        if end == -1:
            items = sorted_items[start:]
        else:
            items = sorted_items[start:end+1]

        if withscores:
            return [(member, score) for member, score in items]
        return [member for member, score in items]

    def zrangebyscore(self, key: str, min_score: float, max_score: float, withscores: bool = False) -> List:
        """Get range by score."""
        if key not in self.data:
            return []

        filtered = [(m, s) for m, s in self.data[key].items() if min_score <= s <= max_score]
        sorted_items = sorted(filtered, key=lambda x: (x[1], x[0]))

        if withscores:
            return sorted_items
        return [member for member, score in sorted_items]

    def zcard(self, key: str) -> int:
        """Get sorted set cardinality."""
        return len(self.data.get(key, {}))

    def zincrby(self, key: str, increment: float, member: str) -> float:
        """Increment score of member."""
        if key not in self.data:
            self.data[key] = {}

        current = self.data[key].get(member, 0.0)
        new_score = current + increment
        self.data[key][member] = new_score
        return new_score

class RedisHash:
    """Simulated Redis Hash operations."""

    def __init__(self):
        self.data: Dict[str, Dict[str, str]] = {}

    def hset(self, key: str, field: str, value: str) -> int:
        """Set hash field."""
        if key not in self.data:
            self.data[key] = {}

        is_new = field not in self.data[key]
        self.data[key][field] = str(value)
        return 1 if is_new else 0

    def hget(self, key: str, field: str) -> Optional[str]:
        """Get hash field."""
        if key not in self.data:
            return None
        return self.data[key].get(field)

    def hmset(self, key: str, mapping: Dict[str, str]) -> str:
        """Set multiple hash fields."""
        if key not in self.data:
            self.data[key] = {}

        for field, value in mapping.items():
            self.data[key][field] = str(value)
        return "OK"

    def hmget(self, key: str, *fields: str) -> List[Optional[str]]:
        """Get multiple hash fields."""
        if key not in self.data:
            return [None] * len(fields)

        return [self.data[key].get(field) for field in fields]

    def hgetall(self, key: str) -> Dict[str, str]:
        """Get all hash fields and values."""
        return self.data.get(key, {}).copy()

    def hdel(self, key: str, *fields: str) -> int:
        """Delete hash fields."""
        if key not in self.data:
            return 0

        count = 0
        for field in fields:
            if field in self.data[key]:
                del self.data[key][field]
                count += 1
        return count

    def hexists(self, key: str, field: str) -> bool:
        """Check if hash field exists."""
        return key in self.data and field in self.data[key]

    def hkeys(self, key: str) -> List[str]:
        """Get all hash field names."""
        return list(self.data.get(key, {}).keys())

    def hvals(self, key: str) -> List[str]:
        """Get all hash values."""
        return list(self.data.get(key, {}).values())

    def hincrby(self, key: str, field: str, increment: int) -> int:
        """Increment hash field by integer."""
        if key not in self.data:
            self.data[key] = {}

        current = int(self.data[key].get(field, 0))
        new_value = current + increment
        self.data[key][field] = str(new_value)
        return new_value

# Example 1: Strings - Caching and Counters
print("Example 1: Strings - Caching and Counters")
print("=" * 60)

strings = RedisString()

# Cache user session
strings.set("session:abc123", "user_id:1000", ex=3600)
print("Set session with 1-hour expiration:")
print(f"  session:abc123 = {strings.get('session:abc123')}")
print()

# Atomic counter
print("Page view counter:")
for i in range(5):
    count = strings.incr("pageviews:home")
    print(f"  Visit {i+1}: {count} total views")
print()

# SET with NX (only if not exists) - distributed lock
lock_acquired = strings.set("lock:resource:123", "worker1", ex=10, nx=True)
print(f"Acquire lock: {'SUCCESS' if lock_acquired else 'FAILED'}")

lock_acquired_2 = strings.set("lock:resource:123", "worker2", ex=10, nx=True)
print(f"Second acquire: {'SUCCESS' if lock_acquired_2 else 'FAILED (already locked)'}")
print()

# Example 2: Lists - Job Queue and Activity Feed
print("Example 2: Lists - Job Queue and Activity Feed")
print("=" * 60)

lists = RedisList()

# Job queue (FIFO)
print("Job Queue (producer adds to right, worker pops from left):")
lists.rpush("jobs:queue", "job1", "job2", "job3")
print(f"  Queued 3 jobs, length: {lists.llen('jobs:queue')}")

# Process jobs
for i in range(3):
    job = lists.lpop("jobs:queue")
    print(f"  Processing: {job}")
print()

# Activity feed (most recent first)
print("Activity Feed:")
lists.lpush("feed:user:100", "liked photo", "commented", "shared post")

recent_activities = lists.lrange("feed:user:100", 0, 4)
for i, activity in enumerate(recent_activities, 1):
    print(f"  {i}. {activity}")

# Trim to keep only last 100 items
lists.ltrim("feed:user:100", 0, 99)
print(f"  Feed trimmed to {lists.llen('feed:user:100')} items")
print()

# Example 3: Sets - Tags and Social Features
print("Example 3: Sets - Tags and Social Features")
print("=" * 60)

sets = RedisSet()

# Article tags
sets.sadd("article:1:tags", "python", "redis", "caching")
sets.sadd("article:2:tags", "python", "django", "web")
sets.sadd("article:3:tags", "redis", "performance", "database")

print("Article tags:")
print(f"  Article 1: {sets.smembers('article:1:tags')}")
print(f"  Article 2: {sets.smembers('article:2:tags')}")
print(f"  Article 3: {sets.smembers('article:3:tags')}")
print()

# Find articles with common tags
common = sets.sinter("article:1:tags", "article:2:tags")
print(f"Articles 1 & 2 common tags: {common}")

common2 = sets.sinter("article:1:tags", "article:3:tags")
print(f"Articles 1 & 3 common tags: {common2}")
print()

# Social features - mutual friends
sets.sadd("user:alice:friends", "bob", "charlie", "david")
sets.sadd("user:bob:friends", "alice", "charlie", "eve")

mutual = sets.sinter("user:alice:friends", "user:bob:friends")
print(f"Alice and Bob mutual friends: {mutual}")

# Friend suggestions (Bob's friends who aren't Alice's friends)
suggestions = sets.sdiff("user:bob:friends", "user:alice:friends")
print(f"Friend suggestions for Alice: {suggestions}")
print()

# Example 4: Sorted Sets - Leaderboards and Rankings
print("Example 4: Sorted Sets - Leaderboards and Rankings")
print("=" * 60)

zsets = RedisSortedSet()

# Game leaderboard
zsets.zadd("leaderboard:game1", {
    "player1": 1500,
    "player2": 2300,
    "player3": 1800,
    "player4": 2100,
    "player5": 1900,
})

print("Top 3 Players:")
top3 = zsets.zrevrange("leaderboard:game1", 0, 2, withscores=True)
for rank, (player, score) in enumerate(top3, 1):
    print(f"  {rank}. {player}: {int(score)} points")
print()

# Update score
new_score = zsets.zincrby("leaderboard:game1", 500, "player1")
print(f"Player1 earned 500 points, new score: {int(new_score)}")
print()

# Trending articles (time-decaying scores)
now = time.time()
zsets.zadd("trending:articles", {
    "article:100": now - 3600,   # 1 hour ago
    "article:101": now - 1800,   # 30 min ago
    "article:102": now - 300,    # 5 min ago
})

print("Trending Articles (most recent first):")
trending = zsets.zrevrange("trending:articles", 0, -1, withscores=True)
for article, timestamp in trending:
    age = int((now - timestamp) / 60)
    print(f"  {article}: {age} minutes ago")
print()

# Example 5: Hashes - Object Storage
print("Example 5: Hashes - Object Storage")
print("=" * 60)

hashes = RedisHash()

# Store user object
hashes.hmset("user:1000", {
    "username": "alice",
    "email": "alice@example.com",
    "age": "28",
    "country": "USA"
})

print("User Profile:")
user_data = hashes.hgetall("user:1000")
for field, value in user_data.items():
    print(f"  {field}: {value}")
print()

# Update specific fields
hashes.hset("user:1000", "age", "29")
print(f"Updated age: {hashes.hget('user:1000', 'age')}")
print()

# Product inventory
hashes.hmset("product:500", {
    "name": "Laptop",
    "price": "999",
    "stock": "50"
})

# Sell 3 units
new_stock = hashes.hincrby("product:500", "stock", -3)
print(f"Sold 3 laptops, stock remaining: {new_stock}")
print()

# Get specific fields
name, price = hashes.hmget("product:500", "name", "price")
print(f"Product: {name}, Price: ${price}")

print()
print("=" * 60)
print("DATA STRUCTURE SELECTION GUIDE")
print("=" * 60)
print("""
STRING - Simple key-value storage
  Use cases:
    - Caching (HTML fragments, API responses)
    - Session storage
    - Distributed locks (SET with NX)
    - Counters (INCR/DECR)
    - Feature flags
  Operations: O(1) for GET, SET, INCR

LIST - Ordered collection with duplicates
  Use cases:
    - Job queues (LPUSH/RPOP)
    - Activity feeds (LPUSH/LRANGE)
    - Recent items (with LTRIM)
    - Timeline data
  Operations: O(1) for head/tail, O(N) for middle

SET - Unordered unique elements
  Use cases:
    - Tags/categories
    - Unique visitors tracking
    - Social graphs (followers/following)
    - Intersection/union queries
  Operations: O(1) for add/remove/membership

SORTED SET - Ordered unique elements with scores
  Use cases:
    - Leaderboards
    - Priority queues
    - Time-series data
    - Rate limiting windows
    - Trending content
  Operations: O(log(N)) for add/remove

HASH - Field-value pairs (sub-keys)
  Use cases:
    - Object storage (user profiles)
    - Shopping carts
    - Configuration
    - Multi-field counters
  Operations: O(1) for field access

MEMORY EFFICIENCY:
  - Hashes: Best for objects with many fields
  - Sorted Sets: Efficient for range queries
  - Sets: Compact for unique values
  - Lists: Good for sequential access
  - Strings: Simple but can waste memory for small values

Production note: Real Redis provides:
  - Bitmaps (SETBIT, GETBIT)
  - HyperLogLogs (PFADD, PFCOUNT)
  - Geospatial indexes (GEOADD, GEORADIUS)
  - Streams (XADD, XREAD)
  - JSON (RedisJSON module)
  - Search capabilities (RediSearch module)
""")
'''

    # Lesson 855: Redis Persistence
    lesson_855 = next(l for l in lessons if l['id'] == 855)
    lesson_855['fullSolution'] = '''# Redis Persistence - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis persistence mechanisms (RDB and AOF)

import time
import json
import os
from typing import Dict, List, Any, Optional
from enum import Enum
from dataclasses import dataclass
import gzip

class PersistenceMode(Enum):
    """Redis persistence modes."""
    NONE = "none"
    RDB = "rdb"          # Snapshots
    AOF = "aof"          # Append-only file
    BOTH = "both"        # RDB + AOF

@dataclass
class RDBConfig:
    """RDB snapshot configuration."""
    save_intervals: List[tuple]  # (seconds, min_changes)
    filename: str = "dump.rdb"
    compression: bool = True

    def should_save(self, seconds_elapsed: int, changes: int) -> bool:
        """Check if snapshot should be triggered."""
        for interval_seconds, min_changes in self.save_intervals:
            if seconds_elapsed >= interval_seconds and changes >= min_changes:
                return True
        return False

@dataclass
class AOFConfig:
    """AOF (Append-Only File) configuration."""
    filename: str = "appendonly.aof"
    fsync_policy: str = "everysec"  # "always", "everysec", "no"
    auto_rewrite_percentage: int = 100  # Rewrite when 100% bigger
    auto_rewrite_min_size: int = 64 * 1024  # Min 64MB

class RDBSnapshot:
    """
    RDB Snapshot Handler.

    RDB creates point-in-time snapshots of the dataset.

    Advantages:
    - Compact single-file backups
    - Faster restart times
    - Good for disaster recovery

    Disadvantages:
    - Data loss between snapshots
    - Fork can be expensive with large datasets
    """

    def __init__(self, config: RDBConfig):
        self.config = config
        self.last_save_time = time.time()
        self.changes_since_save = 0

    def save(self, data: Dict[str, Any]) -> bool:
        """
        Create RDB snapshot.

        In real Redis:
        1. BGSAVE forks a child process
        2. Child writes to temp file
        3. Temp file replaces old RDB
        4. Parent continues serving requests
        """
        print(f"  RDB: Creating snapshot to {self.config.filename}")

        snapshot = {
            "version": "REDIS0011",
            "created_at": time.time(),
            "data": data.copy()
        }

        # Simulate compression
        serialized = json.dumps(snapshot)
        if self.config.compression:
            # Simulate gzip compression
            compressed_size = len(serialized) // 3  # Rough estimate
            print(f"  RDB: Compressed {len(serialized)} -> {compressed_size} bytes")

        # Write to file (simulated)
        with open(self.config.filename, 'w') as f:
            f.write(serialized)

        self.last_save_time = time.time()
        self.changes_since_save = 0

        print(f"  RDB: Snapshot saved successfully")
        return True

    def load(self) -> Optional[Dict[str, Any]]:
        """Load data from RDB snapshot."""
        if not os.path.exists(self.config.filename):
            return None

        print(f"  RDB: Loading snapshot from {self.config.filename}")

        with open(self.config.filename, 'r') as f:
            serialized = f.read()

        snapshot = json.loads(serialized)
        print(f"  RDB: Loaded snapshot from {snapshot['created_at']}")

        return snapshot['data']

    def track_change(self):
        """Track a data modification."""
        self.changes_since_save += 1

    def check_auto_save(self) -> bool:
        """Check if auto-save should trigger."""
        elapsed = int(time.time() - self.last_save_time)
        return self.config.should_save(elapsed, self.changes_since_save)

class AOFLog:
    """
    AOF (Append-Only File) Handler.

    AOF logs every write operation.

    Advantages:
    - More durable (less data loss)
    - Log is human-readable
    - Auto-rewrite keeps file compact

    Disadvantages:
    - Larger file sizes
    - Slower restart times
    - More I/O operations
    """

    def __init__(self, config: AOFConfig):
        self.config = config
        self.buffer: List[str] = []
        self.last_fsync = time.time()
        self.file_size = 0

    def append(self, command: str, *args: Any):
        """
        Append command to AOF.

        Redis protocol format (RESP):
        *<num_args>\\r\\n$<len>\\r\\n<arg>\\r\\n...
        """
        # Simplified RESP format
        cmd_parts = [command] + [str(arg) for arg in args]
        serialized = json.dumps(cmd_parts)

        self.buffer.append(serialized + "\\n")
        self.file_size += len(serialized) + 1

        # Check fsync policy
        if self.config.fsync_policy == "always":
            self.fsync()
        elif self.config.fsync_policy == "everysec":
            if time.time() - self.last_fsync >= 1.0:
                self.fsync()

    def fsync(self):
        """
        Flush buffer to disk (fsync).

        fsync policies:
        - always: fsync after every write (safest, slowest)
        - everysec: fsync every second (balanced)
        - no: let OS decide (fastest, least safe)
        """
        if not self.buffer:
            return

        with open(self.config.filename, 'a') as f:
            f.writelines(self.buffer)

        self.buffer.clear()
        self.last_fsync = time.time()

    def replay(self, redis_instance) -> int:
        """
        Replay AOF to restore state.

        Returns: number of commands replayed
        """
        if not os.path.exists(self.config.filename):
            return 0

        print(f"  AOF: Replaying commands from {self.config.filename}")

        count = 0
        with open(self.config.filename, 'r') as f:
            for line in f:
                if line.strip():
                    cmd_parts = json.loads(line.strip())
                    command = cmd_parts[0]
                    args = cmd_parts[1:]

                    # Execute command
                    if command == "SET":
                        redis_instance.data[args[0]] = args[1]
                    elif command == "DEL":
                        redis_instance.data.pop(args[0], None)
                    elif command == "INCR":
                        current = int(redis_instance.data.get(args[0], 0))
                        redis_instance.data[args[0]] = str(current + 1)

                    count += 1

        print(f"  AOF: Replayed {count} commands")
        return count

    def rewrite(self, data: Dict[str, Any]) -> bool:
        """
        AOF Rewrite: Create new AOF from current state.

        Optimization to keep AOF file compact.
        Instead of: INCR counter (1000 times)
        Write: SET counter 1000
        """
        print(f"  AOF: Rewriting {self.config.filename}")

        temp_file = self.config.filename + ".temp"

        # Write current state as SET commands
        with open(temp_file, 'w') as f:
            for key, value in data.items():
                serialized = json.dumps(["SET", key, value]) + "\\n"
                f.write(serialized)

        # Replace old AOF
        if os.path.exists(self.config.filename):
            os.remove(self.config.filename)
        os.rename(temp_file, self.config.filename)

        # Update file size
        self.file_size = os.path.getsize(self.config.filename)

        print(f"  AOF: Rewrite complete, new size: {self.file_size} bytes")
        return True

    def check_auto_rewrite(self, base_size: int) -> bool:
        """Check if auto-rewrite should trigger."""
        if self.file_size < self.config.auto_rewrite_min_size:
            return False

        growth_percentage = ((self.file_size - base_size) / base_size * 100)
        return growth_percentage >= self.config.auto_rewrite_percentage

class PersistentRedis:
    """Redis instance with persistence support."""

    def __init__(self, mode: PersistenceMode = PersistenceMode.BOTH):
        self.data: Dict[str, str] = {}
        self.mode = mode

        # RDB config: save if 60 seconds passed and 100+ changes
        self.rdb = RDBSnapshot(RDBConfig(
            save_intervals=[(60, 100), (300, 10), (900, 1)],
            filename="dump.rdb"
        )) if mode in [PersistenceMode.RDB, PersistenceMode.BOTH] else None

        # AOF config
        self.aof = AOFLog(AOFConfig(
            filename="appendonly.aof",
            fsync_policy="everysec"
        )) if mode in [PersistenceMode.AOF, PersistenceMode.BOTH] else None

        self.aof_base_size = 0

    def set(self, key: str, value: str) -> str:
        """SET with persistence."""
        self.data[key] = value

        # Track change for RDB
        if self.rdb:
            self.rdb.track_change()

        # Append to AOF
        if self.aof:
            self.aof.append("SET", key, value)

        # Check auto-save
        self._check_persistence()

        return "OK"

    def get(self, key: str) -> Optional[str]:
        """GET (read-only, no persistence needed)."""
        return self.data.get(key)

    def incr(self, key: str) -> int:
        """INCR with persistence."""
        current = int(self.data.get(key, 0))
        current += 1
        self.data[key] = str(current)

        if self.rdb:
            self.rdb.track_change()

        if self.aof:
            self.aof.append("INCR", key)

        self._check_persistence()

        return current

    def delete(self, key: str) -> int:
        """DELETE with persistence."""
        if key in self.data:
            del self.data[key]

            if self.rdb:
                self.rdb.track_change()

            if self.aof:
                self.aof.append("DEL", key)

            self._check_persistence()

            return 1
        return 0

    def _check_persistence(self):
        """Check and trigger persistence mechanisms."""
        # RDB auto-save
        if self.rdb and self.rdb.check_auto_save():
            print("\\n[AUTO-SAVE TRIGGERED]")
            self.rdb.save(self.data)

        # AOF fsync
        if self.aof:
            self.aof.fsync()

            # AOF rewrite
            if self.aof.check_auto_rewrite(self.aof_base_size):
                print("\\n[AOF REWRITE TRIGGERED]")
                self.aof.rewrite(self.data)
                self.aof_base_size = self.aof.file_size

    def save(self) -> str:
        """Manual SAVE command."""
        if self.rdb:
            self.rdb.save(self.data)
            return "OK"
        return "ERR RDB not enabled"

    def bgsave(self) -> str:
        """
        Background save (BGSAVE).

        In real Redis, this forks a child process.
        """
        if self.rdb:
            print("Background saving started")
            self.rdb.save(self.data)
            return "Background saving started"
        return "ERR RDB not enabled"

    def bgrewriteaof(self) -> str:
        """Background AOF rewrite."""
        if self.aof:
            print("Background AOF rewrite started")
            self.aof.rewrite(self.data)
            return "Background append only file rewriting started"
        return "ERR AOF not enabled"

    def load_from_disk(self):
        """
        Load data from persistence files.

        Priority: AOF > RDB (AOF is more up-to-date)
        """
        # Try AOF first (more recent)
        if self.aof and os.path.exists(self.aof.config.filename):
            print("Loading from AOF...")
            self.aof.replay(self)
            self.aof_base_size = self.aof.file_size

        # Fallback to RDB
        elif self.rdb and os.path.exists(self.rdb.config.filename):
            print("Loading from RDB...")
            loaded_data = self.rdb.load()
            if loaded_data:
                self.data = loaded_data

        else:
            print("No persistence files found, starting fresh")

# Example 1: RDB Snapshots
print("Example 1: RDB Snapshots")
print("=" * 60)

redis_rdb = PersistentRedis(mode=PersistenceMode.RDB)

print("Writing 150 keys (will trigger auto-save at 100 changes):")
for i in range(150):
    redis_rdb.set(f"key:{i}", f"value{i}")

    if i == 99:
        print(f"  ...at {i+1} changes...")

print(f"\\nTotal keys: {len(redis_rdb.data)}")
print()

# Manual save
print("Manual SAVE:")
redis_rdb.save()
print()

# Example 2: AOF Logging
print("Example 2: AOF Logging")
print("=" * 60)

redis_aof = PersistentRedis(mode=PersistenceMode.AOF)

print("Executing commands (logged to AOF):")
redis_aof.set("user:1000", "alice")
redis_aof.set("user:1001", "bob")
redis_aof.set("counter", "0")

for i in range(5):
    count = redis_aof.incr("counter")
    print(f"  INCR counter -> {count}")

print()

# Example 3: AOF Replay
print("Example 3: AOF Replay (Crash Recovery)")
print("=" * 60)

# Simulate crash and recovery
print("Simulating server crash...")
redis_aof = None  # "Crash"

print("Starting new Redis instance...")
redis_recovered = PersistentRedis(mode=PersistenceMode.AOF)
redis_recovered.load_from_disk()

print("\\nRecovered data:")
print(f"  user:1000 = {redis_recovered.get('user:1000')}")
print(f"  user:1001 = {redis_recovered.get('user:1001')}")
print(f"  counter = {redis_recovered.get('counter')}")
print()

# Example 4: RDB + AOF (Hybrid)
print("Example 4: RDB + AOF Hybrid Mode")
print("=" * 60)

redis_both = PersistentRedis(mode=PersistenceMode.BOTH)

print("Writing data (persisted to both RDB and AOF):")
for i in range(50):
    redis_both.set(f"product:{i}", f"item{i}")

print(f"  Wrote {len(redis_both.data)} keys")
print()

# Force save
print("Manual saves:")
redis_both.save()
redis_both.bgrewriteaof()
print()

# Example 5: Persistence Trade-offs
print("Example 5: Persistence Trade-offs Demonstration")
print("=" * 60)

print("Scenario: 10,000 write operations\\n")

# No persistence
redis_none = PersistentRedis(mode=PersistenceMode.NONE)
start = time.time()
for i in range(10000):
    redis_none.set(f"k:{i}", f"v{i}")
time_none = (time.time() - start) * 1000

# RDB only
redis_rdb2 = PersistentRedis(mode=PersistenceMode.RDB)
redis_rdb2.rdb.config.save_intervals = [(999999, 999999)]  # Disable auto-save
start = time.time()
for i in range(10000):
    redis_rdb2.set(f"k:{i}", f"v{i}")
time_rdb = (time.time() - start) * 1000

# AOF with everysec
redis_aof2 = PersistentRedis(mode=PersistenceMode.AOF)
redis_aof2.aof.config.fsync_policy = "everysec"
start = time.time()
for i in range(10000):
    redis_aof2.set(f"k:{i}", f"v{i}")
time_aof = (time.time() - start) * 1000

print("Performance comparison:")
print(f"  No persistence: {time_none:.1f}ms")
print(f"  RDB only:       {time_rdb:.1f}ms")
print(f"  AOF (everysec): {time_aof:.1f}ms")
print()

print("Data durability:")
print("  No persistence: All data lost on crash")
print("  RDB only:       Data since last snapshot lost")
print("  AOF (everysec): At most 1 second of data lost")
print("  AOF (always):   No data loss (but slowest)")

print()
print("=" * 60)
print("PERSISTENCE BEST PRACTICES")
print("=" * 60)
print("""
RDB (SNAPSHOT) CONFIGURATION:
  Recommended: save 900 1, save 300 10, save 60 10000
  - Every 15 min if 1+ change
  - Every 5 min if 10+ changes
  - Every 1 min if 10,000+ changes

  Pros:
    + Compact single-file backups
    + Faster restarts
    + Lower I/O overhead
    + Good for disaster recovery

  Cons:
    - Data loss between snapshots
    - Fork can pause server (large datasets)
    - Not suitable for strict durability

AOF (APPEND-ONLY FILE) CONFIGURATION:
  fsync policies:
    - always: Every write (slowest, safest)
    - everysec: Every second (recommended)
    - no: OS decides (fastest, risky)

  Pros:
    + More durable
    + Human-readable logs
    + Auto-rewrite optimization

  Cons:
    - Larger file sizes
    - Slower restarts
    - More I/O operations

HYBRID MODE (RDB + AOF):
  Best of both worlds:
  - Use RDB for fast restarts
  - Use AOF for durability
  - Redis loads from AOF (most recent)
  - Keep both files for backup

PRODUCTION RECOMMENDATIONS:
  1. Enable both RDB and AOF
  2. Use AOF with fsync=everysec
  3. Configure auto-rewrite thresholds
  4. Monitor disk I/O and space
  5. Test recovery procedures
  6. Consider Redis Cluster for HA
  7. Use separate disk for persistence
  8. Schedule backups to remote storage

DISASTER RECOVERY:
  - Keep RDB snapshots offsite
  - Test restore procedures regularly
  - Monitor replication lag
  - Use Redis Sentinel for failover
  - Consider Redis Cluster for sharding

Production note: Real Redis provides:
  - Background fork-based saving
  - Incremental RDB snapshots (Redis 7.0+)
  - Mixed RDB-AOF format
  - Diskless replication
  - Point-in-time recovery
  - Crash-safe AOF
""")

# Cleanup
for f in ["dump.rdb", "appendonly.aof", "appendonly.aof.temp"]:
    if os.path.exists(f):
        os.remove(f)
'''

    # Lesson 854: Redis Transactions
    lesson_854 = next(l for l in lessons if l['id'] == 854)
    lesson_854['fullSolution'] = '''# Redis Transactions - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis transactions with MULTI/EXEC/WATCH

from typing import Any, Callable, Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class TransactionState(Enum):
    """Transaction states."""
    IDLE = "idle"
    QUEUED = "queued"
    EXECUTING = "executing"
    ABORTED = "aborted"

@dataclass
class Command:
    """Queued command."""
    name: str
    args: tuple
    func: Callable

class SimulatedRedis:
    """
    Redis simulation with transaction support (MULTI/EXEC/WATCH).

    Redis transactions provide:
    - Atomicity: All or nothing execution
    - Isolation: Commands execute sequentially
    - No rollback: Errors don't undo previous commands
    - Optimistic locking with WATCH
    """

    def __init__(self):
        self.data: Dict[str, str] = {}
        self.tx_state = TransactionState.IDLE
        self.command_queue: List[Command] = []
        self.watched_keys: Dict[str, str] = {}  # key -> value snapshot
        self.tx_aborted = False

    def get(self, key: str) -> Optional[str]:
        """Get value."""
        if self.tx_state == TransactionState.QUEUED:
            self.command_queue.append(Command("GET", (key,), lambda: self.data.get(key)))
            return "QUEUED"

        return self.data.get(key)

    def set(self, key: str, value: str) -> str:
        """Set value."""
        if self.tx_state == TransactionState.QUEUED:
            self.command_queue.append(Command("SET", (key, value), lambda: self._do_set(key, value)))
            return "QUEUED"

        return self._do_set(key, value)

    def _do_set(self, key: str, value: str) -> str:
        """Internal SET implementation."""
        self.data[key] = value
        return "OK"

    def incr(self, key: str) -> Any:
        """Increment value."""
        if self.tx_state == TransactionState.QUEUED:
            self.command_queue.append(Command("INCR", (key,), lambda: self._do_incr(key)))
            return "QUEUED"

        return self._do_incr(key)

    def _do_incr(self, key: str) -> int:
        """Internal INCR implementation."""
        current = int(self.data.get(key, 0))
        current += 1
        self.data[key] = str(current)
        return current

    def decr(self, key: str) -> Any:
        """Decrement value."""
        if self.tx_state == TransactionState.QUEUED:
            self.command_queue.append(Command("DECR", (key,), lambda: self._do_decr(key)))
            return "QUEUED"

        return self._do_decr(key)

    def _do_decr(self, key: str) -> int:
        """Internal DECR implementation."""
        current = int(self.data.get(key, 0))
        current -= 1
        self.data[key] = str(current)
        return current

    def multi(self) -> str:
        """
        Start transaction.

        After MULTI:
        - Commands are queued, not executed
        - Returns "QUEUED" for each command
        - Use EXEC to execute all commands
        """
        if self.tx_state != TransactionState.IDLE:
            raise Exception("ERR MULTI calls can not be nested")

        self.tx_state = TransactionState.QUEUED
        self.command_queue.clear()
        self.tx_aborted = False

        return "OK"

    def exec(self) -> Any:
        """
        Execute transaction.

        Atomically executes all queued commands.

        Returns:
        - List of results if successful
        - None if transaction was aborted (WATCH conflict)
        """
        if self.tx_state != TransactionState.QUEUED:
            raise Exception("ERR EXEC without MULTI")

        # Check if any watched keys were modified
        if self.tx_aborted or self._check_watched_keys_modified():
            print("  Transaction ABORTED (watched key modified)")
            self._reset_transaction()
            return None

        # Execute all commands atomically
        self.tx_state = TransactionState.EXECUTING
        results = []

        for cmd in self.command_queue:
            try:
                result = cmd.func()
                results.append(result)
            except Exception as e:
                # Redis doesn't rollback on errors
                results.append(f"ERR: {str(e)}")

        self._reset_transaction()
        return results

    def discard(self) -> str:
        """Discard transaction."""
        if self.tx_state != TransactionState.QUEUED:
            raise Exception("ERR DISCARD without MULTI")

        self._reset_transaction()
        return "OK"

    def watch(self, *keys: str) -> str:
        """
        Watch keys for optimistic locking.

        If any watched key is modified before EXEC:
        - Transaction is aborted
        - EXEC returns None
        - Client should retry

        This enables check-and-set (CAS) patterns.
        """
        if self.tx_state == TransactionState.QUEUED:
            raise Exception("ERR WATCH inside MULTI is not allowed")

        for key in keys:
            self.watched_keys[key] = self.data.get(key, "__NOTEXIST__")

        return "OK"

    def unwatch(self) -> str:
        """Unwatch all keys."""
        self.watched_keys.clear()
        return "OK"

    def _check_watched_keys_modified(self) -> bool:
        """Check if any watched keys were modified."""
        for key, original_value in self.watched_keys.items():
            current_value = self.data.get(key, "__NOTEXIST__")
            if current_value != original_value:
                return True
        return False

    def _reset_transaction(self):
        """Reset transaction state."""
        self.tx_state = TransactionState.IDLE
        self.command_queue.clear()
        self.watched_keys.clear()
        self.tx_aborted = False

    def modify_key(self, key: str, value: str):
        """Simulate external modification (for testing WATCH)."""
        self.data[key] = value

# Example 1: Basic Transaction (MULTI/EXEC)
print("Example 1: Basic Transaction (MULTI/EXEC)")
print("=" * 60)

redis = SimulatedRedis()
redis.set("balance", "1000")

print("Initial balance:", redis.get("balance"))
print()

print("Starting transaction:")
redis.multi()
print("  MULTI ->", "OK")

# Queue commands
result = redis.incr("balance")
print(f"  INCR balance -> {result}")

result = redis.incr("balance")
print(f"  INCR balance -> {result}")

result = redis.incr("balance")
print(f"  INCR balance -> {result}")

# Execute atomically
print("\\nExecuting transaction:")
results = redis.exec()
print(f"  EXEC -> {results}")

print(f"\\nFinal balance: {redis.get('balance')}")
print()

# Example 2: Transaction Atomicity
print("Example 2: Transaction Atomicity (All or Nothing)")
print("=" * 60)

redis2 = SimulatedRedis()
redis2.set("account:A", "500")
redis2.set("account:B", "300")

print(f"Account A: ${redis2.get('account:A')}")
print(f"Account B: ${redis2.get('account:B')}")
print()

# Transfer $200 from A to B
print("Transfer $200 from A to B (atomic):")
redis2.multi()

# Deduct from A
redis2.decr("account:A")
redis2.decr("account:A")  # Doing this 200 times (simplified to 2 for demo)

# Add to B
redis2.incr("account:B")
redis2.incr("account:B")

results = redis2.exec()
print(f"  Transaction results: {results}")

print(f"\\nAccount A: ${redis2.get('account:A')}")
print(f"Account B: ${redis2.get('account:B')}")
print()

# Example 3: DISCARD Transaction
print("Example 3: DISCARD Transaction")
print("=" * 60)

redis3 = SimulatedRedis()
redis3.set("counter", "10")

print(f"Initial counter: {redis3.get('counter')}")
print()

print("Starting transaction:")
redis3.multi()
redis3.incr("counter")
redis3.incr("counter")
redis3.incr("counter")

print("  Commands queued, but NOT executed yet")
print(f"  Current counter value: {redis3.data.get('counter')}")
print()

print("Discarding transaction:")
redis3.discard()
print(f"  Counter unchanged: {redis3.get('counter')}")
print()

# Example 4: Optimistic Locking with WATCH
print("Example 4: Optimistic Locking with WATCH")
print("=" * 60)

redis4 = SimulatedRedis()
redis4.set("inventory:item:100", "50")

print(f"Initial inventory: {redis4.get('inventory:item:100')} units")
print()

# Transaction 1: Watch inventory, read, calculate, write
print("Transaction 1: Customer wants to buy 5 units")
redis4.watch("inventory:item:100")
print("  WATCH inventory:item:100")

current = int(redis4.get("inventory:item:100"))
print(f"  Current stock: {current}")

if current >= 5:
    new_stock = current - 5
    print(f"  Calculated new stock: {new_stock}")
else:
    print("  Insufficient stock!")

# Simulate concurrent modification BEFORE our transaction executes
print("\\n  [CONCURRENT: Another customer buys 3 units]")
redis4.modify_key("inventory:item:100", "47")
print(f"  Inventory now: {redis4.get('inventory:item:100')}")
print()

# Try to execute our transaction
print("Transaction 1: Attempting to commit...")
redis4.multi()
redis4.set("inventory:item:100", str(new_stock))
result = redis4.exec()

if result is None:
    print("  EXEC -> None (transaction aborted due to WATCH)")
    print("  Must retry with current inventory value")
else:
    print(f"  EXEC -> {result}")

print(f"\\nFinal inventory: {redis4.get('inventory:item:100')} units")
print()

# Example 5: Retry Pattern with WATCH
print("Example 5: Retry Pattern with WATCH (Check-and-Set)")
print("=" * 60)

redis5 = SimulatedRedis()
redis5.set("likes:post:500", "100")

def increment_likes_safe(redis: SimulatedRedis, post_key: str, max_retries: int = 5):
    """
    Safely increment likes with optimistic locking.

    Pattern:
    1. WATCH key
    2. Read current value
    3. MULTI
    4. Set new value
    5. EXEC
    6. If None (conflict), retry
    """
    for attempt in range(max_retries):
        redis.watch(post_key)
        current = int(redis.get(post_key) or 0)
        new_value = current + 1

        redis.multi()
        redis.set(post_key, str(new_value))
        result = redis.exec()

        if result is not None:
            # Success!
            return new_value
        else:
            print(f"  Attempt {attempt + 1}: Conflict detected, retrying...")

    raise Exception("Max retries exceeded")

print(f"Initial likes: {redis5.get('likes:post:500')}")
print()

# Simulate 3 concurrent users liking
print("3 concurrent users clicking 'Like':")
for i in range(3):
    # Simulate some conflict for demonstration
    if i == 1:
        redis5.modify_key("likes:post:500", "102")  # Simulate concurrent update

    new_likes = increment_likes_safe(redis5, "likes:post:500")
    print(f"  User {i+1}: Liked! Total likes: {new_likes}")

print()

# Example 6: Transaction vs Pipeline
print("Example 6: Transaction vs Pipeline")
print("=" * 60)

redis6 = SimulatedRedis()

print("PIPELINE (no atomicity guarantee):")
print("  - Batches commands to reduce RTT")
print("  - Commands may interleave with other clients")
print("  - Used for performance")
print()

print("TRANSACTION (atomicity guarantee):")
print("  - All commands execute atomically")
print("  - No other client can execute between commands")
print("  - Used for consistency")
print()

redis6.multi()
redis6.set("tx:key1", "value1")
redis6.set("tx:key2", "value2")
redis6.set("tx:key3", "value3")
results = redis6.exec()

print(f"Transaction results: {results}")
print("All 3 SETs executed atomically")

print()
print("=" * 60)
print("REDIS TRANSACTIONS BEST PRACTICES")
print("=" * 60)
print("""
MULTI/EXEC BASICS:
  - MULTI starts transaction (commands queued)
  - EXEC executes all commands atomically
  - DISCARD cancels transaction
  - Commands return "QUEUED" until EXEC

IMPORTANT DIFFERENCES FROM SQL:
  ✗ NO ROLLBACK: Errors don't undo previous commands
  ✗ NO NESTED TRANSACTIONS: Can't nest MULTI
  ✓ ATOMIC: All commands execute sequentially
  ✓ ISOLATED: No interleaving with other clients

WATCH FOR OPTIMISTIC LOCKING:
  Pattern (Check-and-Set):
    1. WATCH key(s)
    2. Read current value
    3. Calculate new value
    4. MULTI
    5. SET new value
    6. EXEC (returns None if conflict)
    7. Retry if None

  Use cases:
    - Inventory management
    - Like counters with race conditions
    - Account balance transfers
    - Any read-modify-write operation

WHEN TO USE TRANSACTIONS:
  ✓ Multiple related updates must be atomic
  ✓ Read-modify-write patterns (with WATCH)
  ✓ Preventing race conditions
  ✓ Ensuring consistency

WHEN NOT TO USE TRANSACTIONS:
  ✗ Single command (already atomic)
  ✗ Just batching for performance (use pipeline)
  ✗ Need rollback (use Lua script instead)
  ✗ Complex conditional logic (use Lua script)

COMMON PATTERNS:
  1. Account Transfer:
     WATCH account:A account:B
     MULTI
     DECRBY account:A 100
     INCRBY account:B 100
     EXEC

  2. Inventory Update:
     WATCH inventory:item:123
     current = GET inventory:item:123
     if current >= quantity:
         MULTI
         DECRBY inventory:item:123 quantity
         EXEC

  3. Counter with Limit:
     WATCH counter
     current = GET counter
     if current < MAX:
         MULTI
         INCR counter
         EXEC

TRANSACTION vs LUA SCRIPT:
  Transaction:
    + Simple check-and-set
    + Client-side logic
    - Multiple round trips

  Lua Script:
    + Single round trip
    + Complex logic
    + Guaranteed atomic
    - Must be pre-loaded

PERFORMANCE CONSIDERATIONS:
  - Transactions block other clients briefly
  - WATCH failures require retries (backoff recommended)
  - Large transactions increase latency
  - Consider Lua scripts for complex atomicity

Production note: Real Redis provides:
  - Full ACID properties for transactions
  - Integration with clustering (single-slot limit)
  - WATCH works across connections
  - Transaction pipelining optimization
  - Automatic UNWATCH after EXEC/DISCARD
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 12 COMPLETE: Redis Data Structures, Persistence & Transactions")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 851: Redis Data Structures")
    print(f"  - Lesson 855: Redis Persistence")
    print(f"  - Lesson 854: Redis Transactions")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
