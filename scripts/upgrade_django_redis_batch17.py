#!/usr/bin/env python3
"""
Upgrade Django and Redis lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 17: Django Caching Strategies, Django Deployment, and Redis Basics
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 761: Django Caching Strategies
    lesson_761 = next(l for l in lessons if l['id'] == 761)
    lesson_761['fullSolution'] = '''# Django Caching Strategies - Complete Simulation
# In production: pip install django redis
# This lesson simulates Django caching with multiple backends and strategies

import time
import hashlib
import pickle
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass
from functools import wraps

class CacheBackend:
    """Base cache backend interface."""

    def get(self, key: str) -> Optional[Any]:
        raise NotImplementedError

    def set(self, key: str, value: Any, timeout: Optional[int] = None):
        raise NotImplementedError

    def delete(self, key: str):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

class LocMemCache(CacheBackend):
    """
    Local memory cache (django.core.cache.backends.locmem.LocMemCache).

    In-process memory cache using a dictionary.
    Fast but limited to single process.
    """

    def __init__(self, max_entries: int = 300):
        self.cache: Dict[str, Tuple[Any, Optional[float]]] = {}
        self.max_entries = max_entries

    def get(self, key: str, default: Any = None) -> Any:
        """Get value from cache."""
        if key not in self.cache:
            return default

        value, expiry = self.cache[key]

        # Check expiry
        if expiry and time.time() > expiry:
            del self.cache[key]
            return default

        return value

    def set(self, key: str, value: Any, timeout: Optional[int] = None):
        """Set value in cache."""
        # Evict if at capacity
        if len(self.cache) >= self.max_entries and key not in self.cache:
            # Simple FIFO eviction
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]

        expiry = time.time() + timeout if timeout else None
        self.cache[key] = (value, expiry)

    def delete(self, key: str):
        """Delete key from cache."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all cache."""
        self.cache.clear()

class RedisCache(CacheBackend):
    """
    Redis cache backend (django.core.cache.backends.redis.RedisCache).

    Distributed cache using Redis.
    Persisted, shared across processes.
    """

    def __init__(self):
        self.data: Dict[str, Tuple[Any, Optional[float]]] = {}

    def get(self, key: str, default: Any = None) -> Any:
        """Get value from Redis."""
        if key not in self.data:
            return default

        value, expiry = self.data[key]

        if expiry and time.time() > expiry:
            del self.data[key]
            return default

        # Deserialize (Redis stores bytes)
        return pickle.loads(pickle.dumps(value))

    def set(self, key: str, value: Any, timeout: Optional[int] = None):
        """Set value in Redis."""
        expiry = time.time() + timeout if timeout else None
        # Serialize for storage
        serialized = pickle.loads(pickle.dumps(value))
        self.data[key] = (serialized, expiry)

    def delete(self, key: str):
        """Delete key from Redis."""
        if key in self.data:
            del self.data[key]

    def clear(self):
        """Flush Redis database."""
        self.data.clear()

class Cache:
    """
    Django cache interface.

    Provides unified API for different cache backends.
    """

    def __init__(self, backend: CacheBackend):
        self.backend = backend

    def get(self, key: str, default: Any = None, version: Optional[int] = None) -> Any:
        """Get cached value."""
        versioned_key = self._make_key(key, version)
        return self.backend.get(versioned_key, default)

    def set(self, key: str, value: Any, timeout: Optional[int] = None, version: Optional[int] = None):
        """Set cached value."""
        versioned_key = self._make_key(key, version)
        self.backend.set(versioned_key, value, timeout)

    def add(self, key: str, value: Any, timeout: Optional[int] = None) -> bool:
        """Add value only if key doesn't exist."""
        versioned_key = self._make_key(key)
        if self.backend.get(versioned_key) is None:
            self.backend.set(versioned_key, value, timeout)
            return True
        return False

    def get_or_set(self, key: str, default: Callable, timeout: Optional[int] = None) -> Any:
        """Get value or set default."""
        value = self.get(key)
        if value is None:
            value = default() if callable(default) else default
            self.set(key, value, timeout)
        return value

    def delete(self, key: str, version: Optional[int] = None):
        """Delete cached value."""
        versioned_key = self._make_key(key, version)
        self.backend.delete(versioned_key)

    def delete_many(self, keys: List[str]):
        """Delete multiple keys."""
        for key in keys:
            self.delete(key)

    def clear(self):
        """Clear all cache."""
        self.backend.clear()

    def incr(self, key: str, delta: int = 1) -> int:
        """Increment integer value."""
        value = self.get(key, 0)
        new_value = int(value) + delta
        self.set(key, new_value)
        return new_value

    def decr(self, key: str, delta: int = 1) -> int:
        """Decrement integer value."""
        return self.incr(key, -delta)

    def _make_key(self, key: str, version: Optional[int] = None) -> str:
        """Create versioned cache key."""
        if version:
            return f"v{version}:{key}"
        return key

