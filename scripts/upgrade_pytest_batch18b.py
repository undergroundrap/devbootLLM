"""
Upgrade pytest batch 18 part 2: Integration Testing and Parametrize
Upgrade 2 pytest lessons to 13,000-17,000+ characters
Zero package installation required!
"""

import json
import os

def upgrade_lessons():
    lessons_file = os.path.join('public', 'lessons-python.json')

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 508: Integration Testing with pytest
    lesson_508 = next(l for l in lessons if l['id'] == 508)
    lesson_508['fullSolution'] = '''# Integration Testing with pytest - Complete Simulation
# In production: pip install pytest
# This lesson simulates integration testing patterns with pytest

import time
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime
import json

# Example 1: Database Integration Testing
print("Example 1: Database Integration Testing")
print("=" * 60)

class TestDatabase:
    """Simulates test database for integration testing."""

    def __init__(self):
        self.data: Dict[str, List[Dict[str, Any]]] = {}
        self.transaction_active = False
        self.transaction_data: Optional[Dict[str, List[Dict[str, Any]]]] = None

    def create_table(self, table_name: str):
        """Create a table in the test database."""
        self.data[table_name] = []

    def insert(self, table: str, record: Dict[str, Any]):
        """Insert a record into a table."""
        if self.transaction_active:
            if table not in self.transaction_data:
                self.transaction_data[table] = []
            self.transaction_data[table].append(record.copy())
        else:
            if table not in self.data:
                self.data[table] = []
            self.data[table].append(record.copy())

    def select_all(self, table: str) -> List[Dict[str, Any]]:
        """Select all records from a table."""
        if self.transaction_active and table in self.transaction_data:
            return self.transaction_data[table].copy()
        return self.data.get(table, []).copy()

    def begin_transaction(self):
        """Start a database transaction."""
        self.transaction_active = True
        self.transaction_data = {}
        # Copy current data
        for table, records in self.data.items():
            self.transaction_data[table] = records.copy()

    def commit(self):
        """Commit the active transaction."""
        if self.transaction_active:
            self.data = self.transaction_data.copy()
            self.transaction_active = False
            self.transaction_data = None

    def rollback(self):
        """Rollback the active transaction."""
        if self.transaction_active:
            self.transaction_active = False
            self.transaction_data = None

    def clear(self):
        """Clear all data from the database."""
        self.data = {}

@dataclass
class DatabaseFixture:
    """pytest-style database fixture."""
    db: TestDatabase

    @classmethod
    def setup(cls):
        """Setup test database."""
        print("  [FIXTURE] Setting up test database")
        db = TestDatabase()
        db.create_table('users')
        db.create_table('posts')
        return cls(db=db)

    def teardown(self):
        """Teardown test database."""
        print("  [FIXTURE] Tearing down test database")
        self.db.clear()

# Create database fixture
db_fixture = DatabaseFixture.setup()

def test_user_creation():
    """Test creating a user in the database."""
    print("  Running: test_user_creation")

    # Arrange
    user = {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'}

    # Act
    db_fixture.db.insert('users', user)

    # Assert
    users = db_fixture.db.select_all('users')
    assert len(users) == 1
    assert users[0]['name'] == 'Alice'

    print("    PASS: User created successfully")

def test_transaction_rollback():
    """Test transaction rollback."""
    print("  Running: test_transaction_rollback")

    # Arrange
    initial_count = len(db_fixture.db.select_all('users'))

    # Act
    db_fixture.db.begin_transaction()
    db_fixture.db.insert('users', {'id': 2, 'name': 'Bob'})

    # Verify data in transaction
    users_in_transaction = db_fixture.db.select_all('users')
    assert len(users_in_transaction) == initial_count + 1

    # Rollback
    db_fixture.db.rollback()

    # Assert
    users_after_rollback = db_fixture.db.select_all('users')
    assert len(users_after_rollback) == initial_count

    print("    PASS: Transaction rollback works")

# Run integration tests
test_user_creation()
test_transaction_rollback()

# Teardown
db_fixture.teardown()
print()

# Example 2: API Integration Testing
print("Example 2: API Integration Testing")
print("=" * 60)

class TestAPIClient:
    """Simulates API client for integration testing."""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.auth_token: Optional[str] = None

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate with the API."""
        if username == "testuser" and password == "testpass":
            self.auth_token = "test_token_123"
            return True
        return False

    def get(self, endpoint: str) -> Dict[str, Any]:
        """Make a GET request to the API."""
        if not self.auth_token:
            raise RuntimeError("Not authenticated")

        # Simulate API response
        return {
            'status': 200,
            'data': {
                'endpoint': endpoint,
                'message': 'Success'
            }
        }

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request to the API."""
        if not self.auth_token:
            raise RuntimeError("Not authenticated")

        return {
            'status': 201,
            'data': {
                'endpoint': endpoint,
                'created': data
            }
        }

@dataclass
class APIFixture:
    """pytest-style API client fixture."""
    client: TestAPIClient

    @classmethod
    def setup(cls):
        """Setup API client."""
        print("  [FIXTURE] Setting up API client")
        client = TestAPIClient("https://api.example.com")
        client.authenticate("testuser", "testpass")
        return cls(client=client)

# Create API fixture
api_fixture = APIFixture.setup()

def test_authenticated_get_request():
    """Test authenticated GET request."""
    print("  Running: test_authenticated_get_request")

    # Act
    response = api_fixture.client.get('/users')

    # Assert
    assert response['status'] == 200
    assert response['data']['endpoint'] == '/users'

    print("    PASS: Authenticated GET request works")

def test_create_resource():
    """Test creating a resource via API."""
    print("  Running: test_create_resource")

    # Arrange
    new_user = {'name': 'Charlie', 'email': 'charlie@example.com'}

    # Act
    response = api_fixture.client.post('/users', new_user)

    # Assert
    assert response['status'] == 201
    assert response['data']['created'] == new_user

    print("    PASS: Resource creation works")

# Run API integration tests
test_authenticated_get_request()
test_create_resource()
print()

# Example 3: Multi-Component Integration
print("Example 3: Multi-Component Integration Testing")
print("=" * 60)

class UserService:
    """User service component."""

    def __init__(self, database):
        self.db = database

    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        """Create a new user."""
        user = {
            'id': len(self.db.select_all('users')) + 1,
            'name': name,
            'email': email,
            'created_at': datetime.now().isoformat()
        }
        self.db.insert('users', user)
        return user

    def get_user(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get a user by ID."""
        users = self.db.select_all('users')
        return next((u for u in users if u['id'] == user_id), None)

class NotificationService:
    """Notification service component."""

    def __init__(self):
        self.sent_notifications: List[Dict[str, Any]] = []

    def send_welcome_email(self, user: Dict[str, Any]):
        """Send welcome email to user."""
        notification = {
            'type': 'welcome_email',
            'recipient': user['email'],
            'subject': f"Welcome {user['name']}!",
            'sent_at': datetime.now().isoformat()
        }
        self.sent_notifications.append(notification)
        return notification

class UserRegistrationWorkflow:
    """Complete user registration workflow."""

    def __init__(self, user_service, notification_service):
        self.user_service = user_service
        self.notification_service = notification_service

    def register_user(self, name: str, email: str) -> Dict[str, Any]:
        """Register a new user (creates user and sends welcome email)."""
        # Create user
        user = self.user_service.create_user(name, email)

        # Send welcome email
        notification = self.notification_service.send_welcome_email(user)

        return {
            'user': user,
            'notification': notification
        }

# Setup fixtures for multi-component test
integration_db = TestDatabase()
integration_db.create_table('users')

user_service = UserService(integration_db)
notification_service = NotificationService()
registration_workflow = UserRegistrationWorkflow(user_service, notification_service)

def test_complete_user_registration():
    """Test complete user registration workflow."""
    print("  Running: test_complete_user_registration")

    # Act
    result = registration_workflow.register_user("Diana", "diana@example.com")

    # Assert - User created
    assert result['user']['name'] == "Diana"
    assert result['user']['email'] == "diana@example.com"

    # Assert - Notification sent
    assert result['notification']['type'] == 'welcome_email'
    assert result['notification']['recipient'] == "diana@example.com"

    # Assert - User can be retrieved
    user = user_service.get_user(result['user']['id'])
    assert user is not None
    assert user['name'] == "Diana"

    # Assert - Notification was recorded
    assert len(notification_service.sent_notifications) == 1

    print("    PASS: Complete workflow integration works")

test_complete_user_registration()
print()

# Example 4: Fixture Scopes
print("Example 4: Fixture Scopes (Session, Module, Function)")
print("=" * 60)

class FixtureScopeDemo:
    """Demonstrates different fixture scopes."""

    session_db = None  # Session-scoped (shared across all tests)
    module_api = None  # Module-scoped (shared within module)

    @classmethod
    def setup_session_fixture(cls):
        """Setup session-scoped fixture (once per test session)."""
        if cls.session_db is None:
            print("  [SESSION] Setting up session database")
            cls.session_db = TestDatabase()
            cls.session_db.create_table('global_data')
        return cls.session_db

    @classmethod
    def setup_module_fixture(cls):
        """Setup module-scoped fixture (once per module)."""
        if cls.module_api is None:
            print("  [MODULE] Setting up module API client")
            cls.module_api = TestAPIClient("https://api.example.com")
            cls.module_api.authenticate("testuser", "testpass")
        return cls.module_api

    @classmethod
    def setup_function_fixture(cls):
        """Setup function-scoped fixture (before each test)."""
        print("  [FUNCTION] Setting up function-specific data")
        return {'test_data': 'fresh for each test'}

    @classmethod
    def teardown_session_fixture(cls):
        """Teardown session-scoped fixture."""
        print("  [SESSION] Tearing down session database")
        cls.session_db = None

# Simulate tests with different scopes
print("Test 1:")
session_db = FixtureScopeDemo.setup_session_fixture()
module_api = FixtureScopeDemo.setup_module_fixture()
func_data = FixtureScopeDemo.setup_function_fixture()
print()

print("Test 2:")
session_db = FixtureScopeDemo.setup_session_fixture()  # Reuses existing
module_api = FixtureScopeDemo.setup_module_fixture()  # Reuses existing
func_data = FixtureScopeDemo.setup_function_fixture()  # Creates new
print()

print("Test 3:")
session_db = FixtureScopeDemo.setup_session_fixture()  # Reuses existing
module_api = FixtureScopeDemo.setup_module_fixture()  # Reuses existing
func_data = FixtureScopeDemo.setup_function_fixture()  # Creates new
print()

# Teardown
FixtureScopeDemo.teardown_session_fixture()
print()

# Example 5: Test Data Factories
print("Example 5: Test Data Factories")
print("=" * 60)

class UserFactory:
    """Factory for creating test users."""

    _counter = 0

    @classmethod
    def create(cls, **overrides):
        """Create a test user with default values."""
        cls._counter += 1
        defaults = {
            'id': cls._counter,
            'name': f'User{cls._counter}',
            'email': f'user{cls._counter}@example.com',
            'active': True,
            'created_at': datetime.now().isoformat()
        }
        defaults.update(overrides)
        return defaults

    @classmethod
    def create_batch(cls, count: int, **overrides):
        """Create multiple test users."""
        return [cls.create(**overrides) for _ in range(count)]

class PostFactory:
    """Factory for creating test posts."""

    _counter = 0

    @classmethod
    def create(cls, author_id: int, **overrides):
        """Create a test post."""
        cls._counter += 1
        defaults = {
            'id': cls._counter,
            'author_id': author_id,
            'title': f'Post {cls._counter}',
            'content': f'Content for post {cls._counter}',
            'published': True,
            'created_at': datetime.now().isoformat()
        }
        defaults.update(overrides)
        return defaults

def test_user_with_posts():
    """Test creating users with associated posts."""
    print("  Running: test_user_with_posts")

    # Create test user
    user = UserFactory.create(name='Author', email='author@example.com')

    # Create posts for user
    posts = [
        PostFactory.create(user['id'], title='First Post'),
        PostFactory.create(user['id'], title='Second Post'),
        PostFactory.create(user['id'], title='Third Post', published=False)
    ]

    # Assert
    assert user['name'] == 'Author'
    assert len(posts) == 3
    assert all(p['author_id'] == user['id'] for p in posts)
    assert posts[0]['published'] is True
    assert posts[2]['published'] is False

    print("    PASS: User with posts created successfully")

test_user_with_posts()
print()

# Example 6: Integration Test Organization
print("Example 6: Integration Test Organization")
print("=" * 60)

class IntegrationTestSuite:
    """Organizes integration tests."""

    def __init__(self):
        self.db = None
        self.results = []

    def setup_suite(self):
        """Setup before all integration tests."""
        print("  [SUITE SETUP] Initializing integration test environment")
        self.db = TestDatabase()
        self.db.create_table('users')
        self.db.create_table('posts')
        self.db.create_table('comments')

    def teardown_suite(self):
        """Teardown after all integration tests."""
        print("  [SUITE TEARDOWN] Cleaning up integration test environment")
        self.db.clear()

    def run_test(self, test_func: Callable, test_name: str):
        """Run a single integration test."""
        print(f"  Running: {test_name}")

        try:
            # Setup transaction for isolation
            self.db.begin_transaction()

            # Run test
            test_func(self.db)

            # Rollback transaction (isolation)
            self.db.rollback()

            self.results.append({'test': test_name, 'status': 'PASS'})
            print(f"    PASS")
        except Exception as e:
            self.db.rollback()
            self.results.append({'test': test_name, 'status': 'FAIL', 'error': str(e)})
            print(f"    FAIL: {e}")

    def print_summary(self):
        """Print test summary."""
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        total = len(self.results)
        print(f"\\n  Integration Tests: {passed}/{total} passed")

# Create test suite
suite = IntegrationTestSuite()
suite.setup_suite()

# Define integration tests
def test_create_user_with_post(db):
    """Integration test: Create user and post."""
    user = UserFactory.create()
    db.insert('users', user)

    post = PostFactory.create(user['id'])
    db.insert('posts', post)

    users = db.select_all('users')
    posts = db.select_all('posts')

    assert len(users) == 1
    assert len(posts) == 1
    assert posts[0]['author_id'] == users[0]['id']

def test_database_relationships(db):
    """Integration test: Test database relationships."""
    user = UserFactory.create()
    db.insert('users', user)

    # Create multiple posts
    for i in range(3):
        post = PostFactory.create(user['id'], title=f'Post {i+1}')
        db.insert('posts', post)

    posts = db.select_all('posts')
    assert len(posts) == 3
    assert all(p['author_id'] == user['id'] for p in posts)

# Run integration tests
suite.run_test(test_create_user_with_post, 'test_create_user_with_post')
suite.run_test(test_database_relationships, 'test_database_relationships')

suite.print_summary()
suite.teardown_suite()
print()

print("=" * 60)
print("INTEGRATION TESTING BEST PRACTICES")
print("=" * 60)
print("""
INTEGRATION TEST PATTERNS:

Database integration:
  @pytest.fixture(scope="function")
  def db(database_session):
      db.begin()
      yield db
      db.rollback()  # Isolate each test

API integration:
  @pytest.fixture
  def api_client():
      client = TestClient(app)
      client.authenticate()
      return client

Multi-component:
  def test_complete_workflow(db, api, cache):
      # Test multiple components together
      pass

TEST ISOLATION:

Transaction rollback:
  - Each test runs in a transaction
  - Rollback after test completes
  - No data pollution between tests

Clean database state:
  - Use factories for test data
  - Clear data after each test
  - Avoid shared mutable state

FIXTURE ORGANIZATION:

conftest.py:
  @pytest.fixture(scope="session")
  def database_engine():
      engine = create_test_engine()
      yield engine
      engine.dispose()

  @pytest.fixture
  def db_session(database_engine):
      session = create_session(database_engine)
      yield session
      session.close()

TEST DATA:

Factories:
  class UserFactory:
      @classmethod
      def create(cls, **overrides):
          defaults = {...}
          defaults.update(overrides)
          return User(**defaults)

Fixtures with data:
  @pytest.fixture
  def sample_user(db):
      user = UserFactory.create()
      db.add(user)
      db.commit()
      return user

COMMON PATTERNS:

Setup/teardown:
  - Session: Database connections
  - Module: Expensive resources
  - Function: Per-test isolation

Dependency injection:
  def test_feature(db, api_client, cache):
      # All dependencies provided
      pass

Production note: Real pytest integration provides:
  - pytest-django for Django apps
  - pytest-flask for Flask apps
  - pytest-postgresql for PostgreSQL
  - Transaction management
  - Fixture parametrization
  - Test database management
  - Parallel test execution
  - Resource pooling
""")
'''

    # Lesson 984: pytest - Parametrize
    lesson_984 = next(l for l in lessons if l['id'] == 984)
    lesson_984['fullSolution'] = '''# pytest Parametrize - Complete Simulation
# In production: pip install pytest
# This lesson simulates parametrized testing with pytest

from typing import List, Tuple, Any, Dict, Callable
from dataclasses import dataclass
import itertools

# Example 1: Basic Parametrization
print("Example 1: Basic Parametrization")
print("=" * 60)

def add(a, b):
    """Simple addition function."""
    return a + b

# Test data - list of (input_a, input_b, expected_result)
test_cases = [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 20, 30),
    (100, 200, 300),
]

print("Parametrized addition tests:")
for i, (a, b, expected) in enumerate(test_cases, 1):
    result = add(a, b)
    status = "PASS" if result == expected else "FAIL"
    print(f"  Test {i}: add({a}, {b}) = {result} (expected {expected}) [{status}]")

print()

# Example 2: Multiple Parameters
print("Example 2: Multiple Parameters")
print("=" * 60)

def validate_email(email: str) -> bool:
    """Validate email format."""
    if not email or '@' not in email:
        return False
    parts = email.split('@')
    if len(parts) != 2:
        return False
    if not parts[0] or not parts[1]:
        return False
    if '.' not in parts[1]:
        return False
    return True

# Test cases: (email, is_valid)
email_test_cases = [
    ("user@example.com", True),
    ("user.name@example.com", True),
    ("user@sub.example.com", True),
    ("invalid", False),
    ("@example.com", False),
    ("user@", False),
    ("user@domain", False),
    ("", False),
]

print("Email validation tests:")
for email, expected_valid in email_test_cases:
    result = validate_email(email)
    status = "PASS" if result == expected_valid else "FAIL"
    expected_str = "valid" if expected_valid else "invalid"
    result_str = "valid" if result else "invalid"
    print(f"  {email!r:30} -> {result_str:7} (expected {expected_str:7}) [{status}]")

print()

# Example 3: Parametrize with IDs
print("Example 3: Parametrize with Test IDs")
print("=" * 60)

@dataclass
class TestCase:
    """Test case with ID and description."""
    id: str
    input_data: Any
    expected: Any
    description: str = ""

def process_string(s: str, uppercase: bool = False) -> str:
    """Process a string."""
    result = s.strip()
    if uppercase:
        result = result.upper()
    return result

# Test cases with IDs
string_test_cases = [
    TestCase(
        id="normal_string",
        input_data=("hello  ", False),
        expected="hello",
        description="Strip whitespace from normal string"
    ),
    TestCase(
        id="uppercase_string",
        input_data=("hello  ", True),
        expected="HELLO",
        description="Strip and uppercase"
    ),
    TestCase(
        id="empty_string",
        input_data=("   ", False),
        expected="",
        description="Handle empty/whitespace string"
    ),
    TestCase(
        id="already_clean",
        input_data=("hello", False),
        expected="hello",
        description="Already clean string"
    ),
]

print("String processing tests:")
for test_case in string_test_cases:
    input_str, uppercase = test_case.input_data
    result = process_string(input_str, uppercase)
    status = "PASS" if result == test_case.expected else "FAIL"
    print(f"  [{test_case.id}] {test_case.description}")
    print(f"    Result: {result!r} (expected {test_case.expected!r}) [{status}]")

print()

# Example 4: Parametrize Combinations
print("Example 4: Parametrize Combinations (Cartesian Product)")
print("=" * 60)

def calculate_discount(price: float, discount_percent: float, member: bool) -> float:
    """Calculate final price with discount."""
    discount = discount_percent
    if member:
        discount += 5  # Additional 5% for members

    return price * (1 - discount / 100)

# Generate all combinations
prices = [100, 200, 500]
discounts = [0, 10, 20]
member_status = [True, False]

print("Discount calculation tests (combinations):")
combinations = list(itertools.product(prices, discounts, member_status))

for price, discount, is_member in combinations[:10]:  # Show first 10
    result = calculate_discount(price, discount, is_member)
    member_str = "member" if is_member else "non-member"
    print(f"  Price ${price}, {discount}% off, {member_str}: ${result:.2f}")

print(f"  ... ({len(combinations)} total combinations)")
print()

# Example 5: Indirect Parametrization
print("Example 5: Indirect Parametrization (Fixture-based)")
print("=" * 60)

class UserRole:
    """User role for testing."""

    def __init__(self, name: str, permissions: List[str]):
        self.name = name
        self.permissions = permissions

    def can(self, permission: str) -> bool:
        """Check if role has permission."""
        return permission in self.permissions

# Role fixtures
roles = {
    'admin': UserRole('admin', ['read', 'write', 'delete', 'admin']),
    'editor': UserRole('editor', ['read', 'write']),
    'viewer': UserRole('viewer', ['read']),
}

# Test cases: (role_name, permission, should_have_access)
permission_tests = [
    ('admin', 'read', True),
    ('admin', 'delete', True),
    ('editor', 'write', True),
    ('editor', 'delete', False),
    ('viewer', 'read', True),
    ('viewer', 'write', False),
]

print("Permission tests:")
for role_name, permission, expected in permission_tests:
    role = roles[role_name]
    result = role.can(permission)
    status = "PASS" if result == expected else "FAIL"
    access = "allowed" if result else "denied"
    print(f"  {role_name:10} {permission:10} -> {access:10} [{status}]")

print()

# Example 6: Parametrize with Marks
print("Example 6: Parametrize with Test Marks")
print("=" * 60)

@dataclass
class MarkedTestCase:
    """Test case with markers."""
    params: Tuple
    expected: Any
    marks: List[str] = None

    def __post_init__(self):
        if self.marks is None:
            self.marks = []

def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

# Test cases with marks
division_tests = [
    MarkedTestCase((10, 2), 5.0, marks=[]),
    MarkedTestCase((100, 10), 10.0, marks=[]),
    MarkedTestCase((1, 3), 0.333, marks=['approximate']),
    MarkedTestCase((10, 0), ZeroDivisionError, marks=['xfail']),  # Expected to fail
    MarkedTestCase((1000000, 1), 1000000.0, marks=['slow']),
]

print("Division tests:")
for i, test in enumerate(division_tests, 1):
    a, b = test.params
    marks_str = f" [{', '.join(test.marks)}]" if test.marks else ""

    try:
        result = divide(a, b)

        if isinstance(test.expected, type) and issubclass(test.expected, Exception):
            # Expected exception but got result
            print(f"  Test {i}: divide({a}, {b}) = {result} [FAIL - expected exception]{marks_str}")
        else:
            # Check result
            if 'approximate' in test.marks:
                # Approximate comparison
                passed = abs(result - test.expected) < 0.001
            else:
                passed = result == test.expected

            status = "PASS" if passed else "FAIL"
            print(f"  Test {i}: divide({a}, {b}) = {result:.3f} (expected {test.expected}) [{status}]{marks_str}")

    except Exception as e:
        if isinstance(test.expected, type) and isinstance(e, test.expected):
            print(f"  Test {i}: divide({a}, {b}) raised {type(e).__name__} [PASS]{marks_str}")
        else:
            print(f"  Test {i}: divide({a}, {b}) raised {type(e).__name__} [FAIL]{marks_str}")

print()

# Example 7: Parametrize Class Methods
print("Example 7: Parametrize Class Methods")
print("=" * 60)

class Calculator:
    """Calculator class for testing."""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

# Test class with parametrized methods
class TestCalculator:
    """Test calculator with parametrized tests."""

    # Test data for each operation
    addition_tests = [(1, 2, 3), (5, 5, 10), (-1, 1, 0)]
    subtraction_tests = [(5, 3, 2), (10, 5, 5), (0, 0, 0)]
    multiplication_tests = [(2, 3, 6), (5, 5, 25), (0, 10, 0)]

    def run_addition_tests(self):
        """Run parametrized addition tests."""
        print("  Addition tests:")
        for a, b, expected in self.addition_tests:
            result = Calculator.add(a, b)
            status = "PASS" if result == expected else "FAIL"
            print(f"    {a} + {b} = {result} (expected {expected}) [{status}]")

    def run_subtraction_tests(self):
        """Run parametrized subtraction tests."""
        print("  Subtraction tests:")
        for a, b, expected in self.subtraction_tests:
            result = Calculator.subtract(a, b)
            status = "PASS" if result == expected else "FAIL"
            print(f"    {a} - {b} = {result} (expected {expected}) [{status}]")

    def run_multiplication_tests(self):
        """Run parametrized multiplication tests."""
        print("  Multiplication tests:")
        for a, b, expected in self.multiplication_tests:
            result = Calculator.multiply(a, b)
            status = "PASS" if result == expected else "FAIL"
            print(f"    {a} * {b} = {result} (expected {expected}) [{status}]")

# Run class tests
test_calc = TestCalculator()
test_calc.run_addition_tests()
test_calc.run_subtraction_tests()
test_calc.run_multiplication_tests()
print()

# Example 8: Dynamic Test Generation
print("Example 8: Dynamic Test Generation")
print("=" * 60)

class TestGenerator:
    """Generates tests dynamically."""

    @staticmethod
    def generate_range_tests(start: int, end: int, func: Callable) -> List[tuple]:
        """Generate test cases for a range of values."""
        return [(i, func(i)) for i in range(start, end + 1)]

    @staticmethod
    def generate_boundary_tests(boundaries: List[int], func: Callable) -> List[tuple]:
        """Generate tests for boundary values."""
        tests = []
        for boundary in boundaries:
            tests.append((boundary - 1, func(boundary - 1)))
            tests.append((boundary, func(boundary)))
            tests.append((boundary + 1, func(boundary + 1)))
        return tests

def is_even(n: int) -> bool:
    """Check if number is even."""
    return n % 2 == 0

# Generate tests dynamically
print("Dynamically generated tests:")

# Range tests
range_tests = TestGenerator.generate_range_tests(0, 5, is_even)
print("  Range tests (0-5):")
for value, expected in range_tests:
    result = is_even(value)
    status = "PASS" if result == expected else "FAIL"
    print(f"    is_even({value}) = {result} [{status}]")

# Boundary tests
boundary_tests = TestGenerator.generate_boundary_tests([10, 100], is_even)
print("  Boundary tests (around 10, 100):")
for value, expected in boundary_tests[:6]:  # Show first 6
    result = is_even(value)
    status = "PASS" if result == expected else "FAIL"
    print(f"    is_even({value}) = {result} [{status}]")

print()

# Example 9: Fixture Parametrization
print("Example 9: Fixture Parametrization")
print("=" * 60)

class DatabaseConfig:
    """Database configuration."""

    def __init__(self, db_type: str, host: str, port: int):
        self.db_type = db_type
        self.host = host
        self.port = port

    def __repr__(self):
        return f"{self.db_type}://{self.host}:{self.port}"

# Parametrize database configs
db_configs = [
    DatabaseConfig('postgresql', 'localhost', 5432),
    DatabaseConfig('mysql', 'localhost', 3306),
    DatabaseConfig('sqlite', 'memory', 0),
]

print("Testing with multiple database configurations:")
for config in db_configs:
    print(f"  Testing with {config}")
    print(f"    Connection string: {config}")
    print(f"    Status: PASS")

print()

# Example 10: Best Practices Summary
print("Example 10: Parametrization Best Practices")
print("=" * 60)

best_practices = """
1. Use descriptive test IDs:
   - Helps identify failing tests
   - Makes test reports readable
   - Example: "valid_email", "invalid_format", etc.

2. Group related test cases:
   - Keep similar tests together
   - Use test classes for organization
   - Separate by feature or component

3. Test edge cases:
   - Boundary values
   - Empty inputs
   - Maximum values
   - Invalid inputs

4. Use appropriate granularity:
   - Not too many parameters (hard to debug)
   - Not too few (miss edge cases)
   - Balance coverage and clarity

5. Combine with fixtures:
   - Parametrize fixtures for setup variations
   - Share common setup across parametrized tests
   - Use indirect parametrization when needed
"""

print(best_practices)

print("=" * 60)
print("PARAMETRIZE PATTERNS")
print("=" * 60)
print("""
BASIC PARAMETRIZATION:

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert double(input) == expected

MULTIPLE PARAMETERS:

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

WITH TEST IDS:

@pytest.mark.parametrize(
    "email,valid",
    [
        ("user@example.com", True),
        ("invalid", False),
    ],
    ids=["valid_email", "invalid_format"]
)
def test_email(email, valid):
    assert validate(email) == valid

COMBINATIONS:

@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_combo(x, y):
    # Tests: (1,3), (1,4), (2,3), (2,4)
    assert x * y > 0

INDIRECT PARAMETRIZATION:

@pytest.fixture
def user(request):
    return create_user(request.param)

@pytest.mark.parametrize(
    "user",
    ["admin", "editor"],
    indirect=True
)
def test_user(user):
    assert user.role in ["admin", "editor"]

WITH MARKS:

@pytest.mark.parametrize(
    "input,expected",
    [
        (1, 2),
        pytest.param(1000000, 2000000, marks=pytest.mark.slow),
        pytest.param(0, 0, marks=pytest.mark.xfail),
    ]
)
def test_with_marks(input, expected):
    assert double(input) == expected

Production note: Real pytest.mark.parametrize provides:
  - Test ID generation
  - Mark support (skip, xfail, etc.)
  - Indirect parametrization
  - Fixture parametrization
  - Combination support
  - Custom ID functions
  - Lazy evaluation
  - Test filtering
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 18 PART 2 COMPLETE: Integration Testing and Parametrize")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 508: Integration Testing with pytest")
    print(f"  - Lesson 984: pytest - Parametrize")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
