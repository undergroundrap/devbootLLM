import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons
lesson_774 = next(l for l in lessons if l['id'] == 774)  # Django Testing Strategies
lesson_751 = next(l for l in lessons if l['id'] == 751)  # Flask Production Deployment
lesson_769 = next(l for l in lessons if l['id'] == 769)  # Django DRF Custom Permissions

# Lesson 774: Django Testing Strategies
lesson_774['fullSolution'] = '''"""
Django Testing Strategies - Comprehensive Guide

Covers unit tests, integration tests, test fixtures, mocking, test client,
database testing, API testing, test coverage, CI/CD testing, and best practices.

**Zero Package Installation Required**
"""

from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
import json

# Example 1: Basic Unit Testing
print("="*60)
print("Example 1: Basic Unit Testing")
print("="*60)

class TestCase:
    """Base test case class."""

    def __init__(self, name: str):
        self.name = name
        self.passed = []
        self.failed = []

    def assertEqual(self, actual, expected, msg=""):
        """Assert that two values are equal."""
        if actual == expected:
            self.passed.append(f"✓ {msg or f'{actual} == {expected}'}")
            print(f"  ✓ PASS: {msg or f'{actual} == {expected}'}")
        else:
            self.failed.append(f"✗ {msg or f'{actual} != {expected}'}")
            print(f"  ✗ FAIL: {msg or f'{actual} != {expected} (got {actual})'}")

    def assertTrue(self, value, msg=""):
        """Assert that value is True."""
        if value:
            self.passed.append(f"✓ {msg or 'Value is True'}")
            print(f"  ✓ PASS: {msg or 'Value is True'}")
        else:
            self.failed.append(f"✗ {msg or 'Value is False'}")
            print(f"  ✗ FAIL: {msg or 'Value is not True'}")

    def assertFalse(self, value, msg=""):
        """Assert that value is False."""
        if not value:
            self.passed.append(f"✓ {msg or 'Value is False'}")
            print(f"  ✓ PASS: {msg or 'Value is False'}")
        else:
            self.failed.append(f"✗ {msg or 'Value is True'}")
            print(f"  ✗ FAIL: {msg or 'Value is not False'}")

    def summary(self):
        """Print test summary."""
        total = len(self.passed) + len(self.failed)
        print(f"\\n  Summary: {len(self.passed)}/{total} tests passed")

# Simple model to test
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.is_active = True

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

# Test the User model
print("\\nTesting User model:")
test = TestCase("UserTests")

user = User("alice", "alice@example.com")
test.assertEqual(user.username, "alice", "Username should be alice")
test.assertEqual(user.email, "alice@example.com", "Email should match")
test.assertTrue(user.is_active, "User should be active by default")

user.deactivate()
test.assertFalse(user.is_active, "User should be inactive after deactivation")

test.summary()
print()

# Example 2: Test Fixtures
print("="*60)
print("Example 2: Test Fixtures")
print("="*60)

class TestFixtures:
    """Test fixture management."""

    @staticmethod
    def setUp():
        """Set up test fixtures before each test."""
        print("  [SETUP] Creating test data...")
        return {
            'users': [
                {'id': 1, 'username': 'alice', 'role': 'admin'},
                {'id': 2, 'username': 'bob', 'role': 'user'},
            ],
            'posts': [
                {'id': 1, 'title': 'First Post', 'author_id': 1},
                {'id': 2, 'title': 'Second Post', 'author_id': 2},
            ]
        }

    @staticmethod
    def tearDown(data):
        """Clean up after each test."""
        print("  [TEARDOWN] Cleaning up test data...")
        data.clear()

# Using fixtures
print("\\nUsing test fixtures:")
fixtures = TestFixtures.setUp()
print(f"  Created {len(fixtures['users'])} users")
print(f"  Created {len(fixtures['posts'])} posts")

# Run tests with fixtures
test = TestCase("FixtureTests")
test.assertEqual(len(fixtures['users']), 2, "Should have 2 users")
test.assertEqual(fixtures['users'][0]['username'], 'alice', "First user is alice")

TestFixtures.tearDown(fixtures)
print(f"  Fixtures cleaned: {len(fixtures)} items remain")
print()

# Example 3: Mocking
print("="*60)
print("Example 3: Mocking")
print("="*60)

class Mock:
    """Simple mock object."""

    def __init__(self, return_value=None):
        self.return_value = return_value
        self.called = False
        self.call_count = 0
        self.call_args = []

    def __call__(self, *args, **kwargs):
        """Record call and return mock value."""
        self.called = True
        self.call_count += 1
        self.call_args.append((args, kwargs))
        print(f"  [MOCK] Called with args={args}, kwargs={kwargs}")
        return self.return_value

# Example service that makes external API call
class EmailService:
    def send_email(self, to: str, subject: str, body: str) -> bool:
        """Send email (would normally call external service)."""
        # In real app, this would call external API
        print(f"  [EMAIL] Sending to {to}: {subject}")
        return True

# Test with mock
print("\\nTesting with mocks:")
mock_send = Mock(return_value=True)

# Replace real method with mock
EmailService.send_email = mock_send

# Use the mocked service
service = EmailService()
result = service.send_email("user@example.com", "Test", "Hello")

print(f"  Mock was called: {mock_send.called}")
print(f"  Call count: {mock_send.call_count}")
print(f"  Return value: {result}")
print()

# Example 4: Test Client for HTTP Requests
print("="*60)
print("Example 4: Test Client for HTTP Requests")
print("="*60)

class TestClient:
    """Simulated test client for making requests."""

    def __init__(self, app):
        self.app = app

    def get(self, path: str, **kwargs) -> Dict:
        """Make GET request."""
        print(f"  [CLIENT] GET {path}")
        return self.app.handle_request('GET', path, kwargs)

    def post(self, path: str, data: Dict = None, **kwargs) -> Dict:
        """Make POST request."""
        print(f"  [CLIENT] POST {path}")
        return self.app.handle_request('POST', path, data or {})

    def put(self, path: str, data: Dict = None, **kwargs) -> Dict:
        """Make PUT request."""
        print(f"  [CLIENT] PUT {path}")
        return self.app.handle_request('PUT', path, data or {})

    def delete(self, path: str, **kwargs) -> Dict:
        """Make DELETE request."""
        print(f"  [CLIENT] DELETE {path}")
        return self.app.handle_request('DELETE', path, {})

class SimpleApp:
    """Simple app for testing."""

    def __init__(self):
        self.routes = {
            ('GET', '/api/users'): lambda d: {'status': 200, 'data': [{'id': 1, 'name': 'Alice'}]},
            ('POST', '/api/users'): lambda d: {'status': 201, 'data': d},
            ('GET', '/api/users/1'): lambda d: {'status': 200, 'data': {'id': 1, 'name': 'Alice'}},
        }

    def handle_request(self, method: str, path: str, data: Dict) -> Dict:
        """Handle request."""
        handler = self.routes.get((method, path))
        if handler:
            return handler(data)
        return {'status': 404, 'error': 'Not found'}

# Test API endpoints
print("\\nTesting API with test client:")
app = SimpleApp()
client = TestClient(app)

test = TestCase("APITests")

# Test GET endpoint
response = client.get('/api/users')
test.assertEqual(response['status'], 200, "GET /api/users should return 200")
test.assertTrue(len(response['data']) > 0, "Should return users list")

# Test POST endpoint
response = client.post('/api/users', data={'name': 'Bob'})
test.assertEqual(response['status'], 201, "POST should return 201")
test.assertEqual(response['data']['name'], 'Bob', "Should return posted data")

test.summary()
print()

# Example 5: Database Testing
print("="*60)
print("Example 5: Database Testing")
print("="*60)

class TestDatabase:
    """Simulated test database."""

    def __init__(self):
        self.data = {}
        self.transaction_active = False

    def begin_transaction(self):
        """Start transaction."""
        self.transaction_active = True
        self._backup = json.dumps(self.data)
        print("  [DB] Transaction started")

    def commit(self):
        """Commit transaction."""
        self.transaction_active = False
        print("  [DB] Transaction committed")

    def rollback(self):
        """Rollback transaction."""
        if self.transaction_active:
            self.data = json.loads(self._backup)
            self.transaction_active = False
            print("  [DB] Transaction rolled back")

    def insert(self, table: str, record: Dict):
        """Insert record."""
        if table not in self.data:
            self.data[table] = []
        self.data[table].append(record)
        print(f"  [DB] Inserted into {table}: {record}")

    def select(self, table: str) -> List[Dict]:
        """Select all records."""
        return self.data.get(table, [])

# Test database operations
print("\\nTesting database operations:")
db = TestDatabase()

test = TestCase("DatabaseTests")

# Test transaction rollback
db.begin_transaction()
db.insert('users', {'id': 1, 'name': 'Alice'})
db.insert('users', {'id': 2, 'name': 'Bob'})
test.assertEqual(len(db.select('users')), 2, "Should have 2 users")

db.rollback()
test.assertEqual(len(db.select('users')), 0, "Should have 0 users after rollback")

# Test transaction commit
db.begin_transaction()
db.insert('users', {'id': 1, 'name': 'Alice'})
db.commit()
test.assertEqual(len(db.select('users')), 1, "Should have 1 user after commit")

test.summary()
print()

# Example 6: Testing Async Code
print("="*60)
print("Example 6: Testing Async Code")
print("="*60)

class AsyncTestCase:
    """Test case for async code."""

    @staticmethod
    def run_async(coro):
        """Simulate running async code."""
        # In real testing, would use asyncio.run()
        print(f"  [ASYNC] Running coroutine: {coro.__name__}")
        return coro()

def async_fetch_user():
    """Simulate async user fetch."""
    print("  [ASYNC] Fetching user data...")
    return {'id': 1, 'name': 'Alice'}

def async_save_user():
    """Simulate async user save."""
    print("  [ASYNC] Saving user data...")
    return True

# Test async functions
print("\\nTesting async functions:")
test = TestCase("AsyncTests")

result = AsyncTestCase.run_async(async_fetch_user)
test.assertEqual(result['name'], 'Alice', "Should fetch user data")

result = AsyncTestCase.run_async(async_save_user)
test.assertTrue(result, "Should save successfully")

test.summary()
print()

# Example 7: API Integration Testing
print("="*60)
print("Example 7: API Integration Testing")
print("="*60)

class IntegrationTestCase:
    """Integration test case."""

    def __init__(self):
        self.client = None
        self.db = None

    def setUp(self):
        """Set up integration test environment."""
        print("  [SETUP] Setting up integration test environment")
        self.db = TestDatabase()
        self.db.begin_transaction()

        # Seed database
        self.db.insert('users', {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'})
        self.db.insert('posts', {'id': 1, 'user_id': 1, 'title': 'First Post'})

    def tearDown(self):
        """Clean up after integration test."""
        print("  [TEARDOWN] Cleaning up integration test environment")
        if self.db:
            self.db.rollback()

# Run integration test
print("\\nRunning integration test:")
integration = IntegrationTestCase()
integration.setUp()

test = TestCase("IntegrationTests")

# Test user exists
users = integration.db.select('users')
test.assertEqual(len(users), 1, "Should have 1 user")

# Test post belongs to user
posts = integration.db.select('posts')
test.assertEqual(posts[0]['user_id'], 1, "Post should belong to user 1")

integration.tearDown()
test.summary()
print()

# Example 8: Test Coverage Simulation
print("="*60)
print("Example 8: Test Coverage Simulation")
print("="*60)

class CoverageTracker:
    """Track code coverage."""

    def __init__(self):
        self.executed_lines = set()
        self.total_lines = 0

    def mark_executed(self, line_number: int):
        """Mark line as executed."""
        self.executed_lines.add(line_number)

    def report(self) -> float:
        """Generate coverage report."""
        if self.total_lines == 0:
            return 0.0
        coverage = (len(self.executed_lines) / self.total_lines) * 100
        print(f"  [COVERAGE] {len(self.executed_lines)}/{self.total_lines} lines executed")
        print(f"  [COVERAGE] {coverage:.1f}% coverage")
        return coverage

# Simulate coverage tracking
print("\\nTracking test coverage:")
coverage = CoverageTracker()
coverage.total_lines = 10

# Simulate executing different code paths
coverage.mark_executed(1)
coverage.mark_executed(2)
coverage.mark_executed(3)
coverage.mark_executed(5)
coverage.mark_executed(7)
coverage.mark_executed(8)

result = coverage.report()

test = TestCase("CoverageTests")
test.assertTrue(result >= 50, "Coverage should be at least 50%")
test.summary()
print()

# Example 9: Parameterized Testing
print("="*60)
print("Example 9: Parameterized Testing")
print("="*60)

class ParameterizedTest:
    """Run tests with multiple parameter sets."""

    @staticmethod
    def run_with_params(test_func: Callable, params: List[tuple]):
        """Run test with multiple parameter sets."""
        passed = 0
        failed = 0

        for i, param_set in enumerate(params, 1):
            print(f"  [TEST {i}] Running with params: {param_set}")
            try:
                result = test_func(*param_set)
                if result:
                    print(f"  ✓ PASS")
                    passed += 1
                else:
                    print(f"  ✗ FAIL")
                    failed += 1
            except Exception as e:
                print(f"  ✗ ERROR: {e}")
                failed += 1

        print(f"\\n  Results: {passed} passed, {failed} failed")
        return passed, failed

# Test function
def validate_email(email: str) -> bool:
    """Validate email format."""
    return '@' in email and '.' in email.split('@')[1]

# Run parameterized tests
print("\\nRunning parameterized email validation tests:")

test_params = [
    ("user@example.com", True),
    ("invalid.email", False),
    ("another@test.org", True),
    ("bad@", False),
]

def email_test(email: str, expected: bool) -> bool:
    """Test email validation."""
    result = validate_email(email)
    return result == expected

ParameterizedTest.run_with_params(email_test, test_params)
print()

# Example 10: CI/CD Testing Pipeline
print("="*60)
print("Example 10: CI/CD Testing Pipeline")
print("="*60)

class TestPipeline:
    """Simulate CI/CD test pipeline."""

    def __init__(self):
        self.stages = []
        self.results = {}

    def add_stage(self, name: str, tests: List[Callable]):
        """Add test stage to pipeline."""
        self.stages.append((name, tests))

    def run(self):
        """Run entire test pipeline."""
        print("  [PIPELINE] Starting test pipeline\\n")
        all_passed = True

        for stage_name, tests in self.stages:
            print(f"  [STAGE] Running: {stage_name}")
            stage_passed = True

            for test in tests:
                try:
                    result = test()
                    if result:
                        print(f"    ✓ {test.__name__} passed")
                    else:
                        print(f"    ✗ {test.__name__} failed")
                        stage_passed = False
                        all_passed = False
                except Exception as e:
                    print(f"    ✗ {test.__name__} error: {e}")
                    stage_passed = False
                    all_passed = False

            self.results[stage_name] = stage_passed
            status = "PASSED" if stage_passed else "FAILED"
            print(f"  [STAGE] {stage_name}: {status}\\n")

            # Stop pipeline if stage fails
            if not stage_passed:
                print(f"  [PIPELINE] Stopped due to failure in {stage_name}")
                return False

        print(f"  [PIPELINE] All stages passed!")
        return all_passed

# Define test functions for pipeline
def unit_tests():
    """Run unit tests."""
    return True

def integration_tests():
    """Run integration tests."""
    return True

def api_tests():
    """Run API tests."""
    return True

def security_tests():
    """Run security tests."""
    return True

# Run test pipeline
print("\\nRunning CI/CD test pipeline:")
pipeline = TestPipeline()

pipeline.add_stage("Unit Tests", [unit_tests])
pipeline.add_stage("Integration Tests", [integration_tests])
pipeline.add_stage("API Tests", [api_tests])
pipeline.add_stage("Security Tests", [security_tests])

success = pipeline.run()
print(f"  Pipeline result: {'SUCCESS' if success else 'FAILURE'}")

print("\\n" + "="*60)
print("All Django Testing Strategies examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 774: Django Testing Strategies ({len(lesson_774['fullSolution']):,} chars)")

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

# Lesson 751: Flask Production Deployment
lesson_751['fullSolution'] = '''"""
Flask Production Deployment - Comprehensive Guide

Covers WSGI servers (Gunicorn, uWSGI), reverse proxy (Nginx), process managers,
load balancing, SSL/TLS, environment config, logging, monitoring, Docker deployment,
and production best practices.

**Zero Package Installation Required**
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import json

# Example 1: WSGI Server Configuration
print("="*60)
print("Example 1: WSGI Server Configuration")
print("="*60)

class WSGIServer:
    """Simulated WSGI server (like Gunicorn)."""

    def __init__(self, app, workers=4, bind="0.0.0.0:8000"):
        self.app = app
        self.workers = workers
        self.bind = bind
        self.worker_processes = []

    def start(self):
        """Start WSGI server."""
        print(f"  [SERVER] Starting WSGI server")
        print(f"  Workers: {self.workers}")
        print(f"  Binding: {self.bind}")

        for i in range(self.workers):
            worker = {
                'id': i + 1,
                'pid': 1000 + i,
                'status': 'running',
                'requests_handled': 0
            }
            self.worker_processes.append(worker)
            print(f"  [WORKER {worker['id']}] Started (PID: {worker['pid']})")

    def handle_request(self, request: Dict):
        """Distribute request to worker."""
        # Simple round-robin
        worker = self.worker_processes[0]
        worker['requests_handled'] += 1
        self.worker_processes.append(self.worker_processes.pop(0))

        print(f"  [WORKER {worker['id']}] Handling request to {request['path']}")
        return self.app(request)

    def stats(self):
        """Show server statistics."""
        total_requests = sum(w['requests_handled'] for w in self.worker_processes)
        print(f"\\n  [STATS] Total requests: {total_requests}")
        for worker in self.worker_processes:
            print(f"  Worker {worker['id']}: {worker['requests_handled']} requests")

# Simple WSGI app
def simple_app(environ):
    """Simple WSGI application."""
    return {
        'status': 200,
        'body': f"Hello from {environ['path']}",
        'headers': {'Content-Type': 'text/plain'}
    }

# Start WSGI server
print("\\nStarting production WSGI server:")
server = WSGIServer(simple_app, workers=4)
server.start()

# Simulate requests
print("\\nHandling requests:")
for i in range(10):
    server.handle_request({'path': f'/api/item/{i}', 'method': 'GET'})

server.stats()
print()

# Example 2: Reverse Proxy Configuration
print("="*60)
print("Example 2: Reverse Proxy Configuration")
print("="*60)

class ReverseProxy:
    """Simulated Nginx reverse proxy."""

    def __init__(self, upstream_servers: List[str]):
        self.upstream_servers = upstream_servers
        self.current_server = 0
        self.cache = {}

    def proxy_request(self, request: Dict) -> Dict:
        """Proxy request to upstream server."""
        # Check cache
        cache_key = f"{request['method']}:{request['path']}"
        if cache_key in self.cache:
            print(f"  [CACHE HIT] Returning cached response for {cache_key}")
            return self.cache[cache_key]

        # Load balance to upstream
        upstream = self.upstream_servers[self.current_server]
        self.current_server = (self.current_server + 1) % len(self.upstream_servers)

        print(f"  [PROXY] Forwarding to {upstream} -> {request['path']}")

        # Simulate upstream response
        response = {
            'status': 200,
            'body': f"Response from {upstream}",
            'headers': {
                'X-Upstream-Server': upstream,
                'X-Cache': 'MISS'
            }
        }

        # Cache GET requests
        if request['method'] == 'GET':
            self.cache[cache_key] = response

        return response

    def configure_ssl(self, cert_path: str, key_path: str):
        """Configure SSL/TLS."""
        print(f"  [SSL] Configured with cert: {cert_path}")
        print(f"  [SSL] Private key: {key_path}")
        print(f"  [SSL] TLS 1.2+ enforced")

# Configure reverse proxy
print("\\nConfiguring reverse proxy:")
proxy = ReverseProxy([
    'http://127.0.0.1:8001',
    'http://127.0.0.1:8002',
    'http://127.0.0.1:8003'
])

proxy.configure_ssl('/etc/ssl/cert.pem', '/etc/ssl/key.pem')

# Handle requests through proxy
print("\\nProxying requests:")
for i in range(5):
    response = proxy.proxy_request({'path': f'/api/data', 'method': 'GET'})
    print(f"  Response from: {response['headers']['X-Upstream-Server']}")

print()

# Example 3: Environment Configuration
print("="*60)
print("Example 3: Environment Configuration")
print("="*60)

class ConfigManager:
    """Manage environment-specific configuration."""

    def __init__(self, env: str = 'production'):
        self.env = env
        self.config = {}
        self.load_config()

    def load_config(self):
        """Load environment-specific config."""
        print(f"  [CONFIG] Loading {self.env} configuration")

        base_config = {
            'APP_NAME': 'MyFlaskApp',
            'DEBUG': False,
            'TESTING': False
        }

        env_configs = {
            'development': {
                **base_config,
                'DEBUG': True,
                'DATABASE_URL': 'sqlite:///dev.db',
                'LOG_LEVEL': 'DEBUG',
                'SECRET_KEY': 'dev-secret-key-change-in-prod'
            },
            'production': {
                **base_config,
                'DATABASE_URL': 'postgresql://prod-db:5432/myapp',
                'LOG_LEVEL': 'WARNING',
                'SECRET_KEY': 'prod-secret-key-from-env',
                'SSL_REQUIRED': True,
                'SESSION_COOKIE_SECURE': True,
                'SESSION_COOKIE_HTTPONLY': True,
                'PERMANENT_SESSION_LIFETIME': 3600
            },
            'testing': {
                **base_config,
                'TESTING': True,
                'DATABASE_URL': 'sqlite:///:memory:',
                'LOG_LEVEL': 'ERROR'
            }
        }

        self.config = env_configs.get(self.env, base_config)

        for key, value in self.config.items():
            print(f"    {key}: {value}")

    def get(self, key: str, default=None):
        """Get configuration value."""
        return self.config.get(key, default)

# Load production config
print("\\nLoading production configuration:")
config = ConfigManager('production')

print("\\n  Security settings:")
print(f"  SSL Required: {config.get('SSL_REQUIRED')}")
print(f"  Secure Cookies: {config.get('SESSION_COOKIE_SECURE')}")
print(f"  HTTP Only Cookies: {config.get('SESSION_COOKIE_HTTPONLY')}")
print()

# Example 4: Logging Configuration
print("="*60)
print("Example 4: Logging Configuration")
print("="*60)

class ProductionLogger:
    """Production logging system."""

    def __init__(self, app_name: str, log_level: str = 'INFO'):
        self.app_name = app_name
        self.log_level = log_level
        self.logs = []
        self.log_levels = {'DEBUG': 0, 'INFO': 1, 'WARNING': 2, 'ERROR': 3, 'CRITICAL': 4}

    def _should_log(self, level: str) -> bool:
        """Check if message should be logged."""
        return self.log_levels.get(level, 0) >= self.log_levels.get(self.log_level, 1)

    def _format_log(self, level: str, message: str, **kwargs) -> str:
        """Format log message."""
        timestamp = datetime.now().isoformat()
        extra = ' '.join(f'{k}={v}' for k, v in kwargs.items())
        return f"[{timestamp}] {level} - {self.app_name} - {message} {extra}"

    def debug(self, message: str, **kwargs):
        """Log debug message."""
        if self._should_log('DEBUG'):
            log = self._format_log('DEBUG', message, **kwargs)
            self.logs.append(log)
            print(f"  {log}")

    def info(self, message: str, **kwargs):
        """Log info message."""
        if self._should_log('INFO'):
            log = self._format_log('INFO', message, **kwargs)
            self.logs.append(log)
            print(f"  {log}")

    def warning(self, message: str, **kwargs):
        """Log warning message."""
        if self._should_log('WARNING'):
            log = self._format_log('WARNING', message, **kwargs)
            self.logs.append(log)
            print(f"  {log}")

    def error(self, message: str, **kwargs):
        """Log error message."""
        if self._should_log('ERROR'):
            log = self._format_log('ERROR', message, **kwargs)
            self.logs.append(log)
            print(f"  {log}")

# Configure production logging
print("\\nProduction logging:")
logger = ProductionLogger('MyFlaskApp', log_level='WARNING')

logger.debug("This won't be logged in production")
logger.info("This won't be logged either")
logger.warning("High memory usage detected", memory_mb=512, threshold_mb=400)
logger.error("Database connection failed", db_host='prod-db', error='Connection timeout')

print(f"\\n  Total logs: {len(logger.logs)}")
print()

# Example 5: Health Checks and Monitoring
print("="*60)
print("Example 5: Health Checks and Monitoring")
print("="*60)

class HealthCheck:
    """Application health check system."""

    def __init__(self):
        self.checks = {}

    def register_check(self, name: str, check_func):
        """Register health check."""
        self.checks[name] = check_func

    def run_checks(self) -> Dict:
        """Run all health checks."""
        results = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'checks': {}
        }

        print("  [HEALTH] Running health checks...")

        for name, check_func in self.checks.items():
            try:
                check_result = check_func()
                results['checks'][name] = {
                    'status': 'pass' if check_result else 'fail',
                    'checked_at': datetime.now().isoformat()
                }
                status = '✓' if check_result else '✗'
                print(f"  {status} {name}: {'PASS' if check_result else 'FAIL'}")

                if not check_result:
                    results['status'] = 'unhealthy'
            except Exception as e:
                results['checks'][name] = {
                    'status': 'error',
                    'error': str(e)
                }
                results['status'] = 'unhealthy'
                print(f"  ✗ {name}: ERROR - {e}")

        return results

# Define health checks
def check_database():
    """Check database connectivity."""
    # Simulate database check
    return True

def check_redis():
    """Check Redis connectivity."""
    # Simulate Redis check
    return True

def check_disk_space():
    """Check available disk space."""
    # Simulate disk space check
    return True

# Run health checks
print("\\nRunning health checks:")
health = HealthCheck()
health.register_check('database', check_database)
health.register_check('redis', check_redis)
health.register_check('disk_space', check_disk_space)

result = health.run_checks()
print(f"\\n  Overall status: {result['status'].upper()}")
print()

# Example 6: Load Balancing
print("="*60)
print("Example 6: Load Balancing")
print("="*60)

class LoadBalancer:
    """Load balancer with multiple strategies."""

    def __init__(self, servers: List[Dict], strategy='round_robin'):
        self.servers = servers
        self.strategy = strategy
        self.current_index = 0

    def get_server_round_robin(self) -> Dict:
        """Round-robin load balancing."""
        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers)
        return server

    def get_server_least_connections(self) -> Dict:
        """Least connections load balancing."""
        return min(self.servers, key=lambda s: s['connections'])

    def get_server_weighted(self) -> Dict:
        """Weighted load balancing."""
        total_weight = sum(s['weight'] for s in self.servers)
        # Simplified weighted selection
        return max(self.servers, key=lambda s: s['weight'])

    def get_server(self) -> Dict:
        """Get server based on strategy."""
        if self.strategy == 'round_robin':
            return self.get_server_round_robin()
        elif self.strategy == 'least_connections':
            return self.get_server_least_connections()
        elif self.strategy == 'weighted':
            return self.get_server_weighted()

    def handle_request(self, request: Dict):
        """Handle request with load balancing."""
        server = self.get_server()
        server['connections'] += 1
        server['requests_handled'] += 1

        print(f"  [LB] Routing to {server['name']} (connections: {server['connections']})")

        # Simulate processing
        server['connections'] -= 1

# Configure load balancer
print("\\nConfiguring load balancer:")
servers = [
    {'name': 'server-1', 'weight': 3, 'connections': 0, 'requests_handled': 0},
    {'name': 'server-2', 'weight': 2, 'connections': 0, 'requests_handled': 0},
    {'name': 'server-3', 'weight': 1, 'connections': 0, 'requests_handled': 0},
]

lb = LoadBalancer(servers, strategy='round_robin')

print("\\nDistributing requests (round-robin):")
for i in range(9):
    lb.handle_request({'path': f'/api/request/{i}'})

print("\\n  Request distribution:")
for server in servers:
    print(f"  {server['name']}: {server['requests_handled']} requests")
print()

# Example 7: Process Management
print("="*60)
print("Example 7: Process Management")
print("="*60)

class ProcessManager:
    """Manage application processes (like systemd/supervisor)."""

    def __init__(self):
        self.processes = {}

    def start_process(self, name: str, command: str):
        """Start a process."""
        process = {
            'name': name,
            'command': command,
            'pid': len(self.processes) + 1000,
            'status': 'running',
            'restarts': 0,
            'started_at': datetime.now().isoformat()
        }
        self.processes[name] = process
        print(f"  [PM] Started {name} (PID: {process['pid']})")

    def stop_process(self, name: str):
        """Stop a process."""
        if name in self.processes:
            self.processes[name]['status'] = 'stopped'
            print(f"  [PM] Stopped {name}")

    def restart_process(self, name: str):
        """Restart a process."""
        if name in self.processes:
            self.processes[name]['restarts'] += 1
            self.processes[name]['started_at'] = datetime.now().isoformat()
            print(f"  [PM] Restarted {name} (restart #{self.processes[name]['restarts']})")

    def status(self):
        """Show process status."""
        print("\\n  Process Status:")
        for name, proc in self.processes.items():
            print(f"  {name}: {proc['status']} (PID: {proc['pid']}, restarts: {proc['restarts']})")

# Manage processes
print("\\nManaging application processes:")
pm = ProcessManager()

pm.start_process('gunicorn', 'gunicorn app:app -w 4')
pm.start_process('celery-worker', 'celery -A app worker')
pm.start_process('celery-beat', 'celery -A app beat')

pm.status()

print("\\nRestarting gunicorn:")
pm.restart_process('gunicorn')

pm.status()
print()

# Example 8: Docker Deployment
print("="*60)
print("Example 8: Docker Deployment")
print("="*60)

class DockerDeployment:
    """Simulate Docker deployment."""

    @staticmethod
    def build_dockerfile() -> str:
        """Generate production Dockerfile."""
        dockerfile = """FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \\\\
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Run application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
"""
        return dockerfile

    @staticmethod
    def build_docker_compose() -> str:
        """Generate docker-compose for production."""
        compose = """version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://db:5432/myapp
    depends_on:
      - db
      - redis
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_PASSWORD=secret
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7
    restart: unless-stopped

  nginx:
    image: nginx:latest
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - web
    restart: unless-stopped

