#!/usr/bin/env python3
"""
Upgrade FastAPI OAuth2, pytest Testing, and async lessons
"""

import json
import sys

def upgrade_lesson_961():
    """FastAPI - OAuth2 Authentication"""
    return '''# FastAPI OAuth2 Authentication
# In production: pip install fastapi python-jose[cryptography] passlib[bcrypt]

"""
FastAPI OAuth2 Authentication with JWT

Complete OAuth2 password flow implementation:
- Password hashing with bcrypt
- JWT token generation and validation
- OAuth2 password bearer scheme
- Protected routes with dependencies
- Token refresh mechanism
- User authentication and authorization

Used by: Microsoft, Uber, Netflix API authentication
"""

import hmac
import hashlib
import base64
import json
import time
import secrets
from typing import Dict, Optional, List, Any
from datetime import datetime, timedelta


# ============================================================================
# Password Hashing (simulated bcrypt)
# ============================================================================

class PasswordHasher:
    """Password hashing utility"""

    @staticmethod
    def hash(password: str) -> str:
        """Hash password"""
        # In production: use bcrypt
        # return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        # Simulated hash (DO NOT use in production)
        salt = secrets.token_hex(16)
        hash_value = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt.encode(),
            100000
        )
        return f"{salt}${hash_value.hex()}"

    @staticmethod
    def verify(password: str, hashed: str) -> bool:
        """Verify password against hash"""
        # In production: use bcrypt.checkpw()

        try:
            salt, hash_value = hashed.split('$')
            new_hash = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode(),
                salt.encode(),
                100000
            )
            return new_hash.hex() == hash_value
        except Exception:
            return False


# ============================================================================
# JWT Token Manager
# ============================================================================

class JWT:
    """JWT encoding/decoding"""

    @staticmethod
    def _base64_url_encode(data: bytes) -> str:
        """Base64 URL-safe encoding"""
        return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

    @staticmethod
    def _base64_url_decode(data: str) -> bytes:
        """Base64 URL-safe decoding"""
        padding = 4 - (len(data) % 4)
        if padding != 4:
            data += '=' * padding
        return base64.urlsafe_b64decode(data.encode('utf-8'))

    @staticmethod
    def _sign_hs256(message: str, secret: str) -> str:
        """Create HMAC-SHA256 signature"""
        signature = hmac.new(
            secret.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).digest()
        return JWT._base64_url_encode(signature)

    @staticmethod
    def encode(payload: Dict[str, Any], secret: str) -> str:
        """Encode payload as JWT"""
        header = {'typ': 'JWT', 'alg': 'HS256'}

        header_b64 = JWT._base64_url_encode(json.dumps(header).encode())
        payload_b64 = JWT._base64_url_encode(json.dumps(payload).encode())

        message = f"{header_b64}.{payload_b64}"
        signature = JWT._sign_hs256(message, secret)

        return f"{message}.{signature}"

    @staticmethod
    def decode(token: str, secret: str, verify: bool = True) -> Dict[str, Any]:
        """Decode and verify JWT"""
        try:
            header_b64, payload_b64, signature = token.split('.')
        except ValueError:
            raise ValueError("Invalid token format")

        if verify:
            message = f"{header_b64}.{payload_b64}"
            expected_signature = JWT._sign_hs256(message, secret)
            if signature != expected_signature:
                raise ValueError("Invalid signature")

        payload_json = JWT._base64_url_decode(payload_b64)
        payload = json.loads(payload_json)

        if verify and 'exp' in payload:
            if time.time() > payload['exp']:
                raise ValueError("Token expired")

        return payload


# ============================================================================
# User Database (simulated)
# ============================================================================

class UserDatabase:
    """User storage"""

    def __init__(self):
        self.users: Dict[str, Dict[str, Any]] = {}

    def create_user(self, username: str, email: str, password: str) -> Dict:
        """Create new user"""
        if username in self.users:
            raise ValueError("User already exists")

        user = {
            'username': username,
            'email': email,
            'hashed_password': PasswordHasher.hash(password),
            'is_active': True,
            'scopes': ['user'],
            'created_at': datetime.now().isoformat()
        }

        self.users[username] = user
        return user

    def get_user(self, username: str) -> Optional[Dict]:
        """Get user by username"""
        return self.users.get(username)

    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        """Authenticate user"""
        user = self.get_user(username)
        if not user:
            return None

        if not PasswordHasher.verify(password, user['hashed_password']):
            return None

        return user


# ============================================================================
# OAuth2 Token Manager
# ============================================================================

class OAuth2TokenManager:
    """Manage OAuth2 tokens"""

    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.access_token_expire_minutes = 30
        self.refresh_token_expire_days = 7

    def create_access_token(self, data: Dict[str, Any], expires_delta: timedelta = None) -> str:
        """Create access token"""
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=self.access_token_expire_minutes)

        to_encode.update({
            'exp': expire.timestamp(),
            'iat': time.time(),
            'type': 'access'
        })

        return JWT.encode(to_encode, self.secret_key)

    def create_refresh_token(self, data: Dict[str, Any]) -> str:
        """Create refresh token"""
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=self.refresh_token_expire_days)

        to_encode.update({
            'exp': expire.timestamp(),
            'iat': time.time(),
            'type': 'refresh'
        })

        return JWT.encode(to_encode, self.secret_key)

    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify and decode token"""
        try:
            payload = JWT.decode(token, self.secret_key, verify=True)
            return payload
        except Exception as e:
            raise ValueError(f"Invalid token: {e}")


# ============================================================================
# FastAPI OAuth2 Scheme
# ============================================================================

class OAuth2PasswordBearer:
    """OAuth2 password bearer scheme"""

    def __init__(self, token_url: str):
        self.token_url = token_url

    def __call__(self, authorization: str = None) -> str:
        """Extract token from Authorization header"""
        if not authorization:
            raise ValueError("Not authenticated")

        if not authorization.startswith("Bearer "):
            raise ValueError("Invalid authentication scheme")

        return authorization.replace("Bearer ", "")


# ============================================================================
# Dependencies
# ============================================================================

# Database instance
db = UserDatabase()

# Token manager
SECRET_KEY = secrets.token_urlsafe(32)
token_manager = OAuth2TokenManager(SECRET_KEY)

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(token_url="/token")


def get_current_user(token: str) -> Dict:
    """
    Dependency: Get current user from token

    FastAPI will inject this automatically
    """
    try:
        payload = token_manager.verify_token(token)
        username = payload.get("sub")

        if username is None:
            raise ValueError("Invalid token payload")

        user = db.get_user(username)
        if user is None:
            raise ValueError("User not found")

        return user

    except Exception as e:
        raise ValueError(f"Could not validate credentials: {e}")


def get_current_active_user(current_user: Dict) -> Dict:
    """
    Dependency: Ensure user is active

    Depends on get_current_user
    """
    if not current_user.get('is_active'):
        raise ValueError("Inactive user")

    return current_user


# ============================================================================
# FastAPI Application
# ============================================================================

class Request:
    """Simulated request"""
    def __init__(self, method: str, url: str, headers: Dict = None, json_data: Dict = None, form_data: Dict = None):
        self.method = method
        self.url = url
        self.headers = headers or {}
        self.json_data = json_data
        self.form_data = form_data


class Response:
    """Simulated response"""
    def __init__(self, content: Any, status_code: int = 200):
        self.content = content
        self.status_code = status_code


class FastAPI:
    """Simulated FastAPI app"""

    def __init__(self):
        self.routes = {}

    def post(self, path: str):
        def decorator(func):
            self.routes[f"POST {path}"] = func
            return func
        return decorator

    def get(self, path: str):
        def decorator(func):
            self.routes[f"GET {path}"] = func
            return func
        return decorator

    async def handle_request(self, request: Request) -> Response:
        route_key = f"{request.method} {request.url}"

        if route_key not in self.routes:
            return Response({"error": "Not found"}, 404)

        try:
            result = await self.routes[route_key](request)
            return Response(result, 200)
        except ValueError as e:
            return Response({"error": str(e)}, 401)
        except Exception as e:
            return Response({"error": str(e)}, 500)


app = FastAPI()


# ============================================================================
# Auth Routes
# ============================================================================

@app.post("/register")
async def register(request: Request):
    """Register new user"""
    data = request.form_data or request.json_data

    try:
        user = db.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        return {
            "username": user['username'],
            "email": user['email'],
            "message": "User created successfully"
        }

    except Exception as e:
        raise ValueError(f"Registration failed: {e}")


@app.post("/token")
async def login(request: Request):
    """
    OAuth2 compatible token login

    Returns access_token and refresh_token
    """
    data = request.form_data

    # Authenticate user
    user = db.authenticate_user(data['username'], data['password'])
    if not user:
        raise ValueError("Incorrect username or password")

    if not user.get('is_active'):
        raise ValueError("Inactive user")

    # Create tokens
    access_token = token_manager.create_access_token(
        data={"sub": user['username'], "scopes": user['scopes']}
    )

    refresh_token = token_manager.create_refresh_token(
        data={"sub": user['username']}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@app.post("/token/refresh")
async def refresh_token(request: Request):
    """Refresh access token"""
    data = request.json_data
    refresh_token = data.get('refresh_token')

    try:
        payload = token_manager.verify_token(refresh_token)

        if payload.get('type') != 'refresh':
            raise ValueError("Invalid token type")

        username = payload.get('sub')
        user = db.get_user(username)

        if not user:
            raise ValueError("User not found")

        # Create new access token
        new_access_token = token_manager.create_access_token(
            data={"sub": username, "scopes": user['scopes']}
        )

        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except Exception as e:
        raise ValueError(f"Token refresh failed: {e}")


# ============================================================================
# Protected Routes
# ============================================================================

@app.get("/users/me")
async def read_users_me(request: Request):
    """
    Get current user (protected route)

    Requires valid access token
    """
    # Extract token
    authorization = request.headers.get('Authorization')
    token = oauth2_scheme(authorization)

    # Get current user (dependency)
    current_user = get_current_user(token)

    # Ensure active (dependency)
    active_user = get_current_active_user(current_user)

    return {
        "username": active_user['username'],
        "email": active_user['email'],
        "scopes": active_user['scopes'],
        "is_active": active_user['is_active']
    }


@app.get("/items/")
async def read_items(request: Request):
    """Protected route - list items"""
    authorization = request.headers.get('Authorization')
    token = oauth2_scheme(authorization)
    current_user = get_current_user(token)

    return {
        "items": [
            {"id": 1, "name": "Item 1", "owner": current_user['username']},
            {"id": 2, "name": "Item 2", "owner": current_user['username']},
        ]
    }


# ============================================================================
# Main Example
# ============================================================================

import asyncio

async def main():
    print("=" * 80)
    print("FASTAPI OAUTH2 AUTHENTICATION")
    print("=" * 80)

    # 1. Register user
    print("\\n1. REGISTER USER")
    print("-" * 80)
    register_req = Request("POST", "/register", form_data={
        "username": "alice",
        "email": "alice@example.com",
        "password": "secret123"
    })
    register_resp = await app.handle_request(register_req)
    print(f"Response: {register_resp.content}")

    # 2. Login and get tokens
    print("\\n2. LOGIN - GET TOKENS")
    print("-" * 80)
    login_req = Request("POST", "/token", form_data={
        "username": "alice",
        "password": "secret123"
    })
    login_resp = await app.handle_request(login_req)
    print(f"Response: {login_resp.content}")

    access_token = login_resp.content['access_token']
    refresh_token = login_resp.content['refresh_token']

    print(f"\\nAccess token (first 50 chars): {access_token[:50]}...")
    print(f"Refresh token (first 50 chars): {refresh_token[:50]}...")

    # 3. Access protected route
    print("\\n3. ACCESS PROTECTED ROUTE - /users/me")
    print("-" * 80)
    me_req = Request("GET", "/users/me", headers={
        "Authorization": f"Bearer {access_token}"
    })
    me_resp = await app.handle_request(me_req)
    print(f"User info: {me_resp.content}")

    # 4. Access another protected route
    print("\\n4. ACCESS PROTECTED ROUTE - /items/")
    print("-" * 80)
    items_req = Request("GET", "/items/", headers={
        "Authorization": f"Bearer {access_token}"
    })
    items_resp = await app.handle_request(items_req)
    print(f"Items: {items_resp.content}")

    # 5. Try accessing without token
    print("\\n5. ACCESS WITHOUT TOKEN (Should Fail)")
    print("-" * 80)
    unauth_req = Request("GET", "/users/me")
    unauth_resp = await app.handle_request(unauth_req)
    print(f"Response: {unauth_resp.content} (Status: {unauth_resp.status_code})")

    # 6. Refresh access token
    print("\\n6. REFRESH ACCESS TOKEN")
    print("-" * 80)
    refresh_req = Request("POST", "/token/refresh", json_data={
        "refresh_token": refresh_token
    })
    refresh_resp = await app.handle_request(refresh_req)
    print(f"New access token: {refresh_resp.content['access_token'][:50]}...")

    print("\\n" + "=" * 80)
    print("OAUTH2 BEST PRACTICES")
    print("=" * 80)
    print("""
1. PASSWORD SECURITY:
   - Hash passwords with bcrypt (work factor 12+)
   - Never store plaintext passwords
   - Use strong secret keys (32+ bytes random)
   - Rotate secret keys periodically

2. TOKEN SECURITY:
   - Short access token lifetime (15-30 min)
   - Long refresh token lifetime (7 days)
   - Use HTTPS only in production
   - Store tokens securely (httpOnly cookies)

3. OAUTH2 SCOPES:
   - Define granular scopes (user, admin, read, write)
   - Enforce scope checks in endpoints
   - Include scopes in token payload
   - Document required scopes per endpoint

4. DEPENDENCIES:
   - Use FastAPI dependency injection
   - Chain dependencies (token -> user -> active user)
   - Reuse dependencies across routes
   - Handle dependency errors gracefully

5. ERROR HANDLING:
   - Return 401 for authentication failures
   - Return 403 for authorization failures
   - Don't leak information in error messages
   - Log security events

6. PRODUCTION:
   - Use HTTPS/TLS certificates
   - Enable CORS properly
   - Rate limit authentication endpoints
   - Monitor for suspicious activity
   - Implement account lockout
""")

    print("\\n✓ OAuth2 authentication complete!")


if __name__ == '__main__':
    asyncio.run(main())
'''

