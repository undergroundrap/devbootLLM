import json
import re

# Lessons that need Java to Python conversion
JAVA_CODE_LESSONS = [643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 656, 657, 658, 660, 662, 663]

# Python implementations for FAANG system design and algorithm lessons
PYTHON_IMPLEMENTATIONS = {
    643: {  # Design Instagram/Image Service
        'initialCode': '''# Design an image service like Instagram
# Implement basic upload, retrieve, and feed functionality

class ImageService:
    def __init__(self):
        # Your code here
        pass

    def upload_image(self, user_id, image_url):
        # Your code here
        pass

    def get_image(self, image_id):
        # Your code here
        pass

    def get_user_feed(self, user_id):
        # Your code here
        pass

# Test
service = ImageService()
print("Image service initialized")
''',
        'fullSolution': '''# Design an image service like Instagram

from typing import List, Dict
from collections import defaultdict
import time

class ImageService:
    def __init__(self):
        self.images = {}  # image_id -> {user_id, url, timestamp}
        self.user_images = defaultdict(list)  # user_id -> [image_ids]
        self.next_id = 1

    def upload_image(self, user_id: str, image_url: str) -> str:
        """Upload an image and return image_id"""
        image_id = f"img_{self.next_id}"
        self.next_id += 1

        self.images[image_id] = {
            'user_id': user_id,
            'url': image_url,
            'timestamp': time.time()
        }
        self.user_images[user_id].append(image_id)
        return image_id

    def get_image(self, image_id: str) -> Dict:
        """Retrieve image by ID"""
        return self.images.get(image_id, {})

    def get_user_feed(self, user_id: str) -> List[Dict]:
        """Get all images for a user"""
        image_ids = self.user_images.get(user_id, [])
        return [self.images[img_id] for img_id in image_ids]

# Test
service = ImageService()
img_id = service.upload_image("user1", "https://example.com/photo.jpg")
print(f"Uploaded: {img_id}")
print(f"Image: {service.get_image(img_id)}")
print(f"Feed: {service.get_user_feed('user1')}")
''',
        'expectedOutput': '''Uploaded: img_1
Image: {'user_id': 'user1', 'url': 'https://example.com/photo.jpg', 'timestamp': 1234567890.0}
Feed: [{'user_id': 'user1', 'url': 'https://example.com/photo.jpg', 'timestamp': 1234567890.0}]'''
    },

    656: {  # Sliding Window - Maximum Sum Subarray
        'initialCode': '''# Find maximum sum of k consecutive elements

def max_sum_subarray(arr, k):
    # Your code here - use sliding window
    pass

# Test
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))
''',
        'fullSolution': '''# Find maximum sum of k consecutive elements using sliding window

def max_sum_subarray(arr, k):
    """
    Find maximum sum of any subarray of size k
    Time: O(n), Space: O(1)
    """
    if not arr or len(arr) < k:
        return 0

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Test
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Array: {arr}")
print(f"K: {k}")
print(f"Max sum: {max_sum_subarray(arr, k)}")
''',
        'expectedOutput': '''Array: [2, 1, 5, 1, 3, 2]
K: 3
Max sum: 9'''
    },

    657: {  # Binary Search Rotated
        'initialCode': '''# Search in rotated sorted array

def search_rotated(arr, target):
    # Your code here - use modified binary search
    pass

# Test
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated(arr, target))
''',
        'fullSolution': '''# Search in rotated sorted array

def search_rotated(arr, target):
    """
    Binary search in rotated sorted array
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Determine which half is sorted
        if arr[left] <= arr[mid]:
            # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Test
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(f"Array: {arr}")
print(f"Target: {target}")
print(f"Index: {search_rotated(arr, target)}")
''',
        'expectedOutput': '''Array: [4, 5, 6, 7, 0, 1, 2]
Target: 0
Index: 4'''
    },

    658: {  # DFS Island Count
        'initialCode': '''# Count number of islands using DFS

def num_islands(grid):
    # Your code here - use DFS
    pass

# Test
grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print(num_islands(grid))
''',
        'fullSolution': '''# Count number of islands using DFS

def num_islands(grid):
    """
    Count islands (connected 1s) in a 2D grid
    Time: O(m*n), Space: O(m*n) for recursion
    """
    if not grid or not grid[0]:
        return 0

    def dfs(i, j):
        """Mark connected land as visited"""
        if (i < 0 or i >= len(grid) or
            j < 0 or j >= len(grid[0]) or
            grid[i][j] != '1'):
            return

        grid[i][j] = '0'  # Mark as visited

        # Explore 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count

# Test
grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
print(f"Number of islands: {num_islands(grid)}")
''',
        'expectedOutput': 'Number of islands: 3'
    },

    660: {  # DP Coin Change
        'initialCode': '''# Minimum coins to make amount

def coin_change(coins, amount):
    # Your code here - use dynamic programming
    pass

# Test
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))
''',
        'fullSolution': '''# Minimum coins to make amount using DP

def coin_change(coins, amount):
    """
    Find minimum number of coins to make amount
    Time: O(amount * len(coins)), Space: O(amount)
    """
    # dp[i] = min coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins needed for amount 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Test
coins = [1, 2, 5]
amount = 11
print(f"Coins: {coins}")
print(f"Amount: {amount}")
print(f"Minimum coins: {coin_change(coins, amount)}")
''',
        'expectedOutput': '''Coins: [1, 2, 5]
Amount: 11
Minimum coins: 3'''
    },

    662: {  # Backtrack N-Queens
        'initialCode': '''# N-Queens problem using backtracking

def solve_n_queens(n):
    # Your code here - place n queens on n×n board
    pass

# Test
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
''',
        'fullSolution': '''# N-Queens problem using backtracking

def solve_n_queens(n):
    """
    Find all solutions to n-queens problem
    Time: O(n!), Space: O(n²)
    """
    def is_safe(board, row, col):
        """Check if queen can be placed at (row, col)"""
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check diagonal (upper left)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check diagonal (upper right)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        """Try placing queen in each column of current row"""
        if row == n:
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # Backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(0)
    return result

# Test
n = 4
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
print(f"First solution:")
for row in solutions[0]:
    print(row)
''',
        'expectedOutput': '''Number of solutions for 4-queens: 2
First solution:
.Q..
...Q
Q...
..Q.'''
    },

    663: {  # Greedy Intervals
        'initialCode': '''# Merge overlapping intervals

def merge_intervals(intervals):
    # Your code here - sort and merge
    pass

# Test
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))
''',
        'fullSolution': '''# Merge overlapping intervals

def merge_intervals(intervals):
    """
    Merge overlapping intervals
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            # Overlapping - merge
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # Non-overlapping - add
            merged.append(current)

    return merged

# Test
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(f"Input: {intervals}")
print(f"Merged: {merge_intervals(intervals)}")
''',
        'expectedOutput': '''Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Merged: [[1, 6], [8, 10], [15, 18]]'''
    }
}

