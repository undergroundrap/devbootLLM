#!/usr/bin/env python3
"""
Upgrade OAuth2 and Spring Cloud lessons (Batch 10)
Upgrades 4 final high-priority framework lessons with production-ready Java simulations
"""

import json
import sys
from pathlib import Path

def create_oauth2_resource_server_solution():
    """ID 808: OAuth2 Resource Server - Production-ready simulation"""
    return '''import java.util.*;
import java.time.Instant;

// In production: import org.springframework.security.oauth2.server.resource.authentication.*;
// In production: import org.springframework.security.oauth2.jwt.*;
// In production: import org.springframework.security.access.prepost.PreAuthorize;

class OAuth2ResourceServerSimulation {
    public static void main(String[] args) {
        System.out.println("=== OAuth2 Resource Server Simulation ===\\n");

        // Simulate resource server protecting API endpoints
        ResourceServerConfig config = new ResourceServerConfig();
        JwtTokenValidator validator = new JwtTokenValidator(config);
        ApiController controller = new ApiController(validator);

        // Test 1: Valid JWT with read scope
        String validReadToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIiwic2NvcGUiOiJyZWFkIiwiZXhwIjoxOTAwMDAwMDAwfQ.signature";
        controller.handleGetRequest(validReadToken);

        // Test 2: Valid JWT with write scope
        String validWriteToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyNDU2Iiwic2NvcGUiOiJ3cml0ZSIsImV4cCI6MTkwMDAwMDAwMH0.signature";
        controller.handlePostRequest(validWriteToken);

        // Test 3: Invalid token (expired)
        String expiredToken = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyNzg5Iiwic2NvcGUiOiJyZWFkIiwiZXhwIjoxNTAwMDAwMDAwfQ.signature";
        controller.handleGetRequest(expiredToken);

        // Test 4: Insufficient scope
        controller.handleDeleteRequest(validReadToken);

        // Test 5: Token introspection
        System.out.println("\\n=== Token Introspection ===");
        validator.introspectToken(validWriteToken);

        // Production deployment info
        System.out.println("\\n=== Production Deployment ===");
        System.out.println("1. Configure JWT decoder with public key");
        System.out.println("2. Set issuer URI for token validation");
        System.out.println("3. Enable method security for @PreAuthorize");
        System.out.println("4. Configure CORS for cross-origin requests");
        System.out.println("5. Use HTTPS only in production");
        System.out.println("6. Implement token revocation checking");
    }
}

class ResourceServerConfig {
    private final String issuerUri;
    private final String audience;
    private final Set<String> allowedScopes;

    public ResourceServerConfig() {
        // In production: Load from application.yml
        this.issuerUri = "https://auth.example.com/oauth2";
        this.audience = "api.example.com";
        this.allowedScopes = new HashSet<>(Arrays.asList("read", "write", "delete", "admin"));
    }

    public String getIssuerUri() { return issuerUri; }
    public String getAudience() { return audience; }
    public Set<String> getAllowedScopes() { return allowedScopes; }
}

class JwtTokenValidator {
    private final ResourceServerConfig config;

    public JwtTokenValidator(ResourceServerConfig config) {
        this.config = config;
    }

    public JwtClaims validateToken(String token) {
        System.out.println("\\n[VALIDATION] Validating JWT token...");

        // Simulate JWT parsing (base64 decode)
        String[] parts = token.split("\\\\.");
        if (parts.length != 3) {
            System.out.println("[ERROR] Invalid token format");
            return null;
        }

        // Simulate header and payload decoding
        String payload = parts[1];
        JwtClaims claims = parsePayload(payload);

        // Validate expiration
        if (claims.getExpiration() < Instant.now().getEpochSecond()) {
            System.out.println("[ERROR] Token expired at " +
                new Date(claims.getExpiration() * 1000));
            return null;
        }

        // Validate issuer
        if (!config.getIssuerUri().equals(claims.getIssuer())) {
            System.out.println("[ERROR] Invalid issuer: " + claims.getIssuer());
            return null;
        }

        // In production: Verify signature with public key
        System.out.println("[SUCCESS] Token validated successfully");
        System.out.println("  Subject: " + claims.getSubject());
        System.out.println("  Scopes: " + String.join(", ", claims.getScopes()));
        System.out.println("  Expires: " + new Date(claims.getExpiration() * 1000));

        return claims;
    }

    public void introspectToken(String token) {
        JwtClaims claims = validateToken(token);
        if (claims == null) return;

        System.out.println("\\n[INTROSPECTION] Token details:");
        System.out.println("  Active: true");
        System.out.println("  Subject: " + claims.getSubject());
        System.out.println("  Scopes: " + String.join(", ", claims.getScopes()));
        System.out.println("  Issuer: " + claims.getIssuer());
        System.out.println("  Audience: " + claims.getAudience());
        System.out.println("  Issued At: " + new Date(claims.getIssuedAt() * 1000));
        System.out.println("  Expires At: " + new Date(claims.getExpiration() * 1000));
        System.out.println("  Time to Live: " +
            (claims.getExpiration() - Instant.now().getEpochSecond()) + " seconds");
    }

    private JwtClaims parsePayload(String payload) {
        // Simplified payload parsing simulation
        // In production: Use JWT library for proper parsing
        JwtClaims claims = new JwtClaims();

        if (payload.contains("user123")) {
            claims.setSubject("user123");
            claims.setScopes(Arrays.asList("read"));
            claims.setExpiration(1900000000L);
        } else if (payload.contains("user456")) {
            claims.setSubject("user456");
            claims.setScopes(Arrays.asList("write", "read"));
            claims.setExpiration(1900000000L);
        } else if (payload.contains("user789")) {
            claims.setSubject("user789");
            claims.setScopes(Arrays.asList("read"));
            claims.setExpiration(1500000000L); // Expired
        }

        claims.setIssuer(config.getIssuerUri());
        claims.setAudience(config.getAudience());
        claims.setIssuedAt(Instant.now().getEpochSecond() - 3600);

        return claims;
    }
}

class JwtClaims {
    private String subject;
    private List<String> scopes;
    private long expiration;
    private String issuer;
    private String audience;
    private long issuedAt;

    public String getSubject() { return subject; }
    public void setSubject(String subject) { this.subject = subject; }

    public List<String> getScopes() { return scopes; }
    public void setScopes(List<String> scopes) { this.scopes = scopes; }

    public long getExpiration() { return expiration; }
    public void setExpiration(long expiration) { this.expiration = expiration; }

    public String getIssuer() { return issuer; }
    public void setIssuer(String issuer) { this.issuer = issuer; }

    public String getAudience() { return audience; }
    public void setAudience(String audience) { this.audience = audience; }

    public long getIssuedAt() { return issuedAt; }
    public void setIssuedAt(long issuedAt) { this.issuedAt = issuedAt; }

    public boolean hasScope(String scope) {
        return scopes != null && scopes.contains(scope);
    }
}

class ApiController {
    private final JwtTokenValidator validator;

    public ApiController(JwtTokenValidator validator) {
        this.validator = validator;
    }

    // In production: @PreAuthorize("hasAuthority('SCOPE_read')")
    public void handleGetRequest(String token) {
        System.out.println("\\n=== GET /api/resources ===");
        JwtClaims claims = validator.validateToken(token);

        if (claims == null) {
            System.out.println("[DENIED] Invalid or expired token");
            return;
        }

        if (!claims.hasScope("read") && !claims.hasScope("admin")) {
            System.out.println("[DENIED] Insufficient scope - requires 'read'");
            return;
        }

        System.out.println("[ALLOWED] Returning resources for user: " + claims.getSubject());
        System.out.println("Response: [{id:1, name:'Resource A'}, {id:2, name:'Resource B'}]");
    }

    // In production: @PreAuthorize("hasAuthority('SCOPE_write')")
    public void handlePostRequest(String token) {
        System.out.println("\\n=== POST /api/resources ===");
        JwtClaims claims = validator.validateToken(token);

        if (claims == null) {
            System.out.println("[DENIED] Invalid or expired token");
            return;
        }

        if (!claims.hasScope("write") && !claims.hasScope("admin")) {
            System.out.println("[DENIED] Insufficient scope - requires 'write'");
            return;
        }

        System.out.println("[ALLOWED] Creating resource for user: " + claims.getSubject());
        System.out.println("Response: {id:3, name:'New Resource', created:true}");
    }

    // In production: @PreAuthorize("hasAuthority('SCOPE_delete')")
    public void handleDeleteRequest(String token) {
        System.out.println("\\n=== DELETE /api/resources/1 ===");
        JwtClaims claims = validator.validateToken(token);

        if (claims == null) {
            System.out.println("[DENIED] Invalid or expired token");
            return;
        }

        if (!claims.hasScope("delete") && !claims.hasScope("admin")) {
            System.out.println("[DENIED] Insufficient scope - requires 'delete'");
            System.out.println("  User scopes: " + String.join(", ", claims.getScopes()));
            return;
        }

        System.out.println("[ALLOWED] Deleting resource for user: " + claims.getSubject());
    }
}'''

