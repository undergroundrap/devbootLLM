#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const LEVELS = ["Beginner", "Intermediate", "Advanced"];
const CORE_TAG = "Core Language";
const MAX_ADDITIONAL = 4;
const PRESERVE_TAGS = new Set(["Git", "Workflow", "Flask", "Project", "Deployment", "Testing", "Tooling"]);

const levelRules = [
  { tag: "Beginner", test: lesson => Number(lesson.id) <= 80 },
  { tag: "Intermediate", test: lesson => Number(lesson.id) > 80 && Number(lesson.id) <= 220 },
  { tag: "Advanced", test: lesson => Number(lesson.id) > 220 }
];

const topicRules = [
  { tag: "Basics", priority: 10, maxId: 60 },
  { tag: "Control Flow", priority: 20, anyToken: ["if", "elif", "else", "switch", "case", "match", "while", "for"] },
  { tag: "Functions", priority: 30, anyToken: ["def", "lambda", "function", "callable", "method"] },
  { tag: "Strings", priority: 40, match: ({ hay }) => /\b(substring|split|join|format|uppercase|lowercase|strip|trim|regex|stringbuilder|char|f-string|startswith|endswith)\b/.test(hay) },
  { tag: "Collections", priority: 50, anyToken: ["list", "lists", "dict", "map", "set", "tuple", "collections", "deque", "queue", "stack", "array", "arraylist", "hashmap", "linkedlist", "collection"] },
  { tag: "OOP", priority: 60, anyToken: ["class", "interface", "implements", "extends", "inheritance", "polymorphism", "object", "dataclass", "constructor", "encapsulation"] },
  { tag: "Math and Stats", priority: 70, anyToken: ["math", "statistics", "random", "decimal", "fractions", "quantiles", "sqrt", "pow", "factorial", "gcd", "variance", "stdev"] },
  { tag: "Algorithms", priority: 80, any: ["algorithm", "sort", "sorted", "search", "binary search", "graph", "tree", "topological", "bfs", "dfs", "dijkstra", "permutation", "combination", "heap", "priority queue", "dynamic programming", "dp", "backtracking", "recursion", "shortest path"], anyToken: ["dijkstra", "topological", "permutation", "combination", "heap", "graph"] },
  { tag: "I/O", priority: 90, any: ["with open", "open(", "pathlib", "read_text", "write_text", "readlines", "java.nio", "files.", "inputstream", "outputstream", "reader", "writer", "fileinputstream", "fileoutputstream", "path.of", "os.path"] },
  { tag: "Serialization", priority: 100, any: ["json", "yaml", "pickle", "marshal", "serialize", "deserialize", "toml", "csv", "xml", "objectmapper", "gson", "jackson", "protobuf", "bson", "messagepack", "tomllib", "tarfile"] },
  { tag: "Networking", priority: 110, any: ["socket", "http", "tcp", "udp", "client", "server", "endpoint", "request", "response", "httpclient", "urlopen", "websocket"] },
  { tag: "Web", priority: 120, any: ["flask", "fastapi", "django", "spring", "controller", "restcontroller", "servlet", "router", "template", "jinja", "view"] },
  { tag: "Databases", priority: 130, any: ["sql", "sqlite", "postgres", "mysql", "database", "query", "transaction", "jdbc", "jpa", "hibernate", "entitymanager", "cursor"] },
  { tag: "Concurrency", priority: 140, any: ["thread", "threading", "lock", "mutex", "synchronized", "concurrent", "executor", "threadpool", "volatile", "atomic", "semaphore"] },
  { tag: "Async", priority: 150, any: ["async ", "asyncio", "await", "coroutine", "event loop", "completablefuture", "future", "promise", "structuredtaskscope", "async def", "task "] },
  { tag: "Testing", priority: 160, any: ["pytest", "unittest", "assert", "testcase", "junit", "assertequals", "mockito", "asserttrue", "assertfalse", "assert_that"] },
  { tag: "Tooling", priority: 170, any: ["virtualenv", "poetry", "pip ", "pipenv", "black", "flake8", "git ", "docker", "maven", "gradle", "lint", "formatter", "requirements.txt", "pyproject", "setuptools", "build.gradle", "package.json", "pre-commit", "ruff"] },
  { tag: "Security", priority: 180, any: ["hash", "encrypt", "decrypt", "jwt", "oauth", "secrets", "ssl", "bcrypt", "token", "crypto", "signature", "sha256"] },
  { tag: "CLI", priority: 190, any: ["argparse", "click", "typer", "command-line", "cli ", "terminal", "shell command", "options parsing", "flags", "prompt", "readline"] },
  { tag: "Type System", priority: 200, any: ["typing", "typevar", "generic", "protocol", "mypy", "annotated", "literal", "typedict", "typeddict", "newtype", "record ", "sealed", "variance", "type hint", "type token", "class<?>", "wildcard type"] },
  { tag: "Performance", priority: 210, any: ["timeit", "profile", "benchmark", "performance", "lru_cache", "optimize", "profiling", "timing", "jmh", "microbenchmark"] },
  { tag: "Debugging", priority: 220, any: ["logging", "traceback", "debug", "stack trace", "logger", "printstacktrace"] },
  { tag: "Data Science", priority: 230, any: ["pandas", "numpy", "dataframe", "series", "matplotlib", "seaborn", "polars", "scikit"] },
  { tag: "Design Patterns", priority: 240, any: ["builder pattern", "factory pattern", "strategy pattern", "observer pattern", "singleton", "adapter pattern", "command pattern", "visitor pattern"] },
  { tag: "Functional", priority: 250, any: ["map(", "filter(", "reduce(", "lambda ", "itertools", "functools", "collect(", "flatmap", "optional.map", "function<"] },
  { tag: "Error Handling", priority: 260, match: ({ hay }) => /try\s*[{:]/.test(hay) && /(catch\s*\(|except\s+)/.test(hay) },
  { tag: "Date/Time", priority: 270, any: ["datetime", "timedelta", "timezone", "calendar", "dateutil", "localdate", "localdatetime", "zoneddatetime", "instant", "offsetdatetime", "chrono"] },
  { tag: "Metaprogramming", priority: 280, any: ["inspect", "reflection", "metaclass", "getattr", "setattr", "methodhandles", "proxy", "dynamic invocation", "__getattr__", "__setattr__"] },
  { tag: "Generators", priority: 290, any: ["yield", "yield from", "generator", "comprehension", "iterable"], anyToken: ["generator", "yield"] },
  { tag: "Decorators", priority: 300, any: ["@wraps", "decorator", "@lru_cache", "@cache", "@contextmanager", "@classmethod", "@staticmethod", "@dataclass"] },
  { tag: "Parsing", priority: 310, any: ["parse", "parser", "tokenize", "ast.", "beautifulsoup", "xml.etree", "regex parser", "antlr", "csv.reader"] },
  { tag: "Packaging", priority: 320, any: ["setup.cfg", "pyproject", "wheel", "module-info", "manifest", "dependency", "artifact", "distribution", "pom.xml"] },
  { tag: "Regex", priority: 330, match: ({ hay }) => /\bregex\b/.test(hay) || /pattern\.compile/.test(hay) || /matches\(/.test(hay) || /(?:^|[^a-z])re\./.test(hay) },
  { tag: "Streams", priority: 340, language: "java", any: ["stream.", "stream<", "collect(", "collectors", "stream.of", "flatmap", "peek("] }
];

function stripHtml(value) {
  if (!value) return "";
  return String(value).replace(/<[^>]+>/g, " ");
}

function buildContext(lesson) {
  const parts = [
    lesson.title,
    lesson.description,
    lesson.initialCode,
    lesson.fullSolution,
    lesson.expectedOutput,
    lesson.tutorial
  ];
  const hay = parts
    .filter(Boolean)
    .map(stripHtml)
    .join(" ")
    .toLowerCase();
  const tokens = hay.replace(/[^a-z0-9.]+/g, " ").split(/\s+/).filter(Boolean);
  const tokenSet = new Set(tokens);
  return { hay, tokens, tokenSet };
}

function matchesRule(rule, context, lesson, language) {
  if (rule.language && rule.language !== language) return false;
  if (rule.minId !== undefined && Number(lesson.id) < rule.minId) return false;
  if (rule.maxId !== undefined && Number(lesson.id) > rule.maxId) return false;

  if (rule.match) {
    try {
      return !!rule.match(context, lesson);
    } catch {
      return false;
    }
  }

  const { hay, tokenSet } = context;

  if (rule.not && rule.not.some(word => hay.includes(word))) return false;
  if (rule.notToken && rule.notToken.some(word => tokenSet.has(word))) return false;
  if (rule.all && !rule.all.every(word => hay.includes(word))) return false;
  if (rule.allToken && !rule.allToken.every(word => tokenSet.has(word))) return false;

  let positive = false;
  if (rule.any && rule.any.some(word => hay.includes(word))) positive = true;
  if (!positive && rule.anyToken && rule.anyToken.some(word => tokenSet.has(word))) positive = true;
  if (!positive && rule.regex && rule.regex.test(hay)) positive = true;
  if (!positive && !rule.any && !rule.anyToken && !rule.regex && !rule.match) positive = true;
  return positive;
}

function assignTags(lesson, language) {
  const original = Array.isArray(lesson.tags) ? lesson.tags.filter(tag => typeof tag === "string" && tag.trim()) : [];
  const existingNonLevels = original.filter(tag => !LEVELS.includes(tag) && PRESERVE_TAGS.has(tag));
  const context = buildContext(lesson);

  const derivedMap = new Map();
  for (const rule of topicRules) {
    if (!matchesRule(rule, context, lesson, language)) continue;
    const priority = rule.priority ?? (400 + derivedMap.size);
    const current = derivedMap.get(rule.tag);
    if (current === undefined || priority < current) {
      derivedMap.set(rule.tag, priority);
    }
  }

  const derived = Array.from(derivedMap.entries())
    .sort((a, b) => a[1] - b[1])
    .map(entry => entry[0]);

  const finalTags = [];
  const tagSet = new Set();

  for (const level of LEVELS) {
    const rule = levelRules.find(r => r.tag === level);
    if (rule && rule.test(lesson)) {
      finalTags.push(level);
      tagSet.add(level);
    }
  }

  if (!finalTags.length) {
    finalTags.push("Intermediate");
    tagSet.add("Intermediate");
  }

  for (const tag of existingNonLevels) {
    if (tagSet.has(tag)) continue;
    finalTags.push(tag);
    tagSet.add(tag);
  }

  const currentExtras = finalTags.filter(tag => !LEVELS.includes(tag)).length;
  const slots = Math.max(0, MAX_ADDITIONAL - currentExtras);

  const newTopics = [];
  for (const tag of derived) {
    if (tagSet.has(tag) || LEVELS.includes(tag)) continue;
    newTopics.push(tag);
    tagSet.add(tag);
    if (newTopics.length >= slots) break;
  }

  if (!existingNonLevels.length && !newTopics.length) {
    finalTags.push(CORE_TAG);
  } else {
    finalTags.push(...newTopics);
  }

  lesson.tags = finalTags;
  return lesson;
}

function processFile(relPath, language) {
  const abs = path.resolve(relPath);
  const data = JSON.parse(fs.readFileSync(abs, "utf8"));
  data.lessons = data.lessons.map(lesson => assignTags(lesson, language));
  fs.writeFileSync(abs, JSON.stringify(data, null, 2) + "\n", "utf8");
  return { file: relPath, total: data.lessons.length };
}

const targets = [
  { file: "public/lessons-python.json", language: "python" },
  { file: "public/lessons-java.json", language: "java" }
];

const results = targets.map(t => processFile(t.file, t.language));
results.forEach(res => {
  console.log(`Tagged ${res.total} lessons in ${res.file}`);
});