def cache_page(timeout: int = 60):
    """
    Django view cache decorator.

    Caches entire view response.
    """
    def decorator(view_func: Callable):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Generate cache key from request
            cache_key = f"view:{request.path}:{request.GET}"

            # Try cache
            cached = cache.get(cache_key)
            if cached:
                print(f"  [CACHE HIT] View: {request.path}")
                return cached

            # Execute view
            print(f"  [CACHE MISS] View: {request.path}")
            response = view_func(request, *args, **kwargs)

            # Cache response
            cache.set(cache_key, response, timeout)

            return response

        return wrapper
    return decorator

def cache_method(timeout: int = 60):
    """
    Cache method result.

    Useful for expensive computations or database queries.
    """
    def decorator(method: Callable):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            # Generate cache key from method name and args
            cache_key = f"method:{self.__class__.__name__}:{method.__name__}:{args}:{kwargs}"

            # Try cache
            cached = cache.get(cache_key)
            if cached is not None:
                print(f"  [CACHE HIT] Method: {method.__name__}")
                return cached

            # Execute method
            print(f"  [CACHE MISS] Method: {method.__name__}")
            result = method(self, *args, **kwargs)

            # Cache result
            cache.set(cache_key, result, timeout)

            return result

        return wrapper
    return decorator

# Initialize cache (using local memory backend)
cache = Cache(LocMemCache())

# Example 1: Basic Cache Operations
print("Example 1: Basic Cache Operations")
print("=" * 60)

print("Setting values:")
cache.set("username", "alice", timeout=300)
cache.set("score", 100, timeout=300)
print("  Set username and score")
print()

print("Getting values:")
print(f"  username: {cache.get('username')}")
print(f"  score: {cache.get('score')}")
print(f"  nonexistent: {cache.get('nonexistent', default='N/A')}")
print()

print("Incrementing score:")
for i in range(3):
    new_score = cache.incr("score", delta=10)
    print(f"  Score: {new_score}")
print()

# Example 2: Cache Versioning
print("Example 2: Cache Versioning")
print("=" * 60)

print("Setting values with different versions:")
cache.set("config", {"theme": "dark"}, version=1)
cache.set("config", {"theme": "light", "lang": "en"}, version=2)
print()

print("Getting versioned values:")
v1_config = cache.get("config", version=1)
v2_config = cache.get("config", version=2)
print(f"  Version 1: {v1_config}")
print(f"  Version 2: {v2_config}")
print()

# Example 3: get_or_set Pattern
print("Example 3: get_or_set Pattern")
print("=" * 60)

def expensive_computation():
    """Simulate expensive operation."""
    print("  [COMPUTE] Running expensive computation...")
    time.sleep(0.1)
    return {"result": "computed value"}

print("First call (computes):")
result = cache.get_or_set("computation", expensive_computation, timeout=60)
print(f"  Result: {result}")
print()

print("Second call (from cache):")
result = cache.get_or_set("computation", expensive_computation, timeout=60)
print(f"  Result: {result}")
print()

# Example 4: View Caching
print("Example 4: View Caching")
print("=" * 60)

@dataclass
class Request:
    """Simulated HTTP request."""
    path: str
    GET: Dict[str, str]

class ProductView:
    """Product view with caching."""

    @cache_page(timeout=60)
    def list_products(self, request):
        """List all products (cached)."""
        print("  [DATABASE] Fetching products from database...")
        time.sleep(0.1)  # Simulate DB query

        products = [
            {"id": 1, "name": "Laptop", "price": 999},
            {"id": 2, "name": "Mouse", "price": 29},
            {"id": 3, "name": "Keyboard", "price": 79},
        ]

        return {"products": products}

view = ProductView()

print("First request (database query):")
request1 = Request(path="/products/", GET={})
response1 = view.list_products(request1)
print(f"  Products: {len(response1['products'])}")
print()

print("Second request (from cache):")
request2 = Request(path="/products/", GET={})
response2 = view.list_products(request2)
print(f"  Products: {len(response2['products'])}")
print()

# Example 5: Method Caching
print("Example 5: Method Caching (QuerySet Pattern)")
print("=" * 60)