volumes:
  postgres_data:
"""
        return compose

# Show Docker deployment files
print("\\nProduction Dockerfile:")
print(DockerDeployment.build_dockerfile())

print("\\nDocker Compose configuration:")
print(DockerDeployment.build_docker_compose())
print()

# Example 9: Security Hardening
print("="*60)
print("Example 9: Security Hardening")
print("="*60)

class SecurityHardening:
    """Production security configuration."""

    @staticmethod
    def configure_headers() -> Dict[str, str]:
        """Configure security headers."""
        headers = {
            'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
            'X-Content-Type-Options': 'nosniff',
            'X-Frame-Options': 'DENY',
            'X-XSS-Protection': '1; mode=block',
            'Content-Security-Policy': "default-src 'self'",
            'Referrer-Policy': 'strict-origin-when-cross-origin'
        }

        print("  [SECURITY] Configured security headers:")
        for header, value in headers.items():
            print(f"    {header}: {value}")

        return headers

    @staticmethod
    def configure_cors(allowed_origins: List[str]) -> Dict:
        """Configure CORS for production."""
        config = {
            'allowed_origins': allowed_origins,
            'allow_credentials': True,
            'max_age': 3600
        }

        print("\\n  [SECURITY] Configured CORS:")
        print(f"    Allowed origins: {', '.join(allowed_origins)}")
        print(f"    Allow credentials: {config['allow_credentials']}")

        return config

    @staticmethod
    def configure_rate_limiting() -> Dict:
        """Configure rate limiting."""
        config = {
            'per_ip': '100/hour',
            'per_user': '1000/hour',
            'burst': 20
        }

        print("\\n  [SECURITY] Configured rate limiting:")
        for key, value in config.items():
            print(f"    {key}: {value}")

        return config

# Apply security hardening
print("\\nApplying security hardening:")
security = SecurityHardening()

security.configure_headers()
security.configure_cors(['https://app.example.com', 'https://www.example.com'])
security.configure_rate_limiting()
print()

# Example 10: Zero-Downtime Deployment
print("="*60)
print("Example 10: Zero-Downtime Deployment")
print("="*60)

class BlueGreenDeployment:
    """Blue-green deployment strategy."""

    def __init__(self):
        self.blue_version = {'version': 'v1.0', 'active': True, 'instances': 4}
        self.green_version = {'version': 'v1.1', 'active': False, 'instances': 0}
        self.router = 'blue'

    def deploy_green(self):
        """Deploy new version to green environment."""
        print("  [DEPLOY] Deploying to green environment")
        print(f"  Version: {self.green_version['version']}")

        # Start green instances
        self.green_version['instances'] = 4
        print(f"  [DEPLOY] Started {self.green_version['instances']} green instances")

        # Health check green
        print("  [DEPLOY] Running health checks on green...")
        print("  [DEPLOY] Green environment healthy")

    def switch_traffic(self):
        """Switch traffic from blue to green."""
        print("\\n  [DEPLOY] Switching traffic to green...")
        self.router = 'green'
        self.green_version['active'] = True
        print(f"  [DEPLOY] Traffic now routing to {self.router} ({self.green_version['version']})")

    def decommission_blue(self):
        """Decommission old blue environment."""
        print("\\n  [DEPLOY] Keeping blue environment for rollback (5 min)")
        print("  [DEPLOY] No errors detected, decommissioning blue...")
        self.blue_version['active'] = False
        self.blue_version['instances'] = 0
        print(f"  [DEPLOY] Blue environment stopped")

    def rollback(self):
        """Rollback to blue environment."""
        print("\\n  [ROLLBACK] Switching traffic back to blue...")
        self.router = 'blue'
        self.blue_version['active'] = True
        self.green_version['active'] = False
        print(f"  [ROLLBACK] Traffic restored to {self.router} ({self.blue_version['version']})")

# Perform blue-green deployment
print("\\nPerforming zero-downtime deployment:")
deployment = BlueGreenDeployment()

print(f"Current version: {deployment.blue_version['version']} (blue)")
print(f"New version: {deployment.green_version['version']} (green)\\n")

deployment.deploy_green()
deployment.switch_traffic()
deployment.decommission_blue()

print(f"\\n  Deployment complete! Running version: {deployment.green_version['version']}")

print("\\n" + "="*60)
print("All Flask Production Deployment examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 751: Flask Production Deployment ({len(lesson_751['fullSolution']):,} chars)")

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

# Lesson 769: Django DRF Custom Permissions
lesson_769['fullSolution'] = '''"""
Django REST Framework Custom Permissions - Comprehensive Guide

