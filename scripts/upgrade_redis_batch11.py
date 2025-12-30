#!/usr/bin/env python3
"""
Upgrade Redis lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 11: Redis Lua Scripting, Cluster, and Pipelining
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 858: Redis Lua Scripting
    lesson_858 = next(l for l in lessons if l['id'] == 858)
    lesson_858['fullSolution'] = '''# Redis Lua Scripting - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis Lua scripting for atomic operations

import hashlib
import time
import json
from typing import Any, Dict, List, Optional, Tuple

class LuaScript:
    """Simulated Redis Lua script with SHA1 hash."""

    def __init__(self, script: str, redis_client):
        self.script = script
        self.redis = redis_client
        self.sha = hashlib.sha1(script.encode()).hexdigest()

    def __call__(self, keys: List[str] = None, args: List[Any] = None):
        """Execute the Lua script."""
        keys = keys or []
        args = args or []
        return self.redis.evalsha(self.sha, len(keys), keys, args)

class SimulatedRedis:
    """Complete Redis simulation with Lua scripting support."""

    def __init__(self):
        self.data = {}
        self.scripts = {}  # SHA -> script
        self.expires = {}

    def get(self, key: str) -> Optional[str]:
        """Get value by key."""
        if key in self.expires and time.time() > self.expires[key]:
            del self.data[key]
            del self.expires[key]
            return None
        return self.data.get(key)

    def set(self, key: str, value: Any, ex: Optional[int] = None) -> str:
        """Set key to value."""
        self.data[key] = str(value)
        if ex:
            self.expires[key] = time.time() + ex
        return "OK"

    def incr(self, key: str) -> int:
        """Increment value."""
        current = int(self.data.get(key, 0))
        current += 1
        self.data[key] = str(current)
        return current

    def decr(self, key: str) -> int:
        """Decrement value."""
        current = int(self.data.get(key, 0))
        current -= 1
        self.data[key] = str(current)
        return current

    def exists(self, key: str) -> int:
        """Check if key exists."""
        return 1 if key in self.data else 0

    def delete(self, *keys: str) -> int:
        """Delete keys."""
        count = 0
        for key in keys:
            if key in self.data:
                del self.data[key]
                count += 1
        return count

    def lpush(self, key: str, *values: str) -> int:
        """Push to list."""
        if key not in self.data:
            self.data[key] = []
        for value in reversed(values):
            self.data[key].insert(0, value)
        return len(self.data[key])

    def lrange(self, key: str, start: int, end: int) -> List[str]:
        """Get list range."""
        if key not in self.data:
            return []
        lst = self.data[key]
        if end == -1:
            return lst[start:]
        return lst[start:end+1]

    def zadd(self, key: str, mapping: Dict[str, float]) -> int:
        """Add to sorted set."""
        if key not in self.data:
            self.data[key] = {}
        count = 0
        for member, score in mapping.items():
            if member not in self.data[key]:
                count += 1
            self.data[key][member] = score
        return count

    def zrange(self, key: str, start: int, end: int, withscores: bool = False) -> List:
        """Get sorted set range."""
        if key not in self.data:
            return []

        sorted_items = sorted(self.data[key].items(), key=lambda x: x[1])
        if end == -1:
            items = sorted_items[start:]
        else:
            items = sorted_items[start:end+1]

        if withscores:
            return [(member, score) for member, score in items]
        return [member for member, score in items]

    def zscore(self, key: str, member: str) -> Optional[float]:
        """Get score of member in sorted set."""
        if key not in self.data or member not in self.data[key]:
            return None
        return self.data[key][member]

    def register_script(self, script: str) -> LuaScript:
        """Register a Lua script."""
        lua_script = LuaScript(script, self)
        self.scripts[lua_script.sha] = script
        return lua_script

    def evalsha(self, sha: str, numkeys: int, keys: List[str], args: List[Any]) -> Any:
        """Execute Lua script by SHA."""
        if sha not in self.scripts:
            raise Exception(f"NOSCRIPT: No matching script. SHA: {sha}")

        script = self.scripts[sha]
        return self._execute_lua(script, keys, args)

    def _execute_lua(self, script: str, keys: List[str], args: List[Any]) -> Any:
        """
        Execute Lua script simulation.
        This is a simplified interpreter for common Redis Lua patterns.
        """
        # Parse script to determine operation

        # Pattern 1: Rate limiting with sliding window
        if "redis.call('ZREMRANGEBYSCORE'" in script and "redis.call('ZADD'" in script:
            return self._lua_rate_limit(keys, args)

        # Pattern 2: Atomic increment with max limit
        if "redis.call('GET'" in script and "redis.call('INCR'" in script and "return 0" in script:
            return self._lua_limited_incr(keys, args)

        # Pattern 3: Compare and set (CAS)
        if "redis.call('GET'" in script and "redis.call('SET'" in script and "return 0" in script:
            return self._lua_compare_and_set(keys, args)

        # Pattern 4: Multi-key atomic operation
        if "for" in script and "redis.call" in script:
            return self._lua_multi_operation(keys, args, script)

        # Default: simple operation
        return None

    def _lua_rate_limit(self, keys: List[str], args: List[Any]) -> int:
        """Rate limiting with sliding window."""
        key = keys[0]
        current_time = float(args[0])
        window = int(args[1])
        limit = int(args[2])

        # Remove old entries
        if key not in self.data:
            self.data[key] = {}

        cutoff = current_time - window
        to_remove = [member for member, score in self.data[key].items() if score < cutoff]
        for member in to_remove:
            del self.data[key][member]

        # Check current count
        current_count = len(self.data[key])

        if current_count < limit:
            # Add new entry
            self.data[key][str(current_time)] = current_time
            return 1
        else:
            return 0

    def _lua_limited_incr(self, keys: List[str], args: List[Any]) -> int:
        """Increment with maximum limit."""
        key = keys[0]
        max_value = int(args[0])

        current = int(self.data.get(key, 0))

        if current >= max_value:
            return 0
        else:
            current += 1
            self.data[key] = str(current)
            return 1

    def _lua_compare_and_set(self, keys: List[str], args: List[Any]) -> int:
        """Compare and set operation."""
        key = keys[0]
        expected = str(args[0])
        new_value = str(args[1])

        current = self.data.get(key)

        if current == expected:
            self.data[key] = new_value
            return 1
        else:
            return 0

    def _lua_multi_operation(self, keys: List[str], args: List[Any], script: str) -> Any:
        """Handle multi-key operations."""
        # Simplified: transfer value between keys
        if "INCRBY" in script and len(keys) >= 2:
            source_key = keys[0]
            dest_key = keys[1]
            amount = int(args[0]) if args else 1

            source_val = int(self.data.get(source_key, 0))
            if source_val >= amount:
                self.data[source_key] = str(source_val - amount)
                dest_val = int(self.data.get(dest_key, 0))
                self.data[dest_key] = str(dest_val + amount)
                return 1
            return 0

        return None

# Example 1: Rate Limiting with Sliding Window
print("Example 1: Rate Limiting with Sliding Window")
print("=" * 60)

redis = SimulatedRedis()

# Lua script for rate limiting
rate_limit_script = """
local key = KEYS[1]
local current_time = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])

