"""
Upgrade Flask batch 19: CORS, Caching, and Authentication
Upgrade 3 Flask extension lessons to 13,000-17,000+ characters
Zero package installation required!
"""

import json
import os

def upgrade_lessons():
    lessons_file = os.path.join('public', 'lessons-python.json')

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 747: Flask - Flask-CORS
    lesson_747 = next(l for l in lessons if l['id'] == 747)
    lesson_747['fullSolution'] = '''# Flask-CORS - Complete Simulation
# In production: pip install flask flask-cors
# This lesson simulates CORS (Cross-Origin Resource Sharing) in Flask

import time
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
import json

# Example 1: Understanding CORS
print("Example 1: Understanding CORS Basics")
print("=" * 60)

@dataclass
class HTTPRequest:
    """Simulates HTTP request."""
    method: str
    origin: str
    path: str
    headers: Dict[str, str] = field(default_factory=dict)

@dataclass
class HTTPResponse:
    """Simulates HTTP response."""
    status_code: int
    headers: Dict[str, str] = field(default_factory=dict)
    body: Any = None

class CORSPolicy:
    """Simulates CORS policy."""

    def __init__(self, allowed_origins: List[str] = None, allowed_methods: List[str] = None):
        self.allowed_origins = allowed_origins or ['*']
        self.allowed_methods = allowed_methods or ['GET', 'POST', 'PUT', 'DELETE']
        self.allowed_headers = ['Content-Type', 'Authorization']
        self.max_age = 86400  # 24 hours

    def is_origin_allowed(self, origin: str) -> bool:
        """Check if origin is allowed."""
        if '*' in self.allowed_origins:
            return True
        return origin in self.allowed_origins

    def add_cors_headers(self, response: HTTPResponse, request: HTTPRequest):
        """Add CORS headers to response."""
        origin = request.origin

        if self.is_origin_allowed(origin):
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Methods'] = ', '.join(self.allowed_methods)
            response.headers['Access-Control-Allow-Headers'] = ', '.join(self.allowed_headers)
            response.headers['Access-Control-Max-Age'] = str(self.max_age)

# Create CORS policy
cors_policy = CORSPolicy(allowed_origins=['https://example.com', 'https://app.example.com'])

# Simulate request
request = HTTPRequest(
    method='GET',
    origin='https://example.com',
    path='/api/users'
)

response = HTTPResponse(status_code=200, body={'users': []})
cors_policy.add_cors_headers(response, request)

print("Request:")
print(f"  Origin: {request.origin}")
print(f"  Method: {request.method}")
print(f"  Path: {request.path}")
print()
print("Response CORS Headers:")
for header, value in response.headers.items():
    print(f"  {header}: {value}")
print()

# Example 2: Preflight Requests
print("Example 2: Preflight Requests (OPTIONS)")
print("=" * 60)

class PreflightHandler:
    """Handles CORS preflight requests."""

    def __init__(self, cors_policy: CORSPolicy):
        self.cors_policy = cors_policy

    def handle_preflight(self, request: HTTPRequest) -> HTTPResponse:
        """Handle OPTIONS preflight request."""
        response = HTTPResponse(status_code=204)  # No Content

        # Add CORS headers
        self.cors_policy.add_cors_headers(response, request)

        # Add additional preflight headers
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers['Vary'] = 'Origin'

        return response

    def is_preflight(self, request: HTTPRequest) -> bool:
        """Check if request is a preflight request."""
        return (request.method == 'OPTIONS' and
                'Access-Control-Request-Method' in request.headers)

# Create preflight handler
preflight_handler = PreflightHandler(cors_policy)

# Simulate preflight request
preflight_request = HTTPRequest(
    method='OPTIONS',
    origin='https://example.com',
    path='/api/users',
    headers={
        'Access-Control-Request-Method': 'POST',
        'Access-Control-Request-Headers': 'Content-Type, Authorization'
    }
)

if preflight_handler.is_preflight(preflight_request):
    print("Detected preflight request")
    preflight_response = preflight_handler.handle_preflight(preflight_request)

    print()
    print("Preflight Response:")
    print(f"  Status: {preflight_response.status_code}")
    print("  Headers:")
    for header, value in preflight_response.headers.items():
        print(f"    {header}: {value}")
print()

# Example 3: Flask-CORS Decorator Pattern
print("Example 3: Flask-CORS Decorator Pattern")
print("=" * 60)

class FlaskApp:
    """Simulates Flask application."""

    def __init__(self):
        self.routes = {}
        self.cors_policy = None

    def route(self, path: str, methods: List[str] = None):
        """Route decorator."""
        def decorator(func: Callable):
            self.routes[path] = {
                'func': func,
                'methods': methods or ['GET']
            }
            return func
        return decorator

    def apply_cors(self, cors_policy: CORSPolicy):
        """Apply CORS policy to all routes."""
        self.cors_policy = cors_policy

    def handle_request(self, request: HTTPRequest) -> HTTPResponse:
        """Handle incoming request."""
        if request.path in self.routes:
            route_info = self.routes[request.path]

            # Check method
            if request.method not in route_info['methods']:
                return HTTPResponse(status_code=405, body="Method Not Allowed")

            # Call route function
            response_data = route_info['func']()
            response = HTTPResponse(status_code=200, body=response_data)

            # Apply CORS headers
            if self.cors_policy:
                self.cors_policy.add_cors_headers(response, request)

            return response

        return HTTPResponse(status_code=404, body="Not Found")

# Create Flask app with CORS
app = FlaskApp()
app.apply_cors(CORSPolicy(allowed_origins=['*']))

@app.route('/api/hello', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    return {'users': [{'id': 1, 'name': 'Alice'}]}

# Simulate requests
test_request = HTTPRequest(
    method='GET',
    origin='https://frontend.example.com',
    path='/api/hello'
)

test_response = app.handle_request(test_request)

print(f"Request: {test_request.method} {test_request.path}")
print(f"Response: {test_response.status_code}")
print("CORS Headers:")
for header, value in test_response.headers.items():
    if 'Access-Control' in header:
        print(f"  {header}: {value}")
print()

# Example 4: Origin Validation
print("Example 4: Origin Validation Strategies")
print("=" * 60)

class OriginValidator:
    """Validates request origins."""

    @staticmethod
    def exact_match(origin: str, allowed_origins: List[str]) -> bool:
        """Exact origin matching."""
        return origin in allowed_origins

    @staticmethod
    def wildcard_subdomain(origin: str, domain: str) -> bool:
        """Allow all subdomains of a domain."""
        # e.g., *.example.com allows app.example.com, api.example.com
        return origin.endswith(f'.{domain}') or origin == f'https://{domain}'

    @staticmethod
    def regex_pattern(origin: str, pattern: str) -> bool:
        """Regex pattern matching."""
        import re
        return bool(re.match(pattern, origin))

# Test origin validation
test_origins = [
    'https://example.com',
    'https://app.example.com',
    'https://api.example.com',
    'https://evil.com',
]

allowed_origins = ['https://example.com']
domain = 'example.com'

print("Origin Validation Results:")
for origin in test_origins:
    exact = OriginValidator.exact_match(origin, allowed_origins)
    subdomain = OriginValidator.wildcard_subdomain(origin, domain)
    print(f"  {origin}")
    print(f"    Exact match: {exact}")
    print(f"    Subdomain match: {subdomain}")
print()

# Example 5: Credentials and Cookies
print("Example 5: CORS with Credentials")
print("=" * 60)

class CORSWithCredentials:
    """CORS configuration for credentials."""

    def __init__(self, allowed_origins: List[str]):
        # With credentials, cannot use wildcard origin
        if '*' in allowed_origins:
            raise ValueError("Cannot use wildcard origin with credentials")
        self.allowed_origins = allowed_origins
        self.supports_credentials = True

    def add_cors_headers(self, response: HTTPResponse, request: HTTPRequest):
        """Add CORS headers with credentials support."""
        origin = request.origin

        if origin in self.allowed_origins:
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
            # Vary header ensures proper caching
            response.headers['Vary'] = 'Origin'

# Create CORS with credentials
cors_with_creds = CORSWithCredentials(allowed_origins=['https://app.example.com'])

# Simulate authenticated request
auth_request = HTTPRequest(
    method='POST',
    origin='https://app.example.com',
    path='/api/profile',
    headers={'Cookie': 'session=abc123'}
)

auth_response = HTTPResponse(status_code=200, body={'user': 'alice'})
cors_with_creds.add_cors_headers(auth_response, auth_request)

print("Request with credentials:")
print(f"  Origin: {auth_request.origin}")
print(f"  Cookie: {auth_request.headers.get('Cookie')}")
print()
print("Response headers:")
for header, value in auth_response.headers.items():
    print(f"  {header}: {value}")
print()

# Example 6: Route-Specific CORS
print("Example 6: Route-Specific CORS Configuration")
print("=" * 60)

class RouteSpecificCORS:
    """Apply different CORS policies to different routes."""

    def __init__(self):
        self.route_policies: Dict[str, CORSPolicy] = {}
        self.default_policy = CORSPolicy(allowed_origins=['*'])

    def configure_route(self, path: str, allowed_origins: List[str] = None):
        """Configure CORS for specific route."""
        policy = CORSPolicy(allowed_origins=allowed_origins or ['*'])
        self.route_policies[path] = policy

    def get_policy(self, path: str) -> CORSPolicy:
        """Get CORS policy for route."""
        return self.route_policies.get(path, self.default_policy)

    def apply_cors(self, response: HTTPResponse, request: HTTPRequest):
        """Apply route-specific CORS policy."""
        policy = self.get_policy(request.path)
        policy.add_cors_headers(response, request)

# Configure route-specific CORS
route_cors = RouteSpecificCORS()

# Public API - allow all origins
route_cors.configure_route('/api/public', allowed_origins=['*'])

# Admin API - restrict to specific origins
route_cors.configure_route('/api/admin', allowed_origins=['https://admin.example.com'])

# Test different routes
public_request = HTTPRequest(method='GET', origin='https://anyone.com', path='/api/public')
admin_request = HTTPRequest(method='GET', origin='https://admin.example.com', path='/api/admin')

public_response = HTTPResponse(status_code=200)
admin_response = HTTPResponse(status_code=200)

route_cors.apply_cors(public_response, public_request)
route_cors.apply_cors(admin_response, admin_request)

print("Public API (/api/public):")
print(f"  Origin: {public_request.origin}")
print(f"  Allowed: {public_response.headers.get('Access-Control-Allow-Origin')}")
print()
print("Admin API (/api/admin):")
print(f"  Origin: {admin_request.origin}")
print(f"  Allowed: {admin_response.headers.get('Access-Control-Allow-Origin')}")
print()

# Example 7: Error Handling
print("Example 7: CORS Error Handling")
print("=" * 60)

class CORSErrorHandler:
    """Handle CORS errors."""

    def __init__(self, cors_policy: CORSPolicy):
        self.cors_policy = cors_policy

    def validate_request(self, request: HTTPRequest) -> tuple[bool, Optional[str]]:
        """Validate CORS request."""
        # Check if origin is provided
        if not request.origin:
            return False, "Origin header missing"

        # Check if origin is allowed
        if not self.cors_policy.is_origin_allowed(request.origin):
            return False, f"Origin {request.origin} not allowed"

        # Check if method is allowed
        if request.method not in self.cors_policy.allowed_methods:
            return False, f"Method {request.method} not allowed"

        return True, None

    def create_error_response(self, error_message: str) -> HTTPResponse:
        """Create error response."""
        return HTTPResponse(
            status_code=403,
            body={'error': 'CORS policy violation', 'message': error_message}
        )

# Create error handler
error_handler = CORSErrorHandler(CORSPolicy(allowed_origins=['https://example.com']))

# Test various error scenarios
error_scenarios = [
    HTTPRequest(method='GET', origin='', path='/api/data'),
    HTTPRequest(method='GET', origin='https://evil.com', path='/api/data'),
    HTTPRequest(method='PATCH', origin='https://example.com', path='/api/data'),
]

print("Testing error scenarios:")
for scenario in error_scenarios:
    valid, error = error_handler.validate_request(scenario)
    if not valid:
        print(f"  Request from {scenario.origin or 'NO ORIGIN'} with {scenario.method}")
        print(f"    Error: {error}")

print()

# Example 8: Performance Optimization
print("Example 8: CORS Performance Optimization")
print("=" * 60)

class OptimizedCORS:
    """Optimized CORS handling with caching."""

    def __init__(self, allowed_origins: List[str]):
        self.allowed_origins = set(allowed_origins)  # Use set for O(1) lookup
        self.origin_cache: Dict[str, bool] = {}
        self.cache_hits = 0
        self.cache_misses = 0

    def is_origin_allowed(self, origin: str) -> bool:
        """Check if origin is allowed with caching."""
        if origin in self.origin_cache:
            self.cache_hits += 1
            return self.origin_cache[origin]

        self.cache_misses += 1
        allowed = origin in self.allowed_origins or '*' in self.allowed_origins
        self.origin_cache[origin] = allowed
        return allowed

    def get_cache_stats(self) -> Dict[str, int]:
        """Get cache statistics."""
        total = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total * 100) if total > 0 else 0
        return {
            'hits': self.cache_hits,
            'misses': self.cache_misses,
            'hit_rate': hit_rate
        }

# Test performance
optimized_cors = OptimizedCORS(allowed_origins=['https://example.com', 'https://app.example.com'])

# Simulate many requests
test_origins_repeated = ['https://example.com'] * 5 + ['https://app.example.com'] * 5

for origin in test_origins_repeated:
    optimized_cors.is_origin_allowed(origin)

stats = optimized_cors.get_cache_stats()
print("Cache Statistics:")
print(f"  Cache hits: {stats['hits']}")
print(f"  Cache misses: {stats['misses']}")
print(f"  Hit rate: {stats['hit_rate']:.1f}%")
print()

# Example 9: Complete Flask-CORS Integration
print("Example 9: Complete Flask-CORS Integration")
print("=" * 60)

class FlaskCORSApp:
    """Complete Flask application with CORS."""

    def __init__(self):
        self.routes = {}
        self.before_request_funcs = []
        self.after_request_funcs = []

    def before_request(self, func: Callable):
        """Register before request handler."""
        self.before_request_funcs.append(func)
        return func

    def after_request(self, func: Callable):
        """Register after request handler."""
        self.after_request_funcs.append(func)
        return func

    def route(self, path: str):
        """Route decorator."""
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator

    def handle_request(self, request: HTTPRequest) -> HTTPResponse:
        """Handle request with middleware."""
        # Before request
        for func in self.before_request_funcs:
            result = func(request)
            if isinstance(result, HTTPResponse):
                return result

        # Handle route
        if request.path in self.routes:
            data = self.routes[request.path]()
            response = HTTPResponse(status_code=200, body=data)
        else:
            response = HTTPResponse(status_code=404, body={'error': 'Not found'})

        # After request
        for func in self.after_request_funcs:
            response = func(response, request)

        return response

# Create app
cors_app = FlaskCORSApp()

# Configure CORS middleware
cors_config = CORSPolicy(allowed_origins=['https://example.com'])

@cors_app.after_request
def add_cors_headers(response: HTTPResponse, request: HTTPRequest) -> HTTPResponse:
    """Add CORS headers to all responses."""
    cors_config.add_cors_headers(response, request)
    return response

@cors_app.route('/api/data')
def get_data():
    return {'data': [1, 2, 3]}

# Test the app
test_req = HTTPRequest(method='GET', origin='https://example.com', path='/api/data')
test_resp = cors_app.handle_request(test_req)

print(f"Request: {test_req.method} {test_req.path}")
print(f"Response Status: {test_resp.status_code}")
print(f"Response Body: {test_resp.body}")
print("CORS Headers:")
for header, value in test_resp.headers.items():
    print(f"  {header}: {value}")
print()

print("=" * 60)
print("FLASK-CORS BEST PRACTICES")
print("=" * 60)
print("""
BASIC CONFIGURATION:

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

SPECIFIC ORIGINS:

CORS(app, origins=[
    "https://example.com",
    "https://app.example.com"
])

ROUTE-SPECIFIC CORS:

from flask_cors import cross_origin

@app.route('/api/public')
@cross_origin(origins="*")
def public_api():
    return {'data': 'public'}

@app.route('/api/private')
@cross_origin(origins="https://app.example.com")
def private_api():
    return {'data': 'private'}

WITH CREDENTIALS:

CORS(app, supports_credentials=True)

# Frontend must include:
# credentials: 'include' in fetch()

PREFLIGHT CACHING:

CORS(app, max_age=86400)  # Cache preflight for 24 hours

CUSTOM HEADERS:

CORS(app, allow_headers=[
    'Content-Type',
    'Authorization',
    'X-Custom-Header'
])

METHODS:

CORS(app, methods=[
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'OPTIONS'
])

EXPOSE HEADERS:

CORS(app, expose_headers=[
    'X-Total-Count',
    'X-Page-Number'
])

SECURITY CONSIDERATIONS:

1. Never use '*' with credentials
2. Validate origins strictly
3. Use HTTPS only
4. Limit allowed methods
5. Set appropriate max_age
6. Monitor CORS errors
7. Use Vary header for caching

COMMON ISSUES:

Missing Origin header:
  - Browser doesn't send for same-origin
  - Not a CORS issue

Credentials with wildcard:
  - Error: Cannot use * with credentials
  - Must specify exact origins

Preflight failures:
  - OPTIONS request blocked
  - Missing required headers
  - Wrong status code (must be 2xx)

Production note: Real Flask-CORS provides:
  - Automatic preflight handling
  - Resource-level configuration
  - Regular expression origins
  - Decorator support
  - Error handling
  - Integration with Flask blueprints
  - Logging and debugging
""")
'''

    # Lesson 746: Flask - Flask-Caching
    lesson_746 = next(l for l in lessons if l['id'] == 746)
    lesson_746['fullSolution'] = '''# Flask-Caching - Complete Simulation
# In production: pip install flask flask-caching
# This lesson simulates caching strategies in Flask applications

import time
import hashlib
import json
from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass, field
from datetime import datetime, timedelta

# Example 1: Simple Cache Implementation
print("Example 1: Simple In-Memory Cache")
print("=" * 60)

class SimpleCache:
    """Basic in-memory cache."""

    def __init__(self):
        self.cache: Dict[str, tuple[Any, float]] = {}
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        if key in self.cache:
            value, expiry = self.cache[key]
            if expiry == 0 or time.time() < expiry:
                self.hits += 1
                return value
            else:
                # Expired
                del self.cache[key]

        self.misses += 1
        return None

    def set(self, key: str, value: Any, timeout: int = 300):
        """Set value in cache with optional timeout."""
        expiry = time.time() + timeout if timeout > 0 else 0
        self.cache[key] = (value, expiry)

    def delete(self, key: str):
        """Delete key from cache."""
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        """Clear all cache entries."""
        self.cache.clear()

    def get_stats(self) -> Dict[str, int]:
        """Get cache statistics."""
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return {
            'hits': self.hits,
            'misses': self.misses,
            'hit_rate': hit_rate,
            'size': len(self.cache)
        }

# Test simple cache
cache = SimpleCache()

# Cache miss
result1 = cache.get('user:1')
print(f"First access (miss): {result1}")

# Set value
cache.set('user:1', {'id': 1, 'name': 'Alice'}, timeout=60)

# Cache hit
result2 = cache.get('user:1')
print(f"Second access (hit): {result2}")

# Stats
stats = cache.get_stats()
print(f"Cache stats: {stats}")
print()

# Example 2: Cache Decorator Pattern
print("Example 2: Cache Decorator Pattern")
print("=" * 60)

class CacheDecorator:
    """Decorator for caching function results."""

    def __init__(self, cache: SimpleCache, timeout: int = 300):
        self.cache = cache
        self.timeout = timeout

    def __call__(self, func: Callable):
        """Decorator implementation."""
        def wrapper(*args, **kwargs):
            # Generate cache key
            key = self._generate_key(func.__name__, args, kwargs)

            # Check cache
            result = self.cache.get(key)
            if result is not None:
                print(f"  [CACHE HIT] {func.__name__}")
                return result

            # Call function
            print(f"  [CACHE MISS] {func.__name__}")
            result = func(*args, **kwargs)

            # Store in cache
            self.cache.set(key, result, self.timeout)
            return result

        return wrapper

    def _generate_key(self, func_name: str, args: tuple, kwargs: dict) -> str:
        """Generate cache key from function name and arguments."""
        key_data = f"{func_name}:{args}:{sorted(kwargs.items())}"
        return hashlib.md5(key_data.encode()).hexdigest()

# Create cache decorator
cached = CacheDecorator(cache, timeout=60)

@cached
def get_user_posts(user_id: int) -> List[Dict]:
    """Expensive function to get user posts."""
    time.sleep(0.1)  # Simulate slow query
    return [
        {'id': 1, 'title': 'Post 1', 'user_id': user_id},
        {'id': 2, 'title': 'Post 2', 'user_id': user_id}
    ]

# First call - cache miss
posts1 = get_user_posts(1)
print(f"Posts: {len(posts1)} posts")

# Second call - cache hit
posts2 = get_user_posts(1)
print(f"Posts: {len(posts2)} posts")
print()

# Example 3: Cache Key Strategies
print("Example 3: Cache Key Strategies")
print("=" * 60)

class CacheKeyBuilder:
    """Build cache keys using different strategies."""

    @staticmethod
    def simple(prefix: str, identifier: Any) -> str:
        """Simple key: prefix:id."""
        return f"{prefix}:{identifier}"

    @staticmethod
    def versioned(prefix: str, identifier: Any, version: int) -> str:
        """Versioned key: prefix:id:v1."""
        return f"{prefix}:{identifier}:v{version}"

    @staticmethod
    def namespaced(namespace: str, prefix: str, identifier: Any) -> str:
        """Namespaced key: app:users:1."""
        return f"{namespace}:{prefix}:{identifier}"

    @staticmethod
    def hashed(data: Dict[str, Any]) -> str:
        """Hash-based key for complex data."""
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()[:16]

# Test key strategies
print("Key strategies:")
print(f"  Simple: {CacheKeyBuilder.simple('user', 1)}")
print(f"  Versioned: {CacheKeyBuilder.versioned('user', 1, 2)}")
print(f"  Namespaced: {CacheKeyBuilder.namespaced('myapp', 'user', 1)}")
print(f"  Hashed: {CacheKeyBuilder.hashed({'user_id': 1, 'type': 'profile'})}")
print()

# Example 4: Cache Invalidation
print("Example 4: Cache Invalidation Strategies")
print("=" * 60)

class CacheInvalidator:
    """Handle cache invalidation."""

    def __init__(self, cache: SimpleCache):
        self.cache = cache
        self.tags: Dict[str, List[str]] = {}

    def set_with_tags(self, key: str, value: Any, tags: List[str], timeout: int = 300):
        """Set cache value with tags for invalidation."""
        self.cache.set(key, value, timeout)

        # Track tags
        for tag in tags:
            if tag not in self.tags:
                self.tags[tag] = []
            self.tags[tag].append(key)

    def invalidate_tag(self, tag: str):
        """Invalidate all keys associated with a tag."""
        if tag in self.tags:
            for key in self.tags[tag]:
                self.cache.delete(key)
            del self.tags[tag]
            print(f"  Invalidated tag '{tag}'")

    def invalidate_pattern(self, pattern: str):
        """Invalidate keys matching a pattern."""
        keys_to_delete = [k for k in self.cache.cache.keys() if pattern in k]
        for key in keys_to_delete:
            self.cache.delete(key)
        print(f"  Invalidated {len(keys_to_delete)} keys matching '{pattern}'")

# Test invalidation
invalidator = CacheInvalidator(cache)

# Set values with tags
invalidator.set_with_tags('user:1:profile', {'name': 'Alice'}, ['user:1', 'profiles'])
invalidator.set_with_tags('user:1:posts', [1, 2, 3], ['user:1', 'posts'])
invalidator.set_with_tags('user:2:profile', {'name': 'Bob'}, ['user:2', 'profiles'])

print(f"Cache size before invalidation: {cache.get_stats()['size']}")

# Invalidate by tag
invalidator.invalidate_tag('user:1')

print(f"Cache size after tag invalidation: {cache.get_stats()['size']}")
print()

# Example 5: Memoization
print("Example 5: Memoization Pattern")
print("=" * 60)

class Memoize:
    """Memoization decorator with cache."""

    def __init__(self):
        self.cache = {}
        self.call_count = 0

    def __call__(self, func: Callable):
        def wrapper(*args):
            self.call_count += 1

            if args in self.cache:
                print(f"  [MEMO HIT] {func.__name__}{args}")
                return self.cache[args]

            print(f"  [MEMO MISS] {func.__name__}{args}")
            result = func(*args)
            self.cache[args] = result
            return result

        wrapper.cache = self.cache
        wrapper.call_count = lambda: self.call_count
        return wrapper

@Memoize()
def fibonacci(n: int) -> int:
    """Calculate fibonacci number (expensive without memoization)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Calculate fibonacci
result = fibonacci(10)
print(f"fibonacci(10) = {result}")
print(f"Function calls: {fibonacci.call_count()}")
print()

# Example 6: Time-based Cache Expiration
print("Example 6: Time-based Cache Expiration")
print("=" * 60)

class TTLCache:
    """Cache with time-to-live (TTL) support."""

    def __init__(self, default_ttl: int = 300):
        self.cache: Dict[str, tuple[Any, datetime]] = {}
        self.default_ttl = default_ttl

    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Set value with TTL."""
        ttl = ttl or self.default_ttl
        expiry = datetime.now() + timedelta(seconds=ttl)
        self.cache[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        """Get value if not expired."""
        if key in self.cache:
            value, expiry = self.cache[key]
            if datetime.now() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def cleanup(self):
        """Remove expired entries."""
        now = datetime.now()
        expired = [k for k, (_, exp) in self.cache.items() if now >= exp]
        for key in expired:
            del self.cache[key]
        return len(expired)

# Test TTL cache
ttl_cache = TTLCache(default_ttl=2)

ttl_cache.set('short', 'expires soon', ttl=1)
ttl_cache.set('long', 'expires later', ttl=10)

print(f"Immediate access - short: {ttl_cache.get('short')}")
print(f"Immediate access - long: {ttl_cache.get('long')}")

time.sleep(1.5)
print(f"After 1.5s - short: {ttl_cache.get('short')}")
print(f"After 1.5s - long: {ttl_cache.get('long')}")
print()

# Example 7: LRU Cache
print("Example 7: LRU (Least Recently Used) Cache")
print("=" * 60)

from collections import OrderedDict

class LRUCache:
    """LRU cache with size limit."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> Optional[Any]:
        """Get value and mark as recently used."""
        if key in self.cache:
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def set(self, key: str, value: Any):
        """Set value, evict LRU if over capacity."""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            evicted_key = next(iter(self.cache))
            del self.cache[evicted_key]
            print(f"  Evicted LRU: {evicted_key}")

# Test LRU cache
lru = LRUCache(capacity=3)

lru.set('a', 1)
lru.set('b', 2)
lru.set('c', 3)
print(f"Cache: {list(lru.cache.keys())}")

lru.set('d', 4)  # Should evict 'a'
print(f"After adding 'd': {list(lru.cache.keys())}")

lru.get('b')  # Access 'b', making it most recent
lru.set('e', 5)  # Should evict 'c' (not 'b')
print(f"After adding 'e': {list(lru.cache.keys())}")
print()

# Example 8: Cache Warming
print("Example 8: Cache Warming")
print("=" * 60)

class CacheWarmer:
    """Preload cache with frequently accessed data."""

    def __init__(self, cache: SimpleCache):
        self.cache = cache

    def warm_users(self, user_ids: List[int]):
        """Preload user data into cache."""
        print(f"Warming cache for {len(user_ids)} users...")
        for user_id in user_ids:
            # Simulate fetching user data
            user_data = {'id': user_id, 'name': f'User{user_id}'}
            self.cache.set(f'user:{user_id}', user_data, timeout=3600)
        print(f"  Warmed {len(user_ids)} users")

    def warm_popular_posts(self):
        """Preload popular posts."""
        print("Warming cache for popular posts...")
        popular_posts = [
            {'id': 1, 'title': 'Popular Post 1', 'views': 1000},
            {'id': 2, 'title': 'Popular Post 2', 'views': 800},
        ]
        for post in popular_posts:
            self.cache.set(f'post:{post["id"]}', post, timeout=1800)
        print(f"  Warmed {len(popular_posts)} posts")

# Test cache warming
warmer = CacheWarmer(cache)
cache.clear()

print(f"Cache size before warming: {cache.get_stats()['size']}")
warmer.warm_users([1, 2, 3, 4, 5])
warmer.warm_popular_posts()
print(f"Cache size after warming: {cache.get_stats()['size']}")
print()

# Example 9: Fragment Caching
print("Example 9: Fragment Caching (Template Fragments)")
print("=" * 60)

class FragmentCache:
    """Cache template fragments."""

    def __init__(self, cache: SimpleCache):
        self.cache = cache

    def render_user_widget(self, user_id: int, use_cache: bool = True) -> str:
        """Render user widget with optional caching."""
        cache_key = f'fragment:user_widget:{user_id}'

        if use_cache:
            cached = self.cache.get(cache_key)
            if cached:
                print(f"  [FRAGMENT CACHE HIT] user_widget:{user_id}")
                return cached

        print(f"  [FRAGMENT CACHE MISS] user_widget:{user_id}")

        # Expensive render
        html = f"""
        <div class="user-widget">
            <h3>User {user_id}</h3>
            <p>Profile information...</p>
            <p>Generated at: {datetime.now()}</p>
        </div>
        """

        if use_cache:
            self.cache.set(cache_key, html, timeout=600)

        return html

# Test fragment caching
fragment_cache = FragmentCache(cache)

# First render - cache miss
widget1 = fragment_cache.render_user_widget(1)
print("First render (partial):", widget1[:50])

# Second render - cache hit
widget2 = fragment_cache.render_user_widget(1)
print("Second render (partial):", widget2[:50])
print()

# Example 10: Cache-Aside Pattern
print("Example 10: Cache-Aside Pattern (Lazy Loading)")
print("=" * 60)

class Database:
    """Simulated database."""

    def __init__(self):
        self.query_count = 0

    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Simulate database query."""
        self.query_count += 1
        time.sleep(0.05)  # Simulate latency
        return {'id': user_id, 'name': f'User{user_id}', 'email': f'user{user_id}@example.com'}

class CacheAsideService:
    """Service using cache-aside pattern."""

    def __init__(self, cache: SimpleCache, database: Database):
        self.cache = cache
        self.database = database

    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Get user with cache-aside pattern."""
        cache_key = f'user:{user_id}'

        # Try cache first
        user = self.cache.get(cache_key)
        if user:
            print(f"  [CACHE] User {user_id}")
            return user

        # Cache miss - query database
        print(f"  [DATABASE] User {user_id}")
        user = self.database.get_user(user_id)

        # Store in cache
        self.cache.set(cache_key, user, timeout=300)

        return user

# Test cache-aside
db = Database()
service = CacheAsideService(cache, db)

# Multiple requests for same user
for i in range(3):
    user = service.get_user(1)
    print(f"    Retrieved: {user['name']}")

print(f"Database queries: {db.query_count}")
print()

print("=" * 60)
print("FLASK-CACHING BEST PRACTICES")
print("=" * 60)
print("""
CONFIGURATION:

from flask_caching import Cache

cache = Cache(app, config={
    'CACHE_TYPE': 'SimpleCache',  # or 'RedisCache', 'MemcachedCache'
    'CACHE_DEFAULT_TIMEOUT': 300
})

DECORATORS:

@cache.cached(timeout=60)
def expensive_function():
    return compute_result()

@cache.cached(timeout=120, key_prefix='view_%s')
def view_function(page):
    return render_template('page.html')

@cache.memoize(timeout=300)
def get_user(user_id):
    return User.query.get(user_id)

CACHE TYPES:

SimpleCache:
  - In-memory, single process
  - Development only

RedisCache:
  - Distributed, persistent
  - Production recommended

MemcachedCache:
  - Distributed, fast
  - No persistence

FileSystemCache:
  - Disk-based
  - Slower but persistent

KEY STRATEGIES:

Function-based:
  @cache.memoize()  # Auto-generates key from args

Custom key:
  @cache.cached(key_prefix=lambda: f"user_{current_user.id}")

Dynamic key:
  cache.set(f"user:{user_id}:v{version}", data)

INVALIDATION:

Delete single key:
  cache.delete('user:1')

Delete pattern:
  cache.delete_many('user:*')

Clear all:
  cache.clear()

Tagged invalidation:
  Use custom tag tracking

COMMON PATTERNS:

Cache-aside (lazy loading):
  - Check cache first
  - Load from DB if miss
  - Store in cache

Cache warming:
  - Preload frequently accessed data
  - Background job at startup

Fragment caching:
  - Cache rendered HTML
  - Per-user or per-page

Time-based expiration:
  - Set appropriate TTL
  - Balance freshness vs performance

MONITORING:

Track metrics:
  - Hit rate
  - Miss rate
  - Eviction rate
  - Memory usage

Set alerts:
  - Low hit rate
  - High memory
  - Slow response times

PERFORMANCE TIPS:

1. Cache expensive operations only
2. Use appropriate TTL values
3. Implement cache warming for predictable data
4. Monitor and adjust cache size
5. Use tags for organized invalidation
6. Consider distributed caching for scaling
7. Implement graceful degradation on cache failure

Production note: Real Flask-Caching provides:
  - Multiple backend support
  - Automatic key generation
  - Decorator-based caching
  - Template fragment caching
  - Jinja2 integration
  - Configuration management
  - Cache versioning
  - Distributed caching support
""")
'''

    # Lesson 750: Flask-Login Authentication
    lesson_750 = next(l for l in lessons if l['id'] == 750)
    lesson_750['fullSolution'] = '''# Flask-Login Authentication - Complete Simulation
# In production: pip install flask flask-login
# This lesson simulates user authentication with Flask-Login

from typing import Dict, Optional, Callable, List
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import hashlib
import secrets

# Example 1: User Model
print("Example 1: User Model with Flask-Login")
print("=" * 60)

class UserMixin:
    """Provides default implementations for Flask-Login methods."""

    @property
    def is_authenticated(self) -> bool:
        """Return True if user is authenticated."""
        return True

    @property
    def is_active(self) -> bool:
        """Return True if user account is active."""
        return True

    @property
    def is_anonymous(self) -> bool:
        """Return False for regular users."""
        return False

    def get_id(self) -> str:
        """Return user ID as string."""
        return str(self.id)

@dataclass
class User(UserMixin):
    """User model for authentication."""
    id: int
    username: str
    email: str
    password_hash: str
    active: bool = True
    created_at: datetime = field(default_factory=datetime.now)

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        """Verify password against hash."""
        return self.password_hash == self.hash_password(password)

# Create test user
user = User(
    id=1,
    username='alice',
    email='alice@example.com',
    password_hash=User.hash_password('password123')
)

print(f"User created: {user.username}")
print(f"Is authenticated: {user.is_authenticated}")
print(f"Is active: {user.is_active}")
print(f"User ID: {user.get_id()}")
print(f"Password check: {user.check_password('password123')}")
print()

# Example 2: User Database
print("Example 2: User Database")
print("=" * 60)

class UserDatabase:
    """Simple user database."""

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.username_index: Dict[str, int] = {}
        self.next_id = 1

    def create_user(self, username: str, email: str, password: str) -> User:
        """Create a new user."""
        user = User(
            id=self.next_id,
            username=username,
            email=email,
            password_hash=User.hash_password(password)
        )
        self.users[user.id] = user
        self.username_index[username] = user.id
        self.next_id += 1
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        return self.users.get(user_id)

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        user_id = self.username_index.get(username)
        return self.users.get(user_id) if user_id else None

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Authenticate user with username and password."""
        user = self.get_by_username(username)
        if user and user.check_password(password):
            return user
        return None

# Create database and users
user_db = UserDatabase()
alice = user_db.create_user('alice', 'alice@example.com', 'pass123')
bob = user_db.create_user('bob', 'bob@example.com', 'pass456')

print(f"Created users: {len(user_db.users)}")
print(f"Authenticate alice: {user_db.authenticate('alice', 'pass123') is not None}")
print(f"Authenticate with wrong password: {user_db.authenticate('alice', 'wrong') is not None}")
print()

# Example 3: Login Manager
print("Example 3: Login Manager")
print("=" * 60)

class LoginManager:
    """Manages user sessions and authentication."""

    def __init__(self, user_loader: Callable[[int], Optional[User]]):
        self.user_loader = user_loader
        self.sessions: Dict[str, int] = {}  # session_token -> user_id
        self.session_expiry: Dict[str, datetime] = {}

    def create_session(self, user: User, remember: bool = False) -> str:
        """Create a session for user."""
        session_token = secrets.token_urlsafe(32)
        self.sessions[session_token] = user.id

        # Set expiry
        if remember:
            expiry = datetime.now() + timedelta(days=30)
        else:
            expiry = datetime.now() + timedelta(hours=2)

        self.session_expiry[session_token] = expiry
        return session_token

    def get_user_from_session(self, session_token: str) -> Optional[User]:
        """Get user from session token."""
        if session_token not in self.sessions:
            return None

        # Check expiry
        if datetime.now() > self.session_expiry[session_token]:
            self.logout_session(session_token)
            return None

        user_id = self.sessions[session_token]
        return self.user_loader(user_id)

    def logout_session(self, session_token: str):
        """Remove session."""
        if session_token in self.sessions:
            del self.sessions[session_token]
            del self.session_expiry[session_token]

# Create login manager
login_manager = LoginManager(user_loader=user_db.get_by_id)

# Create session for alice
session_token = login_manager.create_session(alice, remember=True)
print(f"Session created: {session_token[:20]}...")

# Get user from session
current_user = login_manager.get_user_from_session(session_token)
print(f"Current user: {current_user.username if current_user else None}")

# Logout
login_manager.logout_session(session_token)
current_user = login_manager.get_user_from_session(session_token)
print(f"After logout: {current_user}")
print()

# Example 4: Login Required Decorator
print("Example 4: Login Required Decorator")
print("=" * 60)

class LoginRequired:
    """Decorator to require authentication."""

    def __init__(self, login_manager: LoginManager):
        self.login_manager = login_manager
        self.current_session_token: Optional[str] = None

    def set_session(self, session_token: str):
        """Set current session token."""
        self.current_session_token = session_token

    def __call__(self, func: Callable):
        """Decorator implementation."""
        def wrapper(*args, **kwargs):
            if not self.current_session_token:
                print(f"  [UNAUTHORIZED] Login required for {func.__name__}")
                return {'error': 'Login required'}, 401

            user = self.login_manager.get_user_from_session(self.current_session_token)
            if not user:
                print(f"  [UNAUTHORIZED] Invalid session for {func.__name__}")
                return {'error': 'Invalid session'}, 401

            print(f"  [AUTHORIZED] {user.username} accessing {func.__name__}")
            return func(user, *args, **kwargs)

        return wrapper

# Create login_required decorator
login_required = LoginRequired(login_manager)

@login_required
def get_profile(user: User):
    """Protected route - requires login."""
    return {
        'username': user.username,
        'email': user.email,
        'id': user.id
    }

# Try without login
result = get_profile()
print(f"Without login: {result}")

# Login and try again
session = login_manager.create_session(alice)
login_required.set_session(session)
result = get_profile()
print(f"With login: {result}")
print()

# Example 5: Remember Me Functionality
print("Example 5: Remember Me Functionality")
print("=" * 60)

class RememberMeManager:
    """Manage remember me tokens."""

    def __init__(self):
        self.remember_tokens: Dict[str, int] = {}  # token -> user_id

    def create_remember_token(self, user: User) -> str:
        """Create remember me token."""
        token = secrets.token_urlsafe(48)
        self.remember_tokens[token] = user.id
        return token

    def get_user_from_token(self, token: str, user_loader: Callable) -> Optional[User]:
        """Load user from remember token."""
        user_id = self.remember_tokens.get(token)
        return user_loader(user_id) if user_id else None

    def delete_token(self, token: str):
        """Delete remember token."""
        if token in self.remember_tokens:
            del self.remember_tokens[token]

# Test remember me
remember_me = RememberMeManager()

# Create remember token
remember_token = remember_me.create_remember_token(alice)
print(f"Remember token created: {remember_token[:30]}...")

# Load user from token
loaded_user = remember_me.get_user_from_token(remember_token, user_db.get_by_id)
print(f"User from token: {loaded_user.username if loaded_user else None}")
print()

# Example 6: User Roles and Permissions
print("Example 6: User Roles and Permissions")
print("=" * 60)

@dataclass
class Role:
    """User role."""
    name: str
    permissions: List[str]

class RoleBasedAuth:
    """Role-based authorization."""

    def __init__(self):
        self.roles: Dict[str, Role] = {
            'admin': Role('admin', ['read', 'write', 'delete', 'admin']),
            'editor': Role('editor', ['read', 'write']),
            'viewer': Role('viewer', ['read'])
        }
        self.user_roles: Dict[int, str] = {}

    def assign_role(self, user: User, role_name: str):
        """Assign role to user."""
        self.user_roles[user.id] = role_name

    def has_permission(self, user: User, permission: str) -> bool:
        """Check if user has permission."""
        role_name = self.user_roles.get(user.id)
        if not role_name:
            return False

        role = self.roles.get(role_name)
        return permission in role.permissions if role else False

    def require_permission(self, permission: str):
        """Decorator to require specific permission."""
        def decorator(func: Callable):
            def wrapper(user: User, *args, **kwargs):
                if not self.has_permission(user, permission):
                    print(f"  [FORBIDDEN] User {user.username} lacks '{permission}' permission")
                    return {'error': 'Permission denied'}, 403

                print(f"  [ALLOWED] User {user.username} has '{permission}' permission")
                return func(user, *args, **kwargs)
            return wrapper
        return decorator

# Test role-based auth
rbac = RoleBasedAuth()

# Assign roles
rbac.assign_role(alice, 'admin')
rbac.assign_role(bob, 'viewer')

print(f"Alice has 'delete' permission: {rbac.has_permission(alice, 'delete')}")
print(f"Bob has 'delete' permission: {rbac.has_permission(bob, 'delete')}")
print(f"Bob has 'read' permission: {rbac.has_permission(bob, 'read')}")
print()

# Example 7: Session Management
print("Example 7: Advanced Session Management")
print("=" * 60)

class SessionManager:
    """Advanced session management."""

    def __init__(self):
        self.sessions: Dict[str, Dict] = {}

    def create_session(self, user: User, ip_address: str, user_agent: str) -> str:
        """Create session with metadata."""
        session_id = secrets.token_urlsafe(32)
        self.sessions[session_id] = {
            'user_id': user.id,
            'ip_address': ip_address,
            'user_agent': user_agent,
            'created_at': datetime.now(),
            'last_activity': datetime.now()
        }
        return session_id

    def update_activity(self, session_id: str):
        """Update session last activity."""
        if session_id in self.sessions:
            self.sessions[session_id]['last_activity'] = datetime.now()

    def validate_session(self, session_id: str, ip_address: str) -> bool:
        """Validate session and IP."""
        if session_id not in self.sessions:
            return False

        session = self.sessions[session_id]

        # Check IP matches
        if session['ip_address'] != ip_address:
            print(f"  [SECURITY] IP mismatch for session")
            return False

        # Check activity timeout
        inactive_time = datetime.now() - session['last_activity']
        if inactive_time > timedelta(hours=1):
            print(f"  [TIMEOUT] Session inactive for {inactive_time}")
            return False

        self.update_activity(session_id)
        return True

    def get_active_sessions(self, user_id: int) -> List[Dict]:
        """Get all active sessions for user."""
        return [
            {**session, 'session_id': sid}
            for sid, session in self.sessions.items()
            if session['user_id'] == user_id
        ]

# Test session management
session_mgr = SessionManager()

# Create session
session_id = session_mgr.create_session(alice, '192.168.1.1', 'Mozilla/5.0')
print(f"Session created: {session_id[:20]}...")

# Validate with correct IP
valid = session_mgr.validate_session(session_id, '192.168.1.1')
print(f"Validation (correct IP): {valid}")

# Validate with wrong IP
valid = session_mgr.validate_session(session_id, '192.168.1.2')
print(f"Validation (wrong IP): {valid}")

# Get active sessions
active = session_mgr.get_active_sessions(alice.id)
print(f"Active sessions for alice: {len(active)}")
print()

# Example 8: Two-Factor Authentication
print("Example 8: Two-Factor Authentication (TOTP)")
print("=" * 60)

class TwoFactorAuth:
    """Two-factor authentication manager."""

    def __init__(self):
        self.user_secrets: Dict[int, str] = {}
        self.pending_logins: Dict[str, int] = {}

    def enable_2fa(self, user: User) -> str:
        """Enable 2FA for user and return secret."""
        secret = secrets.token_hex(20)
        self.user_secrets[user.id] = secret
        return secret

    def generate_code(self, secret: str) -> str:
        """Generate 6-digit TOTP code (simplified)."""
        import time
        timestamp = int(time.time() / 30)
        data = f"{secret}:{timestamp}"
        hash_val = hashlib.sha256(data.encode()).hexdigest()
        return hash_val[:6]

    def verify_code(self, user: User, code: str) -> bool:
        """Verify TOTP code."""
        if user.id not in self.user_secrets:
            return True  # 2FA not enabled

        secret = self.user_secrets[user.id]
        valid_code = self.generate_code(secret)
        return code == valid_code

    def create_pending_login(self, user: User) -> str:
        """Create pending login requiring 2FA."""
        token = secrets.token_urlsafe(32)
        self.pending_logins[token] = user.id
        return token

# Test 2FA
twofa = TwoFactorAuth()

# Enable 2FA for alice
secret = twofa.enable_2fa(alice)
print(f"2FA secret: {secret}")

# Generate code
code = twofa.generate_code(secret)
print(f"Generated code: {code}")

# Verify code
valid = twofa.verify_code(alice, code)
print(f"Code verification: {valid}")

# Wrong code
valid = twofa.verify_code(alice, '000000')
print(f"Wrong code verification: {valid}")
print()

# Example 9: Account Lockout
print("Example 9: Account Lockout (Brute Force Protection)")
print("=" * 60)

class AccountLockout:
    """Protect against brute force attacks."""

    def __init__(self, max_attempts: int = 5, lockout_duration: int = 900):
        self.max_attempts = max_attempts
        self.lockout_duration = lockout_duration
        self.failed_attempts: Dict[str, List[datetime]] = {}

    def record_failed_login(self, username: str):
        """Record failed login attempt."""
        if username not in self.failed_attempts:
            self.failed_attempts[username] = []

        self.failed_attempts[username].append(datetime.now())

        # Clean old attempts
        cutoff = datetime.now() - timedelta(seconds=self.lockout_duration)
        self.failed_attempts[username] = [
            attempt for attempt in self.failed_attempts[username]
            if attempt > cutoff
        ]

    def is_locked_out(self, username: str) -> bool:
        """Check if account is locked out."""
        if username not in self.failed_attempts:
            return False

        # Clean old attempts first
        cutoff = datetime.now() - timedelta(seconds=self.lockout_duration)
        recent_attempts = [
            attempt for attempt in self.failed_attempts[username]
            if attempt > cutoff
        ]
        self.failed_attempts[username] = recent_attempts

        return len(recent_attempts) >= self.max_attempts

    def clear_attempts(self, username: str):
        """Clear failed attempts after successful login."""
        if username in self.failed_attempts:
            del self.failed_attempts[username]

# Test account lockout
lockout = AccountLockout(max_attempts=3, lockout_duration=60)

# Simulate failed logins
for i in range(4):
    lockout.record_failed_login('alice')
    locked = lockout.is_locked_out('alice')
    print(f"Attempt {i+1} - Locked out: {locked}")

# Successful login clears lockout
lockout.clear_attempts('alice')
print(f"After successful login - Locked out: {lockout.is_locked_out('alice')}")
print()

# Example 10: Complete Login Flow
print("Example 10: Complete Login Flow")
print("=" * 60)

class AuthenticationService:
    """Complete authentication service."""

    def __init__(self):
        self.user_db = UserDatabase()
        self.login_manager = LoginManager(self.user_db.get_by_id)
        self.lockout = AccountLockout()
        self.session_mgr = SessionManager()

    def register(self, username: str, email: str, password: str) -> Dict:
        """Register new user."""
        # Check if username exists
        if self.user_db.get_by_username(username):
            return {'success': False, 'error': 'Username already exists'}

        # Create user
        user = self.user_db.create_user(username, email, password)
        return {'success': True, 'user_id': user.id}

    def login(self, username: str, password: str, ip_address: str, remember: bool = False) -> Dict:
        """Login user."""
        # Check lockout
        if self.lockout.is_locked_out(username):
            return {'success': False, 'error': 'Account locked due to too many failed attempts'}

        # Authenticate
        user = self.user_db.authenticate(username, password)
        if not user:
            self.lockout.record_failed_login(username)
            return {'success': False, 'error': 'Invalid credentials'}

        # Clear lockout on successful login
        self.lockout.clear_attempts(username)

        # Create session
        session_token = self.login_manager.create_session(user, remember=remember)

        return {
            'success': True,
            'session_token': session_token,
            'user': {'id': user.id, 'username': user.username}
        }

    def logout(self, session_token: str) -> Dict:
        """Logout user."""
        self.login_manager.logout_session(session_token)
        return {'success': True}

# Test complete flow
auth_service = AuthenticationService()

# Register
result = auth_service.register('charlie', 'charlie@example.com', 'pass789')
print(f"Registration: {result}")

# Login with wrong password
result = auth_service.login('charlie', 'wrong', '192.168.1.1')
print(f"Login (wrong password): {result}")

# Login with correct password
result = auth_service.login('charlie', 'pass789', '192.168.1.1', remember=True)
print(f"Login (correct): {result}")

# Logout
if result['success']:
    logout_result = auth_service.logout(result['session_token'])
    print(f"Logout: {logout_result}")
print()

print("=" * 60)
print("FLASK-LOGIN BEST PRACTICES")
print("=" * 60)
print("""
BASIC SETUP:

from flask_login import LoginManager, UserMixin, login_user, logout_user

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

USER MODEL:

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

LOGIN ROUTE:

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    remember = request.form.get('remember', False)

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user, remember=remember)
        return redirect(url_for('dashboard'))

    return 'Invalid credentials'

PROTECTED ROUTES:

from flask_login import login_required, current_user

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome {current_user.username}'

LOGOUT:

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

REMEMBER ME:

login_user(user, remember=True, duration=timedelta(days=30))

CUSTOM AUTHENTICATION:

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

@login_manager.needs_refresh_handler
def refresh():
    return redirect(url_for('reauthenticate'))

SESSION SECURITY:

app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
app.config['SESSION_COOKIE_HTTPONLY'] = True  # No JavaScript access
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF protection
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)

ADDITIONAL SECURITY:

Two-factor authentication:
  - Use TOTP (Time-based One-Time Password)
  - Libraries: pyotp, qrcode

Account lockout:
  - Track failed login attempts
  - Temporary account lock
  - Rate limiting

Password requirements:
  - Minimum length
  - Complexity rules
  - Password history

Session management:
  - IP validation
  - User-agent checking
  - Inactivity timeout
  - Concurrent session limits

Production note: Real Flask-Login provides:
  - Session management
  - Remember me functionality
  - User loader callbacks
  - Login/logout handling
  - Anonymous user support
  - Custom authentication
  - Fresh login tracking
  - Integration with Flask
  - Cookie-based sessions
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 19 COMPLETE: Flask Extensions (CORS, Caching, Authentication)")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 747: Flask-CORS")
    print(f"  - Lesson 746: Flask-Caching")
    print(f"  - Lesson 750: Flask-Login Authentication")
    print("\nAll lessons upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