Covers permission classes, object-level permissions, custom permissions,
permission combinations, role-based access, ownership permissions, and best practices.

**Zero Package Installation Required**
"""

from typing import Dict, List, Any, Optional
from datetime import datetime

# Example 1: Basic Permission System
print("="*60)
print("Example 1: Basic Permission System")
print("="*60)

class BasePermission:
    """Base permission class."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if request has permission to access view."""
        return True

    def has_object_permission(self, request: Dict, view, obj: Dict) -> bool:
        """Check if request has permission to access specific object."""
        return True

class AllowAny(BasePermission):
    """Allow any request - no restrictions."""

    def has_permission(self, request: Dict, view) -> bool:
        print("  [PERM] AllowAny: Access granted")
        return True

class DenyAll(BasePermission):
    """Deny all requests."""

    def has_permission(self, request: Dict, view) -> bool:
        print("  [PERM] DenyAll: Access denied")
        return False

# Test basic permissions
print("\\nTesting basic permissions:")

allow = AllowAny()
deny = DenyAll()

request = {'user': None}
view = None

print("Testing AllowAny:")
result = allow.has_permission(request, view)
print(f"  Result: {result}")

print("\\nTesting DenyAll:")
result = deny.has_permission(request, view)
print(f"  Result: {result}")
print()

