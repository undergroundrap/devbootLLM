#!/usr/bin/env python3
"""
Upgrade Python lessons 101-110 with comprehensive content.
- Lesson 101: asyncio.Semaphore (limit concurrency)
- Lesson 102: typing.TypedDict
- Lesson 103: Adding to Sets
- Lesson 104: Removing from Sets
- Lesson 105: Set Basics
- Lesson 106: Set Comprehension
- Lesson 107: Set Operations
- Lesson 108: @classmethod
- Lesson 109: @staticmethod
- Lesson 110: Class __init__ Method
"""

import json

# Read the lessons file
with open('public/lessons-python.json', 'r', encoding='utf-8') as f:
    lessons = json.load(f)

# Find lessons 101-110
lesson101 = next(l for l in lessons if l['id'] == 101)
lesson102 = next(l for l in lessons if l['id'] == 102)
lesson103 = next(l for l in lessons if l['id'] == 103)
lesson104 = next(l for l in lessons if l['id'] == 104)
lesson105 = next(l for l in lessons if l['id'] == 105)
lesson106 = next(l for l in lessons if l['id'] == 106)
lesson107 = next(l for l in lessons if l['id'] == 107)
lesson108 = next(l for l in lessons if l['id'] == 108)
lesson109 = next(l for l in lessons if l['id'] == 109)
lesson110 = next(l for l in lessons if l['id'] == 110)

