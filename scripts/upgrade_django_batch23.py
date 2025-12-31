import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons
lesson_765 = next(l for l in lessons if l['id'] == 765)  # Custom Middleware
lesson_754 = next(l for l in lessons if l['id'] == 754)  # Class-Based Views
lesson_756 = next(l for l in lessons if l['id'] == 756)  # DRF ViewSet

# Lesson 765: Django Custom Middleware
lesson_765['fullSolution'] = '''"""
Django Custom Middleware - Comprehensive Guide

Covers middleware basics, request/response processing, middleware ordering,
custom middleware classes, authentication middleware, logging, caching,
CORS, rate limiting, and middleware best practices.

**Zero Package Installation Required**
"""

import time
from typing import Callable, Dict, Any, Optional, List
from datetime import datetime, timedelta

# Example 1: Basic Middleware Structure
print("="*60)
print("Example 1: Basic Middleware Structure")
print("="*60)

class SimpleMiddleware:
    """Basic middleware implementation."""

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        print("  [INIT] SimpleMiddleware initialized")

    def __call__(self, request: Dict) -> Dict:
        """Process request and response."""
        # Before view
        print(f"  [REQUEST] {request['method']} {request['path']}")

        # Call next middleware/view
        response = self.get_response(request)

        # After view
        print(f"  [RESPONSE] Status: {response.get('status', 200)}")

        return response

def example_view(request):
    """Simple view."""
    return {'status': 200, 'body': 'Hello World'}

# Simulate middleware chain
print("\\nMiddleware execution:")
middleware = SimpleMiddleware(example_view)
request = {'method': 'GET', 'path': '/api/test'}
response = middleware(request)
print()

# Example 2: Request Processing Middleware
print("="*60)
print("Example 2: Request Processing Middleware")
print("="*60)

class RequestProcessingMiddleware:
    """Middleware that processes requests."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Add request ID
        request['request_id'] = f"req_{int(time.time() * 1000)}"

        # Add timestamp
        request['timestamp'] = datetime.now()

        # Parse headers
        request['parsed_headers'] = self.parse_headers(request.get('headers', {}))

        print(f"  [PROCESSED] Request ID: {request['request_id']}")

        response = self.get_response(request)
        return response

    def parse_headers(self, headers: Dict) -> Dict:
        """Parse and validate headers."""
        parsed = {}
        for key, value in headers.items():
            parsed[key.lower()] = value
        return parsed

request = {
    'method': 'POST',
    'path': '/api/users',
    'headers': {'Content-Type': 'application/json', 'User-Agent': 'TestClient'}
}

middleware = RequestProcessingMiddleware(example_view)
response = middleware(request)
print(f"  Request ID assigned: {request['request_id']}")
print()

# Example 3: Response Processing Middleware
print("="*60)
print("Example 3: Response Processing Middleware")
print("="*60)

class ResponseProcessingMiddleware:
    """Middleware that processes responses."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add headers
        if 'headers' not in response:
            response['headers'] = {}

        response['headers']['X-Request-ID'] = request.get('request_id', 'unknown')
        response['headers']['X-Response-Time'] = datetime.now().isoformat()
        response['headers']['X-Content-Type-Options'] = 'nosniff'
        response['headers']['X-Frame-Options'] = 'DENY'

        print(f"  [HEADERS] Added security headers")

        return response

middleware_chain = ResponseProcessingMiddleware(
    RequestProcessingMiddleware(example_view)
)

request = {'method': 'GET', 'path': '/api/data'}
response = middleware_chain(request)
print(f"  Response headers: {list(response['headers'].keys())}")
print()

# Example 4: Authentication Middleware
print("="*60)
print("Example 4: Authentication Middleware")
print("="*60)

class AuthenticationMiddleware:
    """Middleware for JWT token authentication."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = ['/api/login', '/api/register']

    def __call__(self, request):
        # Skip auth for public paths
        if request['path'] in self.public_paths:
            print(f"  [AUTH] Public path, skipping authentication")
            return self.get_response(request)

        # Check for auth header
        auth_header = request.get('headers', {}).get('Authorization')

        if not auth_header:
            print(f"  [AUTH] Missing authorization header")
            return {'status': 401, 'body': 'Unauthorized'}

        # Validate token (simplified)
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]
            user = self.validate_token(token)

            if user:
                request['user'] = user
                print(f"  [AUTH] User authenticated: {user['username']}")
                return self.get_response(request)

        print(f"  [AUTH] Invalid token")
        return {'status': 401, 'body': 'Invalid token'}

    def validate_token(self, token: str) -> Optional[Dict]:
        """Validate JWT token (simplified)."""
        # In real app, decode and verify JWT
        if token == 'valid_token':
            return {'id': 1, 'username': 'alice'}
        return None

auth_middleware = AuthenticationMiddleware(example_view)

# Test with valid token
print("\\nWith valid token:")
request = {
    'method': 'GET',
    'path': '/api/profile',
    'headers': {'Authorization': 'Bearer valid_token'}
}
response = auth_middleware(request)
print(f"  Status: {response['status']}")

# Test without token
print("\\nWithout token:")
request = {'method': 'GET', 'path': '/api/profile', 'headers': {}}
response = auth_middleware(request)
print(f"  Status: {response['status']}")
print()

# Example 5: Logging Middleware
print("="*60)
print("Example 5: Logging Middleware")
print("="*60)

class LoggingMiddleware:
    """Middleware for request/response logging."""

    def __init__(self, get_response):
        self.get_response = get_response
        self.logs = []

    def __call__(self, request):
        start_time = time.time()

        # Log request
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'method': request['method'],
            'path': request['path'],
            'request_id': request.get('request_id', 'unknown')
        }

        # Process request
        response = self.get_response(request)

        # Calculate duration
        duration = (time.time() - start_time) * 1000

        # Log response
        log_entry.update({
            'status': response.get('status', 200),
            'duration_ms': round(duration, 2)
        })

        self.logs.append(log_entry)

        print(f"  [LOG] {log_entry['method']} {log_entry['path']} - {log_entry['status']} ({log_entry['duration_ms']}ms)")

        return response

logging_middleware = LoggingMiddleware(example_view)

for i in range(3):
    request = {'method': 'GET', 'path': f'/api/item/{i}', 'request_id': f'req_{i}'}
    response = logging_middleware(request)

print(f"\\n  Total requests logged: {len(logging_middleware.logs)}")
print()

# Example 6: Rate Limiting Middleware
print("="*60)
print("Example 6: Rate Limiting Middleware")
print("="*60)

class RateLimitMiddleware:
    """Middleware for rate limiting."""

    def __init__(self, get_response, max_requests=5, window_seconds=60):
        self.get_response = get_response
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}  # ip -> list of timestamps

    def __call__(self, request):
        ip = request.get('ip', 'unknown')
        now = datetime.now()

        # Clean old requests
        if ip in self.requests:
            cutoff = now - timedelta(seconds=self.window_seconds)
            self.requests[ip] = [ts for ts in self.requests[ip] if ts > cutoff]
        else:
            self.requests[ip] = []

        # Check rate limit
        if len(self.requests[ip]) >= self.max_requests:
            print(f"  [RATE LIMIT] IP {ip} exceeded limit")
            return {
                'status': 429,
                'body': 'Too many requests',
                'headers': {'Retry-After': str(self.window_seconds)}
            }

        # Record request
        self.requests[ip].append(now)

        print(f"  [RATE LIMIT] IP {ip}: {len(self.requests[ip])}/{self.max_requests}")

        return self.get_response(request)

rate_limit = RateLimitMiddleware(example_view, max_requests=3, window_seconds=60)

# Simulate multiple requests from same IP
for i in range(5):
    request = {'method': 'GET', 'path': '/api/data', 'ip': '192.168.1.1'}
    response = rate_limit(request)
    print(f"    Request {i+1}: Status {response['status']}")
print()

# Example 7: CORS Middleware
print("="*60)
print("Example 7: CORS Middleware")
print("="*60)

class CORSMiddleware:
    """Middleware for CORS handling."""

    def __init__(self, get_response, allowed_origins=None):
        self.get_response = get_response
        self.allowed_origins = allowed_origins or ['*']

    def __call__(self, request):
        origin = request.get('headers', {}).get('Origin')

        # Handle preflight
        if request['method'] == 'OPTIONS':
            print(f"  [CORS] Handling preflight request")
            return self.preflight_response(origin)

        # Process normal request
        response = self.get_response(request)

        # Add CORS headers
        if origin and self.is_origin_allowed(origin):
            if 'headers' not in response:
                response['headers'] = {}

            response['headers']['Access-Control-Allow-Origin'] = origin
            response['headers']['Access-Control-Allow-Credentials'] = 'true'

            print(f"  [CORS] Added headers for origin: {origin}")

        return response

    def is_origin_allowed(self, origin: str) -> bool:
        """Check if origin is allowed."""
        return '*' in self.allowed_origins or origin in self.allowed_origins

    def preflight_response(self, origin: str) -> Dict:
        """Return preflight response."""
        return {
            'status': 200,
            'headers': {
                'Access-Control-Allow-Origin': origin if self.is_origin_allowed(origin) else '',
                'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization',
                'Access-Control-Max-Age': '3600'
            }
        }

cors = CORSMiddleware(example_view, allowed_origins=['https://example.com'])

# Preflight request
print("\\nPreflight request:")
request = {
    'method': 'OPTIONS',
    'path': '/api/data',
    'headers': {'Origin': 'https://example.com'}
}
response = cors(request)
print(f"  Status: {response['status']}")

# Normal request
print("\\nNormal request:")
request = {
    'method': 'GET',
    'path': '/api/data',
    'headers': {'Origin': 'https://example.com'}
}
response = cors(request)
print(f"  CORS headers added: {'Access-Control-Allow-Origin' in response.get('headers', {})}")
print()

# Example 8: Caching Middleware
print("="*60)
print("Example 8: Caching Middleware")
print("="*60)

class CachingMiddleware:
    """Middleware for response caching."""

    def __init__(self, get_response, cache_timeout=60):
        self.get_response = get_response
        self.cache_timeout = cache_timeout
        self.cache = {}

    def __call__(self, request):
        # Only cache GET requests
        if request['method'] != 'GET':
            return self.get_response(request)

        cache_key = f"{request['method']}:{request['path']}"

        # Check cache
        if cache_key in self.cache:
            cached_response, timestamp = self.cache[cache_key]
            age = (datetime.now() - timestamp).total_seconds()

            if age < self.cache_timeout:
                print(f"  [CACHE HIT] Returning cached response (age: {age:.1f}s)")
                return cached_response.copy()
            else:
                print(f"  [CACHE EXPIRED] Cache entry too old ({age:.1f}s)")

        # Cache miss
        print(f"  [CACHE MISS] Fetching fresh response")
        response = self.get_response(request)

        # Store in cache
        self.cache[cache_key] = (response.copy(), datetime.now())

        return response

caching = CachingMiddleware(example_view, cache_timeout=10)

# First request - cache miss
request = {'method': 'GET', 'path': '/api/data'}
response1 = caching(request)

# Second request - cache hit
response2 = caching(request)

# POST request - no caching
request_post = {'method': 'POST', 'path': '/api/data'}
response3 = caching(request_post)
print()

# Example 9: Exception Handling Middleware
print("="*60)
print("Example 9: Exception Handling Middleware")
print("="*60)

class ExceptionHandlingMiddleware:
    """Middleware for centralized exception handling."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except ValueError as e:
            print(f"  [ERROR] ValueError: {str(e)}")
            return {
                'status': 400,
                'body': {'error': 'Bad Request', 'message': str(e)}
            }
        except PermissionError as e:
            print(f"  [ERROR] PermissionError: {str(e)}")
            return {
                'status': 403,
                'body': {'error': 'Forbidden', 'message': str(e)}
            }
        except Exception as e:
            print(f"  [ERROR] Unexpected error: {str(e)}")
            return {
                'status': 500,
                'body': {'error': 'Internal Server Error'}
            }

def failing_view(request):
    """View that raises an exception."""
    raise ValueError("Invalid input data")

exception_middleware = ExceptionHandlingMiddleware(failing_view)

request = {'method': 'POST', 'path': '/api/create'}
response = exception_middleware(request)
print(f"  Response status: {response['status']}")
print(f"  Error: {response['body']}")
print()

# Example 10: Complete Middleware Stack
print("="*60)
print("Example 10: Complete Middleware Stack")
print("="*60)

def build_middleware_stack(view, middlewares):
    """Build middleware stack from list."""
    handler = view
    for middleware_class in reversed(middlewares):
        handler = middleware_class(handler)
    return handler

def my_view(request):
    """Example view."""
    return {
        'status': 200,
        'body': {
            'message': 'Success',
            'user': request.get('user', {}).get('username', 'anonymous')
        }
    }

# Build complete stack
middleware_stack = build_middleware_stack(my_view, [
    LoggingMiddleware,
    ExceptionHandlingMiddleware,
    CORSMiddleware,
    AuthenticationMiddleware,
    RateLimitMiddleware
])

print("\\nMiddleware stack order:")
print("  1. RateLimitMiddleware (outermost)")
print("  2. AuthenticationMiddleware")
print("  3. CORSMiddleware")
print("  4. ExceptionHandlingMiddleware")
print("  5. LoggingMiddleware")
print("  6. View (innermost)")

print("\\nProcessing request through middleware stack:")
request = {
    'method': 'GET',
    'path': '/api/profile',
    'headers': {'Authorization': 'Bearer valid_token', 'Origin': 'https://example.com'},
    'ip': '192.168.1.100',
    'request_id': 'req_12345'
}

response = middleware_stack(request)
print(f"\\nFinal response status: {response.get('status')}")

print("\\n" + "="*60)
print("All custom middleware examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 765: Django Custom Middleware ({len(lesson_765['fullSolution']):,} chars)")

# Lesson 754: Django Class-Based Views
lesson_754['fullSolution'] = '''"""
Django Class-Based Views (CBVs) - Comprehensive Guide

Covers view hierarchy, generic views, ListView, DetailView, CreateView,
UpdateView, DeleteView, FormView, mixins, method override, context data,
queryset customization, and CBV best practices.

**Zero Package Installation Required**
"""

