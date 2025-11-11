#!/usr/bin/env python3
"""Enhance Phase 2 Python lessons to match original quality standards (4000-5000 char tutorials/examples)"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

# Enhanced Flask Advanced tutorials and examples
flask_enhanced = {
    783: {
        "tutorial": """# Flask Blueprints for Large Applications

Blueprints are Flask's solution for organizing large applications into modular components. They allow you to structure your application as a collection of reusable components, each with its own views, templates, and static files.

## Why Use Blueprints?

✓ **Modularity**: Break large apps into manageable pieces
✓ **Reusability**: Create components that can be used across projects
✓ **Team Development**: Different teams can work on different blueprints
✓ **Clean Architecture**: Separate concerns and improve maintainability

## Basic Blueprint Structure

```python
# app/auth/routes.py
from flask import Blueprint, render_template, redirect, url_for

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login
        return redirect(url_for('main.index'))
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    # Handle logout
    return redirect(url_for('auth.login'))
```

## Organizing with Blueprints

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from app.auth import auth_bp
    from app.blog import blog_bp
    from app.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp, url_prefix='/blog')
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app
```

## Project Structure

```
myapp/
├── app/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── forms.py
│   │   └── templates/
│   ├── blog/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── models.py
│   └── api/
│       ├── __init__.py
│       └── routes.py
├── config.py
└── run.py
```

## Advanced Blueprint Features

### Blueprint-Specific Templates

```python
# Blueprints can have their own template folders
blog_bp = Blueprint('blog', __name__,
                   template_folder='templates',
                   static_folder='static')

@blog_bp.route('/post/<int:id>')
def view_post(id):
    # This looks in app/blog/templates/
    return render_template('post.html', post_id=id)
```

### Blueprint Error Handlers

```python
@blog_bp.errorhandler(404)
def blog_not_found(error):
    return render_template('blog/404.html'), 404

@blog_bp.errorhandler(500)
def blog_server_error(error):
    return render_template('blog/500.html'), 500
```

## Real-World Example: E-commerce Application

```python
# app/products/__init__.py
from flask import Blueprint

products_bp = Blueprint('products', __name__)

from app.products import routes

# app/products/routes.py
from flask import render_template, request, jsonify
from app.products import products_bp
from app.models import Product

@products_bp.route('/')
def list_products():
    products = Product.query.all()
    return render_template('products/list.html', products=products)

@products_bp.route('/<int:id>')
def view_product(id):
    product = Product.query.get_or_404(id)
    return render_template('products/detail.html', product=product)

@products_bp.route('/search')
def search_products():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.contains(query)).all()
    return jsonify([p.to_dict() for p in products])
```

## Blueprint with Dependency Injection

```python
# app/api/__init__.py
from flask import Blueprint

def create_api_blueprint(db, cache):
    api_bp = Blueprint('api', __name__)

    @api_bp.route('/users')
    def get_users():
        # Blueprint has access to db and cache
        users = cache.get('users')
        if users is None:
            users = db.session.query(User).all()
            cache.set('users', users, timeout=300)
        return jsonify([u.to_dict() for u in users])

    return api_bp
```

## Best Practices

✓ **Use url_prefix**: Keep URLs organized
✓ **Group related functionality**: Auth, blog, API should be separate blueprints
✓ **Avoid circular imports**: Import blueprints in create_app(), not at module level
✓ **Use before_request**: Add blueprint-specific middleware
✓ **Document blueprint APIs**: Make it clear what each blueprint provides

## Common Pitfalls

✗ **Circular imports**: Import views at the end of __init__.py
✗ **Hardcoded URLs**: Always use url_for('blueprint.view')
✗ **Missing url_prefix**: Can lead to URL conflicts
✗ **Global state**: Pass dependencies explicitly to blueprints

## Production Pattern: Multi-Tenant Application

```python
# Each tenant gets their own blueprint instance
def create_tenant_blueprint(tenant_config):
    tenant_bp = Blueprint(
        f'tenant_{tenant_config.id}',
        __name__,
        subdomain=tenant_config.subdomain
    )

    @tenant_bp.before_request
    def load_tenant_context():
        g.tenant = tenant_config

    @tenant_bp.route('/')
    def tenant_home():
        return render_template('tenant/home.html', tenant=g.tenant)

    return tenant_bp

# Register tenant blueprints dynamically
app = Flask(__name__)
for tenant in Tenant.query.all():
    app.register_blueprint(create_tenant_blueprint(tenant))
