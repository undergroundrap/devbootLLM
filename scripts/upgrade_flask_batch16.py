#!/usr/bin/env python3
"""
Upgrade Flask lessons to comprehensive simulations (13,000-17,000+ chars)
Batch 16: Flask Custom Error Handlers, Deployment, and Project Planning
"""

import json
import sys
from pathlib import Path

def upgrade_lessons():
    lessons_file = Path("c:/devbootLLM-app/public/lessons-python.json")

    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Lesson 743: Flask Custom Error Handlers
    lesson_743 = next(l for l in lessons if l['id'] == 743)
    lesson_743['fullSolution'] = '''# Flask Custom Error Handlers - Complete Simulation
# In production: pip install flask
# This lesson simulates Flask error handling with custom error pages and handlers

import json
import traceback
from typing import Any, Callable, Dict, List, Optional, Tuple
from dataclasses import dataclass
from functools import wraps
from datetime import datetime

@dataclass
class Response:
    """HTTP Response."""
    body: str
    status_code: int
    headers: Dict[str, str]
    content_type: str = "text/html"

    def __repr__(self):
        return f"Response({self.status_code}, {len(self.body)} bytes)"

class HTTPException(Exception):
    """Base HTTP exception."""

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class NotFound(HTTPException):
    """404 Not Found."""
    def __init__(self, message: str = "Not Found"):
        super().__init__(message, 404)

class BadRequest(HTTPException):
    """400 Bad Request."""
    def __init__(self, message: str = "Bad Request"):
        super().__init__(message, 400)

class Unauthorized(HTTPException):
    """401 Unauthorized."""
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, 401)

class Forbidden(HTTPException):
    """403 Forbidden."""
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, 403)

class InternalServerError(HTTPException):
    """500 Internal Server Error."""
    def __init__(self, message: str = "Internal Server Error"):
        super().__init__(message, 500)

class Flask:
    """
    Flask application with comprehensive error handling.

    Features:
    - Custom error handlers
    - Error pages
    - Error logging
    - Exception handling
    """

    def __init__(self, name: str):
        self.name = name
        self.routes: Dict[str, Callable] = {}
        self.error_handlers: Dict[int, Callable] = {}
        self.exception_handlers: Dict[type, Callable] = {}
        self.error_logs: List[Dict] = []

        # Register default error handlers
        self._register_default_handlers()

    def route(self, path: str):
        """Route decorator."""
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator

    def errorhandler(self, error_code_or_exception):
        """
        Register custom error handler.

        Usage:
        @app.errorhandler(404)
        def not_found(error):
            return "Custom 404 page", 404

        @app.errorhandler(ValueError)
        def handle_value_error(error):
            return "Invalid value", 400
        """
        def decorator(func: Callable):
            if isinstance(error_code_or_exception, int):
                self.error_handlers[error_code_or_exception] = func
            else:
                self.exception_handlers[error_code_or_exception] = func
            return func
        return decorator

    def _register_default_handlers(self):
        """Register default error handlers."""
        @self.errorhandler(404)
        def default_404(error):
            return self._render_error_page(404, "Page Not Found", str(error))

        @self.errorhandler(500)
        def default_500(error):
            return self._render_error_page(500, "Internal Server Error", "An error occurred")

    def _render_error_page(self, code: int, title: str, message: str) -> Tuple[str, int]:
        """Render default error page."""
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{code} - {title}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        .error-box {{
            border: 2px solid #d32f2f;
            padding: 20px;
            border-radius: 8px;
            background: #ffebee;
        }}
        h1 {{ color: #d32f2f; }}
    </style>
</head>
<body>
    <div class="error-box">
        <h1>{code} - {title}</h1>
        <p>{message}</p>
    </div>
</body>
</html>
        """
        return html.strip(), code

    def handle_request(self, path: str, **kwargs) -> Response:
        """
        Handle HTTP request with error handling.

        Error handling flow:
        1. Try to execute route
        2. Catch HTTP exceptions (404, 500, etc.)
        3. Catch Python exceptions (ValueError, etc.)
        4. Call appropriate error handler
        5. Log error
        """
        try:
            # Check if route exists
            if path not in self.routes:
                raise NotFound(f"The requested URL {path} was not found")

            # Execute route
            handler = self.routes[path]
            result = handler(**kwargs)

            # Handle response
            if isinstance(result, tuple):
                body, status_code = result
                return Response(body, status_code, {})
            else:
                return Response(str(result), 200, {})

        except HTTPException as e:
            # Handle HTTP exceptions (404, 500, etc.)
            return self._handle_http_exception(e)

        except Exception as e:
            # Handle Python exceptions
            return self._handle_python_exception(e)

    def _handle_http_exception(self, exception: HTTPException) -> Response:
        """Handle HTTP exception."""
        # Log error
        self._log_error(exception.status_code, str(exception), type(exception).__name__)

        # Get custom handler if registered
        if exception.status_code in self.error_handlers:
            handler = self.error_handlers[exception.status_code]
            body, status_code = handler(exception)
            return Response(body, status_code, {})

        # Default error response
        body, status_code = self._render_error_page(
            exception.status_code,
            type(exception).__name__,
            exception.message
        )
        return Response(body, status_code, {})

    def _handle_python_exception(self, exception: Exception) -> Response:
        """Handle Python exception."""
        # Log error with traceback
        self._log_error(500, str(exception), type(exception).__name__, traceback.format_exc())

        # Check for custom exception handler
        exception_type = type(exception)
        if exception_type in self.exception_handlers:
            handler = self.exception_handlers[exception_type]
            result = handler(exception)

            if isinstance(result, tuple):
                body, status_code = result
                return Response(body, status_code, {})
            else:
                return Response(str(result), 500, {})

        # Default 500 error
        handler = self.error_handlers.get(500)
        if handler:
            body, status_code = handler(exception)
            return Response(body, status_code, {})

        # Fallback
        body, status_code = self._render_error_page(500, "Internal Server Error", str(exception))
        return Response(body, status_code, {})

    def _log_error(self, status_code: int, message: str, error_type: str, traceback_str: str = None):
        """Log error."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "status_code": status_code,
            "error_type": error_type,
            "message": message,
            "traceback": traceback_str
        }
        self.error_logs.append(log_entry)

        print(f"[ERROR] {status_code} - {error_type}: {message}")

    def get_error_logs(self, limit: int = 10) -> List[Dict]:
        """Get recent error logs."""
        return self.error_logs[-limit:]

# Example 1: Custom 404 Handler
print("Example 1: Custom 404 Handler")
print("=" * 60)

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Home Page</h1>", 200

@app.route("/about")
def about():
    return "<h1>About Page</h1>", 200

# Custom 404 handler
@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    html = """
    <html>
        <body style='text-align: center; padding: 50px;'>
            <h1>🔍 Page Not Found</h1>
            <p>Sorry, we couldn't find what you're looking for.</p>
            <a href='/'>Go Home</a>
        </body>
    </html>
    """
    return html, 404

print("Requesting valid page:")
response = app.handle_request("/")
print(f"  Status: {response.status_code}")
print(f"  Content preview: {response.body[:50]}...")
print()

print("Requesting invalid page:")
response = app.handle_request("/nonexistent")
print(f"  Status: {response.status_code}")
print(f"  Content preview: {response.body[:100]}...")
print()

# Example 2: Multiple Custom Error Handlers
print("Example 2: Multiple Custom Error Handlers")
print("=" * 60)

app2 = Flask(__name__)

@app2.route("/users/<int:user_id>")
def get_user(user_id: int):
    """Get user by ID."""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}

    if user_id not in users:
        raise NotFound(f"User {user_id} not found")

    return f"<h1>User: {users[user_id]}</h1>", 200

@app2.route("/admin")
def admin():
    """Admin page (requires auth)."""
    is_admin = False  # Simulate auth check

    if not is_admin:
        raise Forbidden("You don't have permission to access this page")

    return "<h1>Admin Dashboard</h1>", 200

# Custom 403 handler
@app2.errorhandler(403)
def forbidden(error):
    """Custom 403 page."""
    return """
    <html>
        <body>
            <h1>🚫 Access Denied</h1>
            <p>You need admin privileges.</p>
        </body>
    </html>
    """, 403

# Custom 404 handler
@app2.errorhandler(404)
def not_found(error):
    """Custom 404 page."""
    return f"<h1>404</h1><p>{error}</p>", 404

print("Valid user request:")
response = app2.handle_request("/users/1", user_id=1)
print(f"  Status: {response.status_code}")
print()

print("Invalid user request:")
response = app2.handle_request("/users/999", user_id=999)
print(f"  Status: {response.status_code}")
print()

print("Unauthorized admin request:")
response = app2.handle_request("/admin")
print(f"  Status: {response.status_code}")
print()

# Example 3: Exception Handlers
print("Example 3: Exception Handlers (Python Exceptions)")
print("=" * 60)

app3 = Flask(__name__)

@app3.route("/divide")
def divide():
    """Division endpoint."""
    a = 10
    b = 0  # Will cause ZeroDivisionError
    return str(a / b), 200

@app3.route("/process")
def process():
    """Process endpoint."""
    data = {"age": "invalid"}
    age = int(data["age"])  # Will cause ValueError
    return f"Age: {age}", 200

# Handle ZeroDivisionError
@app3.errorhandler(ZeroDivisionError)
def handle_zero_division(error):
    """Handle division by zero."""
    return """
    <html>
        <body>
            <h1>⚠️ Math Error</h1>
            <p>Cannot divide by zero!</p>
        </body>
    </html>
    """, 400

# Handle ValueError
@app3.errorhandler(ValueError)
def handle_value_error(error):
    """Handle value error."""
    return f"<h1>Invalid Value</h1><p>{error}</p>", 400

print("Division by zero:")
response = app3.handle_request("/divide")
print(f"  Status: {response.status_code}")
print(f"  Error logged: {len(app3.error_logs) > 0}")
print()

print("Invalid value:")
response = app3.handle_request("/process")
print(f"  Status: {response.status_code}")
print()

# Example 4: JSON Error Responses (API)
print("Example 4: JSON Error Responses (API)")
print("=" * 60)

app4 = Flask(__name__)

@app4.route("/api/users/<int:user_id>")
def api_get_user(user_id: int):
    """API endpoint."""
    users = {1: {"name": "Alice", "email": "alice@example.com"}}

    if user_id not in users:
        raise NotFound(f"User {user_id} not found")

    return json.dumps(users[user_id]), 200

# JSON error handler for API
@app4.errorhandler(404)
def api_not_found(error):
    """JSON 404 response."""
    error_response = {
        "error": "Not Found",
        "message": str(error),
        "status_code": 404
    }
    return json.dumps(error_response), 404

@app4.errorhandler(500)
def api_internal_error(error):
    """JSON 500 response."""
    error_response = {
        "error": "Internal Server Error",
        "message": "An unexpected error occurred",
        "status_code": 500
    }
    return json.dumps(error_response), 500

print("API request (not found):")
response = app4.handle_request("/api/users/999", user_id=999)
print(f"  Status: {response.status_code}")
print(f"  Response: {response.body}")
print()

# Example 5: Error Logging and Monitoring
print("Example 5: Error Logging and Monitoring")
print("=" * 60)

app5 = Flask(__name__)

@app5.route("/test1")
def test1():
    raise ValueError("Test error 1")

@app5.route("/test2")
def test2():
    raise NotFound("Test error 2")

@app5.route("/test3")
def test3():
    raise InternalServerError("Test error 3")

# Generic error handler
@app5.errorhandler(Exception)
def handle_all_errors(error):
    """Catch-all error handler."""
    if isinstance(error, HTTPException):
        status_code = error.status_code
    else:
        status_code = 500

    return f"<h1>Error {status_code}</h1><p>{error}</p>", status_code

print("Generating errors for logging:")
app5.handle_request("/test1")
app5.handle_request("/test2")
app5.handle_request("/test3")
print()

print("Error logs:")
for i, log in enumerate(app5.get_error_logs(), 1):
    print(f"  {i}. [{log['timestamp']}] {log['status_code']} - {log['error_type']}")
    print(f"     Message: {log['message']}")
print()

# Example 6: Custom Error Page with Context
print("Example 6: Custom Error Page with Context")
print("=" * 60)

app6 = Flask(__name__)

@app6.route("/product/<int:product_id>")
def get_product(product_id: int):
    """Get product."""
    if product_id > 100:
        raise NotFound(f"Product {product_id} not found")
    return f"<h1>Product {product_id}</h1>", 200

@app6.errorhandler(404)
def enhanced_404(error):
    """Enhanced 404 with suggestions."""
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial; margin: 40px; }}
            .error {{ color: #d32f2f; }}
            .suggestions {{
                background: #f5f5f5;
                padding: 15px;
                border-radius: 5px;
            }}
        </style>
    </head>
    <body>
        <h1 class='error'>404 - Page Not Found</h1>
        <p>{error}</p>
        <div class='suggestions'>
            <h3>Try these instead:</h3>
            <ul>
                <li><a href='/'>Home</a></li>
                <li><a href='/product/1'>Product 1</a></li>
                <li><a href='/product/2'>Product 2</a></li>
            </ul>
        </div>
    </body>
    </html>
    """
    return html, 404

print("Request with enhanced 404 page:")
response = app6.handle_request("/product/999", product_id=999)
print(f"  Status: {response.status_code}")
print(f"  Contains suggestions: {'Try these instead' in response.body}")
print()

print("=" * 60)
print("ERROR HANDLING BEST PRACTICES")
print("=" * 60)
print("""
CUSTOM ERROR HANDLERS:

1. HTTP STATUS CODES:
   400: Bad Request (invalid input)
   401: Unauthorized (authentication required)
   403: Forbidden (insufficient permissions)
   404: Not Found (resource doesn't exist)
   500: Internal Server Error (unexpected error)
   503: Service Unavailable (temporary downtime)

2. HANDLER REGISTRATION:
   @app.errorhandler(404)
   def not_found(error):
       return render_template('404.html'), 404

   @app.errorhandler(ValueError)
   def handle_value_error(error):
       return jsonify(error=str(error)), 400

ERROR PAGE DESIGN:

  User-friendly:
  - Clear error message
  - Helpful suggestions
  - Navigation links
  - Consistent branding

  Developer-friendly:
  - Error ID for tracking
  - Timestamp
  - Request details (in dev mode)
  - Stack trace (in dev mode)

API ERROR RESPONSES:

  JSON format:
  {
    "error": "Not Found",
    "message": "User 123 not found",
    "status_code": 404,
    "error_id": "abc123",
    "timestamp": "2024-01-15T10:30:00Z"
  }

  Consistency:
  - Same structure for all errors
  - Include error details
  - Provide actionable message
  - Add request ID for debugging

ERROR LOGGING:

  What to log:
  - Timestamp
  - Error type
  - Error message
  - Stack trace
  - Request details
  - User context
  - Request ID

  Logging levels:
  - DEBUG: Detailed diagnostic
  - INFO: General information
  - WARNING: Warning messages
  - ERROR: Error messages
  - CRITICAL: Critical errors

EXCEPTION HANDLING:

  Specific exceptions:
  @app.errorhandler(ValueError)
  @app.errorhandler(KeyError)
  @app.errorhandler(SQLAlchemyError)

  Generic catch-all:
  @app.errorhandler(Exception)
  def handle_exception(e):
      # Log unexpected errors
      app.logger.error(f"Unhandled: {e}")
      return "Internal error", 500

SECURITY CONSIDERATIONS:

  Production:
  ✓ Generic error messages
  ✓ Hide stack traces
  ✓ Log detailed errors server-side
  ✓ Use error IDs for tracking
  ✗ Expose sensitive data
  ✗ Show file paths
  ✗ Reveal database structure

  Development:
  ✓ Detailed error pages
  ✓ Stack traces
  ✓ Variable inspection
  ✓ Debug toolbar

MONITORING & ALERTING:

  Metrics:
  - Error rate (errors/minute)
  - Error types distribution
  - Response time on errors
  - User impact

  Alerts:
  - 5xx error spike
  - High error rate
  - New error types
  - Critical errors

TESTING ERROR HANDLERS:

  def test_404():
      response = client.get('/nonexistent')
      assert response.status_code == 404
      assert 'Not Found' in response.data

  def test_500():
      response = client.get('/error')
      assert response.status_code == 500

Production note: Real Flask provides:
  - register_error_handler() method
  - abort() function for raising HTTP errors
  - Integration with logging
  - Werkzeug exception classes
  - Blueprint error handlers
  - Error handler inheritance
  - Request context in handlers
  - Automatic exception catching
""")
'''

    # Save changes
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2)

    print("\n" + "=" * 70)
    print("BATCH 16 PARTIAL: Flask Custom Error Handlers")
    print("=" * 70)
    print("\nUpgraded lessons:")
    print(f"  - Lesson 743: Flask Custom Error Handlers")
    print("\nLesson upgraded to 13,000-17,000+ characters")
    print("Zero package installation required!")
    print("=" * 70)

if __name__ == "__main__":
    upgrade_lessons()
