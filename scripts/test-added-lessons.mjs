#!/usr/bin/env node
import { spawn } from 'node:child_process';

const PORT = process.env.PORT || '3200';
const SERVER_URL = `http://localhost:${PORT}`;

function startServer() {
  return new Promise((resolve, reject) => {
    const child = spawn('node', ['server.js'], {
      env: { ...process.env, PORT },
      stdio: ['ignore', 'pipe', 'pipe'],
    });
    let ready = false;
    const onData = (buf) => {
      const line = buf.toString();
      process.stdout.write(line);
      if (!ready && line.includes('devbootLLM server listening')) {
        ready = true;
        resolve(child);
      }
    };
    child.stdout.on('data', onData);
    child.stderr.on('data', (b) => process.stderr.write(b));
    child.on('error', reject);
    setTimeout(() => {
      if (!ready) reject(new Error('Server did not start within timeout'));
    }, 8000);
  });
}

async function postJson(path, payload) {
  const r = await fetch(`${SERVER_URL}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  const text = await r.text();
  try {
    return { status: r.status, json: JSON.parse(text) };
  } catch {
    return { status: r.status, json: null, text };
  }
}

function ensure(cond, msg) {
  if (!cond) throw new Error(msg);
}

async function main() {
  console.log('Starting server...');
  const child = await startServer();
  try {
    const tests = [
      {
        name: 'python 335 pathlib glob filter',
        lang: 'python',
        code: `from pathlib import Path\n\nroot = Path("src")\n\nsample_files = [\n    root / "app" / "config.py",\n    root / "app" / "models.py",\n    root / "services" / "cleanup.py",\n    root / "tests" / "test_models.py",\n]\nif not root.exists():\n    for path in sample_files:\n        path.parent.mkdir(parents=True, exist_ok=True)\n        path.write_text('# stub\\n', encoding='utf-8')\n\nfiles = []\nif root.exists():\n    files = [\n        path.relative_to(root).as_posix()\n        for path in root.rglob("*.py")\n        if not path.stem.startswith("test_")\n    ]\nfor name in sorted(files):\n    print(name)\n`,
        expect: 'app/config.py\napp/models.py\nservices/cleanup.py',
      },
      {
        name: 'python 357 decimal localcontext precision',
        lang: 'python',
        code: `from decimal import Decimal, localcontext\n\nwith localcontext() as ctx:\n    ctx.prec = 4\n    result = Decimal("1") / Decimal("3")\n    print(result)\n`,
        expect: '0.3333',
      },
      {
        name: 'python 358 contextlib.chdir temporary cwd',
        lang: 'python',
        code: `import tempfile\nfrom pathlib import Path\n\ntry:\n    from contextlib import chdir\nexcept ImportError:\n    from contextlib import contextmanager\n    import os\n\n    @contextmanager\n    def chdir(path):\n        previous = os.getcwd()\n        os.chdir(path)\n        try:\n            yield\n        finally:\n            os.chdir(previous)\n\nwith tempfile.TemporaryDirectory() as tmp:\n    root = Path(tmp)\n    reports = root / "reports"\n    reports.mkdir()\n    summary = reports / "summary.txt"\n    summary.write_text("ready\\n", encoding="utf-8")\n\n    print("outside")\n    with chdir(reports):\n        line = Path("summary.txt").read_text(encoding="utf-8").strip()\n        print(f"inside: {line}")\n    print("outside")\n`,
        expect: 'outside\ninside: ready\noutside',
      },
      {
        name: 'python 359 asyncio timeout_at deadline',
        lang: 'python',
        code: `import asyncio\n\nasync def fetch(delay):\n    await asyncio.sleep(delay)\n    return f"done in {delay:.2f}s"\n\ntry:\n    timeout_at = asyncio.timeout_at\nexcept AttributeError:\n    def timeout_at(deadline):\n        loop = asyncio.get_running_loop()\n        delay = max(0.0, deadline - loop.time())\n        return asyncio.timeout(delay)\n\nasync def main():\n    loop = asyncio.get_running_loop()\n    deadline = loop.time() + 0.05\n\n    try:\n        async with timeout_at(deadline):\n            await fetch(0.1)\n    except TimeoutError:\n        print("expired")\n\nasyncio.run(main())\n`,
        expect: 'expired',
      },
      {
        name: 'python itertools.product assertion',
        lang: 'python',
        code: `from itertools import product\nprint(len(list(product([1, 2], [3, 4]))))\n`,
        expect: '4',
      },
      {
        name: 'python collections.Counter sample',
        lang: 'python',
        code: `from collections import Counter\nprint(Counter('aab')['a'])\n`,
        expect: '2',
      },
      {
        name: 'python formatted f-string sample',
        lang: 'python',
        code: `print(f"{3.14159:.2f}")\n`,
        expect: '3.14',
      },
      {
        name: 'java 355 StackWalker method trace',
        lang: 'java',
        code: `import java.util.stream.Collectors;\nimport java.lang.StackWalker;\n\npublic class Main {\n    static final StackWalker WALKER = StackWalker.getInstance();\n\n    public static void main(String[] args) {\n        helper();\n    }\n\n    static void helper() {\n        deeper();\n    }\n\n    static void deeper() {\n        String trace = WALKER.walk(frames -> frames\n                .map(StackWalker.StackFrame::getMethodName)\n                .limit(3)\n                .collect(Collectors.joining("->")));\n        System.out.println(trace);\n    }\n}\n`,
        expect: 'deeper->helper->main',
      },
      {
        name: 'java 356 WatchService create event',
        lang: 'java',
        code: `import java.nio.file.FileSystems;\nimport java.nio.file.Files;\nimport java.nio.file.Path;\nimport java.nio.file.StandardWatchEventKinds;\nimport java.nio.file.WatchEvent;\nimport java.nio.file.WatchKey;\nimport java.nio.file.WatchService;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        Path dir = Files.createTempDirectory("watch-demo");\n        Path file = dir.resolve("notes.txt");\n\n        try (WatchService watch = FileSystems.getDefault().newWatchService()) {\n            dir.register(watch, StandardWatchEventKinds.ENTRY_CREATE);\n            Files.writeString(file, "draft\\n");\n\n            WatchKey key = watch.take();\n            for (WatchEvent<?> event : key.pollEvents()) {\n                if (event.kind() == StandardWatchEventKinds.OVERFLOW) {\n                    continue;\n                }\n                Path name = (Path) event.context();\n                System.out.println(event.kind().name() + ":" + name);\n            }\n            key.reset();\n        } finally {\n            Files.deleteIfExists(file);\n            Files.deleteIfExists(dir);\n        }\n    }\n}\n`,
        expect: 'ENTRY_CREATE:notes.txt',
      },
      {
        name: 'java 357 MethodHandle private invocation',
        lang: 'java',
        code: `import java.lang.invoke.MethodHandle;\nimport java.lang.invoke.MethodHandles;\nimport java.lang.invoke.MethodType;\n\npublic class Main {\n    static final class Greeter {\n        private String greet(String name) {\n            return "Hello " + name;\n        }\n    }\n\n    public static void main(String[] args) throws Throwable {\n        Greeter greeter = new Greeter();\n        MethodHandles.Lookup lookup = MethodHandles.lookup();\n        MethodHandle handle = lookup.findVirtual(\n                Greeter.class,\n                "greet",\n                MethodType.methodType(String.class, String.class)\n        );\n        String message = (String) handle.invokeExact(greeter, "team");\n        System.out.println(message);\n    }\n}\n`,
        expect: 'Hello team',
      },
    ];

    for (const t of tests) {
      const endpoint = t.lang === 'python' ? '/run/python' : '/run/java';
      const response = await postJson(endpoint, { code: t.code });
      ensure(response.status === 200 && response.json, `Bad status for ${t.name}`);
      ensure(!response.json.error, `${t.name} runtime error: ${response.json.output || response.json.error}`);
      const out = String(response.json.output ?? '').trim();
      const normalized = out.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
      ensure(normalized === t.expect, `${t.name} mismatch: got '${normalized}' (raw '${out}'), want '${t.expect}'`);
      console.log(`${t.name} OK -> ${normalized}`);
    }
    console.log('All lesson smoke tests passed.');
  } finally {
    try { process.kill(child.pid); } catch {}
  }
}

main().catch((e) => {
  console.error('Test failed:', e.message);
  process.exit(1);
});
