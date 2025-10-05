export const lessons = [
  {
    "title": "TypeVarTuple callable forwarding",
    "language": "python",
    "description": "Forward arbitrary positional arguments to a callable using TypeVarTuple and Unpack, then prefix the result before printing it.",
    "initialCode": "from typing import Callable, TypeVarTuple, Unpack\n\nTs = TypeVarTuple(\"Ts\")\n\ndef call_with_prefix(prefix: str, fn: Callable[[Unpack[Ts]], str], *args: Unpack[Ts]) -> str:\n    # TODO: forward args to fn and prefix the result\n    return \"\"\n\ndef describe(name: str, age: int, active: bool) -> str:\n    state = \"active\" if active else \"inactive\"\n    return f\"{name} ({age}) is {state}\"\n\n# Expect to print: team: Ada (36) is active\nprint(call_with_prefix(\"team\", describe, \"Ada\", 36, True))\n",
    "fullSolution": "from typing import Callable, TypeVarTuple, Unpack\n\nTs = TypeVarTuple(\"Ts\")\n\ndef call_with_prefix(prefix: str, fn: Callable[[Unpack[Ts]], str], *args: Unpack[Ts]) -> str:\n    result = fn(*args)\n    return f\"{prefix}: {result}\"\n\ndef describe(name: str, age: int, active: bool) -> str:\n    state = \"active\" if active else \"inactive\"\n    return f\"{name} ({age}) is {state}\"\n\nprint(call_with_prefix(\"team\", describe, \"Ada\", 36, True))\n",
    "expectedOutput": "team: Ada (36) is active",
    "tutorial": "<p class=\"mb-4 text-gray-300\">Use <code>TypeVarTuple</code> with <code>Unpack</code> to bind an arbitrary number of positional argument types and forward them safely. The type checker verifies that <code>call_with_prefix</code> only accepts callables compatible with the provided arguments.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">Ts = TypeVarTuple(\"Ts\")\ndef wrapper(fn: Callable[[Unpack[Ts]], R], *args: Unpack[Ts]) -&gt; R:\n    return fn(*args)</pre></div>\n<p class=\"mt-4 text-gray-300\">This keeps helper utilities transparent to static typing without losing the convenience of <code>*args</code>.</p>",
    "tags": [
      "Advanced",
      "Typing",
      "Functions"
    ]
  },
  {
    "title": "ParamSpec preserving decorator",
    "language": "python",
    "description": "Write a decorator that logs calls while preserving the wrapped signature with ParamSpec.",
    "initialCode": "from typing import Callable, ParamSpec, TypeVar\n\nP = ParamSpec(\"P\")\nR = TypeVar(\"R\")\n\ndef traced(fn: Callable[P, R]) -> Callable[P, R]:\n    # TODO: return a wrapper that logs args/kwargs and calls fn\n    return fn\n\ndef merge(a: int, b: int, *, sep: str = \"-\") -> str:\n    return f\"{a}{sep}{b}\"\n\nwrapped = traced(merge)\nprint(wrapped(2, 3, sep=\":\"))\n",
    "fullSolution": "from typing import Callable, ParamSpec, TypeVar\n\nP = ParamSpec(\"P\")\nR = TypeVar(\"R\")\n\ndef traced(fn: Callable[P, R]) -> Callable[P, R]:\n    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:\n        print(f\"calling {fn.__name__}(args={args}, kwargs={kwargs})\")\n        return fn(*args, **kwargs)\n\n    return wrapper\n\ndef merge(a: int, b: int, *, sep: str = \"-\") -> str:\n    return f\"{a}{sep}{b}\"\n\nwrapped = traced(merge)\nprint(wrapped(2, 3, sep=\":\"))\n",
    "expectedOutput": "calling merge(args=(2, 3), kwargs={'sep': ':'})\n2:3",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>ParamSpec</code> captures a callable's full signature so decorators can forward both positional and keyword arguments without erasing type information.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">P = ParamSpec(\"P\")\nR = TypeVar(\"R\")\ndef decorator(fn: Callable[P, R]) -&gt; Callable[P, R]:\n    def wrapper(*args: P.args, **kwargs: P.kwargs) -&gt; R:\n        return fn(*args, **kwargs)\n    return wrapper</pre></div>\n<p class=\"mt-4 text-gray-300\">Use this pattern for logging, retries, or metrics wrappers that must remain transparent to static analyzers.</p>",
    "tags": [
      "Advanced",
      "Typing",
      "Decorators"
    ]
  },
  {
    "title": "assert_never exhaustiveness",
    "language": "python",
    "description": "Use typing.assert_never to make a status handler exhaustive and print the chosen branch.",
    "initialCode": "from typing import Literal, assert_never\n\nStatus = Literal[\"ok\", \"retry\", \"error\"]\n\ndef describe(status: Status) -> str:\n    # TODO: handle each literal and call assert_never(status) in the fallback\n    return \"\"\n\nprint(describe(\"retry\"))\n",
    "fullSolution": "from typing import Literal, assert_never\n\nStatus = Literal[\"ok\", \"retry\", \"error\"]\n\ndef describe(status: Status) -> str:\n    if status == \"ok\":\n        return \"All systems go\"\n    if status == \"retry\":\n        return \"Retry scheduled\"\n    if status == \"error\":\n        return \"Escalate immediately\"\n    assert_never(status)\n\nprint(describe(\"retry\"))\n",
    "expectedOutput": "Retry scheduled",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>assert_never</code> tells static type-checkers that all valid options were covered. If a new literal is added to <code>Status</code> and the handler is not updated, type-checking will fail.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">match status:\n    case \"ok\":\n        ...\n    case _:\n        assert_never(status)</pre></div>\n<p class=\"mt-4 text-gray-300\">Keep the <code>assert_never</code> in the default branch so future states cannot slip through unnoticed.</p>",
    "tags": [
      "Advanced",
      "Typing",
      "Control Flow"
    ]
  },
  {
    "title": "asyncio.Barrier coordination",
    "language": "python",
    "description": "Coordinate two async workers with asyncio.Barrier so they launch together, then print the recorded timeline.",
    "initialCode": "import asyncio\n\nasync def worker(name: str, delay: float, barrier: asyncio.Barrier, events: list[str]) -> None:\n    await asyncio.sleep(delay)\n    events.append(f\"{name} staged\")\n    await barrier.wait()\n    await asyncio.sleep(delay / 2)\n    events.append(f\"{name} running\")\n\n\nasync def main() -> None:\n    barrier = asyncio.Barrier(3)\n    events: list[str] = []\n\n    # TODO: start two workers (alpha delay 0.01, beta delay 0.02).\n    # Let both reach the barrier, append \"launch\" to events, and\n    # have main await the barrier before gathering the tasks.\n    # Finally, print each event in events on its own line.\n\n\nasyncio.run(main())\n",
    "fullSolution": "import asyncio\n\nasync def worker(name: str, delay: float, barrier: asyncio.Barrier, events: list[str]) -> None:\n    await asyncio.sleep(delay)\n    events.append(f\"{name} staged\")\n    await barrier.wait()\n    await asyncio.sleep(delay / 2)\n    events.append(f\"{name} running\")\n\n\nasync def main() -> None:\n    barrier = asyncio.Barrier(3)\n    events: list[str] = []\n\n    tasks = [\n        asyncio.create_task(worker(\"alpha\", 0.01, barrier, events)),\n        asyncio.create_task(worker(\"beta\", 0.02, barrier, events)),\n    ]\n\n    await asyncio.sleep(0.03)\n    events.append(\"launch\")\n    await barrier.wait()\n    await asyncio.gather(*tasks)\n\n    for entry in events:\n        print(entry)\n\n\nasyncio.run(main())\n",
    "expectedOutput": "alpha staged\nbeta staged\nlaunch\nalpha running\nbeta running",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>asyncio.Barrier</code> (Python 3.11+) lets coroutines rendezvous before continuing. All registered parties must call <code>await barrier.wait()</code>; the last arrival releases everyone.</p>\n<h4 class=\"font-semibold text-gray-200\n      mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">barrier = asyncio.Barrier(n)\nawait asyncio.gather(*(worker(barrier) for _ in range(n - 1)))\nawait barrier.wait()</pre></div>\n<p class=\"mt-4 text-gray-300\">Use barriers for orchestrated rollouts where every participant must be ready before the switch flips.</p>",
    "tags": [
      "Advanced",
      "AsyncIO",
      "Concurrency"
    ]
  }
];
