export const lessons = [
  {
    "title": "VarHandle atomic counter",
    "language": "java",
    "description": "Use VarHandle to atomically initialize and increment a counter field, then print the final value.",
    "initialCode": "import java.lang.invoke.MethodHandles;\nimport java.lang.invoke.VarHandle;\n\npublic class Main {\n    static final class Metrics {\n        volatile int count;\n    }\n\n    public static void main(String[] args) throws Exception {\n        Metrics metrics = new Metrics();\n\n        // TODO: obtain a VarHandle for Metrics.count, set it to 10,\n        // atomically add 5 using getAndAdd, then print the current value.\n    }\n}\n",
    "fullSolution": "import java.lang.invoke.MethodHandles;\nimport java.lang.invoke.VarHandle;\n\npublic class Main {\n    static final class Metrics {\n        volatile int count;\n    }\n\n    public static void main(String[] args) throws Exception {\n        Metrics metrics = new Metrics();\n        VarHandle handle = MethodHandles.lookup().findVarHandle(Metrics.class, \"count\", int.class);\n        handle.set(metrics, 10);\n        handle.getAndAdd(metrics, 5);\n        System.out.println((int) handle.getVolatile(metrics));\n    }\n}\n",
    "expectedOutput": "15",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>VarHandle</code> offers lock-free access to fields and array elements. Locate the handle once, then use operations such as <code>getAndAdd</code> to perform atomic arithmetic.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">VarHandle h = MethodHandles.lookup().findVarHandle(Type.class, \"field\", int.class);\nh.getAndAdd(obj, 1);\nint value = (int) h.getVolatile(obj);</pre></div>\n<p class=\"mt-4 text-gray-300\">VarHandles reduce the need for <code>AtomicInteger</code> wrappers when you want field-level atomics.</p>",
    "tags": [
      "Advanced",
      "Concurrency",
      "JVM Internals"
    ]
  },
  {
    "title": "Flow publisher subscriber",
    "language": "java",
    "description": "Wire a SubmissionPublisher to a Flow.Subscriber, capture events, and print them in order.",
    "initialCode": "import java.util.concurrent.CountDownLatch;\nimport java.util.concurrent.Flow;\nimport java.util.concurrent.SubmissionPublisher;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        SubmissionPublisher<String> publisher = new SubmissionPublisher<>();\n        StringBuilder log = new StringBuilder();\n        CountDownLatch done = new CountDownLatch(1);\n\n        Flow.Subscriber<String> subscriber = new Flow.Subscriber<>() {\n            private Flow.Subscription subscription;\n\n            @Override\n            public void onSubscribe(Flow.Subscription subscription) {\n                this.subscription = subscription;\n                // TODO: request all items\n            }\n\n            @Override\n            public void onNext(String item) {\n                // TODO: append \"onNext: <item>\" followed by System.lineSeparator()\n                // then request the next item\n            }\n\n            @Override\n            public void onError(Throwable throwable) {\n                log.append(\"error: \").append(throwable.getMessage()).append(System.lineSeparator());\n                done.countDown();\n            }\n\n            @Override\n            public void onComplete() {\n                log.append(\"complete\").append(System.lineSeparator());\n                done.countDown();\n            }\n        };\n\n        // TODO: subscribe the subscriber, submit \"deploy\" then \"done\",\n        // close the publisher, wait for the latch, and finally print the log.\n    }\n}\n",
    "fullSolution": "import java.util.concurrent.CountDownLatch;\nimport java.util.concurrent.Flow;\nimport java.util.concurrent.SubmissionPublisher;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        SubmissionPublisher<String> publisher = new SubmissionPublisher<>();\n        StringBuilder log = new StringBuilder();\n        CountDownLatch done = new CountDownLatch(1);\n\n        Flow.Subscriber<String> subscriber = new Flow.Subscriber<>() {\n            private Flow.Subscription subscription;\n\n            @Override\n            public void onSubscribe(Flow.Subscription subscription) {\n                this.subscription = subscription;\n                subscription.request(1);\n            }\n\n            @Override\n            public void onNext(String item) {\n                log.append(\"onNext: \").append(item).append(System.lineSeparator());\n                subscription.request(1);\n            }\n\n            @Override\n            public void onError(Throwable throwable) {\n                log.append(\"error: \").append(throwable.getMessage()).append(System.lineSeparator());\n                done.countDown();\n            }\n\n            @Override\n            public void onComplete() {\n                log.append(\"complete\").append(System.lineSeparator());\n                done.countDown();\n            }\n        };\n\n        publisher.subscribe(subscriber);\n        publisher.submit(\"deploy\");\n        publisher.submit(\"done\");\n        publisher.close();\n\n        done.await();\n        System.out.print(log.toString());\n    }\n}\n",
    "expectedOutput": "onNext: deploy\nonNext: done\ncomplete",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>SubmissionPublisher</code> implements the Reactive Streams <code>Flow.Publisher</code> API. Request demand in <code>onSubscribe</code>, process events in <code>onNext</code>, and close resources in <code>onComplete</code>.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">publisher.subscribe(subscriber);\npublisher.submit(data);\npublisher.close();\nlatched.await();</pre></div>\n<p class=\"mt-4 text-gray-300\">Latch the completion signal to keep the JVM alive until the asynchronous publisher finishes delivering items.</p>",
    "tags": [
      "Advanced",
      "Concurrency",
      "Reactive"
    ]
  },
  {
    "title": "Cleaner resource finalizer",
    "language": "java",
    "description": "Register a resource with java.lang.ref.Cleaner so closing it triggers deterministic cleanup output.",
    "initialCode": "import java.lang.ref.Cleaner;\n\npublic class Main {\n    static final Cleaner CLEANER = Cleaner.create();\n\n    static final class TrackedResource implements AutoCloseable {\n        private final Cleaner.Cleanable cleanable;\n        private boolean closed;\n\n        TrackedResource(String name) {\n            // TODO: register a cleanup action that prints \"cleanup \" + name\n            this.cleanable = null;\n        }\n\n        @Override\n        public void close() {\n            if (closed) {\n                return;\n            }\n            closed = true;\n            System.out.println(\"closing resource\");\n            // TODO: trigger the cleanup immediately\n        }\n    }\n\n    public static void main(String[] args) {\n        try (TrackedResource resource = new TrackedResource(\"cache\")) {\n            System.out.println(\"work\");\n        }\n    }\n}\n",
    "fullSolution": "import java.lang.ref.Cleaner;\n\npublic class Main {\n    static final Cleaner CLEANER = Cleaner.create();\n\n    static final class TrackedResource implements AutoCloseable {\n        private final Cleaner.Cleanable cleanable;\n        private boolean closed;\n\n        TrackedResource(String name) {\n            this.cleanable = CLEANER.register(this, () -> System.out.println(\"cleanup \" + name));\n        }\n\n        @Override\n        public void close() {\n            if (closed) {\n                return;\n            }\n            closed = true;\n            System.out.println(\"closing resource\");\n            cleanable.clean();\n        }\n    }\n\n    public static void main(String[] args) {\n        try (TrackedResource resource = new TrackedResource(\"cache\")) {\n            System.out.println(\"work\");\n        }\n    }\n}\n",
    "expectedOutput": "work\nclosing resource\ncleanup cache",
    "tutorial": "<p class=\"mb-4 text-gray-300\">Use <code>Cleaner</code> to register cleanup tasks that run when a resource is closed or garbage collected. Calling <code>clean()</code> executes the action immediately and deregisters it.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">Cleaner cleaner = Cleaner.create();\nCleaner.Cleanable cleanable = cleaner.register(obj, () -> release());\ncleanable.clean();</pre></div>\n<p class=\"mt-4 text-gray-300\">Pair <code>Cleaner</code> with try-with-resources so cleanup runs deterministically, while still safeguarding against leaked handles.</p>",
    "tags": [
      "Advanced",
      "Lifecycle",
      "Resources"
    ]
  },
  {
    "title": "LinkedTransferQueue handoff",
    "language": "java",
    "description": "Coordinate a producer and consumer with LinkedTransferQueue.transfer and print the received items.",
    "initialCode": "import java.util.concurrent.LinkedTransferQueue;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        LinkedTransferQueue<String> queue = new LinkedTransferQueue<>();\n\n        // TODO: start a producer thread that transfers \"alpha\" then \"beta\".\n        // Start a consumer thread that takes two items and prints each.\n        // Join both threads at the end.\n    }\n}\n",
    "fullSolution": "import java.util.concurrent.LinkedTransferQueue;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        LinkedTransferQueue<String> queue = new LinkedTransferQueue<>();\n\n        Thread producer = new Thread(() -> {\n            try {\n                queue.transfer(\"alpha\");\n                queue.transfer(\"beta\");\n            } catch (InterruptedException e) {\n                Thread.currentThread().interrupt();\n            }\n        });\n\n        Thread consumer = new Thread(() -> {\n            try {\n                System.out.println(queue.take());\n                System.out.println(queue.take());\n            } catch (InterruptedException e) {\n                Thread.currentThread().interrupt();\n            }\n        });\n\n        producer.start();\n        consumer.start();\n        producer.join();\n        consumer.join();\n    }\n}\n",
    "expectedOutput": "alpha\nbeta",
    "tutorial": "<p class=\"mb-4 text-gray-300\"><code>LinkedTransferQueue</code> combines the best of queues and synchronous handoff channels. <code>transfer</code> blocks until a consumer receives the element, making it ideal for throttled pipelines.</p>\n<h4 class=\"font-semibold text-gray-200 mb-2\">Pattern:</h4>\n<div class=\"code-block-wrapper\"><pre class=\"tutorial-code-block\">queue.transfer(task);\nString item = queue.take();</pre></div>\n<p class=\"mt-4 text-gray-300\">Because <code>transfer</code> waits for a taker, producers and consumers stay in lock-step without extra signaling.</p>",
    "tags": [
      "Advanced",
      "Concurrency",
      "Queues"
    ]
  }
];
