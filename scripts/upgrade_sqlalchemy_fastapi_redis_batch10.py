#!/usr/bin/env python3
"""
Upgrade SQLAlchemy Query Optimization, FastAPI API Versioning, and Redis lessons
"""

import json
import sys

def upgrade_lesson_966():
    """SQLAlchemy - Query Optimization"""
    return '''# SQLAlchemy Query Optimization
# In production: pip install sqlalchemy

"""
SQLAlchemy Query Optimization

Complete guide to optimizing SQLAlchemy queries:
- Eager loading (joinedload, subqueryload)
- Lazy loading strategies
- Query result caching
- N+1 query problem
- Index optimization
- Query profiling
- Bulk operations

Used by: High-performance database applications
"""

import time
from typing import List, Dict, Any, Optional
from collections import defaultdict


# ============================================================================
# Query Profiling
# ============================================================================

class QueryProfiler:
    """Profile database queries"""

    def __init__(self):
        self.queries: List[Dict] = []
        self.total_time = 0

    def log_query(self, sql: str, duration: float):
        """Log query execution"""
        self.queries.append({
            'sql': sql,
            'duration': duration,
            'timestamp': time.time()
        })
        self.total_time += duration

    def report(self):
        """Generate performance report"""
        print("\\nQUERY PERFORMANCE REPORT")
        print("-" * 80)
        print(f"Total queries: {len(self.queries)}")
        print(f"Total time: {self.total_time*1000:.2f}ms")
        print(f"Average time: {(self.total_time/len(self.queries)*1000):.2f}ms" if self.queries else "N/A")

        # Slowest queries
        if self.queries:
            sorted_queries = sorted(self.queries, key=lambda q: q['duration'], reverse=True)
            print("\\nSlowest queries:")
            for i, query in enumerate(sorted_queries[:5], 1):
                print(f"  {i}. {query['sql'][:60]}... ({query['duration']*1000:.2f}ms)")


# Global profiler
profiler = QueryProfiler()


# ============================================================================
# Simulated Database
# ============================================================================

class Database:
    """Simulated database with query tracking"""

    def __init__(self):
        self.authors = []
        self.books = []
        self.reviews = []
        self.query_count = 0

    def execute(self, sql: str, simulate_delay: float = 0.01) -> List[Dict]:
        """Execute query with profiling"""
        start = time.time()
        self.query_count += 1

        # Simulate query execution
        time.sleep(simulate_delay)

        # Log query
        duration = time.time() - start
        profiler.log_query(sql, duration)

        # Return dummy data
        if "SELECT * FROM authors" in sql:
            return self.authors
        elif "SELECT * FROM books" in sql:
            return self.books
        elif "SELECT * FROM reviews" in sql:
            return self.reviews
        elif "JOIN" in sql:
            # Simulate join result
            return []

        return []


db = Database()


# ============================================================================
# Models
# ============================================================================

class Model:
    """Base model"""
    _instances = defaultdict(list)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Store instance
        self.__class__._instances[self.__class__.__name__].append(self)

    @classmethod
    def query_all(cls):
        """Query all instances"""
        sql = f"SELECT * FROM {cls.__name__.lower()}s"
        db.execute(sql)
        return cls._instances[cls.__name__]


class Author(Model):
    """Author model"""
    def __init__(self, id: int, name: str):
        super().__init__(id=id, name=name)
        self._books = None

    @property
    def books(self) -> List['Book']:
        """Lazy load books (N+1 problem)"""
        if self._books is None:
            sql = f"SELECT * FROM books WHERE author_id = {self.id}"
            db.execute(sql)
            self._books = [b for b in Book._instances['Book'] if b.author_id == self.id]
        return self._books


class Book(Model):
    """Book model"""
    def __init__(self, id: int, title: str, author_id: int):
        super().__init__(id=id, title=title, author_id=author_id)
        self._author = None
        self._reviews = None

    @property
    def author(self) -> Optional['Author']:
        """Lazy load author"""
        if self._author is None:
            sql = f"SELECT * FROM authors WHERE id = {self.author_id}"
            db.execute(sql)
            authors = [a for a in Author._instances['Author'] if a.id == self.author_id]
            self._author = authors[0] if authors else None
        return self._author

    @property
    def reviews(self) -> List['Review']:
        """Lazy load reviews"""
        if self._reviews is None:
            sql = f"SELECT * FROM reviews WHERE book_id = {self.id}"
            db.execute(sql)
            self._reviews = [r for r in Review._instances['Review'] if r.book_id == self.id]
        return self._reviews


class Review(Model):
    """Review model"""
    def __init__(self, id: int, book_id: int, rating: int, text: str):
        super().__init__(id=id, book_id=book_id, rating=rating, text=text)


# ============================================================================
# Query Strategies
# ============================================================================

class QueryStrategy:
    """Different loading strategies"""

    @staticmethod
    def lazy_loading():
        """Lazy loading - N+1 problem"""
        print("\\n1. LAZY LOADING (N+1 Problem)")
        print("-" * 80)

        # Reset profiler
        profiler.queries.clear()
        profiler.total_time = 0
        db.query_count = 0

        # Query all authors
        authors = Author.query_all()
        print(f"Loaded {len(authors)} authors (1 query)")

        # Access books for each author - triggers N queries!
        for author in authors:
            books = author.books  # N+1 problem!
            print(f"  {author.name}: {len(books)} books")

        print(f"\\nTotal queries: {db.query_count} (1 + N)")
        print("Problem: 1 query for authors + N queries for books")

    @staticmethod
    def eager_loading_joined():
        """Eager loading with JOIN"""
        print("\\n2. EAGER LOADING (Joined)")
        print("-" * 80)

        profiler.queries.clear()
        profiler.total_time = 0
        db.query_count = 0

        # Single query with JOIN
        sql = "SELECT authors.*, books.* FROM authors LEFT JOIN books ON authors.id = books.author_id"
        db.execute(sql)

        # All data loaded in one query
        authors = Author.query_all()

        # Pre-populate books (simulated eager loading)
        for author in authors:
            author._books = [b for b in Book._instances['Book'] if b.author_id == author.id]

        # Access books - no additional queries!
        for author in authors:
            books = author.books
            print(f"  {author.name}: {len(books)} books")

        print(f"\\nTotal queries: {db.query_count}")
        print("Solution: Single JOIN query loads everything")

    @staticmethod
    def eager_loading_subquery():
        """Eager loading with subquery"""
        print("\\n3. EAGER LOADING (Subquery)")
        print("-" * 80)

        profiler.queries.clear()
        profiler.total_time = 0
        db.query_count = 0

        # Query authors
        authors = Author.query_all()

        # Query all books in separate query
        sql = "SELECT * FROM books WHERE author_id IN (SELECT id FROM authors)"
        db.execute(sql)

        # Pre-populate relationships
        for author in authors:
            author._books = [b for b in Book._instances['Book'] if b.author_id == author.id]

        for author in authors:
            books = author.books
            print(f"  {author.name}: {len(books)} books")

        print(f"\\nTotal queries: {db.query_count}")
        print("Solution: 2 queries total (authors + all books)")

    @staticmethod
    def select_only_needed():
        """Select only needed columns"""
        print("\\n4. SELECT ONLY NEEDED COLUMNS")
        print("-" * 80)

        profiler.queries.clear()
        db.query_count = 0

        # Bad: SELECT *
        sql = "SELECT * FROM books"
        db.execute(sql)
        print(f"SELECT *: {db.query_count} query")

        # Good: SELECT specific columns
        sql = "SELECT id, title FROM books"
        db.execute(sql)
        print(f"SELECT id, title: {db.query_count} queries total")
        print("\\nBenefit: Less data transferred, faster queries")

    @staticmethod
    def batch_loading():
        """Batch load related objects"""
        print("\\n5. BATCH LOADING")
        print("-" * 80)

        profiler.queries.clear()
        db.query_count = 0

        # Get all books
        books = Book.query_all()

        # Batch load all authors in one query
        author_ids = {b.author_id for b in books}
        sql = f"SELECT * FROM authors WHERE id IN ({','.join(map(str, author_ids))})"
        db.execute(sql)

        # Create author lookup
        author_map = {a.id: a for a in Author._instances['Author']}

        # Assign authors without additional queries
        for book in books:
            book._author = author_map.get(book.author_id)

        print(f"Loaded {len(books)} books and {len(author_map)} authors")
        print(f"Total queries: {db.query_count}")


# ============================================================================
# Bulk Operations
# ============================================================================

class BulkOperations:
    """Efficient bulk operations"""

    @staticmethod
    def bulk_insert():
        """Bulk insert vs individual inserts"""
        print("\\n6. BULK INSERT")
        print("-" * 80)

        profiler.queries.clear()
        db.query_count = 0

        # Individual inserts - slow
        print("Individual inserts:")
        start = time.time()
        for i in range(100):
            sql = f"INSERT INTO books (title) VALUES ('Book {i}')"
            db.execute(sql, simulate_delay=0.001)
        individual_time = time.time() - start

        print(f"  100 individual inserts: {individual_time*1000:.2f}ms ({db.query_count} queries)")

        # Bulk insert - fast
        db.query_count = 0
        print("\\nBulk insert:")
        start = time.time()
        sql = "INSERT INTO books (title) VALUES " + ", ".join([f"('Book {i}')" for i in range(100)])
        db.execute(sql, simulate_delay=0.01)
        bulk_time = time.time() - start

        print(f"  1 bulk insert: {bulk_time*1000:.2f}ms ({db.query_count} query)")
        print(f"  Speedup: {individual_time/bulk_time:.1f}x faster")

    @staticmethod
    def bulk_update():
        """Bulk update operations"""
        print("\\n7. BULK UPDATE")
        print("-" * 80)

        profiler.queries.clear()
        db.query_count = 0

        # Update multiple records in one query
        sql = "UPDATE books SET published = true WHERE author_id IN (1, 2, 3)"
        db.execute(sql)

        print(f"Updated multiple books: {db.query_count} query")
        print("Better than updating each book individually")


# ============================================================================
# Caching
# ============================================================================

class QueryCache:
    """Query result caching"""

    def __init__(self):
        self.cache: Dict[str, Any] = {}
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Any]:
        """Get from cache"""
        if key in self.cache:
            self.hits += 1
            return self.cache[key]

        self.misses += 1
        return None

    def set(self, key: str, value: Any):
        """Set cache"""
        self.cache[key] = value

    def stats(self):
        """Cache statistics"""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0

        print(f"\\nCache stats:")
        print(f"  Hits: {self.hits}")
        print(f"  Misses: {self.misses}")
        print(f"  Hit rate: {hit_rate:.1f}%")


cache = QueryCache()


def cached_query(sql: str) -> List:
    """Query with caching"""
    # Check cache
    result = cache.get(sql)
    if result is not None:
        print(f"  Cache hit: {sql[:50]}...")
        return result

    # Execute query
    print(f"  Cache miss, executing: {sql[:50]}...")
    result = db.execute(sql)

    # Store in cache
    cache.set(sql, result)

    return result


# ============================================================================
# Example Usage
# ============================================================================

def setup_test_data():
    """Create test data"""
    # Create authors
    for i in range(5):
        Author(id=i+1, name=f"Author {i+1}")

    # Create books
    for i in range(20):
        Book(id=i+1, title=f"Book {i+1}", author_id=(i % 5) + 1)

    # Create reviews
    for i in range(50):
        Review(id=i+1, book_id=(i % 20) + 1, rating=4, text=f"Review {i+1}")


def main():
    print("=" * 80)
    print("SQLALCHEMY QUERY OPTIMIZATION")
    print("=" * 80)

    # Setup data
    setup_test_data()

    # Demonstrate optimization techniques
    QueryStrategy.lazy_loading()
    QueryStrategy.eager_loading_joined()
    QueryStrategy.eager_loading_subquery()
    QueryStrategy.select_only_needed()
    QueryStrategy.batch_loading()

    BulkOperations.bulk_insert()
    BulkOperations.bulk_update()

    # Caching example
    print("\\n8. QUERY CACHING")
    print("-" * 80)
    sql = "SELECT * FROM books WHERE author_id = 1"
    cached_query(sql)  # Miss
    cached_query(sql)  # Hit
    cached_query(sql)  # Hit
    cache.stats()

    # Show overall stats
    profiler.report()

    print("\\n" + "=" * 80)
    print("QUERY OPTIMIZATION BEST PRACTICES")
    print("=" * 80)
    print("""
1. N+1 QUERY PROBLEM:
   - Use eager loading (joinedload, subqueryload)
   - Don't access relationships in loops
   - Batch load related objects
   - Monitor query count

2. LOADING STRATEGIES:
   - lazy: Load on access (default, N+1 risk)
   - joined: Single query with JOIN
   - subquery: Separate subquery
   - selectin: IN clause for related objects

3. SELECT OPTIMIZATION:
   - Select only needed columns
   - Use defer() for large columns
   - Use load_only() for specific columns
   - Avoid SELECT *

4. BULK OPERATIONS:
   - Use bulk_insert_mappings()
   - Use bulk_update_mappings()
   - Batch operations when possible
   - Much faster than individual ops

5. INDEXING:
   - Index foreign keys
   - Index frequently queried columns
   - Composite indexes for multiple columns
   - Monitor slow queries

6. QUERY RESULT CACHING:
   - Cache expensive queries
   - Set appropriate TTL
   - Invalidate on updates
   - Use Redis for distributed cache

7. PROFILING:
   - Enable query logging
   - Track slow queries
   - Use SQLAlchemy events
   - Monitor in production

8. PAGINATION:
   - Use limit/offset for large results
   - Cursor-based pagination for performance
   - Return counts separately
   - Index sort columns
""")

    print("\\n✓ SQLAlchemy query optimization complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_776():
    """FastAPI - API Versioning"""
    return '''# FastAPI API Versioning
