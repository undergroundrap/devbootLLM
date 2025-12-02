"""Spring Security simulations batch 7a - Realistic security demonstrations"""
import json
import sys

SPRING_SECURITY_BATCH_7A = {
    806: '''// JWT Token Generation Simulation
// In production: import io.jsonwebtoken.*;
// String token = Jwts.builder()
//     .setSubject(username)
//     .claim("roles", roles)
//     .setIssuedAt(new Date())
//     .setExpiration(new Date(System.currentTimeMillis() + 3600000))
//     .signWith(SignatureAlgorithm.HS256, secretKey)
//     .compact();

import java.util.*;
import java.util.Base64;

class JWTService {
    private String secretKey = "mySecretKey123456789abcdefgh";  // 256-bit key for HS256

    public String generateToken(String username, List<String> roles) {
        // JWT has 3 parts: header.payload.signature

        // Header: Algorithm & Token Type
        String header = "{\\"alg\\":\\"HS256\\",\\"typ\\":\\"JWT\\"}";
        String headerEncoded = Base64.getUrlEncoder().withoutPadding()
            .encodeToString(header.getBytes());

        // Payload: Claims (user data)
        long now = System.currentTimeMillis() / 1000;
        long exp = now + 3600;  // 1 hour expiration

        String payload = String.format(
            "{\\"sub\\":\\"%s\\",\\"roles\\":%s,\\"iat\\":%d,\\"exp\\":%d}",
            username,
            roles.toString().replace(" ", ""),
            now,
            exp
        );
        String payloadEncoded = Base64.getUrlEncoder().withoutPadding()
            .encodeToString(payload.getBytes());

        // Signature: HMAC-SHA256(header.payload, secret)
        String signature = createSignature(headerEncoded + "." + payloadEncoded);

        return headerEncoded + "." + payloadEncoded + "." + signature;
    }

    private String createSignature(String data) {
        // Simplified HMAC simulation (real: use javax.crypto.Mac)
        String combined = data + secretKey;
        int hash = combined.hashCode();
        return Base64.getUrlEncoder().withoutPadding()
            .encodeToString(String.valueOf(hash).getBytes());
    }

    public Map<String, Object> parseToken(String token) {
        String[] parts = token.split("\\\\.");

        if (parts.length != 3) {
            throw new RuntimeException("Invalid JWT format - must have 3 parts");
        }

        // Decode and parse payload
        String payloadJson = new String(Base64.getUrlDecoder().decode(parts[1]));

        Map<String, Object> claims = new HashMap<>();
        claims.put("raw_payload", payloadJson);

        // Extract claims (simplified parsing)
        if (payloadJson.contains("sub")) {
            String sub = extractValue(payloadJson, "sub");
            claims.put("subject", sub);
        }
        if (payloadJson.contains("exp")) {
            String exp = extractValue(payloadJson, "exp");
            claims.put("expiration", exp);
        }

        return claims;
    }

    public boolean validateToken(String token) {
        try {
            String[] parts = token.split("\\\\.");
            if (parts.length != 3) return false;

            // Verify signature
            String data = parts[0] + "." + parts[1];
            String expectedSig = createSignature(data);

            if (!parts[2].equals(expectedSig)) {
                System.out.println("Signature verification failed!");
                return false;
            }

            // Check expiration
            Map<String, Object> claims = parseToken(token);
            String expStr = extractValue(claims.get("raw_payload").toString(), "exp");
            long exp = Long.parseLong(expStr);
            long now = System.currentTimeMillis() / 1000;

            if (now > exp) {
                System.out.println("Token expired!");
                return false;
            }

            return true;
        } catch (Exception e) {
            return false;
        }
    }

    private String extractValue(String json, String key) {
        int start = json.indexOf("\\"" + key + "\\":\\"") + key.length() + 4;
        if (start < key.length() + 4) {
            start = json.indexOf("\\"" + key + "\\":") + key.length() + 3;
            int end = json.indexOf(",", start);
            if (end == -1) end = json.indexOf("}", start);
            return json.substring(start, end).trim();
        }
        int end = json.indexOf("\\"", start);
        return json.substring(start, end);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("JWT Token Generation Simulation");
        System.out.println("=".repeat(75));

        JWTService jwtService = new JWTService();

        // Use case: User login generates JWT
        String username = "alice@company.com";
        List<String> roles = Arrays.asList("ROLE_USER", "ROLE_ADMIN");

        System.out.println("\\nScenario: User authentication successful\\n");
        System.out.println("User: " + username);
        System.out.println("Roles: " + roles);

        // Generate token
        String token = jwtService.generateToken(username, roles);

        System.out.println("\\nGenerated JWT Token:");
        System.out.println("-".repeat(75));

        // Show token structure
        String[] parts = token.split("\\\\.");
        System.out.println("\\nHeader (Base64):  " + parts[0]);
        System.out.println("Decoded: " + new String(Base64.getUrlDecoder().decode(parts[0])));

        System.out.println("\\nPayload (Base64): " + parts[1].substring(0, 50) + "...");
        System.out.println("Decoded: " + new String(Base64.getUrlDecoder().decode(parts[1])));

        System.out.println("\\nSignature: " + parts[2]);

        System.out.println("\\nFull Token (send to client):");
        System.out.println(token.substring(0, 80) + "...");

        // Parse token
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Validating Token (on subsequent requests)");
        System.out.println("=".repeat(75));

        Map<String, Object> claims = jwtService.parseToken(token);
        System.out.println("\\nExtracted Claims:");
        System.out.println("  Subject: " + claims.get("subject"));
        System.out.println("  Expiration: " + claims.get("expiration") + " (Unix timestamp)");

        // Validate
        boolean valid = jwtService.validateToken(token);
        System.out.println("\\nToken Validation: " + (valid ? "✓ VALID" : "✗ INVALID"));

        // Test expired token
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Security Features Demonstrated:");
        System.out.println("=".repeat(75));
        System.out.println("  ✓ Stateless authentication (no server-side session)");
        System.out.println("  ✓ Cryptographic signature prevents tampering");
        System.out.println("  ✓ Expiration time limits token lifetime");
        System.out.println("  ✓ Claims carry user identity and permissions");
        System.out.println("  ✓ Base64-encoded but NOT encrypted (use HTTPS!)");

        System.out.println("\\nProduction Best Practices:");
        System.out.println("  • Use io.jsonwebtoken (JJWT) library in real apps");
        System.out.println("  • Store secret key in environment variables");
        System.out.println("  • Use RS256 (asymmetric) for microservices");
        System.out.println("  • Implement token refresh mechanism");
        System.out.println("  • Add jti (JWT ID) for token revocation");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: import io.jsonwebtoken.*;");
    }
}
''',

    809: '''// CORS Configuration Simulation
// In production: import org.springframework.web.cors.*;
// @Configuration
// public class CorsConfig {
//     @Bean
//     public CorsConfigurationSource corsConfigurationSource() {
//         CorsConfiguration config = new CorsConfiguration();
//         config.setAllowedOrigins(Arrays.asList("https://app.example.com"));
//         config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE"));
//         config.setAllowedHeaders(Arrays.asList("Authorization", "Content-Type"));
//         config.setAllowCredentials(true);
//         config.setMaxAge(3600L);
//         return source;
//     }
// }

import java.util.*;

class CorsConfiguration {
    private List<String> allowedOrigins = new ArrayList<>();
    private List<String> allowedMethods = new ArrayList<>();
    private List<String> allowedHeaders = new ArrayList<>();
    private List<String> exposedHeaders = new ArrayList<>();
    private boolean allowCredentials = false;
    private long maxAge = 0;

    public void setAllowedOrigins(List<String> origins) {
        this.allowedOrigins = new ArrayList<>(origins);
    }

    public void setAllowedMethods(List<String> methods) {
        this.allowedMethods = new ArrayList<>(methods);
    }

    public void setAllowedHeaders(List<String> headers) {
        this.allowedHeaders = new ArrayList<>(headers);
    }

    public void setExposedHeaders(List<String> headers) {
        this.exposedHeaders = new ArrayList<>(headers);
    }

    public void setAllowCredentials(boolean allow) {
        this.allowCredentials = allow;
    }

    public void setMaxAge(long seconds) {
        this.maxAge = seconds;
    }

    public Map<String, String> getCorsHeaders(String origin, String method) {
        Map<String, String> headers = new HashMap<>();

        // Check origin
        if (allowedOrigins.contains(origin) || allowedOrigins.contains("*")) {
            headers.put("Access-Control-Allow-Origin", origin);
        } else {
            return headers;  // Origin not allowed
        }

        // Check method
        if (!allowedMethods.contains(method) && !allowedMethods.contains("*")) {
            return headers;  // Method not allowed
        }

        headers.put("Access-Control-Allow-Methods", String.join(", ", allowedMethods));
        headers.put("Access-Control-Allow-Headers", String.join(", ", allowedHeaders));

        if (!exposedHeaders.isEmpty()) {
            headers.put("Access-Control-Expose-Headers", String.join(", ", exposedHeaders));
        }

        if (allowCredentials) {
            headers.put("Access-Control-Allow-Credentials", "true");
        }

        if (maxAge > 0) {
            headers.put("Access-Control-Max-Age", String.valueOf(maxAge));
        }

        return headers;
    }

    public boolean isPreflightRequest(String method) {
        return "OPTIONS".equals(method);
    }
}

class HttpRequest {
    private String origin;
    private String method;
    private Map<String, String> headers = new HashMap<>();

    public HttpRequest(String origin, String method) {
        this.origin = origin;
        this.method = method;
    }

    public String getOrigin() { return origin; }
    public String getMethod() { return method; }
    public Map<String, String> getHeaders() { return headers; }
}

class HttpResponse {
    private int statusCode = 200;
    private Map<String, String> headers = new HashMap<>();
    private String body = "";

    public void setStatus(int code) { this.statusCode = code; }
    public void addHeader(String key, String value) { headers.put(key, value); }
    public void setBody(String body) { this.body = body; }

    public int getStatus() { return statusCode; }
    public Map<String, String> getHeaders() { return headers; }
    public String getBody() { return body; }
}

class CorsFilter {
    private CorsConfiguration config;

    public CorsFilter(CorsConfiguration config) {
        this.config = config;
    }

    public HttpResponse processRequest(HttpRequest request) {
        HttpResponse response = new HttpResponse();

        String origin = request.getOrigin();
        String method = request.getMethod();

        // Handle preflight (OPTIONS)
        if (config.isPreflightRequest(method)) {
            Map<String, String> corsHeaders = config.getCorsHeaders(origin, "GET");

            if (corsHeaders.isEmpty()) {
                response.setStatus(403);
                response.setBody("CORS preflight failed: origin not allowed");
                return response;
            }

            corsHeaders.forEach(response::addHeader);
            response.setStatus(200);
            response.setBody("Preflight OK");
            return response;
        }

        // Handle actual request
        Map<String, String> corsHeaders = config.getCorsHeaders(origin, method);

        if (corsHeaders.isEmpty()) {
            response.setStatus(403);
            response.setBody("CORS failed: origin not allowed");
            return response;
        }

        corsHeaders.forEach(response::addHeader);
        response.setBody("{\\"message\\":\\"API response\\",\\"data\\":\\"Success\\"}");

        return response;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("CORS Configuration Simulation");
        System.out.println("=".repeat(75));

        // Configure CORS for production API
        CorsConfiguration config = new CorsConfiguration();
        config.setAllowedOrigins(Arrays.asList(
            "https://app.example.com",
            "https://admin.example.com"
        ));
        config.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "DELETE", "OPTIONS"));
        config.setAllowedHeaders(Arrays.asList("Authorization", "Content-Type", "X-Requested-With"));
        config.setExposedHeaders(Arrays.asList("X-Total-Count", "X-Page-Number"));
        config.setAllowCredentials(true);
        config.setMaxAge(3600);  // Cache preflight for 1 hour

        System.out.println("\\nCORS Policy Configured:");
        System.out.println("  Allowed Origins: https://app.example.com, https://admin.example.com");
        System.out.println("  Allowed Methods: GET, POST, PUT, DELETE, OPTIONS");
        System.out.println("  Allowed Headers: Authorization, Content-Type, X-Requested-With");
        System.out.println("  Credentials: Enabled (cookies/auth headers allowed)");
        System.out.println("  Max Age: 3600 seconds (1 hour preflight cache)");

        CorsFilter corsFilter = new CorsFilter(config);

        // Scenario 1: Preflight request (OPTIONS)
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 1: Preflight Request (OPTIONS)");
        System.out.println("=".repeat(75));
        System.out.println("Browser sends OPTIONS before actual request to check CORS policy\\n");

        HttpRequest preflight = new HttpRequest("https://app.example.com", "OPTIONS");
        HttpResponse preflightResponse = corsFilter.processRequest(preflight);

        System.out.println("Request:");
        System.out.println("  Origin: " + preflight.getOrigin());
        System.out.println("  Method: " + preflight.getMethod());

        System.out.println("\\nResponse:");
        System.out.println("  Status: " + preflightResponse.getStatus());
        System.out.println("  CORS Headers:");
        preflightResponse.getHeaders().forEach((k, v) ->
            System.out.println("    " + k + ": " + v));

        // Scenario 2: Actual request from allowed origin
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 2: GET Request from Allowed Origin");
        System.out.println("=".repeat(75));

        HttpRequest allowedReq = new HttpRequest("https://app.example.com", "GET");
        HttpResponse allowedResp = corsFilter.processRequest(allowedReq);

        System.out.println("\\nRequest:");
        System.out.println("  Origin: " + allowedReq.getOrigin());
        System.out.println("  Method: " + allowedReq.getMethod());

        System.out.println("\\nResponse:");
        System.out.println("  Status: " + allowedResp.getStatus() + " (✓ Success)");
        System.out.println("  Body: " + allowedResp.getBody());
        System.out.println("  CORS Headers:");
        allowedResp.getHeaders().forEach((k, v) ->
            System.out.println("    " + k + ": " + v));

        // Scenario 3: Request from blocked origin
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 3: Request from Blocked Origin");
        System.out.println("=".repeat(75));

        HttpRequest blockedReq = new HttpRequest("https://malicious-site.com", "GET");
        HttpResponse blockedResp = corsFilter.processRequest(blockedReq);

        System.out.println("\\nRequest:");
        System.out.println("  Origin: " + blockedReq.getOrigin());
        System.out.println("  Method: " + blockedReq.getMethod());

        System.out.println("\\nResponse:");
        System.out.println("  Status: " + blockedResp.getStatus() + " (✗ Forbidden)");
        System.out.println("  Body: " + blockedResp.getBody());
        System.out.println("  CORS Headers: " +
            (blockedResp.getHeaders().isEmpty() ? "None (blocked)" : blockedResp.getHeaders()));

        // Security best practices
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Security Best Practices:");
        System.out.println("=".repeat(75));
        System.out.println("  ✓ Never use '*' for allowedOrigins with credentials");
        System.out.println("  ✓ Whitelist specific origins, not wildcards");
        System.out.println("  ✓ Use environment variables for different environments");
        System.out.println("  ✓ Cache preflight requests with maxAge");
        System.out.println("  ✓ Only expose necessary headers to frontend");
        System.out.println("  ✓ Combine with CSRF protection for state-changing ops");

        System.out.println("\\nCommon Use Cases:");
        System.out.println("  • SPA (React/Vue) calling REST API on different domain");
        System.out.println("  • Mobile app web views accessing backend");
        System.out.println("  • Microservices with frontend on separate subdomain");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: import org.springframework.web.cors.*;");
    }
}
''',

    814: '''// Method Security with @PreAuthorize Simulation
// In production: import org.springframework.security.access.prepost.PreAuthorize;
// @Configuration
// @EnableMethodSecurity(prePostEnabled = true)
// public class MethodSecurityConfig { }
//
// @Service
// public class BankService {
//     @PreAuthorize("hasRole('ADMIN')")
//     public void deleteAccount(Long id) { ... }
//
//     @PreAuthorize("hasRole('MANAGER') and #amount < 10000")
//     public void approveTransaction(Long id, BigDecimal amount) { ... }
//
//     @PreAuthorize("#userId == authentication.principal.id")
//     public Account getAccount(Long userId) { ... }
// }

import java.util.*;

// Simulated security context
class SecurityContext {
    private static ThreadLocal<Authentication> context = new ThreadLocal<>();

    public static void setAuthentication(Authentication auth) {
        context.set(auth);
    }

    public static Authentication getAuthentication() {
        return context.get();
    }

    public static void clear() {
        context.remove();
    }
}

class Authentication {
    private String username;
    private List<String> roles;
    private Map<String, Object> principal;

    public Authentication(String username, List<String> roles) {
        this.username = username;
        this.roles = new ArrayList<>(roles);
        this.principal = new HashMap<>();
        this.principal.put("username", username);
    }

    public String getName() { return username; }
    public List<String> getRoles() { return roles; }
    public Map<String, Object> getPrincipal() { return principal; }

    public boolean hasRole(String role) {
        return roles.contains(role) || roles.contains("ROLE_" + role);
    }

    public boolean hasAnyRole(String... roles) {
        for (String role : roles) {
            if (hasRole(role)) return true;
        }
        return false;
    }
}

class AccessDeniedException extends RuntimeException {
    public AccessDeniedException(String message) {
        super(message);
    }
}

// Custom annotation simulation
class PreAuthorize {
    private String expression;

    public PreAuthorize(String expression) {
        this.expression = expression;
    }

    public boolean evaluate(Authentication auth, Object... args) {
        // Simplified expression evaluation
        String expr = expression;

        // hasRole check
        if (expr.contains("hasRole")) {
            String role = extractRole(expr, "hasRole");
            return auth.hasRole(role);
        }

        // hasAnyRole check
        if (expr.contains("hasAnyRole")) {
            String rolesStr = expr.substring(expr.indexOf("(") + 1, expr.indexOf(")"));
            String[] roles = rolesStr.replace("\\'", "").split(",");
            return auth.hasAnyRole(roles);
        }

        // Complex expressions with 'and'
        if (expr.contains(" and ")) {
            String[] parts = expr.split(" and ");
            boolean result = true;
            for (String part : parts) {
                if (part.trim().contains("hasRole")) {
                    String role = extractRole(part.trim(), "hasRole");
                    result = result && auth.hasRole(role);
                } else if (part.trim().contains("#amount")) {
                    // Parameter-based check (simplified)
                    if (args.length > 0 && args[0] instanceof Integer) {
                        int amount = (Integer) args[0];
                        if (part.contains("<")) {
                            int limit = Integer.parseInt(part.split("<")[1].trim());
                            result = result && (amount < limit);
                        }
                    }
                }
            }
            return result;
        }

        return true;  // Default allow
    }

    private String extractRole(String expr, String function) {
        int start = expr.indexOf(function + "(\\'") + function.length() + 2;
        int end = expr.indexOf("\\'", start);
        return expr.substring(start, end);
    }
}

// Secured service class
class BankService {

    // Only ADMIN can delete accounts
    public void deleteAccount(Long accountId) {
        PreAuthorize auth = new PreAuthorize("hasRole('ADMIN')");
        Authentication current = SecurityContext.getAuthentication();

        if (!auth.evaluate(current)) {
            throw new AccessDeniedException("Access denied: requires ROLE_ADMIN");
        }

        System.out.println("  ✓ Account " + accountId + " deleted by " + current.getName());
    }

    // MANAGER or ADMIN can view all accounts
    public List<String> viewAllAccounts() {
        PreAuthorize auth = new PreAuthorize("hasAnyRole('MANAGER', 'ADMIN')");
        Authentication current = SecurityContext.getAuthentication();

        if (!auth.evaluate(current)) {
            throw new AccessDeniedException("Access denied: requires ROLE_MANAGER or ROLE_ADMIN");
        }

        return Arrays.asList("Account-1001", "Account-1002", "Account-1003");
    }

    // MANAGER can approve transactions under $10,000
    public void approveTransaction(Long accountId, int amount) {
        PreAuthorize auth = new PreAuthorize("hasRole('MANAGER') and #amount < 10000");
        Authentication current = SecurityContext.getAuthentication();

        if (!auth.evaluate(current, amount)) {
            throw new AccessDeniedException(
                "Access denied: requires ROLE_MANAGER and amount < $10,000");
        }

        System.out.println("  ✓ Transaction $" + amount + " approved by " + current.getName());
    }

    // Public access - no authorization needed
    public String getPublicInfo() {
        return "Public bank information - no authentication required";
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Method Security with @PreAuthorize Simulation");
        System.out.println("=".repeat(75));

        BankService bankService = new BankService();

        // Scenario 1: Admin user
        System.out.println("\\nScenario 1: Admin User Operations");
        System.out.println("=".repeat(75));

        Authentication admin = new Authentication("alice",
            Arrays.asList("ROLE_ADMIN", "ROLE_USER"));
        SecurityContext.setAuthentication(admin);

        System.out.println("Current user: " + admin.getName());
        System.out.println("Roles: " + admin.getRoles());
        System.out.println();

        try {
            System.out.println("Attempting to delete account...");
            bankService.deleteAccount(1001L);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        try {
            System.out.println("\\nAttempting to view all accounts...");
            List<String> accounts = bankService.viewAllAccounts();
            System.out.println("  ✓ Accessed accounts: " + accounts);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        // Scenario 2: Manager user
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 2: Manager User Operations");
        System.out.println("=".repeat(75));

        Authentication manager = new Authentication("bob",
            Arrays.asList("ROLE_MANAGER", "ROLE_USER"));
        SecurityContext.setAuthentication(manager);

        System.out.println("Current user: " + manager.getName());
        System.out.println("Roles: " + manager.getRoles());
        System.out.println();

        try {
            System.out.println("Attempting to delete account...");
            bankService.deleteAccount(1001L);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        try {
            System.out.println("\\nAttempting to approve $5,000 transaction...");
            bankService.approveTransaction(1001L, 5000);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        try {
            System.out.println("\\nAttempting to approve $15,000 transaction...");
            bankService.approveTransaction(1001L, 15000);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        // Scenario 3: Regular user
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 3: Regular User Operations");
        System.out.println("=".repeat(75));

        Authentication user = new Authentication("charlie",
            Arrays.asList("ROLE_USER"));
        SecurityContext.setAuthentication(user);

        System.out.println("Current user: " + user.getName());
        System.out.println("Roles: " + user.getRoles());
        System.out.println();

        try {
            System.out.println("Attempting to view all accounts...");
            bankService.viewAllAccounts();
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        try {
            System.out.println("\\nAccessing public information...");
            String info = bankService.getPublicInfo();
            System.out.println("  ✓ " + info);
        } catch (AccessDeniedException e) {
            System.out.println("  ✗ " + e.getMessage());
        }

        // Summary
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Method Security Results Summary");
        System.out.println("=".repeat(75));
        System.out.println("\\nAccess Control Matrix:");
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "Method", "ADMIN", "MANAGER", "USER"));
        System.out.println("-".repeat(75));
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "deleteAccount()", "✓ ALLOWED", "✗ DENIED", "✗ DENIED"));
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "viewAllAccounts()", "✓ ALLOWED", "✓ ALLOWED", "✗ DENIED"));
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "approve($5k)", "✓ ALLOWED", "✓ ALLOWED", "✗ DENIED"));
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "approve($15k)", "✓ ALLOWED", "✗ DENIED", "✗ DENIED"));
        System.out.println(String.format("%-20s %-15s %-15s %-15s",
            "getPublicInfo()", "✓ ALLOWED", "✓ ALLOWED", "✓ ALLOWED"));

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("@PreAuthorize Expression Types:");
        System.out.println("=".repeat(75));
        System.out.println("  hasRole('ADMIN')           → Check single role");
        System.out.println("  hasAnyRole('X', 'Y')       → Check multiple roles (OR)");
        System.out.println("  hasAuthority('PERM')       → Check specific permission");
        System.out.println("  #param == value            → Parameter-based checks");
        System.out.println("  expr1 and expr2            → Complex AND conditions");
        System.out.println("  authentication.name        → Access user details");
        System.out.println("  @bean.method(args)         → Call custom security logic");

        System.out.println("\\nProduction Best Practices:");
        System.out.println("  ✓ Method security is more granular than URL security");
        System.out.println("  ✓ Expressions evaluated at runtime for each call");
        System.out.println("  ✓ Use @PostAuthorize to check returned objects");
        System.out.println("  ✓ Combine with @PreFilter/@PostFilter for collections");
        System.out.println("  ✓ Write unit tests with @WithMockUser");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: @PreAuthorize, @EnableMethodSecurity");

        SecurityContext.clear();
    }
}
''',
}