from typing import Dict, List, Any, Optional, Callable
from datetime import datetime

# Example 1: Basic Class-Based View
print("="*60)
print("Example 1: Basic Class-Based View")
print("="*60)

class View:
    """Base class for all views."""

    def __init__(self):
        self.request = None

    def dispatch(self, request: Dict) -> Dict:
        """Dispatch request to appropriate method."""
        self.request = request
        method = request.get('method', 'GET').lower()
        handler = getattr(self, method, self.http_method_not_allowed)
        return handler(request)

    def http_method_not_allowed(self, request: Dict) -> Dict:
        """Handle unsupported HTTP methods."""
        return {'status': 405, 'body': 'Method Not Allowed'}

class HomeView(View):
    """Simple home page view."""

    def get(self, request: Dict) -> Dict:
        """Handle GET requests."""
        print(f"  [GET] Processing request to {request['path']}")
        return {
            'status': 200,
            'body': '<h1>Welcome Home</h1>',
            'content_type': 'text/html'
        }

# Simulate request
home_view = HomeView()
request = {'method': 'GET', 'path': '/'}
response = home_view.dispatch(request)
print(f"  Response: {response['status']} - {len(response['body'])} bytes")
print()

# Example 2: TemplateView
print("="*60)
print("Example 2: TemplateView")
print("="*60)

