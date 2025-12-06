"""
Upgrade Spring Boot Core lessons - Batch 1
IDs: 173, 1012, 1013, 1014
Topics: Application Bootstrap, Actuator, Metrics, Health Indicators
"""
import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

upgrades = {
    173: """// Spring Boot: Application Bootstrap and Auto-configuration
// In production: Add spring-boot-starter-web dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.lang.annotation.*;

// Simulated Spring Boot annotations
@interface SpringBootApplication {}
@interface RestController {}
@interface GetMapping { String value() default ""; }
@interface PostMapping { String value() default ""; }
@interface RequestBody {}
@interface PathVariable { String value() default ""; }
@interface RequestParam { String value() default ""; boolean required() default true; }

// Simulated Spring application context
class SpringApplication {
    public static void run(Class<?> mainClass, String[] args) {
        System.out.println("[Spring Boot] Starting application: " + mainClass.getSimpleName());
        System.out.println("[Spring Boot] Scanning for components...");
        System.out.println("[Spring Boot] Auto-configuration enabled");
        System.out.println("[Spring Boot] Embedded Tomcat started on port 8080");
        System.out.println("[Spring Boot] Application ready!");
    }
}

// User entity
class User {
    protected Long id;
    protected String username;
    protected String email;
    protected String role;

    public User() {}

    public User(Long id, String username, String email, String role) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.role = role;
    }

    public Long getId() { return id; }
    public String getUsername() { return username; }
    public String getEmail() { return email; }
    public String getRole() { return role; }
}

// Main Spring Boot application
@SpringBootApplication
@RestController
public class Main {
    // Simulated in-memory database
    private Map<Long, User> users = new HashMap<>();
    private long idCounter = 1;

    public Main() {
        // Initialize with sample data
        users.put(1L, new User(1L, "alice", "alice@example.com", "ADMIN"));
        users.put(2L, new User(2L, "bob", "bob@example.com", "USER"));
        users.put(3L, new User(3L, "charlie", "charlie@example.com", "USER"));
        idCounter = 4;
    }

    // GET /
    @GetMapping("/")
    public Map<String, Object> home() {
        Map<String, Object> response = new HashMap<>();
        response.put("message", "Welcome to Spring Boot API");
        response.put("version", "1.0.0");
        response.put("status", "running");
        response.put("endpoints", Arrays.asList("/", "/users", "/users/{id}"));
        System.out.println("   [GET /] Home endpoint accessed");
        return response;
    }

    // GET /users
    @GetMapping("/users")
    public List<User> getUsers() {
        System.out.println("   [GET /users] Fetching all users");
        return new ArrayList<>(users.values());
    }

    // GET /users/{id}
    @GetMapping("/users/{id}")
    public Map<String, Object> getUserById(@PathVariable("id") Long id) {
        System.out.println("   [GET /users/" + id + "] Fetching user by ID");
        User user = users.get(id);

        Map<String, Object> response = new HashMap<>();
        if (user != null) {
            response.put("success", true);
            response.put("user", user);
        } else {
            response.put("success", false);
            response.put("error", "User not found");
        }
        return response;
    }

    // POST /users
    @PostMapping("/users")
    public Map<String, Object> createUser(@RequestBody Map<String, String> userData) {
        System.out.println("   [POST /users] Creating new user");

        String username = userData.get("username");
        String email = userData.get("email");
        String role = userData.getOrDefault("role", "USER");

        User newUser = new User(idCounter++, username, email, role);
        users.put(newUser.getId(), newUser);

        Map<String, Object> response = new HashMap<>();
        response.put("success", true);
        response.put("user", newUser);
        response.put("message", "User created successfully");
        return response;
    }

    // Simulated HTTP requests for demonstration
    public static void main(String[] args) {
        // Start Spring Boot application
        SpringApplication.run(Main.class, args);

        System.out.println("\\n=== Spring Boot Application Demo ===\\n");

        // Create application instance
        Main app = new Main();

        // Simulate HTTP requests
        System.out.println("1. GET / (Home endpoint):");
        Map<String, Object> homeResponse = app.home();
        System.out.println("   Response: " + homeResponse.get("message"));
        System.out.println("   Available endpoints: " + homeResponse.get("endpoints"));

        System.out.println("\\n2. GET /users (List all users):");
        List<User> allUsers = app.getUsers();
        System.out.println("   Found " + allUsers.size() + " users:");
        for (User user : allUsers) {
            System.out.println("     - " + user.getUsername() + " (" + user.getRole() + ")");
        }

        System.out.println("\\n3. GET /users/1 (Get user by ID):");
        Map<String, Object> userResponse = app.getUserById(1L);
        System.out.println("   Success: " + userResponse.get("success"));
        if (userResponse.get("user") != null) {
            User user = (User) userResponse.get("user");
            System.out.println("   User: " + user.getUsername() + " - " + user.getEmail());
        }

        System.out.println("\\n4. POST /users (Create new user):");
        Map<String, String> newUserData = new HashMap<>();
        newUserData.put("username", "david");
        newUserData.put("email", "david@example.com");
        newUserData.put("role", "MODERATOR");

        Map<String, Object> createResponse = app.createUser(newUserData);
        System.out.println("   " + createResponse.get("message"));
        User createdUser = (User) createResponse.get("user");
        System.out.println("   Created user ID: " + createdUser.getId());

        System.out.println("\\n5. GET /users (Verify new user):");
        List<User> updatedUsers = app.getUsers();
        System.out.println("   Total users now: " + updatedUsers.size());

        System.out.println("\\nSpring Boot application demonstrates:");
        System.out.println("  - @SpringBootApplication (auto-configuration)");
        System.out.println("  - @RestController (REST API endpoints)");
        System.out.println("  - @GetMapping / @PostMapping (HTTP method mapping)");
        System.out.println("  - @PathVariable / @RequestBody (request parameters)");
        System.out.println("  - JSON response serialization");
        System.out.println("\\nIn production: Spring Boot auto-configures Tomcat, Jackson, etc.");
    }
}
""",

    1012: """// Spring Boot: Actuator Endpoints
// In production: Add spring-boot-starter-actuator dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.time.*;
import java.lang.management.*;

// Simulated Spring Boot Actuator annotations
@interface Endpoint { String id(); }
@interface ReadOperation {}
@interface WriteOperation {}
@interface DeleteOperation {}

// Health status enum
enum HealthStatus {
    UP, DOWN, OUT_OF_SERVICE, UNKNOWN
}

// Health indicator interface
interface HealthIndicator {
    Health health();
}

// Health response class
class Health {
    private HealthStatus status;
    private Map<String, Object> details;

    private Health(HealthStatus status, Map<String, Object> details) {
        this.status = status;
        this.details = details;
    }

    public static Health up() {
        return new Health(HealthStatus.UP, new HashMap<>());
    }

    public static Health down() {
        return new Health(HealthStatus.DOWN, new HashMap<>());
    }

    public Health withDetail(String key, Object value) {
        details.put(key, value);
        return this;
    }

    public HealthStatus getStatus() { return status; }
    public Map<String, Object> getDetails() { return details; }
}

// Database health indicator
class DatabaseHealthIndicator implements HealthIndicator {
    private boolean isConnected = true;

    public Health health() {
        if (isConnected) {
            return Health.up()
                .withDetail("database", "PostgreSQL")
                .withDetail("validationQuery", "SELECT 1")
                .withDetail("responseTime", "5ms");
        } else {
            return Health.down()
                .withDetail("error", "Connection refused");
        }
    }

    public void disconnect() {
        isConnected = false;
    }
}

// Disk space health indicator
class DiskSpaceHealthIndicator implements HealthIndicator {
    public Health health() {
        long totalSpace = 500_000_000_000L; // 500GB
        long usableSpace = 100_000_000_000L; // 100GB
        long threshold = 10_000_000_000L; // 10GB

        if (usableSpace > threshold) {
            return Health.up()
                .withDetail("total", totalSpace / (1024*1024*1024) + "GB")
                .withDetail("free", usableSpace / (1024*1024*1024) + "GB")
                .withDetail("threshold", threshold / (1024*1024*1024) + "GB");
        } else {
            return Health.down()
                .withDetail("error", "Low disk space");
        }
    }
}

// Info endpoint
@Endpoint(id = "info")
class InfoEndpoint {
    @ReadOperation
    public Map<String, Object> info() {
        Map<String, Object> info = new HashMap<>();
        info.put("app", Map.of(
            "name", "Spring Boot App",
            "version", "1.0.0",
            "description", "Sample application"
        ));
        info.put("java", Map.of(
            "version", System.getProperty("java.version"),
            "vendor", System.getProperty("java.vendor")
        ));
        return info;
    }
}

// Metrics endpoint
@Endpoint(id = "metrics")
class MetricsEndpoint {
    private Map<String, Double> metrics = new HashMap<>();

    public MetricsEndpoint() {
        metrics.put("jvm.memory.used", 256.0);
        metrics.put("jvm.memory.max", 512.0);
        metrics.put("http.server.requests.count", 1234.0);
        metrics.put("system.cpu.usage", 0.45);
    }

    @ReadOperation
    public Map<String, Object> listMetrics() {
        Map<String, Object> response = new HashMap<>();
        response.put("names", metrics.keySet());
        return response;
    }

    @ReadOperation
    public Map<String, Object> getMetric(String metricName) {
        Map<String, Object> response = new HashMap<>();
        if (metrics.containsKey(metricName)) {
            response.put("name", metricName);
            response.put("measurement", List.of(Map.of(
                "value", metrics.get(metricName),
                "statistic", "VALUE"
            )));
        }
        return response;
    }
}

// Environment endpoint
@Endpoint(id = "env")
class EnvironmentEndpoint {
    @ReadOperation
    public Map<String, Object> environment() {
        Map<String, Object> env = new HashMap<>();
        env.put("activeProfiles", Arrays.asList("dev"));
        env.put("propertySources", Arrays.asList(
            Map.of("name", "systemProperties"),
            Map.of("name", "systemEnvironment"),
            Map.of("name", "applicationConfig")
        ));
        return env;
    }
}

// Health endpoint
@Endpoint(id = "health")
class HealthEndpoint {
    private List<HealthIndicator> healthIndicators = new ArrayList<>();

    public void addHealthIndicator(HealthIndicator indicator) {
        healthIndicators.add(indicator);
    }

    @ReadOperation
    public Map<String, Object> health() {
        Map<String, Object> healthResponse = new HashMap<>();
        Map<String, Object> components = new HashMap<>();

        boolean allUp = true;
        for (HealthIndicator indicator : healthIndicators) {
            Health health = indicator.health();
            String componentName = indicator.getClass().getSimpleName();
            componentName = componentName.replace("HealthIndicator", "").toLowerCase();

            components.put(componentName, Map.of(
                "status", health.getStatus().toString(),
                "details", health.getDetails()
            ));

            if (health.getStatus() != HealthStatus.UP) {
                allUp = false;
            }
        }

        healthResponse.put("status", allUp ? "UP" : "DOWN");
        healthResponse.put("components", components);
        return healthResponse;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot Actuator Endpoints ===\\n");

        // Health endpoint
        System.out.println("1. /actuator/health endpoint:");
        HealthEndpoint healthEndpoint = new HealthEndpoint();
        healthEndpoint.addHealthIndicator(new DatabaseHealthIndicator());
        healthEndpoint.addHealthIndicator(new DiskSpaceHealthIndicator());

        Map<String, Object> health = healthEndpoint.health();
        System.out.println("   Overall status: " + health.get("status"));
        Map<String, Object> components = (Map<String, Object>) health.get("components");
        for (String component : components.keySet()) {
            Map<String, Object> details = (Map<String, Object>) components.get(component);
            System.out.println("   - " + component + ": " + details.get("status"));
        }

        // Info endpoint
        System.out.println("\\n2. /actuator/info endpoint:");
        InfoEndpoint infoEndpoint = new InfoEndpoint();
        Map<String, Object> info = infoEndpoint.info();
        Map<String, Object> appInfo = (Map<String, Object>) info.get("app");
        System.out.println("   App: " + appInfo.get("name") + " v" + appInfo.get("version"));
        Map<String, Object> javaInfo = (Map<String, Object>) info.get("java");
        System.out.println("   Java: " + javaInfo.get("version"));

        // Metrics endpoint
        System.out.println("\\n3. /actuator/metrics endpoint:");
        MetricsEndpoint metricsEndpoint = new MetricsEndpoint();
        Map<String, Object> metricsList = metricsEndpoint.listMetrics();
        System.out.println("   Available metrics: " + ((Set) metricsList.get("names")).size());

        System.out.println("\\n4. /actuator/metrics/jvm.memory.used:");
        Map<String, Object> memoryMetric = metricsEndpoint.getMetric("jvm.memory.used");
        System.out.println("   Metric: " + memoryMetric.get("name"));
        List<Map<String, Object>> measurements = (List<Map<String, Object>>) memoryMetric.get("measurement");
        if (!measurements.isEmpty()) {
            System.out.println("   Value: " + measurements.get(0).get("value") + "MB");
        }

        // Environment endpoint
        System.out.println("\\n5. /actuator/env endpoint:");
        EnvironmentEndpoint envEndpoint = new EnvironmentEndpoint();
        Map<String, Object> environment = envEndpoint.environment();
        System.out.println("   Active profiles: " + environment.get("activeProfiles"));

        System.out.println("\\nSpring Boot Actuator provides:");
        System.out.println("  - /health - Application health status");
        System.out.println("  - /info - Application information");
        System.out.println("  - /metrics - Performance metrics");
        System.out.println("  - /env - Environment properties");
        System.out.println("  - /loggers - Logging configuration");
        System.out.println("  - /threaddump - Thread information");
        System.out.println("\\nIn production: Enable/disable endpoints via application.properties");
    }
}
""",

    1013: """// Spring Boot: Custom Metrics with Micrometer
// In production: Add spring-boot-starter-actuator and micrometer dependencies
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.util.concurrent.*;
import java.time.*;

// Simulated Micrometer annotations and classes
@interface Timed { String value(); }
@interface Counted { String value(); }

// Meter registry interface
interface MeterRegistry {
    Counter counter(String name, String... tags);
    Timer timer(String name, String... tags);
    Gauge gauge(String name, Object obj, java.util.function.ToDoubleFunction<?> valueFunction);
}

// Counter interface
interface Counter {
    void increment();
    void increment(double amount);
    double count();
}

// Timer interface
interface Timer {
    void record(Runnable task);
    Sample start();
    long count();
    double totalTime();
}

// Timer sample
interface Sample {
    long stop(Timer timer);
}

// Gauge (functional interface for value supplier)
interface Gauge {
    double value();
}

// Simple meter registry implementation
class SimpleMeterRegistry implements MeterRegistry {
    private Map<String, SimpleCounter> counters = new HashMap<>();
    private Map<String, SimpleTimer> timers = new HashMap<>();
    private Map<String, SimpleGauge> gauges = new HashMap<>();

    public Counter counter(String name, String... tags) {
        String key = name + Arrays.toString(tags);
        counters.putIfAbsent(key, new SimpleCounter(name));
        return counters.get(key);
    }

    public Timer timer(String name, String... tags) {
        String key = name + Arrays.toString(tags);
        timers.putIfAbsent(key, new SimpleTimer(name));
        return timers.get(key);
    }

    public Gauge gauge(String name, Object obj, java.util.function.ToDoubleFunction valueFunction) {
        SimpleGauge gauge = new SimpleGauge(name, () -> valueFunction.applyAsDouble(obj));
        gauges.put(name, gauge);
        return gauge;
    }

    public void printMetrics() {
        System.out.println("\\n=== Current Metrics ===");

        System.out.println("\\nCounters:");
        for (SimpleCounter counter : counters.values()) {
            System.out.println("  " + counter.getName() + ": " + counter.count());
        }

        System.out.println("\\nTimers:");
        for (SimpleTimer timer : timers.values()) {
            System.out.println("  " + timer.getName() + ":");
            System.out.println("    Count: " + timer.count());
            System.out.println("    Total time: " + timer.totalTime() + "ms");
            if (timer.count() > 0) {
                System.out.println("    Avg time: " + (timer.totalTime() / timer.count()) + "ms");
            }
        }

        System.out.println("\\nGauges:");
        for (SimpleGauge gauge : gauges.values()) {
            System.out.println("  " + gauge.getName() + ": " + gauge.value());
        }
    }

    // Inner classes for metric implementations
    static class SimpleCounter implements Counter {
        private String name;
        private double value = 0;

        SimpleCounter(String name) { this.name = name; }
        public void increment() { value++; }
        public void increment(double amount) { value += amount; }
        public double count() { return value; }
        public String getName() { return name; }
    }

    static class SimpleTimer implements Timer {
        private String name;
        private long totalTimeMs = 0;
        private long executionCount = 0;

        SimpleTimer(String name) { this.name = name; }

        public void record(Runnable task) {
            long start = System.currentTimeMillis();
            task.run();
            long duration = System.currentTimeMillis() - start;
            totalTimeMs += duration;
            executionCount++;
        }

        public Sample start() {
            long startTime = System.currentTimeMillis();
            return (timer) -> {
                long duration = System.currentTimeMillis() - startTime;
                ((SimpleTimer)timer).totalTimeMs += duration;
                ((SimpleTimer)timer).executionCount++;
                return duration;
            };
        }

        public long count() { return executionCount; }
        public double totalTime() { return totalTimeMs; }
        public String getName() { return name; }
    }

    static class SimpleGauge implements Gauge {
        private String name;
        private java.util.function.Supplier<Double> valueSupplier;

        SimpleGauge(String name, java.util.function.Supplier<Double> supplier) {
            this.name = name;
            this.valueSupplier = supplier;
        }

        public double value() { return valueSupplier.get(); }
        public String getName() { return name; }
    }
}

// Service with custom metrics
class OrderService {
    private MeterRegistry meterRegistry;
    private Counter ordersCreated;
    private Counter ordersFailed;
    private Timer orderProcessingTime;
    private List<String> activeOrders = new ArrayList<>();

    public OrderService(MeterRegistry registry) {
        this.meterRegistry = registry;

        // Create custom metrics
        this.ordersCreated = registry.counter("orders.created", "type", "online");
        this.ordersFailed = registry.counter("orders.failed", "type", "online");
        this.orderProcessingTime = registry.timer("orders.processing.time");

        // Gauge for active orders
        registry.gauge("orders.active", activeOrders, List::size);
    }

    @Counted("orders.created")
    @Timed("orders.processing.time")
    public String createOrder(String orderId, double amount) {
        Sample sample = orderProcessingTime.start();

        try {
            // Simulate order processing
            activeOrders.add(orderId);
            Thread.sleep(100); // Simulate processing time

            if (amount > 10000) {
                // Simulate failure for large orders
                ordersFailed.increment();
                activeOrders.remove(orderId);
                return "FAILED";
            }

            ordersCreated.increment();
            System.out.println("   [METRIC] Order created: " + orderId);
            return "SUCCESS";

        } catch (InterruptedException e) {
            ordersFailed.increment();
            activeOrders.remove(orderId);
            return "ERROR";
        } finally {
            sample.stop(orderProcessingTime);
        }
    }

    public void completeOrder(String orderId) {
        activeOrders.remove(orderId);
        System.out.println("   [METRIC] Order completed: " + orderId);
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Spring Boot: Custom Metrics with Micrometer ===\\n");

        // Create meter registry
        SimpleMeterRegistry registry = new SimpleMeterRegistry();

        // Create service with metrics
        OrderService orderService = new OrderService(registry);

        System.out.println("1. Processing orders with metrics:");

        // Create successful orders
        for (int i = 1; i <= 5; i++) {
            String result = orderService.createOrder("ORD-" + i, 100.0 * i);
            System.out.println("   Order " + i + ": " + result);
        }

        // Try to create a large order (will fail)
        String largeOrderResult = orderService.createOrder("ORD-LARGE", 15000.0);
        System.out.println("   Large order: " + largeOrderResult);

        // Complete some orders
        orderService.completeOrder("ORD-1");
        orderService.completeOrder("ORD-2");

        // Print all metrics
        registry.printMetrics();

        System.out.println("\\nMetric Types:");
        System.out.println("  - Counter: Monotonically increasing value (orders created, requests)");
        System.out.println("  - Timer: Measures duration and count (processing time)");
        System.out.println("  - Gauge: Current value that can go up or down (active orders, memory)");
        System.out.println("  - Distribution Summary: Statistical distribution (request sizes)");

        System.out.println("\\nIn production:");
        System.out.println("  - Metrics exported to Prometheus, Graphite, DataDog, etc.");
        System.out.println("  - Use @Timed and @Counted annotations");
        System.out.println("  - Monitor via /actuator/metrics endpoint");
        System.out.println("  - Create dashboards in Grafana");
    }
}
""",

    1014: """// Spring Boot: Custom Health Indicators
// In production: Add spring-boot-starter-actuator dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.time.*;

// Simulated Spring Boot health annotations
@interface Component {}

// Health status enum
enum HealthStatus {
    UP, DOWN, OUT_OF_SERVICE, UNKNOWN
}

// Health interface
interface Health {
    HealthStatus getStatus();
    Map<String, Object> getDetails();
}

// Health builder
class HealthBuilder {
    private HealthStatus status;
    private Map<String, Object> details = new HashMap<>();

    public static HealthBuilder status(HealthStatus status) {
        HealthBuilder builder = new HealthBuilder();
        builder.status = status;
        return builder;
    }

    public static HealthBuilder up() {
        return status(HealthStatus.UP);
    }

    public static HealthBuilder down() {
        return status(HealthStatus.DOWN);
    }

    public static HealthBuilder outOfService() {
        return status(HealthStatus.OUT_OF_SERVICE);
    }

    public static HealthBuilder unknown() {
        return status(HealthStatus.UNKNOWN);
    }

    public HealthBuilder withDetail(String key, Object value) {
        details.put(key, value);
        return this;
    }

    public HealthBuilder withDetails(Map<String, Object> details) {
        this.details.putAll(details);
        return this;
    }

    public Health build() {
        return new SimpleHealth(status, details);
    }

    private static class SimpleHealth implements Health {
        private HealthStatus status;
        private Map<String, Object> details;

        SimpleHealth(HealthStatus status, Map<String, Object> details) {
            this.status = status;
            this.details = details;
        }

        public HealthStatus getStatus() { return status; }
        public Map<String, Object> getDetails() { return new HashMap<>(details); }
    }
}

// Base health indicator interface
interface HealthIndicator {
    Health health();
}

// Database health indicator
@Component
class DatabaseHealthIndicator implements HealthIndicator {
    private boolean connected = true;
    private long queryTime = 5;

    public Health health() {
        try {
            // Simulate database check
            if (!connected) {
                return HealthBuilder.down()
                    .withDetail("error", "Connection refused")
                    .withDetail("database", "PostgreSQL")
                    .build();
            }

            // Check query performance
            if (queryTime > 1000) {
                return HealthBuilder.outOfService()
                    .withDetail("warning", "Slow query performance")
                    .withDetail("queryTime", queryTime + "ms")
                    .build();
            }

            return HealthBuilder.up()
                .withDetail("database", "PostgreSQL")
                .withDetail("validationQuery", "SELECT 1")
                .withDetail("responseTime", queryTime + "ms")
                .withDetail("maxConnections", 100)
                .withDetail("activeConnections", 15)
                .build();

        } catch (Exception e) {
            return HealthBuilder.down()
                .withDetail("error", e.getMessage())
                .build();
        }
    }

    public void disconnect() {
        connected = false;
    }

    public void slowDown() {
        queryTime = 1500;
    }
}

// External API health indicator
@Component
class ExternalApiHealthIndicator implements HealthIndicator {
    private String apiUrl = "https://api.example.com";
    private boolean available = true;

    public Health health() {
        try {
            // Simulate API call
            if (!available) {
                return HealthBuilder.down()
                    .withDetail("endpoint", apiUrl)
                    .withDetail("error", "API unavailable")
                    .build();
            }

            return HealthBuilder.up()
                .withDetail("endpoint", apiUrl)
                .withDetail("status", "reachable")
                .withDetail("responseTime", "120ms")
                .build();

        } catch (Exception e) {
            return HealthBuilder.down()
                .withDetail("error", e.getMessage())
                .build();
        }
    }

    public void makeUnavailable() {
        available = false;
    }
}

// Disk space health indicator
@Component
class DiskSpaceHealthIndicator implements HealthIndicator {
    private long totalSpace = 500_000_000_000L; // 500GB
    private long freeSpace = 100_000_000_000L; // 100GB
    private long threshold = 10_000_000_000L; // 10GB

    public Health health() {
        if (freeSpace < threshold) {
            return HealthBuilder.down()
                .withDetail("total", formatBytes(totalSpace))
                .withDetail("free", formatBytes(freeSpace))
                .withDetail("threshold", formatBytes(threshold))
                .withDetail("error", "Disk space below threshold")
                .build();
        }

        return HealthBuilder.up()
            .withDetail("total", formatBytes(totalSpace))
            .withDetail("free", formatBytes(freeSpace))
            .withDetail("threshold", formatBytes(threshold))
            .build();
    }

    private String formatBytes(long bytes) {
        return (bytes / (1024 * 1024 * 1024)) + "GB";
    }

    public void fillDisk() {
        freeSpace = 5_000_000_000L; // 5GB
    }
}

// Custom business logic health indicator
@Component
class BusinessHealthIndicator implements HealthIndicator {
    private int pendingOrders = 50;
    private int failedProcesses = 2;

    public Health health() {
        Map<String, Object> details = new HashMap<>();
        details.put("pendingOrders", pendingOrders);
        details.put("failedProcesses", failedProcesses);
        details.put("lastCheck", Instant.now().toString());

        // Business rule: fail if too many failed processes
        if (failedProcesses > 10) {
            return HealthBuilder.down()
                .withDetails(details)
                .withDetail("error", "Too many failed processes")
                .build();
        }

        // Warning if too many pending orders
        if (pendingOrders > 1000) {
            return HealthBuilder.outOfService()
                .withDetails(details)
                .withDetail("warning", "High pending order count")
                .build();
        }

        return HealthBuilder.up()
            .withDetails(details)
            .build();
    }

    public void addFailures(int count) {
        failedProcesses += count;
    }
}

// Health aggregator
class HealthAggregator {
    private List<HealthIndicator> indicators = new ArrayList<>();

    public void addIndicator(HealthIndicator indicator) {
        indicators.add(indicator);
    }

    public Map<String, Object> getAggregatedHealth() {
        Map<String, Object> result = new HashMap<>();
        Map<String, Map<String, Object>> components = new HashMap<>();

        HealthStatus overallStatus = HealthStatus.UP;

        for (HealthIndicator indicator : indicators) {
            Health health = indicator.health();
            String name = indicator.getClass().getSimpleName()
                .replace("HealthIndicator", "").toLowerCase();

            Map<String, Object> component = new HashMap<>();
            component.put("status", health.getStatus().toString());
            component.put("details", health.getDetails());

            components.put(name, component);

            // Aggregate status (DOWN takes precedence)
            if (health.getStatus() == HealthStatus.DOWN) {
                overallStatus = HealthStatus.DOWN;
            } else if (health.getStatus() == HealthStatus.OUT_OF_SERVICE &&
                      overallStatus == HealthStatus.UP) {
                overallStatus = HealthStatus.OUT_OF_SERVICE;
            }
        }

        result.put("status", overallStatus.toString());
        result.put("components", components);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Custom Health Indicators ===\\n");

        // Create health indicators
        DatabaseHealthIndicator dbHealth = new DatabaseHealthIndicator();
        ExternalApiHealthIndicator apiHealth = new ExternalApiHealthIndicator();
        DiskSpaceHealthIndicator diskHealth = new DiskSpaceHealthIndicator();
        BusinessHealthIndicator businessHealth = new BusinessHealthIndicator();

        // Create aggregator
        HealthAggregator aggregator = new HealthAggregator();
        aggregator.addIndicator(dbHealth);
        aggregator.addIndicator(apiHealth);
        aggregator.addIndicator(diskHealth);
        aggregator.addIndicator(businessHealth);

        // Check 1: All healthy
        System.out.println("1. Initial health check (all systems UP):");
        Map<String, Object> health1 = aggregator.getAggregatedHealth();
        printHealth(health1);

        // Check 2: Database goes down
        System.out.println("\\n2. Database connection lost:");
        dbHealth.disconnect();
        Map<String, Object> health2 = aggregator.getAggregatedHealth();
        printHealth(health2);

        // Check 3: External API unavailable
        System.out.println("\\n3. External API unavailable:");
        apiHealth.makeUnavailable();
        Map<String, Object> health3 = aggregator.getAggregatedHealth();
        printHealth(health3);

        System.out.println("\\nCustom Health Indicators:");
        System.out.println("  - Implement HealthIndicator interface");
        System.out.println("  - Return Health with status and details");
        System.out.println("  - Health statuses: UP, DOWN, OUT_OF_SERVICE, UNKNOWN");
        System.out.println("  - Add custom business logic checks");
        System.out.println("\\nIn production:");
        System.out.println("  - Access via /actuator/health endpoint");
        System.out.println("  - Configure management.endpoint.health.show-details=always");
        System.out.println("  - Use for load balancer health checks");
    }

    private static void printHealth(Map<String, Object> health) {
        System.out.println("   Overall Status: " + health.get("status"));
        Map<String, Map<String, Object>> components =
            (Map<String, Map<String, Object>>) health.get("components");

        for (String name : components.keySet()) {
            Map<String, Object> component = components.get(name);
            System.out.println("   - " + name + ": " + component.get("status"));
        }
    }
}
"""
}