-- Remove old entries outside the window
redis.call('ZREMRANGEBYSCORE', key, 0, current_time - window)

-- Get current count
local current = redis.call('ZCARD', key)

if current < limit then
    -- Add new entry
    redis.call('ZADD', key, current_time, current_time)
    return 1
else
    return 0
end
"""

rate_limiter = redis.register_script(rate_limit_script)

# Simulate API rate limiting (10 requests per 60 seconds)
user_key = "rate_limit:user:123"
current_time = time.time()
window_seconds = 60
max_requests = 10

print(f"Rate Limit: {max_requests} requests per {window_seconds} seconds")
print()

# Simulate 15 requests
for i in range(15):
    allowed = rate_limiter(
        keys=[user_key],
        args=[current_time + i * 0.1, window_seconds, max_requests]
    )

    status = "ALLOWED" if allowed else "BLOCKED"
    print(f"Request {i+1:2d}: {status}")

    if i == 9:
        print("  ^ Reached limit")

print()

# Example 2: Atomic Increment with Maximum
print("Example 2: Atomic Increment with Maximum")
print("=" * 60)

limited_incr_script = """
local key = KEYS[1]
local max = tonumber(ARGV[1])

local current = redis.call('GET', key)
if not current then
    current = 0
else
    current = tonumber(current)
end

if current >= max then
    return 0
else
    redis.call('INCR', key)
    return 1
end
"""

redis2 = SimulatedRedis()
limited_incr = redis2.register_script(limited_incr_script)

# Inventory management - limited stock
product_key = "inventory:product:456"
max_stock = 5

print(f"Maximum stock: {max_stock}")
print()

# Try to add 8 items (should stop at 5)
for i in range(8):
    success = limited_incr(keys=[product_key], args=[max_stock])
    current_stock = redis2.get(product_key) or "0"

    status = "SUCCESS" if success else "FAILED (at max)"
    print(f"Add item {i+1}: {status} | Stock: {current_stock}")

print()

# Example 3: Compare and Set (Optimistic Locking)
print("Example 3: Compare and Set (Optimistic Locking)")
print("=" * 60)

cas_script = """
local key = KEYS[1]
local expected = ARGV[1]
local new_value = ARGV[2]

local current = redis.call('GET', key)

if current == expected then
    redis.call('SET', key, new_value)
    return 1
else
    return 0
end
"""

redis3 = SimulatedRedis()
compare_and_set = redis3.register_script(cas_script)

# Account balance updates with optimistic locking
account_key = "account:balance:789"
redis3.set(account_key, "1000")

print("Initial balance: $1000")
print()

# Scenario: Two concurrent transactions
print("Transaction 1: Read balance")
balance_t1 = redis3.get(account_key)
print(f"  T1 sees: ${balance_t1}")

print("Transaction 2: Read balance")
balance_t2 = redis3.get(account_key)
print(f"  T2 sees: ${balance_t2}")
print()

# T1 tries to update (withdraw $100)
print("Transaction 1: Withdraw $100")
new_balance_t1 = str(int(balance_t1) - 100)
success_t1 = compare_and_set(
    keys=[account_key],
    args=[balance_t1, new_balance_t1]
)
print(f"  Result: {'SUCCESS' if success_t1 else 'FAILED'}")
print(f"  Balance: ${redis3.get(account_key)}")
print()

# T2 tries to update (withdraw $50) - should fail because balance changed
print("Transaction 2: Withdraw $50")
new_balance_t2 = str(int(balance_t2) - 50)
success_t2 = compare_and_set(
    keys=[account_key],
    args=[balance_t2, new_balance_t2]
)
print(f"  Result: {'SUCCESS' if success_t2 else 'FAILED (balance changed)'}")
print(f"  Balance: ${redis3.get(account_key)}")
print()

# T2 retries with current value
print("Transaction 2: Retry with current balance")
balance_t2_retry = redis3.get(account_key)
new_balance_t2_retry = str(int(balance_t2_retry) - 50)
success_t2_retry = compare_and_set(
    keys=[account_key],
    args=[balance_t2_retry, new_balance_t2_retry]
)
print(f"  Result: {'SUCCESS' if success_t2_retry else 'FAILED'}")
print(f"  Final balance: ${redis3.get(account_key)}")
print()

# Example 4: Multi-Key Atomic Transfer
print("Example 4: Multi-Key Atomic Transfer")
print("=" * 60)

transfer_script = """
local from_key = KEYS[1]
local to_key = KEYS[2]
local amount = tonumber(ARGV[1])

local from_balance = redis.call('GET', from_key)
if not from_balance then
    from_balance = 0
else
    from_balance = tonumber(from_balance)
end

if from_balance >= amount then
    redis.call('DECRBY', from_key, amount)
    redis.call('INCRBY', to_key, amount)
    return 1
else
    return 0
