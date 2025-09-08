#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

function removeInlineBlock(filePath, startMarker, endMarker) {
  const abs = path.resolve(filePath);
  let content = fs.readFileSync(abs, 'utf8');
  const startIdx = content.indexOf(startMarker);
  if (startIdx === -1) return { changed: false, reason: 'start marker not found' };
  const endIdx = content.indexOf(endMarker, startIdx + startMarker.length);
  if (endIdx === -1) return { changed: false, reason: 'end marker not found' };
  const before = content.slice(0, startIdx);
  const after = content.slice(endIdx + endMarker.length);
  content = before + after;
  fs.writeFileSync(abs, content, 'utf8');
  return { changed: true };
}

function buildPythonTutorial(lesson) {
  const title = String(lesson.title || '').toLowerCase();
  const desc = String(lesson.description || '').trim();
  const block = (code) => `<h4 class="font-semibold text-gray-200 mb-2">Example:</h4><div class="code-block-wrapper"><pre class="tutorial-code-block">${code}</pre></div>`;
  const p = (text) => `<p class=\"mb-4 text-gray-300\">${text}</p>`;

  const examples = {
    hello: `${p('Use the built-in print() function to write text to the console. Strings must be quoted.')}${block('print("Hello there!")\nprint(42)')}`,
    variables: `${p('A variable is a named reference to a value. Python infers types at runtime (dynamic typing).')}${block('my_number = 42\nname = "Alice"\npi = 3.14\nis_active = True\nprint(name, my_number)')}`,
    while: `${p('A while loop repeats while a condition remains True. Be sure the condition eventually becomes False to avoid infinite loops.')}${block('i = 1\nwhile i <= 3:\n    print(i)\n    i += 1')}`,
    for: `${p('for iterates directly over items or over a range of numbers. range(n) yields 0..n-1.')}${block('for i in range(3):\n    print(i)')}`,
    list: `${p('Lists are ordered, zero-indexed, and mutable. Access by index and modify with methods like append() and pop().')}${block('nums = [10, 20, 30]\nprint(nums[1])  # 20\nnums.append(40)\nprint(nums)')}`,
    functions: `${p('Define functions with def. Parameters are local names; return sends a value back to the caller.')}${block('def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("World"))')}`,
    ifelse: `${p('Use if/elif/else to branch on conditions. Use % (modulo) to check divisibility.')}${block('x = 7\nif x % 2 == 0:\n    print("Even")\nelse:\n    print("Odd")')}`,
    sum: `${p('sum() adds items of any iterable of numbers. Combine with range() for sequences of integers.')}${block('total = sum(range(1, 6))\nprint(total)  # 15')}`,
    fstring: `${p('f-strings embed expressions inside string literals using {name}. They are concise and readable.')}${block("name = 'Alice'\nprint(f'Hello, {name}!')")}`,
    dict: `${p('Dictionaries store key/value pairs. Access values by key; add new keys by assignment.')}${block('capitals = {"England": "London", "Germany": "Berlin"}\nprint(capitals["Germany"])\ncapitals["Japan"] = "Tokyo"')}`,
    boolean: `${p('Combine logical conditions with and / or / not. Parentheses improve readability.')}${block('is_admin = True\nis_active = True\nif is_admin and is_active:\n    print("Access Granted")\nelse:\n    print("Access Denied")')}`,
    foreach: `${p('Loop over a list and use the loop variable directly; no index needed unless you want it via enumerate().')}${block("names = ['Ana','Bo','Cy']\nfor n in names:\n    print(n)")}`,
    list_methods: `${p('append() adds to the end; pop() removes and returns the last item (or by index).')}${block('nums = [1, 2, 3]\nnums.append(4)\nnums.pop()\nprint(nums)  # [1, 2, 3]')}`,
    string_methods: `${p('Common string methods: lower(), upper(), strip(), replace(), split(). They return new strings (immutable).')}${block("s = 'Python'\nprint(s.lower())\nprint(s.upper())")}`,
    continue: `${p('continue skips the rest of the current loop iteration and moves on to the next.')}${block('for i in range(10):\n    if i % 2 == 0:\n        continue\n    print(i)  # prints odds')}`,
    break: `${p('break exits the nearest loop immediately.')}${block('for i in range(10):\n    if i == 3:\n        break\n    print(i)  # 0,1,2')}`,
    max: `${p('Built-ins like max(), min(), and sum() work with lists and other iterables of numbers.')}${block('numbers = [1, 44, 7, 99, 23]\nprint(max(numbers))')}`,
    params: `${p('Functions can accept parameters and return computed results.')}${block('def add(a, b):\n    return a + b\n\nprint(add(3, 4))  # 7')}`,
    classes: `${p('Define classes with methods. The first parameter of instance methods is conventionally named self and refers to the instance.')}${block("class Dog:\n    def bark(self):\n        print('Woof!')\n\nDog().bark()")}`,
    inheritance: `${p('A subclass inherits from a parent class and can override methods. Use super() to call the parent implementation when needed.')}${block('class Animal:\n    def speak(self):\n        return "..."\n\nclass Dog(Animal):\n    def speak(self):\n        return "Woof!"\n\nprint(Dog().speak())')}`,
    enums: `${p('The enum module lets you define named constants. Access by EnumName.MEMBER.')}${block('from enum import Enum\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nprint(Color.RED.name)  # "RED"')}`,
    slicing: `${p('Slicing returns a sub-sequence: seq[start:end:step]. Negative indexes count from the end.')}${block('nums = [1,2,3,4,5]\nprint(nums[-3:])  # last three')}`,
    iter_keys: `${p('Iterate dict keys, values, or items with .keys(), .values(), .items(). The default iterates keys.')}${block('person = {"name":"Ada","city":"London"}\nfor k in person:\n    print(k)')}`,
    average: `${p('Compute an average by dividing the sum by the count. Convert to float if needed for decimal results.')}${block('nums = [2,4,6,8]\nprint(sum(nums)/len(nums))  # 5.0')}`,
    fizzbuzz: `${p('Use modulo to test divisibility by 3 and 5. Check 15 first to handle both.')}${block('for i in range(1, 16):\n    if i % 15 == 0: print("FizzBuzz")\n    elif i % 3 == 0: print("Fizz")\n    elif i % 5 == 0: print("Buzz")\n    else: print(i)')}`,
    list_comp: `${p('List comprehensions create lists concisely from iterables, optionally with a condition.')}${block('[i*i for i in range(5)]  # [0,1,4,9,16]')}`,
    lambda_map_filter: `${p('Use lambda for small anonymous functions. map() transforms; filter() keeps items where predicate is True.')}${block('nums = [1,2,3]\ndoubled = list(map(lambda x: x*2, nums))\nevens = list(filter(lambda x: x%2==0, nums))\nprint(doubled)\nprint(evens)')}`,
    math: `${p('The math module provides functions like sqrt, floor, ceil, and constants like pi.')}${block('import math\nprint("Sqrt:", math.sqrt(64))\nprint("Pi:", math.pi)')}`,
    join: `${p('" ".join(list_of_strings) concatenates with a separator. Remember join is a string method, not on lists.')}${block("words = ['Python','is','efficient!']\nprint(' '.join(words))")}`,
    super_ctor: `${p('Inside a subclass constructor, call super().__init__(...) to run parent initialization.')}${block("class A:\n    def __init__(self):\n        print('A init')\nclass B(A):\n    def __init__(self):\n        super().__init__()\n        print('B init')\nB()")}`,
    property: `${p('@property turns a method into a computed attribute accessed without parentheses.')}${block("class Person:\n    def __init__(self, first, last):\n        self.first, self.last = first, last\n    @property\n    def full_name(self):\n        return f'{self.first} {self.last}'\nprint(Person('Ada','Lovelace').full_name)")}`,
    staticmethod: `${p('@staticmethod belongs to the class namespace and does not receive self or cls.')}${block('class Math:\n    @staticmethod\n    def cube(x): return x**3\nprint(Math.cube(3))')}`,
    classmethod: `${p('@classmethod receives the class (cls) as the first argument and is useful for alternative constructors.')}${block('class C:\n    total = 0\n    @classmethod\n    def create(cls):\n        cls.total += 1\n        return cls()\nC.create(); C.create(); print(C.total)')}`,
    tuple_unpack: `${p('Unpack iterables on the left-hand side to bind multiple names at once.')}${block('a,b,c = (1,2,3)\nprint(a)\nprint(c)')}`,
    set_ops: `${p('Sets store unique elements and support union (|), intersection (&), and difference (-).')}${block('A={1,2,3}; B={3,4}\nprint(A|B)\nprint(A&B)')}`,
    try_except: `${p('Wrap risky code in try/except. Catch specific exceptions first to handle them appropriately.')}${block("try:\n    1/0\nexcept ZeroDivisionError:\n    print('Oops! Division by zero')")}`,
    else_finally: `${p('In try/except, the else block runs if no exception occurred; finally always runs, success or failure.')}${block('try:\n    r = 2+2\nexcept Exception:\n    print("Error")\nelse:\n    print(r)\nfinally:\n    print("Done")')}`,
    raise: `${p('Raise exceptions with raise ValueError("message"). Use them to signal invalid inputs.')}${block('def sqrt_nonneg(x):\n    if x < 0:\n        raise ValueError("negative")\n    return x**0.5\ntry:\n    sqrt_nonneg(-1)\nexcept ValueError:\n    print("Invalid")')}`,
    fileio: `${p('Use with open(...) as f to read/write files safely. Files are closed automatically.')}${block("with open('demo.txt','w') as f:\n    f.write('hello')\nwith open('demo.txt') as f:\n    print(f.read())")}`,
    context: `${p('with manages resources that need setup/teardown (file handles, locks, network connections).')}${block("from contextlib import contextmanager\n@contextmanager\ndef tag(name):\n    print(f'<{name}>'); yield; print(f'</{name}>')\nwith tag('b'):\n    print('bold')")}`,
    sorting: `${p('Use sorted(iterable) for a new sorted list, or list.sort() to sort in place. key= controls the sort field.')}${block('print(sorted([3,1,2]))  # [1,2,3]')}`,
    dict_comp: `${p('Dict comprehensions create dictionaries concisely: {k:v for k,v in ...}.')}${block('{n: n*n for n in range(1,4)}')}`,
    generators: `${p('yield produces a sequence lazily. Iterate over the generator like any iterable.')}${block('def gen():\n    yield 1; yield 2; yield 3\nfor x in gen():\n    print(x)')}`,
    json: `${p('json.loads parses a JSON string into Python objects; json.dumps serializes Python objects to JSON strings.')}${block('import json\ns = "{\\"name\\": \\"Ada\\"}"\nobj = json.loads(s)\nprint(obj["name"])')}`,
    regex: `${p('Use the re module for regular expressions. \\d matches digits; groups capture substrings for later use.')}${block("import re\nprint(re.findall(r'\\\\d', 'a1b2c3'))\n# Groups:\nm = re.search(r'^Hello\\\\s+(\\\\w+)$', 'Hello World')\nprint(m.group(1))  # World")}`,
    enumerate: `${p('enumerate(iterable) gives index and value pairs for iteration.')}${block("for i,v in enumerate(['a','b','c']):\n    print(f'{i}:{v}')")}`,
    set_comp: `${p('Set comprehensions build sets; braces {} with an expression and optional condition.')}${block('{n for n in range(7) if n % 2 == 0}')}`,
    isinstance: `${p('isinstance(obj, type) checks an object\'s type (including subclass relationships).')}${block('x = 5\nprint(isinstance(x, int))\nprint(isinstance(x, str))\nprint(isinstance(x, object))')}`,
    review: `${p('Combine multiple concepts: classes, loops, and aggregations. Think in steps: represent data, iterate, and compute.')}${block("class Student:\n    def __init__(self, name, score):\n        self.name, self.score = name, score\nstudents=[Student('A',90), Student('B',80)]\nprint(sum(s.score for s in students)/len(students))")}`,
    // --- LESSONS 51-100 ---
    lambda_map: `${p('`map()` applies a function to every item of an iterable. Combine it with a `lambda` for concise transformations.')}${block('nums = [1, 2, 3]\ndoubled = list(map(lambda x: x * 2, nums))\nprint(doubled) # [2, 4, 6]')}`,
    filter_evens: `${p('`filter()` creates an iterator from elements of an iterable for which a function returns true. It is often used with a `lambda` for the condition.')}${block('nums = [1, 2, 3, 4]\nevens = list(filter(lambda x: x % 2 == 0, nums))\nprint(evens) # [2, 4]')}`,
    zip: `${p('`zip()` aggregates elements from two or more iterables, creating an iterator that generates tuples of corresponding elements.')}${block('nums = [1, 2]\nlets = ["a", "b"]\nprint(list(zip(nums, lets))) # [(1, "a"), (2, "b")]')}`,
    sort_by_len: `${p('The `sorted()` function can take a `key` argument. Provide `len` to sort an iterable of strings by their length.')}${block('words = ["pear", "fig", "apple"]\nprint(sorted(words, key=len)) # [\'fig\', \'pear\', \'apple\']')}`,
    sort_dicts: `${p('To sort a list of dictionaries, use a `lambda` function as the key to specify which dictionary value to sort by.')}${block("people = [{'name': 'Bob', 'age': 30}, {'name': 'Alice', 'age': 25}]\nprint(sorted(people, key=lambda p: p['age']))")}`,
    extended_unpack: `${p('Use an asterisk `*` to capture multiple items into a list during unpacking. This is often used to get the first/last items.')}${block('nums = [1, 2, 3, 4]\nfirst, *middle, last = nums\nprint(first, last) # 1 4\nprint(middle) # [2, 3]')}`,
    closures: `${p('A closure is a function that remembers variables from the enclosing scope even after that scope has finished executing.')}${block('def make_adder(n):\n    def adder(x):\n        return x + n\n    return adder\n\nadd_five = make_adder(5)\nprint(add_five(10)) # 15')}`,
    decorators: `${p('A decorator is a function that takes another function as an argument, adds some functionality, and returns another function.')}${block('def my_decorator(func):\n    def wrapper():\n        print("Something is happening before the function is called.")\n        func()\n        print("Something is happening after the function is called.")\n    return wrapper\n\n@my_decorator\ndef say_whee():\n    print("Whee!")\n\nsay_whee()')}`,
    dataclasses: `${p('Dataclasses (available in Python 3.7+) provide a decorator for automatically adding generated special methods like `__init__()` and `__repr__()`.')}${block('from dataclasses import dataclass\n\n@dataclass\nclass Point:\n    x: int\n    y: int\n\np = Point(10, 20)\nprint(p) # Point(x=10, y=20)')}`,
    type_hints: `${p('Type hints are a way to statically indicate the type of a value in your Python code. They are not enforced at runtime but can be checked by tools like mypy.')}${block('def greet(name: str) -> str:\n    return "Hello, " + name\n\nprint(greet("World"))')}`,
    itertools_chain: `${p('`itertools.chain()` takes several iterables as arguments and returns a single iterator that produces the contents of all of them as if they came from a single sequence.')}${block('import itertools\n\nfor i in itertools.chain([1, 2], ["a", "b"]):\n    print(i)')}`,
    groupby: `${p('`itertools.groupby()` makes an iterator that returns consecutive keys and groups from the iterable. The input needs to be sorted on the same key function.')}${block('from itertools import groupby\n\nfor key, group in groupby("AAABBC"): # Works on strings too\n    print(f\'{key}: {list(group)}\')')}`,
    counter: `${p('`collections.Counter` is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values.')}${block('from collections import Counter\n\nc = Counter("gallahad")\nprint(c) # Counter({\'a\': 3, \'l\': 2, \'g\': 1, \'h\': 1, \'d\': 1})')}`,
    defaultdict: `${p('`collections.defaultdict` is a subclass of `dict` that calls a factory function to supply missing values.')}${block('from collections import defaultdict\n\nd = defaultdict(int) # 0 is the default for int()\nprint(d["missing_key"]) # prints 0')}`,
    deque: `${p('`collections.deque` is a list-like container with fast appends and pops on either end.')}${block('from collections import deque\n\nd = deque(["task2", "task3"])\nd.appendleft("task1")\nd.append("task4")\nprint(d.popleft()) # task1')}`,
    namedtuple: `${p('`collections.namedtuple` returns a new tuple subclass named `typename`. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable.')}${block('from collections import namedtuple\n\nPoint = namedtuple("Point", ["x", "y"])\np = Point(11, y=22)\nprint(p.x + p.y) # 33')}`,
    contextmanager_decorator: `${p('The `@contextmanager` decorator lets you build a context manager from a simple generator function, automatically handling the `__enter__` and `__exit__` parts.')}${block('from contextlib import contextmanager\n\n@contextmanager\ndef managed_resource(*args, **kwds):\n    print("Acquiring resource")\n    yield\n    print("Releasing resource")\n\nwith managed_resource():\n    print("Doing work")')}`,
    suppress: `${p('`contextlib.suppress` is a context manager to selectively ignore specified exceptions.')}${block('from contextlib import suppress\n\nwith suppress(FileNotFoundError):\n    with open("non_existent_file.txt") as f:\n        print("This will not print")\n\nprint("Program continues without crashing")')}`,
    pathlib: `${p('The `pathlib` module offers classes representing filesystem paths with semantics appropriate for different operating systems.')}${block('from pathlib import Path\n\np = Path("my_file.txt")\np.write_text("Hello from pathlib!")\nprint(p.read_text())')}`,
    json_dumps: `${p('`json.dumps()` serializes a Python object to a JSON formatted `str`.')}${block('import json\n\ndata = {"name": "John", "age": 30}\njson_string = json.dumps(data, indent=2)\nprint(json_string)')}`,
    csv: `${p('The `csv` module implements classes to read and write tabular data in CSV format.')}${block('import csv, io\n\noutput = io.StringIO()\nwriter = csv.writer(output)\nwriter.writerow(["name", "age"])\nwriter.writerow(["Alice", 25])\nprint(output.getvalue())')}`,
    regex_sub: `${p('`re.sub()` returns the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement `repl`.')}${block('import re\n\nprint(re.sub(r"\\d+", "#", "There are 12 apples and 34 oranges."))')}`,
    datetime: `${p('The `datetime` module supplies classes for manipulating dates and times.')}${block('from datetime import datetime\n\nnow = datetime.now()\nprint(now.strftime("%Y-%m-%d %H:%M:%S"))')}`,
    logging: `${p('The `logging` module defines functions and classes which implement a flexible event logging system for applications and libraries.')}${block('import logging\n\nlogging.basicConfig(level=logging.INFO)\nlogging.info("This is an info message.")')}`,
    args: `${p('The special syntax `*args` in function definitions is used to pass a variable number of non-keyword arguments to a function.')}${block('def my_sum(*numbers):\n    return sum(numbers)\n\nprint(my_sum(1, 2, 3, 4)) # 10')}`,
    partial: `${p('`functools.partial` allows you to "freeze" some portion of a function\'s arguments and/or keywords, resulting in a new object with a simplified signature.')}${block('from functools import partial\n\nbasetwo = partial(int, base=2)\nprint(basetwo("10010")) # 18')}`,
    lru_cache: `${p('`functools.lru_cache` is a decorator to wrap a function with a memoizing callable that saves up to the `maxsize` most recent calls.')}${block('from functools import lru_cache\n\n@lru_cache(maxsize=None)\ndef fib(n):\n    if n < 2: return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(10)) # 55')}`,
    lt: `${p('Implementing the `__lt__` (less than) rich comparison method allows instances of your class to be sorted naturally.')}${block('class Person:\n    def __init__(self, name, age):\n        self.name, self.age = name, age\n    def __lt__(self, other):\n        return self.age < other.age\n\np1 = Person("Alice", 25)\np2 = Person("Bob", 30)\nprint(p1 < p2) # True')}`,
    str: `${p('The `__str__` method should return a "user-friendly" string representation of the object, which is what `print()` and `str()` will display.')}${block('class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return f"Person: {self.name}"\n\nprint(Person("Alice"))')}`,
    ordered_dataclass: `${p('Setting `order=True` in the `@dataclass` decorator automatically generates rich comparison methods (`__lt__`, `__le__`, etc.), making instances sortable.')}${block('from dataclasses import dataclass\n\n@dataclass(order=True)\nclass Item:\n    price: int\n    name: str\n\nprint(Item(10, "B") > Item(5, "A")) # True')}`,
    product: `${p('`itertools.product()` provides the cartesian product of input iterables.')}${block('import itertools\n\nfor p in itertools.product("AB", "12"):\n    print("".join(p)) # A1, A2, B1, B2')}`,
    permutations: `${p('`itertools.permutations()` returns successive r-length permutations of elements in an iterable.')}${block('import itertools\n\nprint(list(itertools.permutations("ABC", 2)))')}`,
    accumulate: `${p('`itertools.accumulate()` makes an iterator that returns accumulated sums, or accumulated results of other binary functions.')}${block('import itertools\n\nprint(list(itertools.accumulate([1, 2, 3, 4]))) # [1, 3, 6, 10]')}`,
    chaining: `${p('Exception chaining allows you to preserve the original exception when you raise a new one. Use `raise NewException from original_exception`.')}${block('try:\n    1/0\nexcept ZeroDivisionError as e:\n    raise ValueError("Input error") from e')}`,
    threading: `${p('The `threading` module provides a way to create and manage threads. A `Lock` is a synchronization primitive that is not owned by a particular thread when locked.')}${block('import threading\n\nlock = threading.Lock()\n\ndef critical_section():\n    with lock:\n        print("Critical section accessed")\n\ncritical_section()')}`,
    threadpool: `${p('`concurrent.futures.ThreadPoolExecutor` provides a high-level interface for asynchronously executing callables in a pool of threads.')}${block('from concurrent.futures import ThreadPoolExecutor\n\nwith ThreadPoolExecutor(max_workers=1) as executor:\n    future = executor.submit(pow, 2, 5)\n    print(future.result()) # 32')}`,
    asyncio: `${p('`asyncio` is a library to write concurrent code using the `async/await` syntax. `asyncio.gather` runs awaitable objects concurrently.')}${block('import asyncio\n\nasync def main():\n    print(await asyncio.gather(asyncio.sleep(1, result="Done")))\n\nasyncio.run(main())')}`,
    glob: `${p('The `glob` module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.')}${block('import glob\n\n# This example won\'t run here, but shows the concept.\n# open("a.txt", "w"); open("b.log", "w")\n# print(glob.glob("*.txt")) # [\'a.txt\']')}`,
    decimal: `${p('The `decimal` module provides a `Decimal` datatype for decimal floating-point arithmetic, which is useful for financial applications.')}${block('from decimal import Decimal\n\nprint(Decimal("0.1") + Decimal("0.2")) # 0.3')}`,
    fractions: `${p('The `fractions` module provides support for rational number arithmetic.')}${block('from fractions import Fraction\n\nprint(Fraction(1, 3) + Fraction(1, 3)) # 2/3')}`,
    bisect: `${p('The `bisect` module provides support for maintaining a list in sorted order without having to sort the list after each insertion.')}${block('import bisect\n\nitems = [1, 2, 4]\nbisect.insort(items, 3)\nprint(items) # [1, 2, 3, 4]')}`,
    heapq: `${p('The `heapq` module provides an implementation of the min-heap queue algorithm.')}${block('import heapq\n\nh = [3, 1, 4, 1, 5, 9, 2]\nheapq.heapify(h)\nprint(heapq.heappop(h)) # 1')}`,
    statistics: `${p('The `statistics` module provides functions for calculating mathematical statistics of numeric data.')}${block('import statistics\n\nprint(statistics.mean([1, 2, 3, 4, 4])) # 2.8')}`,
    slice_assign: `${p('You can assign to a slice of a list to replace, remove, or insert elements.')}${block('a = [1, 2, 3, 4]\na[1:3] = [8, 9, 10]\nprint(a) # [1, 8, 9, 10, 4]')}`,
    ordereddict: `${p('`collections.OrderedDict` is a dict subclass that remembers the order that keys were first inserted. (Note: standard dicts in Python 3.7+ also preserve insertion order.)')}${block('from collections import OrderedDict\n\nd = OrderedDict.fromkeys("abcde")\nd.move_to_end("b")\nprint("".join(d.keys())) # acdeb')}`,
    frozenset: `${p('`frozenset` is an immutable version of `set`. Since it is hashable, it can be used as a dictionary key or as an element of another set.')}${block('fs = frozenset([1, 2, 3])\n# fs.add(4) would raise an AttributeError')}`,
    sort_last_char: `${p('You can provide a `lambda` to the `key` argument of `sorted` to implement custom sorting logic, such as sorting by the last character of a string.')}${block('words = ["apple", "fig", "banana"]\nprint(sorted(words, key=lambda w: w[-1]))')}`,
    iterator: `${p('To create a custom iterator, a class needs to implement the `__iter__()` and `__next__()` methods.')}${block('class UpToThree:\n    def __init__(self):\n        self.count = 1\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.count > 3: raise StopIteration\n        val = self.count\n        self.count += 1\n        return val\n\nprint(list(UpToThree())) # [1, 2, 3]')}`,
    capstone: `${p('This capstone combines several concepts: JSON parsing, finding the maximum item in a list of dictionaries using a lambda function as the key.')}${block('import json\ns = \'[{"name":"Alice","score":90},{"name":"Charlie","score":100}]\'\nstudents = json.loads(s)\nrichest = max(students, key=lambda s: s["score"])\nprint(richest["name"]) # Charlie')}`,
  };

  const choose = (keys) => keys.find(k => title.includes(k));
  let key = choose(['hello']) && 'hello'
         || choose(['variable','data']) && 'variables'
         || choose(['while']) && 'while'
         || choose(['for-','for loops','for ']) && 'for'
         || choose(['list basics','lists basics','list ']) && (title.includes('comprehension') ? 'list_comp' : (title.includes('methods') ? 'list_methods' : 'list'))
         || choose(['function']) && (title.includes('parameter') ? 'params' : 'functions')
         || choose(['if / else','if/ else','if ']) && 'ifelse'
         || choose(['sum','range()']) && 'sum'
         || choose(['f-strings','strings & f']) && 'fstring'
         || choose(['dictionar']) && (title.includes('comprehension') ? 'dict_comp' : 'dict')
         || choose(['boolean']) && 'boolean'
         || choose(['for-each']) && 'foreach'
         || choose(['string methods']) && 'string_methods'
         || choose(['continue']) && 'continue'
         || choose(['break']) && 'break'
         || choose(['max ']) && 'max'
         || choose(['classes','methods']) && 'classes'
         || choose(['inherit']) && 'inheritance'
         || choose(['enum']) && 'enums'
         || choose(['slicing']) && 'slicing'
         || choose(['iterate dict']) && 'iter_keys'
         || choose(['average']) && 'average'
         || choose(['fizzbuzz']) && 'fizzbuzz'
         || choose(['lambda','map','filter']) && (title.includes('lambda + map') ? 'lambda_map' : (title.includes('filter') ? 'filter_evens' : 'lambda_map_filter'))
         || choose(['math']) && 'math'
         || choose([' join']) && 'join'
         || choose(['super()']) && 'super_ctor'
         || choose(['@property','properties']) && 'property'
         || choose(['@staticmethod','staticmethod']) && 'staticmethod'
         || choose(['@classmethod','classmethod']) && 'classmethod'
         || choose(['tuple']) && 'tuple_unpack'
         || choose(['set operations']) && 'set_ops'
         || choose(['try/except','try','except']) && 'try_except'
         || choose(['else and finally','finally']) && 'else_finally'
         || choose(['raise']) && 'raise'
         || choose(['file i/o','file ','i/o']) && 'fileio'
         || choose(['context']) && (title.includes('contextmanager') ? 'contextmanager_decorator' : 'context')
         || choose(['sorting']) && 'sorting'
         || choose(['generator']) && 'generators'
         || choose(['json ']) && (title.includes('dumps') ? 'json_dumps' : 'json')
         || choose(['regular expressions','regex']) && (title.includes('subst') ? 'regex_sub' : 'regex')
         || choose(['enumerate']) && 'enumerate'
         || choose(['set comprehension']) && 'set_comp'
         || choose(['isinstance']) && 'isinstance'
         || choose(['review']) && 'review'
         || choose(['zip()']) && 'zip'
         || choose(['sort by length']) && 'sort_by_len'
         || choose(['sort dicts']) && 'sort_dicts'
         || choose(['extended unpacking']) && 'extended_unpack'
         || choose(['closures']) && 'closures'
         || choose(['decorators']) && 'decorators'
         || choose(['dataclasses']) && 'dataclasses'
         || choose(['type hints']) && 'type_hints'
         || choose(['itertools.chain']) && 'itertools_chain'
         || choose(['groupby']) && 'groupby'
         || choose(['counter']) && 'counter'
         || choose(['defaultdict']) && 'defaultdict'
         || choose(['deque']) && 'deque'
         || choose(['namedtuple']) && 'namedtuple'
         || choose(['suppress']) && 'suppress'
         || choose(['pathlib']) && 'pathlib'
         || choose(['csv']) && 'csv'
         || choose(['datetime']) && 'datetime'
         || choose(['logging']) && 'logging'
         || choose(['*args']) && 'args'
         || choose(['functools.partial']) && 'partial'
         || choose(['lru_cache']) && 'lru_cache'
         || choose(['__lt__']) && 'lt'
         || choose(['__str__']) && 'str'
         || choose(['ordered dataclass']) && 'ordered_dataclass'
         || choose(['itertools.product']) && 'product'
         || choose(['permutations']) && 'permutations'
         || choose(['accumulate']) && 'accumulate'
         || choose(['exception chaining']) && 'chaining'
         || choose(['threading']) && 'threading'
         || choose(['threadpoolexecutor']) && 'threadpool'
         || choose(['asyncio']) && 'asyncio'
         || choose(['glob']) && 'glob'
         || choose(['decimal']) && 'decimal'
         || choose(['fractions']) && 'fractions'
         || choose(['bisect']) && 'bisect'
         || choose(['heapq']) && 'heapq'
         || choose(['statistics']) && 'statistics'
         || choose(['slice assignment']) && 'slice_assign'
         || choose(['ordereddict']) && 'ordereddict'
         || choose(['frozenset']) && 'frozenset'
         || choose(['sort by last char']) && 'sort_last_char'
         || choose(['custom iterator']) && 'iterator'
         || choose(['capstone']) && 'capstone';


  if (!key || !examples[key]) {
    const intro = p(desc || 'Practice the concept with a short example below.');
    return `${intro}${block('x = 10\ny = 20\nprint(x + y)')}`;
  }
  return examples[key];
}