# In production: pip install fastapi

"""
FastAPI API Versioning

Complete guide to API versioning strategies:
- URL path versioning (/v1/, /v2/)
- Header versioning
- Query parameter versioning
- Content negotiation versioning
- Deprecation strategies
- Backward compatibility

Used by: All production APIs (Stripe, GitHub, Twitter)
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# API Version Management
# ============================================================================

class APIVersion(Enum):
    """API version enum"""
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"


class VersionManager:
    """Manage API versions and deprecation"""

    def __init__(self):
        self.versions = {
            APIVersion.V1: {
                'status': 'deprecated',
                'sunset_date': '2024-12-31',
                'replacement': 'v2'
            },
            APIVersion.V2: {
                'status': 'current',
                'sunset_date': None,
                'replacement': None
            },
            APIVersion.V3: {
                'status': 'beta',
                'sunset_date': None,
                'replacement': None
            }
        }

    def is_supported(self, version: APIVersion) -> bool:
        """Check if version is supported"""
        return version in self.versions

    def is_deprecated(self, version: APIVersion) -> bool:
        """Check if version is deprecated"""
        return self.versions.get(version, {}).get('status') == 'deprecated'

    def get_deprecation_info(self, version: APIVersion) -> Dict:
        """Get deprecation information"""
        return self.versions.get(version, {})


version_manager = VersionManager()


# ============================================================================
# Request/Response Models
# ============================================================================

@dataclass
class Request:
    """HTTP request"""
    method: str
    url: str
    headers: Dict[str, str]
    query_params: Dict[str, str]
    json_data: Optional[Dict] = None


@dataclass
class Response:
    """HTTP response"""
    status_code: int
    content: Any
    headers: Dict[str, str]


# ============================================================================
# FastAPI Application
# ============================================================================

class FastAPI:
    """Simulated FastAPI app"""

    def __init__(self, title: str = "API"):
        self.title = title
        self.routes = {}

    def get(self, path: str):
        """Register GET route"""
        def decorator(func):
            self.routes[f"GET {path}"] = func
            return func
        return decorator

    def post(self, path: str):
        """Register POST route"""
        def decorator(func):
            self.routes[f"POST {path}"] = func
            return func
        return decorator

    async def handle_request(self, request: Request) -> Response:
        """Handle request"""
        route_key = f"{request.method} {request.url}"

        if route_key not in self.routes:
            return Response(404, {"error": "Not found"}, {})

        try:
            result = await self.routes[route_key](request)
            return Response(200, result, {})
        except Exception as e:
            return Response(500, {"error": str(e)}, {})


# ============================================================================
# Strategy 1: URL Path Versioning
# ============================================================================

app_path_versioning = FastAPI()


@app_path_versioning.get("/v1/users")
async def get_users_v1(request: Request):
    """V1 users endpoint - simple response"""
    return {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ],
        "version": "1.0"
    }


@app_path_versioning.get("/v2/users")
async def get_users_v2(request: Request):
    """V2 users endpoint - enhanced response"""
    return {
        "data": [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com",
                "created_at": "2024-01-01"
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com",
                "created_at": "2024-01-02"
            }
        ],
        "metadata": {
            "total": 2,
            "page": 1
        },
        "version": "2.0"
    }


# ============================================================================
# Strategy 2: Header Versioning
# ============================================================================

app_header_versioning = FastAPI()


@app_header_versioning.get("/users")
async def get_users_header(request: Request):
    """Users endpoint with header-based versioning"""
    # Extract version from header
    api_version = request.headers.get('X-API-Version', 'v1')

    if api_version == 'v1':
        return {
            "users": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ]
        }
    elif api_version == 'v2':
        return {
            "data": [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"}
            ],
            "metadata": {"total": 2}
        }
    else:
        raise ValueError(f"Unsupported API version: {api_version}")


# ============================================================================
# Strategy 3: Query Parameter Versioning
# ============================================================================

app_query_versioning = FastAPI()


@app_query_versioning.get("/users")
async def get_users_query(request: Request):
    """Users endpoint with query parameter versioning"""
    # Extract version from query params
    api_version = request.query_params.get('version', 'v1')

    if api_version == 'v1':
        return {"users": [{"id": 1, "name": "Alice"}]}
    elif api_version == 'v2':
        return {"data": [{"id": 1, "name": "Alice", "email": "alice@example.com"}]}
    else:
        raise ValueError(f"Unsupported version: {api_version}")


# ============================================================================
# Strategy 4: Content Negotiation
# ============================================================================

app_content_negotiation = FastAPI()


@app_content_negotiation.get("/users")
async def get_users_content_negotiation(request: Request):
    """Users endpoint with Accept header versioning"""
    accept_header = request.headers.get('Accept', 'application/json')

    if 'application/vnd.myapi.v1+json' in accept_header:
        return {"users": [{"id": 1, "name": "Alice"}]}
    elif 'application/vnd.myapi.v2+json' in accept_header:
        return {"data": [{"id": 1, "name": "Alice", "email": "alice@example.com"}]}
    else:
        # Default to latest version
        return {"data": [{"id": 1, "name": "Alice", "email": "alice@example.com"}]}


# ============================================================================
# Deprecation Headers
# ============================================================================

def add_deprecation_headers(response: Response, version: APIVersion) -> Response:
    """Add deprecation warning headers"""
    if version_manager.is_deprecated(version):
        info = version_manager.get_deprecation_info(version)

        response.headers['X-API-Deprecated'] = 'true'
        response.headers['X-API-Sunset-Date'] = info.get('sunset_date', '')
        response.headers['X-API-Replacement'] = info.get('replacement', '')
        response.headers['Warning'] = f'299 - "API version {version.value} is deprecated"'

    return response


# ============================================================================
# Migration Strategy
# ============================================================================

class MigrationHelper:
    """Helper for migrating between API versions"""

    @staticmethod
    def v1_to_v2_user(v1_user: Dict) -> Dict:
        """Convert V1 user format to V2"""
        return {
            "id": v1_user["id"],
            "name": v1_user["name"],
            "email": f"{v1_user['name'].lower()}@example.com",
            "created_at": "2024-01-01"
        }

    @staticmethod
    def v2_to_v1_user(v2_user: Dict) -> Dict:
        """Convert V2 user format to V1 (backward compatibility)"""
        return {
            "id": v2_user["id"],
            "name": v2_user["name"]
        }


# ============================================================================
# Versioned Router
# ============================================================================

class VersionedRouter:
    """Router that handles multiple versions"""

    def __init__(self):
        self.versioned_routes = {}

    def add_route(self, method: str, path: str, version: APIVersion, handler):
        """Add versioned route"""
        key = f"{method} {path} {version.value}"
        self.versioned_routes[key] = handler

    async def route_request(self, request: Request, version: APIVersion) -> Response:
        """Route request to appropriate version handler"""
        key = f"{request.method} {request.url} {version.value}"

        if key in self.versioned_routes:
            handler = self.versioned_routes[key]
            result = await handler(request)
            response = Response(200, result, {})

            # Add deprecation headers
            response = add_deprecation_headers(response, version)

            return response

        return Response(404, {"error": "Not found"}, {})


# ============================================================================
# Example Usage
# ============================================================================

import asyncio


async def demo_path_versioning():
    """Demonstrate path-based versioning"""
    print("\\n1. PATH-BASED VERSIONING")
    print("-" * 80)

    # V1 request
    request_v1 = Request("GET", "/v1/users", {}, {})
    response_v1 = await app_path_versioning.handle_request(request_v1)
    print(f"GET /v1/users: {response_v1.content}")

    # V2 request
    request_v2 = Request("GET", "/v2/users", {}, {})
    response_v2 = await app_path_versioning.handle_request(request_v2)
    print(f"GET /v2/users: {response_v2.content}")

    print("\\nPros: Clear, easy to understand")
    print("Cons: URL changes, can have many endpoints")


async def demo_header_versioning():
    """Demonstrate header-based versioning"""
    print("\\n2. HEADER-BASED VERSIONING")
    print("-" * 80)

    # V1 request
    request_v1 = Request("GET", "/users", {'X-API-Version': 'v1'}, {})
    response_v1 = await app_header_versioning.handle_request(request_v1)
    print(f"GET /users (X-API-Version: v1): {response_v1.content}")

    # V2 request
    request_v2 = Request("GET", "/users", {'X-API-Version': 'v2'}, {})
    response_v2 = await app_header_versioning.handle_request(request_v2)
    print(f"GET /users (X-API-Version: v2): {response_v2.content}")

    print("\\nPros: Clean URLs, easy to test")
    print("Cons: Not visible in URL, harder to cache")


async def demo_query_versioning():
    """Demonstrate query parameter versioning"""
    print("\\n3. QUERY PARAMETER VERSIONING")
    print("-" * 80)

    # V1 request
    request_v1 = Request("GET", "/users", {}, {'version': 'v1'})
    response_v1 = await app_query_versioning.handle_request(request_v1)
    print(f"GET /users?version=v1: {response_v1.content}")

    # V2 request
    request_v2 = Request("GET", "/users", {}, {'version': 'v2'})
    response_v2 = await app_query_versioning.handle_request(request_v2)
    print(f"GET /users?version=v2: {response_v2.content}")

    print("\\nPros: Visible in URL, easy to test")
    print("Cons: Can conflict with other query params")


async def demo_deprecation():
    """Demonstrate deprecation warnings"""
    print("\\n4. DEPRECATION WARNINGS")
    print("-" * 80)

    router = VersionedRouter()

    # V1 handler (deprecated)
    async def v1_handler(req):
        return {"users": [{"id": 1, "name": "Alice"}]}

    router.add_route("GET", "/users", APIVersion.V1, v1_handler)

    # Make request to deprecated version
    request = Request("GET", "/users", {}, {})
    response = await router.route_request(request, APIVersion.V1)

    print(f"Response: {response.content}")
    print(f"\\nDeprecation headers:")
    for header, value in response.headers.items():
        print(f"  {header}: {value}")


async def main():
    print("=" * 80)
    print("FASTAPI API VERSIONING")
    print("=" * 80)

    await demo_path_versioning()
    await demo_header_versioning()
    await demo_query_versioning()
    await demo_deprecation()

    print("\\n" + "=" * 80)
    print("API VERSIONING BEST PRACTICES")
    print("=" * 80)
    print("""