end
"""

redis4 = SimulatedRedis()
atomic_transfer = redis4.register_script(transfer_script)

# Setup accounts
alice_key = "balance:alice"
bob_key = "balance:bob"
redis4.set(alice_key, "500")
redis4.set(bob_key, "300")

print(f"Alice balance: ${redis4.get(alice_key)}")
print(f"Bob balance:   ${redis4.get(bob_key)}")
print()

# Transfer $200 from Alice to Bob
print("Transfer $200 from Alice to Bob")
success = atomic_transfer(
    keys=[alice_key, bob_key],
    args=[200]
)
print(f"Result: {'SUCCESS' if success else 'FAILED'}")
print(f"Alice balance: ${redis4.get(alice_key)}")
print(f"Bob balance:   ${redis4.get(bob_key)}")
print()

# Try to transfer $400 (should fail - insufficient funds)
print("Transfer $400 from Alice to Bob")
success = atomic_transfer(
    keys=[alice_key, bob_key],
    args=[400]
)
print(f"Result: {'SUCCESS' if success else 'FAILED (insufficient funds)'}")
print(f"Alice balance: ${redis4.get(alice_key)}")
print(f"Bob balance:   ${redis4.get(bob_key)}")
print()

# Example 5: Leaderboard with Score Update
print("Example 5: Leaderboard with Score Update")
print("=" * 60)

leaderboard_update_script = """
local key = KEYS[1]
local player = ARGV[1]
local score_delta = tonumber(ARGV[2])

local current_score = redis.call('ZSCORE', key, player)
if not current_score then
    current_score = 0
else
    current_score = tonumber(current_score)
end

local new_score = current_score + score_delta
redis.call('ZADD', key, new_score, player)

return new_score
"""

redis5 = SimulatedRedis()
update_leaderboard = redis5.register_script(leaderboard_update_script)

leaderboard_key = "leaderboard:game:combat"

# Initial scores
redis5.zadd(leaderboard_key, {"Alice": 1000, "Bob": 850, "Charlie": 920})

print("Initial Leaderboard:")
for rank, (player, score) in enumerate(redis5.zrange(leaderboard_key, 0, -1, withscores=True), 1):
    print(f"  {rank}. {player}: {int(score)} points")
print()

# Game events - update scores atomically
print("Game Events:")
events = [
    ("Alice", 150, "kills dragon"),
    ("Bob", 200, "completes quest"),
    ("Charlie", -50, "defeated in battle"),
    ("Alice", 75, "finds treasure"),
]

for player, score_change, event in events:
    new_score = update_leaderboard(
        keys=[leaderboard_key],
        args=[player, score_change]
    )
    sign = "+" if score_change > 0 else ""
    print(f"  {player} {event}: {sign}{score_change} points -> {int(new_score)} total")

print()
print("Final Leaderboard:")
for rank, (player, score) in enumerate(redis5.zrange(leaderboard_key, 0, -1, withscores=True), 1):
    print(f"  {rank}. {player}: {int(score)} points")

print()
print("=" * 60)
print("BEST PRACTICES FOR LUA SCRIPTING")
print("=" * 60)
print("""
1. ATOMICITY
   - All Redis commands in a Lua script execute atomically
   - No other client can execute commands during script execution
   - Perfect for complex operations requiring consistency

2. SCRIPT CACHING
   - Use SCRIPT LOAD to pre-load scripts
   - Execute with EVALSHA instead of EVAL to save bandwidth
   - Scripts are cached by SHA1 hash

3. PERFORMANCE CONSIDERATIONS
   - Keep scripts short and fast
   - Avoid loops over large datasets
   - Use built-in Redis commands when possible
   - Scripts block the server while executing

4. COMMON USE CASES
   - Rate limiting with sliding windows
   - Optimistic locking (compare-and-set)
   - Multi-key atomic operations
   - Complex scoring and ranking logic
   - Conditional updates based on current state

5. KEYS AND ARGV
   - Pass key names in KEYS array (for cluster compatibility)
   - Pass arguments in ARGV array
   - Access in Lua: KEYS[1], ARGV[1] (1-indexed)

6. DEBUGGING
   - Use redis.log() for debugging
   - Test scripts thoroughly before production
   - Handle nil values carefully
   - Return meaningful values for error handling