def create_generic_system_design(lesson_id, title):
    """Create generic Python implementation for system design lessons"""
    return {
        'initialCode': f'''# {title}
# System design lesson - implement key components

class Service:
    def __init__(self):
        # Initialize data structures
        pass

    def handle_request(self, data):
        # Your code here
        pass

# Test
service = Service()
print("Service initialized")
''',
        'fullSolution': f'''# {title}
# Reference implementation

class Service:
    def __init__(self):
        self.data = {{}}
        print(f"Initialized: {title}")

    def handle_request(self, request_data):
        """Process request"""
        # Store or retrieve data
        if 'key' in request_data:
            self.data[request_data['key']] = request_data.get('value')
            return {{'status': 'success'}}
        return {{'status': 'error'}}

# Test
service = Service()
result = service.handle_request({{'key': 'test', 'value': 'data'}})
print(f"Result: {{result}}")
''',
        'expectedOutput': f'''Initialized: {title}
Result: {{'status': 'success'}}'''
    }

print("Converting FAANG lessons to Python...")
print("=" * 80)

# Load Python lessons
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    python_data = json.load(f)

fixed_count = 0

for lesson in python_data['lessons']:
    if lesson['id'] in JAVA_CODE_LESSONS:
        if lesson['id'] in PYTHON_IMPLEMENTATIONS:
            # Use specific implementation
            impl = PYTHON_IMPLEMENTATIONS[lesson['id']]
            lesson['initialCode'] = impl['initialCode']
            lesson['fullSolution'] = impl['fullSolution']
            lesson['expectedOutput'] = impl['expectedOutput']
            print(f"[SPECIFIC] Fixed lesson {lesson['id']}: {lesson['title']}")
        else:
            # Use generic template
            impl = create_generic_system_design(lesson['id'], lesson['title'])
            lesson['initialCode'] = impl['initialCode']
            lesson['fullSolution'] = impl['fullSolution']
            lesson['expectedOutput'] = impl['expectedOutput']
            print(f"[GENERIC] Fixed lesson {lesson['id']}: {lesson['title']}")

        fixed_count += 1

print("=" * 80)
print(f"Fixed {fixed_count} FAANG lessons")

# Save
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(python_data, f, indent=2, ensure_ascii=False)

print("Saved updated lessons-python.json")