# Example 2: IsAuthenticated Permission
print("="*60)
print("Example 2: IsAuthenticated Permission")
print("="*60)

class IsAuthenticated(BasePermission):
    """Require user to be authenticated."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if user is authenticated."""
        has_user = request.get('user') is not None

        if has_user:
            print(f"  [PERM] User '{request['user']['username']}' is authenticated")
            return True
        else:
            print("  [PERM] No authenticated user found")
            return False

# Test authentication
print("\\nTesting IsAuthenticated:")

auth_perm = IsAuthenticated()

# Without user
request = {'method': 'GET'}
result = auth_perm.has_permission(request, view)
print(f"  Result: {result}")

# With user
print("\\nWith authenticated user:")
request = {'method': 'GET', 'user': {'id': 1, 'username': 'alice'}}
result = auth_perm.has_permission(request, view)
print(f"  Result: {result}")
print()

# Example 3: Role-Based Permissions
print("="*60)
print("Example 3: Role-Based Permissions")
print("="*60)

class IsAdminUser(BasePermission):
    """Require user to have admin role."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if user is admin."""
        user = request.get('user')
        if not user:
            print("  [PERM] No user - denied")
            return False

        is_admin = user.get('role') == 'admin'
        if is_admin:
            print(f"  [PERM] User '{user['username']}' is admin")
        else:
            print(f"  [PERM] User '{user['username']}' is not admin (role: {user.get('role')})")

        return is_admin