class TemplateView(View):
    """Render a template with context."""

    template_name = None

    def get_context_data(self, **kwargs) -> Dict:
        """Get context for template."""
        return kwargs

    def render_to_response(self, context: Dict) -> Dict:
        """Render template with context."""
        # Simplified template rendering
        html = f"<html><body><h1>{context.get('title', 'Page')}</h1>"
        html += f"<p>{context.get('content', '')}</p></body></html>"
        return {'status': 200, 'body': html}

    def get(self, request: Dict) -> Dict:
        """Handle GET requests."""
        context = self.get_context_data()
        return self.render_to_response(context)

class AboutView(TemplateView):
    """About page view."""

    template_name = 'about.html'

    def get_context_data(self, **kwargs) -> Dict:
        """Add custom context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['content'] = 'This is the about page'
        return context

about_view = AboutView()
response = about_view.dispatch({'method': 'GET', 'path': '/about'})
print(f"  Rendered template: {about_view.template_name}")
print(f"  Response length: {len(response['body'])} bytes")
print()

# Example 3: ListView
print("="*60)
print("Example 3: ListView")
print("="*60)

# Sample data
ARTICLES = [
    {'id': 1, 'title': 'First Post', 'author': 'Alice', 'published': '2024-01-15'},
    {'id': 2, 'title': 'Second Post', 'author': 'Bob', 'published': '2024-01-20'},
    {'id': 3, 'title': 'Third Post', 'author': 'Alice', 'published': '2024-01-25'},
]

class ListView(TemplateView):
    """Display list of objects."""

    model = None
    queryset = None
    context_object_name = 'object_list'
    paginate_by = None

    def get_queryset(self) -> List[Dict]:
        """Get queryset for the view."""
        if self.queryset is not None:
            return self.queryset
        return []

    def get_context_data(self, **kwargs) -> Dict:
        """Add object list to context."""
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context[self.context_object_name] = queryset
        context['count'] = len(queryset)
        return context

class ArticleListView(ListView):
    """List all articles."""

    template_name = 'article_list.html'
    context_object_name = 'articles'

    def get_queryset(self) -> List[Dict]:
        """Get all articles."""
        return ARTICLES

article_list_view = ArticleListView()
response = article_list_view.dispatch({'method': 'GET', 'path': '/articles'})
print(f"  Listed {len(ARTICLES)} articles")
print(f"  Articles: {[a['title'] for a in ARTICLES]}")
print()

# Example 4: DetailView
print("="*60)
print("Example 4: DetailView")
print("="*60)

class DetailView(TemplateView):
    """Display single object detail."""

    model = None
    context_object_name = 'object'
    pk_url_kwarg = 'pk'

    def get_object(self, **kwargs) -> Optional[Dict]:
        """Get single object by pk."""
        pk = kwargs.get(self.pk_url_kwarg)
        # Simplified object lookup
        for item in ARTICLES:
            if item['id'] == pk:
                return item
        return None

    def get_context_data(self, **kwargs) -> Dict:
        """Add object to context."""
        context = super().get_context_data(**kwargs)
        obj = self.get_object(**kwargs)
        context[self.context_object_name] = obj
        return context

class ArticleDetailView(DetailView):
    """Show single article."""

    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get(self, request: Dict, pk: int) -> Dict:
        """Handle GET with pk."""
        article = self.get_object(pk=pk)
        if not article:
            return {'status': 404, 'body': 'Article not found'}

        context = self.get_context_data(pk=pk)
        print(f"  [DETAIL] Article: {article['title']}")
        print(f"  Author: {article['author']}, Published: {article['published']}")
        return self.render_to_response(context)

detail_view = ArticleDetailView()
response = detail_view.get({'method': 'GET', 'path': '/articles/1'}, pk=1)
print(f"  Response status: {response['status']}")
print()

# Example 5: CreateView
print("="*60)
print("Example 5: CreateView")
print("="*60)

class FormView(TemplateView):
    """Display and process forms."""

    form_class = None
    success_url = None

    def get_form(self, data=None) -> Dict:
        """Get form instance."""
        return {'data': data or {}, 'errors': {}}

    def form_valid(self, form: Dict) -> Dict:
        """Handle valid form."""
        return {'status': 302, 'location': self.success_url}

    def form_invalid(self, form: Dict) -> Dict:
        """Handle invalid form."""
        return self.render_to_response({'form': form})

    def post(self, request: Dict) -> Dict:
        """Handle POST requests."""
        form = self.get_form(data=request.get('POST', {}))
        if self.validate_form(form):
            return self.form_valid(form)
        return self.form_invalid(form)

    def validate_form(self, form: Dict) -> bool:
        """Validate form data."""
        return len(form['errors']) == 0

class CreateView(FormView):
    """Create new object."""

    model = None
    fields = []

    def form_valid(self, form: Dict) -> Dict:
        """Save new object."""
        obj = self.save_object(form['data'])
        print(f"  [CREATE] Created new object: {obj}")
        return super().form_valid(form)

    def save_object(self, data: Dict) -> Dict:
        """Save object to database."""
        new_obj = {
            'id': len(ARTICLES) + 1,
            **data,
            'published': datetime.now().strftime('%Y-%m-%d')
        }
        ARTICLES.append(new_obj)
        return new_obj

class ArticleCreateView(CreateView):
    """Create new article."""

    template_name = 'article_form.html'
    fields = ['title', 'author']
    success_url = '/articles'

    def validate_form(self, form: Dict) -> bool:
        """Validate article form."""
        data = form['data']
        errors = {}

        if not data.get('title'):
            errors['title'] = 'Title is required'
        if not data.get('author'):
            errors['author'] = 'Author is required'

        form['errors'] = errors
        return len(errors) == 0

create_view = ArticleCreateView()
request = {
    'method': 'POST',
    'path': '/articles/create',
    'POST': {'title': 'New Article', 'author': 'Charlie'}
}
response = create_view.dispatch(request)
print(f"  Total articles now: {len(ARTICLES)}")
print()

# Example 6: UpdateView
print("="*60)
print("Example 6: UpdateView")
print("="*60)

class UpdateView(FormView):
    """Update existing object."""

    model = None
    fields = []
    pk_url_kwarg = 'pk'

    def get_object(self, **kwargs) -> Optional[Dict]:
        """Get object to update."""
        pk = kwargs.get(self.pk_url_kwarg)
        for item in ARTICLES:
            if item['id'] == pk:
                return item
        return None

    def get_form(self, data=None) -> Dict:
        """Get form with initial data."""
        obj = self.get_object(pk=self.current_pk)
        return {
            'data': data or obj,
            'errors': {},
            'instance': obj
        }

    def form_valid(self, form: Dict) -> Dict:
        """Update object."""
        obj = form['instance']
        obj.update(form['data'])
        print(f"  [UPDATE] Updated object: {obj}")
        return super().form_valid(form)

    def post(self, request: Dict, pk: int) -> Dict:
        """Handle POST with pk."""
        self.current_pk = pk
        return super().post(request)

class ArticleUpdateView(UpdateView):
    """Update article."""

    template_name = 'article_form.html'
    fields = ['title', 'author']
    success_url = '/articles'

update_view = ArticleUpdateView()
update_view.current_pk = 1
request = {
    'method': 'POST',
    'path': '/articles/1/edit',
    'POST': {'title': 'Updated First Post', 'author': 'Alice'}
}
response = update_view.post(request, pk=1)
print(f"  Updated article 1: {ARTICLES[0]['title']}")
print()

# Example 7: DeleteView
print("="*60)
print("Example 7: DeleteView")
print("="*60)

class DeleteView(DetailView):
    """Delete object."""

    success_url = None

    def post(self, request: Dict, pk: int) -> Dict:
        """Handle POST to delete."""
        obj = self.get_object(pk=pk)
        if not obj:
            return {'status': 404, 'body': 'Not found'}

        self.delete_object(obj)
        print(f"  [DELETE] Deleted object: {obj}")
        return {'status': 302, 'location': self.success_url}

    def delete_object(self, obj: Dict):
        """Delete object from database."""
        ARTICLES.remove(obj)

class ArticleDeleteView(DeleteView):
    """Delete article."""

    template_name = 'article_confirm_delete.html'
    success_url = '/articles'

# Add a test article
ARTICLES.append({'id': 99, 'title': 'To Delete', 'author': 'Test', 'published': '2024-01-01'})
delete_view = ArticleDeleteView()
response = delete_view.post({'method': 'POST', 'path': '/articles/99/delete'}, pk=99)
print(f"  Remaining articles: {len(ARTICLES)}")
print()

# Example 8: Mixins
print("="*60)
print("Example 8: Mixins")
print("="*60)

class LoginRequiredMixin:
    """Require user to be logged in."""

    def dispatch(self, request: Dict) -> Dict:
        """Check authentication before dispatch."""
        if not request.get('user'):
            print(f"  [AUTH] User not authenticated, redirecting to login")
            return {'status': 302, 'location': '/login'}

        print(f"  [AUTH] User {request['user']['username']} authenticated")
        return super().dispatch(request)

class PermissionRequiredMixin:
    """Require specific permission."""

    permission_required = None

    def has_permission(self, request: Dict) -> bool:
        """Check if user has permission."""
        user_permissions = request.get('user', {}).get('permissions', [])
        return self.permission_required in user_permissions

    def dispatch(self, request: Dict) -> Dict:
        """Check permission before dispatch."""
        if not self.has_permission(request):
            print(f"  [PERM] Permission denied: {self.permission_required}")
            return {'status': 403, 'body': 'Forbidden'}

        print(f"  [PERM] Permission granted: {self.permission_required}")
        return super().dispatch(request)

class ProtectedArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """Create view with auth and permission checks."""

    permission_required = 'create_article'
    fields = ['title', 'author']
    success_url = '/articles'

protected_view = ProtectedArticleCreateView()

# Test without auth
print("\\nWithout authentication:")
response = protected_view.dispatch({'method': 'POST', 'path': '/articles/create'})
print(f"  Status: {response['status']}")

# Test with auth but no permission
print("\\nWith auth but no permission:")
request = {
    'method': 'POST',
    'path': '/articles/create',
    'user': {'username': 'bob', 'permissions': []}
}
response = protected_view.dispatch(request)
print(f"  Status: {response['status']}")

# Test with auth and permission
print("\\nWith auth and permission:")
request = {
    'method': 'POST',
    'path': '/articles/create',
    'user': {'username': 'alice', 'permissions': ['create_article']},
    'POST': {'title': 'Protected Article', 'author': 'Alice'}
}
response = protected_view.dispatch(request)
print(f"  Status: {response['status']}")
print()

# Example 9: Custom QuerySet Filtering
print("="*60)
print("Example 9: Custom QuerySet Filtering")
print("="*60)

class FilteredListView(ListView):
    """ListView with custom filtering."""

    def get_queryset(self) -> List[Dict]:
        """Get filtered queryset."""
        queryset = super().get_queryset()

        # Apply filters from query params
        author_filter = self.request.get('GET', {}).get('author')
        if author_filter:
            queryset = [item for item in queryset if item['author'] == author_filter]
            print(f"  [FILTER] Filtered by author: {author_filter}")

        # Apply ordering
        queryset = sorted(queryset, key=lambda x: x['published'], reverse=True)
        print(f"  [FILTER] Ordered by published date (desc)")

        return queryset

class FilteredArticleListView(FilteredListView):
    """Filtered article list."""

    context_object_name = 'articles'

    def get_queryset(self) -> List[Dict]:
        """Get articles."""
        # Start with all articles
        self.queryset = ARTICLES
        return super().get_queryset()

filtered_view = FilteredArticleListView()
filtered_view.request = {'method': 'GET', 'path': '/articles', 'GET': {'author': 'Alice'}}
response = filtered_view.dispatch(filtered_view.request)
print(f"  Results: {len([a for a in ARTICLES if a['author'] == 'Alice'])} articles")
print()

# Example 10: Method Override Pattern
print("="*60)
print("Example 10: Method Override Pattern")
print("="*60)

class BaseArticleView(ListView):
    """Base view for articles with common functionality."""

    context_object_name = 'articles'

    def get_queryset(self) -> List[Dict]:
        """Get base queryset."""
        return ARTICLES

    def get_context_data(self, **kwargs) -> Dict:
        """Add common context."""
        context = super().get_context_data(**kwargs)
        context['site_name'] = 'My Blog'
        context['current_year'] = datetime.now().year
        return context

class PublishedArticleView(BaseArticleView):
    """Show only published articles."""

    def get_queryset(self) -> List[Dict]:
        """Filter for published only."""
        queryset = super().get_queryset()
        # In real app, filter by published status
        print(f"  [OVERRIDE] Applying published filter")
        return queryset

    def get_context_data(self, **kwargs) -> Dict:
        """Add extra context."""
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Published Articles'
        context['show_drafts'] = False
        print(f"  [OVERRIDE] Added custom context: page_title, show_drafts")
        return context

published_view = PublishedArticleView()
response = published_view.dispatch({'method': 'GET', 'path': '/published'})
print(f"  Context keys: {['site_name', 'current_year', 'page_title', 'show_drafts']}")
print()

print("="*60)
print("All Django Class-Based Views examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 754: Django Class-Based Views ({len(lesson_754['fullSolution']):,} chars)")

# Lesson 756: Django REST Framework ViewSet
lesson_756['fullSolution'] = '''"""
Django REST Framework ViewSet - Comprehensive Guide