def upgrade_lesson_813():
    """pytest - API Testing"""
    return '''# pytest API Testing
# In production: pip install pytest requests responses

"""
pytest API Testing

Complete guide to testing REST APIs:
- HTTP request/response testing
- Mocking external API calls
- Testing error scenarios
- Async API testing
- Integration testing with test client
- API contract testing

Used by: All Python API projects (FastAPI, Flask, Django)
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


# ============================================================================
# Mock HTTP Client
# ============================================================================

@dataclass
class MockResponse:
    """Mock HTTP response"""
    status_code: int
    text: str
    headers: Dict[str, str]

    def json(self) -> Any:
        """Parse JSON response"""
        return json.loads(self.text)

    def raise_for_status(self):
        """Raise exception for bad status codes"""
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}: {self.text}")


class MockHTTPClient:
    """Mock HTTP client for testing"""

    def __init__(self):
        self.requests_made: List[Dict] = []
        self.mock_responses: Dict[str, MockResponse] = {}

    def register_response(self, url: str, method: str, response: MockResponse):
        """Register mock response for URL"""
        key = f"{method.upper()} {url}"
        self.mock_responses[key] = response

    def get(self, url: str, headers: Dict = None) -> MockResponse:
        """Make GET request"""
        self.requests_made.append({
            'method': 'GET',
            'url': url,
            'headers': headers
        })

        key = f"GET {url}"
        if key in self.mock_responses:
            return self.mock_responses[key]

        # Default 404
        return MockResponse(404, '{"error": "Not found"}', {})

    def post(self, url: str, json_data: Dict = None, headers: Dict = None) -> MockResponse:
        """Make POST request"""
        self.requests_made.append({
            'method': 'POST',
            'url': url,
            'json': json_data,
            'headers': headers
        })

        key = f"POST {url}"
        if key in self.mock_responses:
            return self.mock_responses[key]

        return MockResponse(201, json.dumps(json_data), {})

    def put(self, url: str, json_data: Dict = None, headers: Dict = None) -> MockResponse:
        """Make PUT request"""
        self.requests_made.append({
            'method': 'PUT',
            'url': url,
            'json': json_data,
            'headers': headers
        })

        key = f"PUT {url}"
        if key in self.mock_responses:
            return self.mock_responses[key]

        return MockResponse(200, json.dumps(json_data), {})

    def delete(self, url: str, headers: Dict = None) -> MockResponse:
        """Make DELETE request"""
        self.requests_made.append({
            'method': 'DELETE',
            'url': url,
            'headers': headers
        })

        key = f"DELETE {url}"
        if key in self.mock_responses:
            return self.mock_responses[key]

        return MockResponse(204, '', {})


# ============================================================================
# API Client to Test
# ============================================================================

class UserAPIClient:
    """User API client"""

    def __init__(self, base_url: str, http_client=None):
        self.base_url = base_url
        self.http = http_client or MockHTTPClient()

    def get_user(self, user_id: int) -> Dict:
        """Get user by ID"""
        response = self.http.get(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def list_users(self) -> List[Dict]:
        """List all users"""
        response = self.http.get(f"{self.base_url}/users")
        response.raise_for_status()
        return response.json()['users']

    def create_user(self, username: str, email: str) -> Dict:
        """Create new user"""
        response = self.http.post(
            f"{self.base_url}/users",
            json_data={'username': username, 'email': email}
        )
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id: int, data: Dict) -> Dict:
        """Update user"""
        response = self.http.put(
            f"{self.base_url}/users/{user_id}",
            json_data=data
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id: int):
        """Delete user"""
        response = self.http.delete(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()


# ============================================================================
# Test Fixtures
# ============================================================================

def create_mock_client():
    """Fixture: Create mock HTTP client"""
    return MockHTTPClient()


def create_api_client(mock_client):
    """Fixture: Create API client with mock"""
    return UserAPIClient("https://api.example.com", mock_client)


# ============================================================================
# Tests: GET Requests
# ============================================================================

def test_get_user_success():
    """Test getting user by ID"""
    print("\\nTest: GET /users/1 - Success")
    print("-" * 60)

    # Setup mock
    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/1",
        "GET",
        MockResponse(200, '{"id": 1, "username": "alice", "email": "alice@example.com"}', {})
    )

    # Create API client
    api = create_api_client(mock_client)

    # Make request
    user = api.get_user(1)

    # Assertions
    assert user['id'] == 1
    assert user['username'] == 'alice'
    assert user['email'] == 'alice@example.com'

    # Verify request was made
    assert len(mock_client.requests_made) == 1
    assert mock_client.requests_made[0]['method'] == 'GET'
    assert mock_client.requests_made[0]['url'] == 'https://api.example.com/users/1'

    print("✓ User retrieved successfully")
    print(f"  User: {user}")


def test_get_user_not_found():
    """Test getting non-existent user"""
    print("\\nTest: GET /users/999 - Not Found")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/999",
        "GET",
        MockResponse(404, '{"error": "User not found"}', {})
    )

    api = create_api_client(mock_client)

    # Should raise exception
    try:
        api.get_user(999)
        print("✗ Should have raised exception")
        assert False
    except Exception as e:
        print(f"✓ Exception raised: {e}")
        assert "404" in str(e)


# ============================================================================
# Tests: POST Requests
# ============================================================================

def test_create_user():
    """Test creating new user"""
    print("\\nTest: POST /users - Create User")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users",
        "POST",
        MockResponse(201, '{"id": 1, "username": "bob", "email": "bob@example.com"}', {})
    )

    api = create_api_client(mock_client)

    # Create user
    user = api.create_user("bob", "bob@example.com")

    # Assertions
    assert user['id'] == 1
    assert user['username'] == 'bob'

    # Verify request payload
    request = mock_client.requests_made[0]
    assert request['method'] == 'POST'
    assert request['json']['username'] == 'bob'
    assert request['json']['email'] == 'bob@example.com'

    print("✓ User created successfully")
    print(f"  User: {user}")


# ============================================================================
# Tests: PUT Requests
# ============================================================================

def test_update_user():
    """Test updating user"""
    print("\\nTest: PUT /users/1 - Update User")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/1",
        "PUT",
        MockResponse(200, '{"id": 1, "username": "alice_updated", "email": "alice@example.com"}', {})
    )

    api = create_api_client(mock_client)

    # Update user
    user = api.update_user(1, {'username': 'alice_updated'})

    # Assertions
    assert user['username'] == 'alice_updated'

    print("✓ User updated successfully")


# ============================================================================
# Tests: DELETE Requests
# ============================================================================

def test_delete_user():
    """Test deleting user"""
    print("\\nTest: DELETE /users/1 - Delete User")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/1",
        "DELETE",
        MockResponse(204, '', {})
    )

    api = create_api_client(mock_client)

    # Delete user (should not raise exception)
    api.delete_user(1)

    # Verify request
    assert len(mock_client.requests_made) == 1
    assert mock_client.requests_made[0]['method'] == 'DELETE'

    print("✓ User deleted successfully")


# ============================================================================
# Tests: List Resources
# ============================================================================

def test_list_users():
    """Test listing all users"""
    print("\\nTest: GET /users - List Users")
    print("-" * 60)

    mock_client = create_mock_client()
    response_json = json.dumps({"users": [
        {"id": 1, "username": "alice"},
        {"id": 2, "username": "bob"},
        {"id": 3, "username": "charlie"}
    ]})
    mock_client.register_response(
        "https://api.example.com/users",
        "GET",
        MockResponse(200, response_json, {})
    )

    api = create_api_client(mock_client)

    # List users
    users = api.list_users()

    # Assertions
    assert len(users) == 3
    assert users[0]['username'] == 'alice'
    assert users[1]['username'] == 'bob'

    print(f"✓ Listed {len(users)} users")


# ============================================================================
# Tests: Error Scenarios
# ============================================================================

def test_server_error():
    """Test handling server error"""
    print("\\nTest: Server Error (500)")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/1",
        "GET",
        MockResponse(500, '{"error": "Internal server error"}', {})
    )

    api = create_api_client(mock_client)

    try:
        api.get_user(1)
        print("✗ Should have raised exception")
        assert False
    except Exception as e:
        print(f"✓ Server error handled: {e}")
        assert "500" in str(e)


def test_invalid_json_response():
    """Test handling invalid JSON"""
    print("\\nTest: Invalid JSON Response")
    print("-" * 60)

    mock_client = create_mock_client()
    mock_client.register_response(
        "https://api.example.com/users/1",
        "GET",
        MockResponse(200, 'Not valid JSON', {})
    )

    api = create_api_client(mock_client)

    try:
        api.get_user(1)
        print("✗ Should have raised exception")
        assert False
    except json.JSONDecodeError:
        print("✓ JSON decode error handled correctly")


# ============================================================================
# Main Test Runner
# ============================================================================

def main():
    print("=" * 80)
    print("PYTEST API TESTING")
    print("=" * 80)

    # Run all tests
    tests = [
        test_get_user_success,
        test_get_user_not_found,
        test_create_user,
        test_update_user,
        test_delete_user,
        test_list_users,
        test_server_error,
        test_invalid_json_response,
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
    print(f"TEST SUMMARY: {passed} passed, {failed} failed")
    print("=" * 80)

    print("\\n" + "=" * 80)
    print("API TESTING BEST PRACTICES")
    print("=" * 80)
    print("""
1. TEST STRUCTURE:
   - Arrange: Setup mocks and test data
   - Act: Make API call
   - Assert: Verify response and side effects
   - Verify: Check request was made correctly

2. WHAT TO TEST:
   - Success scenarios (200, 201, 204)
   - Error scenarios (400, 401, 404, 500)
   - Edge cases (empty lists, null values)
   - Request payloads
   - Response parsing

3. MOCKING:
   - Mock external HTTP calls (use responses/httpretty)
   - Don't make real HTTP requests in unit tests
   - Test API client logic, not external service
   - Mock at HTTP layer, not business logic

4. FIXTURES:
   - Create reusable test data factories
   - Share mock client across tests
   - Reset state between tests
   - Use pytest fixtures for setup/teardown

5. ASSERTIONS:
   - Test status codes
   - Verify response structure
   - Check error messages
   - Validate request payloads
   - Test headers and authentication

6. INTEGRATION TESTS:
   - Use real test server (FastAPI TestClient)
   - Test complete request/response cycle
   - Verify database changes
   - Test authentication flows
   - Run against staging environment
""")

    print("\\n✓ API testing complete!")


if __name__ == '__main__':
    main()
'''

def main():
    print("=" * 80)
    print("UPGRADING: FastAPI OAuth2, pytest API Testing")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (961, upgrade_lesson_961, "FastAPI - OAuth2 Authentication"),
        (813, upgrade_lesson_813, "pytest - API Testing"),
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
    print("FASTAPI OAUTH2 AND PYTEST API TESTING COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