class IsStaffUser(BasePermission):
    """Require user to be staff member."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if user is staff."""
        user = request.get('user')
        if not user:
            return False

        is_staff = user.get('is_staff', False)
        if is_staff:
            print(f"  [PERM] User '{user['username']}' is staff")
        else:
            print(f"  [PERM] User '{user['username']}' is not staff")

        return is_staff

# Test role-based permissions
print("\\nTesting role-based permissions:")

admin_perm = IsAdminUser()
staff_perm = IsStaffUser()

# Admin user
request = {'user': {'username': 'admin', 'role': 'admin', 'is_staff': True}}
print("Testing with admin user:")
print(f"  IsAdminUser: {admin_perm.has_permission(request, view)}")
print(f"  IsStaffUser: {staff_perm.has_permission(request, view)}")

# Regular user
print("\\nTesting with regular user:")
request = {'user': {'username': 'bob', 'role': 'user', 'is_staff': False}}
print(f"  IsAdminUser: {admin_perm.has_permission(request, view)}")
print(f"  IsStaffUser: {staff_perm.has_permission(request, view)}")
print()

# Example 4: Object-Level Permissions
print("="*60)
print("Example 4: Object-Level Permissions")
print("="*60)

class IsOwner(BasePermission):
    """Require user to be owner of object."""

    def has_object_permission(self, request: Dict, view, obj: Dict) -> bool:
        """Check if user owns the object."""
        user = request.get('user')
        if not user:
            print("  [PERM] No user - not owner")
            return False

        owner_id = obj.get('owner_id') or obj.get('user_id')
        is_owner = user['id'] == owner_id

        if is_owner:
            print(f"  [PERM] User '{user['username']}' owns object {obj.get('id')}")
        else:
            print(f"  [PERM] User '{user['username']}' does not own object {obj.get('id')}")

        return is_owner

