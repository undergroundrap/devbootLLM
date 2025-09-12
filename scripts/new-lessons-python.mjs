export const lessons = [
  {
    title: "Assertions for Lightweight Tests",
    language: "python",
    description: "Implement add(a, b) and verify with assert; print OK when all tests pass.",
    initialCode: `def add(a, b):
    # TODO: return the sum
    pass

# Add a couple of asserts and print "OK" if they pass
`,
    fullSolution: `def add(a, b):
    return a + b

assert add(2, 3) == 5
assert add(-1, 1) == 0
print("OK")
`,
    expectedOutput: "OK",
    tutorial: `<p class=\"mb-4 text-gray-300\">assert is a simple built-in way to check expectations while coding. If the condition is False, Python raises AssertionError and stops; if all asserts pass, execution continues.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">def square(x):
    return x * x

assert square(3) == 9
print("OK")</pre></div>`
  },
  {
    title: "Regex Basics: Extract Email",
    language: "python",
    description: "Use re.search to find and print the email in the given text.",
    initialCode: `import re
text = "Contact us at support@example.com for help."
# Print the email address from text
`,
    fullSolution: `import re
text = "Contact us at support@example.com for help."
m = re.search(r"[\w\.-]+@[\w\.-]+", text)
if m:
    print(m.group(0))
`,
    expectedOutput: "support@example.com",
    tutorial: `<p class=\"mb-4 text-gray-300\">Regular expressions match patterns in text. Use re.search to find the first match, and groups to extract portions.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">import re
m = re.search(r"\d+", "Order A-1023")
print(m.group(0))  # 1023</pre></div>`
  },
  {
    title: "JSON Encode/Decode",
    language: "python",
    description: "Serialize a dict to JSON and parse it back; print the name value.",
    initialCode: `import json
data = {"name": "Alice", "age": 30}
# Dump to JSON, load it back, then print the name
`,
    fullSolution: `import json
data = {"name": "Alice", "age": 30}
s = json.dumps(data)
obj = json.loads(s)
print(obj["name"])\n`,
    expectedOutput: "Alice",
    tutorial: `<p class=\"mb-4 text-gray-300\">Use the json module to convert between Python objects and JSON strings: dumps() to serialize, loads() to parse.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">import json
payload = {"ok": True}
s = json.dumps(payload)
print(s)  # {\"ok\": true}</pre></div>`
  }
];