1. VERSIONING STRATEGIES:
   - Path versioning (/v1/, /v2/): Most common, clear
   - Header versioning (X-API-Version): Clean URLs
   - Query param (?version=v1): Visible in URL
   - Content negotiation (Accept header): RESTful

2. WHEN TO VERSION:
   - Breaking changes to response structure
   - Removing endpoints or fields
   - Changing validation rules
   - Different authentication methods

3. DEPRECATION PROCESS:
   - Announce deprecation early
   - Set sunset date (6-12 months)
   - Add deprecation headers
   - Provide migration guide
   - Monitor usage of old versions

4. BACKWARD COMPATIBILITY:
   - Add new fields (don't remove)
   - Make new fields optional
   - Provide default values
   - Support old request formats
   - Test both versions

5. VERSION LIFECYCLE:
   - Beta: Testing, may change
   - Current: Stable, recommended
   - Deprecated: Still works, sunset date set
   - Sunset: No longer supported

6. MIGRATION HELPERS:
   - Provide conversion functions
   - Document changes clearly
   - Offer migration tools
   - Example code for new version

7. DOCUMENTATION:
   - Document all versions
   - Highlight changes between versions
   - Provide migration guides
   - Show deprecation timeline

8. MONITORING:
   - Track version usage
   - Alert on deprecated version calls
   - Monitor migration progress
   - Plan sunsetting based on usage
""")

    print("\\n✓ FastAPI API versioning complete!")


if __name__ == '__main__':
    asyncio.run(main())
'''

def main():
    print("=" * 80)
    print("UPGRADING: SQLAlchemy Query Optimization and FastAPI API Versioning")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (966, upgrade_lesson_966, "SQLAlchemy - Query Optimization"),
        (776, upgrade_lesson_776, "FastAPI - API Versioning"),
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
    print("BATCH COMPLETE!")
    print("=" * 80)
    print(f"Total lessons in file: {len(lessons)} (maintaining 1030)")


if __name__ == '__main__':
    main()