# Test object-level permissions
print("\\nTesting object-level permissions:")

owner_perm = IsOwner()

# User's own post
post = {'id': 1, 'title': 'My Post', 'owner_id': 1}
request = {'user': {'id': 1, 'username': 'alice'}}

print("User accessing their own post:")
result = owner_perm.has_object_permission(request, view, post)
print(f"  Result: {result}")

# User accessing someone else's post
print("\\nUser accessing another user's post:")
request = {'user': {'id': 2, 'username': 'bob'}}
result = owner_perm.has_object_permission(request, view, post)
print(f"  Result: {result}")
print()

# Example 5: Method-Based Permissions
print("="*60)
print("Example 5: Method-Based Permissions")
print("="*60)

class ReadOnly(BasePermission):
    """Allow read-only operations (GET, HEAD, OPTIONS)."""

    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request: Dict, view) -> bool:
        """Check if request method is safe."""
        method = request.get('method', 'GET')
        is_safe = method in self.SAFE_METHODS

        if is_safe:
            print(f"  [PERM] {method} is a safe method - allowed")
        else:
            print(f"  [PERM] {method} is not a safe method - denied")

        return is_safe

class IsAuthenticatedOrReadOnly(BasePermission):
    """Allow authenticated users full access, others read-only."""

    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    def has_permission(self, request: Dict, view) -> bool:
        """Check authentication or safe method."""
        method = request.get('method', 'GET')
        user = request.get('user')

        if method in self.SAFE_METHODS:
            print(f"  [PERM] {method} is safe method - allowed")
            return True

        if user:
            print(f"  [PERM] User authenticated - {method} allowed")
            return True

        print(f"  [PERM] Not authenticated - {method} denied")
        return False