Covers ViewSet basics, ModelViewSet, action decorators, custom actions,
filtering, pagination, permissions, serializers, bulk operations,
nested resources, and ViewSet best practices.

**Zero Package Installation Required**
"""

from typing import Dict, List, Any, Optional, Callable
from datetime import datetime

# Example 1: Basic ViewSet Structure
print("="*60)
print("Example 1: Basic ViewSet Structure")
print("="*60)

class ViewSet:
    """Base ViewSet class."""

    def __init__(self):
        self.action = None
        self.request = None

    def dispatch(self, request: Dict, action: str, **kwargs) -> Dict:
        """Dispatch request to appropriate action."""
        self.request = request
        self.action = action
        handler = getattr(self, action, None)

        if not handler:
            return {'status': 405, 'body': 'Action not allowed'}

        return handler(request, **kwargs)

class SimpleViewSet(ViewSet):
    """Simple ViewSet with basic actions."""

    def list(self, request: Dict) -> Dict:
        """List all items."""
        print(f"  [LIST] Retrieving all items")
        return {'status': 200, 'data': []}

    def retrieve(self, request: Dict, pk: int) -> Dict:
        """Retrieve single item."""
        print(f"  [RETRIEVE] Getting item {pk}")
        return {'status': 200, 'data': {'id': pk}}

    def create(self, request: Dict) -> Dict:
        """Create new item."""
        print(f"  [CREATE] Creating new item")
        return {'status': 201, 'data': request.get('data', {})}

    def update(self, request: Dict, pk: int) -> Dict:
        """Update item."""
        print(f"  [UPDATE] Updating item {pk}")
        return {'status': 200, 'data': request.get('data', {})}

    def destroy(self, request: Dict, pk: int) -> Dict:
        """Delete item."""
        print(f"  [DESTROY] Deleting item {pk}")
        return {'status': 204}

viewset = SimpleViewSet()

# Test different actions
print("\\nTesting basic CRUD actions:")
viewset.dispatch({'method': 'GET'}, 'list')
viewset.dispatch({'method': 'GET'}, 'retrieve', pk=1)
viewset.dispatch({'method': 'POST', 'data': {'name': 'New Item'}}, 'create')
viewset.dispatch({'method': 'PUT', 'data': {'name': 'Updated'}}, 'update', pk=1)
viewset.dispatch({'method': 'DELETE'}, 'destroy', pk=1)
print()

# Example 2: ModelViewSet with Serializer
print("="*60)
print("Example 2: ModelViewSet with Serializer")
print("="*60)

# Sample data store
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99, 'stock': 10},
    {'id': 2, 'name': 'Mouse', 'price': 29.99, 'stock': 50},
    {'id': 3, 'name': 'Keyboard', 'price': 79.99, 'stock': 30},
]

class Serializer:
    """Base serializer."""

    def __init__(self, data=None, instance=None):
        self.data = data
        self.instance = instance
        self.errors = {}

    def is_valid(self) -> bool:
        """Validate data."""
        return len(self.errors) == 0

    def save(self) -> Dict:
        """Save data."""
        if self.instance:
            self.instance.update(self.data)
            return self.instance
        else:
            new_obj = {'id': max([p['id'] for p in PRODUCTS]) + 1, **self.data}
            PRODUCTS.append(new_obj)
            return new_obj

class ProductSerializer(Serializer):
    """Product serializer."""

    def is_valid(self) -> bool:
        """Validate product data."""
        if not self.data.get('name'):
            self.errors['name'] = 'Name is required'
        if self.data.get('price', 0) <= 0:
            self.errors['price'] = 'Price must be positive'

        return super().is_valid()

class ModelViewSet(ViewSet):
    """ViewSet with model operations."""

    queryset = []
    serializer_class = None

    def get_queryset(self) -> List[Dict]:
        """Get queryset."""
        return self.queryset

    def get_object(self, pk: int) -> Optional[Dict]:
        """Get single object by pk."""
        for item in self.get_queryset():
            if item['id'] == pk:
                return item
        return None

    def get_serializer(self, data=None, instance=None):
        """Get serializer instance."""
        return self.serializer_class(data=data, instance=instance)

    def list(self, request: Dict) -> Dict:
        """List all objects."""
        queryset = self.get_queryset()
        print(f"  [LIST] Retrieved {len(queryset)} items")
        return {'status': 200, 'data': queryset, 'count': len(queryset)}

    def retrieve(self, request: Dict, pk: int) -> Dict:
        """Retrieve single object."""
        obj = self.get_object(pk)
        if not obj:
            return {'status': 404, 'error': 'Not found'}

        print(f"  [RETRIEVE] Retrieved: {obj['name']}")
        return {'status': 200, 'data': obj}

    def create(self, request: Dict) -> Dict:
        """Create new object."""
        serializer = self.get_serializer(data=request.get('data', {}))

        if not serializer.is_valid():
            print(f"  [CREATE ERROR] Validation failed: {serializer.errors}")
            return {'status': 400, 'errors': serializer.errors}

        obj = serializer.save()
        print(f"  [CREATE] Created: {obj['name']}")
        return {'status': 201, 'data': obj}

    def update(self, request: Dict, pk: int) -> Dict:
        """Update object."""
        obj = self.get_object(pk)
        if not obj:
            return {'status': 404, 'error': 'Not found'}

        serializer = self.get_serializer(data=request.get('data', {}), instance=obj)

        if not serializer.is_valid():
            return {'status': 400, 'errors': serializer.errors}

        updated = serializer.save()
        print(f"  [UPDATE] Updated: {updated['name']}")
        return {'status': 200, 'data': updated}

    def destroy(self, request: Dict, pk: int) -> Dict:
        """Delete object."""
        obj = self.get_object(pk)
        if not obj:
            return {'status': 404, 'error': 'Not found'}

        PRODUCTS.remove(obj)
        print(f"  [DESTROY] Deleted: {obj['name']}")
        return {'status': 204}

class ProductViewSet(ModelViewSet):
    """Product ViewSet."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer

