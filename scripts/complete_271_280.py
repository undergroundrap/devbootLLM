#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 271: WSGI Hello App
lesson271 = next(l for l in lessons if l['id'] == 271)
lesson271['content'] = '''# WSGI Hello App

Build web applications using WSGI (Web Server Gateway Interface), the Python standard for web servers and applications. WSGI provides a universal interface between web servers and Python web applications, enabling framework-agnostic web development.

## Example 1: Basic WSGI Application

Create a simple WSGI app:

```python
def simple_app(environ, start_response):
    """Minimal WSGI application."""
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [b'Hello, WSGI World!']

# To run with built-in server:
# from wsgiref.simple_server import make_server
# server = make_server('localhost', 8000, simple_app)
# server.serve_forever()
```

**Result**: Minimal WSGI application returning plain text.

## Example 2: HTML Response

Serve HTML content:

```python
def html_app(environ, start_response):
    """WSGI app serving HTML."""
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)

    html = b"""
    <!DOCTYPE html>
    <html>
        <head><title>WSGI App</title></head>
        <body>
            <h1>Hello from WSGI!</h1>
            <p>This is a WSGI application.</p>
        </body>
    </html>
    """

    return [html]
```

**Result**: HTML response from WSGI application.

## Example 3: Request Information

Access request data:

```python
def request_info_app(environ, start_response):
    """Display request information."""
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    query = environ.get('QUERY_STRING', '')

    response = f"""Request Information:
Method: {method}
Path: {path}
Query String: {query}
""".encode('utf-8')

    return [response]
```

**Result**: Display HTTP request details.

## Example 4: Routing

Implement basic routing:

```python
def routing_app(environ, start_response):
    """WSGI app with routing."""
    path = environ['PATH_INFO']

    if path == '/':
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'Home Page']

    elif path == '/about':
        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'About Page']

    else:
        status = '404 Not Found'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)
        return [b'Page Not Found']
```

**Result**: Route-based request handling.

## Example 5: Query Parameters

Parse query strings:

```python
from urllib.parse import parse_qs

def query_app(environ, start_response):
    """Handle query parameters."""
    query_string = environ.get('QUERY_STRING', '')
    params = parse_qs(query_string)

    name = params.get('name', ['Guest'])[0]

    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    response = f'Hello, {name}!'.encode('utf-8')
    return [response]

# Access: http://localhost:8000/?name=Alice
```

**Result**: Query parameter parsing and usage.

## Example 6: POST Data

Handle form submissions:

```python
from urllib.parse import parse_qs

def post_app(environ, start_response):
    """Handle POST requests."""
    method = environ['REQUEST_METHOD']

    if method == 'POST':
        # Read POST data
        try:
            content_length = int(environ.get('CONTENT_LENGTH', 0))
        except ValueError:
            content_length = 0

        post_data = environ['wsgi.input'].read(content_length)
        params = parse_qs(post_data.decode('utf-8'))

        status = '200 OK'
        headers = [('Content-Type', 'text/plain')]
        start_response(status, headers)

        message = params.get('message', [''])[0]
        return [f'Received: {message}'.encode('utf-8')]

    else:
        status = '200 OK'
        headers = [('Content-Type', 'text/html')]
        start_response(status, headers)

        form = b"""
        <form method="POST">
            <input name="message" placeholder="Enter message">
            <button type="submit">Send</button>
        </form>
        """
        return [form]
```

**Result**: Form submission handling.

## Example 7: JSON API

Create JSON API endpoint:

```python
import json as json_module

def json_api_app(environ, start_response):
    """JSON API endpoint."""
    path = environ['PATH_INFO']

    if path == '/api/users':
        users = [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Charlie'}
        ]

        status = '200 OK'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)

        response = json_module.dumps(users).encode('utf-8')
        return [response]

    else:
        status = '404 Not Found'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)

        error = {'error': 'Not Found'}
        return [json_module.dumps(error).encode('utf-8')]
```

**Result**: JSON API with WSGI.

## Example 8: Middleware

Add middleware functionality:

```python
class LoggingMiddleware:
    """Middleware to log requests."""
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Log request
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        print(f'{method} {path}')

        # Call wrapped app
        return self.app(environ, start_response)

# Usage
def base_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b'Response']

# Wrap with middleware
app = LoggingMiddleware(base_app)
```

**Result**: Request logging middleware.

## Example 9: Session Management

Implement simple sessions:

```python
import secrets

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self):
        session_id = secrets.token_hex(16)
        self.sessions[session_id] = {}
        return session_id

    def get_session(self, session_id):
        return self.sessions.get(session_id, {})

    def set_session_data(self, session_id, key, value):
        if session_id in self.sessions:
            self.sessions[session_id][key] = value

session_mgr = SessionManager()

def session_app(environ, start_response):
    """WSGI app with sessions."""
    # Get cookie
    cookie = environ.get('HTTP_COOKIE', '')
    session_id = None

    if 'session_id=' in cookie:
        session_id = cookie.split('session_id=')[1].split(';')[0]

    if not session_id or session_id not in session_mgr.sessions:
        session_id = session_mgr.create_session()
        set_cookie = f'session_id={session_id}; Path=/'
        headers = [
            ('Content-Type', 'text/plain'),
            ('Set-Cookie', set_cookie)
        ]
    else:
        headers = [('Content-Type', 'text/plain')]

    session_data = session_mgr.get_session(session_id)

    status = '200 OK'
    start_response(status, headers)

    return [f'Session ID: {session_id}'.encode('utf-8')]
```

**Result**: Session management in WSGI.

## Example 10: Production WSGI Application

Complete WSGI application with routing and error handling:

```python
import json as json_module
from urllib.parse import parse_qs
from typing import Callable, List, Tuple

class WSGIApp:
    """Production-ready WSGI application."""

    def __init__(self):
        self.routes = {}

    def route(self, path: str, methods: List[str] = None):
        """Decorator to register routes."""
        if methods is None:
            methods = ['GET']

        def decorator(func: Callable):
            self.routes[path] = {'handler': func, 'methods': methods}
            return func
        return decorator

    def __call__(self, environ, start_response):
        """WSGI application entry point."""
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']

        # Find matching route
        route_config = self.routes.get(path)

        if not route_config:
            return self._not_found(environ, start_response)

        if method not in route_config['methods']:
            return self._method_not_allowed(environ, start_response)

        try:
            return route_config['handler'](environ, start_response)
        except Exception as e:
            return self._internal_error(environ, start_response, e)

    def _not_found(self, environ, start_response):
        status = '404 Not Found'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        error = {'error': 'Not Found', 'path': environ['PATH_INFO']}
        return [json_module.dumps(error).encode('utf-8')]

    def _method_not_allowed(self, environ, start_response):
        status = '405 Method Not Allowed'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        error = {'error': 'Method Not Allowed'}
        return [json_module.dumps(error).encode('utf-8')]

    def _internal_error(self, environ, start_response, exception):
        status = '500 Internal Server Error'
        headers = [('Content-Type', 'application/json')]
        start_response(status, headers)
        error = {'error': 'Internal Server Error', 'message': str(exception)}
        return [json_module.dumps(error).encode('utf-8')]

# Create application instance
app = WSGIApp()

@app.route('/', methods=['GET'])
def index(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    start_response(status, headers)
    response = {'message': 'Welcome to WSGI App'}
    return [json_module.dumps(response).encode('utf-8')]

@app.route('/users', methods=['GET'])
def get_users(environ, start_response):
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ]
    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    start_response(status, headers)
    return [json_module.dumps(users).encode('utf-8')]

@app.route('/echo', methods=['POST'])
def echo(environ, start_response):
    try:
        content_length = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        content_length = 0

    post_data = environ['wsgi.input'].read(content_length)

    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    start_response(status, headers)

    response = {'received': post_data.decode('utf-8')}
    return [json_module.dumps(response).encode('utf-8')]

# Run with: from wsgiref.simple_server import make_server
# server = make_server('localhost', 8000, app)
# server.serve_forever()
```

**Result**: Production-grade WSGI application framework.

## KEY TAKEAWAYS

- **WSGI Protocol**: Standard interface between web servers and Python apps
- **environ**: Dictionary containing request information
- **start_response**: Callable to set status and headers
- **Response**: Iterable of byte strings
- **Routing**: Match URL paths to handler functions
- **Middleware**: Wrap applications to add functionality
- **Status Codes**: Use proper HTTP status codes
- **Headers**: Set Content-Type and other HTTP headers
- **Query/POST Data**: Parse using urllib.parse
- **Production**: Use frameworks like Flask/Django that build on WSGI
'''

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Lesson 272: Web Scraping Basics
lesson272 = next(l for l in lessons if l['id'] == 272)
lesson272['content'] = '''# Web Scraping Basics

Extract data from websites using Python's urllib and html.parser modules. Web scraping enables automated data collection from web pages for analysis, monitoring, and integration. Understanding HTML parsing and HTTP requests is essential for effective web scraping.

## Example 1: Basic URL Fetch

Fetch web page content:

```python
import urllib.request

def fetch_page(url):
    """Fetch web page content."""
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Simulated fetch (without actual URL)
html_content = "<html><body><h1>Hello</h1></body></html>"
print(html_content[:100])
```

**Result**: Basic web page fetching.

## Example 2: HTML Parser

Parse HTML structure:

```python
from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []

    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}")
        if attrs:
            print(f"  Attributes: {attrs}")

    def handle_endtag(self, tag):
        print(f"End tag: {tag}")

    def handle_data(self, data):
        if data.strip():
            self.data.append(data.strip())

# Usage
parser = SimpleHTMLParser()
html = "<html><body><h1>Title</h1><p>Paragraph</p></body></html>"
parser.feed(html)
print(f"Extracted data: {parser.data}")
```

**Result**: Parse HTML tags and data.

## Example 3: Extract Links

Find all links in HTML:

```python
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.append(value)

# Usage
extractor = LinkExtractor()
html = '<a href="/page1">Link 1</a><a href="/page2">Link 2</a>'
extractor.feed(html)
print(f"Found links: {extractor.links}")
```

**Result**: Extract all hyperlinks.

## Example 4: Extract Specific Tags

Find specific HTML elements:

```python
from html.parser import HTMLParser

class TagExtractor(HTMLParser):
    def __init__(self, target_tag):
        super().__init__()
        self.target_tag = target_tag
        self.in_target = False
        self.results = []

    def handle_starttag(self, tag, attrs):
        if tag == self.target_tag:
            self.in_target = True

    def handle_endtag(self, tag):
        if tag == self.target_tag:
            self.in_target = False

    def handle_data(self, data):
        if self.in_target and data.strip():
            self.results.append(data.strip())

# Extract all h1 tags
extractor = TagExtractor('h1')
html = "<h1>Title 1</h1><p>Text</p><h1>Title 2</h1>"
extractor.feed(html)
print(f"H1 tags: {extractor.results}")
```

**Result**: Extract specific tag content.

## Example 5: Table Scraping

Extract table data:

```python
from html.parser import HTMLParser

class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table = False
        self.in_row = False
        self.in_cell = False
        self.current_row = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.in_table = True
        elif tag == 'tr' and self.in_table:
            self.in_row = True
            self.current_row = []
        elif tag in ('td', 'th') and self.in_row:
            self.in_cell = True

    def handle_endtag(self, tag):
        if tag == 'table':
            self.in_table = False
        elif tag == 'tr':
            if self.current_row:
                self.rows.append(self.current_row)
            self.in_row = False
        elif tag in ('td', 'th'):
            self.in_cell = False

    def handle_data(self, data):
        if self.in_cell and data.strip():
            self.current_row.append(data.strip())

# Usage
parser = TableParser()
html = """
<table>
    <tr><th>Name</th><th>Age</th></tr>
    <tr><td>Alice</td><td>30</td></tr>
    <tr><td>Bob</td><td>25</td></tr>
</table>
"""
parser.feed(html)
print("Table data:")
for row in parser.rows:
    print(row)
```

**Result**: Structured table data extraction.

## Example 6: HTTP Headers

Set custom headers:

```python
import urllib.request

def fetch_with_headers(url):
    """Fetch with custom headers."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Python Scraper)',
        'Accept': 'text/html'
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return None

# Simulated
print("Fetching with custom User-Agent header")
```

**Result**: Custom HTTP headers for scraping.

## Example 7: Handle Redirects

Follow HTTP redirects:

```python
import urllib.request
import urllib.error

def fetch_with_redirects(url, max_redirects=5):
    """Fetch URL, following redirects."""
    redirects = 0

    while redirects < max_redirects:
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                # Check if redirected
                final_url = response.geturl()
                if final_url != url:
                    print(f"Redirected to: {final_url}")
                    url = final_url
                    redirects += 1
                else:
                    return response.read().decode('utf-8')

        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                url = e.headers['Location']
                redirects += 1
            else:
                raise

    return None
```

**Result**: Redirect handling.

## Example 8: Rate Limiting

Implement request throttling:

```python
import time

class RateLimiter:
    def __init__(self, requests_per_second=1):
        self.delay = 1.0 / requests_per_second
        self.last_request = 0

    def wait(self):
        """Wait if necessary to respect rate limit."""
        now = time.time()
        time_since_last = now - self.last_request

        if time_since_last < self.delay:
            time.sleep(self.delay - time_since_last)

        self.last_request = time.time()

# Usage
limiter = RateLimiter(requests_per_second=2)

urls = ['url1', 'url2', 'url3']
for url in urls:
    limiter.wait()
    print(f"Fetching {url}")
    # fetch_page(url)
```

**Result**: Rate-limited requests.

## Example 9: Error Handling

Robust error handling:

```python
import urllib.request
import urllib.error

def safe_fetch(url, retries=3, timeout=10):
    """Fetch with error handling and retries."""
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return {
                    'success': True,
                    'data': response.read().decode('utf-8'),
                    'status': response.getcode()
                }

        except urllib.error.HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason}")
            if e.code >= 500 and attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            return {'success': False, 'error': f"HTTP {e.code}"}

        except urllib.error.URLError as e:
            print(f"URL Error: {e.reason}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return {'success': False, 'error': str(e.reason)}

        except Exception as e:
            return {'success': False, 'error': str(e)}

    return {'success': False, 'error': 'Max retries exceeded'}
```

**Result**: Resilient web scraping.

## Example 10: Production Web Scraper

Complete scraping framework:

```python
import urllib.request
import urllib.error
from html.parser import HTMLParser
import time
from typing import List, Dict, Optional

class WebScraper:
    """Production web scraping framework."""

    def __init__(self, rate_limit=1.0, user_agent=None):
        self.rate_limit = rate_limit
        self.last_request = 0
        self.user_agent = user_agent or 'Python WebScraper/1.0'

    def _wait_for_rate_limit(self):
        """Respect rate limiting."""
        if self.rate_limit > 0:
            now = time.time()
            time_since_last = now - self.last_request
            delay = 1.0 / self.rate_limit

            if time_since_last < delay:
                time.sleep(delay - time_since_last)

            self.last_request = time.time()

    def fetch(self, url: str, timeout: int = 10) -> Optional[str]:
        """Fetch URL with rate limiting."""
        self._wait_for_rate_limit()

        headers = {'User-Agent': self.user_agent}
        req = urllib.request.Request(url, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, html: str, base_url: str = '') -> List[str]:
        """Extract all links from HTML."""
        class LinkExtractor(HTMLParser):
            def __init__(self):
                super().__init__()
                self.links = []

            def handle_starttag(self, tag, attrs):
                if tag == 'a':
                    for attr, value in attrs:
                        if attr == 'href':
                            # Convert relative to absolute
                            if value.startswith('http'):
                                self.links.append(value)
                            elif base_url:
                                self.links.append(f"{base_url}{value}")

        extractor = LinkExtractor()
        extractor.feed(html)
        return extractor.links

    def extract_tag_content(self, html: str, tag: str) -> List[str]:
        """Extract content from specific tags."""
        class TagExtractor(HTMLParser):
            def __init__(self, target_tag):
                super().__init__()
                self.target_tag = target_tag
                self.in_target = False
                self.results = []

            def handle_starttag(self, tag, attrs):
                if tag == self.target_tag:
                    self.in_target = True

            def handle_endtag(self, tag):
                if tag == self.target_tag:
                    self.in_target = False

            def handle_data(self, data):
                if self.in_target and data.strip():
                    self.results.append(data.strip())

        extractor = TagExtractor(tag)
        extractor.feed(html)
        return extractor.results

# Usage
scraper = WebScraper(rate_limit=2.0)

# Simulated scraping
html = """
<html>
    <head><title>Page Title</title></head>
    <body>
        <h1>Main Heading</h1>
        <p>Paragraph 1</p>
        <p>Paragraph 2</p>
        <a href="/page1">Link 1</a>
        <a href="https://example.com/page2">Link 2</a>
    </body>
</html>
"""

# Extract titles
titles = scraper.extract_tag_content(html, 'h1')
print(f"Titles: {titles}")

# Extract paragraphs
paragraphs = scraper.extract_tag_content(html, 'p')
print(f"Paragraphs: {paragraphs}")

# Extract links
links = scraper.extract_links(html, base_url='https://example.com')
print(f"Links: {links}")
```

**Result**: Production-ready web scraping framework.

## KEY TAKEAWAYS

- **urllib.request**: Standard library for HTTP requests
- **HTMLParser**: Parse HTML structure and extract data
- **Rate Limiting**: Respect server resources with throttling
- **Error Handling**: Robust error handling and retries
- **User-Agent**: Set proper User-Agent header
- **Robots.txt**: Respect robots.txt and terms of service
- **CSS Selectors**: Use libraries like BeautifulSoup for complex parsing
- **Legal/Ethical**: Ensure scraping is legal and ethical
- **API First**: Prefer official APIs over scraping when available
- **Best Practices**: Handle redirects, timeouts, and HTTP errors properly
'''

