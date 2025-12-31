import json

# Read lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lesson to upgrade
lesson_518 = next(l for l in lessons if l['id'] == 518)  # Django Function-Based Views

# ============================================================================
# LESSON 518: Django Function-Based Views
# ============================================================================

lesson_518['fullSolution'] = '''"""
Django Function-Based Views - Comprehensive Guide
=================================================

This lesson covers comprehensive Django function-based views (FBVs) including
request/response handling, form processing, GET/POST patterns, view decorators,
file uploads, pagination, AJAX handling, and advanced view patterns.

**Zero Package Installation Required**

Learning Objectives:
- Master Django function-based view patterns
- Handle HTTP requests and responses
- Implement form validation and processing
- Use view decorators for authentication and permissions
- Handle file uploads and downloads
- Implement pagination and filtering
- Process AJAX requests and return JSON
- Implement CRUD operations with FBVs
- Handle errors and custom error pages
- Optimize view performance
"""

import json
import time
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime, timedelta
from functools import wraps

# ============================================================================
# Example 1: HTTP Request/Response Simulation
# ============================================================================

class HttpRequest:
    """
    Simulates Django HttpRequest object.
    """

    def __init__(self, method: str = 'GET', path: str = '/', data: Dict = None):
        self.method = method
        self.path = path
        self.GET = data if method == 'GET' else {}
        self.POST = data if method == 'POST' else {}
        self.FILES = {}
        self.session = {}
        self.user = None
        self.META = {
            'REMOTE_ADDR': '127.0.0.1',
            'HTTP_USER_AGENT': 'Mozilla/5.0',
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
        }
        self.COOKIES = {}

class HttpResponse:
    """
    Simulates Django HttpResponse object.
    """

    def __init__(self, content: str = '', status: int = 200, content_type: str = 'text/html'):
        self.content = content
        self.status_code = status
        self.content_type = content_type
        self.headers = {'Content-Type': content_type}

    def __repr__(self):
        return f"<HttpResponse status_code={self.status_code}, content_type='{self.content_type}'>"

class JsonResponse(HttpResponse):
    """
    Simulates Django JsonResponse object.
    """

    def __init__(self, data: Dict, status: int = 200):
        content = json.dumps(data, indent=2)
        super().__init__(content, status, 'application/json')
        self.data = data

def example_request_response():
    """
    Demonstrates basic request/response handling.
    """
    print(f"{'='*60}")
    print("Example 1: HTTP Request/Response Handling")
    print(f"{'='*60}")

    # Create sample request
    request = HttpRequest('GET', '/products/', {'category': 'electronics', 'page': '1'})

    print("\\nIncoming Request:")
    print(f"  Method: {request.method}")
    print(f"  Path: {request.path}")
    print(f"  GET params: {request.GET}")
    print(f"  User Agent: {request.META['HTTP_USER_AGENT']}")
    print(f"  Remote IP: {request.META['REMOTE_ADDR']}")

    # Simple view function
    def product_list_view(request):
        category = request.GET.get('category', 'all')
        page = int(request.GET.get('page', 1))

        html = f"""
        <html>
          <body>
            <h1>Product List</h1>
            <p>Category: {category}</p>
            <p>Page: {page}</p>
          </body>
        </html>
        """
        return HttpResponse(html)

    # Process request
    response = product_list_view(request)

    print("\\nGenerated Response:")
    print(f"  Status: {response.status_code}")
    print(f"  Content-Type: {response.content_type}")
    print(f"  Content preview: {response.content[:100]}...")

# ============================================================================
# Example 2: Form Processing (GET/POST Pattern)
# ============================================================================

class Form:
    """
    Simulates Django Form class.
    """

    def __init__(self, data: Dict = None):
        self.data = data or {}
        self.errors = {}
        self.cleaned_data = {}

    def is_valid(self) -> bool:
        """Validate form data."""
        # Override in subclass
        return True

    def clean(self):
        """Clean and validate all fields."""
        return self.cleaned_data

class ContactForm(Form):
    """
    Example contact form.
    """

    def is_valid(self) -> bool:
        self.errors = {}
        self.cleaned_data = {}

        # Validate name
        name = self.data.get('name', '').strip()
        if not name:
            self.errors['name'] = 'Name is required'
        elif len(name) < 2:
            self.errors['name'] = 'Name must be at least 2 characters'
        else:
            self.cleaned_data['name'] = name

        # Validate email
        email = self.data.get('email', '').strip()
        if not email:
            self.errors['email'] = 'Email is required'
        elif '@' not in email:
            self.errors['email'] = 'Invalid email address'
        else:
            self.cleaned_data['email'] = email

        # Validate message
        message = self.data.get('message', '').strip()
        if not message:
            self.errors['message'] = 'Message is required'
        elif len(message) < 10:
            self.errors['message'] = 'Message must be at least 10 characters'
        else:
            self.cleaned_data['message'] = message

        return len(self.errors) == 0

def example_form_processing():
    """
    Demonstrates form processing with GET/POST pattern.
    """
    print(f"\\n{'='*60}")
    print("Example 2: Form Processing (GET/POST Pattern)")
    print(f"{'='*60}")

    def contact_view(request):
        """Contact form view."""
        if request.method == 'POST':
            print("\\nProcessing POST request (form submission)...")
            form = ContactForm(request.POST)

            if form.is_valid():
                # Process the form data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                print(f"  Form is valid!")
                print(f"  Name: {name}")
                print(f"  Email: {email}")
                print(f"  Message: {message[:50]}...")

                # Simulate sending email or saving to database
                print("  Sending email...")
                time.sleep(0.1)
                print("  Email sent successfully!")

                return HttpResponse("<html><body><h1>Thank you! Message sent.</h1></body></html>")
            else:
                print(f"  Form is invalid!")
                print(f"  Errors: {form.errors}")
                return HttpResponse(f"<html><body><h1>Form Errors</h1><ul>{''.join([f'<li>{k}: {v}</li>' for k, v in form.errors.items()])}</ul></body></html>", status=400)
        else:
            print("\\nProcessing GET request (showing form)...")
            html = """
            <html>
              <body>
                <h1>Contact Us</h1>
                <form method="post">
                  <input type="text" name="name" placeholder="Name" required>
                  <input type="email" name="email" placeholder="Email" required>
                  <textarea name="message" placeholder="Message" required></textarea>
                  <button type="submit">Send</button>
                </form>
              </body>
            </html>
            """
            return HttpResponse(html)

    # Test GET request
    get_request = HttpRequest('GET', '/contact/')
    response = contact_view(get_request)
    print(f"  Response: {response.status_code} - Form displayed")

    # Test POST request with valid data
    post_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'This is a test message with enough characters.'
    }
    post_request = HttpRequest('POST', '/contact/', post_data)
    response = contact_view(post_request)
    print(f"  Response: {response.status_code}")

    # Test POST request with invalid data
    print("\\nTesting with invalid data...")
    invalid_data = {
        'name': 'J',
        'email': 'invalid',
        'message': 'short'
    }
    invalid_request = HttpRequest('POST', '/contact/', invalid_data)
    response = contact_view(invalid_request)
    print(f"  Response: {response.status_code}")

# ============================================================================
# Example 3: View Decorators (Authentication & Permissions)
# ============================================================================

class User:
    """
    Simulates Django User model.
    """

    def __init__(self, username: str, is_authenticated: bool = True, is_staff: bool = False):
        self.username = username
        self.is_authenticated = is_authenticated
        self.is_staff = is_staff
        self.is_superuser = False

def login_required(view_func: Callable) -> Callable:
    """
    Decorator to require user authentication.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user or not request.user.is_authenticated:
            return HttpResponse("<html><body><h1>401 Unauthorized</h1><p>Please login</p></body></html>", status=401)
        return view_func(request, *args, **kwargs)
    return wrapper

def staff_required(view_func: Callable) -> Callable:
    """
    Decorator to require staff status.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user or not request.user.is_staff:
            return HttpResponse("<html><body><h1>403 Forbidden</h1><p>Staff access required</p></body></html>", status=403)
        return view_func(request, *args, **kwargs)
    return wrapper

def require_http_methods(methods: List[str]) -> Callable:
    """
    Decorator to restrict allowed HTTP methods.
    """
    def decorator(view_func: Callable) -> Callable:
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponse(f"<html><body><h1>405 Method Not Allowed</h1><p>Allowed: {', '.join(methods)}</p></body></html>", status=405)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

def example_view_decorators():
    """
    Demonstrates view decorators for authentication and permissions.
    """
    print(f"\\n{'='*60}")
    print("Example 3: View Decorators (Auth & Permissions)")
    print(f"{'='*60}")

    @login_required
    def profile_view(request):
        return HttpResponse(f"<html><body><h1>Profile: {request.user.username}</h1></body></html>")

    @login_required
    @staff_required
    def admin_dashboard_view(request):
        return HttpResponse("<html><body><h1>Admin Dashboard</h1></body></html>")

    @require_http_methods(['POST'])
    def delete_item_view(request):
        return HttpResponse("<html><body><h1>Item deleted</h1></body></html>")

    # Test 1: Unauthenticated user
    print("\\nTest 1: Unauthenticated user accessing profile")
    request = HttpRequest('GET', '/profile/')
    request.user = None
    response = profile_view(request)
    print(f"  Response: {response.status_code} - {'PASS' if response.status_code == 401 else 'FAIL'}")

    # Test 2: Authenticated user
    print("\\nTest 2: Authenticated user accessing profile")
    request = HttpRequest('GET', '/profile/')
    request.user = User('john_doe', is_authenticated=True)
    response = profile_view(request)
    print(f"  Response: {response.status_code} - {'PASS' if response.status_code == 200 else 'FAIL'}")

    # Test 3: Non-staff user accessing admin
    print("\\nTest 3: Non-staff user accessing admin dashboard")
    request = HttpRequest('GET', '/admin/dashboard/')
    request.user = User('john_doe', is_authenticated=True, is_staff=False)
    response = admin_dashboard_view(request)
    print(f"  Response: {response.status_code} - {'PASS' if response.status_code == 403 else 'FAIL'}")

    # Test 4: Staff user accessing admin
    print("\\nTest 4: Staff user accessing admin dashboard")
    request = HttpRequest('GET', '/admin/dashboard/')
    request.user = User('admin', is_authenticated=True, is_staff=True)
    response = admin_dashboard_view(request)
    print(f"  Response: {response.status_code} - {'PASS' if response.status_code == 200 else 'FAIL'}")

    # Test 5: Wrong HTTP method
    print("\\nTest 5: GET request to POST-only view")
    request = HttpRequest('GET', '/delete/123/')
    response = delete_item_view(request)
    print(f"  Response: {response.status_code} - {'PASS' if response.status_code == 405 else 'FAIL'}")

# ============================================================================
# Example 4: File Upload Handling
# ============================================================================

class UploadedFile:
    """
    Simulates Django UploadedFile.
    """

    def __init__(self, name: str, content: bytes, content_type: str):
        self.name = name
        self.content = content
        self.content_type = content_type
        self.size = len(content)

    def read(self) -> bytes:
        return self.content

def example_file_upload():
    """
    Demonstrates file upload handling.
    """
    print(f"\\n{'='*60}")
    print("Example 4: File Upload Handling")
    print(f"{'='*60}")

    def upload_view(request):
        """Handle file upload."""
        if request.method == 'POST':
            print("\\nProcessing file upload...")

            if 'file' not in request.FILES:
                return HttpResponse("<html><body><h1>Error: No file uploaded</h1></body></html>", status=400)

            uploaded_file = request.FILES['file']

            # Validate file
            print(f"  File name: {uploaded_file.name}")
            print(f"  File size: {uploaded_file.size:,} bytes")
            print(f"  Content type: {uploaded_file.content_type}")

            # Check file size (max 5MB)
            max_size = 5 * 1024 * 1024  # 5MB
            if uploaded_file.size > max_size:
                print(f"  ERROR: File too large (max {max_size:,} bytes)")
                return HttpResponse("<html><body><h1>Error: File too large</h1></body></html>", status=400)

            # Check file type
            allowed_types = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']
            if uploaded_file.content_type not in allowed_types:
                print(f"  ERROR: Invalid file type")
                return HttpResponse("<html><body><h1>Error: Invalid file type</h1></body></html>", status=400)

            # Save file (simulated)
            file_path = f"/uploads/{datetime.now().strftime('%Y%m%d%H%M%S')}_{uploaded_file.name}"
            print(f"  Saving to: {file_path}")
            print(f"  SUCCESS: File uploaded")

            return HttpResponse(f"<html><body><h1>File uploaded: {uploaded_file.name}</h1></body></html>")
        else:
            html = """
            <html>
              <body>
                <h1>Upload File</h1>
                <form method="post" enctype="multipart/form-data">
                  <input type="file" name="file" required>
                  <button type="submit">Upload</button>
                </form>
              </body>
            </html>
            """
            return HttpResponse(html)

    # Test valid upload
    request = HttpRequest('POST', '/upload/')
    request.FILES['file'] = UploadedFile(
        'photo.jpg',
        b'fake_image_data' * 100,
        'image/jpeg'
    )
    response = upload_view(request)
    print(f"  Response: {response.status_code}")

    # Test invalid file type
    print("\\nTesting invalid file type...")
    request = HttpRequest('POST', '/upload/')
    request.FILES['file'] = UploadedFile(
        'script.exe',
        b'fake_exe_data',
        'application/x-msdownload'
    )
    response = upload_view(request)
    print(f"  Response: {response.status_code}")

# ============================================================================
# Example 5: Pagination Implementation
# ============================================================================

class Paginator:
    """
    Simulates Django Paginator.
    """

    def __init__(self, object_list: List, per_page: int):
        self.object_list = object_list
        self.per_page = per_page
        self.count = len(object_list)
        self.num_pages = (self.count + per_page - 1) // per_page

    def page(self, number: int):
        """Get specific page."""
        if number < 1 or number > self.num_pages:
            raise Exception(f"Page {number} does not exist")

        start = (number - 1) * self.per_page
        end = start + self.per_page
        return Page(self.object_list[start:end], number, self)

class Page:
    """
    Represents a single page of results.
    """

    def __init__(self, object_list: List, number: int, paginator: Paginator):
        self.object_list = object_list
        self.number = number
        self.paginator = paginator

    def has_previous(self) -> bool:
        return self.number > 1

    def has_next(self) -> bool:
        return self.number < self.paginator.num_pages

    def previous_page_number(self) -> int:
        return self.number - 1

    def next_page_number(self) -> int:
        return self.number + 1

def example_pagination():
    """
    Demonstrates pagination in views.
    """
    print(f"\\n{'='*60}")
    print("Example 5: Pagination Implementation")
    print(f"{'='*60}")

    # Sample data
    products = [{'id': i, 'name': f'Product {i}', 'price': 10 + i} for i in range(1, 51)]

    def product_list_view(request):
        """Product list with pagination."""
        page_number = int(request.GET.get('page', 1))
        per_page = int(request.GET.get('per_page', 10))

        print(f"\\nPagination request:")
        print(f"  Page: {page_number}")
        print(f"  Per page: {per_page}")

        paginator = Paginator(products, per_page)

        try:
            page = paginator.page(page_number)
            print(f"  Total items: {paginator.count}")
            print(f"  Total pages: {paginator.num_pages}")
            print(f"  Items on this page: {len(page.object_list)}")
            print(f"  Has previous: {page.has_previous()}")
            print(f"  Has next: {page.has_next()}")

            html = f"""
            <html>
              <body>
                <h1>Products (Page {page_number} of {paginator.num_pages})</h1>
                <ul>
                  {''.join([f"<li>{p['name']} - ${p['price']}</li>" for p in page.object_list])}
                </ul>
                <div>
                  {'<a href=\"?page=' + str(page.previous_page_number()) + '\">Previous</a>' if page.has_previous() else ''}
                  {'<a href=\"?page=' + str(page.next_page_number()) + '\">Next</a>' if page.has_next() else ''}
                </div>
              </body>
            </html>
            """
            return HttpResponse(html)
        except Exception as e:
            return HttpResponse(f"<html><body><h1>Error: {str(e)}</h1></body></html>", status=404)

    # Test pagination
    request = HttpRequest('GET', '/products/', {'page': '2', 'per_page': '10'})
    response = product_list_view(request)
    print(f"  Response: {response.status_code}")

# ============================================================================
# Example 6: AJAX and JSON Responses
# ============================================================================

def example_ajax_json():
    """
    Demonstrates AJAX request handling and JSON responses.
    """
    print(f"\\n{'='*60}")
    print("Example 6: AJAX and JSON Responses")
    print(f"{'='*60}")

    def api_search_view(request):
        """Search API endpoint."""
        query = request.GET.get('q', '')
        print(f"\\nSearch query: '{query}'")

        # Simulate database search
        all_items = [
            {'id': 1, 'name': 'Laptop', 'category': 'Electronics'},
            {'id': 2, 'name': 'Phone', 'category': 'Electronics'},
            {'id': 3, 'name': 'Desk', 'category': 'Furniture'},
            {'id': 4, 'name': 'Chair', 'category': 'Furniture'},
        ]

        results = [item for item in all_items if query.lower() in item['name'].lower()]

        print(f"  Found {len(results)} results")

        return JsonResponse({
            'query': query,
            'count': len(results),
            'results': results
        })

    @require_http_methods(['POST'])
    def api_create_item_view(request):
        """Create item API endpoint."""
        try:
            data = json.loads(request.POST.get('data', '{}'))
            print(f"\\nCreating item: {data}")

            # Validate data
            if 'name' not in data:
                return JsonResponse({'error': 'Name is required'}, status=400)

            # Simulate saving to database
            item = {
                'id': 123,
                'name': data['name'],
                'created_at': datetime.now().isoformat()
            }

            print(f"  Item created with ID: {item['id']}")

            return JsonResponse({
                'success': True,
                'item': item
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # Test search
    request = HttpRequest('GET', '/api/search/', {'q': 'lap'})
    response = api_search_view(request)
    print(f"  Response: {response.status_code}")
    print(f"  Data: {json.loads(response.content)}")

    # Test create
    request = HttpRequest('POST', '/api/items/', {'data': json.dumps({'name': 'New Item'})})
    response = api_create_item_view(request)
    print(f"  Response: {response.status_code}")
    print(f"  Data: {json.loads(response.content)}")

# ============================================================================
# Example 7: CRUD Operations with FBVs
# ============================================================================

class InMemoryDB:
    """
    Simple in-memory database for demonstration.
    """

    def __init__(self):
        self.items: Dict[int, Dict] = {}
        self.next_id = 1

    def create(self, data: Dict) -> Dict:
        item = {'id': self.next_id, **data}
        self.items[self.next_id] = item
        self.next_id += 1
        return item

    def get(self, item_id: int) -> Optional[Dict]:
        return self.items.get(item_id)

    def list(self) -> List[Dict]:
        return list(self.items.values())

    def update(self, item_id: int, data: Dict) -> Optional[Dict]:
        if item_id in self.items:
            self.items[item_id].update(data)
            return self.items[item_id]
        return None

    def delete(self, item_id: int) -> bool:
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

def example_crud_operations():
    """
    Demonstrates CRUD operations with function-based views.
    """
    print(f"\\n{'='*60}")
    print("Example 7: CRUD Operations with FBVs")
    print(f"{'='*60}")

    db = InMemoryDB()

    # Create view
    @require_http_methods(['POST'])
    def item_create_view(request):
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'created_at': datetime.now().isoformat()
        }
        item = db.create(data)
        print(f"\\nCreated item: ID={item['id']}, Title={item['title']}")
        return JsonResponse({'success': True, 'item': item}, status=201)

    # List view
    def item_list_view(request):
        items = db.list()
        print(f"\\nListing {len(items)} items")
        return JsonResponse({'items': items})

    # Detail view
    def item_detail_view(request, item_id: int):
        item = db.get(item_id)
        if item:
            print(f"\\nRetrieving item {item_id}")
            return JsonResponse({'item': item})
        print(f"\\nItem {item_id} not found")
        return JsonResponse({'error': 'Item not found'}, status=404)

    # Update view
    @require_http_methods(['POST'])
    def item_update_view(request, item_id: int):
        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'updated_at': datetime.now().isoformat()
        }
        item = db.update(item_id, data)
        if item:
            print(f"\\nUpdated item {item_id}")
            return JsonResponse({'success': True, 'item': item})
        print(f"\\nItem {item_id} not found")
        return JsonResponse({'error': 'Item not found'}, status=404)

    # Delete view
    @require_http_methods(['POST'])
    def item_delete_view(request, item_id: int):
        if db.delete(item_id):
            print(f"\\nDeleted item {item_id}")
            return JsonResponse({'success': True})
        print(f"\\nItem {item_id} not found")
        return JsonResponse({'error': 'Item not found'}, status=404)

    # Test CRUD operations
    # Create
    request = HttpRequest('POST', '/items/', {'title': 'Test Item', 'description': 'Test description'})
    response = item_create_view(request)
    created_item = json.loads(response.content)['item']

    # List
    request = HttpRequest('GET', '/items/')
    response = item_list_view(request)

    # Detail
    request = HttpRequest('GET', f'/items/{created_item["id"]}/')
    response = item_detail_view(request, created_item['id'])

    # Update
    request = HttpRequest('POST', f'/items/{created_item["id"]}/', {'title': 'Updated Title', 'description': 'Updated description'})
    response = item_update_view(request, created_item['id'])

    # Delete
    request = HttpRequest('POST', f'/items/{created_item["id"]}/delete/')
    response = item_delete_view(request, created_item['id'])

    print("\\n  All CRUD operations completed successfully!")

# ============================================================================
# Example 8: Error Handling and Custom Error Pages
# ============================================================================

def example_error_handling():
    """
    Demonstrates error handling in views.
    """
    print(f"\\n{'='*60}")
    print("Example 8: Error Handling and Custom Error Pages")
    print(f"{'='*60}")

    def safe_view(request):
        """View with comprehensive error handling."""
        try:
            item_id = request.GET.get('id')

            if not item_id:
                print("\\n  ERROR: Missing required parameter 'id'")
                return HttpResponse("<html><body><h1>400 Bad Request</h1><p>Missing 'id' parameter</p></body></html>", status=400)

            if not item_id.isdigit():
                print("\\n  ERROR: Invalid parameter type")
                return HttpResponse("<html><body><h1>400 Bad Request</h1><p>Invalid 'id' format</p></body></html>", status=400)

            item_id = int(item_id)

            # Simulate database query
            if item_id == 404:
                print(f"\\n  ERROR: Item {item_id} not found")
                return HttpResponse("<html><body><h1>404 Not Found</h1><p>Item does not exist</p></body></html>", status=404)

            if item_id == 403:
                print(f"\\n  ERROR: Access denied to item {item_id}")
                return HttpResponse("<html><body><h1>403 Forbidden</h1><p>You don't have permission</p></body></html>", status=403)

            print(f"\\n  SUCCESS: Retrieved item {item_id}")
            return HttpResponse(f"<html><body><h1>Item {item_id}</h1></body></html>")

        except ValueError as e:
            print(f"\\n  ERROR: Value error - {str(e)}")
            return HttpResponse("<html><body><h1>400 Bad Request</h1></body></html>", status=400)
        except Exception as e:
            print(f"\\n  ERROR: Unexpected error - {str(e)}")
            return HttpResponse("<html><body><h1>500 Internal Server Error</h1></body></html>", status=500)

    # Test various error scenarios
    test_cases = [
        ({'id': '123'}, 200, "Valid request"),
        ({}, 400, "Missing parameter"),
        ({'id': 'abc'}, 400, "Invalid format"),
        ({'id': '404'}, 404, "Not found"),
        ({'id': '403'}, 403, "Forbidden"),
    ]

    for params, expected_status, description in test_cases:
        print(f"\\nTest: {description}")
        request = HttpRequest('GET', '/item/', params)
        response = safe_view(request)
        print(f"  Expected: {expected_status}, Got: {response.status_code} - {'PASS' if response.status_code == expected_status else 'FAIL'}")

# ============================================================================
# Example 9: View Composition and Reusability
# ============================================================================

def example_view_composition():
    """
    Demonstrates view composition patterns.
    """
    print(f"\\n{'='*60}")
    print("Example 9: View Composition and Reusability")
    print(f"{'='*60}")

    # Mixin functions
    def add_user_context(request, context: Dict) -> Dict:
        """Add user information to context."""
        if request.user:
            context['user'] = {
                'username': request.user.username,
                'is_staff': request.user.is_staff
            }
        return context

    def add_site_context(context: Dict) -> Dict:
        """Add site-wide information to context."""
        context['site_name'] = 'My Django Site'
        context['year'] = datetime.now().year
        return context

    # Base view builder
    def base_view(request, template_context: Dict = None):
        """Build base context for all views."""
        context = template_context or {}
        context = add_user_context(request, context)
        context = add_site_context(context)
        return context

    # Specific views using base
    def home_view(request):
        context = base_view(request, {'page_title': 'Home'})
        print(f"\\nHome view context: {json.dumps(context, indent=2)}")
        return HttpResponse(f"<html><body><h1>{context['site_name']} - {context['page_title']}</h1></body></html>")

    def dashboard_view(request):
        context = base_view(request, {
            'page_title': 'Dashboard',
            'stats': {'users': 100, 'items': 500}
        })
        print(f"\\nDashboard view context: {json.dumps(context, indent=2)}")
        return HttpResponse(f"<html><body><h1>{context['page_title']}</h1></body></html>")

    # Test views
    request = HttpRequest('GET', '/home/')
    request.user = User('john_doe', is_authenticated=True)
    response = home_view(request)

    request = HttpRequest('GET', '/dashboard/')
    request.user = User('admin', is_authenticated=True, is_staff=True)
    response = dashboard_view(request)

# ============================================================================
# Example 10: Complete FBV Application
# ============================================================================

def example_complete_fbv_app():
    """
    Complete function-based view application with all patterns.
    """
    print(f"\\n{'='*60}")
    print("Example 10: Complete FBV Application")
    print(f"{'='*60}")

    db = InMemoryDB()

    # Create some test data
    db.create({'title': 'First Post', 'content': 'Hello World', 'published': True})
    db.create({'title': 'Second Post', 'content': 'Another post', 'published': True})
    db.create({'title': 'Draft', 'content': 'Not published yet', 'published': False})

    # Views
    @login_required
    def post_list_view(request):
        """List published posts with pagination."""
        page = int(request.GET.get('page', 1))
        posts = [p for p in db.list() if p.get('published')]

        paginator = Paginator(posts, 2)
        page_obj = paginator.page(page)

        print(f"\\nPost List (Page {page}):")
        for post in page_obj.object_list:
            print(f"  - {post['title']}")

        return JsonResponse({
            'page': page,
            'total_pages': paginator.num_pages,
            'posts': page_obj.object_list,
            'has_next': page_obj.has_next()
        })

    @login_required
    def post_detail_view(request, post_id: int):
        """View single post."""
        post = db.get(post_id)
        if not post:
            return JsonResponse({'error': 'Post not found'}, status=404)

        print(f"\\nPost Detail: {post['title']}")
        return JsonResponse({'post': post})

    @login_required
    @require_http_methods(['POST'])
    def post_create_view(request):
        """Create new post."""
        data = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'published': request.POST.get('published', 'false').lower() == 'true',
            'author': request.user.username,
            'created_at': datetime.now().isoformat()
        }

        post = db.create(data)
        print(f"\\nPost Created: {post['title']} by {post['author']}")

        return JsonResponse({'success': True, 'post': post}, status=201)

    # Run application simulation
    print("\\nSimulating Blog Application...")

    # Authenticated user
    user = User('blogger', is_authenticated=True)

    # List posts
    request = HttpRequest('GET', '/posts/', {'page': '1'})
    request.user = user
    response = post_list_view(request)

    # View post detail
    request = HttpRequest('GET', '/posts/1/')
    request.user = user
    response = post_detail_view(request, 1)

    # Create new post
    request = HttpRequest('POST', '/posts/create/', {
        'title': 'New Post',
        'content': 'This is a new post',
        'published': 'true'
    })
    request.user = user
    response = post_create_view(request)

    # List posts again
    request = HttpRequest('GET', '/posts/', {'page': '1'})
    request.user = user
    response = post_list_view(request)

    print("\\n  Application simulation completed!")

# ============================================================================
# Run All Examples
# ============================================================================

if __name__ == "__main__":
    # Example 1: Basic request/response
    example_request_response()

    # Example 2: Form processing
    example_form_processing()

    # Example 3: View decorators
    example_view_decorators()

    # Example 4: File uploads
    example_file_upload()

    # Example 5: Pagination
    example_pagination()

    # Example 6: AJAX and JSON
    example_ajax_json()

    # Example 7: CRUD operations
    example_crud_operations()

    # Example 8: Error handling
    example_error_handling()

    # Example 9: View composition
    example_view_composition()

    # Example 10: Complete application
    example_complete_fbv_app()

    print(f"\\n{'='*60}")
    print("All Django FBV examples completed successfully!")
    print(f"{'='*60}")
'''

print("Upgraded Lesson 518: Django Function-Based Views")
print(f"  New length: {len(lesson_518['fullSolution']):,} characters")

# Save lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

print("\\n" + "="*70)
print("BATCH 20 PART 2 COMPLETE: Django Function-Based Views")
print("="*70)
print("\\nUpgraded lessons:")
print(f"  - Lesson 518: Django Function-Based Views ({len(lesson_518['fullSolution']):,} chars)")
print("\\nLesson upgraded to 13,000+ characters")
print("Zero package installation required!")
print("="*70)