product_viewset = ProductViewSet()

# Test CRUD operations
print("\\nListing products:")
response = product_viewset.dispatch({'method': 'GET'}, 'list')

print("\\nCreating new product:")
response = product_viewset.dispatch({
    'method': 'POST',
    'data': {'name': 'Monitor', 'price': 299.99, 'stock': 15}
}, 'create')

print(f"  Total products: {len(PRODUCTS)}")
print()

# Example 3: Custom Actions
print("="*60)
print("Example 3: Custom Actions")
print("="*60)

class ActionViewSet(ModelViewSet):
    """ViewSet with custom actions."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer

    def low_stock(self, request: Dict) -> Dict:
        """Custom action: Get low stock items."""
        threshold = int(request.get('query_params', {}).get('threshold', 20))
        low_stock_items = [p for p in self.get_queryset() if p['stock'] < threshold]

        print(f"  [CUSTOM ACTION] Found {len(low_stock_items)} low stock items (< {threshold})")
        return {'status': 200, 'data': low_stock_items, 'count': len(low_stock_items)}

    def price_range(self, request: Dict) -> Dict:
        """Custom action: Filter by price range."""
        min_price = float(request.get('query_params', {}).get('min', 0))
        max_price = float(request.get('query_params', {}).get('max', 10000))

        filtered = [p for p in self.get_queryset() if min_price <= p['price'] <= max_price]
        print(f"  [CUSTOM ACTION] Found {len(filtered)} products in range ${min_price}-${max_price}")

        return {'status': 200, 'data': filtered, 'count': len(filtered)}

    def bulk_update_stock(self, request: Dict) -> Dict:
        """Custom action: Bulk update stock."""
        updates = request.get('data', {}).get('updates', [])
        updated_count = 0

        for update in updates:
            obj = self.get_object(update['id'])
            if obj:
                obj['stock'] = update['stock']
                updated_count += 1

        print(f"  [BULK UPDATE] Updated stock for {updated_count} products")
        return {'status': 200, 'message': f'Updated {updated_count} products'}

action_viewset = ActionViewSet()

# Test custom actions
print("\\nGetting low stock items:")
response = action_viewset.dispatch({
    'method': 'GET',
    'query_params': {'threshold': '25'}
}, 'low_stock')

print("\\nFiltering by price range:")
response = action_viewset.dispatch({
    'method': 'GET',
    'query_params': {'min': '20', 'max': '100'}
}, 'price_range')

print("\\nBulk updating stock:")
response = action_viewset.dispatch({
    'method': 'POST',
    'data': {
        'updates': [
            {'id': 1, 'stock': 15},
            {'id': 2, 'stock': 60}
        ]
    }
}, 'bulk_update_stock')
print()

# Example 4: Filtering and Pagination
print("="*60)
print("Example 4: Filtering and Pagination")
print("="*60)

class FilteredViewSet(ModelViewSet):
    """ViewSet with filtering and pagination."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer
    filter_fields = ['name', 'price']
    page_size = 2

    def filter_queryset(self, queryset: List[Dict], filters: Dict) -> List[Dict]:
        """Apply filters to queryset."""
        filtered = queryset

        if 'name' in filters:
            search = filters['name'].lower()
            filtered = [p for p in filtered if search in p['name'].lower()]
            print(f"  [FILTER] Name contains '{search}'")

        if 'min_price' in filters:
            min_price = float(filters['min_price'])
            filtered = [p for p in filtered if p['price'] >= min_price]
            print(f"  [FILTER] Min price: ${min_price}")

        if 'max_price' in filters:
            max_price = float(filters['max_price'])
            filtered = [p for p in filtered if p['price'] <= max_price]
            print(f"  [FILTER] Max price: ${max_price}")

        return filtered

    def paginate_queryset(self, queryset: List[Dict], page: int) -> tuple:
        """Paginate queryset."""
        start = (page - 1) * self.page_size
        end = start + self.page_size
        total_pages = (len(queryset) + self.page_size - 1) // self.page_size

        print(f"  [PAGINATION] Page {page}/{total_pages} (page_size={self.page_size})")

        return queryset[start:end], {
            'page': page,
            'page_size': self.page_size,
            'total': len(queryset),
            'total_pages': total_pages
        }

    def list(self, request: Dict) -> Dict:
        """List with filtering and pagination."""
        queryset = self.get_queryset()

        # Apply filters
        filters = request.get('query_params', {})
        queryset = self.filter_queryset(queryset, filters)

        # Apply pagination
        page = int(filters.get('page', 1))
        paginated_data, pagination_info = self.paginate_queryset(queryset, page)

        return {
            'status': 200,
            'data': paginated_data,
            'pagination': pagination_info
        }