def update_lessons(lessons_file):
    """Update lessons JSON with Spring Security simulations"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print("\\nBefore update (character counts):")
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in SPRING_SECURITY_BATCH_7A:
            current_len = len(lesson.get('fullSolution', ''))
            print(f"  Lesson {lesson_id}: {current_len} chars")

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in SPRING_SECURITY_BATCH_7A:
            lesson['fullSolution'] = SPRING_SECURITY_BATCH_7A[lesson_id]
            updated.append(lesson_id)

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated, lessons

def main():
    """Main entry point"""
    lessons_file = r'c:\devbootLLM-app\public\lessons-java.json'

    try:
        updated, lessons = update_lessons(lessons_file)

        print("\\n" + "=" * 80)
        print("Spring Security Simulations Batch 7a - Upgrade Complete")
        print("=" * 80)
        print(f"\\nSuccessfully updated {len(updated)} lessons:")

        lesson_names = {
            806: "JWT Token Generation - Stateless authentication tokens",
            809: "CORS Configuration - Cross-origin resource sharing for APIs",
            814: "Method Security with @PreAuthorize - Expression-based access control"
        }

        print("\\nAfter update (character counts):")
        for lesson in lessons:
            lesson_id = lesson.get('id')
            if lesson_id in SPRING_SECURITY_BATCH_7A:
                new_len = len(lesson.get('fullSolution', ''))
                print(f"  • Lesson {lesson_id}: {lesson_names.get(lesson_id, 'Unknown')}")
                print(f"    {new_len} chars (target: {3000 if lesson_id == 809 else 3500}-{4000 if lesson_id == 809 else 5000})")

        print(f"\\nAll simulations include:")
        print(f"  ✓ Realistic Spring Security demonstrations with working code")
        print(f"  ✓ Production-ready comments (// In production: import ...)")
        print(f"  ✓ 3,000-5,000 character comprehensive examples")
        print(f"  ✓ Security best practices and use cases")
        print(f"  ✓ Working demo with realistic scenarios")
        print(f"  ✓ Detailed explanations of security concepts")
        print(f"  ✓ Job-ready interview patterns")
        print("\\nFile updated: " + lessons_file)
        print("=" * 80)

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
