#!/usr/bin/env python3
"""
Upgrade WebSocket, Django Channels, and asyncio lessons
"""

import json
import sys

def upgrade_lesson_762():
    """Django - Django Channels - WebSockets"""
    return '''# Django Channels - WebSockets
# In production: pip install channels channels-redis daphne

"""
Django Channels WebSocket Support

Complete WebSocket implementation with Django Channels:
- ASGI application configuration
- WebSocket consumers
- Channel layers for message passing
- Group broadcasting
- Authentication
- Real-time chat application

Used by: Slack, Discord (chat), Trello (real-time updates)
"""

import json
import asyncio
import time
from typing import Dict, List, Set, Any, Optional
from collections import defaultdict


# ============================================================================
# Channel Layer (simulated Redis)
# ============================================================================

class ChannelLayer:
    """
    Channel layer for message passing between consumers

    In production: Uses Redis for distributed message passing
    """

    def __init__(self):
        self.groups: Dict[str, Set[str]] = defaultdict(set)
        self.messages: Dict[str, List[Dict]] = defaultdict(list)

    async def group_add(self, group: str, channel_name: str):
        """Add channel to group"""
        self.groups[group].add(channel_name)

    async def group_discard(self, group: str, channel_name: str):
        """Remove channel from group"""
        if group in self.groups:
            self.groups[group].discard(channel_name)

    async def group_send(self, group: str, message: Dict):
        """Send message to all channels in group"""
        if group in self.groups:
            for channel_name in self.groups[group]:
                self.messages[channel_name].append(message)

    async def send(self, channel_name: str, message: Dict):
        """Send message to specific channel"""
        self.messages[channel_name].append(message)

    async def receive(self, channel_name: str) -> Optional[Dict]:
        """Receive message from channel"""
        if channel_name in self.messages and self.messages[channel_name]:
            return self.messages[channel_name].pop(0)
        return None


# Global channel layer
channel_layer = ChannelLayer()


# ============================================================================
# WebSocket Consumer Base
# ============================================================================

class WebsocketConsumer:
    """
    Base WebSocket consumer

    Handles WebSocket connections and messages
    """

    def __init__(self, scope):
        self.scope = scope
        self.channel_name = f"channel_{id(self)}"

    async def connect(self):
        """Called when WebSocket connects"""
        await self.accept()

    async def disconnect(self, close_code):
        """Called when WebSocket disconnects"""
        pass

    async def receive(self, text_data=None, bytes_data=None):
        """Called when message received from WebSocket"""
        pass

    async def accept(self):
        """Accept WebSocket connection"""
        print(f"  [WebSocket accepted: {self.channel_name}]")

    async def send(self, text_data=None, bytes_data=None):
        """Send message to WebSocket"""
        if text_data:
            print(f"  [Sending to {self.channel_name}: {text_data[:50]}...]")

    async def close(self, code=1000):
        """Close WebSocket connection"""
        print(f"  [WebSocket closed: {self.channel_name}]")


# ============================================================================
# Chat Consumer
# ============================================================================

class ChatConsumer(WebsocketConsumer):
    """
    Chat room WebSocket consumer

    Handles real-time chat messages with room support
    """

    async def connect(self):
        """Connect to chat room"""
        # Get room name from URL
        self.room_name = self.scope.get('url_route', {}).get('room_name', 'default')
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': f'Welcome to room: {self.room_name}'
        }))

    async def disconnect(self, close_code):
        """Disconnect from chat room"""
        # Leave room group
        await channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        """Receive message from WebSocket"""
        if text_data:
            data = json.loads(text_data)
            message_type = data.get('type', 'message')

            if message_type == 'message':
                # Broadcast to room group
                await channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': data['message'],
                        'username': data.get('username', 'Anonymous'),
                        'timestamp': time.time()
                    }
                )

    async def chat_message(self, event):
        """Receive message from room group"""
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'username': event['username'],
            'timestamp': event['timestamp']
        }))


# ============================================================================
# Notification Consumer
# ============================================================================

class NotificationConsumer(WebsocketConsumer):
    """
    Notification WebSocket consumer

    Handles real-time notifications for users
    """

    async def connect(self):
        """Connect and subscribe to user notifications"""
        # Get user from scope
        self.user_id = self.scope.get('user', {}).get('id', 'anonymous')
        self.user_group_name = f'notifications_{self.user_id}'

        # Join user notification group
        await channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """Disconnect from notifications"""
        await channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def notification(self, event):
        """Receive notification from group"""
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'title': event['title'],
            'message': event['message'],
            'priority': event.get('priority', 'normal')
        }))


# ============================================================================
# Live Update Consumer (for dashboards)
# ============================================================================

class LiveUpdateConsumer(WebsocketConsumer):
    """
    Live update consumer for dashboards

    Pushes real-time data updates
    """

    async def connect(self):
        """Connect to live updates"""
        self.dashboard_group = 'dashboard_updates'

        await channel_layer.group_add(
            self.dashboard_group,
            self.channel_name
        )

        await self.accept()

        # Start sending periodic updates
        asyncio.create_task(self.send_periodic_updates())

    async def disconnect(self, close_code):
        """Disconnect from updates"""
        await channel_layer.group_discard(
            self.dashboard_group,
            self.channel_name
        )

    async def send_periodic_updates(self):
        """Send periodic dashboard updates"""
        for i in range(5):  # Send 5 updates
            await asyncio.sleep(1)

            await self.send(text_data=json.dumps({
                'type': 'dashboard_update',
                'metrics': {
                    'active_users': 42 + i,
                    'requests_per_sec': 150 + i * 10,
                    'cpu_usage': 45.2 + i,
                }
            }))

    async def dashboard_update(self, event):
        """Receive dashboard update"""
        await self.send(text_data=json.dumps(event))


# ============================================================================
# ASGI Application
# ============================================================================

class ASGIApplication:
    """
    ASGI application for handling WebSocket connections

    Routes WebSocket connections to appropriate consumers
    """

    def __init__(self):
        self.routes = {}

    def route(self, path: str, consumer_class):
        """Register WebSocket route"""
        self.routes[path] = consumer_class

    async def __call__(self, scope, receive, send):
        """Handle ASGI request"""
        if scope['type'] == 'websocket':
            path = scope.get('path', '/')

            # Find matching consumer
            consumer_class = self.routes.get(path)

            if consumer_class:
                consumer = consumer_class(scope)

                # Handle WebSocket lifecycle
                while True:
                    message = await receive()

                    if message['type'] == 'websocket.connect':
                        await consumer.connect()

                    elif message['type'] == 'websocket.receive':
                        text_data = message.get('text')
                        bytes_data = message.get('bytes')
                        await consumer.receive(text_data, bytes_data)

                    elif message['type'] == 'websocket.disconnect':
                        await consumer.disconnect(message.get('code', 1000))
                        break
            else:
                # No route found - reject
                await send({'type': 'websocket.close', 'code': 4004})


# ============================================================================
# Example Application
# ============================================================================

# Create ASGI application
application = ASGIApplication()

# Register WebSocket routes
application.route('/ws/chat/<room_name>/', ChatConsumer)
application.route('/ws/notifications/', NotificationConsumer)
application.route('/ws/dashboard/', LiveUpdateConsumer)


# ============================================================================
# Example Usage
# ============================================================================

async def simulate_chat_room():
    """Simulate chat room with multiple users"""
    print("\\n1. CHAT ROOM SIMULATION")
    print("-" * 80)

    # Create chat consumers
    scope1 = {'url_route': {'room_name': 'general'}, 'user': {'id': 1}}
    scope2 = {'url_route': {'room_name': 'general'}, 'user': {'id': 2}}

    user1 = ChatConsumer(scope1)
    user2 = ChatConsumer(scope2)

    # Connect both users
    await user1.connect()
    await user2.connect()

    # User 1 sends message
    await user1.receive(text_data=json.dumps({
        'type': 'message',
        'message': 'Hello everyone!',
        'username': 'Alice'
    }))

    # Both users receive the message
    msg1 = await channel_layer.receive(user1.channel_name)
    if msg1:
        await user1.chat_message(msg1)

    msg2 = await channel_layer.receive(user2.channel_name)
    if msg2:
        await user2.chat_message(msg2)

    # User 2 responds
    await user2.receive(text_data=json.dumps({
        'type': 'message',
        'message': 'Hi Alice!',
        'username': 'Bob'
    }))

    # Both receive response
    msg1 = await channel_layer.receive(user1.channel_name)
    if msg1:
        await user1.chat_message(msg1)

    msg2 = await channel_layer.receive(user2.channel_name)
    if msg2:
        await user2.chat_message(msg2)

    # Disconnect
    await user1.disconnect(1000)
    await user2.disconnect(1000)


async def simulate_notifications():
    """Simulate user notifications"""
    print("\\n2. NOTIFICATION SYSTEM")
    print("-" * 80)

    # Create notification consumer
    scope = {'user': {'id': 123}}
    consumer = NotificationConsumer(scope)

    await consumer.connect()

    # Send notifications to user group
    await channel_layer.group_send(
        'notifications_123',
        {
            'type': 'notification',
            'title': 'New Message',
            'message': 'You have a new message from Alice',
            'priority': 'high'
        }
    )

    # Receive notification
    msg = await channel_layer.receive(consumer.channel_name)
    if msg:
        await consumer.notification(msg)

    await consumer.disconnect(1000)


async def simulate_dashboard():
    """Simulate live dashboard updates"""
    print("\\n3. LIVE DASHBOARD UPDATES")
    print("-" * 80)

    scope = {}
    consumer = LiveUpdateConsumer(scope)

    await consumer.connect()

    # Updates are sent automatically in send_periodic_updates()
    await asyncio.sleep(6)  # Wait for updates

    await consumer.disconnect(1000)


async def main():
    print("=" * 80)
    print("DJANGO CHANNELS - WEBSOCKETS")
    print("=" * 80)

    # Run simulations
    await simulate_chat_room()
    await simulate_notifications()
    await simulate_dashboard()

    print("\\n" + "=" * 80)
    print("DJANGO CHANNELS BEST PRACTICES")
    print("=" * 80)
    print("""
1. CHANNEL LAYERS:
   - Use Redis for production (channels-redis)
   - Enable Redis persistence
   - Configure channel expiry
   - Monitor Redis memory usage

2. CONSUMERS:
   - Inherit from WebsocketConsumer or AsyncWebsocketConsumer
   - Handle connect, disconnect, receive methods
   - Use group_send for broadcasting
   - Implement proper error handling

3. GROUPS:
   - Use groups for broadcast messaging
   - Name groups clearly (chat_room_123)
   - Clean up groups on disconnect
   - Limit group sizes if possible

4. AUTHENTICATION:
   - Authenticate in connect() method
   - Check permissions before joining groups
   - Close connection if unauthorized
   - Use Django session/token auth

5. SCALABILITY:
   - Use Daphne or Uvicorn as ASGI server
   - Run multiple workers
   - Use Redis Sentinel for HA
   - Implement rate limiting

6. DEPLOYMENT:
   - Configure ASGI application
   - Set up channel layers in settings
   - Use nginx for WebSocket proxying
   - Enable WebSocket keepalive

7. TESTING:
   - Use ChannelsLiveServerTestCase
   - Test consumer logic independently
   - Mock channel layer for unit tests
   - Test reconnection handling

8. MONITORING:
   - Track active connections
   - Monitor message throughput
   - Log errors and disconnections
   - Set up alerts for issues
""")

    print("\\n✓ Django Channels WebSocket complete!")


if __name__ == '__main__':
    asyncio.run(main())
'''