class UserManager:
    """User manager with cached queries."""

    def __init__(self):
        self.users = [
            {"id": 1, "username": "alice", "active": True},
            {"id": 2, "username": "bob", "active": True},
            {"id": 3, "username": "charlie", "active": False},
        ]

    @cache_method(timeout=60)
    def get_active_users(self):
        """Get active users (cached)."""
        print("  [DATABASE] Querying active users...")
        time.sleep(0.1)
        return [u for u in self.users if u["active"]]

    @cache_method(timeout=60)
    def get_user_count(self):
        """Get user count (cached)."""
        print("  [DATABASE] Counting users...")
        time.sleep(0.1)
        return len(self.users)

manager = UserManager()

print("First call (database query):")
users = manager.get_active_users()
print(f"  Active users: {len(users)}")
print()

print("Second call (from cache):")
users = manager.get_active_users()
print(f"  Active users: {len(users)}")
print()

print("User count (first call):")
count = manager.get_user_count()
print(f"  Total: {count}")
print()

# Example 6: Fragment Caching
print("Example 6: Template Fragment Caching")
print("=" * 60)

class TemplateCache:
    """Template fragment caching."""

    def cache_fragment(self, fragment_name: str, timeout: int = 60):
        """Cache template fragment."""
        def decorator(render_func: Callable):
            @wraps(render_func)
            def wrapper(*args, **kwargs):
                cache_key = f"fragment:{fragment_name}"

                # Try cache
                cached = cache.get(cache_key)
                if cached:
                    print(f"  [CACHE HIT] Fragment: {fragment_name}")
                    return cached

                # Render fragment
                print(f"  [CACHE MISS] Fragment: {fragment_name}")
                html = render_func(*args, **kwargs)

                # Cache fragment
                cache.set(cache_key, html, timeout)

                return html

            return wrapper
        return decorator

template = TemplateCache()

@template.cache_fragment("sidebar", timeout=300)
def render_sidebar():
    """Render sidebar (expensive)."""
    time.sleep(0.1)
    return "<div>Sidebar content with recent posts...</div>"

@template.cache_fragment("footer", timeout=600)
def render_footer():
    """Render footer."""
    return "<footer>Copyright 2024</footer>"

print("Rendering page components:")
sidebar = render_sidebar()
footer = render_footer()
print()

print("Re-rendering (from cache):")
sidebar = render_sidebar()
footer = render_footer()
print()

# Example 7: Cache Invalidation
print("Example 7: Cache Invalidation Strategies")
print("=" * 60)

class Product:
    """Product model with cache invalidation."""

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def save(self):
        """Save and invalidate related caches."""
        print(f"  [DATABASE] Saving product {self.id}")

        # Invalidate product cache
        cache.delete(f"product:{self.id}")

        # Invalidate product list cache
        cache.delete("product:list")

        # Invalidate category caches
        cache.delete(f"category:{self.category}:products")

        print(f"  [CACHE] Invalidated caches for product {self.id}")

    @classmethod
    def get_cached(cls, product_id: int):
        """Get product with caching."""
        cache_key = f"product:{product_id}"

        product = cache.get(cache_key)
        if product:
            print(f"  [CACHE HIT] Product {product_id}")
            return product

        print(f"  [DATABASE] Fetching product {product_id}")
        product = cls(product_id, "Laptop", 999)
        cache.set(cache_key, product, timeout=300)

        return product

print("Get product (database):")
product = Product.get_cached(1)
print(f"  Product: {product.name}")
print()

print("Get product again (cache):")
product = Product.get_cached(1)
print(f"  Product: {product.name}")
print()

print("Update product:")
product.category = "electronics"
product.save()
print()

print("Get product after update (database):")
product = Product.get_cached(1)
print(f"  Product: {product.name}")
print()

# Example 8: Redis Cache Backend
print("Example 8: Redis Cache Backend")
print("=" * 60)

redis_cache = Cache(RedisCache())

print("Using Redis cache:")
redis_cache.set("session:abc123", {"user_id": 1, "login_at": "2024-01-01"}, timeout=3600)
redis_cache.set("rate_limit:user:1", 10, timeout=60)

session = redis_cache.get("session:abc123")
rate_limit = redis_cache.get("rate_limit:user:1")

print(f"  Session: {session}")
print(f"  Rate limit: {rate_limit}")
print()

# Example 9: Cache Performance Comparison
print("Example 9: Cache Performance Comparison")
print("=" * 60)