Production note: Real Redis Lua scripting provides:
- Full Lua 5.1 interpreter
- Rich standard library
- Advanced data structure manipulation
- Integration with Redis replication
- Support for Redis Cluster
""")
'''

    # Lesson 856: Redis Cluster
    lesson_856 = next(l for l in lessons if l['id'] == 856)
    lesson_856['fullSolution'] = '''# Redis Cluster - Complete Simulation
# In production: pip install redis-py-cluster
# This lesson simulates Redis Cluster for horizontal scaling and high availability

import hashlib
import random
from typing import Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class NodeState(Enum):
    """Redis Cluster node states."""
    ONLINE = "online"
    OFFLINE = "offline"
    FAIL = "fail"
    HANDSHAKE = "handshake"

@dataclass
class SlotRange:
    """Hash slot range."""
    start: int
    end: int

    def contains(self, slot: int) -> bool:
        return self.start <= slot <= self.end

    def __repr__(self):
        return f"{self.start}-{self.end}"

@dataclass
class ClusterNode:
    """Represents a Redis Cluster node."""
    node_id: str
    host: str
    port: int
    role: str  # "master" or "replica"
    master_id: Optional[str] = None
    slots: List[SlotRange] = None
    state: NodeState = NodeState.ONLINE

    def __post_init__(self):
        if self.slots is None:
            self.slots = []
        self.data = {}  # Simulated Redis data

    def get(self, key: str) -> Optional[str]:
        """Get value from this node."""
        return self.data.get(key)

    def set(self, key: str, value: str) -> str:
        """Set value on this node."""
        self.data[key] = value
        return "OK"

    def delete(self, key: str) -> int:
        """Delete key from this node."""
        if key in self.data:
            del self.data[key]
            return 1
        return 0

    def keys(self) -> List[str]:
        """Get all keys on this node."""
        return list(self.data.keys())

    def owns_slot(self, slot: int) -> bool:
        """Check if this node owns a hash slot."""
        return any(slot_range.contains(slot) for slot_range in self.slots)

class RedisCluster:
    """
    Simulated Redis Cluster with hash slot distribution.

    Redis Cluster uses 16384 hash slots distributed across master nodes.
    Each key is mapped to a slot using CRC16, enabling:
    - Automatic sharding
    - Client-side routing
    - Resharding without downtime
    - High availability with replicas
    """

    HASH_SLOTS = 16384

    def __init__(self):
        self.nodes: Dict[str, ClusterNode] = {}
        self.slot_map: Dict[int, str] = {}  # slot -> node_id

    def add_node(self, node: ClusterNode) -> None:
        """Add a node to the cluster."""
        self.nodes[node.node_id] = node

        # Update slot mappings for master nodes
        if node.role == "master":
            for slot_range in node.slots:
                for slot in range(slot_range.start, slot_range.end + 1):
                    self.slot_map[slot] = node.node_id

    def crc16(self, key: str) -> int:
        """
        Calculate CRC16 hash for a key (simplified version).
        Real Redis uses CRC16-CCITT.
        """
        # Simplified hash for simulation
        hash_val = 0
        for char in key:
            hash_val = ((hash_val << 5) + hash_val) + ord(char)
        return hash_val & 0xFFFF

    def key_slot(self, key: str) -> int:
        """
        Calculate hash slot for a key.

        Hash tags: {user:1000}.profile -> hashes only "user:1000"
        This ensures related keys map to the same slot.
        """
        # Check for hash tag
        start = key.find('{')
        if start != -1:
            end = key.find('}', start + 1)
            if end != -1 and end > start + 1:
                key = key[start + 1:end]

        return self.crc16(key) % self.HASH_SLOTS

    def get_node_for_key(self, key: str) -> ClusterNode:
        """Get the master node responsible for a key."""
        slot = self.key_slot(key)
        node_id = self.slot_map.get(slot)

        if not node_id:
            raise Exception(f"CLUSTERDOWN: No node owns slot {slot}")

        node = self.nodes[node_id]

        if node.state != NodeState.ONLINE:
            # Try replica failover
            replica = self._get_replica_for_master(node_id)
            if replica and replica.state == NodeState.ONLINE:
                return replica
            raise Exception(f"CLUSTERDOWN: Node {node_id} is {node.state.value}")

        return node

    def _get_replica_for_master(self, master_id: str) -> Optional[ClusterNode]:
        """Find a replica for a master node."""
        for node in self.nodes.values():
            if node.role == "replica" and node.master_id == master_id:
                return node
        return None

    def get(self, key: str) -> Optional[str]:
        """Get value for a key (routed to correct node)."""
        node = self.get_node_for_key(key)
        return node.get(key)

    def set(self, key: str, value: str) -> str:
        """Set value for a key (routed to correct node)."""
        node = self.get_node_for_key(key)
        result = node.set(key, value)

        # Replicate to replicas
        if node.role == "master":
            for replica_node in self.nodes.values():
                if replica_node.role == "replica" and replica_node.master_id == node.node_id:
                    replica_node.set(key, value)

        return result

    def delete(self, key: str) -> int:
        """Delete a key (routed to correct node)."""
        node = self.get_node_for_key(key)
        result = node.delete(key)

        # Replicate to replicas
        if node.role == "master":
            for replica_node in self.nodes.values():
                if replica_node.role == "replica" and replica_node.master_id == node.node_id:
                    replica_node.delete(key)

        return result

    def cluster_info(self) -> Dict:
        """Get cluster information."""
        total_keys = sum(len(node.data) for node in self.nodes.values() if node.role == "master")
        online_nodes = sum(1 for node in self.nodes.values() if node.state == NodeState.ONLINE)

        return {
            "state": "ok" if all(node.state == NodeState.ONLINE for node in self.nodes.values()) else "fail",
            "slots_assigned": len(self.slot_map),
            "slots_ok": len(self.slot_map),
            "slots_pfail": 0,
            "slots_fail": 0,
            "known_nodes": len(self.nodes),
            "online_nodes": online_nodes,
            "total_keys": total_keys
        }

    def cluster_nodes(self) -> List[Dict]:
        """Get information about all cluster nodes."""
        nodes_info = []
        for node in self.nodes.values():
            slots_str = ",".join(str(sr) for sr in node.slots)
            nodes_info.append({
                "id": node.node_id,
                "address": f"{node.host}:{node.port}",
                "role": node.role,
                "master_id": node.master_id or "-",
                "state": node.state.value,
                "slots": slots_str,
                "keys": len(node.data)
            })
        return nodes_info

    def failover(self, master_id: str) -> bool:
        """
        Simulate failover: promote replica to master.

        In real Redis Cluster:
        1. Replica detects master failure
        2. Replica requests votes from other masters
        3. With majority votes, replica promotes itself
        4. Cluster updates routing table
        """
        master = self.nodes.get(master_id)
        if not master or master.role != "master":
            return False

        # Find a replica
        replica = self._get_replica_for_master(master_id)
        if not replica:
            return False

        print(f"  FAILOVER: Promoting {replica.node_id} to master")

        # Mark master as failed
        master.state = NodeState.FAIL

        # Promote replica
        replica.role = "master"
        replica.slots = master.slots
        replica.master_id = None

        # Update slot mappings
        for slot_range in replica.slots:
            for slot in range(slot_range.start, slot_range.end + 1):
                self.slot_map[slot] = replica.node_id

        return True

    def reshard(self, source_node_id: str, target_node_id: str, num_slots: int) -> bool:
        """
        Simulate resharding: move slots from one node to another.

        In real Redis Cluster:
        1. Mark slots as migrating/importing
        2. Migrate keys one by one
        3. Update cluster configuration
        4. Clients get MOVED redirections
        """
        source = self.nodes.get(source_node_id)
        target = self.nodes.get(target_node_id)

        if not source or not target:
            return False

        if source.role != "master" or target.role != "master":
            return False

        # Get slots to move
        slots_to_move = []
        for slot_range in source.slots:
            for slot in range(slot_range.start, min(slot_range.end + 1, slot_range.start + num_slots)):
                slots_to_move.append(slot)
                if len(slots_to_move) >= num_slots:
                    break
            if len(slots_to_move) >= num_slots:
                break

        print(f"  RESHARD: Moving {len(slots_to_move)} slots from {source_node_id} to {target_node_id}")

        # Move keys
        keys_moved = 0
        for slot in slots_to_move:
            # Find keys in this slot
            keys_in_slot = [k for k in source.keys() if self.key_slot(k) == slot]

            for key in keys_in_slot:
                value = source.get(key)
                target.set(key, value)
                source.delete(key)
                keys_moved += 1

            # Update slot mapping
            self.slot_map[slot] = target_node_id

        # Update source node slot ranges
        new_ranges = []
        for slot_range in source.slots:
            if not any(slot_range.contains(s) for s in slots_to_move):
                new_ranges.append(slot_range)
        source.slots = new_ranges

        # Update target node slot ranges
        if slots_to_move:
            target.slots.append(SlotRange(min(slots_to_move), max(slots_to_move)))

        print(f"  Moved {keys_moved} keys")
        return True

# Example 1: Creating a Redis Cluster
print("Example 1: Creating a Redis Cluster")
print("=" * 60)

cluster = RedisCluster()

# Create 3 master nodes with slot distribution
master1 = ClusterNode(
    node_id="node1",
    host="127.0.0.1",
    port=7000,
    role="master",
    slots=[SlotRange(0, 5460)]
)

master2 = ClusterNode(
    node_id="node2",
    host="127.0.0.1",
    port=7001,
    role="master",
    slots=[SlotRange(5461, 10922)]
)

master3 = ClusterNode(
    node_id="node3",
    host="127.0.0.1",
    port=7002,
    role="master",
    slots=[SlotRange(10923, 16383)]
)

# Create replica nodes
replica1 = ClusterNode(
    node_id="node4",
    host="127.0.0.1",
    port=7003,
    role="replica",
    master_id="node1"
)

replica2 = ClusterNode(
    node_id="node5",
    host="127.0.0.1",
    port=7004,
    role="replica",
    master_id="node2"
)

replica3 = ClusterNode(
    node_id="node6",
    host="127.0.0.1",
    port=7005,
    role="replica",
    master_id="node3"
)

# Add all nodes to cluster
for node in [master1, master2, master3, replica1, replica2, replica3]:
    cluster.add_node(node)

print("Cluster created with 3 masters + 3 replicas")
print()

# Display cluster nodes
print("Cluster Nodes:")
for node_info in cluster.cluster_nodes():
    role_icon = "M" if node_info["role"] == "master" else "R"
    print(f"  [{role_icon}] {node_info['id']} @ {node_info['address']}")
    if node_info["role"] == "master":
        print(f"      Slots: {node_info['slots']}")
    else:
        print(f"      Replicates: {node_info['master_id']}")

print()

# Example 2: Key Distribution with Hash Slots
print("Example 2: Key Distribution with Hash Slots")
print("=" * 60)

# Set keys - automatically routed to correct nodes
test_keys = [
    "user:1000",
    "user:1001",
    "user:1002",
    "session:abc123",
    "session:def456",
    "product:5001",
    "product:5002",
    "cart:user:1000",
]

print("Writing keys to cluster:")
for key in test_keys:
    cluster.set(key, f"value_{key}")
    slot = cluster.key_slot(key)
    node = cluster.get_node_for_key(key)
    print(f"  {key:20s} -> slot {slot:5d} -> {node.node_id}")

print()

# Show key distribution
print("Key distribution across nodes:")
for node_info in cluster.cluster_nodes():
    if node_info["role"] == "master":
        print(f"  {node_info['id']}: {node_info['keys']} keys")

print()

# Example 3: Hash Tags for Multi-Key Operations
print("Example 3: Hash Tags for Multi-Key Operations")
print("=" * 60)

# Hash tags ensure related keys map to the same slot
user_id = "1000"
user_keys = [
    f"{{user:{user_id}}}:profile",
    f"{{user:{user_id}}}:settings",
    f"{{user:{user_id}}}:preferences",
]

print(f"Using hash tag {{user:{user_id}}} to colocate keys:")
slots = set()
for key in user_keys:
    cluster.set(key, f"data_{key}")
    slot = cluster.key_slot(key)
    slots.add(slot)
    node = cluster.get_node_for_key(key)
    print(f"  {key:35s} -> slot {slot:5d} -> {node.node_id}")

print(f"\nAll keys map to {len(slots)} slot(s) - enabling multi-key operations!")
print()

# Example 4: Automatic Failover
print("Example 4: Automatic Failover")
print("=" * 60)

print("Cluster status BEFORE failover:")
info = cluster.cluster_info()
print(f"  State: {info['state']}")
print(f"  Online nodes: {info['online_nodes']}/{info['known_nodes']}")
print()

# Simulate master1 failure
print(f"Simulating failure of {master1.node_id}...")
master1.state = NodeState.FAIL
print()

# Perform failover
print("Initiating failover...")
success = cluster.failover("node1")
print(f"Failover: {'SUCCESS' if success else 'FAILED'}")
print()

print("Cluster status AFTER failover:")
for node_info in cluster.cluster_nodes():
    if node_info['id'] in ['node1', 'node4']:
        role_marker = "M" if node_info["role"] == "master" else "R"
        state_marker = "UP" if node_info["state"] == "online" else "DOWN"
        print(f"  [{role_marker}] {node_info['id']}: {state_marker}")
        if node_info["role"] == "master":
            print(f"      Now serving slots: {node_info['slots']}")

print()

# Keys are still accessible via promoted replica
test_key = "user:1000"
try:
    value = cluster.get(test_key)
    print(f"Key '{test_key}' still accessible: {value}")
except Exception as e:
    print(f"Error: {e}")

print()

# Example 5: Resharding
print("Example 5: Resharding (Moving Slots)")
print("=" * 60)

# Create fresh cluster for resharding example
cluster2 = RedisCluster()

m1 = ClusterNode("m1", "127.0.0.1", 8000, "master", slots=[SlotRange(0, 8191)])
m2 = ClusterNode("m2", "127.0.0.1", 8001, "master", slots=[SlotRange(8192, 16383)])

cluster2.add_node(m1)
cluster2.add_node(m2)

# Add some test data
for i in range(20):
    key = f"key:{i}"
    cluster2.set(key, f"value{i}")

print("Initial distribution:")
print(f"  m1 (slots 0-8191):     {len(m1.data)} keys")
print(f"  m2 (slots 8192-16383): {len(m2.data)} keys")
print()

# Reshard 1000 slots from m1 to m2
print("Resharding 1000 slots from m1 to m2...")
cluster2.reshard("m1", "m2", 1000)
print()

print("Distribution after resharding:")
print(f"  m1 (reduced slots):    {len(m1.data)} keys")
print(f"  m2 (increased slots):  {len(m2.data)} keys")

print()
print("=" * 60)
print("REDIS CLUSTER BEST PRACTICES")
print("=" * 60)
print("""
1. CLUSTER DESIGN
   - Minimum 3 master nodes (for quorum)
   - At least 1 replica per master (high availability)
   - Odd number of masters (easier quorum)
   - Plan for 1000+ slots per node