filtered_viewset = FilteredViewSet()

print("\\nFiltered list with pagination:")
response = filtered_viewset.dispatch({
    'method': 'GET',
    'query_params': {'name': 'o', 'page': '1'}
}, 'list')
print(f"  Results on page 1: {len(response['data'])} items")

print("\\nPage 2:")
response = filtered_viewset.dispatch({
    'method': 'GET',
    'query_params': {'page': '2'}
}, 'list')
print(f"  Results on page 2: {len(response['data'])} items")
print()

# Example 5: Permissions
print("="*60)
print("Example 5: Permissions")
print("="*60)

class Permission:
    """Base permission class."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check if request has permission."""
        return True

    def has_object_permission(self, request: Dict, view, obj: Dict) -> bool:
        """Check if request has permission for object."""
        return True

class IsAuthenticated(Permission):
    """Require authentication."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check authentication."""
        has_auth = 'user' in request
        if not has_auth:
            print(f"  [PERMISSION DENIED] User not authenticated")
        else:
            print(f"  [PERMISSION] User authenticated: {request['user']['username']}")
        return has_auth

class IsAdminUser(Permission):
    """Require admin role."""

    def has_permission(self, request: Dict, view) -> bool:
        """Check admin role."""
        user = request.get('user', {})
        is_admin = user.get('role') == 'admin'

        if not is_admin:
            print(f"  [PERMISSION DENIED] User is not admin")
        else:
            print(f"  [PERMISSION] Admin user: {user['username']}")

        return is_admin