def create_config_encryption_solution():
    """ID 1021: Spring Cloud Config Encryption - Production-ready simulation"""
    return '''import java.util.*;
import javax.crypto.*;
import javax.crypto.spec.*;
import java.security.*;
import java.util.Base64;

// In production: import org.springframework.cloud.config.server.encryption.*;
// In production: import org.springframework.security.crypto.encrypt.*;

class ConfigEncryptionSimulation {
    public static void main(String[] args) {
        System.out.println("=== Spring Cloud Config Encryption Simulation ===\\n");

        // Initialize encryption service
        String encryptionKey = "MySecretEncryptionKey123!@#";
        ConfigEncryptionService encryptionService = new ConfigEncryptionService(encryptionKey);

        // Simulate Config Server with encrypted properties
        ConfigServer configServer = new ConfigServer(encryptionService);

        // Test 1: Store encrypted database password
        System.out.println("=== Storing Encrypted Configuration ===");
        configServer.storeProperty("spring.datasource.password", "SuperSecretDBPass123!");
        configServer.storeProperty("stripe.api.key", "sk_test_51AbCdEfGhIjK123456");
        configServer.storeProperty("jwt.signing.key", "MyJWTSigningSecretKey987654");

        // Test 2: Retrieve and decrypt properties
        System.out.println("\\n=== Retrieving Decrypted Configuration ===");
        Map<String, String> appConfig = configServer.getConfiguration("payment-service");
        appConfig.forEach((key, value) ->
            System.out.println("  " + key + " = " + maskSensitive(value)));

        // Test 3: Client-side decryption
        System.out.println("\\n=== Client-Side Decryption ===");
        ConfigClient client = new ConfigClient(encryptionService);
        client.loadConfiguration(configServer);

        // Test 4: Key rotation scenario
        System.out.println("\\n=== Key Rotation Scenario ===");
        String newKey = "NewRotatedEncryptionKey456$%^";
        configServer.rotateEncryptionKey(newKey);

        // Production deployment info
        System.out.println("\\n=== Production Best Practices ===");
        System.out.println("1. Store encryption key in secure vault (HashiCorp Vault, AWS KMS)");
        System.out.println("2. Use asymmetric encryption (RSA) for multi-environment");
        System.out.println("3. Rotate encryption keys regularly");
        System.out.println("4. Prefix encrypted values with {cipher} in properties");
        System.out.println("5. Enable server-side decryption for better security");
        System.out.println("6. Use environment-specific encryption keys");
        System.out.println("7. Audit all decryption operations");
    }

    private static String maskSensitive(String value) {
        if (value.length() <= 4) return "****";
        return value.substring(0, 2) + "****" + value.substring(value.length() - 2);
    }
}

class ConfigEncryptionService {
    private String encryptionKey;
    private final String ALGORITHM = "AES";
    private final String TRANSFORMATION = "AES/ECB/PKCS5Padding";

    public ConfigEncryptionService(String encryptionKey) {
        this.encryptionKey = padKey(encryptionKey);
    }

    public String encrypt(String plainText) {
        try {
            System.out.println("[ENCRYPT] Encrypting sensitive value...");

            // In production: Use Spring Security Encryptors
            SecretKeySpec keySpec = new SecretKeySpec(
                encryptionKey.getBytes(), ALGORITHM);
            Cipher cipher = Cipher.getInstance(TRANSFORMATION);
            cipher.init(Cipher.ENCRYPT_MODE, keySpec);

            byte[] encrypted = cipher.doFinal(plainText.getBytes());
            String encoded = Base64.getEncoder().encodeToString(encrypted);

            System.out.println("  Original: " + maskValue(plainText));
            System.out.println("  Encrypted: {cipher}" + encoded.substring(0, 20) + "...");

            return "{cipher}" + encoded;

        } catch (Exception e) {
            System.err.println("[ERROR] Encryption failed: " + e.getMessage());
            return null;
        }
    }

    public String decrypt(String encryptedText) {
        try {
            // Remove {cipher} prefix if present
            String cipherText = encryptedText.startsWith("{cipher}")
                ? encryptedText.substring(8)
                : encryptedText;

            System.out.println("[DECRYPT] Decrypting value...");

            SecretKeySpec keySpec = new SecretKeySpec(
                encryptionKey.getBytes(), ALGORITHM);
            Cipher cipher = Cipher.getInstance(TRANSFORMATION);
            cipher.init(Cipher.DECRYPT_MODE, keySpec);

            byte[] decoded = Base64.getDecoder().decode(cipherText);
            byte[] decrypted = cipher.doFinal(decoded);
            String plainText = new String(decrypted);

            System.out.println("  Decrypted: " + maskValue(plainText));

            return plainText;

        } catch (Exception e) {
            System.err.println("[ERROR] Decryption failed: " + e.getMessage());
            return null;
        }
    }

    public void rotateKey(String newKey) {
        System.out.println("[ROTATION] Rotating encryption key...");
        System.out.println("  Old key hash: " + hashKey(this.encryptionKey));
        this.encryptionKey = padKey(newKey);
        System.out.println("  New key hash: " + hashKey(this.encryptionKey));
    }

    private String padKey(String key) {
        // Pad or truncate to 16 bytes for AES-128
        if (key.length() < 16) {
            return String.format("%-16s", key).replace(' ', '0');
        }
        return key.substring(0, 16);
    }

    private String maskValue(String value) {
        if (value.length() <= 4) return "****";
        return value.substring(0, 2) + "****" + value.substring(value.length() - 2);
    }

    private String hashKey(String key) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hash = md.digest(key.getBytes());
            return Base64.getEncoder().encodeToString(hash).substring(0, 8);
        } catch (Exception e) {
            return "unknown";
        }
    }
}

class ConfigServer {
    private final ConfigEncryptionService encryptionService;
    private final Map<String, String> encryptedProperties;
    private int version;

    public ConfigServer(ConfigEncryptionService encryptionService) {
        this.encryptionService = encryptionService;
        this.encryptedProperties = new HashMap<>();
        this.version = 1;
    }

    public void storeProperty(String key, String value) {
        System.out.println("\\n[CONFIG-SERVER] Storing property: " + key);

        // Encrypt sensitive properties
        String encryptedValue = encryptionService.encrypt(value);
        encryptedProperties.put(key, encryptedValue);

        System.out.println("  Stored in repository as encrypted value");
        System.out.println("  Version: " + version);
    }

    public Map<String, String> getConfiguration(String applicationName) {
        System.out.println("\\n[CONFIG-SERVER] Fetching config for: " + applicationName);
        System.out.println("  Decrypting properties before sending...");

        Map<String, String> decryptedConfig = new HashMap<>();

        for (Map.Entry<String, String> entry : encryptedProperties.entrySet()) {
            String decryptedValue = encryptionService.decrypt(entry.getValue());
            decryptedConfig.put(entry.getKey(), decryptedValue);
        }

        System.out.println("  Config version: " + version);
        System.out.println("  Properties sent: " + decryptedConfig.size());

        return decryptedConfig;
    }

    public void rotateEncryptionKey(String newKey) {
        System.out.println("\\n[CONFIG-SERVER] Key Rotation Process");

        // Step 1: Decrypt all with old key
        Map<String, String> decryptedValues = new HashMap<>();
        for (Map.Entry<String, String> entry : encryptedProperties.entrySet()) {
            decryptedValues.put(entry.getKey(),
                encryptionService.decrypt(entry.getValue()));
        }

        // Step 2: Rotate key
        encryptionService.rotateKey(newKey);

        // Step 3: Re-encrypt all with new key
        encryptedProperties.clear();
        for (Map.Entry<String, String> entry : decryptedValues.entrySet()) {
            String encrypted = encryptionService.encrypt(entry.getValue());
            encryptedProperties.put(entry.getKey(), encrypted);
        }

        version++;
        System.out.println("  Re-encrypted " + encryptedProperties.size() + " properties");
        System.out.println("  New version: " + version);
    }
}

class ConfigClient {
    private final ConfigEncryptionService encryptionService;
    private Map<String, String> localConfig;

    public ConfigClient(ConfigEncryptionService encryptionService) {
        this.encryptionService = encryptionService;
        this.localConfig = new HashMap<>();
    }

    public void loadConfiguration(ConfigServer server) {
        System.out.println("[CONFIG-CLIENT] Loading configuration...");

        // In production: HTTP call to Config Server
        localConfig = server.getConfiguration("payment-service");

        System.out.println("  Loaded " + localConfig.size() + " properties");
        System.out.println("  Configuration ready for application use");
    }

    public String getProperty(String key) {
        return localConfig.get(key);
    }
}'''