```

Blueprints are essential for building maintainable Flask applications at scale. Used by: Reddit, Pinterest, Lyft.""",
        "additionalExamples": """# Example 1: Admin Blueprint with Authentication
from flask import Blueprint, render_template, redirect, url_for, flash
from functools import wraps

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    stats = {
        'users': User.query.count(),
        'posts': Post.query.count(),
        'revenue': Order.query.with_entities(func.sum(Order.total)).scalar()
    }
    return render_template('admin/dashboard.html', stats=stats)

@admin_bp.route('/users')
@admin_required
def manage_users():
    users = User.query.paginate(page=request.args.get('page', 1, type=int), per_page=50)
    return render_template('admin/users.html', users=users)

# Output: Admin blueprint with protected routes

# Example 2: API Blueprint with Versioning
from flask import Blueprint, jsonify, request

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

# V1 endpoints
@api_v1.route('/users')
def get_users_v1():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])

# V2 endpoints with enhanced data
@api_v2.route('/users')
def get_users_v2():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'created_at': u.created_at.isoformat(),
        'profile': u.profile.to_dict() if u.profile else None
    } for u in users])

# Register both versions
app.register_blueprint(api_v1)
app.register_blueprint(api_v2)

# Output: Multiple API versions running simultaneously

# Example 3: Microservices-Style Blueprint Organization
from flask import Blueprint, current_app

# Payment service blueprint
payments_bp = Blueprint('payments', __name__)

@payments_bp.before_request
def before_payment_request():
    current_app.logger.info(f'Payment request: {request.endpoint}')

@payments_bp.route('/charge', methods=['POST'])
def charge():
    amount = request.json.get('amount')
    token = request.json.get('token')
    # Process payment with Stripe
    return jsonify({'status': 'success', 'charge_id': 'ch_123'})

# Notification service blueprint
notifications_bp = Blueprint('notifications', __name__)

@notifications_bp.route('/send', methods=['POST'])
def send_notification():
    user_id = request.json.get('user_id')
    message = request.json.get('message')
    # Send via email, SMS, push
    return jsonify({'status': 'sent'})

# Output: Service-oriented architecture with Flask

# Example 4: RESTful Resource Blueprint
from flask import Blueprint, request, jsonify

def create_resource_blueprint(name, model):
    \"\"\"Factory function to create RESTful blueprints\"\"\"
    bp = Blueprint(name, __name__, url_prefix=f'/{name}')

    @bp.route('/', methods=['GET'])
    def list_resources():
        items = model.query.all()
        return jsonify([item.to_dict() for item in items])

    @bp.route('/', methods=['POST'])
    def create_resource():
        data = request.get_json()
        item = model(**data)
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict()), 201

    @bp.route('/<int:id>', methods=['GET'])
    def get_resource(id):
        item = model.query.get_or_404(id)
        return jsonify(item.to_dict())

    @bp.route('/<int:id>', methods=['PUT'])
    def update_resource(id):
        item = model.query.get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(item, key, value)
        db.session.commit()
        return jsonify(item.to_dict())

    @bp.route('/<int:id>', methods=['DELETE'])
    def delete_resource(id):
        item = model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204

    return bp

# Create blueprints for different models
app.register_blueprint(create_resource_blueprint('articles', Article))
app.register_blueprint(create_resource_blueprint('products', Product))
app.register_blueprint(create_resource_blueprint('orders', Order))

# Output: DRY RESTful API with blueprint factory

# Example 5: Plugin System with Blueprints
import importlib
import os

def load_plugins(app):
    \"\"\"Dynamically load blueprint plugins from plugins directory\"\"\"
    plugins_dir = 'app/plugins'

    for plugin_name in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin_name)

        if os.path.isdir(plugin_path) and os.path.exists(f'{plugin_path}/__init__.py'):
            try:
                # Import the plugin module
                module = importlib.import_module(f'app.plugins.{plugin_name}')

                # Get the blueprint
                if hasattr(module, 'blueprint'):
                    app.register_blueprint(module.blueprint)
                    app.logger.info(f'Loaded plugin: {plugin_name}')
            except Exception as e:
                app.logger.error(f'Failed to load plugin {plugin_name}: {e}')

# In app/__init__.py
app = create_app()
load_plugins(app)

# Output: Extensible application with plugin architecture

print("Flask Blueprints examples loaded - production-ready modular architecture")"""
    },
    784: {
        "tutorial": """# Application Factory Pattern in Flask

The Application Factory pattern is a best practice for creating Flask applications. Instead of creating the app at the module level, you use a function that returns a configured Flask instance. This enables testing, multiple configurations, and better application structure.

## Why Use the Factory Pattern?

✓ **Multiple Configurations**: Easy to create app instances with different configs (dev, test, prod)
✓ **Testing**: Create isolated app instances for each test
✓ **Delayed Configuration**: Configure extensions after app creation
✓ **No Circular Imports**: Extensions can be imported at module level
✓ **Blueprint Registration**: Register blueprints cleanly

## Basic Application Factory

```python
# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions (don't bind to app yet)
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name='development'):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    from app.auth import auth_bp
    from app.main import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
```

## Configuration Classes

```python
# config.py
import os

