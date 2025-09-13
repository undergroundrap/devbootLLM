export const lessons = [
  {
    title: "asyncio.Semaphore (limit concurrency)",
    language: "python",
    description: "Run 4 async tasks with a concurrency limit of 2 using Semaphore; print the total tasks run (4).",
    initialCode: `import asyncio

# Use an asyncio.Semaphore to limit concurrency to 2 while running 4 tasks.
# Each task should return 1; after gathering, print the sum (4).

`,
    fullSolution: `import asyncio

async def worker(sema):
    async with sema:
        await asyncio.sleep(0.05)
        return 1

async def main():
    sema = asyncio.Semaphore(2)
    tasks = [asyncio.create_task(worker(sema)) for _ in range(4)]
    results = await asyncio.gather(*tasks)
    print(sum(results))

asyncio.run(main())
`,
    expectedOutput: "4",
    tutorial: `<p class=\"mb-4 text-gray-300\">Use <code>asyncio.Semaphore</code> to bound simultaneous operations (e.g., API calls, file I/O). It prevents too many tasks from running at once.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">import asyncio
sema = asyncio.Semaphore(2)
async def work():
    async with sema:
        await asyncio.sleep(0.01)
        return 1
</pre></div>`
  },
  {
    title: "ProcessPoolExecutor (sum of cubes)",
    language: "python",
    description: "Use ProcessPoolExecutor to compute the sum of cubes from 1..50 and print it.",
    initialCode: `from concurrent.futures import ProcessPoolExecutor

# Define a top-level cube(x) and safely run a ProcessPoolExecutor
# to sum x*x*x for x in 1..50, then print the total.

`,
    fullSolution: `from concurrent.futures import ProcessPoolExecutor

def cube(x):
    return x*x*x

if __name__ == '__main__':
    with ProcessPoolExecutor() as ex:
        total = sum(ex.map(cube, range(1, 51)))
        print(total)
`,
    expectedOutput: "1625625",
    tutorial: `<p class=\"mb-4 text-gray-300\">CPU-bound work scales with processes, not threads. Use <code>ProcessPoolExecutor</code> to fan out heavy computation across cores and then reduce results.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">from concurrent.futures import ProcessPoolExecutor
def f(x):
    return x*x
if __name__ == '__main__':
    with ProcessPoolExecutor() as ex:
        print(sum(ex.map(f, range(5))))  # 0+1+4+9+16 = 30</pre></div>`
  },
  {
    title: "asyncio.Queue producer/consumer",
    language: "python",
    description: "Use an asyncio.Queue with a producer that enqueues 5 items and a consumer that counts them; print 5.",
    initialCode: `import asyncio

# Create an asyncio.Queue. Producer should put 5 items then a sentinel (None).
# Consumer should count items until sentinel, then print the count (5).

`,
    fullSolution: `import asyncio

async def producer(q):
    for i in range(5):
        await q.put(i)
    await q.put(None)  # sentinel

async def consumer(q):
    count = 0
    while True:
        item = await q.get()
        if item is None:
            print(count)
            return
        count += 1

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main())
`,
    expectedOutput: "5",
    tutorial: `<p class=\"mb-4 text-gray-300\"><code>asyncio.Queue</code> coordinates producers and consumers without busy-waiting. Use a sentinel to signal completion.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">q = asyncio.Queue()
# producer: await q.put(x)
# consumer: x = await q.get()
</pre></div>`
  },
  {
    title: "contextlib.ExitStack (multiple resources)",
    language: "python",
    description: "Use ExitStack to manage two file handles, write 'A' and 'B', then read both and print AB.",
    initialCode: `from contextlib import ExitStack

# Open a.txt and b.txt with ExitStack, write 'A' and 'B' respectively.
# Reopen and read both, then print their concatenation (AB).

`,
    fullSolution: `from contextlib import ExitStack

with ExitStack() as stack:
    fa = stack.enter_context(open('a.txt', 'w'))
    fb = stack.enter_context(open('b.txt', 'w'))
    fa.write('A')
    fb.write('B')

with ExitStack() as stack:
    fa = stack.enter_context(open('a.txt'))
    fb = stack.enter_context(open('b.txt'))
    print(fa.read() + fb.read())
`,
    expectedOutput: "AB",
    tutorial: `<p class=\"mb-4 text-gray-300\"><code>ExitStack</code> lets you dynamically compose multiple context managers (files, locks, etc.) and guarantees cleanup in reverse order.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">from contextlib import ExitStack
with ExitStack() as stack:
    f1 = stack.enter_context(open('x.txt', 'w'))
    f2 = stack.enter_context(open('y.txt', 'w'))
    f1.write('X'); f2.write('Y')
</pre></div>`
  }
];

