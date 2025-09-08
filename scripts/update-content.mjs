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
  // If the next lines already include the external JSON setup, keep as is.
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
    json: `${p('json.loads parses a JSON string into Python objects; json.dumps serializes Python objects to JSON strings.')}${block('import json\ns = "{\"name\": \"Ada\"}"\nobj = json.loads(s)\nprint(obj["name"])')}`,
    regex: `${p('Use the re module for regular expressions. \\d matches digits; groups capture substrings for later use.')}${block("import re\nprint(re.findall(r'\\\\d', 'a1b2c3'))\n# Groups:\nm = re.search(r'^Hello\\\s+(\\\\w+)$', 'Hello World')\nprint(m.group(1))  # World")}`,
    enumerate: `${p('enumerate(iterable) gives index and value pairs for iteration.')}${block("for i,v in enumerate(['a','b','c']):\n    print(f'{i}:{v}')")}`,
    set_comp: `${p('Set comprehensions build sets; braces {} with an expression and optional condition.')}${block('{n for n in range(7) if n % 2 == 0}')}`,
    isinstance: `${p('isinstance(obj, type) checks an object\'s type (including subclass relationships).')}${block('x = 5\nprint(isinstance(x, int))\nprint(isinstance(x, str))\nprint(isinstance(x, object))')}`,
    review: `${p('Combine multiple concepts: classes, loops, and aggregations. Think in steps: represent data, iterate, and compute.')}${block("class Student:\n    def __init__(self, name, score):\n        self.name, self.score = name, score\nstudents=[Student('A',90), Student('B',80)]\nprint(sum(s.score for s in students)/len(students))")}`,
  };

  const choose = (keys) => keys.find(k => title.includes(k));
  let key = choose(['hello']) && 'hello'
         || choose(['variable','data']) && 'variables'
         || choose(['while']) && 'while'
         || choose(['for-','for loops','for ']) && 'for'
         || choose(['list basics','lists basics','list ']) && 'list'
         || choose(['function']) && (title.includes('parameter') ? 'params' : 'functions')
         || choose(['if / else','if/ else','if /','if ']) && 'ifelse'
         || choose(['sum','range()']) && 'sum'
         || choose(['f-strings','strings & f']) && 'fstring'
         || choose(['dictionar']) && 'dict'
         || choose(['boolean']) && 'boolean'
         || choose(['for-each']) && 'foreach'
         || choose(['list methods']) && 'list_methods'
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
         || choose(['list comprehension']) && 'list_comp'
         || choose(['lambda','map','filter']) && 'lambda_map_filter'
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
         || choose(['context']) && 'context'
         || choose(['sorting']) && 'sorting'
         || choose(['dict comprehension']) && 'dict_comp'
         || choose(['generator']) && 'generators'
         || choose(['json ']) && 'json'
         || choose(['regular expressions','regex']) && 'regex'
         || choose(['enumerate']) && 'enumerate'
         || choose(['set comprehension']) && 'set_comp'
         || choose(['isinstance']) && 'isinstance'
         || choose(['review']) && 'review';

  if (!key || !examples[key]) {
    const intro = p(desc || 'Practice the concept with a short example below.');
    return `${intro}${block('x = 10\ny = 20\nprint(x + y)')}`;
  }
  return examples[key];
}

function ensureParagraph(htmlOrText) {
  const s = String(htmlOrText || '').trim();
  if (!s) return '';
  // If looks like HTML already, return as is; else wrap in <p>
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
  };

  const has = (arr) => arr.some(k => title.includes(k));
  let key = has(['hello']) && 'hello'
        || has(['variable','data type']) && 'variables'
        || has(['while']) && 'while'
        || has(['for loop','for ']) && 'for'
        || has(['enhanced for','for-each','for each']) && 'foreach'
        || has(['array ']) && 'array'
        || has(['if / else','if/ else','if ']) && 'ifelse'
        || has(['switch']) && 'switch'
        || has(['scanner','input']) && 'scanner'
        || has(['string']) && 'string'
        || has(['method']) && 'methods'
        || has(['class']) && 'classes'
        || has(['exception','try/catch']) && 'exceptions'
        || has(['fizzbuzz']) && 'fizzbuzz'
        || has(['arraylist','list']) && 'arraylist'
        || has(['boolean']) && 'boolean';

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
    const hasBlock = t.includes('code-block-wrapper');
    const tooShort = t.length < 120;
    if (hasBlock && !tooShort && !process.env.FORCE_ENHANCE_JAVA_TUTORIALS) return lesson;
    const intro = tooShort ? ensureParagraph(lesson.description || '') : (t || ensureParagraph(lesson.description || ''));
    const example = buildJavaTutorial(lesson);
    const enriched = `${intro}${example}`;
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
    const isPlaceholder = /Welcome to Python!|^<p class="mb-4 text-gray-300">.*<\/p>\s*<h4/.test(t) || t.length < 80;
    if (!isPlaceholder && !process.env.FORCE_ENHANCE_PY_TUTORIALS) return lesson;
    const enriched = buildPythonTutorial(lesson);
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