class PermissionedViewSet(ModelViewSet):
    """ViewSet with permission checks."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer
    permission_classes = []

    def check_permissions(self, request: Dict) -> Optional[Dict]:
        """Check all permission classes."""
        for permission_class in self.permission_classes:
            permission = permission_class()
            if not permission.has_permission(request, self):
                return {'status': 403, 'error': 'Permission denied'}
        return None

    def dispatch(self, request: Dict, action: str, **kwargs) -> Dict:
        """Dispatch with permission check."""
        # Check permissions
        permission_error = self.check_permissions(request)
        if permission_error:
            return permission_error

        return super().dispatch(request, action, **kwargs)

class ProductAdminViewSet(PermissionedViewSet):
    """Product ViewSet requiring admin."""

    permission_classes = [IsAuthenticated, IsAdminUser]

admin_viewset = ProductAdminViewSet()

# Test without auth
print("\\nAttempt without authentication:")
response = admin_viewset.dispatch({'method': 'GET'}, 'list')
print(f"  Status: {response['status']}")

# Test with auth but not admin
print("\\nAttempt as regular user:")
response = admin_viewset.dispatch({
    'method': 'GET',
    'user': {'username': 'john', 'role': 'user'}
}, 'list')
print(f"  Status: {response['status']}")

# Test as admin
print("\\nAttempt as admin:")
response = admin_viewset.dispatch({
    'method': 'GET',
    'user': {'username': 'admin', 'role': 'admin'}
}, 'list')
print(f"  Status: {response['status']}")
print()

# Example 6: Nested Resources
print("="*60)
print("Example 6: Nested Resources")
print("="*60)

REVIEWS = [
    {'id': 1, 'product_id': 1, 'rating': 5, 'comment': 'Great laptop!'},
    {'id': 2, 'product_id': 1, 'rating': 4, 'comment': 'Good value'},
    {'id': 3, 'product_id': 2, 'rating': 5, 'comment': 'Perfect mouse'},
]

class NestedViewSet(ModelViewSet):
    """ViewSet for nested resources."""

    parent_field = None

    def get_queryset(self) -> List[Dict]:
        """Get filtered queryset for parent."""
        queryset = super().get_queryset()
        parent_id = self.request.get('parent_id')

        if parent_id and self.parent_field:
            queryset = [item for item in queryset if item.get(self.parent_field) == parent_id]
            print(f"  [NESTED] Filtering by {self.parent_field}={parent_id}")

        return queryset

class ReviewViewSet(NestedViewSet):
    """Review ViewSet nested under products."""

    queryset = REVIEWS
    parent_field = 'product_id'

review_viewset = ReviewViewSet()

# Get reviews for product 1
print("\\nGetting reviews for product 1:")
response = review_viewset.dispatch({
    'method': 'GET',
    'parent_id': 1
}, 'list')
print(f"  Found {len(response['data'])} reviews")

# Create review for product
print("\\nCreating review for product 2:")
response = review_viewset.dispatch({
    'method': 'POST',
    'parent_id': 2,
    'data': {'product_id': 2, 'rating': 4, 'comment': 'Nice'}
}, 'create')
print()

# Example 7: Bulk Operations
print("="*60)
print("Example 7: Bulk Operations")
print("="*60)

class BulkViewSet(ModelViewSet):
    """ViewSet with bulk operations."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer

    def bulk_create(self, request: Dict) -> Dict:
        """Create multiple objects."""
        items = request.get('data', [])
        created = []

        for item_data in items:
            serializer = self.get_serializer(data=item_data)
            if serializer.is_valid():
                obj = serializer.save()
                created.append(obj)

        print(f"  [BULK CREATE] Created {len(created)} items")
        return {'status': 201, 'data': created, 'count': len(created)}

    def bulk_update(self, request: Dict) -> Dict:
        """Update multiple objects."""
        updates = request.get('data', [])
        updated = []

        for update_data in updates:
            obj = self.get_object(update_data['id'])
            if obj:
                serializer = self.get_serializer(data=update_data, instance=obj)
                if serializer.is_valid():
                    updated_obj = serializer.save()
                    updated.append(updated_obj)

        print(f"  [BULK UPDATE] Updated {len(updated)} items")
        return {'status': 200, 'data': updated, 'count': len(updated)}

    def bulk_delete(self, request: Dict) -> Dict:
        """Delete multiple objects."""
        ids = request.get('data', {}).get('ids', [])
        deleted_count = 0

        for pk in ids:
            obj = self.get_object(pk)
            if obj:
                PRODUCTS.remove(obj)
                deleted_count += 1

        print(f"  [BULK DELETE] Deleted {deleted_count} items")
        return {'status': 200, 'message': f'Deleted {deleted_count} items'}