# Test method-based permissions
print("\\nTesting method-based permissions:")

readonly_perm = ReadOnly()
auth_or_readonly = IsAuthenticatedOrReadOnly()

# GET request
print("GET request:")
request = {'method': 'GET'}
print(f"  ReadOnly: {readonly_perm.has_permission(request, view)}")

# POST request without auth
print("\\nPOST request (no auth):")
request = {'method': 'POST'}
print(f"  ReadOnly: {readonly_perm.has_permission(request, view)}")
print(f"  IsAuthenticatedOrReadOnly: {auth_or_readonly.has_permission(request, view)}")

# POST request with auth
print("\\nPOST request (with auth):")
request = {'method': 'POST', 'user': {'id': 1, 'username': 'alice'}}
print(f"  IsAuthenticatedOrReadOnly: {auth_or_readonly.has_permission(request, view)}")
print()

# Example 6: Custom Permission Classes
print("="*60)
print("Example 6: Custom Permission Classes")
print("="*60)

class HasAPIKey(BasePermission):
    """Require valid API key in headers."""

    VALID_API_KEYS = ['key_123456', 'key_789012']

    def has_permission(self, request: Dict, view) -> bool:
        """Check for valid API key."""
        api_key = request.get('headers', {}).get('X-API-Key')

        if not api_key:
            print("  [PERM] No API key provided")
            return False

        is_valid = api_key in self.VALID_API_KEYS
        if is_valid:
            print(f"  [PERM] Valid API key: {api_key[:10]}...")
        else:
            print(f"  [PERM] Invalid API key: {api_key}")

        return is_valid

class IsInOrganization(BasePermission):
    """Require user to be member of organization."""

    def has_object_permission(self, request: Dict, view, obj: Dict) -> bool:
        """Check if user is in organization."""
        user = request.get('user')
        if not user:
            return False

        org_id = obj.get('organization_id')
        user_org_id = user.get('organization_id')

        is_member = user_org_id == org_id
        if is_member:
            print(f"  [PERM] User is in organization {org_id}")
        else:
            print(f"  [PERM] User not in organization {org_id}")

        return is_member

# Test custom permissions
print("\\nTesting custom permissions:")

api_key_perm = HasAPIKey()
org_perm = IsInOrganization()

# Valid API key
print("Testing API key:")
request = {'headers': {'X-API-Key': 'key_123456'}}
result = api_key_perm.has_permission(request, view)

# Organization membership
print("\\nTesting organization membership:")
project = {'id': 1, 'name': 'Project A', 'organization_id': 10}
request = {'user': {'id': 1, 'username': 'alice', 'organization_id': 10}}
result = org_perm.has_object_permission(request, view, project)
print()

# Example 7: Permission Combinations (AND/OR)
print("="*60)
print("Example 7: Permission Combinations (AND/OR)")
print("="*60)

class PermissionCombination:
    """Combine multiple permissions with AND/OR logic."""

    @staticmethod
    def check_and(permissions: List[BasePermission], request: Dict, view) -> bool:
        """All permissions must pass (AND)."""
        print("  [COMBO] Checking AND combination:")
        for perm in permissions:
            if not perm.has_permission(request, view):
                print("  [COMBO] AND failed - at least one permission denied")
                return False
        print("  [COMBO] AND passed - all permissions granted")
        return True

    @staticmethod
    def check_or(permissions: List[BasePermission], request: Dict, view) -> bool:
        """At least one permission must pass (OR)."""
        print("  [COMBO] Checking OR combination:")
        for perm in permissions:
            if perm.has_permission(request, view):
                print("  [COMBO] OR passed - at least one permission granted")
                return True
        print("  [COMBO] OR failed - all permissions denied")
        return False

# Test permission combinations
print("\\nTesting permission combinations:")

# AND: Must be authenticated AND admin
request = {'user': {'id': 1, 'username': 'alice', 'role': 'admin'}}
result = PermissionCombination.check_and([
    IsAuthenticated(),
    IsAdminUser()
], request, view)
print(f"  Result: {result}")

# OR: Must be admin OR staff
print("\\nTesting OR with regular user:")
request = {'user': {'id': 2, 'username': 'bob', 'role': 'user', 'is_staff': True}}
result = PermissionCombination.check_or([
    IsAdminUser(),
    IsStaffUser()
], request, view)
print(f"  Result: {result}")
print()

# Example 8: Time-Based Permissions
print("="*60)
print("Example 8: Time-Based Permissions")
print("="*60)

