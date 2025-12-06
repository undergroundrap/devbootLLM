"""
Upgrade Spring Boot Core lessons - Batch 2
IDs: 511, 843, 844, 1015
Topics: Build Info, Properties, Profiles, Prometheus
"""
import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

upgrades = {
    511: """// Spring Boot: Build Information and Version Management
// In production: Add spring-boot-starter-actuator dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.time.*;
import java.io.*;

// Simulated Spring Boot annotations
@interface Component {}
@interface Value { String value(); }

// Build properties class
class BuildProperties {
    private String version;
    private String name;
    private String group;
    private Instant time;
    private String artifact;

    public BuildProperties() {
        this.version = "1.0.0-SNAPSHOT";
        this.name = "spring-boot-app";
        this.group = "com.example";
        this.time = Instant.now();
        this.artifact = "app";
    }

    public String getVersion() { return version; }
    public String getName() { return name; }
    public String getGroup() { return group; }
    public Instant getTime() { return time; }
    public String getArtifact() { return artifact; }

    public Map<String, Object> toMap() {
        Map<String, Object> props = new HashMap<>();
        props.put("version", version);
        props.put("name", name);
        props.put("group", group);
        props.put("artifact", artifact);
        props.put("time", time.toString());
        return props;
    }
}

// Git properties class
class GitProperties {
    private String branch;
    private String commitId;
    private String commitTime;
    private String commitUser;
    private String commitMessage;
    private boolean dirty;

    public GitProperties() {
        this.branch = "main";
        this.commitId = "abc123def456";
        this.commitTime = "2024-01-15T10:30:00Z";
        this.commitUser = "developer@example.com";
        this.commitMessage = "Add new feature";
        this.dirty = false;
    }

    public String getBranch() { return branch; }
    public String getCommitId() { return commitId; }
    public String getShortCommitId() { return commitId.substring(0, 7); }
    public String getCommitTime() { return commitTime; }
    public String getCommitUser() { return commitUser; }
    public String getCommitMessage() { return commitMessage; }
    public boolean isDirty() { return dirty; }

    public Map<String, Object> toMap() {
        Map<String, Object> props = new HashMap<>();
        props.put("branch", branch);
        props.put("commit.id", commitId);
        props.put("commit.id.abbrev", getShortCommitId());
        props.put("commit.time", commitTime);
        props.put("commit.user.name", commitUser);
        props.put("commit.message.short", commitMessage);
        props.put("dirty", dirty);
        return props;
    }
}

// Version info endpoint
@Component
class VersionInfoService {
    private BuildProperties buildProperties;
    private GitProperties gitProperties;

    public VersionInfoService() {
        this.buildProperties = new BuildProperties();
        this.gitProperties = new GitProperties();
    }

    public Map<String, Object> getVersionInfo() {
        Map<String, Object> info = new HashMap<>();
        info.put("application", buildProperties.toMap());
        info.put("git", gitProperties.toMap());
        info.put("java", getJavaInfo());
        info.put("os", getOsInfo());
        return info;
    }

    public String getVersionString() {
        return String.format("%s v%s (commit: %s)",
            buildProperties.getName(),
            buildProperties.getVersion(),
            gitProperties.getShortCommitId()
        );
    }

    public Map<String, String> getJavaInfo() {
        Map<String, String> java = new HashMap<>();
        java.put("version", System.getProperty("java.version"));
        java.put("vendor", System.getProperty("java.vendor"));
        java.put("runtime", System.getProperty("java.runtime.name"));
        return java;
    }

    public Map<String, String> getOsInfo() {
        Map<String, String> os = new HashMap<>();
        os.put("name", System.getProperty("os.name"));
        os.put("version", System.getProperty("os.version"));
        os.put("arch", System.getProperty("os.arch"));
        return os;
    }

    public void printBuildInfo() {
        System.out.println("=== Build Information ===");
        System.out.println("Application: " + buildProperties.getName());
        System.out.println("Version: " + buildProperties.getVersion());
        System.out.println("Group: " + buildProperties.getGroup());
        System.out.println("Artifact: " + buildProperties.getArtifact());
        System.out.println("Built: " + buildProperties.getTime());
    }

    public void printGitInfo() {
        System.out.println("\\n=== Git Information ===");
        System.out.println("Branch: " + gitProperties.getBranch());
        System.out.println("Commit: " + gitProperties.getCommitId());
        System.out.println("Short: " + gitProperties.getShortCommitId());
        System.out.println("Time: " + gitProperties.getCommitTime());
        System.out.println("Author: " + gitProperties.getCommitUser());
        System.out.println("Message: " + gitProperties.getCommitMessage());
        System.out.println("Dirty: " + gitProperties.isDirty());
    }
}

// Build info endpoint (for /actuator/info)
class InfoEndpoint {
    private VersionInfoService versionInfo;

    public InfoEndpoint(VersionInfoService versionInfo) {
        this.versionInfo = versionInfo;
    }

    public Map<String, Object> getInfo() {
        return versionInfo.getVersionInfo();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Build Information ===\\n");

        VersionInfoService versionService = new VersionInfoService();
        InfoEndpoint infoEndpoint = new InfoEndpoint(versionService);

        // Display build information
        versionService.printBuildInfo();
        versionService.printGitInfo();

        // Get version string
        System.out.println("\\n=== Version String ===");
        System.out.println(versionService.getVersionString());

        // Full info endpoint response
        System.out.println("\\n=== /actuator/info Response ===");
        Map<String, Object> info = infoEndpoint.getInfo();

        Map<String, Object> app = (Map<String, Object>) info.get("application");
        System.out.println("Application:");
        System.out.println("  Name: " + app.get("name"));
        System.out.println("  Version: " + app.get("version"));

        Map<String, Object> git = (Map<String, Object>) info.get("git");
        System.out.println("\\nGit:");
        System.out.println("  Branch: " + git.get("branch"));
        System.out.println("  Commit: " + git.get("commit.id.abbrev"));

        System.out.println("\\nHow to enable in production:");
        System.out.println("\\n1. Add to build.gradle:");
        System.out.println("   springBoot {");
        System.out.println("       buildInfo()");
        System.out.println("   }");

        System.out.println("\\n2. Add git-commit-id plugin:");
        System.out.println("   plugins {");
        System.out.println("       id 'com.gorylenko.gradle-git-properties' version '2.4.1'");
        System.out.println("   }");

        System.out.println("\\n3. Access via /actuator/info");
        System.out.println("\\nBuild info helps with:");
        System.out.println("  - Version tracking in production");
        System.out.println("  - Debugging which commit is deployed");
        System.out.println("  - Build reproducibility");
        System.out.println("  - Release management");
    }
}
""",

    843: """// Spring Boot: Properties Externalization
// In production: Add spring-boot dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.io.*;

// Simulated Spring annotations
@interface Component {}
@interface Value { String value(); }
@interface ConfigurationProperties { String prefix(); }

// Application properties holder
class ApplicationProperties {
    // Default values
    private Map<String, String> properties = new HashMap<>();

    public ApplicationProperties() {
        // Simulate loading from application.properties
        properties.put("app.name", "MyApp");
        properties.put("app.version", "1.0.0");
        properties.put("app.max-connections", "100");
        properties.put("app.timeout", "5000");
        properties.put("app.api-key", "${API_KEY:default-key}");
        properties.put("server.port", "8080");
        properties.put("spring.datasource.url", "jdbc:postgresql://localhost:5432/mydb");
        properties.put("spring.datasource.username", "user");
        properties.put("spring.datasource.password", "${DB_PASSWORD:secret}");
    }

    public String getProperty(String key) {
        String value = properties.get(key);
        if (value != null && value.contains("${")) {
            // Resolve environment variable
            return resolveEnvironmentVariable(value);
        }
        return value;
    }

    private String resolveEnvironmentVariable(String value) {
        // Parse ${VAR:default} format
        if (value.startsWith("${") && value.endsWith("}")) {
            String content = value.substring(2, value.length() - 1);
            String[] parts = content.split(":", 2);
            String varName = parts[0];
            String defaultValue = parts.length > 1 ? parts[1] : "";

            // Simulate environment variable lookup
            String envValue = System.getenv(varName);
            return envValue != null ? envValue : defaultValue;
        }
        return value;
    }

    public void setProperty(String key, String value) {
        properties.put(key, value);
    }

    public Map<String, String> getAllProperties() {
        return new HashMap<>(properties);
    }
}

// Configuration properties class with @ConfigurationProperties
@ConfigurationProperties(prefix = "app")
class AppConfig {
    private String name;
    private String version;
    private int maxConnections;
    private int timeout;
    private String apiKey;

    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getVersion() { return version; }
    public void setVersion(String version) { this.version = version; }

    public int getMaxConnections() { return maxConnections; }
    public void setMaxConnections(int maxConnections) { this.maxConnections = maxConnections; }

    public int getTimeout() { return timeout; }
    public void setTimeout(int timeout) { this.timeout = timeout; }

    public String getApiKey() { return apiKey; }
    public void setApiKey(String apiKey) { this.apiKey = apiKey; }

    @Override
    public String toString() {
        return String.format("AppConfig{name='%s', version='%s', maxConnections=%d, timeout=%d}",
            name, version, maxConnections, timeout);
    }
}

// Database configuration
@ConfigurationProperties(prefix = "spring.datasource")
class DataSourceConfig {
    private String url;
    private String username;
    private String password;
    private int maxPoolSize = 10;

    public String getUrl() { return url; }
    public void setUrl(String url) { this.url = url; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }

    public int getMaxPoolSize() { return maxPoolSize; }
    public void setMaxPoolSize(int maxPoolSize) { this.maxPoolSize = maxPoolSize; }

    public String getConnectionString() {
        return String.format("%s (user: %s, pool: %d)", url, username, maxPoolSize);
    }
}

// Service using @Value injection
@Component
class ConfigService {
    @Value("${app.name}")
    private String appName;

    @Value("${app.max-connections:50}") // With default value
    private int maxConnections;

    @Value("${server.port:8080}")
    private int serverPort;

    private ApplicationProperties props;

    public ConfigService(ApplicationProperties props) {
        this.props = props;
        // Simulate @Value injection
        this.appName = props.getProperty("app.name");
        this.maxConnections = Integer.parseInt(props.getProperty("app.max-connections"));
        this.serverPort = Integer.parseInt(props.getProperty("server.port"));
    }

    public void printConfiguration() {
        System.out.println("=== Service Configuration ===");
        System.out.println("App Name: " + appName);
        System.out.println("Max Connections: " + maxConnections);
        System.out.println("Server Port: " + serverPort);
    }
}

// Configuration properties binder simulation
class ConfigurationBinder {
    private ApplicationProperties props;

    public ConfigurationBinder(ApplicationProperties props) {
        this.props = props;
    }

    public AppConfig bindAppConfig() {
        AppConfig config = new AppConfig();
        config.setName(props.getProperty("app.name"));
        config.setVersion(props.getProperty("app.version"));
        config.setMaxConnections(Integer.parseInt(props.getProperty("app.max-connections")));
        config.setTimeout(Integer.parseInt(props.getProperty("app.timeout")));
        config.setApiKey(props.getProperty("app.api-key"));
        return config;
    }

    public DataSourceConfig bindDataSourceConfig() {
        DataSourceConfig config = new DataSourceConfig();
        config.setUrl(props.getProperty("spring.datasource.url"));
        config.setUsername(props.getProperty("spring.datasource.username"));
        config.setPassword(props.getProperty("spring.datasource.password"));
        return config;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Properties Externalization ===\\n");

        // Load properties
        ApplicationProperties props = new ApplicationProperties();

        System.out.println("1. Using @Value annotation:");
        ConfigService service = new ConfigService(props);
        service.printConfiguration();

        System.out.println("\\n2. Using @ConfigurationProperties:");
        ConfigurationBinder binder = new ConfigurationBinder(props);

        AppConfig appConfig = binder.bindAppConfig();
        System.out.println(appConfig);

        DataSourceConfig dbConfig = binder.bindDataSourceConfig();
        System.out.println("DataSource: " + dbConfig.getConnectionString());

        System.out.println("\\n3. Environment variable resolution:");
        System.out.println("API Key (with default): " + props.getProperty("app.api-key"));
        System.out.println("DB Password (with default): " + props.getProperty("spring.datasource.password"));

        System.out.println("\\n4. Property override hierarchy:");
        System.out.println("  1. Command line arguments: --server.port=9090");
        System.out.println("  2. Environment variables: SERVER_PORT=9090");
        System.out.println("  3. application-{profile}.properties");
        System.out.println("  4. application.properties");
        System.out.println("  5. @PropertySource annotations");
        System.out.println("  6. Default values in @Value");

        System.out.println("\\nProperty sources:");
        System.out.println("  - application.properties (classpath)");
        System.out.println("  - application.yml (YAML format)");
        System.out.println("  - Environment variables");
        System.out.println("  - Command line arguments");
        System.out.println("  - Config server (Spring Cloud Config)");

        System.out.println("\\nBest practices:");
        System.out.println("  - Use @ConfigurationProperties for related properties");
        System.out.println("  - Use @Value for simple injection");
        System.out.println("  - Never hardcode secrets (use environment variables)");
        System.out.println("  - Provide sensible defaults");
        System.out.println("  - Validate configuration with @Validated");
    }
}
""",

    844: """// Spring Boot: Advanced Profiles
// In production: Add spring-boot dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;

// Simulated Spring annotations
@interface Component {}
@interface Profile { String[] value(); }
@interface Configuration {}
@interface Bean {}

// Environment interface simulation
class Environment {
    private Set<String> activeProfiles = new HashSet<>();
    private Map<String, String> properties = new HashMap<>();

    public Environment() {
        // Default to 'dev' profile
        activeProfiles.add("dev");
    }

    public void setActiveProfiles(String... profiles) {
        activeProfiles.clear();
        activeProfiles.addAll(Arrays.asList(profiles));
    }

    public String[] getActiveProfiles() {
        return activeProfiles.toArray(new String[0]);
    }

    public boolean acceptsProfiles(String profile) {
        return activeProfiles.contains(profile);
    }

    public void setProperty(String key, String value) {
        properties.put(key, value);
    }

    public String getProperty(String key) {
        return properties.get(key);
    }
}

// Database configuration interface
interface DatabaseConfig {
    String getUrl();
    int getMaxConnections();
    boolean isPoolingEnabled();
}

// Development database configuration
@Profile({"dev", "local"})
@Configuration
class DevDatabaseConfig implements DatabaseConfig {
    public String getUrl() {
        return "jdbc:h2:mem:devdb";
    }

    public int getMaxConnections() {
        return 5;
    }

    public boolean isPoolingEnabled() {
        return false;
    }

    @Override
    public String toString() {
        return "DevDatabaseConfig{H2 in-memory, 5 connections, no pooling}";
    }
}

// Production database configuration
@Profile("prod")
@Configuration
class ProdDatabaseConfig implements DatabaseConfig {
    public String getUrl() {
        return "jdbc:postgresql://prod-db.example.com:5432/mydb";
    }

    public int getMaxConnections() {
        return 100;
    }

    public boolean isPoolingEnabled() {
        return true;
    }

    @Override
    public String toString() {
        return "ProdDatabaseConfig{PostgreSQL, 100 connections, pooling enabled}";
    }
}

// Staging database configuration
@Profile("staging")
@Configuration
class StagingDatabaseConfig implements DatabaseConfig {
    public String getUrl() {
        return "jdbc:postgresql://staging-db.example.com:5432/mydb";
    }

    public int getMaxConnections() {
        return 50;
    }

    public boolean isPoolingEnabled() {
        return true;
    }

    @Override
    public String toString() {
        return "StagingDatabaseConfig{PostgreSQL, 50 connections, pooling enabled}";
    }
}

// Logging configuration
interface LoggingConfig {
    String getLevel();
    boolean isDebugEnabled();
}

@Profile("dev")
@Configuration
class DevLoggingConfig implements LoggingConfig {
    public String getLevel() { return "DEBUG"; }
    public boolean isDebugEnabled() { return true; }
}

@Profile("prod")
@Configuration
class ProdLoggingConfig implements LoggingConfig {
    public String getLevel() { return "WARN"; }
    public boolean isDebugEnabled() { return false; }
}

// Feature flags based on profiles
@Component
class FeatureToggleService {
    private Environment environment;

    public FeatureToggleService(Environment environment) {
        this.environment = environment;
    }

    public boolean isFeatureEnabled(String feature) {
        if (feature.equals("experimental") && environment.acceptsProfiles("dev")) {
            return true;
        }
        if (feature.equals("analytics") && environment.acceptsProfiles("prod")) {
            return true;
        }
        if (feature.equals("debug-mode") && environment.acceptsProfiles("dev")) {
            return true;
        }
        return false;
    }

    public void printFeatureStatus() {
        System.out.println("=== Feature Toggles ===");
        System.out.println("Experimental features: " + isFeatureEnabled("experimental"));
        System.out.println("Analytics: " + isFeatureEnabled("analytics"));
        System.out.println("Debug mode: " + isFeatureEnabled("debug-mode"));
    }
}

// Profile-aware application context
class ApplicationContext {
    private Environment environment;
    private Map<String, Object> beans = new HashMap<>();

    public ApplicationContext(Environment environment) {
        this.environment = environment;
        initializeBeans();
    }

    private void initializeBeans() {
        // Register database config based on active profile
        for (String profile : environment.getActiveProfiles()) {
            if (profile.equals("dev") || profile.equals("local")) {
                beans.put("databaseConfig", new DevDatabaseConfig());
                beans.put("loggingConfig", new DevLoggingConfig());
            } else if (profile.equals("prod")) {
                beans.put("databaseConfig", new ProdDatabaseConfig());
                beans.put("loggingConfig", new ProdLoggingConfig());
            } else if (profile.equals("staging")) {
                beans.put("databaseConfig", new StagingDatabaseConfig());
            }
        }

        beans.put("featureToggle", new FeatureToggleService(environment));
    }

    public <T> T getBean(String name, Class<T> type) {
        return type.cast(beans.get(name));
    }

    public void printConfiguration() {
        System.out.println("=== Application Configuration ===");
        System.out.println("Active Profiles: " + Arrays.toString(environment.getActiveProfiles()));

        if (beans.containsKey("databaseConfig")) {
            DatabaseConfig dbConfig = (DatabaseConfig) beans.get("databaseConfig");
            System.out.println("\\nDatabase: " + dbConfig);
        }

        if (beans.containsKey("loggingConfig")) {
            LoggingConfig logConfig = (LoggingConfig) beans.get("loggingConfig");
            System.out.println("\\nLogging Level: " + logConfig.getLevel());
            System.out.println("Debug Enabled: " + logConfig.isDebugEnabled());
        }

        FeatureToggleService features = (FeatureToggleService) beans.get("featureToggle");
        System.out.println();
        features.printFeatureStatus();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Advanced Profiles ===\\n");

        // Scenario 1: Development profile
        System.out.println("1. Development Environment:");
        Environment devEnv = new Environment();
        devEnv.setActiveProfiles("dev");
        ApplicationContext devContext = new ApplicationContext(devEnv);
        devContext.printConfiguration();

        // Scenario 2: Production profile
        System.out.println("\\n2. Production Environment:");
        Environment prodEnv = new Environment();
        prodEnv.setActiveProfiles("prod");
        ApplicationContext prodContext = new ApplicationContext(prodEnv);
        prodContext.printConfiguration();

        // Scenario 3: Multiple profiles
        System.out.println("\\n3. Staging with Dev Tools:");
        Environment stagingEnv = new Environment();
        stagingEnv.setActiveProfiles("staging", "dev");
        ApplicationContext stagingContext = new ApplicationContext(stagingEnv);
        stagingContext.printConfiguration();

        System.out.println("\\n=== Profile Usage ===");
        System.out.println("\\n1. Set active profile:");
        System.out.println("   - application.properties: spring.profiles.active=dev");
        System.out.println("   - Environment variable: SPRING_PROFILES_ACTIVE=prod");
        System.out.println("   - Command line: --spring.profiles.active=prod");

        System.out.println("\\n2. Profile-specific files:");
        System.out.println("   - application-dev.properties");
        System.out.println("   - application-prod.properties");
        System.out.println("   - application-staging.properties");

        System.out.println("\\n3. Common profiles:");
        System.out.println("   - dev: Development with debug logging");
        System.out.println("   - test: Integration testing");
        System.out.println("   - staging: Pre-production environment");
        System.out.println("   - prod: Production with optimizations");

        System.out.println("\\n4. Profile expressions:");
        System.out.println("   @Profile(\"!prod\") - All except prod");
        System.out.println("   @Profile({\"dev\", \"local\"}) - Dev OR local");
        System.out.println("   @Profile(\"prod & cloud\") - Prod AND cloud");
    }
}
""",

    1015: """// Spring Boot: Prometheus Integration
// In production: Add spring-boot-starter-actuator and micrometer-registry-prometheus
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.util.concurrent.*;

// Simulated Prometheus/Micrometer annotations
@interface Timed { String value(); }
@interface Counted { String value(); }

// Prometheus metric types
enum MetricType {
    COUNTER, GAUGE, HISTOGRAM, SUMMARY
}

// Prometheus metric
class PrometheusMetric {
    private String name;
    private MetricType type;
    private Map<String, String> labels;
    private double value;

    public PrometheusMetric(String name, MetricType type) {
        this.name = name;
        this.type = type;
        this.labels = new HashMap<>();
        this.value = 0.0;
    }

    public PrometheusMetric withLabel(String key, String value) {
        labels.put(key, value);
        return this;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public void increment() {
        this.value++;
    }

    public void increment(double amount) {
        this.value += amount;
    }

    public String toPrometheusFormat() {
        StringBuilder sb = new StringBuilder();

        // Format: metric_name{label1="value1",label2="value2"} value
        sb.append(name);

        if (!labels.isEmpty()) {
            sb.append("{");
            boolean first = true;
            for (Map.Entry<String, String> entry : labels.entrySet()) {
                if (!first) sb.append(",");
                sb.append(entry.getKey()).append("=\"").append(entry.getValue()).append("\"");
                first = false;
            }
            sb.append("}");
        }

        sb.append(" ").append(value);
        return sb.toString();
    }

    public String getName() { return name; }
    public MetricType getType() { return type; }
}

// Prometheus registry
class PrometheusRegistry {
    private Map<String, PrometheusMetric> metrics = new ConcurrentHashMap<>();

    public PrometheusMetric counter(String name, String... labels) {
        String key = name + Arrays.toString(labels);
        metrics.putIfAbsent(key, new PrometheusMetric(name, MetricType.COUNTER));

        PrometheusMetric metric = metrics.get(key);
        for (int i = 0; i < labels.length; i += 2) {
            if (i + 1 < labels.length) {
                metric.withLabel(labels[i], labels[i + 1]);
            }
        }
        return metric;
    }

    public PrometheusMetric gauge(String name, String... labels) {
        String key = name + Arrays.toString(labels);
        metrics.putIfAbsent(key, new PrometheusMetric(name, MetricType.GAUGE));

        PrometheusMetric metric = metrics.get(key);
        for (int i = 0; i < labels.length; i += 2) {
            if (i + 1 < labels.length) {
                metric.withLabel(labels[i], labels[i + 1]);
            }
        }
        return metric;
    }

    public String scrape() {
        StringBuilder output = new StringBuilder();

        // Group by metric name
        Map<String, List<PrometheusMetric>> grouped = new HashMap<>();
        for (PrometheusMetric metric : metrics.values()) {
            grouped.computeIfAbsent(metric.getName(), k -> new ArrayList<>()).add(metric);
        }

        // Output in Prometheus exposition format
        for (Map.Entry<String, List<PrometheusMetric>> entry : grouped.entrySet()) {
            String metricName = entry.getKey();
            List<PrometheusMetric> metricList = entry.getValue();

            if (!metricList.isEmpty()) {
                MetricType type = metricList.get(0).getType();
                output.append("# HELP ").append(metricName).append(" ").append(metricName).append("\\n");
                output.append("# TYPE ").append(metricName).append(" ").append(type.toString().toLowerCase()).append("\\n");

                for (PrometheusMetric metric : metricList) {
                    output.append(metric.toPrometheusFormat()).append("\\n");
                }
            }
        }

        return output.toString();
    }
}

// Service with Prometheus metrics
class OrderService {
    private PrometheusRegistry registry;
    private PrometheusMetric ordersTotal;
    private PrometheusMetric ordersSuccessful;
    private PrometheusMetric ordersFailed;
    private PrometheusMetric ordersActive;
    private int activeOrders = 0;

    public OrderService(PrometheusRegistry registry) {
        this.registry = registry;

        // Initialize metrics
        this.ordersTotal = registry.counter("orders_total", "type", "all");
        this.ordersSuccessful = registry.counter("orders_successful", "status", "completed");
        this.ordersFailed = registry.counter("orders_failed", "reason", "validation");
        this.ordersActive = registry.gauge("orders_active");
    }

    @Counted("orders_total")
    @Timed("order_processing_duration")
    public String createOrder(String orderId, double amount) {
        ordersTotal.increment();
        activeOrders++;
        ordersActive.setValue(activeOrders);

        try {
            // Simulate order processing
            Thread.sleep(50);

            if (amount < 0) {
                ordersFailed.increment();
                activeOrders--;
                ordersActive.setValue(activeOrders);
                return "FAILED";
            }

            ordersSuccessful.increment();
            activeOrders--;
            ordersActive.setValue(activeOrders);
            return "SUCCESS";

        } catch (InterruptedException e) {
            ordersFailed.increment();
            activeOrders--;
            ordersActive.setValue(activeOrders);
            return "ERROR";
        }
    }
}

// HTTP endpoint metrics
class HttpMetrics {
    private PrometheusRegistry registry;
    private Map<String, PrometheusMetric> requestCounters = new HashMap<>();
    private Map<String, PrometheusMetric> requestDurations = new HashMap<>();

    public HttpMetrics(PrometheusRegistry registry) {
        this.registry = registry;
    }

    public void recordRequest(String method, String path, int statusCode, long durationMs) {
        String key = method + ":" + path;

        // Request counter
        if (!requestCounters.containsKey(key)) {
            requestCounters.put(key,
                registry.counter("http_requests_total",
                    "method", method,
                    "path", path,
                    "status", String.valueOf(statusCode)));
        }
        requestCounters.get(key).increment();

        // Request duration (simulated histogram)
        if (!requestDurations.containsKey(key)) {
            requestDurations.put(key,
                registry.counter("http_request_duration_ms_sum",
                    "method", method,
                    "path", path));
        }
        requestDurations.get(key).increment(durationMs);
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== Spring Boot: Prometheus Integration ===\\n");

        PrometheusRegistry registry = new PrometheusRegistry();

        // Create services with metrics
        OrderService orderService = new OrderService(registry);
        HttpMetrics httpMetrics = new HttpMetrics(registry);

        System.out.println("1. Processing orders (with metrics):");
        for (int i = 1; i <= 5; i++) {
            String result = orderService.createOrder("ORD-" + i, 100.0 * i);
            System.out.println("   Order " + i + ": " + result);
        }

        // Attempt invalid order
        String failedOrder = orderService.createOrder("ORD-BAD", -100.0);
        System.out.println("   Invalid order: " + failedOrder);

        System.out.println("\\n2. Recording HTTP requests:");
        httpMetrics.recordRequest("GET", "/api/orders", 200, 45);
        httpMetrics.recordRequest("POST", "/api/orders", 201, 120);
        httpMetrics.recordRequest("GET", "/api/orders", 200, 38);
        httpMetrics.recordRequest("DELETE", "/api/orders/123", 404, 15);
        System.out.println("   Recorded 4 HTTP requests");

        // Scrape metrics (Prometheus format)
        System.out.println("\\n3. Metrics endpoint /actuator/prometheus:");
        System.out.println("---");
        String metrics = registry.scrape();
        System.out.println(metrics);
        System.out.println("---");

        System.out.println("\\n=== Prometheus Configuration ===");
        System.out.println("\\n1. Add dependencies:");
        System.out.println("   <dependency>");
        System.out.println("       <groupId>io.micrometer</groupId>");
        System.out.println("       <artifactId>micrometer-registry-prometheus</artifactId>");
        System.out.println("   </dependency>");

        System.out.println("\\n2. Enable Prometheus endpoint (application.properties):");
        System.out.println("   management.endpoints.web.exposure.include=prometheus");
        System.out.println("   management.metrics.export.prometheus.enabled=true");

        System.out.println("\\n3. Prometheus scrape config (prometheus.yml):");
        System.out.println("   scrape_configs:");
        System.out.println("     - job_name: 'spring-boot'");
        System.out.println("       metrics_path: '/actuator/prometheus'");
        System.out.println("       static_configs:");
        System.out.println("         - targets: ['localhost:8080']");

        System.out.println("\\n4. Common queries:");
        System.out.println("   - Request rate: rate(http_requests_total[5m])");
        System.out.println("   - 95th percentile: histogram_quantile(0.95, http_duration)");
        System.out.println("   - Error rate: rate(http_requests_total{status=~\"5..\"}[5m])");

        System.out.println("\\nIntegration benefits:");
        System.out.println("  - Real-time metrics scraping");
        System.out.println("  - Time-series data storage");
        System.out.println("  - Alerting with Alertmanager");
        System.out.println("  - Visualization with Grafana");
    }
}
"""
}

print("=" * 80)
print("UPGRADING SPRING BOOT CORE - BATCH 2")
print("IDs: 511, 843, 844, 1015")
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
print("BATCH 2 COMPLETE!")
print("=" * 80)
print(f"\nUpgraded {len(results)} Spring Boot Core lessons")

for lesson_id, title, old_len, new_len, growth, pct in results:
    print(f"  ID {lesson_id:4d}: {title[:50]:50s} | +{growth:5,} chars ({pct:5.1f}%)")