2. HASH TAGS
   - Use {tag} for multi-key operations
   - Example: {user:1000}:profile, {user:1000}:cart
   - All keys with same tag map to same slot
   - Required for MULTI/EXEC transactions

3. FAILOVER
   - Automatic failover with replica promotion
   - Requires majority vote (quorum)
   - Configure cluster-node-timeout
   - Monitor cluster health continuously

4. RESHARDING
   - Add/remove nodes without downtime
   - Move slots in small batches
   - Use redis-cli --cluster reshard
   - Monitor key migration progress

5. CLIENT-SIDE ROUTING
   - Clients cache slot mappings
   - Handle MOVED and ASK redirections
   - Use cluster-aware client libraries
   - Refresh topology on CLUSTER DOWN

6. LIMITATIONS
   - No multi-key ops across slots
   - No SELECT (single database)
   - Pub/Sub is global across cluster
   - Lua scripts limited to single slot

7. MONITORING
   - Track slot coverage
   - Monitor node health
   - Watch for failing nodes
   - Alert on cluster_state != ok

Production note: Real Redis Cluster provides:
- Gossip protocol for node communication
- Automatic partition detection
- Manual and automatic resharding
- MOVED/ASK client redirections
- Up to 1000 nodes in cluster
""")
'''

    # Lesson 857: Redis Pipelining
    lesson_857 = next(l for l in lessons if l['id'] == 857)
    lesson_857['fullSolution'] = '''# Redis Pipelining - Complete Simulation
# In production: pip install redis
# This lesson simulates Redis pipelining for performance optimization

import time
from typing import Any, List, Tuple, Callable
from dataclasses import dataclass
from enum import Enum

class CommandType(Enum):
    """Redis command types."""
    GET = "GET"
    SET = "SET"
    INCR = "INCR"
    LPUSH = "LPUSH"
    LRANGE = "LRANGE"
    SADD = "SADD"
    SMEMBERS = "SMEMBERS"
    ZADD = "ZADD"
    ZRANGE = "ZRANGE"

@dataclass
class Command:
    """Represents a Redis command."""
    cmd_type: CommandType
    args: Tuple[Any, ...]

    def __repr__(self):
        args_str = " ".join(str(arg) for arg in self.args)
        return f"{self.cmd_type.value} {args_str}"

class NetworkSimulator:
    """Simulates network latency."""

    def __init__(self, latency_ms: float = 0.5):
        self.latency_ms = latency_ms
        self.round_trips = 0

    def round_trip(self):
        """Simulate network round trip time (RTT)."""
        time.sleep(self.latency_ms / 1000)
        self.round_trips += 1

    def reset_stats(self):
        """Reset round trip counter."""
        self.round_trips = 0

class SimulatedRedis:
    """Redis simulation with pipelining support."""

    def __init__(self, network: NetworkSimulator):
        self.data = {}
        self.network = network

    def get(self, key: str) -> str:
        """Get value (with network latency)."""
        self.network.round_trip()
        return self.data.get(key, "(nil)")

    def set(self, key: str, value: str) -> str:
        """Set value (with network latency)."""
        self.network.round_trip()
        self.data[key] = value
        return "OK"

    def incr(self, key: str) -> int:
        """Increment value (with network latency)."""
        self.network.round_trip()
        current = int(self.data.get(key, 0))
        current += 1
        self.data[key] = str(current)
        return current

    def lpush(self, key: str, *values: str) -> int:
        """Push to list (with network latency)."""
        self.network.round_trip()
        if key not in self.data:
            self.data[key] = []
        for value in reversed(values):
            self.data[key].insert(0, value)
        return len(self.data[key])

    def lrange(self, key: str, start: int, end: int) -> List[str]:
        """Get list range (with network latency)."""
        self.network.round_trip()
        if key not in self.data:
            return []
        lst = self.data[key]
        if end == -1:
            return lst[start:]
        return lst[start:end+1]

    def sadd(self, key: str, *members: str) -> int:
        """Add to set (with network latency)."""
        self.network.round_trip()
        if key not in self.data:
            self.data[key] = set()
        before = len(self.data[key])
        self.data[key].update(members)
        return len(self.data[key]) - before

    def smembers(self, key: str) -> set:
        """Get set members (with network latency)."""
        self.network.round_trip()
        return self.data.get(key, set())

    def zadd(self, key: str, *args) -> int:
        """Add to sorted set (with network latency)."""
        self.network.round_trip()
        if key not in self.data:
            self.data[key] = {}

        count = 0
        for i in range(0, len(args), 2):
            score = float(args[i])
            member = args[i + 1]
            if member not in self.data[key]:
                count += 1
            self.data[key][member] = score
        return count

    def zrange(self, key: str, start: int, end: int, withscores: bool = False) -> List:
        """Get sorted set range (with network latency)."""
        self.network.round_trip()
        if key not in self.data:
            return []

        sorted_items = sorted(self.data[key].items(), key=lambda x: x[1])
        if end == -1:
            items = sorted_items[start:]
        else:
            items = sorted_items[start:end+1]

        if withscores:
            return [(member, score) for member, score in items]
        return [member for member, score in items]

class Pipeline:
    """
    Redis Pipeline for batching commands.

    Benefits:
    - Reduces network round trips
    - Improves throughput
    - Lowers latency for bulk operations
    """

    def __init__(self, redis: SimulatedRedis):
        self.redis = redis
        self.commands: List[Command] = []
        self.results: List[Any] = []

    def get(self, key: str) -> 'Pipeline':
        """Queue GET command."""
        self.commands.append(Command(CommandType.GET, (key,)))
        return self

    def set(self, key: str, value: str) -> 'Pipeline':
        """Queue SET command."""
        self.commands.append(Command(CommandType.SET, (key, value)))
        return self

    def incr(self, key: str) -> 'Pipeline':
        """Queue INCR command."""
        self.commands.append(Command(CommandType.INCR, (key,)))
        return self

    def lpush(self, key: str, *values: str) -> 'Pipeline':
        """Queue LPUSH command."""
        self.commands.append(Command(CommandType.LPUSH, (key,) + values))
        return self

    def lrange(self, key: str, start: int, end: int) -> 'Pipeline':
        """Queue LRANGE command."""
        self.commands.append(Command(CommandType.LRANGE, (key, start, end)))
        return self

    def sadd(self, key: str, *members: str) -> 'Pipeline':
        """Queue SADD command."""
        self.commands.append(Command(CommandType.SADD, (key,) + members))
        return self

    def smembers(self, key: str) -> 'Pipeline':
        """Queue SMEMBERS command."""
        self.commands.append(Command(CommandType.SMEMBERS, (key,)))
        return self

    def zadd(self, key: str, *args) -> 'Pipeline':
        """Queue ZADD command."""
        self.commands.append(Command(CommandType.ZADD, (key,) + args))
        return self

    def zrange(self, key: str, start: int, end: int, withscores: bool = False) -> 'Pipeline':
        """Queue ZRANGE command."""
        self.commands.append(Command(CommandType.ZRANGE, (key, start, end, withscores)))
        return self

    def execute(self) -> List[Any]:
        """
        Execute all queued commands in a single network round trip.

        In real Redis:
        - Client sends all commands at once
        - Server executes sequentially
        - Server sends all responses at once
        - Single RTT instead of N RTTs
        """
        if not self.commands:
            return []

        print(f"  Pipeline executing {len(self.commands)} commands in 1 RTT...")

        # Simulate single network round trip for entire pipeline
        self.redis.network.round_trip()

        # Execute commands without additional network overhead
        results = []
        for cmd in self.commands:
            # Execute without network latency (already counted once)
            original_network = self.redis.network
            self.redis.network = NetworkSimulator(0)  # No latency for pipelined commands

            if cmd.cmd_type == CommandType.GET:
                result = self.redis.data.get(cmd.args[0], "(nil)")
            elif cmd.cmd_type == CommandType.SET:
                self.redis.data[cmd.args[0]] = cmd.args[1]
                result = "OK"
            elif cmd.cmd_type == CommandType.INCR:
                current = int(self.redis.data.get(cmd.args[0], 0))
                current += 1
                self.redis.data[cmd.args[0]] = str(current)
                result = current
            elif cmd.cmd_type == CommandType.LPUSH:
                key = cmd.args[0]
                values = cmd.args[1:]
                if key not in self.redis.data:
                    self.redis.data[key] = []
                for value in reversed(values):
                    self.redis.data[key].insert(0, value)
                result = len(self.redis.data[key])
            elif cmd.cmd_type == CommandType.LRANGE:
                key, start, end = cmd.args
                if key not in self.redis.data:
                    result = []
                else:
                    lst = self.redis.data[key]
                    result = lst[start:] if end == -1 else lst[start:end+1]
            elif cmd.cmd_type == CommandType.SADD:
                key = cmd.args[0]
                members = cmd.args[1:]
                if key not in self.redis.data:
                    self.redis.data[key] = set()
                before = len(self.redis.data[key])
                self.redis.data[key].update(members)
                result = len(self.redis.data[key]) - before
            elif cmd.cmd_type == CommandType.SMEMBERS:
                result = self.redis.data.get(cmd.args[0], set())
            elif cmd.cmd_type == CommandType.ZADD:
                key = cmd.args[0]
                args = cmd.args[1:]
                if key not in self.redis.data:
                    self.redis.data[key] = {}
                count = 0
                for i in range(0, len(args), 2):
                    score = float(args[i])
                    member = args[i + 1]
                    if member not in self.redis.data[key]:
                        count += 1
                    self.redis.data[key][member] = score
                result = count
            elif cmd.cmd_type == CommandType.ZRANGE:
                key, start, end, withscores = cmd.args
                if key not in self.redis.data:
                    result = []
                else:
                    sorted_items = sorted(self.redis.data[key].items(), key=lambda x: x[1])
                    items = sorted_items[start:] if end == -1 else sorted_items[start:end+1]
                    result = [(m, s) for m, s in items] if withscores else [m for m, s in items]

            results.append(result)
            self.redis.network = original_network

        self.results = results
        self.commands.clear()
        return results

# Example 1: Without Pipelining (Baseline)
print("Example 1: Without Pipelining (Baseline)")
print("=" * 60)

network = NetworkSimulator(latency_ms=0.5)
redis = SimulatedRedis(network)

print("Setting 1000 keys WITHOUT pipelining:")
network.reset_stats()
start_time = time.time()

for i in range(1000):
    redis.set(f"key:{i}", f"value{i}")

end_time = time.time()
elapsed_ms = (end_time - start_time) * 1000

print(f"  Commands: 1000")
print(f"  Round trips: {network.round_trips}")
print(f"  Time: {elapsed_ms:.1f}ms")
print(f"  Throughput: {1000 / (elapsed_ms / 1000):.0f} ops/sec")
print()

# Example 2: With Pipelining
print("Example 2: With Pipelining")
print("=" * 60)

network2 = NetworkSimulator(latency_ms=0.5)
redis2 = SimulatedRedis(network2)

print("Setting 1000 keys WITH pipelining (batches of 100):")
network2.reset_stats()
start_time = time.time()

batch_size = 100
for batch_start in range(0, 1000, batch_size):
    pipe = Pipeline(redis2)
    for i in range(batch_start, min(batch_start + batch_size, 1000)):
        pipe.set(f"key:{i}", f"value{i}")
    pipe.execute()

end_time = time.time()
elapsed_ms = (end_time - start_time) * 1000

print(f"  Commands: 1000")
print(f"  Round trips: {network2.round_trips}")
print(f"  Time: {elapsed_ms:.1f}ms")
print(f"  Throughput: {1000 / (elapsed_ms / 1000):.0f} ops/sec")
print(f"  Speedup: {(1000 / network2.round_trips):.1f}x fewer RTTs")
print()

# Example 3: Mixed Command Pipelining
print("Example 3: Mixed Command Pipelining")
print("=" * 60)

network3 = NetworkSimulator(latency_ms=0.5)
redis3 = SimulatedRedis(network3)

# Setup initial data
redis3.set("counter", "0")
redis3.lpush("events", "event1", "event2", "event3")

print("Executing mixed commands:")

# Without pipelining
print("\nWITHOUT pipelining:")
network3.reset_stats()
start = time.time()

result1 = redis3.get("counter")
result2 = redis3.incr("counter")
result3 = redis3.incr("counter")
result4 = redis3.get("counter")
result5 = redis3.lrange("events", 0, -1)

elapsed = (time.time() - start) * 1000
print(f"  Results: {result1}, {result2}, {result3}, {result4}, {result5}")
print(f"  Round trips: {network3.round_trips}")
print(f"  Time: {elapsed:.1f}ms")

# Reset for pipelining test
redis3.set("counter", "0")

# With pipelining
print("\nWITH pipelining:")
network3.reset_stats()
start = time.time()

pipe = Pipeline(redis3)
pipe.get("counter")
pipe.incr("counter")
pipe.incr("counter")
pipe.get("counter")
pipe.lrange("events", 0, -1)
results = pipe.execute()

elapsed = (time.time() - start) * 1000
print(f"  Results: {results}")
print(f"  Round trips: {network3.round_trips}")
print(f"  Time: {elapsed:.1f}ms")
print(f"  Speedup: {5}x fewer RTTs")
print()

# Example 4: Bulk Data Loading
print("Example 4: Bulk Data Loading")
print("=" * 60)

network4 = NetworkSimulator(latency_ms=0.5)
redis4 = SimulatedRedis(network4)

# Simulate loading user data
users = [
    {"id": i, "name": f"user{i}", "email": f"user{i}@example.com"}
    for i in range(100)
]

print(f"Loading {len(users)} user records:")

print("\nWITHOUT pipelining:")
network4.reset_stats()
start = time.time()

for user in users:
    redis4.set(f"user:{user['id']}:name", user['name'])
    redis4.set(f"user:{user['id']}:email", user['email'])
    redis4.sadd("users:all", str(user['id']))

elapsed = (time.time() - start) * 1000
print(f"  Commands: {len(users) * 3}")
print(f"  Round trips: {network4.round_trips}")
print(f"  Time: {elapsed:.1f}ms")

# Clear for pipelined version
redis4.data.clear()

print("\nWITH pipelining:")
network4.reset_stats()
start = time.time()

pipe = Pipeline(redis4)
for user in users:
    pipe.set(f"user:{user['id']}:name", user['name'])
    pipe.set(f"user:{user['id']}:email", user['email'])
    pipe.sadd("users:all", str(user['id']))
pipe.execute()

elapsed = (time.time() - start) * 1000
print(f"  Commands: {len(users) * 3}")
print(f"  Round trips: {network4.round_trips}")
print(f"  Time: {elapsed:.1f}ms")
print(f"  Speedup: {(len(users) * 3 / network4.round_trips):.1f}x fewer RTTs")
print()

# Example 5: Leaderboard Updates
print("Example 5: Leaderboard Updates")
print("=" * 60)

network5 = NetworkSimulator(latency_ms=0.5)
redis5 = SimulatedRedis(network5)

# Simulate game score updates
score_updates = [
    ("player1", 1500),
    ("player2", 1200),
    ("player3", 1800),
    ("player4", 1350),
    ("player5", 1650),
]

print("Updating leaderboard with pipelining:")

pipe = Pipeline(redis5)
for player, score in score_updates:
    pipe.zadd("leaderboard", score, player)
    pipe.incr(f"stats:{player}:games")
    pipe.set(f"stats:{player}:last_score", str(score))

network5.reset_stats()
start = time.time()
pipe.execute()
elapsed = (time.time() - start) * 1000

print(f"  Updates: {len(score_updates)} players x 3 operations")
print(f"  Total commands: {len(score_updates) * 3}")
print(f"  Round trips: {network5.round_trips}")
print(f"  Time: {elapsed:.1f}ms")
print()

# Retrieve leaderboard
pipe2 = Pipeline(redis5)
pipe2.zrange("leaderboard", 0, -1, withscores=True)
results = pipe2.execute()

print("Leaderboard (sorted by score):")
for rank, (player, score) in enumerate(results[0], 1):
    print(f"  {rank}. {player}: {int(score)} points")

print()
print("=" * 60)
print("PIPELINING BEST PRACTICES")
print("=" * 60)
print("""
1. WHEN TO USE PIPELINING
   - Bulk data loading/updating
   - Multiple independent operations
   - High-latency networks benefit most
   - Operations that don't depend on each other's results