class Config:
    \"\"\"Base configuration\"\"\"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    \"\"\"Development configuration\"\"\"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    \"\"\"Production configuration\"\"\"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        # Production-specific setup
        import logging
        from logging.handlers import RotatingFileHandler

        file_handler = RotatingFileHandler('logs/app.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

class TestingConfig(Config):
    \"\"\"Testing configuration\"\"\"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
```

## Running the Application

```python
# run.py
from app import create_app
import os

app = create_app(os.environ.get('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run()
```

## Advanced Factory with Extension Configuration

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_caching import Cache
from flask_cors import CORS

# Extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
cache = Cache()

def create_app(config_name='development'):
    app = Flask(__name__)

    # Load config
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Initialize all extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    cache.init_app(app, config={'CACHE_TYPE': 'redis'})
    CORS(app)

    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'

    # Register blueprints
    from app.auth import auth_bp
    from app.main import main_bp
    from app.api import api_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Register error handlers
    register_error_handlers(app)

    # Register CLI commands
    register_commands(app)

    # Initialize production config
    config_class = app.config.get('CONFIG_CLASS')
    if hasattr(config_class, 'init_app'):
        config_class.init_app(app)

    return app

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'error': 'Internal server error'}, 500

def register_commands(app):
    @app.cli.command()
    def init_db():
        \"\"\"Initialize the database.\"\"\"
        db.create_all()
        print('Database initialized')
```

## Testing with Factory Pattern

```python
# tests/conftest.py
import pytest
from app import create_app, db

@pytest.fixture
def app():
    \"\"\"Create application for testing\"\"\"
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    \"\"\"Test client\"\"\"
    return app.test_client()

# tests/test_auth.py
def test_login(client):
    response = client.post('/auth/login', data={
        'username': 'test',
        'password': 'test'
    })
    assert response.status_code == 200
```

## Real-World Example: Multi-Tenant SaaS

```python
def create_app(tenant_id=None):
    app = Flask(__name__)

    # Load base config
    app.config.from_object('config.BaseConfig')

    # Load tenant-specific config
    if tenant_id:
        tenant = Tenant.query.get(tenant_id)
        app.config['TENANT_ID'] = tenant.id
        app.config['TENANT_NAME'] = tenant.name
        app.config['SQLALCHEMY_DATABASE_URI'] = tenant.database_uri

    db.init_app(app)

    # Tenant-specific middleware
    @app.before_request
    def load_tenant_context():
        g.tenant_id = app.config.get('TENANT_ID')

    return app

# Create apps for different tenants
tenant_1_app = create_app(tenant_id=1)
tenant_2_app = create_app(tenant_id=2)
```

## Production Pattern: Environment-Based Configuration

```python
import os
from dotenv import load_dotenv

def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)

    # Configure from environment
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    app.config['DATABASE_URL'] = os.environ['DATABASE_URL']
    app.config['REDIS_URL'] = os.environ.get('REDIS_URL', 'redis://localhost:6379')
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'localhost')

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app, config={
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_URL': app.config['REDIS_URL']
    })

    # Production: Set up logging to external service
    if not app.debug:
        import sentry_sdk
        sentry_sdk.init(dsn=os.environ.get('SENTRY_DSN'))

    return app
```

## Best Practices

✓ **Use environment variables**: Never hardcode secrets
✓ **Separate configs**: Dev, test, prod should be distinct
✓ **Initialize extensions properly**: Use init_app() pattern
✓ **Register blueprints in factory**: Keep imports inside function
✓ **Test multiple configs**: Ensure all configurations work

The factory pattern is the standard for professional Flask applications. Used by: Flask official docs, Flask-RESTful, Flask-Admin.""",
        "additionalExamples": """# Example 1: Factory with Feature Flags
from flask import Flask
import os

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Feature flags
    app.config['FEATURE_NEW_UI'] = os.environ.get('FEATURE_NEW_UI', 'false') == 'true'
    app.config['FEATURE_ANALYTICS'] = os.environ.get('FEATURE_ANALYTICS', 'false') == 'true'

    @app.context_processor
    def inject_features():
        return {
            'feature_new_ui': app.config['FEATURE_NEW_UI'],
            'feature_analytics': app.config['FEATURE_ANALYTICS']
        }

    # Conditional blueprint registration
    if app.config['FEATURE_ANALYTICS']:
        from app.analytics import analytics_bp
        app.register_blueprint(analytics_bp)

    return app

# Usage: FEATURE_NEW_UI=true python run.py

# Example 2: Factory with Dependency Injection
from flask import Flask

class ServiceContainer:
    def __init__(self):
        self.email_service = None
        self.payment_service = None
        self.storage_service = None

def create_app(config_name='development', services=None):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Inject services
    if services is None:
        services = ServiceContainer()
        services.email_service = SendGridEmailService()
        services.payment_service = StripePaymentService()
        services.storage_service = S3StorageService()

    app.services = services

    @app.route('/send-email', methods=['POST'])
    def send_email():
        app.services.email_service.send(
            to=request.json['to'],
            subject=request.json['subject'],
            body=request.json['body']
        )
        return {'status': 'sent'}

    return app

# Testing with mock services
def test_email():
    mock_services = ServiceContainer()
    mock_services.email_service = MockEmailService()
    app = create_app('testing', services=mock_services)
    # Test with mocked dependencies

# Example 3: Factory with Dynamic Blueprint Loading
import importlib
import pkgutil

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Auto-discover and register all blueprints
    import app.blueprints
    for importer, modname, ispkg in pkgutil.iter_modules(app.blueprints.__path__):
        module = importlib.import_module(f'app.blueprints.{modname}')
        if hasattr(module, 'bp'):
            app.register_blueprint(module.bp)
            app.logger.info(f'Registered blueprint: {modname}')

    return app

# app/blueprints/users.py
from flask import Blueprint
bp = Blueprint('users', __name__)

@bp.route('/users')
def list_users():
    return {'users': []}

# app/blueprints/posts.py
from flask import Blueprint
bp = Blueprint('posts', __name__)

@bp.route('/posts')
def list_posts():
    return {'posts': []}

# Output: All blueprints automatically discovered and registered

# Example 4: Factory with Health Checks and Monitoring
from flask import Flask, jsonify
import psutil
import time

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Store app start time
    app.start_time = time.time()

    # Health check endpoint
    @app.route('/health')
    def health_check():
        uptime = time.time() - app.start_time

        # Check database connection
        try:
            db.session.execute('SELECT 1')
            db_status = 'healthy'
        except Exception as e:
            db_status = f'unhealthy: {str(e)}'

        # Check Redis connection
        try:
            cache.get('health_check')
            cache_status = 'healthy'
        except Exception as e:
            cache_status = f'unhealthy: {str(e)}'

        return jsonify({
            'status': 'healthy',
            'uptime_seconds': int(uptime),
            'database': db_status,
            'cache': cache_status,
            'memory_usage_mb': psutil.Process().memory_info().rss / 1024 / 1024
        })

    # Readiness check for Kubernetes
    @app.route('/ready')
    def readiness():
        # Check if app is ready to serve traffic
        if not db.engine:
            return jsonify({'status': 'not ready'}), 503
        return jsonify({'status': 'ready'})

    return app

# Example 5: Factory with Request Context and Logging
from flask import Flask, g, request
import uuid
import logging

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name.capitalize()}Config')

    # Configure structured logging
    logging.basicConfig(
        format='%(asctime)s %(levelname)s [%(request_id)s] %(message)s',
        level=logging.INFO
    )

    @app.before_request
    def before_request():
        # Add request ID for tracing
        g.request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))
        g.start_time = time.time()

        app.logger.info(f'Request started: {request.method} {request.path}',
                       extra={'request_id': g.request_id})

    @app.after_request
    def after_request(response):
        duration = time.time() - g.start_time

        app.logger.info(
            f'Request completed: {response.status_code} in {duration:.3f}s',
            extra={'request_id': g.request_id}
        )

        # Add request ID to response headers
        response.headers['X-Request-ID'] = g.request_id
        response.headers['X-Response-Time'] = f'{duration:.3f}s'

        return response

    @app.errorhandler(Exception)
    def handle_exception(e):
        app.logger.error(f'Unhandled exception: {str(e)}',
                        extra={'request_id': g.request_id},
                        exc_info=True)
        return {'error': 'Internal server error', 'request_id': g.request_id}, 500

    return app

print("Application factory examples loaded - production-ready architecture")"""
    }
}

# Load lessons
print("Loading Python lessons...")
py_lessons = load_lessons('public/lessons-python.json')
print(f"Current: {len(py_lessons)} lessons")

# Enhance Flask Advanced lessons (IDs 783-792)
print("\nEnhancing Flask Advanced lessons (783-792)...")
for lesson_id in range(783, 785):  # Starting with first 2 for now
    if lesson_id in flask_enhanced:
        for lesson in py_lessons:
            if lesson['id'] == lesson_id:
                lesson['tutorial'] = flask_enhanced[lesson_id]['tutorial']
                lesson['additionalExamples'] = flask_enhanced[lesson_id]['additionalExamples']
                print(f"  Enhanced lesson {lesson_id}: {lesson['title']}")
                print(f"    Tutorial: {len(lesson['tutorial'])} chars")
                print(f"    Examples: {len(lesson['additionalExamples'])} chars")

# Save
save_lessons('public/lessons-python.json', py_lessons)
print(f"\nPhase 2 Python lessons enhanced!")
print("First 2 Flask lessons upgraded to production quality")
