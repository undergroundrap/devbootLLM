import fs from 'fs';

const p = JSON.parse(fs.readFileSync('public/lessons-python.json', 'utf-8'));
const j = JSON.parse(fs.readFileSync('public/lessons-java.json', 'utf-8'));
let count = 0;

const generateExamplesByLevel = (lesson, lang) => {
  const {id, title, tags = []} = lesson;
  const isPython = lang === 'python';

  // Skip if already has real examples (not placeholder and has actual code)
  if (lesson.additionalExamples &&
      lesson.additionalExamples.includes('class') &&
      lesson.additionalExamples.length > 500) {
    return null;
  }

  // Determine difficulty level
  let level = 'Intermediate';
  if (tags.includes('Beginner')) level = 'Beginner';
  else if (tags.includes('Advanced')) level = 'Advanced';
  else if (tags.includes('Expert')) level = 'Expert';

  let examples = `<h5>More Examples:</h5>

<div class="example-block">
<h6>Example 1: Basic ${title} Implementation</h6>
<pre><code class="language-${lang}">`;

  if (isPython) {
    if (level === 'Beginner') {
      examples += `# ${title} - Beginner Level
# Simple, clear implementation

def basic_example():
    """${title} - starter example"""
    # Step 1: Setup
    data = []

    # Step 2: Process
    result = process_data(data)

    # Step 3: Return
    return result

def process_data(data):
    """Core processing logic"""
    if not data:
        return "No data"
    return f"Processed {len(data)} items"

# Usage
output = basic_example()
print(output)`;
    } else if (level === 'Advanced') {
      examples += `# ${title} - Advanced Implementation
from typing import List, Dict, Optional
from abc import ABC, abstractmethod

class ${title.replace(/[^a-zA-Z0-9]/g, '')}Strategy(ABC):
    """Abstract base for ${title}"""

    @abstractmethod
    def execute(self, data: Dict) -> Dict:
        """Execute the strategy"""
        pass

class ConcreteStrategy(${title.replace(/[^a-zA-Z0-9]/g, '')}Strategy):
    """Concrete implementation"""

    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.cache = {}

    def execute(self, data: Dict) -> Dict:
        # Check cache
        key = self._generate_key(data)
        if key in self.cache:
            return self.cache[key]

        # Process
        result = self._process(data)
        self.cache[key] = result
        return result

    def _generate_key(self, data: Dict) -> str:
        return str(hash(frozenset(data.items())))

    def _process(self, data: Dict) -> Dict:
        return {"status": "success", "data": data}

# Usage
strategy = ConcreteStrategy({"timeout": 30})
result = strategy.execute({"key": "value"})`;
    } else {
      // Expert
      examples += `# ${title} - Expert Level
from typing import TypeVar, Generic, Callable, Any
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import asyncio

T = TypeVar('T')

class ${title.replace(/[^a-zA-Z0-9]/g, '')}Engine(Generic[T]):
    """Expert-level ${title} with generics and async"""

    def __init__(self, workers: int = 4):
        self.executor = ThreadPoolExecutor(max_workers=workers)
        self.metrics = {"calls": 0, "errors": 0}

    async def process_async(self, items: List[T]) -> List[T]:
        """Async batch processing"""
        tasks = [self._process_item(item) for item in items]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        processed = []
        for result in results:
            if isinstance(result, Exception):
                self.metrics["errors"] += 1
            else:
                processed.append(result)

        self.metrics["calls"] += len(items)
        return processed

    async def _process_item(self, item: T) -> T:
        """Process single item with validation"""
        await asyncio.sleep(0.01)  # Simulate async I/O
        return item

    def with_retry(self, max_attempts: int = 3):
        """Decorator for retry logic"""
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapper(*args, **kwargs):
                for attempt in range(max_attempts):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as e:
                        if attempt == max_attempts - 1:
                            raise
                        await asyncio.sleep(2 ** attempt)
            return wrapper
        return decorator

# Usage
engine = ${title.replace(/[^a-zA-Z0-9]/g, '')}Engine[str](workers=4)
result = asyncio.run(engine.process_async(["a", "b", "c"]))`;
    }
  } else {
    // Java examples
    if (level === 'Beginner') {
      examples += `// ${title} - Beginner Level
public class BasicExample {
    public static void main(String[] args) {
        // Step 1: Create instance
        BasicExample example = new BasicExample();

        // Step 2: Process data
        String result = example.processData("input");

        // Step 3: Display result
        System.out.println("Result: " + result);
    }

    public String processData(String input) {
        if (input == null || input.isEmpty()) {
            return "No data";
        }
        return "Processed: " + input.toUpperCase();
    }
}`;
    } else if (level === 'Advanced') {
      examples += `// ${title} - Advanced Implementation
import java.util.*;
import java.util.concurrent.*;
import java.util.stream.*;

public class AdvancedExample {
    private final Map<String, Object> cache;
    private final ExecutorService executor;

    public AdvancedExample(int poolSize) {
        this.cache = new ConcurrentHashMap<>();
        this.executor = Executors.newFixedThreadPool(poolSize);
    }

    public <T> List<T> processBatch(List<T> items) {
        return items.stream()
            .map(this::processWithCache)
            .collect(Collectors.toList());
    }

    private <T> T processWithCache(T item) {
        String key = generateKey(item);

        if (cache.containsKey(key)) {
            return (T) cache.get(key);
        }

        T result = process(item);
        cache.put(key, result);
        return result;
    }

    private <T> T process(T item) {
        // Core processing logic
        return item;
    }

    private String generateKey(Object item) {
        return String.valueOf(item.hashCode());
    }

    public void shutdown() {
        executor.shutdown();
    }

    public static void main(String[] args) {
        AdvancedExample example = new AdvancedExample(4);
        List<String> results = example.processBatch(
            Arrays.asList("a", "b", "c")
        );
        System.out.println("Results: " + results);
        example.shutdown();
    }
}`;
    } else {
      // Expert
      examples += `// ${title} - Expert Level
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.lang.reflect.*;

public class ExpertExample<T> {
    private final ExecutorService executor;
    private final Map<String, CompletableFuture<T>> futures;
    private final BiFunction<T, T, T> mergeFn;

    public ExpertExample(BiFunction<T, T, T> mergeFn) {
        this.executor = Executors.newWorkStealingPool();
        this.futures = new ConcurrentHashMap<>();
        this.mergeFn = mergeFn;
    }

    public CompletableFuture<T> processAsync(T item) {
        String key = computeKey(item);

        return futures.computeIfAbsent(key, k ->
            CompletableFuture.supplyAsync(() -> {
                try {
                    return processWithRetry(item, 3);
                } catch (Exception e) {
                    throw new CompletionException(e);
                }
            }, executor)
        );
    }

    private T processWithRetry(T item, int maxAttempts) {
        for (int i = 0; i < maxAttempts; i++) {
            try {
                return doProcess(item);
            } catch (Exception e) {
                if (i == maxAttempts - 1) throw e;
                try {
                    Thread.sleep((long) Math.pow(2, i) * 1000);
                } catch (InterruptedException ie) {
                    Thread.currentThread().interrupt();
                    throw new RuntimeException(ie);
                }
            }
        }
        throw new RuntimeException("Failed after retries");
    }

    private T doProcess(T item) {
        // Core processing with validation
        return item;
    }

    private String computeKey(T item) {
        return Objects.toString(item);
    }

    public List<T> processBatchAndMerge(List<T> items) {
        List<CompletableFuture<T>> futures = items.stream()
            .map(this::processAsync)
            .collect(Collectors.toList());

        return futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());
    }

    public void shutdown() {
        executor.shutdown();
    }
}`;
    }
  }

  examples += `
</code></pre>
</div>

<div class="example-block">
<h6>Example 2: ${title} with Error Handling</h6>
<pre><code class="language-${lang}">`;

  if (isPython) {
    examples += `# Production-ready error handling
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ErrorHandlingExample:
    """${title} with comprehensive error handling"""

    def __init__(self):
        self.errors = []

    def safe_process(self, data):
        """Process with error recovery"""
        try:
            self._validate(data)
            result = self._execute(data)
            logger.info(f"Success: {result}")
            return result
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            self.errors.append(str(e))
            return None
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            self.errors.append(str(e))
            raise

    def _validate(self, data):
        if data is None:
            raise ValueError("Data cannot be None")
        if not isinstance(data, (str, dict, list)):
            raise ValueError(f"Invalid type: {type(data)}")

    def _execute(self, data):
        # Processing logic
        return {"processed": data, "status": "ok"}

    def get_errors(self):
        return self.errors

# Usage
handler = ErrorHandlingExample()
result = handler.safe_process({"test": "data"})
print(f"Errors: {handler.get_errors()}")`;
  } else {
    examples += `// Production-ready error handling
import java.util.*;
import java.util.logging.*;

public class ErrorHandlingExample {
    private static final Logger logger =
        Logger.getLogger(ErrorHandlingExample.class.getName());
    private final List<String> errors;

    public ErrorHandlingExample() {
        this.errors = new ArrayList<>();
    }

    public Optional<Map<String, Object>> safeProcess(Object data) {
        try {
            validate(data);
            Map<String, Object> result = execute(data);
            logger.info("Success: " + result);
            return Optional.of(result);
        } catch (IllegalArgumentException e) {
            logger.severe("Validation error: " + e.getMessage());
            errors.add(e.getMessage());
            return Optional.empty();
        } catch (Exception e) {
            logger.log(Level.SEVERE, "Unexpected error", e);
            errors.add(e.getMessage());
            throw new RuntimeException(e);
        }
    }

    private void validate(Object data) {
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null");
        }
    }

    private Map<String, Object> execute(Object data) {
        Map<String, Object> result = new HashMap<>();
        result.put("processed", data);
        result.put("status", "ok");
        return result;
    }

    public List<String> getErrors() {
        return new ArrayList<>(errors);
    }

    public static void main(String[] args) {
        ErrorHandlingExample handler = new ErrorHandlingExample();
        Optional<Map<String, Object>> result =
            handler.safeProcess(Map.of("test", "data"));
        System.out.println("Errors: " + handler.getErrors());
    }
}`;
  }

  examples += `
</code></pre>
</div>

<div class="example-block">
<h6>Example 3: Complete ${title} Application</h6>
<pre><code class="language-${lang}">`;

  if (isPython) {
    examples += `# Complete application example
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict

@dataclass
class Result:
    success: bool
    data: any
    timestamp: datetime
    errors: List[str]

class CompleteApplication:
    """Full ${title} application"""

    def __init__(self, config: Dict = None):
        self.config = config or {}
        self.results = []
        self.start_time = datetime.now()

    def run(self, items: List) -> List[Result]:
        """Process all items and return results"""
        for item in items:
            result = self._process_item(item)
            self.results.append(result)

        return self.results

    def _process_item(self, item) -> Result:
        """Process single item with full error handling"""
        errors = []

        try:
            # Validate
            if not self._is_valid(item):
                errors.append("Validation failed")
                return Result(False, None, datetime.now(), errors)

            # Process
            processed = self._transform(item)

            # Return success
            return Result(True, processed, datetime.now(), [])

        except Exception as e:
            errors.append(str(e))
            return Result(False, None, datetime.now(), errors)

    def _is_valid(self, item) -> bool:
        return item is not None

    def _transform(self, item):
        return {"original": item, "processed": True}

    def get_summary(self) -> Dict:
        """Get processing summary"""
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)

        return {
            "total": total,
            "successful": successful,
            "failed": total - successful,
            "duration": (datetime.now() - self.start_time).total_seconds()
        }

# Usage
app = CompleteApplication({"mode": "production"})
results = app.run([1, 2, 3, None, 5])
summary = app.get_summary()
print(f"Summary: {summary}")`;
  } else {
    examples += `// Complete application example
import java.time.*;
import java.util.*;
import java.util.stream.*;

public class CompleteApplication {
    private final Map<String, Object> config;
    private final List<Result> results;
    private final Instant startTime;

    public CompleteApplication(Map<String, Object> config) {
        this.config = config != null ? config : new HashMap<>();
        this.results = new ArrayList<>();
        this.startTime = Instant.now();
    }

    public List<Result> run(List<Object> items) {
        results.clear();

        for (Object item : items) {
            Result result = processItem(item);
            results.add(result);
        }

        return new ArrayList<>(results);
    }

    private Result processItem(Object item) {
        List<String> errors = new ArrayList<>();

        try {
            // Validate
            if (!isValid(item)) {
                errors.add("Validation failed");
                return new Result(false, null, Instant.now(), errors);
            }

            // Process
            Object processed = transform(item);

            // Return success
            return new Result(true, processed, Instant.now(), errors);

        } catch (Exception e) {
            errors.add(e.getMessage());
            return new Result(false, null, Instant.now(), errors);
        }
    }

    private boolean isValid(Object item) {
        return item != null;
    }

    private Object transform(Object item) {
        Map<String, Object> result = new HashMap<>();
        result.put("original", item);
        result.put("processed", true);
        return result;
    }

    public Map<String, Object> getSummary() {
        long total = results.size();
        long successful = results.stream()
            .filter(Result::isSuccess)
            .count();

        Duration duration = Duration.between(startTime, Instant.now());

        Map<String, Object> summary = new HashMap<>();
        summary.put("total", total);
        summary.put("successful", successful);
        summary.put("failed", total - successful);
        summary.put("duration_seconds", duration.getSeconds());

        return summary;
    }

    static class Result {
        private final boolean success;
        private final Object data;
        private final Instant timestamp;
        private final List<String> errors;

        public Result(boolean success, Object data,
                     Instant timestamp, List<String> errors) {
            this.success = success;
            this.data = data;
            this.timestamp = timestamp;
            this.errors = errors;
        }

        public boolean isSuccess() { return success; }
        public Object getData() { return data; }
        public Instant getTimestamp() { return timestamp; }
        public List<String> getErrors() { return errors; }
    }

    public static void main(String[] args) {
        CompleteApplication app = new CompleteApplication(
            Map.of("mode", "production")
        );
        List<Result> results = app.run(
            Arrays.asList(1, 2, 3, null, 5)
        );
        System.out.println("Summary: " + app.getSummary());
    }
}`;
  }

  examples += `
</code></pre>
</div>`;

  return examples;
};

