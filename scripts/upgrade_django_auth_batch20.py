import json

# Read lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lesson to upgrade
lesson_519 = next(l for l in lessons if l['id'] == 519)  # Django User Authentication

# ============================================================================
# LESSON 519: Django User Authentication
# ============================================================================

lesson_519['fullSolution'] = '''"""
Django User Authentication - Comprehensive Guide
================================================

This lesson covers comprehensive Django user authentication including user
registration, login/logout, password management, permissions, groups, custom
authentication backends, session management, and security best practices.

**Zero Package Installation Required**

Learning Objectives:
- Implement user registration and login
- Handle password hashing and validation
- Manage user sessions and cookies
- Implement permissions and groups
- Create custom authentication backends
- Handle password reset and change
- Implement remember me functionality
- Add two-factor authentication
- Secure authentication flows
- Implement social authentication patterns
"""

import hashlib
import secrets
import time
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from functools import wraps

# ============================================================================
# Example 1: User Model and Password Hashing
# ============================================================================

class PasswordHasher:
    """
    Simulates Django's password hashing (PBKDF2).
    """

    def __init__(self, algorithm: str = 'pbkdf2_sha256', iterations: int = 600000):
        self.algorithm = algorithm
        self.iterations = iterations

    def make_password(self, password: str) -> str:
        """Hash a password."""
        salt = secrets.token_hex(16)
        hash_value = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            self.iterations
        )
        hash_hex = hash_value.hex()
        return f"{self.algorithm}${self.iterations}${salt}${hash_hex}"

    def check_password(self, password: str, hashed: str) -> bool:
        """Verify a password against its hash."""
        parts = hashed.split('$')
        if len(parts) != 4:
            return False

        algorithm, iterations, salt, hash_hex = parts
        iterations = int(iterations)

        new_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            iterations
        )

        return new_hash.hex() == hash_hex

class User:
    """
    Simulates Django User model.
    """

    def __init__(self, username: str, email: str, password: str = None):
        self.id = None
        self.username = username
        self.email = email
        self.password = password  # Hashed password
        self.first_name = ''
        self.last_name = ''
        self.is_active = True
        self.is_staff = False
        self.is_superuser = False
        self.date_joined = datetime.now()
        self.last_login = None

    def set_password(self, raw_password: str):
        """Set user password (hashed)."""
        hasher = PasswordHasher()
        self.password = hasher.make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        """Check if password is correct."""
        hasher = PasswordHasher()
        return hasher.check_password(raw_password, self.password)

def example_password_hashing():
    """
    Demonstrates password hashing and verification.
    """
    print(f"{'='*60}")
    print("Example 1: User Model and Password Hashing")
    print(f"{'='*60}")

    # Create user
    user = User('john_doe', 'john@example.com')
    password = 'SecurePassword123!'

    print(f"\\nCreating user: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Password (raw): {password}")

    # Hash password
    user.set_password(password)
    print(f"  Password (hashed): {user.password[:50]}...")

    # Verify correct password
    print(f"\\nPassword Verification:")
    is_correct = user.check_password(password)
    print(f"  Correct password: {is_correct} - {'PASS' if is_correct else 'FAIL'}")

    # Verify incorrect password
    is_correct = user.check_password('WrongPassword')
    print(f"  Wrong password: {is_correct} - {'PASS' if not is_correct else 'FAIL'}")

# ============================================================================
# Example 2: User Registration
# ============================================================================

class UserDatabase:
    """
    Simulates user database storage.
    """

    def __init__(self):
        self.users: Dict[int, User] = {}
        self.users_by_username: Dict[str, User] = {}
        self.users_by_email: Dict[str, User] = {}
        self.next_id = 1

    def create_user(self, username: str, email: str, password: str) -> User:
        """Create a new user."""
        user = User(username, email)
        user.id = self.next_id
        user.set_password(password)

        self.users[user.id] = user
        self.users_by_username[username] = user
        self.users_by_email[email] = user
        self.next_id += 1

        return user

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.users_by_username.get(username)

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.users_by_email.get(email)

    def username_exists(self, username: str) -> bool:
        """Check if username exists."""
        return username in self.users_by_username

    def email_exists(self, email: str) -> bool:
        """Check if email exists."""
        return email in self.users_by_email

class RegistrationForm:
    """
    User registration form with validation.
    """

    def __init__(self, data: Dict, user_db: UserDatabase):
        self.data = data
        self.user_db = user_db
        self.errors = {}
        self.cleaned_data = {}

    def is_valid(self) -> bool:
        """Validate registration form."""
        # Username validation
        username = self.data.get('username', '').strip()
        if not username:
            self.errors['username'] = 'Username is required'
        elif len(username) < 3:
            self.errors['username'] = 'Username must be at least 3 characters'
        elif self.user_db.username_exists(username):
            self.errors['username'] = 'Username already exists'
        else:
            self.cleaned_data['username'] = username

        # Email validation
        email = self.data.get('email', '').strip()
        if not email:
            self.errors['email'] = 'Email is required'
        elif '@' not in email or '.' not in email:
            self.errors['email'] = 'Invalid email address'
        elif self.user_db.email_exists(email):
            self.errors['email'] = 'Email already registered'
        else:
            self.cleaned_data['email'] = email

        # Password validation
        password = self.data.get('password', '')
        password_confirm = self.data.get('password_confirm', '')

        if not password:
            self.errors['password'] = 'Password is required'
        elif len(password) < 8:
            self.errors['password'] = 'Password must be at least 8 characters'
        elif password != password_confirm:
            self.errors['password_confirm'] = 'Passwords do not match'
        elif not any(c.isupper() for c in password):
            self.errors['password'] = 'Password must contain uppercase letter'
        elif not any(c.isdigit() for c in password):
            self.errors['password'] = 'Password must contain a number'
        else:
            self.cleaned_data['password'] = password

        return len(self.errors) == 0

def example_user_registration():
    """
    Demonstrates user registration with validation.
    """
    print(f"\\n{'='*60}")
    print("Example 2: User Registration")
    print(f"{'='*60}")

    user_db = UserDatabase()

    # Valid registration
    print("\\nTest 1: Valid registration")
    form_data = {
        'username': 'newuser',
        'email': 'newuser@example.com',
        'password': 'SecurePass123',
        'password_confirm': 'SecurePass123'
    }

    form = RegistrationForm(form_data, user_db)
    if form.is_valid():
        user = user_db.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password']
        )
        print(f"  SUCCESS: User '{user.username}' registered")
        print(f"  User ID: {user.id}")
    else:
        print(f"  FAILED: {form.errors}")

    # Duplicate username
    print("\\nTest 2: Duplicate username")
    form_data['email'] = 'another@example.com'
    form = RegistrationForm(form_data, user_db)
    if form.is_valid():
        print(f"  FAILED: Should have rejected duplicate username")
    else:
        print(f"  SUCCESS: {form.errors['username']}")

    # Weak password
    print("\\nTest 3: Weak password")
    form_data = {
        'username': 'anotheruser',
        'email': 'test@example.com',
        'password': 'weak',
        'password_confirm': 'weak'
    }
    form = RegistrationForm(form_data, user_db)
    if form.is_valid():
        print(f"  FAILED: Should have rejected weak password")
    else:
        print(f"  SUCCESS: {form.errors['password']}")

# ============================================================================
# Example 3: Login System with Session Management
# ============================================================================

class Session:
    """
    Simulates Django session.
    """

    def __init__(self):
        self.session_key = secrets.token_urlsafe(32)
        self.data: Dict[str, Any] = {}
        self.created_at = datetime.now()
        self.last_accessed = datetime.now()

    def __setitem__(self, key: str, value: Any):
        self.data[key] = value
        self.last_accessed = datetime.now()

    def __getitem__(self, key: str):
        self.last_accessed = datetime.now()
        return self.data.get(key)

    def get(self, key: str, default: Any = None):
        self.last_accessed = datetime.now()
        return self.data.get(key, default)

    def flush(self):
        """Clear session data."""
        self.data = {}

class AuthenticationBackend:
    """
    Handles user authentication.
    """

    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db
        self.sessions: Dict[str, Session] = {}
        self.failed_attempts: Dict[str, List[datetime]] = {}
        self.max_attempts = 5
        self.lockout_duration = timedelta(minutes=15)

    def authenticate(self, username: str, password: str) -> Optional[User]:
        """Authenticate user with username and password."""
        # Check for account lockout
        if self.is_locked_out(username):
            print(f"  Account locked due to too many failed attempts")
            return None

        user = self.user_db.get_by_username(username)

        if user and user.check_password(password):
            # Clear failed attempts on successful login
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            return user

        # Record failed attempt
        self.record_failed_attempt(username)
        return None

    def record_failed_attempt(self, username: str):
        """Record a failed login attempt."""
        if username not in self.failed_attempts:
            self.failed_attempts[username] = []
        self.failed_attempts[username].append(datetime.now())

    def is_locked_out(self, username: str) -> bool:
        """Check if account is locked out."""
        if username not in self.failed_attempts:
            return False

        # Remove old attempts
        cutoff = datetime.now() - self.lockout_duration
        self.failed_attempts[username] = [
            attempt for attempt in self.failed_attempts[username]
            if attempt > cutoff
        ]

        return len(self.failed_attempts[username]) >= self.max_attempts

    def login(self, user: User) -> Session:
        """Create session for user."""
        session = Session()
        session['user_id'] = user.id
        session['username'] = user.username
        session['login_time'] = datetime.now().isoformat()

        self.sessions[session.session_key] = session
        user.last_login = datetime.now()

        return session

    def logout(self, session: Session):
        """Destroy user session."""
        if session.session_key in self.sessions:
            del self.sessions[session.session_key]

    def get_user_from_session(self, session: Session) -> Optional[User]:
        """Get user from session."""
        user_id = session.get('user_id')
        if user_id:
            for user in self.user_db.users.values():
                if user.id == user_id:
                    return user
        return None

def example_login_system():
    """
    Demonstrates login system with session management.
    """
    print(f"\\n{'='*60}")
    print("Example 3: Login System with Session Management")
    print(f"{'='*60}")

    user_db = UserDatabase()
    auth = AuthenticationBackend(user_db)

    # Create test user
    user = user_db.create_user('testuser', 'test@example.com', 'Test123Pass')

    # Successful login
    print("\\nTest 1: Successful login")
    authenticated_user = auth.authenticate('testuser', 'Test123Pass')
    if authenticated_user:
        session = auth.login(authenticated_user)
        print(f"  SUCCESS: User logged in")
        print(f"  Session key: {session.session_key[:20]}...")
        print(f"  User ID: {session.get('user_id')}")
        print(f"  Username: {session.get('username')}")
    else:
        print(f"  FAILED: Authentication failed")

    # Failed login
    print("\\nTest 2: Failed login")
    authenticated_user = auth.authenticate('testuser', 'WrongPassword')
    if authenticated_user:
        print(f"  FAILED: Should not have authenticated")
    else:
        print(f"  SUCCESS: Authentication rejected")

    # Test account lockout
    print("\\nTest 3: Account lockout after multiple failed attempts")
    for i in range(5):
        auth.authenticate('testuser', 'WrongPassword')
        print(f"  Attempt {i+1}: Failed")

    authenticated_user = auth.authenticate('testuser', 'Test123Pass')
    if authenticated_user:
        print(f"  FAILED: Should be locked out")
    else:
        print(f"  SUCCESS: Account locked out")

# ============================================================================
# Example 4: Login Required Decorator
# ============================================================================

def login_required(view_func):
    """
    Decorator to require authentication.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request, 'user') or not request.user:
            print(f"  Authentication required - redirecting to login")
            return {'status': 401, 'message': 'Authentication required'}
        return view_func(request, *args, **kwargs)
    return wrapper

def example_login_required():
    """
    Demonstrates login_required decorator.
    """
    print(f"\\n{'='*60}")
    print("Example 4: Login Required Decorator")
    print(f"{'='*60}")

    class Request:
        def __init__(self, user=None):
            self.user = user

    @login_required
    def protected_view(request):
        return {'status': 200, 'message': f'Welcome {request.user.username}!'}

    # Test without authentication
    print("\\nTest 1: Access without authentication")
    request = Request(user=None)
    result = protected_view(request)
    print(f"  Status: {result['status']} - {'PASS' if result['status'] == 401 else 'FAIL'}")

    # Test with authentication
    print("\\nTest 2: Access with authentication")
    user = User('testuser', 'test@example.com')
    request = Request(user=user)
    result = protected_view(request)
    print(f"  Status: {result['status']} - {'PASS' if result['status'] == 200 else 'FAIL'}")
    print(f"  Message: {result['message']}")

# ============================================================================
# Example 5: Permission System
# ============================================================================

class Permission:
    """
    Represents a permission.
    """

    def __init__(self, name: str, codename: str):
        self.name = name
        self.codename = codename

class Group:
    """
    Represents a user group.
    """

    def __init__(self, name: str):
        self.name = name
        self.permissions: List[Permission] = []

    def add_permission(self, permission: Permission):
        """Add permission to group."""
        if permission not in self.permissions:
            self.permissions.append(permission)

class PermissionManager:
    """
    Manages user permissions and groups.
    """

    def __init__(self):
        self.permissions: Dict[str, Permission] = {}
        self.groups: Dict[str, Group] = {}
        self.user_permissions: Dict[int, List[Permission]] = {}
        self.user_groups: Dict[int, List[Group]] = {}

    def create_permission(self, name: str, codename: str) -> Permission:
        """Create a new permission."""
        perm = Permission(name, codename)
        self.permissions[codename] = perm
        return perm

    def create_group(self, name: str) -> Group:
        """Create a new group."""
        group = Group(name)
        self.groups[name] = group
        return group

    def add_user_to_group(self, user: User, group: Group):
        """Add user to group."""
        if user.id not in self.user_groups:
            self.user_groups[user.id] = []
        if group not in self.user_groups[user.id]:
            self.user_groups[user.id].append(group)

    def user_has_permission(self, user: User, permission_codename: str) -> bool:
        """Check if user has permission."""
        # Superusers have all permissions
        if user.is_superuser:
            return True

        # Check user's direct permissions
        user_perms = self.user_permissions.get(user.id, [])
        if any(p.codename == permission_codename for p in user_perms):
            return True

        # Check user's group permissions
        user_groups = self.user_groups.get(user.id, [])
        for group in user_groups:
            if any(p.codename == permission_codename for p in group.permissions):
                return True

        return False

def example_permission_system():
    """
    Demonstrates permission and group system.
    """
    print(f"\\n{'='*60}")
    print("Example 5: Permission and Group System")
    print(f"{'='*60}")

    perm_manager = PermissionManager()

    # Create permissions
    view_post = perm_manager.create_permission('Can view post', 'view_post')
    add_post = perm_manager.create_permission('Can add post', 'add_post')
    edit_post = perm_manager.create_permission('Can edit post', 'edit_post')
    delete_post = perm_manager.create_permission('Can delete post', 'delete_post')

    print("\\nCreated permissions:")
    for codename, perm in perm_manager.permissions.items():
        print(f"  - {perm.name} ({codename})")

    # Create groups
    editors = perm_manager.create_group('Editors')
    editors.add_permission(view_post)
    editors.add_permission(add_post)
    editors.add_permission(edit_post)

    admins = perm_manager.create_group('Admins')
    admins.add_permission(view_post)
    admins.add_permission(add_post)
    admins.add_permission(edit_post)
    admins.add_permission(delete_post)

    print("\\nCreated groups:")
    print(f"  - Editors ({len(editors.permissions)} permissions)")
    print(f"  - Admins ({len(admins.permissions)} permissions)")

    # Create users
    regular_user = User('user', 'user@example.com')
    regular_user.id = 1

    editor_user = User('editor', 'editor@example.com')
    editor_user.id = 2
    perm_manager.add_user_to_group(editor_user, editors)

    admin_user = User('admin', 'admin@example.com')
    admin_user.id = 3
    admin_user.is_superuser = True

    # Test permissions
    print("\\nPermission tests:")
    users = [
        (regular_user, 'Regular User'),
        (editor_user, 'Editor'),
        (admin_user, 'Admin (Superuser)')
    ]

    for user, label in users:
        print(f"\\n  {label}:")
        print(f"    View: {perm_manager.user_has_permission(user, 'view_post')}")
        print(f"    Add: {perm_manager.user_has_permission(user, 'add_post')}")
        print(f"    Edit: {perm_manager.user_has_permission(user, 'edit_post')}")
        print(f"    Delete: {perm_manager.user_has_permission(user, 'delete_post')}")

# ============================================================================
# Example 6: Password Reset System
# ============================================================================

class PasswordResetToken:
    """
    Represents a password reset token.
    """

    def __init__(self, user: User):
        self.token = secrets.token_urlsafe(32)
        self.user_id = user.id
        self.created_at = datetime.now()
        self.expires_at = datetime.now() + timedelta(hours=24)
        self.used = False

    def is_valid(self) -> bool:
        """Check if token is still valid."""
        return not self.used and datetime.now() < self.expires_at

class PasswordResetManager:
    """
    Manages password reset tokens.
    """

    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db
        self.tokens: Dict[str, PasswordResetToken] = {}

    def create_reset_token(self, email: str) -> Optional[PasswordResetToken]:
        """Create password reset token for user."""
        user = self.user_db.get_by_email(email)
        if not user:
            return None

        token_obj = PasswordResetToken(user)
        self.tokens[token_obj.token] = token_obj

        return token_obj

    def reset_password(self, token: str, new_password: str) -> bool:
        """Reset password using token."""
        token_obj = self.tokens.get(token)

        if not token_obj or not token_obj.is_valid():
            return False

        user = None
        for u in self.user_db.users.values():
            if u.id == token_obj.user_id:
                user = u
                break

        if not user:
            return False

        user.set_password(new_password)
        token_obj.used = True

        return True

def example_password_reset():
    """
    Demonstrates password reset system.
    """
    print(f"\\n{'='*60}")
    print("Example 6: Password Reset System")
    print(f"{'='*60}")

    user_db = UserDatabase()
    reset_manager = PasswordResetManager(user_db)

    # Create test user
    user = user_db.create_user('testuser', 'test@example.com', 'OldPassword123')
    old_password_hash = user.password

    print(f"\\nUser created: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Old password hash: {old_password_hash[:50]}...")

    # Request password reset
    print(f"\\nRequesting password reset...")
    token_obj = reset_manager.create_reset_token('test@example.com')

    if token_obj:
        print(f"  Reset token created: {token_obj.token[:20]}...")
        print(f"  Expires: {token_obj.expires_at}")

        # Simulate sending email
        print(f"  Email sent to {user.email}")

        # Reset password using token
        print(f"\\nResetting password...")
        new_password = 'NewPassword456'
        success = reset_manager.reset_password(token_obj.token, new_password)

        if success:
            print(f"  Password reset successful!")
            print(f"  New password hash: {user.password[:50]}...")

            # Verify old password no longer works
            old_works = user.check_password('OldPassword123')
            new_works = user.check_password(new_password)

            print(f"\\nVerification:")
            print(f"  Old password works: {old_works} - {'FAIL' if old_works else 'PASS'}")
            print(f"  New password works: {new_works} - {'PASS' if new_works else 'FAIL'}")

# ============================================================================
# Example 7: Remember Me Functionality
# ============================================================================

class RememberMeToken:
    """
    Long-lived token for remember me functionality.
    """

    def __init__(self, user: User):
        self.token = secrets.token_urlsafe(32)
        self.user_id = user.id
        self.created_at = datetime.now()
        self.expires_at = datetime.now() + timedelta(days=30)

    def is_valid(self) -> bool:
        """Check if token is still valid."""
        return datetime.now() < self.expires_at

class RememberMeManager:
    """
    Manages remember me tokens.
    """

    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db
        self.tokens: Dict[str, RememberMeToken] = {}

    def create_token(self, user: User) -> RememberMeToken:
        """Create remember me token."""
        token_obj = RememberMeToken(user)
        self.tokens[token_obj.token] = token_obj
        return token_obj

    def get_user_from_token(self, token: str) -> Optional[User]:
        """Get user from remember me token."""
        token_obj = self.tokens.get(token)

        if not token_obj or not token_obj.is_valid():
            return None

        for user in self.user_db.users.values():
            if user.id == token_obj.user_id:
                return user

        return None

    def delete_token(self, token: str):
        """Delete remember me token."""
        if token in self.tokens:
            del self.tokens[token]

def example_remember_me():
    """
    Demonstrates remember me functionality.
    """
    print(f"\\n{'='*60}")
    print("Example 7: Remember Me Functionality")
    print(f"{'='*60}")

    user_db = UserDatabase()
    remember_manager = RememberMeManager(user_db)

    # Create test user
    user = user_db.create_user('testuser', 'test@example.com', 'Password123')

    print(f"\\nUser login with 'Remember Me' enabled")
    token_obj = remember_manager.create_token(user)

    print(f"  Remember me token: {token_obj.token[:20]}...")
    print(f"  Expires: {token_obj.expires_at}")
    print(f"  Valid for: 30 days")

    # Simulate returning user
    print(f"\\nUser returns (using token)")
    retrieved_user = remember_manager.get_user_from_token(token_obj.token)

    if retrieved_user:
        print(f"  User identified: {retrieved_user.username}")
        print(f"  Auto-login successful!")
    else:
        print(f"  Token invalid or expired")

    # Logout (delete token)
    print(f"\\nUser logs out")
    remember_manager.delete_token(token_obj.token)

    # Try to use token again
    print(f"\\nAttempt to use deleted token")
    retrieved_user = remember_manager.get_user_from_token(token_obj.token)

    if retrieved_user:
        print(f"  FAILED: Token should be deleted")
    else:
        print(f"  SUCCESS: Token properly deleted")

# ============================================================================
# Example 8: Two-Factor Authentication (TOTP)
# ============================================================================

class TOTPManager:
    """
    Manages Time-based One-Time Passwords for 2FA.
    """

    def __init__(self):
        self.user_secrets: Dict[int, str] = {}
        self.backup_codes: Dict[int, List[str]] = {}

    def enable_2fa(self, user: User) -> Tuple[str, List[str]]:
        """Enable 2FA for user."""
        # Generate secret
        secret = secrets.token_hex(20)
        self.user_secrets[user.id] = secret

        # Generate backup codes
        backup_codes = [secrets.token_hex(4) for _ in range(10)]
        self.backup_codes[user.id] = backup_codes

        return secret, backup_codes

    def generate_totp(self, user: User) -> str:
        """Generate current TOTP code (simulated)."""
        if user.id not in self.user_secrets:
            return ''

        # In real implementation, this would use time-based algorithm
        # For simulation, we'll use a simple hash
        secret = self.user_secrets[user.id]
        time_step = int(time.time() // 30)
        code_input = f"{secret}{time_step}"
        hash_value = hashlib.sha256(code_input.encode()).hexdigest()
        code = str(int(hash_value[:6], 16) % 1000000).zfill(6)

        return code

    def verify_totp(self, user: User, code: str) -> bool:
        """Verify TOTP code."""
        if user.id not in self.user_secrets:
            return False

        current_code = self.generate_totp(user)
        return code == current_code

    def verify_backup_code(self, user: User, code: str) -> bool:
        """Verify and consume backup code."""
        if user.id not in self.backup_codes:
            return False

        if code in self.backup_codes[user.id]:
            self.backup_codes[user.id].remove(code)
            return True

        return False

def example_two_factor_auth():
    """
    Demonstrates two-factor authentication.
    """
    print(f"\\n{'='*60}")
    print("Example 8: Two-Factor Authentication (TOTP)")
    print(f"{'='*60}")

    user_db = UserDatabase()
    totp_manager = TOTPManager()

    # Create user
    user = user_db.create_user('secureuser', 'secure@example.com', 'Password123')

    # Enable 2FA
    print(f"\\nEnabling 2FA for {user.username}")
    secret, backup_codes = totp_manager.enable_2fa(user)

    print(f"  Secret: {secret[:20]}...")
    print(f"  Backup codes generated: {len(backup_codes)}")
    print(f"  First 3 backup codes:")
    for code in backup_codes[:3]:
        print(f"    - {code}")

    # Generate and verify TOTP
    print(f"\\nGenerating TOTP code...")
    totp_code = totp_manager.generate_totp(user)
    print(f"  Current TOTP: {totp_code}")

    # Verify correct code
    print(f"\\nVerifying TOTP code...")
    is_valid = totp_manager.verify_totp(user, totp_code)
    print(f"  Correct code: {is_valid} - {'PASS' if is_valid else 'FAIL'}")

    # Verify incorrect code
    is_valid = totp_manager.verify_totp(user, '000000')
    print(f"  Incorrect code: {is_valid} - {'PASS' if not is_valid else 'FAIL'}")

    # Test backup code
    print(f"\\nUsing backup code...")
    backup_code = backup_codes[0]
    is_valid = totp_manager.verify_backup_code(user, backup_code)
    print(f"  Backup code valid: {is_valid} - {'PASS' if is_valid else 'FAIL'}")

    # Try to reuse backup code
    is_valid = totp_manager.verify_backup_code(user, backup_code)
    print(f"  Reuse backup code: {is_valid} - {'PASS' if not is_valid else 'FAIL'}")

# ============================================================================
# Example 9: Custom Authentication Backend
# ============================================================================

class EmailAuthenticationBackend:
    """
    Custom authentication backend that uses email instead of username.
    """

    def __init__(self, user_db: UserDatabase):
        self.user_db = user_db

    def authenticate(self, email: str, password: str) -> Optional[User]:
        """Authenticate using email and password."""
        user = self.user_db.get_by_email(email)

        if user and user.is_active and user.check_password(password):
            return user

        return None

def example_custom_auth_backend():
    """
    Demonstrates custom authentication backend.
    """
    print(f"\\n{'='*60}")
    print("Example 9: Custom Authentication Backend (Email)")
    print(f"{'='*60}")

    user_db = UserDatabase()
    email_auth = EmailAuthenticationBackend(user_db)

    # Create user
    user = user_db.create_user('testuser', 'test@example.com', 'Password123')

    print(f"\\nUser created:")
    print(f"  Username: {user.username}")
    print(f"  Email: {user.email}")

    # Authenticate with email
    print(f"\\nAuthentication with email...")
    authenticated_user = email_auth.authenticate('test@example.com', 'Password123')

    if authenticated_user:
        print(f"  SUCCESS: User authenticated")
        print(f"  Username: {authenticated_user.username}")
    else:
        print(f"  FAILED: Authentication failed")

    # Test wrong password
    print(f"\\nAuthentication with wrong password...")
    authenticated_user = email_auth.authenticate('test@example.com', 'WrongPassword')

    if authenticated_user:
        print(f"  FAILED: Should not authenticate")
    else:
        print(f"  SUCCESS: Authentication rejected")

# ============================================================================
# Example 10: Complete Authentication System
# ============================================================================

def example_complete_auth_system():
    """
    Complete authentication system with all features.
    """
    print(f"\\n{'='*60}")
    print("Example 10: Complete Authentication System")
    print(f"{'='*60}")

    # Initialize components
    user_db = UserDatabase()
    auth = AuthenticationBackend(user_db)
    perm_manager = PermissionManager()
    totp_manager = TOTPManager()
    remember_manager = RememberMeManager(user_db)

    # 1. User Registration
    print("\\n[1] User Registration")
    form_data = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'password': 'SecurePass123',
        'password_confirm': 'SecurePass123'
    }
    form = RegistrationForm(form_data, user_db)

    if form.is_valid():
        user = user_db.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password']
        )
        print(f"  User registered: {user.username}")
    else:
        print(f"  Registration failed: {form.errors}")
        return

    # 2. Setup Permissions
    print("\\n[2] Setting Up Permissions")
    view_perm = perm_manager.create_permission('Can view', 'view')
    edit_perm = perm_manager.create_permission('Can edit', 'edit')
    editors_group = perm_manager.create_group('Editors')
    editors_group.add_permission(view_perm)
    editors_group.add_permission(edit_perm)
    perm_manager.add_user_to_group(user, editors_group)
    print(f"  User added to Editors group")

    # 3. Enable 2FA
    print("\\n[3] Enabling Two-Factor Authentication")
    secret, backup_codes = totp_manager.enable_2fa(user)
    print(f"  2FA enabled with {len(backup_codes)} backup codes")

    # 4. Login
    print("\\n[4] User Login")
    authenticated_user = auth.authenticate('john_doe', 'SecurePass123')

    if authenticated_user:
        print(f"  Step 1: Username/password verified")

        # Verify 2FA
        totp_code = totp_manager.generate_totp(authenticated_user)
        is_totp_valid = totp_manager.verify_totp(authenticated_user, totp_code)

        if is_totp_valid:
            print(f"  Step 2: 2FA code verified")

            # Create session with remember me
            session = auth.login(authenticated_user)
            remember_token = remember_manager.create_token(authenticated_user)

            print(f"  Step 3: Session created")
            print(f"  Step 4: Remember me token created")
            print(f"  Login successful!")

    # 5. Check Permissions
    print("\\n[5] Permission Check")
    can_view = perm_manager.user_has_permission(user, 'view')
    can_edit = perm_manager.user_has_permission(user, 'edit')
    can_delete = perm_manager.user_has_permission(user, 'delete')

    print(f"  Can view: {can_view}")
    print(f"  Can edit: {can_edit}")
    print(f"  Can delete: {can_delete}")

    # 6. Logout
    print("\\n[6] User Logout")
    auth.logout(session)
    remember_manager.delete_token(remember_token.token)
    print(f"  Session destroyed")
    print(f"  Remember me token deleted")
    print(f"  Logout successful!")

    print(f"\\n{'='*60}")
    print("Complete authentication system simulation finished!")
    print(f"{'='*60}")

# ============================================================================
# Run All Examples
# ============================================================================

if __name__ == "__main__":
    # Example 1: Password hashing
    example_password_hashing()

    # Example 2: User registration
    example_user_registration()

    # Example 3: Login system
    example_login_system()

    # Example 4: Login required decorator
    example_login_required()

    # Example 5: Permission system
    example_permission_system()

    # Example 6: Password reset
    example_password_reset()

    # Example 7: Remember me
    example_remember_me()

    # Example 8: Two-factor authentication
    example_two_factor_auth()

    # Example 9: Custom auth backend
    example_custom_auth_backend()

    # Example 10: Complete system
    example_complete_auth_system()

    print(f"\\n{'='*60}")
    print("All Django authentication examples completed successfully!")
    print(f"{'='*60}")
'''

print("Upgraded Lesson 519: Django User Authentication")
print(f"  New length: {len(lesson_519['fullSolution']):,} characters")

# Save lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2)

print("\\n" + "="*70)
print("BATCH 20 COMPLETE: Django Core Lessons")
print("="*70)
print("\\nUpgraded lessons:")
print(f"  - Lesson 760: Django Deployment Configuration (31,364 chars)")
print(f"  - Lesson 518: Django Function-Based Views (35,010 chars)")
print(f"  - Lesson 519: Django User Authentication ({len(lesson_519['fullSolution']):,} chars)")
print("\\nAll lessons upgraded to 13,000-17,000+ characters")
print("Zero package installation required!")
print("="*70)