class IsBusinessHours(BasePermission):
    """Allow access only during business hours."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if current time is within business hours."""
        now = datetime.now()
        hour = now.hour

        # Business hours: 9 AM - 5 PM
        is_business_hours = 9 <= hour < 17

        if is_business_hours:
            print(f"  [PERM] Current hour {hour}:00 is within business hours")
        else:
            print(f"  [PERM] Current hour {hour}:00 is outside business hours")

        return is_business_hours

class SubscriptionActive(BasePermission):
    """Require active subscription."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if user's subscription is active."""
        user = request.get('user')
        if not user:
            return False

        subscription_end = user.get('subscription_end')
        if not subscription_end:
            print("  [PERM] No subscription found")
            return False

        # Parse subscription end date
        end_date = datetime.fromisoformat(subscription_end)
        is_active = datetime.now() < end_date

        if is_active:
            print(f"  [PERM] Subscription active until {subscription_end}")
        else:
            print(f"  [PERM] Subscription expired on {subscription_end}")

        return is_active

# Test time-based permissions
print("\\nTesting time-based permissions:")

business_hours_perm = IsBusinessHours()
subscription_perm = SubscriptionActive()

# Check business hours
request = {}
result = business_hours_perm.has_permission(request, view)

# Check subscription
print("\\nChecking subscription:")
future_date = (datetime.now().replace(year=datetime.now().year + 1)).isoformat()
request = {'user': {'id': 1, 'username': 'alice', 'subscription_end': future_date}}
result = subscription_perm.has_permission(request, view)
print()

# Example 9: IP-Based Permissions
print("="*60)
print("Example 9: IP-Based Permissions")
print("="*60)

class IPWhitelist(BasePermission):
    """Allow access only from whitelisted IPs."""

    ALLOWED_IPS = ['192.168.1.100', '10.0.0.50', '172.16.0.10']

    def has_permission(self, request: Dict, view) -> bool:
        """Check if request IP is whitelisted."""
        client_ip = request.get('ip', '0.0.0.0')
        is_allowed = client_ip in self.ALLOWED_IPS

        if is_allowed:
            print(f"  [PERM] IP {client_ip} is whitelisted")
        else:
            print(f"  [PERM] IP {client_ip} is not whitelisted")

        return is_allowed

class RateLimitPermission(BasePermission):
    """Rate limit based on IP address."""

    def __init__(self):
        self.request_counts = {}

    def has_permission(self, request: Dict, view) -> bool:
        """Check rate limit for IP."""
        client_ip = request.get('ip', '0.0.0.0')

        # Initialize or increment counter
        if client_ip not in self.request_counts:
            self.request_counts[client_ip] = 0

        self.request_counts[client_ip] += 1
        count = self.request_counts[client_ip]

        # Allow up to 10 requests
        is_allowed = count <= 10

        if is_allowed:
            print(f"  [PERM] IP {client_ip}: {count}/10 requests - allowed")
        else:
            print(f"  [PERM] IP {client_ip}: {count}/10 requests - rate limit exceeded")

        return is_allowed

# Test IP-based permissions
print("\\nTesting IP-based permissions:")

ip_whitelist = IPWhitelist()

# Allowed IP
request = {'ip': '192.168.1.100'}
result = ip_whitelist.has_permission(request, view)

# Blocked IP
print()
request = {'ip': '123.45.67.89'}
result = ip_whitelist.has_permission(request, view)

# Rate limiting
print("\\nTesting rate limiting:")
rate_limit = RateLimitPermission()

for i in range(12):
    request = {'ip': '192.168.1.1'}
    result = rate_limit.has_permission(request, view)
    if not result:
        break
print()

# Example 10: Permission Composition Pattern
print("="*60)
print("Example 10: Permission Composition Pattern")
print("="*60)

class PermissionManager:
    """Manage and apply multiple permissions."""

    def __init__(self, permissions: List[BasePermission]):
        self.permissions = permissions

    def check_permissions(self, request: Dict, view) -> Dict:
        """Check all permissions and return detailed results."""
        results = {
            'allowed': True,
            'checks': []
        }

        print("  [MANAGER] Running permission checks:")

        for perm in self.permissions:
            perm_name = perm.__class__.__name__
            passed = perm.has_permission(request, view)

            results['checks'].append({
                'permission': perm_name,
                'passed': passed
            })

            if not passed:
                results['allowed'] = False

        return results

    def check_object_permissions(self, request: Dict, view, obj: Dict) -> Dict:
        """Check object-level permissions."""
        results = {
            'allowed': True,
            'checks': []
        }

        print("  [MANAGER] Running object permission checks:")

        for perm in self.permissions:
            perm_name = perm.__class__.__name__
            passed = perm.has_object_permission(request, view, obj)

            results['checks'].append({
                'permission': perm_name,
                'passed': passed
            })

            if not passed:
                results['allowed'] = False

        return results

# Test permission manager
print("\\nTesting permission manager:")

# Create permission manager with multiple permissions
manager = PermissionManager([
    IsAuthenticated(),
    IsAdminUser()
])

# Test with admin user
request = {'user': {'id': 1, 'username': 'admin', 'role': 'admin'}}
results = manager.check_permissions(request, view)

print("\\n  Results:")
for check in results['checks']:
    status = '✓' if check['passed'] else '✗'
    print(f"  {status} {check['permission']}: {check['passed']}")
print(f"  Overall: {'ALLOWED' if results['allowed'] else 'DENIED'}")

# Test object-level permissions
print("\\nTesting object permissions:")
manager2 = PermissionManager([
    IsAuthenticated(),
    IsOwner()
])

post = {'id': 1, 'title': 'My Post', 'owner_id': 1}
request = {'user': {'id': 1, 'username': 'alice'}}

results = manager2.check_object_permissions(request, view, post)

print("\\n  Results:")
for check in results['checks']:
    status = '✓' if check['passed'] else '✗'
    print(f"  {status} {check['permission']}: {check['passed']}")
print(f"  Overall: {'ALLOWED' if results['allowed'] else 'DENIED'}")

print("\\n" + "="*60)
print("All Django REST Framework Custom Permissions examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 769: Django DRF Custom Permissions ({len(lesson_769['fullSolution']):,} chars)")

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

print("\\n" + "="*70)
print("BATCH 24 COMPLETE: Django/Flask Advanced Topics")
print("="*70)
print(f"\\nUpgraded: Lesson 774 - Django Testing Strategies ({len(lesson_774['fullSolution']):,} chars)")
print(f"Upgraded: Lesson 751 - Flask Production Deployment ({len(lesson_751['fullSolution']):,} chars)")
print(f"Upgraded: Lesson 769 - DRF Custom Permissions ({len(lesson_769['fullSolution']):,} chars)")
print("="*70)
