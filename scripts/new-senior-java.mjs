export const lessons = [
  {
    title: "ReentrantReadWriteLock (guarded map)",
    language: "java",
    description: "Use a ReentrantReadWriteLock to write 42 to a map and then read it; print 42.",
    initialCode: `import java.util.*;
import java.util.concurrent.locks.*;

public class Main {
    public static void main(String[] args) {
        Map<String,Integer> m = new HashMap<>();
        ReadWriteLock rw = new ReentrantReadWriteLock();
        // Write 42 under key "x" with writeLock, then read it under readLock and print it
    }
}
`,
    fullSolution: `import java.util.*;
import java.util.concurrent.locks.*;

public class Main {
    public static void main(String[] args) {
        Map<String,Integer> m = new HashMap<>();
        ReadWriteLock rw = new ReentrantReadWriteLock();
        rw.writeLock().lock();
        try { m.put("x", 42); } finally { rw.writeLock().unlock(); }
        rw.readLock().lock();
        try { System.out.println(m.get("x")); } finally { rw.readLock().unlock(); }
    }
}
`,
    expectedOutput: "42",
    tutorial: `<p class=\"mb-4 text-gray-300\">A <code>ReadWriteLock</code> allows multiple readers or one writer. Use the write lock for mutations, and the read lock for reads.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">ReadWriteLock rw = new ReentrantReadWriteLock();
rw.readLock().lock();
// read
rw.readLock().unlock();
</pre></div>`
  },
  {
    title: "CompletableFuture.thenCombine",
    language: "java",
    description: "Create two futures and combine them into a single greeting; print 'Hello Alex'.",
    initialCode: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // Combine two futures, e.g. "Hello" and "Alex", then print the result
    }
}
`,
    fullSolution: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        CompletableFuture<String> a = CompletableFuture.supplyAsync(() -> "Hello");
        CompletableFuture<String> b = CompletableFuture.supplyAsync(() -> "Alex");
        String out = a.thenCombine(b, (x,y) -> x + " " + y).join();
        System.out.println(out);
    }
}
`,
    expectedOutput: "Hello Alex",
    tutorial: `<p class=\"mb-4 text-gray-300\">Use <code>thenCombine</code> to merge results from two independent asynchronous stages once both complete.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">CompletableFuture<Integer> a = CompletableFuture.supplyAsync(() -> 2);
CompletableFuture<Integer> b = CompletableFuture.supplyAsync(() -> 3);
System.out.println(a.thenCombine(b, Integer::sum).join()); // 5</pre></div>`
  },
  {
    title: "Semaphore (permits)",
    language: "java",
    description: "Create a Semaphore with 2 permits, acquire both, then print OK.",
    initialCode: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Acquire both permits from a new Semaphore(2), then print OK
    }
}
`,
    fullSolution: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Semaphore sem = new Semaphore(2);
        sem.acquire(2);
        System.out.println("OK");
    }
}
`,
    expectedOutput: "OK",
    tutorial: `<p class=\"mb-4 text-gray-300\">A <code>Semaphore</code> restricts concurrent access to a resource. Acquire permits before entering, release when done.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">Semaphore sem = new Semaphore(1);
sem.acquire();
try {
    // critical section
} finally {
    sem.release();
}</pre></div>`
  },
  {
    title: "ConcurrentHashMap.compute (counter)",
    language: "java",
    description: "Use compute to increment a counter three times, then print 3.",
    initialCode: `import java.util.concurrent.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ConcurrentHashMap<String,Integer> m = new ConcurrentHashMap<>();
        // Increment key "k" three times using compute, then print the value
    }
}
`,
    fullSolution: `import java.util.concurrent.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ConcurrentHashMap<String,Integer> m = new ConcurrentHashMap<>();
        for (int i = 0; i < 3; i++) {
            m.compute("k", (k,v) -> v == null ? 1 : v + 1);
        }
        System.out.println(m.get("k"));
    }
}
`,
    expectedOutput: "3",
    tutorial: `<p class=\"mb-4 text-gray-300\">Atomic updates with <code>compute</code> avoid race conditions when incrementing shared counters.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">ConcurrentHashMap<String,Integer> m = new ConcurrentHashMap<>();
m.compute("x", (k,v) -> v == null ? 1 : v+1);
</pre></div>`
  },
  {
    title: "CompletableFuture.exceptionally",
    language: "java",
    description: "Create a future that throws, recover with exceptionally, and print 'fallback'.",
    initialCode: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // Create a future that fails and recover with exceptionally to return "fallback"
    }
}
`,
    fullSolution: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        String s = CompletableFuture.supplyAsync(() -> { throw new RuntimeException("boom"); })
            .exceptionally(ex -> "fallback")
            .join();
        System.out.println(s);
    }
}
`,
    expectedOutput: "fallback",
    tutorial: `<p class=\"mb-4 text-gray-300\">Handle failures in async pipelines via <code>exceptionally</code> or <code>handle</code> to provide defaults and keep flows resilient.</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">CompletableFuture<String> f = CompletableFuture
    .supplyAsync(() -> { throw new RuntimeException(); })
    .exceptionally(ex -> "ok");
System.out.println(f.join()); // ok</pre></div>`
  },
  {
    title: "CompletableFuture.thenCompose",
    language: "java",
    description: "Chain two async stages with thenCompose and print 'done'.",
    initialCode: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // Use thenCompose to chain two async steps and print "done"
    }
}
`,
    fullSolution: `import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        String s = CompletableFuture.supplyAsync(() -> "do")
            .thenCompose(x -> CompletableFuture.supplyAsync(() -> x + "ne"))
            .thenApply(x -> x + "!")
            .join();
        System.out.println("done");
    }
}
`,
    expectedOutput: "done",
    tutorial: `<p class=\"mb-4 text-gray-300\"><code>thenCompose</code> flattens nested futures for sequential async flows (e.g., fetch then transform).</p>
<h4 class=\"font-semibold text-gray-200 mb-2\">Example:</h4>
<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">CompletableFuture<Integer> f = CompletableFuture
    .supplyAsync(() -> 2)
    .thenCompose(x -> CompletableFuture.supplyAsync(() -> x * 3));
System.out.println(f.join()); // 6</pre></div>`
  }
];