function ensureParagraph(htmlOrText) {
  const s = String(htmlOrText || '').trim();
  if (!s) return '';
  if (s.startsWith('<')) return s;
  return `<p class="mb-4 text-gray-300">${s.replaceAll('<', '&lt;').replaceAll('>', '&gt;')}</p>`;
}

function buildJavaTutorial(lesson) {
  const title = String(lesson.title || '').toLowerCase();
  const p = (text) => `<p class=\"mb-4 text-gray-300\">${text}</p>`;
  const block = (code) => `<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4><div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">${code}</pre></div>`;

  const examples = {
    hello: `${p('Use System.out.println(...) to print to the console. Quotes are required for strings; numbers can be printed directly.')}${block('// Prints a greeting and a number.\nSystem.out.println("Hello there!");\nSystem.out.println(42);')}`,
    variables: `${p('Declare variables with a type and a name. Common types include int, double, boolean, and String.')}${block('int myNumber = 42;\nString name = "Alice";\ndouble pi = 3.14;\nboolean isActive = true;\nSystem.out.println(name + " " + myNumber);')}`,
    while: `${p('A while loop repeats while a condition is true. Ensure the loop variable changes to avoid infinite loops.')}${block('int i = 1;\nwhile (i <= 3) {\n    System.out.println(i);\n    i++;\n}')}`,
    for: `${p('A classic for loop uses an index; it runs while the condition remains true, incrementing each time.')}${block('for (int i = 0; i < 3; i++) {\n    System.out.println(i);\n}')}`,
    foreach: `${p('The enhanced for-each loop iterates elements directly, avoiding index management.')}${block('String[] fruits = {"Apple", "Orange", "Banana"};\nfor (String f : fruits) {\n    System.out.println(f);\n}')}`,
    array: `${p('Arrays store a fixed number of elements of the same type. Indexing starts at 0.')}${block('int[] nums = {10, 20, 30};\nSystem.out.println(nums[1]); // 20')}`,
    ifelse: `${p('Use if/else to branch on conditions. The % operator (modulo) helps with divisibility checks.')}${block('int x = 7;\nif (x % 2 == 0) {\n    System.out.println("Even");\n} else {\n    System.out.println("Odd");\n}')}`,
    switch: `${p('switch is useful when testing a value against many constant cases. Remember break to avoid fall-through.')}${block("char grade = 'B';\nString comment;\nswitch (grade) {\n  case 'A': comment = \"Excellent!\"; break;\n  case 'B': comment = \"Good job!\"; break;\n  case 'C': comment = \"You passed.\"; break;\n  default: comment = \"Invalid grade.\";\n}\nSystem.out.println(comment);")}`,
    scanner: `${p('Read input from the console with java.util.Scanner. Close scanners in real programs to free resources.')}${block('import java.util.Scanner;\nScanner scanner = new Scanner(System.in);\nString name = scanner.nextLine();\nSystem.out.println("Hello, " + name);')}`,
    string: `${p('String methods like toLowerCase(), toUpperCase(), and length() return transformed information; Strings are immutable.')}${block('String s = "Java";\nSystem.out.println(s.toLowerCase());\nSystem.out.println(s.toUpperCase());\nSystem.out.println(s.length());')}`,
    methods: `${p('Define reusable logic in methods. Static methods belong to the class and can be called without an instance.')}${block('static int add(int a, int b) { return a + b; }\nSystem.out.println(add(3, 4)); // 7')}`,
    classes: `${p('Classes bundle data and behavior. Create an instance with new and call its methods.')}${block('class Dog {\n  void bark() { System.out.println("Woof!"); }\n}\nnew Dog().bark();')}`,
    exceptions: `${p('Wrap risky code in try/catch. Catch specific exceptions first and handle them appropriately.')}${block('try {\n  Integer.parseInt("abc");\n} catch (NumberFormatException e) {\n  System.out.println("Invalid number");\n}')}`,
    fizzbuzz: `${p('Check 15 first to handle multiples of both 3 and 5. Use else-if to keep tests mutually exclusive.')}${block('for (int i = 1; i <= 15; i++) {\n  if (i % 15 == 0) System.out.println("FizzBuzz");\n  else if (i % 3 == 0) System.out.println("Fizz");\n  else if (i % 5 == 0) System.out.println("Buzz");\n  else System.out.println(i);\n}')}`,
    arraylist: `${p('ArrayList is a resizable list. Use add() to append and get() to access by index.')}${block('java.util.List<Integer> list = new java.util.ArrayList<>();\nlist.add(1); list.add(2); list.add(3);\nSystem.out.println(list);')}`,
    boolean: `${p('Combine boolean expressions with &&, ||, and !. Parentheses help readability.')}${block('boolean isAdmin = true, isActive = true;\nif (isAdmin && isActive) System.out.println("Access Granted");\nelse System.out.println("Access Denied");')}`,
    hashmap: `${p('A HashMap stores key-value pairs. Use `put` to add items and `get` to retrieve them by key.')}${block('import java.util.HashMap;\nHashMap<String, String> capitals = new HashMap<>();\ncapitals.put("England", "London");\nSystem.out.println(capitals.get("England")); // London')}`,
    // --- LESSONS 51-100 ---
    streams_map: `${p('The `map` operation transforms each element of a stream. It applies a function to each element and returns a new stream of the results.')}${block('import java.util.List;\nList<String> names = List.of("alice", "bob");\nnames.stream()\n     .map(String::toUpperCase)\n     .forEach(System.out::println); // ALICE, BOB printed on new lines')}`,
    streams_filter: `${p('The `filter` operation selects elements from a stream that match a given condition (a `Predicate`).')}${block('import java.util.List;\nList<Integer> nums = List.of(1, 2, 3, 4);\nnums.stream()\n    .filter(n -> n % 2 == 0)\n    .forEach(System.out::println); // 2, 4 printed on new lines')}`,
    sort_by_length: `${p('You can sort collections using a `Comparator`. `Comparator.comparingInt` is a helper for sorting by an integer property, like string length.')}${block('import java.util.List;\nimport java.util.Comparator;\nList<String> words = List.of("fig", "apple", "pear");\nwords.stream()\n     .sorted(Comparator.comparingInt(String::length))\n     .forEach(System.out::println); // fig, pear, apple on new lines')}`,
    comparator: `${p('`Comparator.comparing` extracts a sort key from an object. You provide a lambda that takes an object and returns the property to sort by.')}${block('import java.util.*;\nclass Person { String name; Person(String n) { name=n; } }\nList<Person> people = List.of(new Person("Bob"), new Person("Alice"));\npeople.stream().sorted(Comparator.comparing(p -> p.name))\n      .forEach(p -> System.out.println(p.name)); // Alice, Bob')}`,
    optional_map: `${p('`Optional.map` applies a function to the value inside an Optional, if it is present, and returns a new Optional with the result.')}${block('import java.util.Optional;\nOptional<String> opt = Optional.of("text");\nopt.map(String::toUpperCase).ifPresent(System.out::println); // TEXT')}`,
    generics: `${p('Generics allow you to define classes and methods that are parameterized over types. A `Box<T>` can hold any type `T`.')}${block('class Box<T> { private T t; public void set(T t) { this.t=t; } public T get() { return t; } }\nBox<Integer> intBox = new Box<>();\nintBox.set(10);\nSystem.out.println(intBox.get()); // 10')}`,
    wildcards: `${p('Upper-bounded wildcards (`? extends Type`) are used to increase flexibility. A `List<? extends Number>` can hold a list of Integers or a list of Doubles.')}${block('import java.util.List;\npublic static double sum(List<? extends Number> list) {\n    return list.stream().mapToDouble(Number::doubleValue).sum();\n}\nSystem.out.println(sum(List.of(1, 2.5))); // 3.5')}`,
    method_refs: `${p('Method references are a shorthand syntax for a lambda expression that executes just ONE method. They make code more readable.')}${block('import java.util.List;\nList<String> list = List.of("a", "b");\nlist.stream().map(String::toUpperCase).forEach(System.out::println); // A, B')}`,
    reverse_sort: `${p('`Comparator.reverseOrder()` returns a comparator that imposes the reverse of the natural ordering.')}${block('import java.util.*;\nList<Integer> nums = List.of(1, 3, 2);\nnums.stream().sorted(Comparator.reverseOrder()).forEach(System.out::println); // 3, 2, 1')}`,
    enum_switch: `${p('Enums work very well with `switch` statements, providing compile-time checking that all cases are handled.')}${block('enum Level { EASY, HARD }\nLevel level = Level.EASY;\nswitch (level) {\n    case EASY -> System.out.println("Easy mode");\n    case HARD -> System.out.println("Hard mode");\n}')}`,
    record: `${p('Records (Java 16+) provide a compact syntax for declaring classes which are transparent holders for immutable data.')}${block('record Point(int x, int y) {}\nPoint p = new Point(1, 2);\nSystem.out.println(p.x()); // 1')}`,
    streams_reduce: `${p('The `reduce` operation combines all elements of a stream into a single result.')}${block('import java.util.List;\nint sum = List.of(1, 2, 3).stream().reduce(0, (a, b) -> a + b);\nSystem.out.println(sum); // 6')}`,
    collectors_joining: `${p('`Collectors.joining` is a collector that concatenates the input elements into a String, in encounter order.')}${block('import java.util.stream.*;\nString s = Stream.of("a", "b", "c").collect(Collectors.joining(","));\nSystem.out.println(s); // "a,b,c"')}`,
    linkedhashmap: `${p('A `LinkedHashMap` maintains a doubly-linked list running through all of its entries. This linking defines the iteration ordering, which is normally the order in which keys were inserted.')}${block('import java.util.LinkedHashMap;\nLinkedHashMap<String, Integer> map = new LinkedHashMap<>();\nmap.put("b", 2); map.put("a", 1);\nSystem.out.println(map.keySet()); // [b, a]')}`,
    linkedhashset: `${p('A `LinkedHashSet` is an ordered version of HashSet that maintains a doubly-linked List across all elements. The elements are ordered based on their insertion order.')}${block('import java.util.LinkedHashSet;\nLinkedHashSet<Integer> set = new LinkedHashSet<>();\nset.add(3); set.add(1); set.add(3);\nSystem.out.println(set); // [3, 1]')}`,
    treeset: `${p('A `TreeSet` is a NavigableSet implementation based on a TreeMap. The elements are ordered using their natural ordering, or by a Comparator provided at set creation time.')}${block('import java.util.TreeSet;\nTreeSet<Integer> set = new TreeSet<>();\nset.add(3); set.add(1);\nSystem.out.println(set); // [1, 3]')}`,
    comparable: `${p('The `Comparable` interface imposes a total ordering on the objects of each class that implements it. This ordering is referred to as the class\'s natural ordering.')}${block('class User implements Comparable<User> {\n    String name; User(String n){name=n;}\n    public int compareTo(User o) { return name.compareTo(o.name); }\n}\nUser u1=new User("Bob"), u2=new User("Alice");\nSystem.out.println(u1.compareTo(u2) > 0); // true')}`,
    default_methods: `${p('Default methods enable you to add new functionality to the interfaces of your libraries and ensure binary compatibility with code written for older versions of those interfaces.')}${block('interface Greet { default void sayHi() { System.out.println("Hi"); } }\nclass MyGreet implements Greet {}\nnew MyGreet().sayHi(); // Hi')}`,
    abstract_class_again: `${p('Abstract classes are similar to interfaces but can have fields that are not static and final, and they can contain non-abstract methods.')}${block('abstract class Shape { abstract double area(); }\nclass Circle extends Shape { double r=2; double area() {return 3.14*r*r;} }\nSystem.out.println(new Circle().area()); // 12.56')}`,
    localdate: `${p('`LocalDate` is an immutable date-time object that represents a date, often viewed as year-month-day.')}${block('import java.time.LocalDate;\nLocalDate date = LocalDate.of(2023, 1, 31);\nSystem.out.println(date.plusDays(1)); // 2023-02-01')}`,
    regex_find: `${p('The `Matcher` class finds matches for a regular expression pattern in a string. The `find()` method scans the input sequence to find the next subsequence that matches the pattern.')}${block('import java.util.regex.*;\nMatcher m = Pattern.compile("\\\\d+").matcher("a12b34c");\nwhile (m.find()) { System.out.println(m.group()); } // 12, 34')}`,
    arraydeque: `${p('`ArrayDeque` is a resizable-array implementation of the `Deque` interface. It has no capacity restrictions and is faster than LinkedList for stack and queue operations.')}${block('import java.util.ArrayDeque;\nArrayDeque<Integer> dq = new ArrayDeque<>();\ndq.addFirst(1); dq.addLast(2);\nSystem.out.println(dq.pollFirst()); // 1')}`,
    string_format: `${p('`String.format()` returns a formatted string using the specified format string and arguments.')}${block('String s = String.format("Hello, %s! You have %d messages.", "Alice", 5);\nSystem.out.println(s);')}`,
    arrays_stream: `${p('`Arrays.stream()` returns a sequential Stream with the specified array as its source.')}${block('import java.util.Arrays;\nint[] arr = {1, 2, 3};\nSystem.out.println(Arrays.stream(arr).sum()); // 6')}`,
    distinct: `${p('The `distinct()` stream operation returns a stream consisting of the distinct elements (according to `Object.equals(Object)`) of this stream.')}${block('import java.util.stream.Stream;\nStream.of(1, 2, 1, 3).distinct().forEach(System.out::println); // 1, 2, 3')}`,
    groupingby: `${p('`Collectors.groupingBy` is used for grouping objects by some property and storing results in a Map instance.')}${block('import java.util.stream.*;\nimport java.util.List;\nSystem.out.println(Stream.of("a", "bb", "ccc", "dd").collect(Collectors.groupingBy(String::length))); // {1=[a], 2=[bb, dd], 3=[ccc]}')}`,
    flatmap: `${p('`flatMap` transforms each element of a stream into another stream and then concatenates these streams into a single, "flattened" stream.')}${block('import java.util.stream.*;\nimport java.util.List;\nList<List<Integer>> listOfLists = List.of(List.of(1), List.of(2, 3));\nlistOfLists.stream().flatMap(List::stream).forEach(System.out::println); // 1, 2, 3')}`,
    compute: `${p('`Map.compute()` attempts to compute a mapping for the specified key and its current mapped value.')}${block('import java.util.HashMap;\nHashMap<String, Integer> map = new HashMap<>();\nmap.compute("key", (k, v) -> (v == null) ? 1 : v + 1);\nSystem.out.println(map.get("key")); // 1')}`,
    partitioningby: `${p('`Collectors.partitioningBy` is a collector which partitions the input elements into a `Map<Boolean, List<T>>` according to a `Predicate`.')}${block('import java.util.stream.*;\nSystem.out.println(Stream.of(1,2,3,4).collect(Collectors.partitioningBy(n -> n%2==0))); // {false=[1, 3], true=[2, 4]}')}`,
    executorservice: `${p('`ExecutorService` is a framework for asynchronous task execution. It manages a pool of threads and a task queue.')}${block('import java.util.concurrent.*;\nExecutorService es = Executors.newSingleThreadExecutor();\nFuture<Integer> future = es.submit(() -> 1 + 1);\ntry { System.out.println(future.get()); } catch (Exception e) {}\nes.shutdown();')}`,
    completablefuture: `${p('`CompletableFuture` is used for asynchronous programming. It represents a future result of an asynchronous computation.')}${block('import java.util.concurrent.CompletableFuture;\nCompletableFuture.supplyAsync(() -> "Result").thenAccept(System.out::println); // Result')}`,
    atomicinteger: `${p('An `AtomicInteger` is an `int` value that may be updated atomically, making it useful in concurrent programming without locks.')}${block('import java.util.concurrent.atomic.AtomicInteger;\nAtomicInteger ai = new AtomicInteger(5);\nSystem.out.println(ai.incrementAndGet()); // 6')}`,
    optional_orelse: `${p('`Optional.orElse()` returns the value if present, otherwise returns the other value.')}${block('import java.util.Optional;\nString name = (String) Optional.ofNullable(null).orElse("default");\nSystem.out.println(name); // default')}`,
    stringjoiner: `${p('`StringJoiner` is used to construct a sequence of characters separated by a delimiter.')}${block('import java.util.StringJoiner;\nStringJoiner sj = new StringJoiner(", ", "[", "]");\nsj.add("a").add("b");\nSystem.out.println(sj.toString()); // [a, b]')}`,
    bigdecimal: `${p('`BigDecimal` provides arbitrary-precision signed decimal numbers. Use it for financial calculations where precision is critical.')}${block('import java.math.BigDecimal;\nBigDecimal a = new BigDecimal("0.1");\nBigDecimal b = new BigDecimal("0.2");\nSystem.out.println(a.add(b)); // 0.3')}`,
    replaceall: `${p('`String.replaceAll()` replaces each substring of this string that matches the given regular expression with the given replacement.')}${block('String s = "a1b2c3";\nSystem.out.println(s.replaceAll("\\\\d", "#")); // a#b#c#')}`,
    case_insensitive_sort: `${p('`String.CASE_INSENSITIVE_ORDER` is a `Comparator` that orders `String` objects as by `compareToIgnoreCase`.')}${block('import java.util.Arrays;\nString[] arr = {"Bob", "alice"};\nArrays.sort(arr, String.CASE_INSENSITIVE_ORDER);\nSystem.out.println(Arrays.toString(arr)); // [alice, Bob]')}`,
    string_repeat: `${p('`String.repeat(n)` returns a string whose value is the concatenation of this string repeated `n` times.')}${block('System.out.println("-".repeat(5)); // -----')}`,
    varargs: `${p('Varargs allows a method to accept zero or more arguments. The varargs parameter is treated as an array of the specified type.')}${block('static int sum(int... nums) {\n    return java.util.Arrays.stream(nums).sum();\n}\nSystem.out.println(sum(1, 2, 3)); // 6')}`,
    interface_static: `${p('Static methods in interfaces are part of the interface, not the implementing classes. They are called using the interface name.')}${block('interface Util { static String greet() { return "Hello"; } }\nSystem.out.println(Util.greet()); // Hello')}`,
    try_with_resources: `${p('The try-with-resources statement ensures that each resource is closed at the end of the statement. Any object that implements `AutoCloseable` can be used as a resource.')}${block('import java.io.*;\ntry (StringReader r = new StringReader("text")) {\n    System.out.println((char)r.read()); // t\n} catch (IOException e) {}')}`,
    priorityqueue: `${p('A `PriorityQueue` is a heap-based queue where elements are ordered according to their natural ordering, or by a `Comparator`.')}${block('import java.util.PriorityQueue;\nPriorityQueue<Integer> pq = new PriorityQueue<>();\npq.add(3); pq.add(1);\nSystem.out.println(pq.poll()); // 1')}`,
    linkedlist: `${p('A `LinkedList` is a doubly-linked list implementation of the `List` and `Deque` interfaces. It is efficient for additions and removals.')}${block('import java.util.LinkedList;\nLinkedList<String> list = new LinkedList<>();\nlist.addFirst("a");\nlist.addLast("b");\nSystem.out.println(list); // [a, b]')}`,
    deque_stack: `${p('The `Deque` interface provides stack operations like `push` and `pop`. `ArrayDeque` is the recommended implementation.')}${block('import java.util.ArrayDeque;\nArrayDeque<Integer> stack = new ArrayDeque<>();\nstack.push(1); stack.push(2);\nSystem.out.println(stack.pop()); // 2')}`,
    treemap: `${p('A `TreeMap` is a NavigableMap implementation that keeps its entries sorted according to the natural ordering of its keys, or by a `Comparator`.')}${block('import java.util.TreeMap;\nTreeMap<Integer, String> map = new TreeMap<>();\nmap.put(3, "c"); map.put(1, "a");\nSystem.out.println(map.firstKey()); // 1')}`,
    stringbuilder_reverse: `${p('`StringBuilder.reverse()` causes this character sequence to be replaced by the reverse of the sequence.')}${block('StringBuilder sb = new StringBuilder("abc");\nSystem.out.println(sb.reverse().toString()); // cba')}`,
    regex_groups: `${p('Parentheses `()` in a regex create capturing groups. You can access the captured text using `matcher.group(index)`.')}${block('import java.util.regex.*;\nMatcher m = Pattern.compile("(\\\\d+)-(\\w+)").matcher("123-xyz");\nif (m.find()) { System.out.println(m.group(2)); } // xyz')}`,
    binary_search: `${p('`Arrays.binarySearch` searches the specified array for the specified value using the binary search algorithm. The array must be sorted.')}${block('import java.util.Arrays;\nint[] arr = {10, 20, 30};\nSystem.out.println(Arrays.binarySearch(arr, 20)); // 1')}`,
    map_merge: `${p('`Map.merge` lets you update a map entry by applying a function to the old and new values.')}${block('import java.util.HashMap;\nHashMap<String, Integer> counts = new HashMap<>();\ncounts.merge("apple", 1, Integer::sum);\ncounts.merge("apple", 1, Integer::sum);\nSystem.out.println(counts.get("apple")); // 2')}`,
    capstone: `${p('This capstone combines streams, comparators, and Optionals to find the object with the maximum value in a collection.')}${block('import java.util.*;\nclass S { String n; int s; S(String n, int s){this.n=n;this.s=s;} }\nList<S> list = List.of(new S("A",90), new S("B",100));\nlist.stream().max(Comparator.comparingInt(s -> s.s))\n    .ifPresent(s -> System.out.println(s.n)); // B')}`,
  };

  const has = (arr) => arr.some(k => title.includes(k));
  let key = has(['hello']) && 'hello'
        || has(['variable','data type']) && 'variables'
        || has(['while']) && 'while'
        || has(['for loop','for ']) && (has(['enhanced for','for-each','for each']) ? 'foreach' : 'for')
        || has(['array ']) && 'array'
        || has(['if / else','if/ else','if ']) && 'ifelse'
        || has(['switch']) && (has(['enum']) ? 'enum_switch' : 'switch')
        || has(['scanner','input']) && 'scanner'
        || has(['string']) && (has(['format']) ? 'string_format' : (has(['repeat']) ? 'string_repeat' : 'string'))
        || has(['method']) && (has(['reference']) ? 'method_refs' : 'methods')
        || has(['class']) && (has(['abstract']) ? 'abstract_class_again' : 'classes')
        || has(['exception','try/catch']) && 'exceptions'
        || has(['fizzbuzz']) && 'fizzbuzz'
        || has(['arraylist','list']) && 'arraylist'
        || has(['boolean']) && 'boolean'
        || has(['hashmap']) && 'hashmap'
        || has(['streams: map', 'streams map']) && 'streams_map'
        || has(['streams: filter', 'streams filter']) && 'streams_filter'
        || has(['sort by length']) && 'sort_by_length'
        || has(['comparator on objects']) && 'comparator'
        || has(['optional.map']) && 'optional_map'
        || has(['generic']) && 'generics'
        || has(['wildcard']) && 'wildcards'
        || has(['reverse sort']) && 'reverse_sort'
        || has(['record basics']) && 'record'
        || has(['streams: reduce']) && 'streams_reduce'
        || has(['collectors.joining']) && 'collectors_joining'
        || has(['linkedhashmap']) && 'linkedhashmap'
        || has(['linkedhashset']) && 'linkedhashset'
        || has(['treeset']) && 'treeset'
        || has(['comparable']) && 'comparable'
        || has(['default method']) && 'default_methods'
        || has(['localdate']) && 'localdate'
        || has(['regex find', 'regex find']) && 'regex_find'
        || has(['arraydeque']) && 'arraydeque'
        || has(['arrays.stream']) && 'arrays_stream'
        || has(['distinct()']) && 'distinct'
        || has(['groupingby']) && 'groupingby'
        || has(['flatmap']) && 'flatmap'
        || has(['compute()']) && 'compute'
        || has(['partitioningby']) && 'partitioningby'
        || has(['executorservice']) && 'executorservice'
        || has(['completablefuture']) && 'completablefuture'
        || has(['atomicinteger']) && 'atomicinteger'
        || has(['optional.orelse']) && 'optional_orelse'
        || has(['stringjoiner']) && 'stringjoiner'
        || has(['bigdecimal']) && 'bigdecimal'
        || has(['replaceall']) && 'replaceall'
        || has(['case-insensitive sort']) && 'case_insensitive_sort'
        || has(['varargs']) && 'varargs'
        || has(['interface static method']) && 'interface_static'
        || has(['try-with-resources']) && 'try_with_resources'
        || has(['priorityqueue']) && 'priorityqueue'
        || has(['linkedlist']) && 'linkedlist'
        || has(['deque push/pop']) && 'deque_stack'
        || has(['treemap']) && 'treemap'
        || has(['stringbuilder.reverse']) && 'stringbuilder_reverse'
        || has(['regex groups']) && 'regex_groups'
        || has(['arrays.binarysearch']) && 'binary_search'
        || has(['map.merge']) && 'map_merge'
        || has(['capstone']) && 'capstone';

  if (!key || !examples[key]) {
    // Generic fallback
    return `${p('Practice the concept using a short example below.')} ${block('System.out.println("Hello, Java!");')}`;
  }
  return examples[key];
}