# Upgrade Lesson 101: asyncio.Semaphore
lesson101['fullSolution'] = '''"""
asyncio.Semaphore - Limit Concurrency

Master semaphores for controlling concurrent access to resources in asyncio.
Learn to limit parallel operations, prevent resource exhaustion, and manage
connection pools. Essential for production async applications.

**Zero Package Installation Required**
"""

# Example 1: Basic Semaphore - Limit Concurrent Tasks
print("="*70)
print("Example 1: Basic Semaphore Usage")
print("="*70)

import asyncio

async def worker(semaphore, worker_id):
    """Worker that requires semaphore to run"""
    print(f"Worker {worker_id} waiting for semaphore...")

    async with semaphore:
        print(f"Worker {worker_id} acquired semaphore, starting work")
        await asyncio.sleep(1)  # Simulate work
        print(f"Worker {worker_id} finished work, releasing semaphore")

async def example1():
    # Allow only 2 concurrent workers
    semaphore = asyncio.Semaphore(2)

    # Start 5 workers
    tasks = [worker(semaphore, i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(example1())
print()

# Example 2: Semaphore vs No Semaphore
print("="*70)
print("Example 2: With vs Without Semaphore")
print("="*70)

import time

async def download_without_limit(url_id):
    """Simulate download without limit"""
    print(f"  Downloading {url_id}...")
    await asyncio.sleep(0.5)
    return f"Data {url_id}"

async def download_with_limit(semaphore, url_id):
    """Simulate download with semaphore limit"""
    async with semaphore:
        print(f"  Downloading {url_id} (max 3 concurrent)...")
        await asyncio.sleep(0.5)
        return f"Data {url_id}"

async def example2():
    # Without limit - all start at once
    print("Without semaphore (all at once):")
    start = time.time()
    results = await asyncio.gather(*[download_without_limit(i) for i in range(10)])
    print(f"Completed in {time.time() - start:.2f}s\\n")

    # With semaphore - max 3 concurrent
    print("With semaphore (max 3 concurrent):")
    start = time.time()
    sem = asyncio.Semaphore(3)
    results = await asyncio.gather(*[download_with_limit(sem, i) for i in range(10)])
    print(f"Completed in {time.time() - start:.2f}s")

asyncio.run(example2())
print()

# Example 3: Prevent Resource Exhaustion
print("="*70)
print("Example 3: Protect Limited Resource (Database Connections)")
print("="*70)

async def query_database(semaphore, query_id, connection_pool_size):
    """Simulate database query with limited connections"""
    async with semaphore:
        print(f"Query {query_id}: Acquired connection from pool ({connection_pool_size} max)")
        await asyncio.sleep(0.3)  # Simulate query
        print(f"Query {query_id}: Released connection")
        return f"Result {query_id}"

async def example3():
    max_connections = 5
    semaphore = asyncio.Semaphore(max_connections)

    print(f"Database connection pool: {max_connections} connections\\n")

    # Execute 15 queries with limited connections
    queries = [query_database(semaphore, i, max_connections) for i in range(15)]
    results = await asyncio.gather(*queries)

    print(f"\\nAll {len(results)} queries completed successfully")

asyncio.run(example3())
print()

# Example 4: Semaphore with Error Handling
print("="*70)
print("Example 4: Semaphore with Exception Handling")
print("="*70)

async def risky_task(semaphore, task_id):
    """Task that might fail"""
    async with semaphore:
        print(f"Task {task_id} started")

        if task_id == 3:
            raise ValueError(f"Task {task_id} failed!")

        await asyncio.sleep(0.2)
        print(f"Task {task_id} completed")
        return f"Result {task_id}"

async def example4():
    semaphore = asyncio.Semaphore(2)
    tasks = [risky_task(semaphore, i) for i in range(5)]

    # Gather with return_exceptions to handle failures
    results = await asyncio.gather(*tasks, return_exceptions=True)

    print("\\nResults:")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  Task {i}: ERROR - {result}")
        else:
            print(f"  Task {i}: {result}")

asyncio.run(example4())
print()

# Example 5: BoundedSemaphore - Prevent Over-Release
print("="*70)
print("Example 5: BoundedSemaphore vs Regular Semaphore")
print("="*70)

async def example5():
    # Regular semaphore allows over-release
    regular_sem = asyncio.Semaphore(2)
    print("Regular Semaphore:")
    print(f"  Initial value: 2")
    regular_sem.release()
    regular_sem.release()
    print(f"  After 2 releases: value is now 4 (allowed)")

    # BoundedSemaphore prevents over-release
    bounded_sem = asyncio.BoundedSemaphore(2)
    print("\\nBoundedSemaphore:")
    print(f"  Initial value: 2")

    try:
        bounded_sem.release()
        print(f"  After 1 release: value is now 3 (ERROR - should not happen)")
    except ValueError as e:
        print(f"  Attempted release: ValueError - {e}")
        print(f"  BoundedSemaphore prevents over-release!")

asyncio.run(example5())
print()

# Example 6: Rate Limiting with Semaphore
print("="*70)
print("Example 6: API Rate Limiting")
print("="*70)

async def api_call(semaphore, call_id):
    """Simulate API call with rate limiting"""
    async with semaphore:
        print(f"API call {call_id}: Making request...")
        await asyncio.sleep(0.5)
        print(f"API call {call_id}: Response received")
        return {"call_id": call_id, "status": "success"}

async def example6():
    # Limit to 3 concurrent API calls
    rate_limiter = asyncio.Semaphore(3)

    print("Making 10 API calls with max 3 concurrent:\\n")

    start = time.time()
    calls = [api_call(rate_limiter, i) for i in range(10)]
    results = await asyncio.gather(*calls)
    elapsed = time.time() - start

    print(f"\\nCompleted {len(results)} API calls in {elapsed:.2f}s")
    print(f"Average: {elapsed/len(results):.2f}s per call")

asyncio.run(example6())
print()

# Example 7: Dynamic Semaphore Value
print("="*70)
print("Example 7: Checking and Modifying Semaphore")
print("="*70)

async def example7():
    semaphore = asyncio.Semaphore(5)

    print(f"Initial semaphore value: 5\\n")

    # Acquire some
    await semaphore.acquire()
    await semaphore.acquire()
    print(f"After 2 acquires: {5 - 2} available")

    # Release one
    semaphore.release()
    print(f"After 1 release: {5 - 1} available")

    # Check if available
    if semaphore.locked():
        print("\\nSemaphore is locked (no permits available)")
    else:
        print("\\nSemaphore has permits available")

    # Clean up
    semaphore.release()

asyncio.run(example7())
print()

# Example 8: Multiple Semaphores for Different Resources
print("="*70)
print("Example 8: Multiple Resource Types")
print("="*70)

async def process_data(db_sem, api_sem, task_id):
    """Task using multiple resources"""
    # Need database connection
    async with db_sem:
        print(f"Task {task_id}: Got DB connection, querying...")
        await asyncio.sleep(0.2)

        # Also need API access
        async with api_sem:
            print(f"Task {task_id}: Got API access, calling...")
            await asyncio.sleep(0.2)
            print(f"Task {task_id}: Complete")

async def example8():
    db_semaphore = asyncio.Semaphore(3)   # 3 DB connections
    api_semaphore = asyncio.Semaphore(2)  # 2 API slots

    print("Resources: 3 DB connections, 2 API slots\\n")

    tasks = [process_data(db_semaphore, api_semaphore, i) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(example8())
print()

# Example 9: Timeout with Semaphore
print("="*70)
print("Example 9: Semaphore with Timeout")
print("="*70)

async def worker_with_timeout(semaphore, worker_id):
    """Try to acquire semaphore with timeout"""
    try:
        # Try to acquire with 1 second timeout
        async with asyncio.timeout(1.0):
            async with semaphore:
                print(f"Worker {worker_id}: Acquired, working...")
                await asyncio.sleep(2)  # Work takes 2s
                print(f"Worker {worker_id}: Done")
    except asyncio.TimeoutError:
        print(f"Worker {worker_id}: Timeout waiting for semaphore")

async def example9():
    # Only 1 slot available
    semaphore = asyncio.Semaphore(1)

    # Start 3 workers - only 1 can proceed at a time
    tasks = [worker_with_timeout(semaphore, i) for i in range(3)]
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(example9())
print()

# Example 10: Practical Application - Web Scraper
print("="*70)
print("Example 10: Real-World Use Case - Concurrent Web Scraper")
print("="*70)

async def scrape_page(semaphore, url_id, delay=0.5):
    """Simulate web page scraping"""
    async with semaphore:
        print(f"Scraping page {url_id}...")
        await asyncio.sleep(delay)

        # Simulate extracted data
        data = {
            "url_id": url_id,
            "title": f"Page {url_id} Title",
            "word_count": 100 + url_id * 10
        }

        print(f"  Scraped page {url_id}: {data['word_count']} words")
        return data

async def scrape_website():
    """Scrape multiple pages with concurrency limit"""
    max_concurrent = 5  # Be nice to the server
    semaphore = asyncio.Semaphore(max_concurrent)

    urls_to_scrape = 20

    print(f"Scraping {urls_to_scrape} pages (max {max_concurrent} concurrent)\\n")

    start_time = time.time()

    tasks = [scrape_page(semaphore, i) for i in range(urls_to_scrape)]
    results = await asyncio.gather(*tasks)

    elapsed = time.time() - start_time

    # Analyze results
    print("\\n" + "="*70)
    print("SCRAPING SUMMARY")
    print("="*70)
    print(f"Pages scraped: {len(results)}")
    print(f"Total time: {elapsed:.2f}s")
    print(f"Average: {elapsed/len(results):.2f}s per page")
    print(f"Total words: {sum(r['word_count'] for r in results):,}")
    print("="*70)

asyncio.run(scrape_website())

print("\\n" + "="*70)
print("KEY TAKEAWAYS")
print("="*70)
print("1. asyncio.Semaphore(n) - Limit to n concurrent tasks")
print("2. async with semaphore: - Acquire and auto-release")
print("3. semaphore.acquire() / release() - Manual control")
print("4. BoundedSemaphore - Prevents over-release errors")
print("5. Use for: DB connections, API rate limits, resource pools")
print("6. Prevents resource exhaustion in concurrent code")
print("7. semaphore.locked() - Check if permits available")
print("8. Always release in finally or use context manager")
print("9. Multiple semaphores for different resource types")
print("10. Essential for production-grade async applications")
print("="*70)
'''

# Save the updated lessons
with open('public/lessons-python.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

# Print summary
print("\nUpgraded lesson 101:")
print(f"  101: asyncio.Semaphore - {len(lesson101['fullSolution'])} chars")
print("\nBatch 101-110: Lesson 101 complete, continuing with 102-110...")