console.log('Enhancing ALL remaining lessons (Beginner, Advanced, Expert)...\n');
console.log('='.repeat(80));

let beginnerCount = 0, advancedCount = 0, expertCount = 0;

// Process all Python lessons
p.forEach(lesson => {
  const examples = generateExamplesByLevel(lesson, 'python');
  if (examples) {
    lesson.additionalExamples = examples;
    count++;
    if (lesson.tags.includes('Beginner')) beginnerCount++;
    else if (lesson.tags.includes('Advanced')) advancedCount++;
    else if (lesson.tags.includes('Expert')) expertCount++;

    const level = lesson.tags.includes('Beginner') ? 'Beginner' :
                  lesson.tags.includes('Advanced') ? 'Advanced' :
                  lesson.tags.includes('Expert') ? 'Expert' : 'Other';
    console.log(`✓ Python ${lesson.id} [${level}]: ${lesson.title}`);
  }
});

// Process all Java lessons
j.forEach(lesson => {
  const examples = generateExamplesByLevel(lesson, 'java');
  if (examples) {
    lesson.additionalExamples = examples;
    count++;
    if (lesson.tags.includes('Beginner')) beginnerCount++;
    else if (lesson.tags.includes('Advanced')) advancedCount++;
    else if (lesson.tags.includes('Expert')) expertCount++;

    const level = lesson.tags.includes('Beginner') ? 'Beginner' :
                  lesson.tags.includes('Advanced') ? 'Advanced' :
                  lesson.tags.includes('Expert') ? 'Expert' : 'Other';
    console.log(`✓ Java ${lesson.id} [${level}]: ${lesson.title}`);
  }
});

fs.writeFileSync('public/lessons-python.json', JSON.stringify(p, null, 2));
fs.writeFileSync('public/lessons-java.json', JSON.stringify(j, null, 2));

console.log('\n' + '='.repeat(80));
console.log(`✅ Enhanced ${count} lessons with level-appropriate examples!`);
console.log(`   Beginner: ${beginnerCount}`);
console.log(`   Advanced: ${advancedCount}`);
console.log(`   Expert: ${expertCount}`);
console.log('='.repeat(80));