function enhanceJavaTutorials(filePath) {
  const abs = path.resolve(filePath);
  const json = JSON.parse(fs.readFileSync(abs, 'utf8'));
  let modified = 0;
  if (!json || !Array.isArray(json.lessons)) return { changed: false, reason: 'lessons missing' };
  json.lessons = json.lessons.map((lesson) => {
    const lang = (lesson.language || 'java').toLowerCase();
    if (lang && lang !== 'java') return lesson;
    const t = String(lesson.tutorial || '').trim();
    // A more robust check for placeholder content
    const isPlaceholder = !t.includes('code-block-wrapper') || t.length < 120;
    if (!isPlaceholder && !process.env.FORCE_ENHANCE_JAVA_TUTORIALS) return lesson;
    const enriched = buildJavaTutorial(lesson);
    if (enriched === lesson.tutorial) return lesson;
    modified++;
    return { ...lesson, tutorial: enriched };
  });
  fs.writeFileSync(abs, JSON.stringify(json, null, 2), 'utf8');
  return { changed: modified > 0, count: modified };
}

function enhancePythonTutorials(filePath) {
  const abs = path.resolve(filePath);
  const json = JSON.parse(fs.readFileSync(abs, 'utf8'));
  let modified = 0;
  if (!json || !Array.isArray(json.lessons)) return { changed: false, reason: 'lessons missing' };
  json.lessons = json.lessons.map((lesson) => {
    const lang = (lesson.language || '').toLowerCase();
    if (lang && lang !== 'python') return lesson;
    const t = String(lesson.tutorial || '').trim();
    const isPlaceholder = !t.includes('code-block-wrapper') || t.length < 100;
    if (!isPlaceholder && !process.env.FORCE_ENHANCE_PY_TUTORIALS) return lesson;
    const enriched = buildPythonTutorial(lesson);
    if (enriched === lesson.tutorial) return lesson;
    modified++;
    return { ...lesson, tutorial: enriched };
  });
  fs.writeFileSync(abs, JSON.stringify(json, null, 2), 'utf8');
  return { changed: modified > 0, count: modified };
}

function main() {
  const rm = removeInlineBlock('public/index.html', '/* Inlined Java lessons removed; rely on JSON files only.', '*/');
  if (rm.changed) {
    console.log('Removed commented inline Java lessons from public/index.html');
  } else {
    console.log('No inline Java lessons block found (or already removed).');
  }

  const enhJava = enhanceJavaTutorials('public/lessons-java.json');
  if (enhJava.changed) {
    console.log(`Enhanced Java tutorials with example code blocks (${enhJava.count} lessons updated).`);
  } else {
    console.log('Java tutorials already enhanced or file missing.');
  }

  const enh = enhancePythonTutorials('public/lessons-python.json');
  if (enh.changed) {
    console.log(`Enhanced Python tutorials with example code blocks (${enh.count} lessons updated).`);
  } else {
    console.log('Python tutorials already enhanced or file missing.');
  }
}

main();