print("=" * 80)
print("UPGRADING SPRING BOOT CORE - BATCH 1")
print("IDs: 173, 1012, 1013, 1014")
print("=" * 80)

results = []
for lesson_id, new_solution in upgrades.items():
    lesson = next((l for l in lessons if l.get('id') == lesson_id), None)
    if lesson:
        old_len = len(lesson.get('fullSolution', ''))
        lesson['fullSolution'] = new_solution
        new_len = len(new_solution)
        growth = new_len - old_len
        pct = (growth / old_len * 100) if old_len > 0 else 0
        results.append((lesson_id, lesson.get('title', ''), old_len, new_len, growth, pct))
        print(f"\nLesson {lesson_id}: {lesson.get('title', '')}")
        print(f"  {old_len:,} -> {new_len:,} chars (+{growth:,}, +{pct:.1f}%)")

with open(r'c:\devbootLLM-app\public\lessons-java.json', 'w', encoding='utf-8') as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print("\n" + "=" * 80)
print("BATCH 1 COMPLETE!")
print("=" * 80)
print(f"\nUpgraded {len(results)} Spring Boot Core lessons")

for lesson_id, title, old_len, new_len, growth, pct in results:
    print(f"  ID {lesson_id:4d}: {title[:50]:50s} | +{growth:5,} chars ({pct:5.1f}%)")
