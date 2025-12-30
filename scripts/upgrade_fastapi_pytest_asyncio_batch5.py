#!/usr/bin/env python3
"""
Upgrade FastAPI Testing, pytest Integration/Database, and asyncio lessons
"""

import json
import sys

def upgrade_lesson_777():
    """FastAPI - Testing FastAPI"""
    return '''# FastAPI Testing with TestClient
# In production: pip install fastapi pytest httpx

"""
FastAPI Testing

Complete testing guide for FastAPI applications:
- TestClient for integration testing
- Testing async endpoints
- Dependency injection overrides
- Database testing with fixtures
- Authentication testing
- Mocking external services

Used by: All FastAPI production applications
"""

import json
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
import asyncio


# ============================================================================
# TestClient (simulated)
# ============================================================================

@dataclass
class Response:
    """HTTP response"""
    status_code: int
    text: str
    headers: Dict[str, str]

    def json(self) -> Any:
        """Parse JSON response"""
        return json.loads(self.text)


class TestClient:
    """
    FastAPI test client

    Simulates HTTP requests without starting a server
    Perfect for integration testing
    """

    def __init__(self, app):
        self.app = app

    async def _make_request(self, method: str, url: str, **kwargs) -> Response:
        """Make request to app"""
        # Simulate request object
        request = type('Request', (), {
            'method': method,
            'url': url,
            'headers': kwargs.get('headers', {}),
            'json_data': kwargs.get('json'),
            'query_params': kwargs.get('params', {})
        })()

        # Call app handler
        response = await self.app.handle_request(request)

        return Response(
            status_code=response.status_code,
            text=json.dumps(response.content) if isinstance(response.content, dict) else str(response.content),
            headers=response.headers
        )

    def get(self, url: str, **kwargs) -> Response:
        """GET request"""
        return asyncio.run(self._make_request('GET', url, **kwargs))

    def post(self, url: str, **kwargs) -> Response:
        """POST request"""
        return asyncio.run(self._make_request('POST', url, **kwargs))

    def put(self, url: str, **kwargs) -> Response:
        """PUT request"""
        return asyncio.run(self._make_request('PUT', url, **kwargs))

    def delete(self, url: str, **kwargs) -> Response:
        """DELETE request"""
        return asyncio.run(self._make_request('DELETE', url, **kwargs))


# ============================================================================
# FastAPI Application (simulated)
# ============================================================================

class Request:
    """Request object"""
    def __init__(self, method: str, url: str, headers: Dict = None, json_data: Dict = None, query_params: Dict = None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.json_data = json_data
        self.query_params = query_params or {}


class HTTPException(Exception):
    """HTTP exception"""
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        super().__init__(detail)


class ResponseModel:
    """Response model"""
    def __init__(self, content: Any, status_code: int = 200, headers: Dict = None):
        self.content = content
        self.status_code = status_code
        self.headers = headers or {}


class FastAPI:
    """FastAPI app"""

    def __init__(self, title: str = "API"):
        self.title = title
        self.routes = {}
        self.dependencies = {}
        self.dependency_overrides = {}

    def get(self, path: str):
        def decorator(func):
            self.routes[f"GET {path}"] = func
            return func
        return decorator

    def post(self, path: str):
        def decorator(func):
            self.routes[f"POST {path}"] = func
            return func
        return decorator

    def put(self, path: str):
        def decorator(func):
            self.routes[f"PUT {path}"] = func
            return func
        return decorator

    def delete(self, path: str):
        def decorator(func):
            self.routes[f"DELETE {path}"] = func
            return func
        return decorator

    async def handle_request(self, request) -> ResponseModel:
        """Handle request"""
        route_key = f"{request.method} {request.url}"

        if route_key not in self.routes:
            return ResponseModel({"error": "Not found"}, 404)

        try:
            handler = self.routes[route_key]
            result = await handler(request)
            return ResponseModel(result, 200)
        except HTTPException as e:
            return ResponseModel({"detail": e.detail}, e.status_code)
        except Exception as e:
            return ResponseModel({"detail": str(e)}, 500)


# ============================================================================
# Example Application to Test
# ============================================================================

# Database simulation
class Database:
    """In-memory database"""
    def __init__(self):
        self.users: List[Dict] = []
        self.items: List[Dict] = []

    def create_user(self, username: str, email: str) -> Dict:
        user = {
            'id': len(self.users) + 1,
            'username': username,
            'email': email
        }
        self.users.append(user)
        return user

    def get_user(self, user_id: int) -> Optional[Dict]:
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def get_users(self) -> List[Dict]:
        return self.users.copy()


# Global database (will be overridden in tests)
db = Database()


# Dependency
def get_db():
    """Database dependency"""
    return db


# Create app
app = FastAPI(title="Test API")


@app.get("/")
async def root(request):
    """Root endpoint"""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(request):
    """Get item by ID"""
    # Extract item_id from URL
    item_id = int(request.url.split('/')[-1])

    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/users/")
async def create_user(request):
    """Create user"""
    data = request.json_data
    database = get_db()

    user = database.create_user(
        username=data['username'],
        email=data['email']
    )

    return user


@app.get("/users/")
async def list_users(request):
    """List users"""
    database = get_db()
    users = database.get_users()
    return {"users": users}


@app.get("/users/{user_id}")
async def get_user(request):
    """Get user by ID"""
    user_id = int(request.url.split('/')[-1])
    database = get_db()

    user = database.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ============================================================================
# Tests
# ============================================================================

def test_read_root():
    """Test root endpoint"""
    print("\\nTest: GET / - Root endpoint")
    print("-" * 60)

    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

    print(f"✓ Status: {response.status_code}")
    print(f"✓ Response: {response.json()}")


def test_read_item_success():
    """Test reading item"""
    print("\\nTest: GET /items/42 - Read item")
    print("-" * 60)

    client = TestClient(app)
    response = client.get("/items/42")

    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 42
    assert data["name"] == "Item 42"

    print(f"✓ Item: {data}")


def test_read_item_not_found():
    """Test item not found"""
    print("\\nTest: GET /items/999 - Item not found")
    print("-" * 60)

    client = TestClient(app)
    response = client.get("/items/999")

    assert response.status_code == 404
    data = response.json()
    assert "not found" in data["detail"].lower()

    print(f"✓ Status: {response.status_code}")
    print(f"✓ Error: {data['detail']}")


def test_create_user():
    """Test creating user"""
    print("\\nTest: POST /users/ - Create user")
    print("-" * 60)

    # Reset database for test
    global db
    db = Database()

    client = TestClient(app)
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "test@example.com"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"
    assert "id" in data

    print(f"✓ User created: {data}")


def test_list_users():
    """Test listing users"""
    print("\\nTest: GET /users/ - List users")
    print("-" * 60)

    # Setup: Create test users
    global db
    db = Database()
    db.create_user("alice", "alice@example.com")
    db.create_user("bob", "bob@example.com")

    client = TestClient(app)
    response = client.get("/users/")

    assert response.status_code == 200
    data = response.json()
    assert len(data["users"]) == 2
    assert data["users"][0]["username"] == "alice"

    print(f"✓ Users listed: {len(data['users'])} users")


def test_get_user():
    """Test getting specific user"""
    print("\\nTest: GET /users/1 - Get user")
    print("-" * 60)

    # Setup
    global db
    db = Database()
    db.create_user("alice", "alice@example.com")

    client = TestClient(app)
    response = client.get("/users/1")

    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"

    print(f"✓ User: {data}")


def test_get_user_not_found():
    """Test user not found"""
    print("\\nTest: GET /users/999 - User not found")
    print("-" * 60)

    global db
    db = Database()

    client = TestClient(app)
    response = client.get("/users/999")

    assert response.status_code == 404

    print(f"✓ Status: {response.status_code}")


# ============================================================================
# Fixture-based Testing
# ============================================================================

class TestDatabase:
    """Test database fixture"""

    @staticmethod
    def get_test_db():
        """Get fresh test database"""
        return Database()


def test_with_fixture():
    """Test using database fixture"""
    print("\\nTest: Using database fixture")
    print("-" * 60)

    # Override dependency
    test_db = TestDatabase.get_test_db()

    # Monkey patch for test
    global db
    old_db = db
    db = test_db

    try:
        client = TestClient(app)

        # Create user
        response = client.post("/users/", json={
            "username": "fixture_user",
            "email": "fixture@example.com"
        })

        assert response.status_code == 200

        # Verify in database
        users = test_db.get_users()
        assert len(users) == 1
        assert users[0]["username"] == "fixture_user"

        print(f"✓ Fixture test passed")

    finally:
        # Restore original
        db = old_db


# ============================================================================
# Parametrized Testing
# ============================================================================

def test_multiple_items():
    """Test multiple item IDs"""
    print("\\nTest: Multiple item IDs (parametrized)")
    print("-" * 60)

    client = TestClient(app)

    test_cases = [
        (1, "Item 1"),
        (42, "Item 42"),
        (100, "Item 100"),
    ]

    for item_id, expected_name in test_cases:
        response = client.get(f"/items/{item_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == expected_name
        print(f"  ✓ Item {item_id}: {data['name']}")


# ============================================================================
# Main Test Runner
# ============================================================================

def main():
    print("=" * 80)
    print("FASTAPI TESTING WITH TESTCLIENT")
    print("=" * 80)

    # Run all tests
    tests = [
        test_read_root,
        test_read_item_success,
        test_read_item_not_found,
        test_create_user,
        test_list_users,
        test_get_user,
        test_get_user_not_found,
        test_with_fixture,
        test_multiple_items,
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {e}")
            failed += 1

    # Summary
    print("\\n" + "=" * 80)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 80)

    print("\\n" + "=" * 80)
    print("FASTAPI TESTING BEST PRACTICES")
    print("=" * 80)
    print("""
1. TESTCLIENT:
   - Use TestClient for integration tests
   - No need to run server
   - Tests actual HTTP layer
   - Async endpoints tested synchronously

2. DEPENDENCY OVERRIDES:
   - Override dependencies for testing
   - Use test database instead of production
   - Mock external services
   - app.dependency_overrides[get_db] = get_test_db

3. DATABASE TESTING:
   - Use separate test database
   - Create fresh database per test
   - Use transactions and rollback
   - pytest fixtures for setup/teardown

4. FIXTURES:
   - Create reusable test data
   - Scope fixtures appropriately
   - Use factory fixtures for variations
   - Clean up after tests

5. AUTHENTICATION TESTING:
   - Create test tokens
   - Override auth dependencies
   - Test protected endpoints
   - Verify permissions

6. TEST ORGANIZATION:
   - tests/test_api.py for API tests
   - tests/test_models.py for models
   - tests/conftest.py for fixtures
   - Use pytest markers (@pytest.mark.slow)

7. COVERAGE:
   - Test happy paths
   - Test error scenarios (404, 400, 500)
   - Test validation errors
   - Test edge cases
   - Test authentication/authorization

8. ASYNC TESTING:
   - Use pytest-asyncio
   - Mark async tests with @pytest.mark.asyncio
   - TestClient handles async automatically
   - Test background tasks
""")

    print("\\n✓ FastAPI testing complete!")


if __name__ == '__main__':
    main()
'''