def create_refresh_strategies_solution():
    """ID 1022: Spring Cloud Config Refresh Strategies - Production-ready simulation"""
    return '''import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

// In production: import org.springframework.cloud.context.refresh.ContextRefresher;
// In production: import org.springframework.cloud.context.scope.refresh.RefreshScope;
// In production: import org.springframework.cloud.endpoint.RefreshEndpoint;

class ConfigRefreshSimulation {
    public static void main(String[] args) {
        System.out.println("=== Spring Cloud Config Refresh Strategies Simulation ===\\n");

        // Initialize config server and clients
        ConfigServer configServer = new ConfigServer();
        configServer.updateProperty("rate.limit", "100");
        configServer.updateProperty("feature.newUI", "false");
        configServer.updateProperty("cache.ttl", "3600");

        // Create services with refresh capabilities
        RateLimiterService rateLimiter = new RateLimiterService();
        FeatureToggleService featureToggle = new FeatureToggleService();
        CacheService cacheService = new CacheService();

        // Register services with refresh scope
        RefreshScopeManager refreshManager = new RefreshScopeManager();
        refreshManager.register(rateLimiter);
        refreshManager.register(featureToggle);
        refreshManager.register(cacheService);

        // Load initial configuration
        rateLimiter.loadConfig(configServer);
        featureToggle.loadConfig(configServer);
        cacheService.loadConfig(configServer);

        // Test 1: Manual refresh via actuator endpoint
        System.out.println("\\n=== Test 1: Manual Refresh ===");
        simulateRequest(rateLimiter, featureToggle, cacheService);

        configServer.updateProperty("rate.limit", "200");
        configServer.updateProperty("feature.newUI", "true");

        System.out.println("\\n[ADMIN] Triggering /actuator/refresh endpoint...");
        refreshManager.triggerRefresh(configServer);

        simulateRequest(rateLimiter, featureToggle, cacheService);

        // Test 2: Bus refresh (broadcast to all instances)
        System.out.println("\\n=== Test 2: Bus Refresh (Broadcast) ===");
        configServer.updateProperty("cache.ttl", "7200");

        System.out.println("[ADMIN] Triggering /actuator/bus-refresh endpoint...");
        refreshManager.broadcastRefresh(configServer);

        // Test 3: Webhook refresh (Git commit trigger)
        System.out.println("\\n=== Test 3: Webhook Auto-Refresh ===");
        GitWebhookListener webhook = new GitWebhookListener(refreshManager, configServer);
        webhook.simulateGitCommit("rate.limit", "500");

        simulateRequest(rateLimiter, featureToggle, cacheService);

        // Test 4: Scheduled refresh strategy
        System.out.println("\\n=== Test 4: Scheduled Refresh ===");
        ScheduledRefreshStrategy scheduler = new ScheduledRefreshStrategy(
            refreshManager, configServer, 30);
        scheduler.performScheduledRefresh();

        // Production deployment info
        System.out.println("\\n=== Production Refresh Strategies ===");
        System.out.println("1. Manual: POST /actuator/refresh (single instance)");
        System.out.println("2. Bus: POST /actuator/bus-refresh (all instances)");
        System.out.println("3. Webhook: Git commit triggers refresh");
        System.out.println("4. Scheduled: @Scheduled periodic refresh");
        System.out.println("5. @RefreshScope: Beans recreated on refresh");
        System.out.println("6. Zero-downtime: Gradual rollout with health checks");
    }

    private static void simulateRequest(RateLimiterService rateLimiter,
                                       FeatureToggleService featureToggle,
                                       CacheService cacheService) {
        System.out.println("\\n[REQUEST] Processing user request...");
        System.out.println("  Rate limit: " + rateLimiter.getCurrentLimit() + " req/min");
        System.out.println("  New UI enabled: " + featureToggle.isNewUIEnabled());
        System.out.println("  Cache TTL: " + cacheService.getCacheTTL() + " seconds");
    }
}

class ConfigServer {
    private final Map<String, String> properties;
    private int version;
    private LocalDateTime lastModified;

    public ConfigServer() {
        this.properties = new HashMap<>();
        this.version = 1;
        this.lastModified = LocalDateTime.now();
    }

    public void updateProperty(String key, String value) {
        properties.put(key, value);
        version++;
        lastModified = LocalDateTime.now();
    }

    public Map<String, String> getProperties() {
        return new HashMap<>(properties);
    }

    public int getVersion() {
        return version;
    }

    public LocalDateTime getLastModified() {
        return lastModified;
    }
}

// In production: @RefreshScope
class RateLimiterService implements Refreshable {
    private int rateLimit;
    private int configVersion;

    // In production: @Value("${rate.limit}")
    public void loadConfig(ConfigServer server) {
        String value = server.getProperties().get("rate.limit");
        this.rateLimit = value != null ? Integer.parseInt(value) : 100;
        this.configVersion = server.getVersion();
    }

    @Override
    public void refresh(ConfigServer server) {
        int oldLimit = this.rateLimit;
        loadConfig(server);
        System.out.println("  [RateLimiter] Refreshed: " + oldLimit + " -> " + rateLimit);
    }

    public int getCurrentLimit() {
        return rateLimit;
    }

    @Override
    public String getName() {
        return "RateLimiterService";
    }
}

// In production: @RefreshScope
class FeatureToggleService implements Refreshable {
    private boolean newUIEnabled;
    private int configVersion;

    // In production: @Value("${feature.newUI}")
    public void loadConfig(ConfigServer server) {
        String value = server.getProperties().get("feature.newUI");
        this.newUIEnabled = Boolean.parseBoolean(value);
        this.configVersion = server.getVersion();
    }

    @Override
    public void refresh(ConfigServer server) {
        boolean oldValue = this.newUIEnabled;
        loadConfig(server);
        System.out.println("  [FeatureToggle] Refreshed: newUI " + oldValue + " -> " + newUIEnabled);
    }

    public boolean isNewUIEnabled() {
        return newUIEnabled;
    }

    @Override
    public String getName() {
        return "FeatureToggleService";
    }
}

// In production: @RefreshScope
class CacheService implements Refreshable {
    private int cacheTTL;
    private int configVersion;

    // In production: @Value("${cache.ttl}")
    public void loadConfig(ConfigServer server) {
        String value = server.getProperties().get("cache.ttl");
        this.cacheTTL = value != null ? Integer.parseInt(value) : 3600;
        this.configVersion = server.getVersion();
    }

    @Override
    public void refresh(ConfigServer server) {
        int oldTTL = this.cacheTTL;
        loadConfig(server);
        System.out.println("  [CacheService] Refreshed: TTL " + oldTTL + " -> " + cacheTTL);
    }

    public int getCacheTTL() {
        return cacheTTL;
    }

    @Override
    public String getName() {
        return "CacheService";
    }
}

interface Refreshable {
    void refresh(ConfigServer server);
    String getName();
}

class RefreshScopeManager {
    private final List<Refreshable> refreshableServices;
    private final DateTimeFormatter formatter;

    public RefreshScopeManager() {
        this.refreshableServices = new ArrayList<>();
        this.formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    }

    public void register(Refreshable service) {
        refreshableServices.add(service);
        System.out.println("[REFRESH-SCOPE] Registered: " + service.getName());
    }

    // In production: POST /actuator/refresh
    public void triggerRefresh(ConfigServer server) {
        System.out.println("[REFRESH] Single instance refresh triggered");
        System.out.println("  Time: " + LocalDateTime.now().format(formatter));
        System.out.println("  Config version: " + server.getVersion());

        refreshableServices.forEach(service -> service.refresh(server));

        System.out.println("  Refreshed " + refreshableServices.size() + " services");
    }

    // In production: POST /actuator/bus-refresh (with Spring Cloud Bus)
    public void broadcastRefresh(ConfigServer server) {
        System.out.println("[BUS-REFRESH] Broadcasting to all instances");
        System.out.println("  Time: " + LocalDateTime.now().format(formatter));

        // Simulate multiple instances
        String[] instances = {"instance-1", "instance-2", "instance-3"};

        for (String instance : instances) {
            System.out.println("\\n  [" + instance + "] Receiving refresh event...");
            refreshableServices.forEach(service -> service.refresh(server));
        }

        System.out.println("\\n  Broadcast completed to " + instances.length + " instances");
    }
}

class GitWebhookListener {
    private final RefreshScopeManager refreshManager;
    private final ConfigServer configServer;

    public GitWebhookListener(RefreshScopeManager refreshManager, ConfigServer configServer) {
        this.refreshManager = refreshManager;
        this.configServer = configServer;
    }

    // In production: @PostMapping("/webhook/git")
    public void simulateGitCommit(String property, String value) {
        System.out.println("[WEBHOOK] Git commit received");
        System.out.println("  Repository: config-repo");
        System.out.println("  Branch: main");
        System.out.println("  File: application.yml");
        System.out.println("  Changed: " + property + " = " + value);

        // Update config server
        configServer.updateProperty(property, value);

        // Trigger automatic refresh
        System.out.println("  Triggering automatic refresh...");
        refreshManager.broadcastRefresh(configServer);
    }
}

class ScheduledRefreshStrategy {
    private final RefreshScopeManager refreshManager;
    private final ConfigServer configServer;
    private final int intervalSeconds;

    public ScheduledRefreshStrategy(RefreshScopeManager refreshManager,
                                   ConfigServer configServer,
                                   int intervalSeconds) {
        this.refreshManager = refreshManager;
        this.configServer = configServer;
        this.intervalSeconds = intervalSeconds;
    }

    // In production: @Scheduled(fixedRate = 30000)
    public void performScheduledRefresh() {
        System.out.println("[SCHEDULED] Auto-refresh every " + intervalSeconds + " seconds");
        System.out.println("  Checking for config changes...");
        System.out.println("  Last modified: " + configServer.getLastModified());

        refreshManager.triggerRefresh(configServer);

        System.out.println("  Next refresh in " + intervalSeconds + " seconds");
    }
}'''

