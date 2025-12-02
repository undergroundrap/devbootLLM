"""Django simulations batch 4a - First 13 Django lessons"""
import json
import sys

DJANGO_BATCH_4A = {
    515: r'''# In production: from django.db import models
# class User(models.Model):
#     username = models.CharField(max_length=100)
# This simulation demonstrates Django ORM model definition without Django

from datetime import datetime

class DjangoField:
    """Simulates Django model fields"""
    def __init__(self, max_length=None, default=None, null=False, auto_now_add=False):
        self.max_length = max_length
        self.default = default
        self.null = null
        self.auto_now_add = auto_now_add
        self.value = None

    def __get__(self, obj, objtype=None):
        """Descriptor for field access"""
        if obj is None:
            return self
        return obj.__dict__.get(id(self), self.default)

    def __set__(self, obj, value):
        """Descriptor for field assignment"""
        obj.__dict__[id(self)] = value

class CharField(DjangoField):
    """Simulates CharField"""
    pass

class IntegerField(DjangoField):
    """Simulates IntegerField"""
    pass

class DateTimeField(DjangoField):
    """Simulates DateTimeField"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.auto_now_add:
            self.value = datetime.now()

class ModelMeta(type):
    """Metaclass for Django models - handles field registration"""
    def __new__(cls, name, bases, attrs):
        # Real Django: Uses metaclass to register fields and create ORM
        # Simulation: Just collects field information
        model_fields = {}
        for key, value in attrs.items():
            if isinstance(value, DjangoField):
                model_fields[key] = value
        attrs['_fields'] = model_fields
        return super().__new__(cls, name, bases, attrs)

class Model(metaclass=ModelMeta):
    """Simulates django.db.models.Model base class"""
    _fields = {}

    def __init__(self, **kwargs):
        for field_name, value in kwargs.items():
            if field_name in self._fields:
                setattr(self, field_name, value)

    def save(self):
        """Simulate saving to database"""
        print(f"[Simulated] Saving {self.__class__.__name__} to database")
        return self

    def __repr__(self):
        """Display model instance"""
        field_values = []
        for fname in self._fields:
            val = getattr(self, fname, None)
            field_values.append(f"{fname}={val}")
        return f"<{self.__class__.__name__}: {', '.join(field_values)}>"

# Define Django models
print("Django Model Definition - Simulation")
print("=" * 70)

class User(Model):
    """User model with various field types"""
    username = CharField(max_length=100)
    email = CharField(max_length=255)
    age = IntegerField(default=0)
    created_at = DateTimeField(auto_now_add=True)

class Product(Model):
    """Product model for e-commerce"""
    name = CharField(max_length=200)
    price = IntegerField()
    stock = IntegerField(default=0)
    description = CharField(max_length=1000)

# Demonstrate model usage
print("\n1. Create and save User instance:")
user = User(username="john_doe", email="john@example.com", age=25)
print(f"   Created: {user}")
user.save()

print("\n2. Create and save Product instance:")
product = Product(name="Laptop", price=999, stock=50, description="High-performance laptop")
print(f"   Created: {product}")
product.save()

print("\n3. Access model fields:")
print(f"   User.username: {user.username}")
print(f"   User.email: {user.email}")
print(f"   Product.name: {product.name}")
print(f"   Product.price: ${product.price}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.db import models")
print("  class User(models.Model):")
print("      username = models.CharField(max_length=100)")
print("      email = models.CharField(max_length=255)")
print("      age = models.IntegerField(default=0)")
print("      created_at = models.DateTimeField(auto_now_add=True)")
print("  ")
print("  user = User(username='john_doe', email='john@example.com', age=25)")
print("  user.save()  # Saves to database via ORM")
''',

    516: r'''# In production: from django.db import models
# from django.db.models import Q
# User.objects.filter(username='john').exclude(age__lt=18)
# This simulation demonstrates Django QuerySet filtering without database

class QuerySet:
    """Simulates Django ORM QuerySet with filtering capabilities"""
    def __init__(self, data=None):
        self.data = data if data else []
        self._filters = []
        self._excludes = []

    def filter(self, **kwargs):
        """Simulate filter() method - include matching records"""
        qs = QuerySet(self.data.copy())
        qs._filters = self._filters.copy()
        qs._filters.append(kwargs)
        qs._excludes = self._excludes.copy()
        return qs

    def exclude(self, **kwargs):
        """Simulate exclude() method - exclude matching records"""
        qs = QuerySet(self.data.copy())
        qs._filters = self._filters.copy()
        qs._excludes = self._excludes.copy()
        qs._excludes.append(kwargs)
        return qs

    def _match_filters(self, obj):
        """Check if object matches all filter conditions"""
        for filter_dict in self._filters:
            for key, value in filter_dict.items():
                # Simple field matching
                if key.endswith('__gt'):  # Greater than
                    field = key[:-4]
                    if not (getattr(obj, field, None) > value):
                        return False
                elif key.endswith('__lt'):  # Less than
                    field = key[:-4]
                    if not (getattr(obj, field, None) < value):
                        return False
                elif key.endswith('__gte'):  # Greater or equal
                    field = key[:-5]
                    if not (getattr(obj, field, None) >= value):
                        return False
                elif key.endswith('__in'):  # In list
                    field = key[:-4]
                    if getattr(obj, field, None) not in value:
                        return False
                else:  # Exact match
                    if getattr(obj, key, None) != value:
                        return False
        return True

    def _match_excludes(self, obj):
        """Check if object matches any exclude conditions"""
        for exclude_dict in self._excludes:
            for key, value in exclude_dict.items():
                if key.endswith('__lt'):
                    field = key[:-4]
                    if getattr(obj, field, None) < value:
                        return True
                elif getattr(obj, key, None) == value:
                    return True
        return False

    def all(self):
        """Get all records matching filters"""
        result = []
        for obj in self.data:
            if self._match_filters(obj) and not self._match_excludes(obj):
                result.append(obj)
        return result

    def count(self):
        """Count matching records"""
        return len(self.all())

    def first(self):
        """Get first matching record"""
        results = self.all()
        return results[0] if results else None

    def __repr__(self):
        return f"<QuerySet [{self.count()} items]>"

class Q:
    """Simulates Django Q objects for complex queries"""
    def __init__(self, **kwargs):
        self.conditions = kwargs
        self.connector = 'AND'

    def __and__(self, other):
        """Combine queries with AND"""
        combined = Q(**{**self.conditions, **other.conditions})
        combined.connector = 'AND'
        return combined

    def __or__(self, other):
        """Combine queries with OR"""
        combined = Q(**{**self.conditions, **other.conditions})
        combined.connector = 'OR'
        return combined

# Sample data
class User:
    def __init__(self, username, email, age, is_active=True):
        self.username = username
        self.email = email
        self.age = age
        self.is_active = is_active

    def __repr__(self):
        return f"<User: {self.username}, age {self.age}>"

print("Django QuerySet Filtering - Simulation")
print("=" * 70)

# Create sample users
users_data = [
    User("john_doe", "john@example.com", 25, True),
    User("jane_smith", "jane@example.com", 30, True),
    User("bob_johnson", "bob@example.com", 17, False),
    User("alice_williams", "alice@example.com", 28, True),
    User("charlie_brown", "charlie@example.com", 16, False),
]

# Create QuerySet
users_qs = QuerySet(users_data)

print("\n1. Basic filter() - Find users by username:")
result = users_qs.filter(username="john_doe").all()
print(f"   filter(username='john_doe'): {result}")

print("\n2. Filter with comparison - Users older than 20:")
result = users_qs.filter(**{"age__gt": 20}).all()
print(f"   filter(age__gt=20):")
for user in result:
    print(f"     - {user}")

print("\n3. Filter + exclude - Active users over 18:")
result = users_qs.filter(is_active=True).exclude(**{"age__lt": 18}).all()
print(f"   filter(is_active=True).exclude(age__lt=18):")
for user in result:
    print(f"     - {user}")

print("\n4. Count matching records:")
count = users_qs.filter(is_active=True).count()
print(f"   Active users count: {count}")

print("\n5. Get first match:")
user = users_qs.filter(**{"age__gte": 28}).first()
print(f"   First user 28+: {user}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.db import models")
print("  from django.db.models import Q")
print("  User.objects.filter(username='john_doe')")
print("  User.objects.filter(age__gt=20)")
print("  User.objects.filter(is_active=True).exclude(age__lt=18)")
print("  User.objects.filter(is_active=True).exclude(age__lt=18).count()")
print("  User.objects.filter(Q(age__gte=28) | Q(is_active=False))")
''',

    517: r'''# In production: from django.db import models
# class User(models.Model):
#     name = models.CharField(max_length=100)
# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
# This simulation demonstrates Django ForeignKey relationships

class ForeignKey:
    """Simulates Django ForeignKey field"""
    def __init__(self, to_model, on_delete=None, related_name=None):
        self.to_model = to_model
        self.on_delete = on_delete
        self.related_name = related_name
        self.value = None

    def __set__(self, obj, value):
        self.value = value

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.value

class Model:
    """Simulates Django Model base class"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        print(f"[Simulated] Saving {self.__class__.__name__} to database")
        return self

    def __repr__(self):
        if hasattr(self, 'title'):
            return f"<{self.__class__.__name__}: {self.title}>"
        elif hasattr(self, 'name'):
            return f"<{self.__class__.__name__}: {self.name}>"
        return f"<{self.__class__.__name__}>"

# Database simulation
all_users = []
all_posts = []
all_comments = []

class User(Model):
    """User model"""
    def __init__(self, name, email):
        super().__init__(name=name, email=email)
        self.id = len(all_users) + 1
        all_users.append(self)

    def __repr__(self):
        return f"<User: {self.name}>"

class Post(Model):
    """Post model with ForeignKey to User (One-to-Many)"""
    def __init__(self, title, content, user):
        super().__init__(title=title, content=content, user=user)
        self.id = len(all_posts) + 1
        all_posts.append(self)

    def get_author(self):
        """Get related User instance"""
        return self.user

    def __repr__(self):
        return f"<Post: {self.title} by {self.user.name}>"

class Comment(Model):
    """Comment model with ForeignKey to Post"""
    def __init__(self, text, post, author):
        super().__init__(text=text, post=post, author=author)
        self.id = len(all_comments) + 1
        all_comments.append(self)

    def __repr__(self):
        return f"<Comment: {self.text[:30]}... on {self.post.title}>"

print("Django ForeignKey Relationships (One-to-Many) - Simulation")
print("=" * 70)

# Create users
print("\n1. Create User instances:")
user1 = User("Alice Smith", "alice@example.com")
user2 = User("Bob Johnson", "bob@example.com")
print(f"   Created: {user1}")
print(f"   Created: {user2}")

# Create posts with ForeignKey to users
print("\n2. Create Post instances with ForeignKey relationships:")
post1 = Post("Django Tips", "Here are some Django tips...", user1)
post2 = Post("Python Best Practices", "Follow these practices...", user1)
post3 = Post("Web Development", "Introduction to web dev...", user2)
print(f"   Created: {post1}")
print(f"   Created: {post2}")
print(f"   Created: {post3}")

# Create comments on posts
print("\n3. Create Comment instances (nested ForeignKey):")
comment1 = Comment("Great tips!", post1, user2)
comment2 = Comment("Very helpful", post2, user1)
print(f"   Created: {comment1}")
print(f"   Created: {comment2}")

# Access related objects (simulating related_name)
print("\n4. Access related objects via ForeignKey:")
print(f"   post1.get_author(): {post1.get_author()}")
print(f"   post1.user.email: {post1.user.email}")

print("\n5. Query by related object (One-to-Many):")
user_posts = [p for p in all_posts if p.user == user1]
print(f"   Posts by {user1.name}: {len(user_posts)}")
for post in user_posts:
    print(f"     - {post.title}")

print("\n6. Access reverse relation (related_name='posts'):")
post_comments = [c for c in all_comments if c.post == post1]
print(f"   Comments on '{post1.title}': {len(post_comments)}")
for comment in post_comments:
    print(f"     - {comment.text} (by {comment.author.name})")

print("\n" + "=" * 70)
print("Real Django:")
print("  class User(models.Model):")
print("      name = models.CharField(max_length=100)")
print("  class Post(models.Model):")
print("      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')")
print("  # Access related:")
print("  post = Post.objects.first()")
print("  post.user  # Get author")
print("  user.posts.all()  # Get all posts by user (via related_name)")
''',

    518: r'''# In production: from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# def my_view(request):
#     if request.method == 'POST':
#         return redirect('home')
#     return render(request, 'template.html', {'data': 'value'})
# This simulation demonstrates Django function-based views

from datetime import datetime

class HttpRequest:
    """Simulates Django HttpRequest object"""
    def __init__(self, method='GET', path='/', data=None, user=None):
        self.method = method
        self.path = path
        self.GET = {}
        self.POST = data if data else {}
        self.user = user
        self.session = {}
        self.META = {'HTTP_USER_AGENT': 'Mozilla/5.0'}

    def __repr__(self):
        return f"<HttpRequest: {self.method} {self.path}>"

class HttpResponse:
    """Simulates Django HttpResponse object"""
    def __init__(self, content='', status=200):
        self.content = content
        self.status_code = status
        self.headers = {}

    def __repr__(self):
        return f"<HttpResponse: status {self.status_code}>"

class HttpResponseRedirect(HttpResponse):
    """Simulates redirect response"""
    def __init__(self, url, status=302):
        super().__init__(f"Redirect to {url}", status)
        self.url = url
        self.headers['Location'] = url

def render(request, template_name, context=None):
    """Simulates Django render() function"""
    context = context if context else {}
    html = f"<html><body>"
    html += f"<h1>{template_name}</h1>"
    for key, value in context.items():
        html += f"<p>{key}: {value}</p>"
    html += "</body></html>"
    return HttpResponse(html, 200)

def redirect(view_name):
    """Simulates Django redirect() function"""
    url = f"/{view_name}/"
    return HttpResponseRedirect(url)

class User:
    """Simulates Django User"""
    def __init__(self, username, is_authenticated=False):
        self.username = username
        self.is_authenticated = is_authenticated

print("Django Function-Based Views - Simulation")
print("=" * 70)

# Define views
def home_view(request):
    """Simulates a simple home view"""
    print(f"\nProcessing request: {request}")
    context = {
        'title': 'Home Page',
        'message': 'Welcome to Django!',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render(request, 'home.html', context)

def login_view(request):
    """Simulates login view with form processing"""
    print(f"\nProcessing request: {request}")
    if request.method == 'POST':
        username = request.POST.get('username', '')
        # Simulate authentication
        print(f"  [Simulated] Authenticating user: {username}")
        # Redirect on successful login
        return redirect('dashboard')
    else:
        # Show login form
        context = {'form_title': 'Login', 'fields': ['username', 'password']}
        return render(request, 'login.html', context)

def profile_view(request, user_id):
    """Simulates user profile view"""
    print(f"\nProcessing request: {request}")
    if not request.user.is_authenticated:
        print(f"  [Simulated] User not authenticated, redirecting to login")
        return redirect('login')

    context = {
        'username': f'user_{user_id}',
        'email': f'user{user_id}@example.com',
        'joined': '2023-01-15'
    }
    return render(request, 'profile.html', context)

# Simulate requests
print("\n1. GET request to home view:")
request1 = HttpRequest(method='GET', path='/')
response1 = home_view(request1)
print(f"   Response: {response1}")

print("\n2. GET request to login view (show form):")
request2 = HttpRequest(method='GET', path='/login/')
response2 = login_view(request2)
print(f"   Response: {response2}")

print("\n3. POST request to login view (submit form):")
request3 = HttpRequest(method='POST', path='/login/', data={'username': 'alice', 'password': 'secret'})
response3 = login_view(request3)
print(f"   Response: {response3}")
print(f"   Redirect URL: {response3.url}")

print("\n4. GET request to profile view (authenticated):")
request4 = HttpRequest(method='GET', path='/profile/42/')
request4.user = User('alice', is_authenticated=True)
response4 = profile_view(request4, 42)
print(f"   Response: {response4}")

print("\n5. GET request to profile view (not authenticated):")
request5 = HttpRequest(method='GET', path='/profile/42/')
request5.user = User('anonymous', is_authenticated=False)
response5 = profile_view(request5, 42)
print(f"   Response: {response5}")
print(f"   Redirect URL: {response5.url}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.http import HttpResponse")
print("  from django.shortcuts import render, redirect")
print("  def home_view(request):")
print("      context = {'title': 'Home'}")
print("      return render(request, 'home.html', context)")
print("  def login_view(request):")
print("      if request.method == 'POST':")
print("          return redirect('dashboard')")
print("      return render(request, 'login.html')")
''',

    519: r'''# In production: from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# def protected_view(request):
#     user = authenticate(username='user', password='pass')
#     login(request, user)
# This simulation demonstrates Django authentication

from functools import wraps

class User:
    """Simulates Django User model"""
    def __init__(self, username, password, email, is_active=True):
        self.username = username
        self.password = password  # In real Django: hashed with make_password()
        self.email = email
        self.is_active = is_active
        self.is_authenticated = False

    def check_password(self, raw_password):
        """Simulate password verification"""
        # In real Django: uses PBKDF2 or bcrypt
        return self.password == raw_password

    def __repr__(self):
        return f"<User: {self.username}>"

class AnonymousUser:
    """Simulates anonymous user"""
    def __init__(self):
        self.username = 'AnonymousUser'
        self.is_authenticated = False

class AuthenticationBackend:
    """Simulates Django authentication"""
    def __init__(self):
        self.users = []

    def create_user(self, username, email, password):
        """Create new user"""
        user = User(username, password, email)
        self.users.append(user)
        print(f"[Simulated] Created user: {username}")
        return user

    def authenticate(self, username=None, password=None):
        """Authenticate user"""
        for user in self.users:
            if user.username == username and user.check_password(password):
                print(f"[Simulated] Authenticated: {username}")
                user.is_authenticated = True
                return user
        print(f"[Simulated] Authentication failed for: {username}")
        return None

class HttpRequest:
    """Simulates Django HttpRequest"""
    def __init__(self):
        self.user = AnonymousUser()
        self.session = {}

class HttpResponse:
    """Simulates Django HttpResponse"""
    def __init__(self, content=''):
        self.content = content

def login_required(view_func):
    """Decorator simulating @login_required"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            print(f"[Simulated] User not authenticated, denying access")
            return HttpResponse("401 Unauthorized")
        return view_func(request, *args, **kwargs)
    return wrapper

# Authentication backend
auth_backend = AuthenticationBackend()

print("Django User Authentication - Simulation")
print("=" * 70)

# Create users
print("\n1. Create users:")
user1 = auth_backend.create_user('alice', 'alice@example.com', 'secret123')
user2 = auth_backend.create_user('bob', 'bob@example.com', 'mypassword')

# Protected view
@login_required
def dashboard_view(request):
    """Dashboard accessible only to authenticated users"""
    return HttpResponse(f"Dashboard: Welcome {request.user.username}!")

@login_required
def settings_view(request):
    """Settings page for authenticated users"""
    return HttpResponse(f"Settings for {request.user.username}")

# Demo authentication flow
print("\n2. Authenticate with correct credentials:")
request1 = HttpRequest()
user = auth_backend.authenticate(username='alice', password='secret123')
if user:
    request1.user = user
    response = dashboard_view(request1)
    print(f"   Response: {response.content}")

print("\n3. Authenticate with incorrect credentials:")
request2 = HttpRequest()
user = auth_backend.authenticate(username='bob', password='wrongpass')
if not user:
    print(f"   Authentication failed - access denied")

print("\n4. Access protected view without authentication:")
request3 = HttpRequest()
response = dashboard_view(request3)
print(f"   Response: {response.content}")

print("\n5. Successful login and session management:")
request4 = HttpRequest()
authenticated_user = auth_backend.authenticate(username='alice', password='secret123')
if authenticated_user:
    request4.user = authenticated_user
    request4.session['user_id'] = authenticated_user.username
    response = settings_view(request4)
    print(f"   Response: {response.content}")
    print(f"   Session: {request4.session}")

print("\n6. Multiple authentication attempts:")
results = {
    'alice/secret123': auth_backend.authenticate(username='alice', password='secret123'),
    'bob/wrongpass': auth_backend.authenticate(username='bob', password='wrongpass'),
    'unknown/pass': auth_backend.authenticate(username='unknown', password='pass'),
}
print(f"   Authentication results:")
for attempt, result in results.items():
    status = 'Success' if result else 'Failed'
    print(f"     {attempt}: {status}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.contrib.auth import authenticate, login")
print("  from django.contrib.auth.decorators import login_required")
print("  user = authenticate(username='alice', password='secret123')")
print("  if user is not None:")
print("      login(request, user)")
print("  @login_required")
print("  def protected_view(request):")
print("      return HttpResponse(f'Welcome {request.user.username}')")
''',

    752: r'''# In production: from django.db import models
# class Tag(models.Model):
#     name = models.CharField(max_length=50)
# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     tags = models.ManyToManyField(Tag)
# This simulation demonstrates Django ManyToMany relationships

class ManyToManyField:
    """Simulates Django ManyToManyField"""
    def __init__(self, to_model, related_name=None, through=None):
        self.to_model = to_model
        self.related_name = related_name
        self.through = through
        self.relations = []

    def add(self, obj):
        """Add related object"""
        if obj not in self.relations:
            self.relations.append(obj)

    def remove(self, obj):
        """Remove related object"""
        if obj in self.relations:
            self.relations.remove(obj)

    def all(self):
        """Get all related objects"""
        return self.relations.copy()

    def count(self):
        """Count related objects"""
        return len(self.relations)

class Model:
    """Simulates Django Model"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        print(f"[Simulated] Saving {self.__class__.__name__}")
        return self

    def __repr__(self):
        if hasattr(self, 'name'):
            return f"<{self.__class__.__name__}: {self.name}>"
        elif hasattr(self, 'title'):
            return f"<{self.__class__.__name__}: {self.title}>"
        return f"<{self.__class__.__name__}>"

# Database simulation
all_tags = []
all_categories = []
all_articles = []

class Tag(Model):
    """Tag model for classification"""
    def __init__(self, name, slug=None):
        super().__init__(name=name, slug=slug)
        self.id = len(all_tags) + 1
        all_tags.append(self)

class Category(Model):
    """Category model"""
    def __init__(self, name):
        super().__init__(name=name)
        self.id = len(all_categories) + 1
        all_categories.append(self)

class Article(Model):
    """Article with ManyToMany relationship to tags and categories"""
    def __init__(self, title, content):
        super().__init__(title=title, content=content)
        self.id = len(all_articles) + 1
        self.tags = ManyToManyField(Tag)
        self.categories = ManyToManyField(Category)
        all_articles.append(self)

print("Django ManyToMany Relationships - Simulation")
print("=" * 70)

# Create tags
print("\n1. Create Tag instances:")
tag_python = Tag("Python", "python")
tag_django = Tag("Django", "django")
tag_web = Tag("Web Development", "web-dev")
tag_tutorial = Tag("Tutorial", "tutorial")
print(f"   Created: {tag_python}, {tag_django}, {tag_web}, {tag_tutorial}")

# Create categories
print("\n2. Create Category instances:")
cat_backend = Category("Backend")
cat_frontend = Category("Frontend")
cat_fullstack = Category("Full Stack")
print(f"   Created: {cat_backend}, {cat_frontend}, {cat_fullstack}")

# Create articles
print("\n3. Create Article instances:")
article1 = Article("Getting Started with Django", "Django is a powerful web framework...")
article2 = Article("Python Best Practices", "Here are essential Python practices...")
article3 = Article("Building REST APIs", "Learn to build scalable REST APIs...")
print(f"   Created: {article1}")
print(f"   Created: {article2}")
print(f"   Created: {article3}")

# Add ManyToMany relationships
print("\n4. Add ManyToMany relationships (tags):")
article1.tags.add(tag_django)
article1.tags.add(tag_python)
article1.tags.add(tag_web)
print(f"   {article1.title} tags: {[t.name for t in article1.tags.all()]}")

article2.tags.add(tag_python)
article2.tags.add(tag_tutorial)
print(f"   {article2.title} tags: {[t.name for t in article2.tags.all()]}")

article3.tags.add(tag_web)
article3.tags.add(tag_django)
article3.tags.add(tag_tutorial)
print(f"   {article3.title} tags: {[t.name for t in article3.tags.all()]}")

# Add categories
print("\n5. Add ManyToMany relationships (categories):")
article1.categories.add(cat_backend)
article1.categories.add(cat_fullstack)
print(f"   {article1.title} categories: {[c.name for c in article1.categories.all()]}")

article2.categories.add(cat_fullstack)
print(f"   {article2.title} categories: {[c.name for c in article2.categories.all()]}")

article3.categories.add(cat_backend)
article3.categories.add(cat_fullstack)
print(f"   {article3.title} categories: {[c.name for c in article3.categories.all()]}")

# Query through relationships
print("\n6. Query articles by tag:")
python_articles = [a for a in all_articles if tag_python in a.tags.all()]
print(f"   Articles with tag '{tag_python.name}': {len(python_articles)}")
for article in python_articles:
    print(f"     - {article.title}")

print("\n7. Count relationships:")
print(f"   {article1.title} has {article1.tags.count()} tags and {article1.categories.count()} categories")
print(f"   {article3.title} has {article3.tags.count()} tags and {article3.categories.count()} categories")

print("\n8. Remove relationship:")
article1.tags.remove(tag_web)
print(f"   Removed '{tag_web.name}' from {article1.title}")
print(f"   Remaining tags: {[t.name for t in article1.tags.all()]}")

print("\n" + "=" * 70)
print("Real Django:")
print("  class Tag(models.Model):")
print("      name = models.CharField(max_length=50)")
print("  class Article(models.Model):")
print("      title = models.CharField(max_length=200)")
print("      tags = models.ManyToManyField(Tag)")
print("  article = Article.objects.first()")
print("  article.tags.add(tag1, tag2)")
print("  article.tags.all()")
print("  article.tags.count()")
''',

    753: r'''# In production: from django.db.models import Count, Sum, Avg, Max, Min
# Article.objects.annotate(tag_count=Count('tags')).filter(tag_count__gt=2)
# This simulation demonstrates Django model aggregation

class QuerySet:
    """Simulates Django QuerySet with aggregation"""
    def __init__(self, data=None):
        self.data = data if data else []
        self._aggregations = {}

    def annotate(self, **kwargs):
        """Annotate records with aggregated values"""
        qs = QuerySet(self.data.copy())
        qs._aggregations = self._aggregations.copy()
        qs._aggregations.update(kwargs)
        return qs

    def aggregate(self, **kwargs):
        """Aggregate entire queryset"""
        results = {}
        for key, agg_func in kwargs.items():
            results[key] = agg_func(self.data)
        return results

    def all(self):
        """Get all records with annotations"""
        for obj in self.data:
            for agg_name, agg_func in self._aggregations.items():
                setattr(obj, agg_name, agg_func(obj))
        return self.data

    def count(self):
        """Count records"""
        return len(self.data)

class Count:
    """Simulates Count aggregation"""
    def __init__(self, field):
        self.field = field

    def __call__(self, obj):
        """Count items in relation"""
        if hasattr(obj, self.field):
            relation = getattr(obj, self.field)
            if hasattr(relation, '__len__'):
                return len(relation)
            elif hasattr(relation, 'count'):
                return relation.count()
        return 0

class Sum:
    """Simulates Sum aggregation"""
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        """Sum field values"""
        if not isinstance(data, list):
            return getattr(data, self.field, 0)
        total = 0
        for obj in data:
            if hasattr(obj, self.field):
                total += getattr(obj, self.field)
        return total

class Avg:
    """Simulates Average aggregation"""
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        """Calculate average"""
        if not isinstance(data, list):
            return getattr(data, self.field, 0)
        if not data:
            return 0
        total = sum(getattr(obj, self.field, 0) for obj in data)
        return total / len(data)

class Max:
    """Simulates Max aggregation"""
    def __init__(self, field):
        self.field = field

    def __call__(self, data):
        """Get maximum value"""
        if not isinstance(data, list):
            return getattr(data, self.field, 0)
        if not data:
            return None
        values = [getattr(obj, self.field, 0) for obj in data]
        return max(values)

class Article:
    """Article model"""
    def __init__(self, title, view_count, rating):
        self.title = title
        self.view_count = view_count
        self.rating = rating
        self.comments = []
        self.tags = []

    def __repr__(self):
        return f"<Article: {self.title}>"

print("Django Model Aggregation - Simulation")
print("=" * 70)

# Create sample articles
articles = [
    Article("Django Tips", 150, 4.5),
    Article("Python Basics", 200, 4.8),
    Article("REST APIs", 300, 4.9),
    Article("Web Scraping", 100, 4.2),
    Article("Database Design", 180, 4.7),
]

# Add comments to articles (for count demonstration)
for i, article in enumerate(articles):
    article.comments = list(range(i * 2, i * 2 + 5))

# Add tags to articles
for i, article in enumerate(articles):
    article.tags = list(range(i + 1, i + 4))

print("\n1. Count aggregation:")
qs = QuerySet(articles)
qs_with_count = qs.annotate(comment_count=Count('comments'))
for article in qs_with_count.all():
    print(f"   {article.title}: {article.comment_count} comments")

print("\n2. Sum aggregation (total views):")
sum_agg = Sum('view_count')
total_views = sum_agg(articles)
print(f"   Total views across all articles: {total_views}")

print("\n3. Average aggregation (avg rating):")
avg_agg = Avg('rating')
avg_rating = avg_agg(articles)
print(f"   Average rating: {avg_rating:.2f}")

print("\n4. Max aggregation (most viewed):")
max_agg = Max('view_count')
most_views = max_agg(articles)
print(f"   Most viewed article has {most_views} views")

print("\n5. Annotate with multiple aggregations:")
print(f"   Article statistics:")
qs = QuerySet(articles)
qs_annotated = qs.annotate(
    comment_count=Count('comments'),
    tag_count=Count('tags')
)
for article in qs_annotated.all():
    print(f"     {article.title}:")
    print(f"       - Views: {article.view_count}")
    print(f"       - Rating: {article.rating}")
    print(f"       - Comments: {article.comment_count}")
    print(f"       - Tags: {article.tag_count}")

print("\n6. Aggregate entire queryset:")
results = qs.aggregate(
    total_views=Sum('view_count'),
    avg_rating=Avg('rating'),
    total_articles=Count('comments')
)
print(f"   Aggregation results:")
print(f"     - Total views: {results['total_views']}")
print(f"     - Average rating: {results['avg_rating']:.2f}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.db.models import Count, Sum, Avg")
print("  Article.objects.annotate(comment_count=Count('comments'))")
print("  Article.objects.aggregate(total_views=Sum('view_count'))")
print("  Article.objects.aggregate(avg_rating=Avg('rating'))")
print("  Article.objects.annotate(count=Count('tags')).filter(count__gt=2)")
''',

    754: r'''# In production: from django.views import View
# from django.views.generic import ListView, DetailView, CreateView
# class ArticleListView(ListView):
#     model = Article
#     paginate_by = 10
# This simulation demonstrates Django class-based views

class View:
    """Simulates Django View base class"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dispatch(self, request, *args, **kwargs):
        """Route request to appropriate handler"""
        method = request.method.lower()
        handler = getattr(self, method, None)
        if handler:
            return handler(request, *args, **kwargs)
        raise Exception(f"Method {request.method} not allowed")

    def get(self, request, *args, **kwargs):
        """Handle GET request"""
        raise NotImplementedError

    def post(self, request, *args, **kwargs):
        """Handle POST request"""
        raise NotImplementedError

class ListView(View):
    """Simulates Django ListView"""
    model = None
    paginate_by = None
    template_name = None

    def get(self, request, *args, **kwargs):
        """Return list of objects"""
        objects = self.get_queryset()
        context = self.get_context_data(object_list=objects)
        return self.render_to_response(context)

    def get_queryset(self):
        """Get objects to display"""
        return self.model if isinstance(self.model, list) else []

    def get_context_data(self, **kwargs):
        """Build template context"""
        return {
            'object_list': kwargs.get('object_list', []),
            'count': len(kwargs.get('object_list', []))
        }

    def render_to_response(self, context):
        """Render response"""
        return f"<ListView: {self.template_name or 'list'} with {context['count']} items>"

class DetailView(View):
    """Simulates Django DetailView"""
    model = None
    template_name = None
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        """Get single object"""
        pk = kwargs.get(self.pk_url_kwarg)
        obj = self.get_object(pk)
        context = self.get_context_data(object=obj)
        return self.render_to_response(context)

    def get_object(self, pk):
        """Retrieve object by primary key"""
        for obj in self.model:
            if hasattr(obj, 'id') and obj.id == int(pk):
                return obj
        return None

    def get_context_data(self, **kwargs):
        """Build template context"""
        return {'object': kwargs.get('object')}

    def render_to_response(self, context):
        """Render detail response"""
        obj = context.get('object')
        return f"<DetailView: {obj} detail>"

class CreateView(View):
    """Simulates Django CreateView"""
    model = None
    template_name = None
    fields = []

    def get(self, request, *args, **kwargs):
        """Show creation form"""
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        """Create object"""
        obj = self.create_object(request.POST)
        if obj:
            return f"<CreateView: Created {obj}>"
        return "<CreateView: Validation failed>"

    def create_object(self, data):
        """Create new object from form data"""
        return f"New object from {data}"

    def get_context_data(self, **kwargs):
        """Build form context"""
        return {'form_fields': self.fields}

    def render_to_response(self, context):
        """Render form"""
        return f"<CreateView: {self.template_name} form>"

class HttpRequest:
    """Simulates Django HttpRequest"""
    def __init__(self, method='GET', data=None):
        self.method = method
        self.POST = data if data else {}

# Sample data
class Article:
    """Article model"""
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<Article: {self.title}>"

articles = [
    Article(1, "Django Basics", "Learn Django fundamentals..."),
    Article(2, "Advanced Django", "Deep dive into Django..."),
    Article(3, "REST APIs", "Building REST APIs..."),
]

print("Django Class-Based Views - Simulation")
print("=" * 70)

# ListView example
print("\n1. ListView - Display list of articles:")
class ArticleListView(ListView):
    model = articles
    template_name = 'article_list.html'
    paginate_by = 10

view = ArticleListView()
request = HttpRequest(method='GET')
response = view.dispatch(request)
print(f"   {response}")

# DetailView example
print("\n2. DetailView - Display single article:")
class ArticleDetailView(DetailView):
    model = articles
    template_name = 'article_detail.html'

view = ArticleDetailView()
request = HttpRequest(method='GET')
response = view.dispatch(request, pk=1)
print(f"   {response}")

print("\n3. DetailView with different article:")
response = view.dispatch(request, pk=3)
print(f"   {response}")

# CreateView example
print("\n4. CreateView - Show creation form:")
class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'content']

view = ArticleCreateView()
request = HttpRequest(method='GET')
response = view.dispatch(request)
print(f"   {response}")

print("\n5. CreateView - Submit form:")
request = HttpRequest(method='POST', data={'title': 'New Article', 'content': 'Content here'})
response = view.dispatch(request)
print(f"   {response}")

print("\n6. List all articles with context:")
view = ArticleListView()
queryset = view.get_queryset()
context = view.get_context_data(object_list=queryset)
print(f"   Context: {context}")
print(f"   Articles in context:")
for article in context['object_list']:
    print(f"     - {article}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.views.generic import ListView, DetailView, CreateView")
print("  class ArticleListView(ListView):")
print("      model = Article")
print("      template_name = 'article_list.html'")
print("      paginate_by = 10")
print("  class ArticleDetailView(DetailView):")
print("      model = Article")
print("  class ArticleCreateView(CreateView):")
print("      model = Article")
print("      fields = ['title', 'content']")
''',

    755: r'''# In production: from rest_framework import serializers
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ['id', 'title', 'content']
# This simulation demonstrates Django REST Framework serializers

class Serializer:
    """Base serializer class"""
    def __init__(self, instance=None, data=None):
        self.instance = instance
        self.data_input = data
        self.errors = {}
        self._validated_data = None

    def validate(self):
        """Validate incoming data"""
        if not self.data_input:
            return True
        for field_name in self.fields:
            if field_name not in self.data_input:
                self.errors[field_name] = f"{field_name} is required"
        return len(self.errors) == 0

    def save(self):
        """Save validated data"""
        if not self.validate():
            raise ValueError(f"Validation errors: {self.errors}")
        return self.create(self.data_input)

    def create(self, validated_data):
        """Override in subclass"""
        raise NotImplementedError

class ModelSerializer(Serializer):
    """Serializer for Django models"""
    class Meta:
        model = None
        fields = []

    @property
    def fields(self):
        """Get field names from Meta"""
        return self.Meta.fields if hasattr(self.Meta, 'fields') else []

    def to_representation(self):
        """Convert instance to dictionary"""
        if not self.instance:
            return {}
        data = {}
        for field in self.fields:
            if hasattr(self.instance, field):
                value = getattr(self.instance, field)
                data[field] = value
        return data

    def to_internal_value(self):
        """Convert input data to Python objects"""
        return self.data_input

    def create(self, validated_data):
        """Create model instance"""
        return f"Created: {validated_data}"

    def update(self, instance, validated_data):
        """Update model instance"""
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

# Sample model
class Article:
    """Article model"""
    def __init__(self, id=None, title='', content='', author=''):
        self.id = id
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"<Article: {self.title}>"

class Comment:
    """Comment model"""
    def __init__(self, id=None, text='', author=''):
        self.id = id
        self.text = text
        self.author = author

    def __repr__(self):
        return f"<Comment: {self.text[:30]}>"

print("Django REST Framework Serializer - Simulation")
print("=" * 70)

# Define serializers
class ArticleSerializer(ModelSerializer):
    """Serializer for Article model"""
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author']

class CommentSerializer(ModelSerializer):
    """Serializer for Comment model"""
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author']

# Demo serialization
print("\n1. Serialize model instance to JSON:")
article = Article(1, "Django Tips", "Tips for Django development", "alice")
serializer = ArticleSerializer(article)
print(f"   Instance: {article}")
print(f"   Serialized: {serializer.to_representation()}")

print("\n2. Deserialize JSON to create model:")
data = {
    'title': 'REST API Basics',
    'content': 'Learn REST API design...',
    'author': 'bob'
}
serializer = ArticleSerializer(data=data)
if serializer.validate():
    print(f"   Input data: {data}")
    print(f"   Validation: PASSED")
    result = serializer.create(data)
    print(f"   Result: {result}")
else:
    print(f"   Validation errors: {serializer.errors}")

print("\n3. Validate required fields:")
incomplete_data = {'title': 'Partial Article'}
serializer = ArticleSerializer(data=incomplete_data)
if not serializer.validate():
    print(f"   Input data: {incomplete_data}")
    print(f"   Validation errors:")
    for field, error in serializer.errors.items():
        print(f"     - {field}: {error}")

print("\n4. Serialize multiple instances:")
articles = [
    Article(1, "Django", "Django tutorial", "alice"),
    Article(2, "Flask", "Flask basics", "bob"),
    Article(3, "FastAPI", "Fast APIs", "charlie"),
]
print(f"   Serializing {len(articles)} articles:")
for article in articles:
    serializer = ArticleSerializer(article)
    print(f"     - {serializer.to_representation()}")

print("\n5. Update existing instance:")
article = Article(1, "Django Tips", "Original content", "alice")
update_data = {'title': 'Advanced Django', 'content': 'New content'}
serializer = ArticleSerializer(article, data=update_data)
if serializer.validate():
    updated = serializer.update(article, update_data)
    print(f"   Updated article: title='{updated.title}', content='{updated.content}'")

print("\n6. Serialize with nested data:")
article = Article(1, "Article", "Content", "alice")
serializer = ArticleSerializer(article)
output = serializer.to_representation()
print(f"   Serialized output: {output}")
print(f"   Field types: {[(k, type(v).__name__) for k, v in output.items()]}")

print("\n" + "=" * 70)
print("Real Django REST Framework:")
print("  from rest_framework import serializers")
print("  class ArticleSerializer(serializers.ModelSerializer):")
print("      class Meta:")
print("          model = Article")
print("          fields = ['id', 'title', 'content', 'author']")
print("  serializer = ArticleSerializer(article)")
print("  serializer.data")
''',

    756: r'''# In production: from rest_framework.viewsets import ModelViewSet
# from rest_framework import routers
# class ArticleViewSet(ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
# This simulation demonstrates Django REST Framework ViewSets

class ViewSet:
    """Base ViewSet class"""
    def __init__(self):
        self.queryset = []
        self.serializer_class = None

    def get_queryset(self):
        """Get base queryset"""
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        """Get serializer instance"""
        return self.serializer_class(*args, **kwargs)

class ModelViewSet(ViewSet):
    """Simulates Django REST ModelViewSet"""
    def list(self, request):
        """List all objects - GET /endpoint/"""
        queryset = self.get_queryset()
        data = [{'id': i, 'name': f'Item {i}'} for i in range(1, len(queryset) + 1)]
        return {
            'method': 'GET',
            'action': 'list',
            'count': len(data),
            'data': data
        }

    def create(self, request, data=None):
        """Create new object - POST /endpoint/"""
        data = data if data else {}
        return {
            'method': 'POST',
            'action': 'create',
            'status': 'created',
            'data': data
        }

    def retrieve(self, request, pk=None):
        """Get single object - GET /endpoint/{id}/"""
        return {
            'method': 'GET',
            'action': 'retrieve',
            'pk': pk,
            'data': {'id': pk, 'name': f'Item {pk}'}
        }

    def update(self, request, pk=None, data=None):
        """Update object - PUT /endpoint/{id}/"""
        data = data if data else {}
        return {
            'method': 'PUT',
            'action': 'update',
            'pk': pk,
            'status': 'updated',
            'data': data
        }

    def partial_update(self, request, pk=None, data=None):
        """Partial update - PATCH /endpoint/{id}/"""
        data = data if data else {}
        return {
            'method': 'PATCH',
            'action': 'partial_update',
            'pk': pk,
            'status': 'partially_updated',
            'data': data
        }

    def destroy(self, request, pk=None):
        """Delete object - DELETE /endpoint/{id}/"""
        return {
            'method': 'DELETE',
            'action': 'destroy',
            'pk': pk,
            'status': 'deleted'
        }

class Router:
    """Simulates DRF router"""
    def __init__(self):
        self.routes = {}

    def register(self, prefix, viewset, basename=None):
        """Register viewset"""
        self.routes[prefix] = {
            'viewset': viewset,
            'basename': basename or prefix
        }
        print(f"[Registered] {prefix} -> {viewset.__class__.__name__}")

    def get_urls(self):
        """Get generated URLs"""
        urls = []
        for prefix, info in self.routes.items():
            viewset = info['viewset']
            urls.append(f"GET    /{prefix}/              # list")
            urls.append(f"POST   /{prefix}/              # create")
            urls.append(f"GET    /{prefix}/{{id}}/        # retrieve")
            urls.append(f"PUT    /{prefix}/{{id}}/        # update")
            urls.append(f"PATCH  /{prefix}/{{id}}/        # partial_update")
            urls.append(f"DELETE /{prefix}/{{id}}/        # destroy")
        return urls

# Sample model and serializer
class Article:
    """Article model"""
    def __init__(self, id=None, title='', content=''):
        self.id = id
        self.title = title
        self.content = content

class ArticleSerializer:
    """Simple serializer"""
    pass

class Comment:
    """Comment model"""
    def __init__(self, id=None, text=''):
        self.id = id
        self.text = text

print("Django REST Framework ViewSet - Simulation")
print("=" * 70)

# Create ViewSet
class ArticleViewSet(ModelViewSet):
    """ViewSet for Article model"""
    queryset = [Article(1, "Django", "Learn Django"),
                Article(2, "REST", "REST APIs"),
                Article(3, "DRF", "Django REST Framework")]
    serializer_class = ArticleSerializer

class CommentViewSet(ModelViewSet):
    """ViewSet for Comment model"""
    queryset = [Comment(1, "Great article!"),
                Comment(2, "Very helpful")]
    serializer_class = None

print("\n1. Register ViewSets with router:")
router = Router()
article_viewset = ArticleViewSet()
comment_viewset = CommentViewSet()
router.register('articles', article_viewset)
router.register('comments', comment_viewset)

print("\n2. Generated API endpoints:")
for url in router.get_urls():
    print(f"   {url}")

print("\n3. List action - GET /articles/")
response = article_viewset.list(None)
print(f"   Action: {response['action']}")
print(f"   Count: {response['count']}")
print(f"   Data: {response['data']}")

print("\n4. Create action - POST /articles/")
new_article = {'title': 'FastAPI', 'content': 'Fast APIs...'}
response = article_viewset.create(None, new_article)
print(f"   Action: {response['action']}")
print(f"   Status: {response['status']}")
print(f"   Data: {response['data']}")

print("\n5. Retrieve action - GET /articles/1/")
response = article_viewset.retrieve(None, pk=1)
print(f"   Action: {response['action']}")
print(f"   Data: {response['data']}")

print("\n6. Update action - PUT /articles/1/")
update_data = {'title': 'Advanced Django', 'content': 'Advanced topics...'}
response = article_viewset.update(None, pk=1, data=update_data)
print(f"   Action: {response['action']}")
print(f"   Status: {response['status']}")

print("\n7. Partial update - PATCH /articles/2/")
patch_data = {'title': 'RESTful APIs'}
response = article_viewset.partial_update(None, pk=2, data=patch_data)
print(f"   Action: {response['action']}")
print(f"   Status: {response['status']}")

print("\n8. Delete action - DELETE /articles/3/")
response = article_viewset.destroy(None, pk=3)
print(f"   Action: {response['action']}")
print(f"   Status: {response['status']}")

print("\n" + "=" * 70)
print("Real Django REST Framework:")
print("  from rest_framework.viewsets import ModelViewSet")
print("  from rest_framework.routers import DefaultRouter")
print("  class ArticleViewSet(ModelViewSet):")
print("      queryset = Article.objects.all()")
print("      serializer_class = ArticleSerializer")
print("  router = DefaultRouter()")
print("  router.register('articles', ArticleViewSet)")
''',

    757: r'''# In production: from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# class ArticleViewSet(ModelViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
# This simulation demonstrates Django REST API authentication

class Token:
    """Simulates API token"""
    def __init__(self, key, user):
        self.key = key
        self.user = user

    def __repr__(self):
        return f"<Token: {self.key[:20]}... for {self.user}>"

class User:
    """User model"""
    def __init__(self, username, is_staff=False):
        self.username = username
        self.is_staff = is_staff

    def __repr__(self):
        return f"<User: {self.username}>"

class Authentication:
    """Base authentication class"""
    def authenticate(self, request):
        """Authenticate request"""
        raise NotImplementedError

class TokenAuthentication(Authentication):
    """Simulates TokenAuthentication"""
    def __init__(self):
        self.tokens = {}

    def create_token(self, user):
        """Create token for user"""
        token_key = f"token_{user.username}_{len(self.tokens)}"
        token = Token(token_key, user)
        self.tokens[token_key] = user
        print(f"[Created] Token for {user.username}: {token_key}")
        return token

    def authenticate(self, request, token_string=None):
        """Authenticate request with token"""
        if not token_string:
            return None

        if token_string in self.tokens:
            user = self.tokens[token_string]
            print(f"[Authenticated] User: {user.username}")
            return user

        print(f"[Auth Failed] Invalid token")
        return None

class Permission:
    """Base permission class"""
    def has_permission(self, request, view):
        """Check permission"""
        raise NotImplementedError

class IsAuthenticated(Permission):
    """Simulates IsAuthenticated permission"""
    def has_permission(self, request, view):
        """Only allow authenticated users"""
        return hasattr(request, 'user') and request.user is not None

class IsAdminUser(Permission):
    """Simulates IsAdminUser permission"""
    def has_permission(self, request, view):
        """Only allow admin users"""
        return hasattr(request, 'user') and hasattr(request.user, 'is_staff') and request.user.is_staff

class HttpRequest:
    """Simulates HTTP request"""
    def __init__(self, token=None):
        self.token = token
        self.user = None
        self.headers = {}
        if token:
            self.headers['Authorization'] = f"Token {token}"

class APIView:
    """Simulates DRF APIView"""
    authentication_classes = []
    permission_classes = []

    def check_authentication(self, request):
        """Check authentication"""
        for auth_class in self.authentication_classes:
            auth = auth_class()
            user = auth.authenticate(request, request.token)
            if user:
                request.user = user
                return True
        return False

    def check_permissions(self, request):
        """Check permissions"""
        for perm_class in self.permission_classes:
            perm = perm_class()
            if not perm.has_permission(request, self):
                return False
        return True

    def dispatch(self, request):
        """Dispatch request with auth checks"""
        # Authenticate
        if self.authentication_classes:
            if not self.check_authentication(request):
                return {'error': 'Authentication failed', 'status': 401}

        # Check permissions
        if self.permission_classes:
            if not self.check_permissions(request):
                return {'error': 'Permission denied', 'status': 403}

        return self.get(request)

    def get(self, request):
        """Handle GET request"""
        return {'status': 'success'}

print("Django REST API Authentication - Simulation")
print("=" * 70)

# Create authentication backend
auth = TokenAuthentication()

# Create users
print("\n1. Create users:")
user_alice = User('alice')
user_bob = User('bob', is_staff=True)
print(f"   Created: {user_alice}")
print(f"   Created: {user_bob} (admin)")

# Create tokens
print("\n2. Generate API tokens:")
token_alice = auth.create_token(user_alice)
token_bob = auth.create_token(user_bob)

# Define protected API view
class ArticleListView(APIView):
    """Protected API endpoint"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return {
            'status': 'success',
            'data': [
                {'id': 1, 'title': 'Article 1'},
                {'id': 2, 'title': 'Article 2'}
            ],
            'user': request.user.username
        }

print("\n3. Access protected endpoint with valid token:")
request1 = HttpRequest(token=token_alice.key)
view = ArticleListView()
response = view.dispatch(request1)
print(f"   Response: {response}")

print("\n4. Access protected endpoint with invalid token:")
request2 = HttpRequest(token="invalid_token_xyz")
response = view.dispatch(request2)
print(f"   Response: {response}")

print("\n5. Access protected endpoint without token:")
request3 = HttpRequest()
response = view.dispatch(request3)
print(f"   Response: {response}")

# Admin-only view
class AdminView(APIView):
    """Admin-only endpoint"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        return {
            'status': 'success',
            'message': f'Admin panel for {request.user.username}',
            'data': {'users': 100, 'articles': 500}
        }

print("\n6. Access admin endpoint with admin token:")
request4 = HttpRequest(token=token_bob.key)
view_admin = AdminView()
# Manually set user for admin check
request4.user = user_bob
response = view_admin.dispatch(request4)
print(f"   Response: {response}")

print("\n7. Access admin endpoint with regular user token:")
request5 = HttpRequest(token=token_alice.key)
request5.user = user_alice
response = view_admin.dispatch(request5)
print(f"   Response: {response}")

print("\n" + "=" * 70)
print("Real Django REST Framework:")
print("  from rest_framework.authentication import TokenAuthentication")
print("  from rest_framework.permissions import IsAuthenticated, IsAdminUser")
print("  class ArticleViewSet(ModelViewSet):")
print("      authentication_classes = [TokenAuthentication]")
print("      permission_classes = [IsAuthenticated]")
print("  # Generate token:")
print("  from rest_framework.authtoken.models import Token")
print("  token = Token.objects.create(user=user)")
''',

    758: r'''# In production: from django.contrib.auth.views import PasswordResetView
# from django.contrib.auth.tokens import default_token_generator
# class PasswordResetView(View):
#     def post(self, request):
#         token = default_token_generator.make_token(user)
# This simulation demonstrates Django password reset flow

import uuid
import hashlib
from datetime import datetime, timedelta

class PasswordResetToken:
    """Simulates password reset token"""
    def __init__(self, user, expires_in=3600):
        self.user = user
        self.token = self._generate_token()
        self.created_at = datetime.now()
        self.expires_at = datetime.now() + timedelta(seconds=expires_in)
        self.used = False

    def _generate_token(self):
        """Generate secure token"""
        data = f"{self.user}_{datetime.now().isoformat()}_{uuid.uuid4()}"
        return hashlib.sha256(data.encode()).hexdigest()[:32]

    def is_valid(self):
        """Check if token is still valid"""
        if self.used:
            return False
        return datetime.now() < self.expires_at

    def __repr__(self):
        return f"<Token: {self.token[:10]}... for {self.user}>"

class User:
    """User model"""
    def __init__(self, username, email, password=''):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<User: {self.username}>"

class EmailBackend:
    """Simulates email sending"""
    def __init__(self):
        self.sent_emails = []

    def send_password_reset_email(self, user, token):
        """Send password reset email"""
        reset_url = f"http://example.com/password-reset/{token.token}/"
        email = {
            'to': user.email,
            'subject': 'Password Reset Request',
            'body': f"Click here to reset: {reset_url}",
            'token': token.token,
            'timestamp': datetime.now()
        }
        self.sent_emails.append(email)
        print(f"[Email Sent] To: {user.email}")
        print(f"  Reset Link: {reset_url}")
        return email

class PasswordResetView:
    """Simulates password reset flow"""
    def __init__(self):
        self.tokens = {}
        self.email_backend = EmailBackend()
        self.users = {}

    def register_user(self, username, email, password):
        """Register a user"""
        user = User(username, email, password)
        self.users[username] = user
        return user

    def request_password_reset(self, email):
        """Request password reset"""
        print(f"\n[Password Reset Request] Email: {email}")

        # Find user by email
        user = None
        for u in self.users.values():
            if u.email == email:
                user = u
                break

        if not user:
            print(f"  [Error] No user found with email: {email}")
            return None

        # Generate token
        token = PasswordResetToken(user.username)
        self.tokens[token.token] = token

        # Send email
        self.email_backend.send_password_reset_email(user, token)

        return token

    def reset_password(self, token_str, new_password):
        """Reset password using token"""
        print(f"\n[Password Reset Verification] Token: {token_str[:10]}...")

        if token_str not in self.tokens:
            print(f"  [Error] Invalid token")
            return False

        token = self.tokens[token_str]

        if not token.is_valid():
            print(f"  [Error] Token expired or already used")
            return False

        # Find user
        user = self.users.get(token.user)
        if not user:
            print(f"  [Error] User not found")
            return False

        # Update password
        user.password = new_password
        token.used = True
        print(f"  [Success] Password reset for {user.username}")
        return True

    def validate_token(self, token_str):
        """Validate token"""
        if token_str not in self.tokens:
            return False, "Invalid token"

        token = self.tokens[token_str]

        if not token.is_valid():
            return False, "Token expired"

        return True, "Token valid"

print("Django Password Reset Flow - Simulation")
print("=" * 70)

# Create password reset system
reset_system = PasswordResetView()

# Register users
print("\n1. Register users:")
user1 = reset_system.register_user('alice', 'alice@example.com', 'password123')
user2 = reset_system.register_user('bob', 'bob@example.com', 'secret456')
print(f"   Registered: {user1}")
print(f"   Registered: {user2}")

# Request password reset
print("\n2. User requests password reset:")
token1 = reset_system.request_password_reset('alice@example.com')

# Request with non-existent email
print("\n3. Request with non-existent email:")
token2 = reset_system.request_password_reset('unknown@example.com')

# Validate token
print("\n4. Validate reset token:")
is_valid, message = reset_system.validate_token(token1.token)
print(f"   Token: {token1.token[:15]}...")
print(f"   Valid: {is_valid}, Message: {message}")

# Reset password with valid token
print("\n5. Reset password with valid token:")
success = reset_system.reset_password(token1.token, 'newpassword789')

# Try to reuse token
print("\n6. Try to reuse token (should fail):")
success = reset_system.reset_password(token1.token, 'anotherpassword')

# Request another reset
print("\n7. Request new password reset for Bob:")
token3 = reset_system.request_password_reset('bob@example.com')

# Create expired token for demo
print("\n8. Validate expired token:")
expired_token = PasswordResetToken(user2.username, expires_in=0)
reset_system.tokens[expired_token.token] = expired_token
is_valid, message = reset_system.validate_token(expired_token.token)
print(f"   Valid: {is_valid}, Message: {message}")

# Show sent emails
print("\n9. Summary of sent emails:")
print(f"   Total emails sent: {len(reset_system.email_backend.sent_emails)}")
for i, email in enumerate(reset_system.email_backend.sent_emails, 1):
    print(f"   {i}. To: {email['to']}")
    print(f"      Subject: {email['subject']}")

print("\n" + "=" * 70)
print("Real Django:")
print("  from django.contrib.auth.views import PasswordResetView")
print("  from django.contrib.auth.tokens import default_token_generator")
print("  class PasswordResetView(View):")
print("      def post(self, request):")
print("          user = User.objects.get(email=request.POST['email'])")
print("          token = default_token_generator.make_token(user)")
print("          send_email(user.email, token)")
print("  # User clicks link:")
print("  user.set_password(new_password)")
print("  user.save()")
''',

    759: r'''# In production: from django.utils.decorators import middleware_decorator
# class CustomMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#     def __call__(self, request):
#         # process_request
#         response = self.get_response(request)
#         # process_response
#         return response
# This simulation demonstrates Django middleware

from datetime import datetime

class HttpRequest:
    """Simulates Django HttpRequest"""
    def __init__(self, path='/', method='GET'):
        self.path = path
        self.method = method
        self.headers = {}
        self.user = None
        self.session = {}
        self.custom_data = {}
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"<HttpRequest: {self.method} {self.path}>"

class HttpResponse:
    """Simulates Django HttpResponse"""
    def __init__(self, content='', status=200):
        self.content = content
        self.status_code = status
        self.headers = {}

    def __repr__(self):
        return f"<HttpResponse: status {self.status_code}>"

class Middleware:
    """Base middleware class"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Called for each request"""
        # process_request
        request = self.process_request(request)
        if request is None:
            return HttpResponse('Request blocked', 403)

        # Call next middleware/view
        response = self.get_response(request)

        # process_response
        response = self.process_response(request, response)

        return response

    def process_request(self, request):
        """Called before view"""
        return request

    def process_response(self, request, response):
        """Called after view"""
        return response

class LoggingMiddleware(Middleware):
    """Logs all requests and responses"""
    def process_request(self, request):
        print(f"[Request] {request.method} {request.path}")
        request.custom_data['start_time'] = datetime.now()
        return request

    def process_response(self, request, response):
        duration = (datetime.now() - request.custom_data.get('start_time', datetime.now())).total_seconds()
        print(f"[Response] Status: {response.status_code}, Duration: {duration:.3f}s")
        response.headers['X-Process-Time'] = str(duration)
        return response

class AuthenticationMiddleware(Middleware):
    """Authenticate user from session"""
    def process_request(self, request):
        # Check for user in session
        if 'user_id' in request.session:
            request.user = f"User{request.session['user_id']}"
            print(f"[Auth] Authenticated as: {request.user}")
        else:
            request.user = 'AnonymousUser'
            print(f"[Auth] Anonymous user")
        return request

class SecurityHeadersMiddleware(Middleware):
    """Add security headers to response"""
    def process_response(self, request, response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        print(f"[Security] Added security headers")
        return response

class RateLimitMiddleware(Middleware):
    """Simulate rate limiting"""
    def __init__(self, get_response):
        super().__init__(get_response)
        self.request_counts = {}

    def process_request(self, request):
        # Simple rate limiting by IP (simulated)
        ip = request.headers.get('X-Forwarded-For', '127.0.0.1')
        count = self.request_counts.get(ip, 0)

        if count > 10:
            print(f"[RateLimit] Too many requests from {ip}")
            return None

        self.request_counts[ip] = count + 1
        print(f"[RateLimit] Request {count + 1} from {ip}")
        return request

# Mock view function
def view(request):
    """Simulated view function"""
    return HttpResponse(f"Response for {request.path}", 200)

print("Django Middleware - Simulation")
print("=" * 70)

# Build middleware chain
print("\n1. Build middleware chain:")
print("   LoggingMiddleware")
print("   ↓")
print("   AuthenticationMiddleware")
print("   ↓")
print("   SecurityHeadersMiddleware")
print("   ↓")
print("   RateLimitMiddleware")
print("   ↓")
print("   view()")

# Create middleware stack
security_mw = SecurityHeadersMiddleware(view)
auth_mw = AuthenticationMiddleware(security_mw)
rate_limit_mw = RateLimitMiddleware(auth_mw)
logging_mw = LoggingMiddleware(rate_limit_mw)

# Process requests
print("\n2. Process authenticated request:")
request1 = HttpRequest('/api/articles/', 'GET')
request1.session['user_id'] = 1
request1.headers['X-Forwarded-For'] = '192.168.1.1'
response1 = logging_mw(request1)
print(f"   Result: {response1}")
print(f"   Headers: {response1.headers}")

print("\n3. Process another request:")
request2 = HttpRequest('/api/products/', 'POST')
request2.headers['X-Forwarded-For'] = '192.168.1.2'
response2 = logging_mw(request2)
print(f"   Result: {response2}")

print("\n4. Process multiple rapid requests (rate limiting):")
for i in range(3):
    request = HttpRequest(f'/api/endpoint/{i}', 'GET')
    request.headers['X-Forwarded-For'] = '192.168.1.3'
    response = logging_mw(request)

print("\n5. Process request that exceeds rate limit:")
# Build new chain to reset count
rate_limit_mw2 = RateLimitMiddleware(auth_mw)
logging_mw2 = LoggingMiddleware(rate_limit_mw2)

# Send many requests
print("   Sending 12 requests from same IP...")
for i in range(12):
    request = HttpRequest(f'/api/endpoint/{i}', 'GET')
    request.headers['X-Forwarded-For'] = '192.168.2.1'
    if i < 11:
        response = logging_mw2(request)
    else:
        response = logging_mw2(request)
        if response:
            print(f"   Final request: {response}")
        else:
            print(f"   Final request: Blocked by rate limit")

print("\n" + "=" * 70)
print("Real Django:")
print("  class CustomMiddleware:")
print("      def __init__(self, get_response):")
print("          self.get_response = get_response")
print("      def __call__(self, request):")
print("          # process_request")
print("          response = self.get_response(request)")
print("          # process_response")
print("          return response")
print("  # In settings.py:")
print("  MIDDLEWARE = [")
print("      'myapp.middleware.CustomMiddleware',")
print("  ]")
''',
}

def update_lessons(lessons_file):
    """Update lessons JSON file with new simulations"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    updated = []
    for lesson in lessons:
        if lesson.get('id') in DJANGO_BATCH_4A:
            lesson['fullSolution'] = DJANGO_BATCH_4A[lesson['id']]
            updated.append(lesson['id'])
            print(f"Updated lesson {lesson['id']}: {lesson.get('title', 'Unknown')}")

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated

def main():
    """Main execution"""
    lessons_file = r'c:\devbootLLM-app\public\lessons-python.json'
    try:
        updated = update_lessons(lessons_file)
        print(f"\n{'=' * 70}")
        print(f"Successfully updated {len(updated)} Django lessons (batch 4a)")
        print(f"Lesson IDs: {updated}")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
