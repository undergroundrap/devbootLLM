"""
Upgrade Spring Boot Core lessons - Batch 3
IDs: 1017, 1016, 845, 218, 1011
Topics: Auto-configuration, Custom Starters, Logging, Deployment
"""
import json

lessons = json.load(open(r'c:\devbootLLM-app\public\lessons-java.json', encoding='utf-8'))

upgrades = {
    1017: """// Spring Boot: Auto-configuration Deep Dive
// In production: Add spring-boot-autoconfigure dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.lang.annotation.*;

// Simulated Spring Boot auto-configuration annotations
@interface Configuration {}
@interface Bean {}
@interface ConditionalOnClass { Class<?>[] value(); }
@interface ConditionalOnMissingBean { Class<?>[] value() default {}; }
@interface ConditionalOnProperty { String name(); String havingValue() default ""; }
@interface EnableAutoConfiguration {}
@interface AutoConfigurationPackage {}

// Auto-configuration class example
@Configuration
@ConditionalOnClass({})
class DataSourceAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public DataSource dataSource() {
        System.out.println("[AUTO-CONFIG] Creating default DataSource");
        return new SimpleDataSource("jdbc:h2:mem:default", "sa", "");
    }
}

// Simple DataSource implementation
class SimpleDataSource {
    private String url;
    private String username;
    private String password;

    public SimpleDataSource(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    public String getUrl() { return url; }
    public String getUsername() { return username; }
}

interface DataSource {
    String getUrl();
    String getUsername();
}

// Web auto-configuration
@Configuration
@ConditionalOnClass({})
class WebMvcAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public ViewResolver viewResolver() {
        System.out.println("[AUTO-CONFIG] Creating default ViewResolver");
        return new SimpleViewResolver();
    }
}

interface ViewResolver {
    String resolve(String viewName);
}

class SimpleViewResolver implements ViewResolver {
    public String resolve(String viewName) {
        return "/WEB-INF/views/" + viewName + ".jsp";
    }
}

// Jackson auto-configuration
@Configuration
@ConditionalOnClass({})
class JacksonAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public ObjectMapper objectMapper() {
        System.out.println("[AUTO-CONFIG] Creating default ObjectMapper");
        return new SimpleObjectMapper();
    }
}

class SimpleObjectMapper {
    public String writeValueAsString(Object obj) {
        return "{\"simulated\":\"json\"}";
    }
}

// Auto-configuration registry
class AutoConfigurationRegistry {
    private List<Object> autoConfigurations = new ArrayList<>();
    private Map<String, Object> beans = new HashMap<>();

    public void register(Object config) {
        autoConfigurations.add(config);
        System.out.println("[REGISTRY] Registered: " + config.getClass().getSimpleName());
    }

    public void processAutoConfigurations() {
        System.out.println("\\n[AUTO-CONFIG] Processing auto-configurations...");

        for (Object config : autoConfigurations) {
            if (config instanceof DataSourceAutoConfiguration) {
                DataSource ds = ((DataSourceAutoConfiguration) config).dataSource();
                beans.put("dataSource", ds);
            } else if (config instanceof WebMvcAutoConfiguration) {
                ViewResolver vr = ((WebMvcAutoConfiguration) config).viewResolver();
                beans.put("viewResolver", vr);
            } else if (config instanceof JacksonAutoConfiguration) {
                ObjectMapper om = ((JacksonAutoConfiguration) config).objectMapper();
                beans.put("objectMapper", om);
            }
        }

        System.out.println("[AUTO-CONFIG] Created " + beans.size() + " beans");
    }

    public <T> T getBean(String name, Class<T> type) {
        return type.cast(beans.get(name));
    }

    public void printBeans() {
        System.out.println("\\n=== Auto-configured Beans ===");
        for (String beanName : beans.keySet()) {
            Object bean = beans.get(beanName);
            System.out.println("  - " + beanName + ": " + bean.getClass().getSimpleName());
        }
    }
}

@EnableAutoConfiguration
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Auto-configuration ===\\n");

        // Simulate Spring Boot's auto-configuration mechanism
        AutoConfigurationRegistry registry = new AutoConfigurationRegistry();

        System.out.println("1. Registering auto-configurations:");
        registry.register(new DataSourceAutoConfiguration());
        registry.register(new WebMvcAutoConfiguration());
        registry.register(new JacksonAutoConfiguration());

        // Process auto-configurations
        System.out.println("\\n2. Processing configurations:");
        registry.processAutoConfigurations();

        // Print registered beans
        registry.printBeans();

        // Use auto-configured beans
        System.out.println("\\n3. Using auto-configured beans:");
        DataSource ds = registry.getBean("dataSource", SimpleDataSource.class);
        System.out.println("  DataSource URL: " + ds.getUrl());

        ViewResolver vr = registry.getBean("viewResolver", ViewResolver.class);
        System.out.println("  View resolved: " + vr.resolve("home"));

        System.out.println("\\n=== Auto-configuration Conditions ===");
        System.out.println("@ConditionalOnClass - Bean created if class is present");
        System.out.println("@ConditionalOnMissingBean - Bean created if no bean of type exists");
        System.out.println("@ConditionalOnProperty - Bean created if property matches");
        System.out.println("@ConditionalOnWebApplication - Only for web applications");

        System.out.println("\\nHow Spring Boot auto-configures:");
        System.out.println("1. Scans META-INF/spring.factories");
        System.out.println("2. Loads EnableAutoConfiguration entries");
        System.out.println("3. Evaluates @Conditional annotations");
        System.out.println("4. Creates beans if conditions met");
        System.out.println("5. User beans override auto-configured beans");
    }
}
""",

    1016: """// Spring Boot: Creating Custom Starters
// In production: Create separate module with dependencies
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.lang.annotation.*;

// Simulated Spring annotations
@interface Configuration {}
@interface Bean {}
@interface ConfigurationProperties { String prefix(); }
@interface EnableConfigurationProperties { Class<?>[] value(); }
@interface ConditionalOnMissingBean {}
@interface AutoConfiguration {}

// Custom starter: Email Service Starter

// 1. Configuration properties
@ConfigurationProperties(prefix = "app.email")
class EmailProperties {
    private String host = "smtp.gmail.com";
    private int port = 587;
    private String username;
    private String password;
    private String from;
    private boolean enabled = true;

    // Getters and setters
    public String getHost() { return host; }
    public void setHost(String host) { this.host = host; }

    public int getPort() { return port; }
    public void setPort(int port) { this.port = port; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }

    public String getFrom() { return from; }
    public void setFrom(String from) { this.from = from; }

    public boolean isEnabled() { return enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}

// 2. Service implementation
class EmailService {
    private EmailProperties properties;

    public EmailService(EmailProperties properties) {
        this.properties = properties;
        System.out.println("[EMAIL] Email service initialized");
        System.out.println("[EMAIL] SMTP: " + properties.getHost() + ":" + properties.getPort());
    }

    public void sendEmail(String to, String subject, String body) {
        if (!properties.isEnabled()) {
            System.out.println("[EMAIL] Email service disabled, skipping send");
            return;
        }

        System.out.println("[EMAIL] Sending email:");
        System.out.println("  From: " + properties.getFrom());
        System.out.println("  To: " + to);
        System.out.println("  Subject: " + subject);
        System.out.println("  Body: " + body);
        System.out.println("  [Simulated SMTP connection to " + properties.getHost() + "]");
    }

    public void sendTemplateEmail(String to, String template, Map<String, String> variables) {
        String body = processTemplate(template, variables);
        sendEmail(to, "Templated Email", body);
    }

    private String processTemplate(String template, Map<String, String> variables) {
        String result = template;
        for (Map.Entry<String, String> var : variables.entrySet()) {
            result = result.replace("{{" + var.getKey() + "}}", var.getValue());
        }
        return result;
    }
}

// 3. Auto-configuration class
@Configuration
@EnableConfigurationProperties({EmailProperties.class})
@AutoConfiguration
class EmailServiceAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public EmailService emailService(EmailProperties properties) {
        System.out.println("[AUTO-CONFIG] Creating EmailService bean");
        return new EmailService(properties);
    }
}

// Custom starter: Cache Service Starter

@ConfigurationProperties(prefix = "app.cache")
class CacheProperties {
    private String type = "memory";
    private int ttl = 3600;
    private int maxSize = 1000;

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public int getTtl() { return ttl; }
    public void setTtl(int ttl) { this.ttl = ttl; }

    public int getMaxSize() { return maxSize; }
    public void setMaxSize(int maxSize) { this.maxSize = maxSize; }
}

class CacheService {
    private CacheProperties properties;
    private Map<String, Object> cache = new HashMap<>();

    public CacheService(CacheProperties properties) {
        this.properties = properties;
        System.out.println("[CACHE] Cache service initialized");
        System.out.println("[CACHE] Type: " + properties.getType());
        System.out.println("[CACHE] TTL: " + properties.getTtl() + "s");
    }

    public void put(String key, Object value) {
        if (cache.size() >= properties.getMaxSize()) {
            System.out.println("[CACHE] Max size reached, evicting oldest entry");
            cache.remove(cache.keySet().iterator().next());
        }
        cache.put(key, value);
        System.out.println("[CACHE] Cached: " + key);
    }

    public Object get(String key) {
        Object value = cache.get(key);
        System.out.println("[CACHE] " + (value != null ? "HIT" : "MISS") + ": " + key);
        return value;
    }
}

@Configuration
@EnableConfigurationProperties({CacheProperties.class})
@AutoConfiguration
class CacheServiceAutoConfiguration {

    @Bean
    @ConditionalOnMissingBean
    public CacheService cacheService(CacheProperties properties) {
        System.out.println("[AUTO-CONFIG] Creating CacheService bean");
        return new CacheService(properties);
    }
}

// Application using custom starters
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Custom Starters ===\\n");

        // Simulate Spring Boot loading custom starters
        System.out.println("1. Loading custom starter configurations:");

        // Email starter
        EmailProperties emailProps = new EmailProperties();
        emailProps.setFrom("noreply@example.com");
        emailProps.setUsername("user@example.com");
        emailProps.setPassword("secret");

        EmailServiceAutoConfiguration emailConfig = new EmailServiceAutoConfiguration();
        EmailService emailService = emailConfig.emailService(emailProps);

        // Cache starter
        CacheProperties cacheProps = new CacheProperties();
        cacheProps.setMaxSize(100);

        CacheServiceAutoConfiguration cacheConfig = new CacheServiceAutoConfiguration();
        CacheService cacheService = cacheConfig.cacheService(cacheProps);

        // Use the services
        System.out.println("\\n2. Using email service:");
        emailService.sendEmail("user@example.com", "Welcome", "Hello from our app!");

        Map<String, String> vars = new HashMap<>();
        vars.put("name", "Alice");
        vars.put("product", "Premium Plan");
        emailService.sendTemplateEmail("alice@example.com",
            "Hi {{name}}, your {{product}} is ready!", vars);

        System.out.println("\\n3. Using cache service:");
        cacheService.put("user:1", "Alice");
        cacheService.put("user:2", "Bob");
        cacheService.get("user:1");
        cacheService.get("user:3");

        System.out.println("\\n=== Custom Starter Structure ===");
        System.out.println("\\nProject layout:");
        System.out.println("  my-email-spring-boot-starter/");
        System.out.println("    src/main/java/");
        System.out.println("      com/example/starter/email/");
        System.out.println("        EmailProperties.java");
        System.out.println("        EmailService.java");
        System.out.println("        EmailServiceAutoConfiguration.java");
        System.out.println("    src/main/resources/");
        System.out.println("      META-INF/");
        System.out.println("        spring.factories");
        System.out.println("    pom.xml");

        System.out.println("\\nspring.factories content:");
        System.out.println("  org.springframework.boot.autoconfigure.EnableAutoConfiguration=\\\\");
        System.out.println("    com.example.starter.email.EmailServiceAutoConfiguration");

        System.out.println("\\nNaming convention:");
        System.out.println("  - Third-party: xxx-spring-boot-starter");
        System.out.println("  - Official Spring: spring-boot-starter-xxx");

        System.out.println("\\nBest practices:");
        System.out.println("  - Use @ConfigurationProperties for configuration");
        System.out.println("  - Provide sensible defaults");
        System.out.println("  - Use @ConditionalOnMissingBean for override");
        System.out.println("  - Document all properties");
        System.out.println("  - Create autoconfigure module + starter module");
    }
}
""",

    845: """// Spring Boot: Logging Configuration
// In production: Uses Logback/Log4j2 via spring-boot-starter-logging
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.time.*;
import java.io.*;

// Simulated logging levels
enum LogLevel {
    TRACE, DEBUG, INFO, WARN, ERROR
}

// Simple logger interface
interface Logger {
    void trace(String message);
    void debug(String message);
    void info(String message);
    void warn(String message);
    void error(String message);
    void error(String message, Throwable t);
}

// Logger implementation
class SimpleLogger implements Logger {
    private String name;
    private LogLevel level;
    private List<LogAppender> appenders = new ArrayList<>();

    public SimpleLogger(String name, LogLevel level) {
        this.name = name;
        this.level = level;
    }

    public void addAppender(LogAppender appender) {
        appenders.add(appender);
    }

    private void log(LogLevel msgLevel, String message, Throwable t) {
        if (msgLevel.ordinal() >= level.ordinal()) {
            LogEvent event = new LogEvent(name, msgLevel, message, t, Instant.now());
            for (LogAppender appender : appenders) {
                appender.append(event);
            }
        }
    }

    public void trace(String message) { log(LogLevel.TRACE, message, null); }
    public void debug(String message) { log(LogLevel.DEBUG, message, null); }
    public void info(String message) { log(LogLevel.INFO, message, null); }
    public void warn(String message) { log(LogLevel.WARN, message, null); }
    public void error(String message) { log(LogLevel.ERROR, message, null); }
    public void error(String message, Throwable t) { log(LogLevel.ERROR, message, t); }
}

// Log event
class LogEvent {
    private String loggerName;
    private LogLevel level;
    private String message;
    private Throwable throwable;
    private Instant timestamp;

    public LogEvent(String loggerName, LogLevel level, String message, Throwable throwable, Instant timestamp) {
        this.loggerName = loggerName;
        this.level = level;
        this.message = message;
        this.throwable = throwable;
        this.timestamp = timestamp;
    }

    public String getLoggerName() { return loggerName; }
    public LogLevel getLevel() { return level; }
    public String getMessage() { return message; }
    public Throwable getThrowable() { return throwable; }
    public Instant getTimestamp() { return timestamp; }
}

// Log appender interface
interface LogAppender {
    void append(LogEvent event);
}

// Console appender
class ConsoleAppender implements LogAppender {
    private String pattern = "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n";

    public void append(LogEvent event) {
        String formatted = formatEvent(event);
        System.out.println(formatted);
    }

    private String formatEvent(LogEvent event) {
        return String.format("%s [%s] %-5s %s - %s",
            event.getTimestamp().toString().substring(11, 23),
            Thread.currentThread().getName(),
            event.getLevel(),
            event.getLoggerName(),
            event.getMessage());
    }
}

// File appender
class FileAppender implements LogAppender {
    private String filename;
    private List<String> buffer = new ArrayList<>();

    public FileAppender(String filename) {
        this.filename = filename;
    }

    public void append(LogEvent event) {
        String line = String.format("%s [%s] %s - %s",
            event.getTimestamp(),
            event.getLevel(),
            event.getLoggerName(),
            event.getMessage());
        buffer.add(line);
        System.out.println("[FILE] Writing to " + filename + ": " + line);
    }

    public int getBufferSize() {
        return buffer.size();
    }
}

// Logger factory
class LoggerFactory {
    private static Map<String, Logger> loggers = new HashMap<>();
    private static LogLevel defaultLevel = LogLevel.INFO;
    private static LogAppender defaultAppender = new ConsoleAppender();

    public static Logger getLogger(Class<?> clazz) {
        return getLogger(clazz.getName());
    }

    public static Logger getLogger(String name) {
        if (!loggers.containsKey(name)) {
            SimpleLogger logger = new SimpleLogger(name, defaultLevel);
            logger.addAppender(defaultAppender);
            loggers.put(name, logger);
        }
        return loggers.get(name);
    }

    public static void setDefaultLevel(LogLevel level) {
        defaultLevel = level;
    }

    public static void addAppender(LogAppender appender) {
        for (Logger logger : loggers.values()) {
            if (logger instanceof SimpleLogger) {
                ((SimpleLogger) logger).addAppender(appender);
            }
        }
    }
}

// Example service with logging
class OrderService {
    private static final Logger log = LoggerFactory.getLogger(OrderService.class);

    public void processOrder(String orderId, double amount) {
        log.info("Processing order: " + orderId);
        log.debug("Order amount: $" + amount);

        try {
            if (amount < 0) {
                log.warn("Invalid amount for order " + orderId + ": " + amount);
                throw new IllegalArgumentException("Amount cannot be negative");
            }

            log.info("Order " + orderId + " processed successfully");

        } catch (IllegalArgumentException e) {
            log.error("Failed to process order " + orderId, e);
        }
    }
}

public class Main {
    private static final Logger log = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Logging Configuration ===\\n");

        // Configure logging
        System.out.println("1. Default logging (INFO level):");
        OrderService service1 = new OrderService();
        service1.processOrder("ORD-001", 100.50);

        // Change log level to DEBUG
        System.out.println("\\n2. DEBUG level logging:");
        LoggerFactory.setDefaultLevel(LogLevel.DEBUG);
        OrderService service2 = new OrderService();
        service2.processOrder("ORD-002", 250.75);

        // Add file appender
        System.out.println("\\n3. Adding file appender:");
        FileAppender fileAppender = new FileAppender("application.log");
        LoggerFactory.addAppender(fileAppender);

        OrderService service3 = new OrderService();
        service3.processOrder("ORD-003", -50.00);

        System.out.println("\\nFile appender wrote " + fileAppender.getBufferSize() + " log entries");

        // Demonstrate different log levels
        System.out.println("\\n4. All log levels:");
        log.trace("This is a TRACE message (very detailed)");
        log.debug("This is a DEBUG message (development info)");
        log.info("This is an INFO message (general information)");
        log.warn("This is a WARN message (potential issues)");
        log.error("This is an ERROR message (actual errors)");

        System.out.println("\\n=== Spring Boot Logging Configuration ===");
        System.out.println("\\napplication.properties:");
        System.out.println("  # Root level");
        System.out.println("  logging.level.root=INFO");
        System.out.println("  ");
        System.out.println("  # Package-specific levels");
        System.out.println("  logging.level.com.example.myapp=DEBUG");
        System.out.println("  logging.level.org.springframework=WARN");
        System.out.println("  ");
        System.out.println("  # File output");
        System.out.println("  logging.file.name=application.log");
        System.out.println("  logging.file.path=/var/log");
        System.out.println("  ");
        System.out.println("  # Pattern");
        System.out.println("  logging.pattern.console=%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n");

        System.out.println("\\nlogback-spring.xml (advanced):");
        System.out.println("  - Rolling file appenders");
        System.out.println("  - Profile-specific configuration");
        System.out.println("  - Async appenders");
        System.out.println("  - Custom patterns");

        System.out.println("\\nBest practices:");
        System.out.println("  - Use SLF4J facade");
        System.out.println("  - Log at appropriate levels");
        System.out.println("  - Don't log sensitive data");
        System.out.println("  - Use parameterized logging");
        System.out.println("  - Configure log rotation");
    }
}
""",

    218: """// Spring Boot: Mini Project - REST API with CRUD Operations
// In production: Add spring-boot-starter-web dependency
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

// Simulated Spring annotations
@interface RestController {}
@interface RequestMapping { String value(); }
@interface GetMapping { String value() default ""; }
@interface PostMapping { String value() default ""; }
@interface PutMapping { String value() default ""; }
@interface DeleteMapping { String value() default ""; }
@interface PathVariable { String value() default ""; }
@interface RequestBody {}
@interface ResponseStatus { int value(); }

// Product entity
class Product {
    protected Long id;
    protected String name;
    protected String category;
    protected double price;
    protected int stock;

    public Product() {}

    public Product(Long id, String name, String category, double price, int stock) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
        this.stock = stock;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getCategory() { return category; }
    public String getPrice() { return String.format("%.2f", price); }
    public int getStock() { return stock; }
    public void setStock(int stock) { this.stock = stock; }
}

// Response wrapper
class ApiResponse<T> {
    private boolean success;
    private String message;
    private T data;

    public ApiResponse(boolean success, String message, T data) {
        this.success = success;
        this.message = message;
        this.data = data;
    }

    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "Success", data);
    }

    public static <T> ApiResponse<T> error(String message) {
        return new ApiResponse<>(false, message, null);
    }

    public boolean isSuccess() { return success; }
    public String getMessage() { return message; }
    public T getData() { return data; }
}

// Product service
class ProductService {
    private Map<Long, Product> products = new HashMap<>();
    private AtomicLong idCounter = new AtomicLong(1);

    public ProductService() {
        // Initialize with sample data
        createProduct(new Product(null, "Laptop", "Electronics", 999.99, 10));
        createProduct(new Product(null, "Mouse", "Electronics", 29.99, 50));
        createProduct(new Product(null, "Desk", "Furniture", 299.99, 5));
    }

    public List<Product> getAllProducts() {
        return new ArrayList<>(products.values());
    }

    public Optional<Product> getProductById(Long id) {
        return Optional.ofNullable(products.get(id));
    }

    public List<Product> getProductsByCategory(String category) {
        List<Product> result = new ArrayList<>();
        for (Product p : products.values()) {
            if (p.getCategory().equalsIgnoreCase(category)) {
                result.add(p);
            }
        }
        return result;
    }

    public Product createProduct(Product product) {
        product.setId(idCounter.getAndIncrement());
        products.put(product.getId(), product);
        return product;
    }

    public Optional<Product> updateProduct(Long id, Product updatedProduct) {
        if (!products.containsKey(id)) {
            return Optional.empty();
        }
        updatedProduct.setId(id);
        products.put(id, updatedProduct);
        return Optional.of(updatedProduct);
    }

    public boolean deleteProduct(Long id) {
        return products.remove(id) != null;
    }
}

// REST Controller
@RestController
@RequestMapping("/api/products")
class ProductController {
    private ProductService productService;

    public ProductController() {
        this.productService = new ProductService();
    }

    @GetMapping
    public ApiResponse<List<Product>> getAllProducts() {
        System.out.println("[GET /api/products] Fetching all products");
        List<Product> products = productService.getAllProducts();
        return ApiResponse.success(products);
    }

    @GetMapping("/{id}")
    public ApiResponse<Product> getProductById(@PathVariable("id") Long id) {
        System.out.println("[GET /api/products/" + id + "] Fetching product");
        Optional<Product> product = productService.getProductById(id);

        if (product.isPresent()) {
            return ApiResponse.success(product.get());
        } else {
            return ApiResponse.error("Product not found");
        }
    }

    @PostMapping
    @ResponseStatus(201)
    public ApiResponse<Product> createProduct(@RequestBody Product product) {
        System.out.println("[POST /api/products] Creating product: " + product.getName());
        Product created = productService.createProduct(product);
        return ApiResponse.success(created);
    }

    @PutMapping("/{id}")
    public ApiResponse<Product> updateProduct(@PathVariable("id") Long id, @RequestBody Product product) {
        System.out.println("[PUT /api/products/" + id + "] Updating product");
        Optional<Product> updated = productService.updateProduct(id, product);

        if (updated.isPresent()) {
            return ApiResponse.success(updated.get());
        } else {
            return ApiResponse.error("Product not found");
        }
    }

    @DeleteMapping("/{id}")
    public ApiResponse<String> deleteProduct(@PathVariable("id") Long id) {
        System.out.println("[DELETE /api/products/" + id + "] Deleting product");
        boolean deleted = productService.deleteProduct(id);

        if (deleted) {
            return ApiResponse.success("Product deleted");
        } else {
            return ApiResponse.error("Product not found");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot Mini Project: REST API ===\\n");

        ProductController controller = new ProductController();

        // Test GET all products
        System.out.println("1. GET /api/products:");
        ApiResponse<List<Product>> allProducts = controller.getAllProducts();
        System.out.println("   Found " + allProducts.getData().size() + " products\\n");

        // Test GET by ID
        System.out.println("2. GET /api/products/1:");
        ApiResponse<Product> product = controller.getProductById(1L);
        if (product.isSuccess()) {
            System.out.println("   Product: " + product.getData().getName() + " - $" + product.getData().getPrice());
        }

        // Test POST create
        System.out.println("\\n3. POST /api/products:");
        Product newProduct = new Product(null, "Keyboard", "Electronics", 79.99, 30);
        ApiResponse<Product> created = controller.createProduct(newProduct);
        System.out.println("   Created ID: " + created.getData().getId());

        // Test PUT update
        System.out.println("\\n4. PUT /api/products/1:");
        Product updateData = new Product(1L, "Gaming Laptop", "Electronics", 1299.99, 8);
        ApiResponse<Product> updated = controller.updateProduct(1L, updateData);
        System.out.println("   Updated: " + updated.getData().getName());

        // Test DELETE
        System.out.println("\\n5. DELETE /api/products/2:");
        ApiResponse<String> deleted = controller.deleteProduct(2L);
        System.out.println("   " + deleted.getMessage());

        // Verify final state
        System.out.println("\\n6. Final product count:");
        allProducts = controller.getAllProducts();
        System.out.println("   Total products: " + allProducts.getData().size());

        System.out.println("\\nProject demonstrates:");
        System.out.println("  - RESTful API design");
        System.out.println("  - CRUD operations (Create, Read, Update, Delete)");
        System.out.println("  - HTTP methods (GET, POST, PUT, DELETE)");
        System.out.println("  - Path variables and request body");
        System.out.println("  - Response wrapping with ApiResponse");
        System.out.println("  - In-memory data storage");
    }
}
""",

    1011: """// Spring Boot: Deploying Spring Boot JAR
// In production: Build with Maven/Gradle and deploy
// This lesson shows syntax only - requires actual Spring Boot in production

import java.util.*;
import java.io.*;

// Deployment configuration
class DeploymentConfig {
    private String environment;
    private String port;
    private String profile;
    private Map<String, String> systemProperties = new HashMap<>();

    public DeploymentConfig(String environment) {
        this.environment = environment;
        configureEnvironment();
    }

    private void configureEnvironment() {
        switch (environment) {
            case "dev":
                port = "8080";
                profile = "dev";
                systemProperties.put("spring.datasource.url", "jdbc:h2:mem:devdb");
                systemProperties.put("logging.level.root", "DEBUG");
                break;
            case "staging":
                port = "8080";
                profile = "staging";
                systemProperties.put("spring.datasource.url", "jdbc:postgresql://staging-db:5432/myapp");
                systemProperties.put("logging.level.root", "INFO");
                break;
            case "prod":
                port = "80";
                profile = "prod";
                systemProperties.put("spring.datasource.url", "jdbc:postgresql://prod-db:5432/myapp");
                systemProperties.put("logging.level.root", "WARN");
                break;
        }
    }

    public String getEnvironment() { return environment; }
    public String getPort() { return port; }
    public String getProfile() { return profile; }
    public Map<String, String> getSystemProperties() { return systemProperties; }
}

// Build configuration
class BuildConfig {
    private String artifact = "myapp";
    private String version = "1.0.0";
    private String mainClass = "com.example.Application";

    public String getJarName() {
        return artifact + "-" + version + ".jar";
    }

    public void printBuildCommand() {
        System.out.println("=== Build Command ===");
        System.out.println("Maven: mvn clean package");
        System.out.println("Gradle: ./gradlew bootJar");
        System.out.println("\\nOutput: target/" + getJarName());
    }
}

// Deployment manager
class DeploymentManager {
    private BuildConfig buildConfig;
    private DeploymentConfig deployConfig;

    public DeploymentManager(BuildConfig buildConfig, DeploymentConfig deployConfig) {
        this.buildConfig = buildConfig;
        this.deployConfig = deployConfig;
    }

    public void deploy() {
        System.out.println("\\n=== Deployment Process ===");
        System.out.println("Environment: " + deployConfig.getEnvironment());
        System.out.println("JAR: " + buildConfig.getJarName());
        System.out.println("Profile: " + deployConfig.getProfile());

        printPreChecks();
        printRunCommand();
        printSystemdService();
        printDockerDeployment();
        printHealthCheck();
    }

    private void printPreChecks() {
        System.out.println("\\n1. Pre-deployment checks:");
        System.out.println("   [OK] JAR file exists");
        System.out.println("   [OK] Java 11+ installed");
        System.out.println("   [OK] Required ports available");
        System.out.println("   [OK] Database connectivity");
    }

    private void printRunCommand() {
        System.out.println("\\n2. Run command:");
        System.out.print("   java -jar ");
        System.out.print(buildConfig.getJarName() + " ");
        System.out.print("--spring.profiles.active=" + deployConfig.getProfile() + " ");
        System.out.print("--server.port=" + deployConfig.getPort());
        System.out.println();

        System.out.println("\\n   With JVM options:");
        System.out.println("   java -Xms512m -Xmx2g -XX:+UseG1GC \\\\");
        System.out.println("        -jar " + buildConfig.getJarName() + " \\\\");
        System.out.println("        --spring.profiles.active=" + deployConfig.getProfile());
    }

    private void printSystemdService() {
        System.out.println("\\n3. Systemd service (/etc/systemd/system/myapp.service):");
        System.out.println("   [Unit]");
        System.out.println("   Description=My Spring Boot App");
        System.out.println("   After=syslog.target network.target");
        System.out.println("   ");
        System.out.println("   [Service]");
        System.out.println("   User=appuser");
        System.out.println("   ExecStart=/usr/bin/java -jar /opt/myapp/" + buildConfig.getJarName());
        System.out.println("   SuccessExitStatus=143");
        System.out.println("   Restart=always");
        System.out.println("   RestartSec=10");
        System.out.println("   ");
        System.out.println("   [Install]");
        System.out.println("   WantedBy=multi-user.target");
    }

    private void printDockerDeployment() {
        System.out.println("\\n4. Docker deployment:");
        System.out.println("   FROM eclipse-temurin:17-jre");
        System.out.println("   COPY target/" + buildConfig.getJarName() + " /app.jar");
        System.out.println("   EXPOSE " + deployConfig.getPort());
        System.out.println("   ENTRYPOINT [\"java\", \"-jar\", \"/app.jar\"]");
        System.out.println("   ");
        System.out.println("   Build: docker build -t myapp:1.0.0 .");
        System.out.println("   Run: docker run -p " + deployConfig.getPort() + ":8080 myapp:1.0.0");
    }

    private void printHealthCheck() {
        System.out.println("\\n5. Health check:");
        System.out.println("   curl http://localhost:" + deployConfig.getPort() + "/actuator/health");
        System.out.println("   Expected: {\"status\":\"UP\"}");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Spring Boot: Deployment Guide ===\\n");

        BuildConfig buildConfig = new BuildConfig();
        buildConfig.printBuildCommand();

        // Deploy to different environments
        String[] environments = {"dev", "staging", "prod"};

        for (String env : environments) {
            DeploymentConfig deployConfig = new DeploymentConfig(env);
            DeploymentManager manager = new DeploymentManager(buildConfig, deployConfig);
            manager.deploy();
            System.out.println("\\n" + "=".repeat(60));
        }

        System.out.println("\\n=== Deployment Best Practices ===");
        System.out.println("\\n1. Configuration:");
        System.out.println("   - Use profiles (dev, staging, prod)");
        System.out.println("   - Externalize configuration");
        System.out.println("   - Use environment variables for secrets");

        System.out.println("\\n2. Monitoring:");
        System.out.println("   - Enable Spring Boot Actuator");
        System.out.println("   - Configure health checks");
        System.out.println("   - Set up application metrics");
        System.out.println("   - Implement distributed tracing");

        System.out.println("\\n3. Security:");
        System.out.println("   - Run as non-root user");
        System.out.println("   - Use HTTPS in production");
        System.out.println("   - Secure actuator endpoints");
        System.out.println("   - Keep dependencies updated");

        System.out.println("\\n4. Performance:");
        System.out.println("   - Tune JVM settings");
        System.out.println("   - Configure connection pools");
        System.out.println("   - Enable caching");
        System.out.println("   - Use async processing");
    }
}
"""
}

print("=" * 80)
print("UPGRADING SPRING BOOT CORE - BATCH 3")
print("IDs: 1017, 1016, 845, 218, 1011")
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
print("BATCH 3 COMPLETE!")
print("=" * 80)
print(f"\nUpgraded {len(results)} Spring Boot Core lessons")

for lesson_id, title, old_len, new_len, growth, pct in results:
    print(f"  ID {lesson_id:4d}: {title[:50]:50s} | +{growth:5,} chars ({pct:5.1f}%)")