def create_service_mesh_solution():
    """ID 1023: Spring Cloud Service Mesh Integration - Production-ready simulation"""
    return '''import java.util.*;
import java.time.Duration;
import java.time.Instant;

// In production: import org.springframework.cloud.client.discovery.*;
// In production: import org.springframework.cloud.gateway.filter.*;
// In production: import org.springframework.cloud.circuitbreaker.*;
// In production: import io.istio.client.*;

class ServiceMeshSimulation {
    public static void main(String[] args) {
        System.out.println("=== Spring Cloud + Service Mesh Integration Simulation ===\\n");

        // Initialize service mesh control plane
        ServiceMeshControlPlane controlPlane = new ServiceMeshControlPlane();

        // Register services with sidecars
        MicroserviceInstance orderService = new MicroserviceInstance(
            "order-service", "10.0.1.10", 8080);
        MicroserviceInstance paymentService = new MicroserviceInstance(
            "payment-service", "10.0.1.20", 8080);
        MicroserviceInstance inventoryService = new MicroserviceInstance(
            "inventory-service", "10.0.1.30", 8080);

        controlPlane.registerService(orderService);
        controlPlane.registerService(paymentService);
        controlPlane.registerService(inventoryService);

        // Configure traffic management
        TrafficManager trafficManager = new TrafficManager();
        trafficManager.configureLoadBalancing("order-service", "ROUND_ROBIN");
        trafficManager.configureCanaryDeployment("payment-service", 0.10); // 10% canary

        // Test 1: Service discovery through mesh
        System.out.println("\\n=== Test 1: Service Discovery ===");
        ServiceClient client = new ServiceClient(controlPlane, trafficManager);
        client.discoverAndCall("order-service");

        // Test 2: Load balancing across instances
        System.out.println("\\n=== Test 2: Load Balancing ===");
        controlPlane.registerService(new MicroserviceInstance(
            "order-service", "10.0.1.11", 8080));
        controlPlane.registerService(new MicroserviceInstance(
            "order-service", "10.0.1.12", 8080));

        for (int i = 1; i <= 5; i++) {
            client.callService("order-service");
        }

        // Test 3: Circuit breaker integration
        System.out.println("\\n=== Test 3: Circuit Breaker ===");
        CircuitBreakerManager cbManager = new CircuitBreakerManager();
        cbManager.simulateFailures("payment-service");

        // Test 4: Canary deployment
        System.out.println("\\n=== Test 4: Canary Deployment ===");
        trafficManager.routeTraffic("payment-service", 20);

        // Test 5: Mutual TLS (mTLS)
        System.out.println("\\n=== Test 5: Mutual TLS ===");
        SecurityManager securityManager = new SecurityManager();
        securityManager.establishMTLS(orderService, paymentService);

        // Test 6: Observability
        System.out.println("\\n=== Test 6: Distributed Tracing ===");
        TracingManager tracingManager = new TracingManager();
        tracingManager.traceRequest("create-order-flow");

        // Production deployment info
        System.out.println("\\n=== Production Service Mesh Patterns ===");
        System.out.println("1. Istio: Full-featured service mesh");
        System.out.println("2. Linkerd: Lightweight, Kubernetes-native");
        System.out.println("3. Consul Connect: HashiCorp service mesh");
        System.out.println("4. AWS App Mesh: AWS-managed service mesh");
        System.out.println("5. Spring Cloud Gateway + Sidecar pattern");
        System.out.println("6. Automatic mTLS, retries, circuit breaking");
    }
}

class ServiceMeshControlPlane {
    private final Map<String, List<MicroserviceInstance>> serviceRegistry;
    private final Map<String, ServicePolicy> policies;

    public ServiceMeshControlPlane() {
        this.serviceRegistry = new HashMap<>();
        this.policies = new HashMap<>();
        System.out.println("[CONTROL-PLANE] Service mesh initialized");
    }

    public void registerService(MicroserviceInstance instance) {
        serviceRegistry.computeIfAbsent(
            instance.getServiceName(), k -> new ArrayList<>()).add(instance);

        System.out.println("[REGISTER] " + instance.getServiceName() +
            " @ " + instance.getHost() + ":" + instance.getPort());

        // Deploy sidecar proxy
        instance.deploySidecar();
    }

    public List<MicroserviceInstance> discoverService(String serviceName) {
        List<MicroserviceInstance> instances = serviceRegistry.get(serviceName);
        if (instances == null || instances.isEmpty()) {
            System.out.println("[DISCOVERY] No instances found for: " + serviceName);
            return Collections.emptyList();
        }

        System.out.println("[DISCOVERY] Found " + instances.size() +
            " instances of " + serviceName);
        return instances;
    }

    public void applyPolicy(String serviceName, ServicePolicy policy) {
        policies.put(serviceName, policy);
        System.out.println("[POLICY] Applied to " + serviceName + ": " + policy);
    }
}

class MicroserviceInstance {
    private final String serviceName;
    private final String host;
    private final int port;
    private SidecarProxy sidecar;
    private boolean healthy;

    public MicroserviceInstance(String serviceName, String host, int port) {
        this.serviceName = serviceName;
        this.host = host;
        this.port = port;
        this.healthy = true;
    }

    public void deploySidecar() {
        this.sidecar = new SidecarProxy(this);
        System.out.println("  [SIDECAR] Deployed Envoy proxy for " + serviceName);
    }

    public String getServiceName() { return serviceName; }
    public String getHost() { return host; }
    public int getPort() { return port; }
    public SidecarProxy getSidecar() { return sidecar; }
    public boolean isHealthy() { return healthy; }
    public void setHealthy(boolean healthy) { this.healthy = healthy; }

    @Override
    public String toString() {
        return serviceName + "@" + host + ":" + port;
    }
}

class SidecarProxy {
    private final MicroserviceInstance instance;
    private int requestCount;
    private int errorCount;

    public SidecarProxy(MicroserviceInstance instance) {
        this.instance = instance;
        this.requestCount = 0;
        this.errorCount = 0;
    }

    public void interceptRequest(String targetService) {
        requestCount++;
        System.out.println("  [SIDECAR] Intercepting request to " + targetService);
        System.out.println("    - Adding trace headers");
        System.out.println("    - Applying mTLS");
        System.out.println("    - Enforcing rate limits");
    }

    public void interceptResponse(boolean success) {
        if (!success) errorCount++;
        System.out.println("  [SIDECAR] Response intercepted");
        System.out.println("    - Success: " + success);
        System.out.println("    - Total requests: " + requestCount);
        System.out.println("    - Error rate: " +
            (requestCount > 0 ? (errorCount * 100.0 / requestCount) : 0) + "%");
    }
}

class TrafficManager {
    private final Map<String, String> loadBalancingStrategies;
    private final Map<String, CanaryConfig> canaryDeployments;
    private int requestCounter;

    public TrafficManager() {
        this.loadBalancingStrategies = new HashMap<>();
        this.canaryDeployments = new HashMap<>();
        this.requestCounter = 0;
    }

    public void configureLoadBalancing(String serviceName, String strategy) {
        loadBalancingStrategies.put(serviceName, strategy);
        System.out.println("[TRAFFIC] Load balancing for " + serviceName + ": " + strategy);
    }

    public void configureCanaryDeployment(String serviceName, double canaryPercent) {
        canaryDeployments.put(serviceName, new CanaryConfig(canaryPercent));
        System.out.println("[TRAFFIC] Canary deployment for " + serviceName +
            ": " + (canaryPercent * 100) + "% to new version");
    }

    public MicroserviceInstance selectInstance(List<MicroserviceInstance> instances) {
        if (instances.isEmpty()) return null;

        String strategy = loadBalancingStrategies.getOrDefault(
            instances.get(0).getServiceName(), "ROUND_ROBIN");

        switch (strategy) {
            case "ROUND_ROBIN":
                return instances.get(requestCounter++ % instances.size());
            case "RANDOM":
                return instances.get(new Random().nextInt(instances.size()));
            case "LEAST_CONNECTIONS":
                return instances.get(0); // Simplified
            default:
                return instances.get(0);
        }
    }

    public void routeTraffic(String serviceName, int requests) {
        CanaryConfig canary = canaryDeployments.get(serviceName);
        if (canary == null) return;

        int stableCount = 0;
        int canaryCount = 0;

        for (int i = 0; i < requests; i++) {
            if (Math.random() < canary.getCanaryPercent()) {
                canaryCount++;
            } else {
                stableCount++;
            }
        }

        System.out.println("[CANARY] Traffic split for " + requests + " requests:");
        System.out.println("  Stable version: " + stableCount + " (" +
            (stableCount * 100.0 / requests) + "%)");
        System.out.println("  Canary version: " + canaryCount + " (" +
            (canaryCount * 100.0 / requests) + "%)");
    }
}

class CanaryConfig {
    private final double canaryPercent;

    public CanaryConfig(double canaryPercent) {
        this.canaryPercent = canaryPercent;
    }

    public double getCanaryPercent() { return canaryPercent; }
}

class ServiceClient {
    private final ServiceMeshControlPlane controlPlane;
    private final TrafficManager trafficManager;

    public ServiceClient(ServiceMeshControlPlane controlPlane, TrafficManager trafficManager) {
        this.controlPlane = controlPlane;
        this.trafficManager = trafficManager;
    }

    public void discoverAndCall(String serviceName) {
        System.out.println("[CLIENT] Discovering service: " + serviceName);
        List<MicroserviceInstance> instances = controlPlane.discoverService(serviceName);

        if (!instances.isEmpty()) {
            MicroserviceInstance selected = trafficManager.selectInstance(instances);
            System.out.println("[CLIENT] Selected instance: " + selected);
            selected.getSidecar().interceptRequest(serviceName);
        }
    }

    public void callService(String serviceName) {
        List<MicroserviceInstance> instances = controlPlane.discoverService(serviceName);
        MicroserviceInstance selected = trafficManager.selectInstance(instances);

        if (selected != null) {
            System.out.println("  Routing to: " + selected.getHost());
        }
    }
}

class CircuitBreakerManager {
    private final Map<String, CircuitBreakerState> circuitBreakers;

    public CircuitBreakerManager() {
        this.circuitBreakers = new HashMap<>();
    }

    public void simulateFailures(String serviceName) {
        CircuitBreakerState cb = new CircuitBreakerState(serviceName);
        circuitBreakers.put(serviceName, cb);

        System.out.println("[CIRCUIT-BREAKER] Monitoring " + serviceName);

        // Simulate failures
        for (int i = 1; i <= 10; i++) {
            boolean success = i > 5; // First 5 fail
            cb.recordResult(success);

            if (cb.isOpen()) {
                System.out.println("  Request " + i + ": BLOCKED (circuit open)");
            } else {
                System.out.println("  Request " + i + ": " +
                    (success ? "SUCCESS" : "FAILED"));
            }
        }
    }
}

class CircuitBreakerState {
    private final String serviceName;
    private int failureCount;
    private int successCount;
    private boolean open;
    private static final int FAILURE_THRESHOLD = 5;

    public CircuitBreakerState(String serviceName) {
        this.serviceName = serviceName;
        this.failureCount = 0;
        this.successCount = 0;
        this.open = false;
    }

    public void recordResult(boolean success) {
        if (success) {
            successCount++;
            if (successCount >= 3) {
                open = false; // Close circuit
                failureCount = 0;
            }
        } else {
            failureCount++;
            if (failureCount >= FAILURE_THRESHOLD) {
                open = true; // Open circuit
                System.out.println("  [CIRCUIT-BREAKER] OPENED for " + serviceName);
            }
        }
    }

    public boolean isOpen() { return open; }
}

class SecurityManager {
    public void establishMTLS(MicroserviceInstance source, MicroserviceInstance target) {
        System.out.println("[SECURITY] Establishing mTLS connection");
        System.out.println("  Source: " + source.getServiceName());
        System.out.println("  Target: " + target.getServiceName());
        System.out.println("  [1] Source sidecar requests certificate");
        System.out.println("  [2] Control plane issues certificate");
        System.out.println("  [3] TLS handshake with mutual authentication");
        System.out.println("  [4] Encrypted channel established");
        System.out.println("  Certificate rotation: every 24 hours");
    }
}

class TracingManager {
    public void traceRequest(String flowName) {
        String traceId = UUID.randomUUID().toString().substring(0, 8);
        System.out.println("[TRACING] Starting trace: " + flowName);
        System.out.println("  Trace ID: " + traceId);

        // Simulate service calls
        traceSpan(traceId, "order-service", "createOrder", 45);
        traceSpan(traceId, "inventory-service", "checkStock", 23);
        traceSpan(traceId, "payment-service", "processPayment", 156);
        traceSpan(traceId, "order-service", "confirmOrder", 12);

        System.out.println("  Total duration: 236ms");
        System.out.println("  View in Jaeger UI: http://jaeger:16686/trace/" + traceId);
    }

    private void traceSpan(String traceId, String service, String operation, int durationMs) {
        String spanId = UUID.randomUUID().toString().substring(0, 8);
        System.out.println("  [" + service + "] " + operation +
            " (span: " + spanId + ", " + durationMs + "ms)");
    }
}

class ServicePolicy {
    private final String type;

    public ServicePolicy(String type) {
        this.type = type;
    }

    @Override
    public String toString() {
        return type;
    }
}'''

