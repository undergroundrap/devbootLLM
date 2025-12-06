"""
Upgrade Spring Boot Core lessons - Batch 4 (FINAL)
IDs: 273, 846, 847, 848, 1010
Topics: Application Runner, Graceful Shutdown, Admin Server, Best Practices
"""
import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

upgrades = {
    273: """// Spring Boot: Application Runner and Command Line Runner
// In production: Add spring-boot dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;

// Simulated Spring Boot interfaces
@interface Component {}
@interface Order { int value(); }

// ApplicationRunner interface
interface ApplicationRunner {
    void run(ApplicationArguments args) throws Exception;
}

// CommandLineRunner interface
interface CommandLineRunner {
    void run(String... args) throws Exception;
}

// Application arguments wrapper
class ApplicationArguments {
    private String[] sourceArgs;
    private Map<String, List<String>> optionArgs = new HashMap<>();
    private List<String> nonOptionArgs = new ArrayList<>();

    public ApplicationArguments(String[] args) {
        this.sourceArgs = args;
        parseArgs(args);
    }

    private void parseArgs(String[] args) {
        for (String arg : args) {
            if (arg.startsWith("--")) {
                String[] parts = arg.substring(2).split("=", 2);
                String key = parts[0];
                String value = parts.length > 1 ? parts[1] : "";

                optionArgs.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
            } else {
                nonOptionArgs.add(arg);
            }
        }
    }

    public String[] getSourceArgs() {
        return sourceArgs;
    }

    public Set<String> getOptionNames() {
        return optionArgs.keySet();
    }

    public boolean containsOption(String name) {
        return optionArgs.containsKey(name);
    }

    public List<String> getOptionValues(String name) {
        return optionArgs.getOrDefault(name, new ArrayList<>());
    }

    public List<String> getNonOptionArgs() {
        return nonOptionArgs;
    }
}

// Database initialization runner
@Component
@Order(1)
class DatabaseInitRunner implements ApplicationRunner {

    public void run(ApplicationArguments args) throws Exception {
        System.out.println("[INIT] DatabaseInitRunner executing...");

        if (args.containsOption("init-db")) {
            System.out.println("[INIT] Initializing database schema");
            System.out.println("[INIT] Creating tables: users, products, orders");
            System.out.println("[INIT] Database initialized successfully");
        } else {
            System.out.println("[INIT] Skipping database initialization (use --init-db)");
        }
    }
}

// Data seeding runner
@Component
@Order(2)
class DataSeedRunner implements CommandLineRunner {

    public void run(String... args) throws Exception {
        System.out.println("\\n[SEED] DataSeedRunner executing...");

        boolean seedData = false;
        for (String arg : args) {
            if (arg.equals("--seed-data")) {
                seedData = true;
                break;
            }
        }

        if (seedData) {
            System.out.println("[SEED] Seeding initial data");
            System.out.println("[SEED] Inserted 10 sample users");
            System.out.println("[SEED] Inserted 50 sample products");
            System.out.println("[SEED] Data seeding completed");
        } else {
            System.out.println("[SEED] Skipping data seeding (use --seed-data)");
        }
    }
}

// Cache warming runner
@Component
@Order(3)
class CacheWarmupRunner implements ApplicationRunner {

    public void run(ApplicationArguments args) throws Exception {
        System.out.println("\\n[CACHE] CacheWarmupRunner executing...");

        System.out.println("[CACHE] Warming up application cache");
        System.out.println("[CACHE] Loading frequently accessed data");
        System.out.println("[CACHE] Cached 100 product categories");
        System.out.println("[CACHE] Cached 50 user profiles");
        System.out.println("[CACHE] Cache warmup completed in 250ms");
    }
}

// Application lifecycle manager
class ApplicationLifecycleManager {
    private List<ApplicationRunner> appRunners = new ArrayList<>();
    private List<CommandLineRunner> cmdRunners = new ArrayList<>();

    public void registerApplicationRunner(ApplicationRunner runner) {
        appRunners.add(runner);
    }

    public void registerCommandLineRunner(CommandLineRunner runner) {
        cmdRunners.add(runner);
    }

    public void executeRunners(String[] args) throws Exception {
        ApplicationArguments appArgs = new ApplicationArguments(args);

        System.out.println("=== Executing Application Runners ===");
        for (ApplicationRunner runner : appRunners) {
            runner.run(appArgs);
        }

        System.out.println("\\n=== Executing Command Line Runners ===");
        for (CommandLineRunner runner : cmdRunners) {
            runner.run(args);
        }
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("=== Spring Boot: Application Runners ===\\n");

        // Simulate Spring Boot startup with runners
        ApplicationLifecycleManager lifecycle = new ApplicationLifecycleManager();

        // Register runners
        lifecycle.registerApplicationRunner(new DatabaseInitRunner());
        lifecycle.registerCommandLineRunner(new DataSeedRunner());
        lifecycle.registerApplicationRunner(new CacheWarmupRunner());

        // Scenario 1: Run with no arguments
        System.out.println("1. Startup without arguments:");
        System.out.println("---");
        lifecycle.executeRunners(new String[]{});

        // Scenario 2: Run with initialization flags
        System.out.println("\\n\\n2. Startup with --init-db and --seed-data:");
        System.out.println("---");
        lifecycle.executeRunners(new String[]{"--init-db", "--seed-data"});

        // Scenario 3: Run with custom arguments
        System.out.println("\\n\\n3. Startup with custom arguments:");
        System.out.println("---");
        String[] customArgs = {
            "--init-db",
            "--environment=prod",
            "--port=8080",
            "extraArg"
        };
        ApplicationArguments args = new ApplicationArguments(customArgs);

        System.out.println("Parsed arguments:");
        System.out.println("  Options: " + args.getOptionNames());
        System.out.println("  Non-options: " + args.getNonOptionArgs());

        System.out.println("\\n=== Use Cases ===");
        System.out.println("ApplicationRunner:");
        System.out.println("  - Database schema initialization");
        System.out.println("  - Cache warmup");
        System.out.println("  - Configuration validation");
        System.out.println("  - Scheduled task registration");

        System.out.println("\\nCommandLineRunner:");
        System.out.println("  - Data import/export");
        System.out.println("  - Batch job execution");
        System.out.println("  - One-time setup tasks");
        System.out.println("  - System health checks");

        System.out.println("\\nExecution order:");
        System.out.println("  1. Use @Order annotation");
        System.out.println("  2. Lower value = higher priority");
        System.out.println("  3. Runs after application context fully initialized");
    }
}
""",

    846: """// Spring Boot: Graceful Shutdown
// In production: Configure in application.properties
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.util.concurrent.*;

// Simulated Spring lifecycle hooks
interface SmartLifecycle {
    void start();
    void stop();
    boolean isRunning();
    int getPhase();
}

@interface Component {}

// Active request tracker
class ActiveRequestTracker {
    private AtomicInteger activeRequests = new AtomicInteger(0);
    private volatile boolean accepting = true;

    public void requestStarted() {
        if (!accepting) {
            throw new IllegalStateException("Server is shutting down");
        }
        activeRequests.incrementAndGet();
    }

    public void requestCompleted() {
        activeRequests.decrementAndGet();
    }

    public int getActiveRequestCount() {
        return activeRequests.get();
    }

    public void stopAccepting() {
        accepting = false;
    }

    public boolean isAccepting() {
        return accepting;
    }
}

// Request processor simulation
class RequestProcessor implements Runnable {
    private String requestId;
    private int durationMs;
    private ActiveRequestTracker tracker;

    public RequestProcessor(String requestId, int durationMs, ActiveRequestTracker tracker) {
        this.requestId = requestId;
        this.durationMs = durationMs;
        this.tracker = tracker;
    }

    public void run() {
        try {
            tracker.requestStarted();
            System.out.println("  [REQ] Processing " + requestId + " (" + durationMs + "ms)");
            Thread.sleep(durationMs);
            System.out.println("  [REQ] Completed " + requestId);
        } catch (InterruptedException e) {
            System.out.println("  [REQ] Interrupted " + requestId);
        } catch (IllegalStateException e) {
            System.out.println("  [REQ] Rejected " + requestId + " - " + e.getMessage());
        } finally {
            tracker.requestCompleted();
        }
    }
}

// Graceful shutdown manager
@Component
class GracefulShutdownManager implements SmartLifecycle {
    private ActiveRequestTracker requestTracker;
    private ExecutorService executor;
    private volatile boolean running = false;
    private int gracePeriodSeconds = 30;

    public GracefulShutdownManager() {
        this.requestTracker = new ActiveRequestTracker();
        this.executor = Executors.newFixedThreadPool(10);
    }

    public void start() {
        running = true;
        System.out.println("[SHUTDOWN] Application started");
    }

    public void stop() {
        System.out.println("\\n[SHUTDOWN] Graceful shutdown initiated...");
        running = false;

        // Phase 1: Stop accepting new requests
        requestTracker.stopAccepting();
        System.out.println("[SHUTDOWN] Stopped accepting new requests");

        // Phase 2: Wait for active requests to complete
        System.out.println("[SHUTDOWN] Waiting for " + requestTracker.getActiveRequestCount() + " active requests");

        long startTime = System.currentTimeMillis();
        long timeout = gracePeriodSeconds * 1000;

        while (requestTracker.getActiveRequestCount() > 0) {
            long elapsed = System.currentTimeMillis() - startTime;
            if (elapsed >= timeout) {
                System.out.println("[SHUTDOWN] Grace period expired, forcing shutdown");
                break;
            }

            try {
                Thread.sleep(100);
                System.out.println("[SHUTDOWN] Active requests: " + requestTracker.getActiveRequestCount());
            } catch (InterruptedException e) {
                break;
            }
        }

        // Phase 3: Shutdown executor
        executor.shutdown();
        try {
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
        }

        System.out.println("[SHUTDOWN] All requests completed, shutdown complete");
    }

    public boolean isRunning() {
        return running;
    }

    public int getPhase() {
        return Integer.MAX_VALUE; // Shutdown last
    }

    // Simulate processing a request
    public void processRequest(String requestId, int durationMs) {
        executor.submit(new RequestProcessor(requestId, durationMs, requestTracker));
    }
}

// Database connection pool (simulated)
@Component
class DatabaseConnectionPool implements SmartLifecycle {
    private int activeConnections = 0;
    private boolean running = false;

    public void start() {
        running = true;
        activeConnections = 10;
        System.out.println("[DB-POOL] Connection pool initialized (10 connections)");
    }

    public void stop() {
        System.out.println("[DB-POOL] Closing database connections...");
        while (activeConnections > 0) {
            System.out.println("[DB-POOL] Closing connection " + activeConnections);
            activeConnections--;
            try {
                Thread.sleep(50);
            } catch (InterruptedException e) {
                break;
            }
        }
        running = false;
        System.out.println("[DB-POOL] All connections closed");
    }

    public boolean isRunning() {
        return running;
    }

    public int getPhase() {
        return Integer.MAX_VALUE - 1; // Close before request handler
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Spring Boot: Graceful Shutdown ===\\n");

        // Create shutdown manager and database pool
        GracefulShutdownManager shutdownManager = new GracefulShutdownManager();
        DatabaseConnectionPool dbPool = new DatabaseConnectionPool();

        // Start application
        shutdownManager.start();
        dbPool.start();

        System.out.println("\\n1. Simulating incoming requests:");
        // Submit some fast requests
        for (int i = 1; i <= 3; i++) {
            shutdownManager.processRequest("REQ-" + i, 200);
        }

        // Submit some slow requests
        shutdownManager.processRequest("REQ-SLOW-1", 2000);
        shutdownManager.processRequest("REQ-SLOW-2", 3000);

        // Wait for requests to start
        Thread.sleep(500);

        System.out.println("\\n2. Initiating shutdown (SIGTERM received):");
        // Trigger shutdown
        shutdownManager.stop();
        dbPool.stop();

        System.out.println("\\n=== Configuration ===");
        System.out.println("\\napplication.properties:");
        System.out.println("  # Enable graceful shutdown");
        System.out.println("  server.shutdown=graceful");
        System.out.println("  ");
        System.out.println("  # Grace period (default: 30s)");
        System.out.println("  spring.lifecycle.timeout-per-shutdown-phase=30s");

        System.out.println("\\nShutdown phases:");
        System.out.println("  1. Stop accepting new requests");
        System.out.println("  2. Complete in-flight requests");
        System.out.println("  3. Close database connections");
        System.out.println("  4. Release resources");
        System.out.println("  5. Exit application");

        System.out.println("\\nBenefits:");
        System.out.println("  - No 502/503 errors during deployment");
        System.out.println("  - Data consistency maintained");
        System.out.println("  - Better user experience");
        System.out.println("  - Clean resource cleanup");

        System.out.println("\\nProduction deployment:");
        System.out.println("  - Use SIGTERM instead of SIGKILL");
        System.out.println("  - Configure load balancer health checks");
        System.out.println("  - Set appropriate grace periods");
        System.out.println("  - Monitor shutdown metrics");
    }
}
""",

    847: """// Spring Boot: Admin Server (Spring Boot Admin)
// In production: Add spring-boot-admin-server and spring-boot-admin-client dependencies
// This lesson shows syntax only - requires actual Spring Boot Admin in production

import java.util.*;
import java.time.*;

// Simulated Spring Boot Admin annotations
@interface EnableAdminServer {}
@interface Configuration {}

// Application info
class ApplicationInfo {
    private String name;
    private String version;
    private String status;
    private Map<String, Object> metadata;

    public ApplicationInfo(String name, String version, String status) {
        this.name = name;
        this.version = version;
        this.status = status;
        this.metadata = new HashMap<>();
    }

    public String getName() { return name; }
    public String getVersion() { return version; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public void addMetadata(String key, Object value) {
        metadata.put(key, value);
    }

    public Map<String, Object> getMetadata() {
        return metadata;
    }
}

// Registered application instance
class ApplicationInstance {
    private String id;
    private ApplicationInfo info;
    private String healthUrl;
    private String metricsUrl;
    private String serviceUrl;
    private Instant registeredAt;
    private Instant lastHeartbeat;

    public ApplicationInstance(String id, ApplicationInfo info, String serviceUrl) {
        this.id = id;
        this.info = info;
        this.serviceUrl = serviceUrl;
        this.healthUrl = serviceUrl + "/actuator/health";
        this.metricsUrl = serviceUrl + "/actuator/metrics";
        this.registeredAt = Instant.now();
        this.lastHeartbeat = Instant.now();
    }

    public String getId() { return id; }
    public ApplicationInfo getInfo() { return info; }
    public String getHealthUrl() { return healthUrl; }
    public void heartbeat() { this.lastHeartbeat = Instant.now(); }
    public Instant getLastHeartbeat() { return lastHeartbeat; }
    public boolean isHealthy() {
        return Duration.between(lastHeartbeat, Instant.now()).getSeconds() < 30;
    }
}

// Admin server registry
class ApplicationRegistry {
    private Map<String, ApplicationInstance> instances = new HashMap<>();

    public void register(ApplicationInstance instance) {
        instances.put(instance.getId(), instance);
        System.out.println("[REGISTRY] Registered: " + instance.getInfo().getName() +
            " (" + instance.getId() + ")");
    }

    public void deregister(String id) {
        ApplicationInstance removed = instances.remove(id);
        if (removed != null) {
            System.out.println("[REGISTRY] Deregistered: " + removed.getInfo().getName());
        }
    }

    public List<ApplicationInstance> getAllInstances() {
        return new ArrayList<>(instances.values());
    }

    public ApplicationInstance getInstance(String id) {
        return instances.get(id);
    }

    public void heartbeat(String id) {
        ApplicationInstance instance = instances.get(id);
        if (instance != null) {
            instance.heartbeat();
            System.out.println("[HEARTBEAT] " + instance.getInfo().getName());
        }
    }
}

// Health check result
class HealthCheck {
    private String status;
    private Map<String, Object> details;

    public HealthCheck(String status) {
        this.status = status;
        this.details = new HashMap<>();
    }

    public String getStatus() { return status; }
    public Map<String, Object> getDetails() { return details; }

    public void addDetail(String key, Object value) {
        details.put(key, value);
    }
}

// Admin server
@Configuration
@EnableAdminServer
class AdminServer {
    private ApplicationRegistry registry;

    public AdminServer() {
        this.registry = new ApplicationRegistry();
    }

    public void registerApplication(String name, String version, String url) {
        ApplicationInfo info = new ApplicationInfo(name, version, "UP");
        info.addMetadata("startup-time", Instant.now());

        String id = UUID.randomUUID().toString();
        ApplicationInstance instance = new ApplicationInstance(id, info, url);
        registry.register(instance);
    }

    public void checkHealth() {
        System.out.println("\\n=== Health Check Results ===");
        for (ApplicationInstance instance : registry.getAllInstances()) {
            HealthCheck health = performHealthCheck(instance);
            System.out.println(instance.getInfo().getName() + ": " + health.getStatus());

            if ("UP".equals(health.getStatus())) {
                System.out.println("  Database: " + health.getDetails().get("database"));
                System.out.println("  Disk Space: " + health.getDetails().get("diskSpace"));
            }
        }
    }

    private HealthCheck performHealthCheck(ApplicationInstance instance) {
        // Simulate health check
        HealthCheck health = new HealthCheck("UP");
        health.addDetail("database", "UP");
        health.addDetail("diskSpace", "OK (80GB free)");
        health.addDetail("responseTime", "5ms");
        return health;
    }

    public void showMetrics() {
        System.out.println("\\n=== Application Metrics ===");
        for (ApplicationInstance instance : registry.getAllInstances()) {
            System.out.println(instance.getInfo().getName() + ":");
            System.out.println("  JVM Memory Used: 256MB / 512MB");
            System.out.println("  HTTP Requests: 1,234");
            System.out.println("  Response Time (avg): 120ms");
            System.out.println("  Error Rate: 0.5%");
        }
    }

    public void showEnvironment() {
        System.out.println("\\n=== Environment Properties ===");
        for (ApplicationInstance instance : registry.getAllInstances()) {
            System.out.println(instance.getInfo().getName() + ":");
            System.out.println("  Active Profiles: [prod]");
            System.out.println("  Server Port: 8080");
            System.out.println("  Database URL: jdbc:postgresql://localhost:5432/mydb");
        }
    }

    public void showLoggers() {
        System.out.println("\\n=== Logger Levels ===");
        System.out.println("com.example.myapp: DEBUG");
        System.out.println("org.springframework: INFO");
        System.out.println("root: WARN");
    }

    public void triggerAction(String action) {
        System.out.println("\\n[ACTION] Triggering: " + action);
        switch (action) {
            case "restart":
                System.out.println("  Restarting application...");
                break;
            case "gc":
                System.out.println("  Running garbage collection...");
                break;
            case "heapdump":
                System.out.println("  Creating heap dump...");
                break;
            case "threaddump":
                System.out.println("  Creating thread dump...");
                break;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot Admin Server ===\\n");

        // Create admin server
        AdminServer adminServer = new AdminServer();

        // Register applications
        System.out.println("1. Registering applications:");
        adminServer.registerApplication("user-service", "1.0.0", "http://localhost:8081");
        adminServer.registerApplication("order-service", "1.2.0", "http://localhost:8082");
        adminServer.registerApplication("payment-service", "2.0.0", "http://localhost:8083");

        // Health checks
        System.out.println("\\n2. Monitoring application health:");
        adminServer.checkHealth();

        // Metrics
        System.out.println("\\n3. Viewing metrics:");
        adminServer.showMetrics();

        // Environment
        System.out.println("\\n4. Environment configuration:");
        adminServer.showEnvironment();

        // Loggers
        System.out.println("\\n5. Logger configuration:");
        adminServer.showLoggers();

        // Actions
        System.out.println("\\n6. Administrative actions:");
        adminServer.triggerAction("gc");
        adminServer.triggerAction("threaddump");

        System.out.println("\\n=== Setup Instructions ===");
        System.out.println("\\nAdmin Server (pom.xml):");
        System.out.println("  <dependency>");
        System.out.println("    <groupId>de.codecentric</groupId>");
        System.out.println("    <artifactId>spring-boot-admin-starter-server</artifactId>");
        System.out.println("  </dependency>");

        System.out.println("\\nAdmin Client (application.properties):");
        System.out.println("  spring.boot.admin.client.url=http://localhost:9090");
        System.out.println("  management.endpoints.web.exposure.include=*");

        System.out.println("\\nFeatures:");
        System.out.println("  - Real-time application monitoring");
        System.out.println("  - Health check dashboard");
        System.out.println("  - Metrics visualization");
        System.out.println("  - Log level management");
        System.out.println("  - Thread/heap dumps");
        System.out.println("  - Email/Slack notifications");
    }
}
""",

    848: """// Spring Boot: Production Best Practices
// In production: Follow these patterns for robust applications
// This lesson shows syntax only - demonstrates production patterns

import java.util.*;
import java.time.*;

// 1. Configuration Management
class ConfigurationBestPractices {
    // Use externalized configuration
    private String databaseUrl = System.getenv("DATABASE_URL");
    private String apiKey = System.getenv("API_KEY");

    // Provide defaults
    private int connectionTimeout = Integer.parseInt(
        System.getenv().getOrDefault("DB_TIMEOUT", "30000"));

    // Validate on startup
    public void validateConfiguration() {
        if (databaseUrl == null || databaseUrl.isEmpty()) {
            throw new IllegalStateException("DATABASE_URL must be set");
        }
        if (apiKey == null || apiKey.isEmpty()) {
            throw new IllegalStateException("API_KEY must be set");
        }
        System.out.println("[CONFIG] Configuration validated successfully");
    }
}

// 2. Error Handling
class ErrorHandlingBestPractices {
    public void processData(String data) {
        try {
            // Business logic
            if (data == null) {
                throw new IllegalArgumentException("Data cannot be null");
            }

            // Process
            System.out.println("[PROCESS] Processing: " + data);

        } catch (IllegalArgumentException e) {
            // Log and handle gracefully
            System.err.println("[ERROR] Validation failed: " + e.getMessage());
            throw e; // Re-throw to caller
        } catch (Exception e) {
            // Log unexpected errors
            System.err.println("[ERROR] Unexpected error: " + e.getMessage());
            // Don't expose internal errors to users
            throw new RuntimeException("Processing failed", e);
        }
    }
}

// 3. Logging Best Practices
class LoggingBestPractices {
    private Map<String, Object> requestContext = new HashMap<>();

    public void processRequest(String requestId, String userId) {
        // Add context to all logs
        requestContext.put("requestId", requestId);
        requestContext.put("userId", userId);
        requestContext.put("timestamp", Instant.now());

        // Structured logging
        logInfo("Request started", requestContext);

        try {
            // Business logic
            Thread.sleep(100);

            logInfo("Request completed successfully", requestContext);

        } catch (Exception e) {
            logError("Request failed", e, requestContext);
        }
    }

    private void logInfo(String message, Map<String, Object> context) {
        System.out.println("[INFO] " + message + " " + formatContext(context));
    }

    private void logError(String message, Exception e, Map<String, Object> context) {
        System.err.println("[ERROR] " + message + " " + formatContext(context) +
            " exception=" + e.getClass().getSimpleName());
    }

    private String formatContext(Map<String, Object> context) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Object> entry : context.entrySet()) {
            sb.append(entry.getKey()).append("=").append(entry.getValue()).append(" ");
        }
        return sb.toString();
    }
}

// 4. Resource Management
class ResourceManagementBestPractices {
    public void processFile(String filename) {
        // Always use try-with-resources
        System.out.println("[RESOURCE] Processing file: " + filename);
        System.out.println("[RESOURCE] File processed successfully");
        System.out.println("[RESOURCE] Resources auto-closed");
    }

    public void manageConnectionPool() {
        // Configure pool limits
        int maxConnections = 100;
        int minIdle = 10;
        int connectionTimeout = 30000;

        System.out.println("[POOL] Connection pool configured:");
        System.out.println("  Max connections: " + maxConnections);
        System.out.println("  Min idle: " + minIdle);
        System.out.println("  Timeout: " + connectionTimeout + "ms");
    }
}

// 5. Security Best Practices
class SecurityBestPractices {
    public void handleSensitiveData() {
        // Never log sensitive data
        String password = "secret123";
        System.out.println("[SECURITY] Processing authentication (password: ***)");

        // Use secure defaults
        boolean httpsOnly = true;
        boolean csrfProtection = true;

        System.out.println("[SECURITY] HTTPS only: " + httpsOnly);
        System.out.println("[SECURITY] CSRF protection: " + csrfProtection);
    }

    public void validateInput(String userInput) {
        // Always validate user input
        if (userInput == null || userInput.trim().isEmpty()) {
            throw new IllegalArgumentException("Input cannot be empty");
        }

        if (userInput.length() > 1000) {
            throw new IllegalArgumentException("Input too long");
        }

        // Sanitize input
        String sanitized = userInput.replaceAll("[^a-zA-Z0-9\\s]", "");
        System.out.println("[SECURITY] Input validated and sanitized");
    }
}

// 6. Performance Best Practices
class PerformanceBestPractices {
    private Map<String, Object> cache = new HashMap<>();

    public Object getCachedData(String key) {
        // Use caching for expensive operations
        if (cache.containsKey(key)) {
            System.out.println("[CACHE] Cache hit: " + key);
            return cache.get(key);
        }

        System.out.println("[CACHE] Cache miss: " + key);
        Object data = loadExpensiveData(key);
        cache.put(key, data);
        return data;
    }

    private Object loadExpensiveData(String key) {
        // Simulate expensive operation
        return "data-" + key;
    }

    public void useConnectionPooling() {
        System.out.println("[PERF] Using connection pooling");
        System.out.println("[PERF] Reusing connections for efficiency");
    }
}

// 7. Monitoring Best Practices
class MonitoringBestPractices {
    private long requestCount = 0;
    private long errorCount = 0;

    public void recordRequest(boolean success) {
        requestCount++;
        if (!success) {
            errorCount++;
        }

        // Expose metrics
        if (requestCount % 100 == 0) {
            printMetrics();
        }
    }

    private void printMetrics() {
        double errorRate = (double) errorCount / requestCount * 100;
        System.out.println("[METRICS] Requests: " + requestCount);
        System.out.println("[METRICS] Errors: " + errorCount);
        System.out.println("[METRICS] Error rate: " + String.format("%.2f%%", errorRate));
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("=== Spring Boot: Production Best Practices ===\\n");

        // 1. Configuration
        System.out.println("1. Configuration Management:");
        ConfigurationBestPractices config = new ConfigurationBestPractices();
        // config.validateConfiguration(); // Would fail without env vars

        // 2. Error Handling
        System.out.println("\\n2. Error Handling:");
        ErrorHandlingBestPractices errors = new ErrorHandlingBestPractices();
        errors.processData("sample-data");

        // 3. Logging
        System.out.println("\\n3. Structured Logging:");
        LoggingBestPractices logging = new LoggingBestPractices();
        logging.processRequest("req-123", "user-456");

        // 4. Resource Management
        System.out.println("\\n4. Resource Management:");
        ResourceManagementBestPractices resources = new ResourceManagementBestPractices();
        resources.processFile("data.csv");
        resources.manageConnectionPool();

        // 5. Security
        System.out.println("\\n5. Security:");
        SecurityBestPractices security = new SecurityBestPractices();
        security.handleSensitiveData();
        security.validateInput("valid input");

        // 6. Performance
        System.out.println("\\n6. Performance:");
        PerformanceBestPractices perf = new PerformanceBestPractices();
        perf.getCachedData("key1");
        perf.getCachedData("key1"); // Cache hit
        perf.useConnectionPooling();

        // 7. Monitoring
        System.out.println("\\n7. Monitoring:");
        MonitoringBestPractices monitoring = new MonitoringBestPractices();
        for (int i = 0; i < 100; i++) {
            monitoring.recordRequest(i % 10 != 0); // 10% error rate
        }

        System.out.println("\\n=== Production Checklist ===");
        System.out.println("[√] Externalize configuration");
        System.out.println("[√] Implement proper error handling");
        System.out.println("[√] Use structured logging");
        System.out.println("[√] Manage resources properly");
        System.out.println("[√] Validate all inputs");
        System.out.println("[√] Enable security features");
        System.out.println("[√] Implement caching");
        System.out.println("[√] Expose health checks");
        System.out.println("[√] Monitor metrics");
        System.out.println("[√] Use graceful shutdown");
        System.out.println("[√] Configure connection pools");
        System.out.println("[√] Enable HTTPS");
        System.out.println("[√] Set up logging aggregation");
        System.out.println("[√] Implement circuit breakers");
        System.out.println("[√] Use rate limiting");
    }
}
""",

    1010: """// Spring Boot: Production Run Checklist
// In production: Verify all items before deployment
// This lesson shows deployment verification steps

import java.util.*;

// Checklist item
class ChecklistItem {
    private String category;
    private String item;
    private boolean required;
    private String status;

    public ChecklistItem(String category, String item, boolean required) {
        this.category = category;
        this.item = item;
        this.required = required;
        this.status = "PENDING";
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getCategory() { return category; }
    public String getItem() { return item; }
    public boolean isRequired() { return required; }
    public String getStatus() { return status; }
}

// Deployment checklist
class DeploymentChecklist {
    private List<ChecklistItem> items = new ArrayList<>();

    public DeploymentChecklist() {
        initializeChecklist();
    }

    private void initializeChecklist() {
        // Configuration
        add("Configuration", "Environment variables set", true);
        add("Configuration", "Database credentials configured", true);
        add("Configuration", "Active profile set (dev/staging/prod)", true);
        add("Configuration", "External configuration loaded", true);
        add("Configuration", "Secrets managed securely", true);

        // Application
        add("Application", "JAR file built successfully", true);
        add("Application", "Version number updated", true);
        add("Application", "Dependencies up to date", false);
        add("Application", "No snapshot dependencies", true);

        // Database
        add("Database", "Database migrations applied", true);
        add("Database", "Connection pool configured", true);
        add("Database", "Database backups enabled", true);
        add("Database", "Connection string validated", true);

        // Security
        add("Security", "HTTPS enabled", true);
        add("Security", "Authentication configured", true);
        add("Security", "CORS policy set", true);
        add("Security", "API keys rotated", false);
        add("Security", "Security headers enabled", true);

        // Monitoring
        add("Monitoring", "Health checks enabled", true);
        add("Monitoring", "Metrics endpoint exposed", true);
        add("Monitoring", "Logging configured", true);
        add("Monitoring", "Error tracking setup", true);
        add("Monitoring", "Alerts configured", false);

        // Performance
        add("Performance", "JVM options tuned", true);
        add("Performance", "Connection timeouts set", true);
        add("Performance", "Caching enabled", false);
        add("Performance", "Thread pool sized", true);

        // Deployment
        add("Deployment", "Load balancer configured", true);
        add("Deployment", "Graceful shutdown enabled", true);
        add("Deployment", "Blue-green deployment ready", false);
        add("Deployment", "Rollback plan prepared", true);
    }

    private void add(String category, String item, boolean required) {
        items.add(new ChecklistItem(category, item, required));
    }

    public void runChecks() {
        System.out.println("=== Running Deployment Checks ===\\n");

        for (ChecklistItem item : items) {
            // Simulate checking
            boolean passed = Math.random() > 0.1; // 90% pass rate
            item.setStatus(passed ? "PASS" : "FAIL");
        }
    }

    public void printReport() {
        Map<String, List<ChecklistItem>> byCategory = new HashMap<>();

        for (ChecklistItem item : items) {
            byCategory.computeIfAbsent(item.getCategory(), k -> new ArrayList<>()).add(item);
        }

        for (String category : byCategory.keySet()) {
            System.out.println("\\n=== " + category + " ===");
            List<ChecklistItem> categoryItems = byCategory.get(category);

            for (ChecklistItem item : categoryItems) {
                String marker = item.getStatus().equals("PASS") ? "[√]" : "[X]";
                String required = item.isRequired() ? "*" : " ";
                System.out.println(marker + required + " " + item.getItem());
            }
        }
    }

    public boolean isReadyForDeployment() {
        for (ChecklistItem item : items) {
            if (item.isRequired() && !item.getStatus().equals("PASS")) {
                return false;
            }
        }
        return true;
    }

    public void printSummary() {
        long total = items.size();
        long passed = items.stream().filter(i -> i.getStatus().equals("PASS")).count();
        long required = items.stream().filter(ChecklistItem::isRequired).count();
        long requiredPassed = items.stream()
            .filter(i -> i.isRequired() && i.getStatus().equals("PASS"))
            .count();

        System.out.println("\\n=== Deployment Readiness Summary ===");
        System.out.println("Total checks: " + passed + "/" + total);
        System.out.println("Required checks: " + requiredPassed + "/" + required);

        if (isReadyForDeployment()) {
            System.out.println("\\nStatus: [READY FOR DEPLOYMENT]");
            System.out.println("All required checks passed!");
        } else {
            System.out.println("\\nStatus: [NOT READY]");
            System.out.println("Required checks failed:");
            items.stream()
                .filter(i -> i.isRequired() && !i.getStatus().equals("PASS"))
                .forEach(i -> System.out.println("  - " + i.getCategory() + ": " + i.getItem()));
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Production Run Checklist ===\\n");

        DeploymentChecklist checklist = new DeploymentChecklist();

        // Run all checks
        checklist.runChecks();

        // Print detailed report
        checklist.printReport();

        // Print summary
        checklist.printSummary();

        System.out.println("\\n=== Pre-Deployment Commands ===");
        System.out.println("\\n1. Build:");
        System.out.println("   mvn clean package -DskipTests");

        System.out.println("\\n2. Test:");
        System.out.println("   mvn test");
        System.out.println("   mvn integration-test");

        System.out.println("\\n3. Verify:");
        System.out.println("   java -jar target/myapp.jar --version");
        System.out.println("   curl http://localhost:8080/actuator/health");

        System.out.println("\\n4. Deploy:");
        System.out.println("   scp target/myapp.jar prod-server:/opt/myapp/");
        System.out.println("   ssh prod-server 'systemctl restart myapp'");

        System.out.println("\\n5. Post-deployment:");
        System.out.println("   curl https://myapp.com/actuator/health");
        System.out.println("   tail -f /var/log/myapp/application.log");

        System.out.println("\\n=== Legend ===");
        System.out.println("  [√] = Passed");
        System.out.println("  [X] = Failed");
        System.out.println("  *   = Required for deployment");
    }
}
"""
}

print("=" * 80)
print("UPGRADING SPRING BOOT CORE - BATCH 4 (FINAL)")
print("IDs: 273, 846, 847, 848, 1010")
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
print("SPRING BOOT CORE COMPLETE!")
print("=" * 80)
print(f"\nUpgraded {len(results)} Spring Boot Core lessons")
print("Total Spring Boot Core lessons completed: 18/18")

for lesson_id, title, old_len, new_len, growth, pct in results:
    print(f"  ID {lesson_id:4d}: {title[:50]:50s} | +{growth:5,} chars ({pct:5.1f}%)")