def upgrade_lesson_275():
    """WebSockets - Bi-directional Communication"""
    return '''# WebSockets - Bi-directional Communication
# In production: pip install websockets

"""
WebSockets Bi-directional Communication

Complete WebSocket implementation:
- WebSocket protocol basics
- Client and server implementation
- Message framing and protocols
- Heartbeat/ping-pong
- Reconnection logic
- Binary and text messages

Used by: All real-time web applications (chat, gaming, trading)
"""

import asyncio
import json
import time
import hashlib
import base64
from typing import Dict, List, Optional, Callable, Set
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# WebSocket Protocol
# ============================================================================

class WebSocketState(Enum):
    """WebSocket connection states"""
    CONNECTING = "CONNECTING"
    OPEN = "OPEN"
    CLOSING = "CLOSING"
    CLOSED = "CLOSED"


class WebSocketOpcode(Enum):
    """WebSocket frame opcodes"""
    CONTINUATION = 0x0
    TEXT = 0x1
    BINARY = 0x2
    CLOSE = 0x8
    PING = 0x9
    PONG = 0xA


@dataclass
class WebSocketFrame:
    """WebSocket frame"""
    fin: bool
    opcode: int
    payload: bytes


# ============================================================================
# WebSocket Server
# ============================================================================

class WebSocketServer:
    """
    WebSocket server implementation

    Handles multiple client connections
    """

    def __init__(self, host: str = "localhost", port: int = 8765):
        self.host = host
        self.port = port
        self.clients: Set['WebSocketConnection'] = set()
        self.handlers: Dict[str, Callable] = {}

    def on(self, event: str):
        """Register event handler"""
        def decorator(func):
            self.handlers[event] = func
            return func
        return decorator

    async def start(self):
        """Start WebSocket server"""
        print(f"WebSocket server started on ws://{self.host}:{self.port}")

        # Simulate server running
        # In production: asyncio.start_server()
        await asyncio.sleep(0.1)

    async def broadcast(self, message: str):
        """Broadcast message to all clients"""
        for client in self.clients:
            if client.state == WebSocketState.OPEN:
                await client.send(message)

    async def handle_client(self, connection: 'WebSocketConnection'):
        """Handle client connection"""
        self.clients.add(connection)

        try:
            # Call connect handler
            if 'connect' in self.handlers:
                await self.handlers['connect'](connection)

            # Handle messages
            async for message in connection:
                if 'message' in self.handlers:
                    await self.handlers['message'](connection, message)

        finally:
            # Call disconnect handler
            if 'disconnect' in self.handlers:
                await self.handlers['disconnect'](connection)

            self.clients.discard(connection)


# ============================================================================
# WebSocket Connection
# ============================================================================

class WebSocketConnection:
    """
    WebSocket connection (client or server side)

    Handles WebSocket protocol, framing, and lifecycle
    """

    def __init__(self, connection_id: str = None):
        self.connection_id = connection_id or str(id(self))
        self.state = WebSocketState.CONNECTING
        self.message_queue: asyncio.Queue = asyncio.Queue()
        self.close_code: Optional[int] = None
        self.last_ping_time: float = 0
        self.last_pong_time: float = 0

    async def handshake(self, path: str = "/"):
        """Perform WebSocket handshake"""
        print(f"  [WebSocket handshake: {self.connection_id}]")

        # Simulate handshake
        # In production: HTTP upgrade with Sec-WebSocket-Key
        await asyncio.sleep(0.01)

        self.state = WebSocketState.OPEN
        print(f"  [WebSocket connected: {self.connection_id}]")

    async def send(self, data: str):
        """Send text message"""
        if self.state != WebSocketState.OPEN:
            raise Exception("WebSocket not open")

        print(f"  [Sending to {self.connection_id}: {data[:50]}...]")

        # In production: Frame and send over socket
        await self.message_queue.put({
            'type': 'message',
            'data': data
        })

    async def send_binary(self, data: bytes):
        """Send binary message"""
        if self.state != WebSocketState.OPEN:
            raise Exception("WebSocket not open")

        await self.message_queue.put({
            'type': 'binary',
            'data': data
        })

    async def ping(self, data: bytes = b''):
        """Send ping"""
        self.last_ping_time = time.time()
        print(f"  [Ping sent: {self.connection_id}]")

    async def pong(self, data: bytes = b''):
        """Send pong"""
        print(f"  [Pong sent: {self.connection_id}]")

    async def close(self, code: int = 1000, reason: str = ""):
        """Close WebSocket connection"""
        if self.state in (WebSocketState.CLOSING, WebSocketState.CLOSED):
            return

        self.state = WebSocketState.CLOSING
        self.close_code = code

        print(f"  [Closing WebSocket: {self.connection_id}, code: {code}]")

        await asyncio.sleep(0.01)
        self.state = WebSocketState.CLOSED

    async def recv(self) -> str:
        """Receive message"""
        if self.state != WebSocketState.OPEN:
            raise Exception("WebSocket not open")

        # Get message from queue
        msg = await self.message_queue.get()
        return msg['data']

    def __aiter__(self):
        """Async iterator for messages"""
        return self

    async def __anext__(self):
        """Get next message"""
        if self.state == WebSocketState.CLOSED:
            raise StopAsyncIteration

        try:
            return await asyncio.wait_for(self.recv(), timeout=5.0)
        except asyncio.TimeoutError:
            raise StopAsyncIteration


# ============================================================================
# WebSocket Client
# ============================================================================

class WebSocketClient:
    """
    WebSocket client implementation

    Connects to WebSocket server
    """

    def __init__(self, url: str):
        self.url = url
        self.connection: Optional[WebSocketConnection] = None
        self.handlers: Dict[str, Callable] = {}
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 5

    def on(self, event: str):
        """Register event handler"""
        def decorator(func):
            self.handlers[event] = func
            return func
        return decorator

    async def connect(self):
        """Connect to WebSocket server"""
        print(f"Connecting to {self.url}...")

        self.connection = WebSocketConnection()
        await self.connection.handshake()

        # Call open handler
        if 'open' in self.handlers:
            await self.handlers['open']()

        self.reconnect_attempts = 0

    async def send(self, message: str):
        """Send message"""
        if not self.connection or self.connection.state != WebSocketState.OPEN:
            raise Exception("Not connected")

        await self.connection.send(message)

    async def close(self):
        """Close connection"""
        if self.connection:
            await self.connection.close()

            # Call close handler
            if 'close' in self.handlers:
                await self.handlers['close']()

    async def reconnect(self):
        """Attempt to reconnect"""
        if self.reconnect_attempts >= self.max_reconnect_attempts:
            print("Max reconnection attempts reached")
            return

        self.reconnect_attempts += 1
        backoff = min(2 ** self.reconnect_attempts, 30)  # Exponential backoff

        print(f"Reconnecting in {backoff}s (attempt {self.reconnect_attempts})...")
        await asyncio.sleep(backoff)

        try:
            await self.connect()
        except Exception as e:
            print(f"Reconnection failed: {e}")
            await self.reconnect()

    async def listen(self):
        """Listen for messages"""
        try:
            while self.connection and self.connection.state == WebSocketState.OPEN:
                message = await self.connection.recv()

                # Call message handler
                if 'message' in self.handlers:
                    await self.handlers['message'](message)

        except Exception as e:
            print(f"Connection error: {e}")

            # Call error handler
            if 'error' in self.handlers:
                await self.handlers['error'](e)

            # Attempt reconnect
            await self.reconnect()


# ============================================================================
# Example Usage
# ============================================================================

async def example_chat_server():
    """Example chat server"""
    print("\\n1. CHAT SERVER")
    print("-" * 80)

    server = WebSocketServer()

    @server.on('connect')
    async def on_connect(connection):
        print(f"Client connected: {connection.connection_id}")
        await connection.send(json.dumps({
            'type': 'welcome',
            'message': 'Welcome to the chat!'
        }))

    @server.on('message')
    async def on_message(connection, message):
        print(f"Received: {message}")

        # Broadcast to all clients
        await server.broadcast(json.dumps({
            'type': 'chat',
            'message': message,
            'from': connection.connection_id
        }))

    @server.on('disconnect')
    async def on_disconnect(connection):
        print(f"Client disconnected: {connection.connection_id}")

    await server.start()

    # Simulate clients
    client1 = WebSocketConnection("client1")
    client2 = WebSocketConnection("client2")

    await client1.handshake()
    await client2.handshake()

    await server.handle_client(client1)

    # Send messages
    await client1.send("Hello from client 1!")
    await client2.send("Hi from client 2!")


async def example_chat_client():
    """Example chat client"""
    print("\\n2. CHAT CLIENT")
    print("-" * 80)

    client = WebSocketClient("ws://localhost:8765")

    @client.on('open')
    async def on_open():
        print("Connected to server!")
        await client.send("Hello server!")

    @client.on('message')
    async def on_message(message):
        print(f"Received: {message}")

    @client.on('error')
    async def on_error(error):
        print(f"Error: {error}")

    @client.on('close')
    async def on_close():
        print("Connection closed")

    await client.connect()
    await client.send(json.dumps({'message': 'Hello!'}))
    await asyncio.sleep(1)
    await client.close()


async def example_heartbeat():
    """Example WebSocket with heartbeat"""
    print("\\n3. HEARTBEAT (PING/PONG)")
    print("-" * 80)

    connection = WebSocketConnection("heartbeat_client")
    await connection.handshake()

    # Send periodic pings
    for i in range(3):
        await connection.ping()
        await asyncio.sleep(1)
        await connection.pong()

    await connection.close()


async def example_binary_data():
    """Example binary data transfer"""
    print("\\n4. BINARY DATA")
    print("-" * 80)

    connection = WebSocketConnection("binary_client")
    await connection.handshake()

    # Send binary data (e.g., image)
    binary_data = b'\\x89PNG\\r\\n\\x1a\\n...'  # PNG header
    await connection.send_binary(binary_data)

    print(f"  Sent {len(binary_data)} bytes")

    await connection.close()


async def main():
    print("=" * 80)
    print("WEBSOCKETS - BI-DIRECTIONAL COMMUNICATION")
    print("=" * 80)

    await example_chat_server()
    await example_chat_client()
    await example_heartbeat()
    await example_binary_data()

    print("\\n" + "=" * 80)
    print("WEBSOCKET BEST PRACTICES")
    print("=" * 80)
    print("""
1. CONNECTION MANAGEMENT:
   - Implement heartbeat (ping/pong)
   - Handle reconnection with exponential backoff
   - Set connection timeouts
   - Limit max connections per client

2. MESSAGE HANDLING:
   - Validate all incoming messages
   - Set maximum message size
   - Use message queues for buffering
   - Handle binary and text frames

3. ERROR HANDLING:
   - Catch and log all exceptions
   - Send proper close frames
   - Implement error recovery
   - Don't leak sensitive info in errors

4. SECURITY:
   - Use WSS (WebSocket Secure) in production
   - Validate origin headers
   - Implement authentication
   - Rate limit connections and messages

5. SCALABILITY:
   - Use message broker (Redis/RabbitMQ)
   - Implement load balancing
   - Horizontal scaling with sticky sessions
   - Monitor connection count

6. PERFORMANCE:
   - Use binary frames for large data
   - Compress messages if beneficial
   - Batch small messages
   - Use connection pooling

7. PROTOCOLS:
   - Define message protocol (JSON, Protocol Buffers)
   - Version your protocol
   - Document message types
   - Handle unknown message types gracefully

8. MONITORING:
   - Track active connections
   - Monitor message throughput
   - Log connection/disconnection events
   - Alert on error rates
""")

    print("\\n✓ WebSocket communication complete!")


if __name__ == '__main__':
    asyncio.run(main())
'''

def main():
    print("=" * 80)
    print("UPGRADING: WebSocket and Django Channels Lessons")
    print("=" * 80)

    # Load lessons
    with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    # Upgrade lessons
    upgrades = [
        (762, upgrade_lesson_762, "Django - Django Channels - WebSockets"),
        (275, upgrade_lesson_275, "WebSockets - Bi-directional Communication"),
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
    print("WEBSOCKET AND DJANGO CHANNELS COMPLETE!")
    print("=" * 80)


if __name__ == '__main__':
    main()