def benchmark_cache(cache_instance: Cache, operations: int = 100):
    """Benchmark cache performance."""
    # Set operations
    start = time.time()
    for i in range(operations):
        cache_instance.set(f"key:{i}", f"value{i}")
    set_time = (time.time() - start) * 1000

    # Get operations
    start = time.time()
    for i in range(operations):
        cache_instance.get(f"key:{i}")
    get_time = (time.time() - start) * 1000

    return set_time, get_time

locmem_cache = Cache(LocMemCache())
redis_cache_bench = Cache(RedisCache())

print("Performance (100 operations):")
locmem_set, locmem_get = benchmark_cache(locmem_cache, 100)
print(f"  LocMem: SET {locmem_set:.2f}ms, GET {locmem_get:.2f}ms")

redis_set, redis_get = benchmark_cache(redis_cache_bench, 100)
print(f"  Redis:  SET {redis_set:.2f}ms, GET {redis_get:.2f}ms")

print()
print("=" * 60)
print("DJANGO CACHING BEST PRACTICES")
print("=" * 60)
print("""
CACHE BACKENDS:

1. LocMemCache (development):
   - In-process memory
   - Fast but single-process
   - No persistence
   - Good for: Development, testing

2. Redis (production):
   - Distributed cache
   - Persistent
   - Multiple processes
   - Good for: Production, sessions

3. Memcached:
   - Distributed cache
   - In-memory only
   - Simple, fast
   - Good for: High-traffic sites

4. Database Cache:
   - Uses database table
   - Persistent
   - Slower than memory
   - Good for: Simple deployments

CACHING STRATEGIES:

Per-Site Cache:
  MIDDLEWARE = [
      'django.middleware.cache.UpdateCacheMiddleware',
      ...
      'django.middleware.cache.FetchFromCacheMiddleware',
  ]

Per-View Cache:
  @cache_page(60 * 15)
  def my_view(request):
      ...

Template Fragment Cache:
  {% load cache %}
  {% cache 500 sidebar %}
      ... expensive sidebar ...
  {% endcache %}

Low-Level Cache:
  from django.core.cache import cache
  cache.set('key', 'value', 300)
  value = cache.get('key')

CACHE KEY PATTERNS:

Good patterns:
  user:{id}:profile
  post:{id}:comments
  category:{slug}:products
  api:{endpoint}:{params_hash}

Versioning:
  cache.set('config', data, version=2)
  cache.get('config', version=2)

CACHE INVALIDATION:

Time-based:
  cache.set('key', value, timeout=300)

Event-based:
  def save(self):
      super().save()
      cache.delete(f'product:{self.id}')

Signals:
  @receiver(post_save, sender=Product)
  def invalidate_cache(sender, instance, **kwargs):
      cache.delete(f'product:{instance.id}')

Pattern-based:
  cache.delete_many([
      'product:1',
      'product:2',
      'product:list'
  ])

PERFORMANCE OPTIMIZATION:

Cache Stampede Prevention:
  - Use get_or_set with lock
  - Probabilistic early refresh
  - Serve stale while revalidating

Connection Pooling:
  CACHES = {
      'default': {
          'BACKEND': 'django_redis.cache.RedisCache',
          'OPTIONS': {
              'CONNECTION_POOL_KWARGS': {
                  'max_connections': 50
              }
          }
      }
  }

Compression:
  CACHES = {
      'default': {
          'OPTIONS': {
              'COMPRESSOR': 'django_redis.compressors.zlib.ZlibCompressor'
          }
      }
  }

MONITORING:

Metrics:
  - Hit rate (> 80% target)
  - Miss rate
  - Eviction rate
  - Memory usage
  - Latency

Django Debug Toolbar:
  - Cache panel
  - Query count
  - Cache keys accessed

COMMON PATTERNS:

Caching QuerySets:
  @cache_method(timeout=300)
  def get_active_users(self):
      return User.objects.filter(is_active=True)

API Response Caching:
  @cache_page(60)
  def api_endpoint(request):
      return JsonResponse(data)

Session Caching:
  SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
  SESSION_CACHE_ALIAS = 'default'

SECURITY:

Cache Separation:
  - Separate cache per user
  - Include user_id in cache key
  - Validate cache permissions

Sensitive Data:
  - Don't cache sensitive data
  - Use encrypted cache backend
  - Set short timeouts

Production note: Real Django caching provides:
  - Multiple backend support
  - Cache key prefixing
  - Version management
  - Automatic serialization
  - Cache middleware
  - Template tags
  - Per-site caching
  - Signal integration
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 17 PARTIAL: Django Caching Strategies")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 761: Django Caching Strategies")
    print("\nLesson upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
