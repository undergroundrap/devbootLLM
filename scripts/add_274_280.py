#!/usr/bin/env python3
import json

with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Lesson 274: WebSocket Chat Application
lesson274 = next(l for l in lessons if l['id'] == 274)
lesson274['content'] = """# WebSocket - Chat Application

Build real-time chat applications using WebSocket for bidirectional communication.

## Example 1: WebSocket Client Simulation

```python
class WebSocketClient:
    def __init__(self):
        self.connected = False
        self.handlers = {}

    def connect(self, url):
        self.connected = True
        if 'open' in self.handlers:
            self.handlers['open']()

    def send(self, message):
        if not self.connected:
            raise RuntimeError('Not connected')
        print(f'Sending: {message}')

    def on(self, event, handler):
        self.handlers[event] = handler

ws = WebSocketClient()
ws.on('open', lambda: print('Connected'))
ws.connect('ws://localhost:8080')
ws.send('Hello')
```

## KEY TAKEAWAYS

- **Persistent Connection**: WebSocket maintains open connection
- **Real-Time**: Instant message delivery
- **Events**: Handle open, message, close, error events
"""

# Lesson 275: WebSockets Bi-directional Communication
lesson275 = next(l for l in lessons if l['id'] == 275)
lesson275['content'] = """# WebSockets - Bi-directional Communication

Implement full-duplex communication using WebSocket protocol.

## Example 1: WebSocket Lifecycle

```python
class WebSocket:
    def __init__(self):
        self.ready_state = 'CONNECTING'
        self.handlers = {}

    def on(self, event, handler):
        self.handlers[event] = handler

    def connect(self):
        self.ready_state = 'OPEN'
        if 'open' in self.handlers:
            self.handlers['open']()

    def send(self, data):
        if self.ready_state != 'OPEN':
            raise RuntimeError('Cannot send')
        print(f'Sent: {data}')

ws = WebSocket()
ws.on('open', lambda: print('Opened'))
ws.connect()
ws.send('Message')
```

## KEY TAKEAWAYS

- **Full-Duplex**: Both parties can send simultaneously
- **States**: CONNECTING, OPEN, CLOSING, CLOSED
- **Events**: open, message, error, close
"""

# Lesson 276: sqlite3 In-Memory
lesson276 = next(l for l in lessons if l['id'] == 276)
lesson276['content'] = """# sqlite3 In-Memory

Use in-memory SQLite databases for testing and temporary storage.

## Example 1: Basic In-Memory DB

```python
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute("INSERT INTO users (name) VALUES (?)", ('Alice',))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
```

## KEY TAKEAWAYS

- **In-Memory**: Use ':memory:' as database name
- **Fast**: No disk I/O, stored in RAM
- **Temporary**: Data lost when connection closes
"""

# Lesson 277: Linked List Implementation
lesson277 = next(l for l in lessons if l['id'] == 277)
lesson277['content'] = """# Linked List Implementation

Implement linked lists for efficient insertion and deletion.

## Example 1: Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
print(ll.display())  # [1, 2, 3]
```

## KEY TAKEAWAYS

- **Node**: Contains data and next pointer
- **Head**: First node in list
- **O(1) Insert**: At beginning
- **O(n) Search**: Linear traversal
"""

# Lesson 278: Graph Representation and Traversal
lesson278 = next(l for l in lessons if l['id'] == 278)
lesson278['content'] = """# Graph Representation and Traversal

Represent graphs and implement BFS/DFS traversal.

## Example 1: Adjacency List

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

print(g.get_neighbors('A'))  # ['B', 'C']
```

## Example 2: BFS

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result

print(bfs(g, 'A'))
```

## KEY TAKEAWAYS

- **Adjacency List**: Dict of vertex -> neighbors
- **BFS**: Level-order using queue
- **DFS**: Depth-first using recursion
"""

# Lesson 279: Variable Arguments
lesson279 = next(l for l in lessons if l['id'] == 279)
lesson279['content'] = """# Variable Arguments: *args and **kwargs

Use *args and **kwargs for flexible function signatures.

## Example 1: *args

```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15
```

## Example 2: **kwargs

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)
# name: Alice
# age: 30
```

## Example 3: Combine Both

```python
def func(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

func(1, 2, 3, a='A', b='B')
```

## KEY TAKEAWAYS

- ***args**: Positional arguments as tuple
- ****kwargs**: Keyword arguments as dict
- **Unpacking**: *list or **dict
- **Flexibility**: Accept any number of arguments
"""

# Lesson 280: Lambda Functions
lesson280 = next(l for l in lessons if l['id'] == 280)
lesson280['content'] = """# Lambda Functions

Create anonymous inline functions using lambda expressions.

## Example 1: Basic Lambda

```python
square = lambda x: x ** 2
print(square(5))  # 25
```

## Example 2: Lambda with map()

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

## Example 3: Lambda with filter()

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]
```

## Example 4: Lambda with sorted()

```python
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_by_age = sorted(users, key=lambda x: x['age'])
print([u['name'] for u in sorted_by_age])
# ['Bob', 'Alice', 'Charlie']
```

## KEY TAKEAWAYS

- **Syntax**: lambda args: expression
- **Anonymous**: No function name
- **Single Expression**: One expression only
- **Use Cases**: map(), filter(), sorted()
"""

with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("Created lessons 274-280:")
for lid in range(274, 281):
    lesson = next(l for l in lessons if l['id'] == lid)
    chars = len(lesson['content'])
    print(f"  {lid}: {lesson['title'][:45]:45s} {chars:5,d} chars")