def main():
    """Main upgrade function"""
    print("=" * 70)
    print("OAuth2 & Spring Cloud Lessons Upgrade - Batch 10")
    print("Upgrading 4 final high-priority framework lessons")
    print("=" * 70)
    print()

    # File path
    lessons_file = Path(r'c:\devbootLLM-app\public\lessons-java.json')

    if not lessons_file.exists():
        print(f"ERROR: File not found: {lessons_file}")
        sys.exit(1)

    # Read JSON
    print("Reading lessons-java.json...")
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons_data = json.load(f)

    print(f"Total lessons: {len(lessons_data)}")
    print()

    # Target lesson IDs
    target_lessons = {
        808: create_oauth2_resource_server_solution(),
        1021: create_config_encryption_solution(),
        1022: create_refresh_strategies_solution(),
        1023: create_service_mesh_solution()
    }

    # Track changes
    updated_count = 0
    before_stats = []
    after_stats = []

    # Update lessons
    for lesson in lessons_data:
        lesson_id = lesson['id']

        if lesson_id in target_lessons:
            before_length = len(lesson['fullSolution'])
            lesson['fullSolution'] = target_lessons[lesson_id]
            after_length = len(lesson['fullSolution'])

            before_stats.append((lesson_id, lesson['title'], before_length))
            after_stats.append((lesson_id, lesson['title'], after_length))
            updated_count += 1

            print(f"Updated lesson {lesson_id}: {lesson['title'][:50]}")
            print(f"  Before: {before_length:,} chars")
            print(f"  After:  {after_length:,} chars")
            print(f"  Change: +{after_length - before_length:,} chars")
            print()

    # Save updated JSON
    print("Saving updated lessons-java.json...")
    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons_data, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 70)
    print("UPGRADE SUMMARY")
    print("=" * 70)
    print()

    # Summary table
    print("BEFORE:")
    print("-" * 70)
    for lesson_id, title, length in before_stats:
        print(f"  ID {lesson_id}: {title[:45]:45} {length:>6,} chars")

    print()
    print("AFTER:")
    print("-" * 70)
    for lesson_id, title, length in after_stats:
        print(f"  ID {lesson_id}: {title[:45]:45} {length:>6,} chars")

    print()
    print("=" * 70)
    print(f"Successfully upgraded {updated_count} lessons!")
    print()
    print("Lessons upgraded:")
    print("  - OAuth2 Resource Server (JWT validation & scopes)")
    print("  - Spring Cloud Config Encryption (secure properties)")
    print("  - Spring Cloud Refresh Strategies (zero-downtime updates)")
    print("  - Service Mesh Integration (Istio/Linkerd patterns)")
    print()
    print("Enterprise cloud-native stack complete!")
    print("=" * 70)

if __name__ == '__main__':
    main()