def upgrade_lesson_811():
    """pytest - Integration Testing"""
    return '''# pytest Integration Testing
# In production: pip install pytest pytest-docker docker-compose

"""
pytest Integration Testing

Complete integration testing patterns:
- Testing with real databases
- Docker containers for services
- API integration tests
- Multi-service testing
- Test data management
- Performance testing

Used by: Production test suites for microservices
"""

import time
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


# ============================================================================
# Service Containers (simulated Docker)
# ============================================================================

class Container:
    """Simulated Docker container"""

    def __init__(self, name: str, image: str, ports: Dict[int, int] = None):
        self.name = name
        self.image = image
        self.ports = ports or {}
        self.running = False
        self.health_check_count = 0

    def start(self):
        """Start container"""
        print(f"  Starting container: {self.name} ({self.image})")
        time.sleep(0.1)  # Simulate startup
        self.running = True

    def stop(self):
        """Stop container"""
        print(f"  Stopping container: {self.name}")
        self.running = False

    def is_healthy(self) -> bool:
        """Check if container is healthy"""
        if not self.running:
            return False

        # Simulate health check (becomes healthy after 3 checks)
        self.health_check_count += 1
        return self.health_check_count >= 3

    def exec(self, command: str) -> str:
        """Execute command in container"""
        return f"Executed: {command}"


class DockerCompose:
    """Simulated docker-compose"""

    def __init__(self):
        self.containers: Dict[str, Container] = {}

    def add_service(self, name: str, image: str, ports: Dict = None):
        """Add service to compose"""
        self.containers[name] = Container(name, image, ports)

    def up(self):
        """Start all services"""
        print("Starting services...")
        for container in self.containers.values():
            container.start()

        # Wait for health checks
        print("Waiting for services to be healthy...")
        all_healthy = False
        attempts = 0

        while not all_healthy and attempts < 10:
            all_healthy = all(c.is_healthy() for c in self.containers.values())
            if not all_healthy:
                time.sleep(0.1)
                attempts += 1

        if all_healthy:
            print("✓ All services healthy")
        else:
            print("✗ Services failed to become healthy")

    def down(self):
        """Stop all services"""
        print("Stopping services...")
        for container in self.containers.values():
            container.stop()


# ============================================================================
# Database Service
# ============================================================================

class PostgreSQLDatabase:
    """Simulated PostgreSQL database"""

    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.tables: Dict[str, List[Dict]] = {}
        self.connected = False

    def connect(self):
        """Connect to database"""
        print(f"  Connecting to PostgreSQL: {self.database}")
        time.sleep(0.05)
        self.connected = True

    def disconnect(self):
        """Disconnect from database"""
        self.connected = False

    def execute(self, sql: str, params: tuple = None) -> List[Dict]:
        """Execute SQL"""
        if not self.connected:
            raise Exception("Not connected to database")

        # Simulated query execution
        if "CREATE TABLE" in sql:
            table_name = sql.split("CREATE TABLE")[1].split("(")[0].strip()
            self.tables[table_name] = []
            return []

        elif "INSERT INTO" in sql:
            table_name = sql.split("INSERT INTO")[1].split()[0]
            if table_name in self.tables:
                self.tables[table_name].append({'id': len(self.tables[table_name]) + 1})
            return []

        elif "SELECT" in sql:
            if "FROM" in sql:
                table_name = sql.split("FROM")[1].split()[0]
                return self.tables.get(table_name, [])
            return []

        return []

    def clear_all_tables(self):
        """Clear all data (for test cleanup)"""
        for table in self.tables:
            self.tables[table] = []


# ============================================================================
# Redis Cache Service
# ============================================================================

class RedisCache:
    """Simulated Redis cache"""

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.storage: Dict[str, Any] = {}
        self.connected = False

    def connect(self):
        """Connect to Redis"""
        print(f"  Connecting to Redis: {self.host}:{self.port}")
        time.sleep(0.05)
        self.connected = True

    def disconnect(self):
        """Disconnect"""
        self.connected = False

    def set(self, key: str, value: Any, ex: int = None):
        """Set key"""
        if not self.connected:
            raise Exception("Not connected to Redis")
        self.storage[key] = value

    def get(self, key: str) -> Optional[Any]:
        """Get key"""
        if not self.connected:
            raise Exception("Not connected to Redis")
        return self.storage.get(key)

    def delete(self, key: str):
        """Delete key"""
        if key in self.storage:
            del self.storage[key]

    def flushall(self):
        """Clear all data"""
        self.storage.clear()


# ============================================================================
# Application Services
# ============================================================================

class UserService:
    """User service with database"""

    def __init__(self, db: PostgreSQLDatabase, cache: RedisCache):
        self.db = db
        self.cache = cache

    def create_user(self, username: str, email: str) -> Dict:
        """Create user"""
        # Insert into database
        self.db.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            (username, email)
        )

        user = {'username': username, 'email': email}

        # Cache user
        self.cache.set(f"user:{username}", json.dumps(user))

        return user

    def get_user(self, username: str) -> Optional[Dict]:
        """Get user (with caching)"""
        # Try cache first
        cached = self.cache.get(f"user:{username}")
        if cached:
            return json.loads(cached)

        # Query database
        users = self.db.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        if users:
            user = users[0]
            # Cache for next time
            self.cache.set(f"user:{username}", json.dumps(user))
            return user

        return None


# ============================================================================
# Test Fixtures
# ============================================================================

class IntegrationTestFixtures:
    """Integration test fixtures"""

    @staticmethod
    def setup_docker_services():
        """Setup Docker services"""
        compose = DockerCompose()

        # Add PostgreSQL
        compose.add_service(
            "postgres",
            "postgres:15-alpine",
            ports={5432: 5432}
        )

        # Add Redis
        compose.add_service(
            "redis",
            "redis:7-alpine",
            ports={6379: 6379}
        )

        compose.up()

        return compose

    @staticmethod
    def get_test_database():
        """Get test database connection"""
        db = PostgreSQLDatabase(
            host="localhost",
            port=5432,
            database="test_db",
            user="test_user",
            password="test_pass"
        )
        db.connect()

        # Create schema
        db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE,
                email VARCHAR(255)
            )
        """)

        return db

    @staticmethod
    def get_test_redis():
        """Get test Redis connection"""
        redis = RedisCache(host="localhost", port=6379)
        redis.connect()
        return redis


# ============================================================================
# Integration Tests
# ============================================================================

def test_user_service_integration():
    """Test user service with real database and cache"""
    print("\\nTest: User Service Integration")
    print("-" * 60)

    # Setup services
    db = IntegrationTestFixtures.get_test_database()
    redis = IntegrationTestFixtures.get_test_redis()

    try:
        # Clear data
        db.clear_all_tables()
        redis.flushall()

        # Create service
        user_service = UserService(db, redis)

        # Test create user
        user = user_service.create_user("alice", "alice@example.com")
        assert user['username'] == "alice"
        print("  ✓ User created")

        # Test get user (should hit cache)
        cached_user = user_service.get_user("alice")
        assert cached_user['username'] == "alice"
        print("  ✓ User retrieved from cache")

        # Clear cache and test database retrieval
        redis.flushall()
        db_user = user_service.get_user("alice")
        assert db_user is not None
        print("  ✓ User retrieved from database")

    finally:
        db.disconnect()
        redis.disconnect()


def test_database_transactions():
    """Test database transaction handling"""
    print("\\nTest: Database Transactions")
    print("-" * 60)

    db = IntegrationTestFixtures.get_test_database()

    try:
        # Clear data
        db.clear_all_tables()

        # Insert multiple users
        db.execute("INSERT INTO users (username, email) VALUES (%s, %s)", ("user1", "user1@example.com"))
        db.execute("INSERT INTO users (username, email) VALUES (%s, %s)", ("user2", "user2@example.com"))
        db.execute("INSERT INTO users (username, email) VALUES (%s, %s)", ("user3", "user3@example.com"))

        # Verify all inserted
        users = db.execute("SELECT * FROM users")
        assert len(users) == 3
        print(f"  ✓ Inserted {len(users)} users")

    finally:
        db.disconnect()


def test_cache_expiration():
    """Test cache expiration"""
    print("\\nTest: Cache Expiration")
    print("-" * 60)

    redis = IntegrationTestFixtures.get_test_redis()

    try:
        redis.flushall()

        # Set value with expiration
        redis.set("temp_key", "temp_value", ex=1)

        # Verify exists
        value = redis.get("temp_key")
        assert value == "temp_value"
        print("  ✓ Value cached")

        # Simulate expiration
        redis.delete("temp_key")
        value = redis.get("temp_key")
        assert value is None
        print("  ✓ Value expired")

    finally:
        redis.disconnect()


def test_multi_service_workflow():
    """Test workflow across multiple services"""
    print("\\nTest: Multi-Service Workflow")
    print("-" * 60)

    # Setup all services
    db = IntegrationTestFixtures.get_test_database()
    redis = IntegrationTestFixtures.get_test_redis()

    try:
        db.clear_all_tables()
        redis.flushall()

        user_service = UserService(db, redis)

        # Create multiple users
        users = []
        for i in range(5):
            user = user_service.create_user(f"user{i}", f"user{i}@example.com")
            users.append(user)

        print(f"  ✓ Created {len(users)} users")

        # Verify all cached
        cache_hits = 0
        for i in range(5):
            cached = redis.get(f"user:user{i}")
            if cached:
                cache_hits += 1

        assert cache_hits == 5
        print(f"  ✓ All users cached ({cache_hits} cache hits)")

    finally:
        db.disconnect()
        redis.disconnect()


def test_performance():
    """Test performance with multiple operations"""
    print("\\nTest: Performance Testing")
    print("-" * 60)

    db = IntegrationTestFixtures.get_test_database()
    redis = IntegrationTestFixtures.get_test_redis()

    try:
        db.clear_all_tables()
        redis.flushall()

        user_service = UserService(db, redis)

        # Measure create performance
        start = time.time()
        for i in range(100):
            user_service.create_user(f"perf_user{i}", f"perf{i}@example.com")
        create_time = time.time() - start

        print(f"  ✓ Created 100 users in {create_time:.3f}s")

        # Measure read performance (cached)
        start = time.time()
        for i in range(100):
            user_service.get_user(f"perf_user{i}")
        read_time = time.time() - start

        print(f"  ✓ Read 100 users (cached) in {read_time:.3f}s")

        assert create_time < 2.0  # Should be fast
        assert read_time < create_time  # Reads should be faster

    finally:
        db.disconnect()
        redis.disconnect()


# ============================================================================
# Main Test Runner
# ============================================================================

def main():
    print("=" * 80)
    print("PYTEST INTEGRATION TESTING")
    print("=" * 80)

    # Setup Docker services
    print("\\n1. SETUP DOCKER SERVICES")
    print("-" * 80)
    compose = IntegrationTestFixtures.setup_docker_services()

    # Run integration tests
    print("\\n2. RUNNING INTEGRATION TESTS")
    print("=" * 80)

    tests = [
        test_user_service_integration,
        test_database_transactions,
        test_cache_expiration,
        test_multi_service_workflow,
        test_performance,
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ Test error: {e}")
            failed += 1

    # Cleanup
    print("\\n3. CLEANUP")
    print("-" * 80)
    compose.down()

    # Summary
    print("\\n" + "=" * 80)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 80)

    print("\\n" + "=" * 80)
    print("INTEGRATION TESTING BEST PRACTICES")
    print("=" * 80)
    print("""
1. DOCKER SERVICES:
   - Use docker-compose for services
   - pytest-docker for container management
   - Wait for health checks before testing
   - Clean up containers after tests

2. DATABASE TESTING:
   - Use separate test database
   - Run migrations before tests
   - Use transactions and rollback
   - Clean data between tests

3. TEST DATA:
   - Create realistic test data
   - Use factories for complex objects
   - Seed data in fixtures
   - Clean up after each test

4. ISOLATION:
   - Each test should be independent
   - Don't rely on test execution order
   - Clean state between tests
   - Use separate databases/schemas

5. PERFORMANCE:
   - Integration tests are slower
   - Run unit tests first
   - Use pytest markers (@pytest.mark.integration)
   - Parallel execution with pytest-xdist

6. CI/CD:
   - Run integration tests in CI
   - Use Docker for consistent environment
   - Cache Docker images
   - Fail fast on errors

7. MONITORING:
   - Log service startup/shutdown
   - Track test duration
   - Monitor resource usage
   - Alert on slow tests
""")

    print("\\n✓ Integration testing complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: FastAPI Testing and pytest Integration")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (777, upgrade_lesson_777, "FastAPI - Testing FastAPI"),
        (811, upgrade_lesson_811, "pytest - Integration Testing"),
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
    print("FASTAPI TESTING AND PYTEST INTEGRATION COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