2. BATCH SIZE
   - Balance between memory and RTT reduction
   - Typical: 100-1000 commands per pipeline
   - Too large: memory issues, slow network transfer
   - Too small: doesn't fully leverage pipelining

3. LIMITATIONS
   - Can't use result of one command in next
   - No transactional guarantees (use MULTI/EXEC for that)
   - Commands may partially succeed
   - Memory usage grows with pipeline size

4. PERFORMANCE GAINS
   - RTT reduction: N commands = 1 RTT (vs N RTTs)
   - Example: 1ms RTT, 1000 commands
     * Without: 1000ms
     * With: ~1ms + processing time
   - Higher gains with higher latency

5. COMMON PATTERNS
   - Bulk user registration/updates
   - Cache warming
   - Analytics data ingestion
   - Leaderboard updates
   - Multi-field object storage

6. COMBINING WITH OTHER FEATURES
   - Pipeline + Lua scripts: Combine atomic ops with batching
   - Pipeline + MULTI/EXEC: Not needed together
   - Pipeline + Cluster: Works but watch for MOVED errors

7. ERROR HANDLING
   - Pipeline continues on error
   - Check results array for errors
   - Consider transaction semantics if needed

Production note: Real Redis pipelining provides:
- Automatic buffering and flushing
- Configurable batch sizes
- Network protocol optimization
- Support for millions of ops/sec
- Integration with connection pooling
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 11 COMPLETE: Redis Advanced Features")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 858: Redis Lua Scripting")
    print(f"  - Lesson 856: Redis Cluster")
    print(f"  - Lesson 857: Redis Pipelining")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