bulk_viewset = BulkViewSet()

print("\\nBulk creating products:")
response = bulk_viewset.dispatch({
    'method': 'POST',
    'data': [
        {'name': 'Webcam', 'price': 89.99, 'stock': 25},
        {'name': 'Headset', 'price': 59.99, 'stock': 40}
    ]
}, 'bulk_create')

print(f"\\nTotal products now: {len(PRODUCTS)}")
print()

# Example 8: ViewSet Router
print("="*60)
print("Example 8: ViewSet Router")
print("="*60)

class Router:
    """Simple router for ViewSets."""

    def __init__(self):
        self.routes = {}

    def register(self, prefix: str, viewset_class, basename: str = None):
        """Register a ViewSet."""
        self.routes[prefix] = {
            'viewset': viewset_class,
            'basename': basename or prefix
        }
        print(f"  [ROUTER] Registered: {prefix} -> {viewset_class.__name__}")

    def resolve(self, path: str, method: str) -> tuple:
        """Resolve path to viewset and action."""
        parts = path.strip('/').split('/')
        prefix = parts[0]

        if prefix not in self.routes:
            return None, None, {}

        viewset_class = self.routes[prefix]['viewset']
        viewset = viewset_class()

        # Determine action based on path and method
        if len(parts) == 1:
            # /products/
            action = 'list' if method == 'GET' else 'create'
            kwargs = {}
        else:
            # /products/1/
            pk = int(parts[1])
            action = {
                'GET': 'retrieve',
                'PUT': 'update',
                'DELETE': 'destroy'
            }.get(method, 'list')
            kwargs = {'pk': pk}

        return viewset, action, kwargs

router = Router()

print("\\nRegistering ViewSets:")
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

# Test routing
print("\\nResolving routes:")
viewset, action, kwargs = router.resolve('/products/', 'GET')
print(f"  /products/ GET -> {viewset.__class__.__name__}.{action}()")

viewset, action, kwargs = router.resolve('/products/1/', 'GET')
print(f"  /products/1/ GET -> {viewset.__class__.__name__}.{action}(pk={kwargs.get('pk')})")
print()

# Example 9: ViewSet Mixins
print("="*60)
print("Example 9: ViewSet Mixins")
print("="*60)

class ListModelMixin:
    """Mixin for list action."""

    def list(self, request: Dict) -> Dict:
        """List objects."""
        queryset = self.get_queryset()
        print(f"  [ListMixin] Listing {len(queryset)} items")
        return {'status': 200, 'data': queryset}

class CreateModelMixin:
    """Mixin for create action."""

    def create(self, request: Dict) -> Dict:
        """Create object."""
        serializer = self.get_serializer(data=request.get('data', {}))
        if serializer.is_valid():
            obj = serializer.save()
            print(f"  [CreateMixin] Created item")
            return {'status': 201, 'data': obj}
        return {'status': 400, 'errors': serializer.errors}

class ReadOnlyViewSet(ListModelMixin, ViewSet):
    """Read-only ViewSet using mixins."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, data=None, instance=None):
        return self.serializer_class(data=data, instance=instance)

readonly_viewset = ReadOnlyViewSet()

print("\\nTesting read-only ViewSet:")
response = readonly_viewset.dispatch({'method': 'GET'}, 'list')
print(f"  Can list: Yes ({len(response['data'])} items)")

response = readonly_viewset.dispatch({'method': 'POST', 'data': {}}, 'create')
print(f"  Can create: {response['status'] != 405}")
print()

# Example 10: Complete ViewSet Example
print("="*60)
print("Example 10: Complete ViewSet Example")
print("="*60)

class CompleteProductViewSet(ModelViewSet):
    """Complete ViewSet with all features."""

    queryset = PRODUCTS
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = ['name', 'price']
    page_size = 5

    def get_queryset(self) -> List[Dict]:
        """Get queryset with filtering."""
        queryset = super().get_queryset()
        filters = self.request.get('query_params', {})

        if 'search' in filters:
            search = filters['search'].lower()
            queryset = [p for p in queryset if search in p['name'].lower()]

        return queryset

    def featured(self, request: Dict) -> Dict:
        """Custom action: Get featured products."""
        # In real app, filter by featured flag
        featured_products = self.get_queryset()[:3]
        print(f"  [CUSTOM] Featured products: {len(featured_products)}")
        return {'status': 200, 'data': featured_products}

    def statistics(self, request: Dict) -> Dict:
        """Custom action: Get product statistics."""
        queryset = self.get_queryset()
        stats = {
            'total_products': len(queryset),
            'total_stock': sum(p['stock'] for p in queryset),
            'avg_price': sum(p['price'] for p in queryset) / len(queryset) if queryset else 0,
            'min_price': min(p['price'] for p in queryset) if queryset else 0,
            'max_price': max(p['price'] for p in queryset) if queryset else 0
        }

        print(f"  [STATISTICS] Generated stats for {stats['total_products']} products")
        return {'status': 200, 'data': stats}

complete_viewset = CompleteProductViewSet()

# Test complete ViewSet
print("\\nTesting complete ViewSet:")
request = {'method': 'GET', 'user': {'username': 'alice', 'role': 'user'}}

print("\\nStandard list:")
complete_viewset.dispatch(request, 'list')

print("\\nFeatured products:")
complete_viewset.dispatch(request, 'featured')

print("\\nProduct statistics:")
response = complete_viewset.dispatch(request, 'statistics')
print(f"  Stats: {response['data']}")

print("\\n" + "="*60)
print("All Django REST Framework ViewSet examples completed!")
print("="*60)
'''

print(f"Upgraded Lesson 756: Django REST Framework ViewSet ({len(lesson_756['fullSolution']):,} chars)")

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

print("\\n" + "="*70)
print("BATCH 23 COMPLETE: Django Advanced Topics")
print("="*70)
print(f"\\nUpgraded: Lesson 765 - Custom Middleware ({len(lesson_765['fullSolution']):,} chars)")
print(f"Upgraded: Lesson 754 - Class-Based Views ({len(lesson_754['fullSolution']):,} chars)")
print(f"Upgraded: Lesson 756 - REST Framework ViewSet ({len(lesson_756['fullSolution']):,} chars)")
print("="*70)