# Lesson 273: WebRTC Peer-to-Peer Communication
lesson273 = next(l for l in lessons if l['id'] == 273)
lesson273['content'] = """# WebRTC - Peer-to-Peer Communication

Understand WebRTC concepts for peer-to-peer real-time communication. WebRTC (Web Real-Time Communication) enables direct browser-to-browser audio, video, and data transfer without intermediary servers, using signaling servers only for connection establishment.

## Example 1: WebRTC Connection Simulation

Simulate peer connection setup:

```python
import json

class RTCPeerConnection:
    def __init__(self):
        self.local_description = None
        self.remote_description = None
        self.ice_candidates = []
        self.state = 'new'

    def create_offer(self):
        '''Create SDP offer for connection.'''
        self.local_description = {
            'type': 'offer',
            'sdp': 'v=0 o=- 123 123 IN IP4 127.0.0.1...'
        }
        return self.local_description

    def create_answer(self):
        '''Create SDP answer.'''
        self.local_description = {
            'type': 'answer',
            'sdp': 'v=0 o=- 456 456 IN IP4 127.0.0.1...'
        }
        return self.local_description

    def set_local_description(self, description):
        '''Set local SDP description.'''
        self.local_description = description
        self.state = 'have-local-offer' if description['type'] == 'offer' else 'stable'

    def set_remote_description(self, description):
        '''Set remote SDP description.'''
        self.remote_description = description
        self.state = 'have-remote-offer' if description['type'] == 'offer' else 'stable'

    def add_ice_candidate(self, candidate):
        '''Add ICE candidate for NAT traversal.'''
        self.ice_candidates.append(candidate)

# Simulate peer connection
peer1 = RTCPeerConnection()
peer2 = RTCPeerConnection()

# Peer 1 creates offer
offer = peer1.create_offer()
peer1.set_local_description(offer)

# Send offer to peer 2 (via signaling server)
peer2.set_remote_description(offer)

# Peer 2 creates answer
answer = peer2.create_answer()
peer2.set_local_description(answer)

# Send answer back to peer 1
peer1.set_remote_description(answer)

print(f'Peer 1 state: {peer1.state}')
print(f'Peer 2 state: {peer2.state}')
```

**Result**: WebRTC peer connection simulation.

## Example 2: Signaling Server Concept

Understand signaling for WebRTC:

```python
class SignalingServer:
    def __init__(self):
        self.peers = {}
        self.messages = []

    def register_peer(self, peer_id):
        '''Register a peer.'''
        self.peers[peer_id] = {'connected': True}
        return True

    def send_message(self, from_peer, to_peer, message):
        '''Send signaling message between peers.'''
        self.messages.append({
            'from': from_peer,
            'to': to_peer,
            'message': message
        })

    def get_messages(self, peer_id):
        '''Get messages for a peer.'''
        return [m for m in self.messages if m['to'] == peer_id]

# Usage
server = SignalingServer()

# Peers register
server.register_peer('peer1')
server.register_peer('peer2')

# Peer 1 sends offer
server.send_message('peer1', 'peer2', {
    'type': 'offer',
    'sdp': 'offer-sdp-data'
})

# Peer 2 receives offer
messages = server.get_messages('peer2')
print(f'Peer 2 received: {messages}')
```

**Result**: Signaling server for WebRTC setup.

## KEY TAKEAWAYS

- **WebRTC**: Enables peer-to-peer real-time communication
- **SDP**: Session Description Protocol for connection parameters
- **ICE**: Interactive Connectivity Establishment for NAT traversal
- **Signaling**: Separate server needed for initial connection setup
- **Data Channel**: Send arbitrary data between peers
- **STUN/TURN**: Servers to help with NAT traversal
"""

print("Created comprehensive unique content for lessons 271-273:")
for lid in range(271, 274):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
