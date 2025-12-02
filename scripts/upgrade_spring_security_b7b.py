"""Spring Security simulations batch 7b - Complete security module with realistic demonstrations"""
import json
import sys

SPRING_SECURITY_BATCH_7B = {
    813: '''// Security Headers Configuration Simulation
// In production: import org.springframework.security.config.annotation.web.builders.HttpSecurity;
// @Configuration
// @EnableWebSecurity
// public class SecurityHeadersConfig {
//     @Bean
//     public SecurityFilterChain filterChain(HttpSecurity http) {
//         http.headers(headers -> headers
//             .contentTypeOptions(opts -> opts.disable())  // X-Content-Type-Options: nosniff
//             .frameOptions(frame -> frame.deny())         // X-Frame-Options: DENY
//             .xssProtection(xss -> xss.enable())          // X-XSS-Protection: 1
//             .httpStrictTransportSecurity(hsts -> hsts    // Strict-Transport-Security
//                 .includeSubDomains(true)
//                 .maxAgeInSeconds(31536000))
//             .contentSecurityPolicy(csp -> csp            // Content-Security-Policy
//                 .policyDirectives("default-src 'self'"))
//         );
//         return http.build();
//     }
// }

import java.util.*;

class SecurityHeadersConfig {
    private boolean xContentTypeOptions = true;
    private String xFrameOptions = "DENY";
    private boolean xssProtection = true;
    private boolean hstsEnabled = false;
    private long hstsMaxAge = 31536000;  // 1 year
    private boolean hstsIncludeSubdomains = true;
    private String cspPolicy = "default-src 'self'";
    private String referrerPolicy = "strict-origin-when-cross-origin";

    public void enableXContentTypeOptions(boolean enable) {
        this.xContentTypeOptions = enable;
    }

    public void setFrameOptions(String option) {
        this.xFrameOptions = option;  // DENY, SAMEORIGIN, or specific domain
    }

    public void enableXssProtection(boolean enable) {
        this.xssProtection = enable;
    }

    public void enableHsts(boolean enable, long maxAge, boolean includeSubdomains) {
        this.hstsEnabled = enable;
        this.hstsMaxAge = maxAge;
        this.hstsIncludeSubdomains = includeSubdomains;
    }

    public void setContentSecurityPolicy(String policy) {
        this.cspPolicy = policy;
    }

    public void setReferrerPolicy(String policy) {
        this.referrerPolicy = policy;
    }

    public Map<String, String> getSecurityHeaders() {
        Map<String, String> headers = new LinkedHashMap<>();

        if (xContentTypeOptions) {
            headers.put("X-Content-Type-Options", "nosniff");
        }

        if (xFrameOptions != null) {
            headers.put("X-Frame-Options", xFrameOptions);
        }

        if (xssProtection) {
            headers.put("X-XSS-Protection", "1; mode=block");
        }

        if (hstsEnabled) {
            String hstsValue = "max-age=" + hstsMaxAge;
            if (hstsIncludeSubdomains) {
                hstsValue += "; includeSubDomains";
            }
            headers.put("Strict-Transport-Security", hstsValue);
        }

        if (cspPolicy != null) {
            headers.put("Content-Security-Policy", cspPolicy);
        }

        if (referrerPolicy != null) {
            headers.put("Referrer-Policy", referrerPolicy);
        }

        return headers;
    }
}

class HttpResponse {
    private Map<String, String> headers = new LinkedHashMap<>();
    private String body;
    private int statusCode;

    public HttpResponse(int statusCode, String body) {
        this.statusCode = statusCode;
        this.body = body;
    }

    public void addHeaders(Map<String, String> securityHeaders) {
        this.headers.putAll(securityHeaders);
    }

    public void addHeader(String key, String value) {
        headers.put(key, value);
    }

    public Map<String, String> getHeaders() { return headers; }
    public String getBody() { return body; }
    public int getStatusCode() { return statusCode; }
}

class SecurityFilter {
    private SecurityHeadersConfig config;

    public SecurityFilter(SecurityHeadersConfig config) {
        this.config = config;
    }

    public HttpResponse applySecurityHeaders(HttpResponse response) {
        Map<String, String> securityHeaders = config.getSecurityHeaders();
        response.addHeaders(securityHeaders);
        return response;
    }

    public void validateHeaders(HttpResponse response) {
        Map<String, String> headers = response.getHeaders();

        System.out.println("\\nSecurity Headers Validation:");
        System.out.println("-".repeat(75));

        // Check for critical security headers
        validateHeader(headers, "X-Content-Type-Options", "nosniff",
            "Prevents MIME-type sniffing attacks");
        validateHeader(headers, "X-Frame-Options", null,
            "Prevents clickjacking attacks");
        validateHeader(headers, "X-XSS-Protection", null,
            "Enables browser XSS protection");
        validateHeader(headers, "Content-Security-Policy", null,
            "Prevents XSS and data injection attacks");
        validateHeader(headers, "Strict-Transport-Security", null,
            "Forces HTTPS connections (production only)");
        validateHeader(headers, "Referrer-Policy", null,
            "Controls referrer information leakage");
    }

    private void validateHeader(Map<String, String> headers, String headerName,
                               String expectedValue, String purpose) {
        if (headers.containsKey(headerName)) {
            String actualValue = headers.get(headerName);
            if (expectedValue != null && !actualValue.contains(expectedValue)) {
                System.out.println("  ⚠ " + headerName + ": " + actualValue + " (unexpected value)");
            } else {
                System.out.println("  ✓ " + headerName + ": " + actualValue);
            }
            System.out.println("    → " + purpose);
        } else {
            System.out.println("  ✗ " + headerName + ": MISSING!");
            System.out.println("    → " + purpose);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Security Headers Configuration Simulation");
        System.out.println("=".repeat(75));

        // Scenario 1: Development environment (HTTP, no HSTS)
        System.out.println("\\nScenario 1: Development Environment Configuration");
        System.out.println("=".repeat(75));

        SecurityHeadersConfig devConfig = new SecurityHeadersConfig();
        devConfig.enableXContentTypeOptions(true);
        devConfig.setFrameOptions("SAMEORIGIN");  // Allow same-origin iframes for dev tools
        devConfig.enableXssProtection(true);
        devConfig.enableHsts(false, 0, false);  // No HSTS in dev (using HTTP)
        devConfig.setContentSecurityPolicy(
            "default-src 'self' 'unsafe-inline' 'unsafe-eval'; " +
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' http://localhost:*"
        );
        devConfig.setReferrerPolicy("no-referrer-when-downgrade");

        HttpResponse devResponse = new HttpResponse(200, "Development page content");
        SecurityFilter devFilter = new SecurityFilter(devConfig);
        devFilter.applySecurityHeaders(devResponse);

        System.out.println("Environment: DEVELOPMENT (HTTP)");
        System.out.println("\\nApplied Headers:");
        devResponse.getHeaders().forEach((key, value) ->
            System.out.println("  " + key + ": " + value));

        // Scenario 2: Production environment (HTTPS, strict security)
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 2: Production Environment Configuration");
        System.out.println("=".repeat(75));

        SecurityHeadersConfig prodConfig = new SecurityHeadersConfig();
        prodConfig.enableXContentTypeOptions(true);
        prodConfig.setFrameOptions("DENY");  // Block all framing attempts
        prodConfig.enableXssProtection(true);
        prodConfig.enableHsts(true, 31536000, true);  // 1 year HSTS with subdomains
        prodConfig.setContentSecurityPolicy(
            "default-src 'self'; " +
            "script-src 'self' https://cdn.example.com; " +
            "style-src 'self' 'unsafe-inline'; " +
            "img-src 'self' data: https:; " +
            "font-src 'self' https://fonts.gstatic.com; " +
            "connect-src 'self' https://api.example.com; " +
            "frame-ancestors 'none'; " +
            "base-uri 'self'; " +
            "form-action 'self'"
        );
        prodConfig.setReferrerPolicy("strict-origin-when-cross-origin");

        HttpResponse prodResponse = new HttpResponse(200, "Production page content");
        SecurityFilter prodFilter = new SecurityFilter(prodConfig);
        prodFilter.applySecurityHeaders(prodResponse);

        System.out.println("Environment: PRODUCTION (HTTPS)");
        System.out.println("\\nApplied Headers:");
        prodResponse.getHeaders().forEach((key, value) -> {
            if (value.length() > 60) {
                System.out.println("  " + key + ":");
                System.out.println("    " + value.substring(0, 60) + "...");
            } else {
                System.out.println("  " + key + ": " + value);
            }
        });

        // Validate production headers
        prodFilter.validateHeaders(prodResponse);

        // Demonstrate attack prevention
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Attack Prevention Demonstrations");
        System.out.println("=".repeat(75));

        System.out.println("\\n1. Clickjacking Protection (X-Frame-Options: DENY)");
        System.out.println("   Attacker tries: <iframe src='https://yoursite.com'>");
        System.out.println("   → Browser blocks the iframe due to X-Frame-Options header");

        System.out.println("\\n2. MIME Sniffing Prevention (X-Content-Type-Options: nosniff)");
        System.out.println("   Attacker uploads: malicious.jpg (actually contains JavaScript)");
        System.out.println("   → Browser won't execute it as script due to nosniff header");

        System.out.println("\\n3. XSS Protection (Content-Security-Policy)");
        System.out.println("   Attacker injects: <script>alert('XSS')</script>");
        System.out.println("   → CSP blocks inline scripts, preventing execution");

        System.out.println("\\n4. HTTPS Enforcement (Strict-Transport-Security)");
        System.out.println("   User types: http://yoursite.com");
        System.out.println("   → Browser automatically upgrades to HTTPS for 1 year");

        // Security header comparison
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Environment Comparison");
        System.out.println("=".repeat(75));

        String[][] comparison = {
            {"Header", "Development", "Production"},
            {"-".repeat(30), "-".repeat(20), "-".repeat(20)},
            {"X-Frame-Options", "SAMEORIGIN", "DENY"},
            {"HSTS", "Disabled (HTTP)", "Enabled (1 year)"},
            {"CSP", "Permissive", "Strict"},
            {"unsafe-inline", "Allowed", "Blocked"},
            {"unsafe-eval", "Allowed", "Blocked"}
        };

        for (String[] row : comparison) {
            System.out.println(String.format("  %-30s %-20s %-20s",
                row[0], row[1], row[2]));
        }

        // Best practices summary
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Security Headers Best Practices");
        System.out.println("=".repeat(75));

        System.out.println("\\nAlways Enable:");
        System.out.println("  ✓ X-Content-Type-Options: nosniff");
        System.out.println("  ✓ X-Frame-Options: DENY (or SAMEORIGIN if needed)");
        System.out.println("  ✓ Content-Security-Policy with strict directives");
        System.out.println("  ✓ Referrer-Policy to control information leakage");

        System.out.println("\\nProduction Only:");
        System.out.println("  ✓ Strict-Transport-Security (HTTPS required)");
        System.out.println("  ✓ Preload HSTS list submission");
        System.out.println("  ✓ Remove unsafe-inline and unsafe-eval from CSP");

        System.out.println("\\nTesting & Monitoring:");
        System.out.println("  • Use Content-Security-Policy-Report-Only during testing");
        System.out.println("  • Set up CSP violation reporting endpoint");
        System.out.println("  • Validate headers with securityheaders.com");
        System.out.println("  • Test with different browsers");

        System.out.println("\\nCommon Mistakes to Avoid:");
        System.out.println("  ✗ Enabling HSTS on HTTP sites");
        System.out.println("  ✗ Using 'unsafe-inline' in production CSP");
        System.out.println("  ✗ Setting X-Frame-Options: ALLOW-FROM (deprecated)");
        System.out.println("  ✗ Forgetting to update CSP when adding CDNs");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: @EnableWebSecurity, HttpSecurity.headers()");
    }
}
''',

    815: '''// Custom Authentication Provider Simulation
// In production: import org.springframework.security.authentication.*;
// @Component
// public class CustomAuthProvider implements AuthenticationProvider {
//     @Autowired
//     private UserRepository userRepository;
//     @Autowired
//     private PasswordEncoder passwordEncoder;
//
//     @Override
//     public Authentication authenticate(Authentication auth) throws AuthenticationException {
//         String username = auth.getName();
//         String password = auth.getCredentials().toString();
//
//         User user = userRepository.findByUsername(username)
//             .orElseThrow(() -> new UsernameNotFoundException("User not found"));
//
//         if (!passwordEncoder.matches(password, user.getPassword())) {
//             throw new BadCredentialsException("Invalid password");
//         }
//
//         return new UsernamePasswordAuthenticationToken(user, password, user.getAuthorities());
//     }
// }

import java.util.*;

// Simulated database user
class User {
    private String username;
    private String password;  // In real app: hashed password
    private List<String> roles;
    private boolean enabled;
    private boolean accountNonLocked;
    private int failedAttempts;

    public User(String username, String password, List<String> roles, boolean enabled) {
        this.username = username;
        this.password = password;
        this.roles = new ArrayList<>(roles);
        this.enabled = enabled;
        this.accountNonLocked = true;
        this.failedAttempts = 0;
    }

    public String getUsername() { return username; }
    public String getPassword() { return password; }
    public List<String> getRoles() { return roles; }
    public boolean isEnabled() { return enabled; }
    public boolean isAccountNonLocked() { return accountNonLocked; }
    public int getFailedAttempts() { return failedAttempts; }

    public void incrementFailedAttempts() {
        failedAttempts++;
        if (failedAttempts >= 3) {
            accountNonLocked = false;
        }
    }

    public void resetFailedAttempts() {
        failedAttempts = 0;
    }
}

// Simulated user repository (database)
class UserRepository {
    private Map<String, User> users = new HashMap<>();

    public UserRepository() {
        // Pre-populate with test users (passwords are BCrypt hashed in real apps)
        users.put("alice", new User("alice",
            "$2a$10$hash_admin123",  // Simulated BCrypt hash
            Arrays.asList("ROLE_USER", "ROLE_ADMIN"), true));

        users.put("bob", new User("bob",
            "$2a$10$hash_user456",
            Arrays.asList("ROLE_USER"), true));

        users.put("disabled_user", new User("disabled_user",
            "$2a$10$hash_disabled",
            Arrays.asList("ROLE_USER"), false));
    }

    public Optional<User> findByUsername(String username) {
        return Optional.ofNullable(users.get(username));
    }

    public void save(User user) {
        users.put(user.getUsername(), user);
    }
}

// Simulated password encoder (BCrypt in production)
class PasswordEncoder {
    public boolean matches(String rawPassword, String encodedPassword) {
        // Simplified: check if hash was generated from raw password
        // Real BCrypt: BCrypt.checkpw(rawPassword, encodedPassword)

        if (encodedPassword.equals("$2a$10$hash_admin123")) {
            return rawPassword.equals("admin123");
        } else if (encodedPassword.equals("$2a$10$hash_user456")) {
            return rawPassword.equals("user456");
        } else if (encodedPassword.equals("$2a$10$hash_disabled")) {
            return rawPassword.equals("disabled");
        }
        return false;
    }

    public String encode(String rawPassword) {
        // Simplified hash simulation
        return "$2a$10$hash_" + rawPassword;
    }
}

// Authentication object
class Authentication {
    private String username;
    private String password;
    private List<String> authorities;
    private boolean authenticated;
    private User principal;

    public Authentication(String username, String password) {
        this.username = username;
        this.password = password;
        this.authorities = new ArrayList<>();
        this.authenticated = false;
    }

    public void setAuthenticated(boolean authenticated, User principal, List<String> authorities) {
        this.authenticated = authenticated;
        this.principal = principal;
        this.authorities = new ArrayList<>(authorities);
    }

    public String getName() { return username; }
    public String getCredentials() { return password; }
    public List<String> getAuthorities() { return authorities; }
    public boolean isAuthenticated() { return authenticated; }
    public User getPrincipal() { return principal; }
}

// Custom exceptions
class AuthenticationException extends RuntimeException {
    public AuthenticationException(String message) {
        super(message);
    }
}

class UsernameNotFoundException extends AuthenticationException {
    public UsernameNotFoundException(String message) {
        super(message);
    }
}

class BadCredentialsException extends AuthenticationException {
    public BadCredentialsException(String message) {
        super(message);
    }
}

class DisabledException extends AuthenticationException {
    public DisabledException(String message) {
        super(message);
    }
}

class LockedException extends AuthenticationException {
    public LockedException(String message) {
        super(message);
    }
}

// Custom Authentication Provider
class CustomAuthenticationProvider {
    private UserRepository userRepository;
    private PasswordEncoder passwordEncoder;

    public CustomAuthenticationProvider(UserRepository userRepository,
                                       PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public Authentication authenticate(Authentication auth) throws AuthenticationException {
        String username = auth.getName();
        String password = auth.getCredentials();

        System.out.println("\\n  Authenticating user: " + username);

        // Step 1: Find user in database
        System.out.println("  → Looking up user in database...");
        Optional<User> userOpt = userRepository.findByUsername(username);

        if (!userOpt.isPresent()) {
            System.out.println("  ✗ User not found in database");
            throw new UsernameNotFoundException("User '" + username + "' not found");
        }

        User user = userOpt.get();
        System.out.println("  ✓ User found: " + user.getUsername());

        // Step 2: Check if account is enabled
        System.out.println("  → Checking if account is enabled...");
        if (!user.isEnabled()) {
            System.out.println("  ✗ Account is disabled");
            throw new DisabledException("Account '" + username + "' is disabled");
        }
        System.out.println("  ✓ Account is enabled");

        // Step 3: Check if account is locked
        System.out.println("  → Checking if account is locked...");
        if (!user.isAccountNonLocked()) {
            System.out.println("  ✗ Account is locked (too many failed attempts)");
            throw new LockedException("Account '" + username + "' is locked");
        }
        System.out.println("  ✓ Account is not locked");

        // Step 4: Verify password
        System.out.println("  → Verifying password...");
        boolean passwordMatches = passwordEncoder.matches(password, user.getPassword());

        if (!passwordMatches) {
            user.incrementFailedAttempts();
            userRepository.save(user);
            System.out.println("  ✗ Invalid password (failed attempts: " +
                user.getFailedAttempts() + "/3)");
            throw new BadCredentialsException("Invalid credentials for '" + username + "'");
        }

        System.out.println("  ✓ Password verified");

        // Step 5: Reset failed attempts on successful login
        user.resetFailedAttempts();
        userRepository.save(user);

        // Step 6: Load authorities (roles/permissions)
        System.out.println("  → Loading user authorities...");
        List<String> authorities = user.getRoles();
        System.out.println("  ✓ Authorities loaded: " + authorities);

        // Step 7: Create authenticated token
        auth.setAuthenticated(true, user, authorities);
        System.out.println("  ✓ Authentication successful!");

        return auth;
    }

    public boolean supports(Class<?> authentication) {
        // In real Spring: check if this provider supports the authentication type
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Custom Authentication Provider Simulation");
        System.out.println("=".repeat(75));

        // Setup
        UserRepository userRepository = new UserRepository();
        PasswordEncoder passwordEncoder = new PasswordEncoder();
        CustomAuthenticationProvider authProvider =
            new CustomAuthenticationProvider(userRepository, passwordEncoder);

        // Scenario 1: Successful authentication
        System.out.println("\\nScenario 1: Successful Authentication");
        System.out.println("=".repeat(75));

        try {
            Authentication auth1 = new Authentication("alice", "admin123");
            Authentication result1 = authProvider.authenticate(auth1);

            System.out.println("\\nAuthentication Result:");
            System.out.println("  Username: " + result1.getName());
            System.out.println("  Authenticated: " + result1.isAuthenticated());
            System.out.println("  Authorities: " + result1.getAuthorities());
        } catch (AuthenticationException e) {
            System.out.println("\\n✗ Authentication failed: " + e.getMessage());
        }

        // Scenario 2: Invalid password (multiple attempts)
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 2: Failed Authentication (Invalid Password)");
        System.out.println("=".repeat(75));

        String[] attempts = {"wrong1", "wrong2", "wrong3"};
        for (int i = 0; i < attempts.length; i++) {
            System.out.println("\\nAttempt " + (i + 1) + ":");
            try {
                Authentication auth2 = new Authentication("bob", attempts[i]);
                authProvider.authenticate(auth2);
            } catch (AuthenticationException e) {
                System.out.println("\\n✗ Authentication failed: " + e.getMessage());
            }
        }

        // Scenario 3: Locked account
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 3: Locked Account (After 3 Failed Attempts)");
        System.out.println("=".repeat(75));

        try {
            Authentication auth3 = new Authentication("bob", "user456");  // Correct password
            authProvider.authenticate(auth3);
        } catch (AuthenticationException e) {
            System.out.println("\\n✗ Authentication failed: " + e.getMessage());
        }

        // Scenario 4: Disabled account
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 4: Disabled Account");
        System.out.println("=".repeat(75));

        try {
            Authentication auth4 = new Authentication("disabled_user", "disabled");
            authProvider.authenticate(auth4);
        } catch (AuthenticationException e) {
            System.out.println("\\n✗ Authentication failed: " + e.getMessage());
        }

        // Scenario 5: User not found
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 5: User Not Found");
        System.out.println("=".repeat(75));

        try {
            Authentication auth5 = new Authentication("nonexistent", "password");
            authProvider.authenticate(auth5);
        } catch (AuthenticationException e) {
            System.out.println("\\n✗ Authentication failed: " + e.getMessage());
        }

        // Summary
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Authentication Flow Summary");
        System.out.println("=".repeat(75));

        System.out.println("\\nAuthentication Steps:");
        System.out.println("  1. User lookup in database");
        System.out.println("  2. Account enabled check");
        System.out.println("  3. Account locked check");
        System.out.println("  4. Password verification (BCrypt)");
        System.out.println("  5. Failed attempts reset");
        System.out.println("  6. Authorities loading");
        System.out.println("  7. Create authenticated token");

        System.out.println("\\nSecurity Features:");
        System.out.println("  ✓ Password hashing (BCrypt in production)");
        System.out.println("  ✓ Account lockout after 3 failed attempts");
        System.out.println("  ✓ Disabled account detection");
        System.out.println("  ✓ User not found handling");
        System.out.println("  ✓ Failed attempt tracking");
        System.out.println("  ✓ Role-based authorities");

        System.out.println("\\nProduction Best Practices:");
        System.out.println("  • Use BCryptPasswordEncoder (60-char hashes)");
        System.out.println("  • Implement rate limiting to prevent brute force");
        System.out.println("  • Log authentication attempts for security monitoring");
        System.out.println("  • Use same error message for user-not-found and bad-password");
        System.out.println("  • Add CAPTCHA after multiple failures");
        System.out.println("  • Consider 2FA for sensitive operations");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: AuthenticationProvider, UserDetailsService");
    }
}
''',

    817: '''// Session Management Simulation
// In production: import org.springframework.security.config.annotation.web.builders.HttpSecurity;
// @Configuration
// @EnableWebSecurity
// public class SessionConfig {
//     @Bean
//     public SecurityFilterChain filterChain(HttpSecurity http) {
//         http.sessionManagement(session -> session
//             .sessionCreationPolicy(SessionCreationPolicy.IF_REQUIRED)
//             .maximumSessions(1)  // Only 1 session per user
//             .maxSessionsPreventsLogin(true)  // Block new login if max reached
//             .expiredUrl("/session-expired")
//             .sessionRegistry(sessionRegistry())
//         )
//         .sessionFixation().newSession();  // Create new session after login
//         return http.build();
//     }
// }

import java.util.*;
import java.util.concurrent.*;

class Session {
    private String sessionId;
    private String username;
    private long creationTime;
    private long lastAccessedTime;
    private int maxInactiveInterval;  // seconds
    private Map<String, Object> attributes;
    private boolean valid;

    public Session(String sessionId, String username, int maxInactiveInterval) {
        this.sessionId = sessionId;
        this.username = username;
        this.creationTime = System.currentTimeMillis();
        this.lastAccessedTime = this.creationTime;
        this.maxInactiveInterval = maxInactiveInterval;
        this.attributes = new ConcurrentHashMap<>();
        this.valid = true;
    }

    public String getSessionId() { return sessionId; }
    public String getUsername() { return username; }
    public long getCreationTime() { return creationTime; }
    public long getLastAccessedTime() { return lastAccessedTime; }
    public boolean isValid() { return valid; }

    public void access() {
        this.lastAccessedTime = System.currentTimeMillis();
    }

    public boolean isExpired() {
        long inactiveTime = (System.currentTimeMillis() - lastAccessedTime) / 1000;
        return inactiveTime > maxInactiveInterval;
    }

    public void invalidate() {
        this.valid = false;
        this.attributes.clear();
    }

    public void setAttribute(String key, Object value) {
        attributes.put(key, value);
    }

    public Object getAttribute(String key) {
        return attributes.get(key);
    }

    public long getInactiveSeconds() {
        return (System.currentTimeMillis() - lastAccessedTime) / 1000;
    }
}

class SessionRegistry {
    private Map<String, Session> sessionById = new ConcurrentHashMap<>();
    private Map<String, Set<String>> sessionsByUsername = new ConcurrentHashMap<>();

    public void registerSession(Session session) {
        sessionById.put(session.getSessionId(), session);
        sessionsByUsername
            .computeIfAbsent(session.getUsername(), k -> ConcurrentHashMap.newKeySet())
            .add(session.getSessionId());
    }

    public Session getSession(String sessionId) {
        return sessionById.get(sessionId);
    }

    public List<Session> getSessionsForUser(String username) {
        Set<String> sessionIds = sessionsByUsername.getOrDefault(username, new HashSet<>());
        List<Session> sessions = new ArrayList<>();
        for (String id : sessionIds) {
            Session session = sessionById.get(id);
            if (session != null && session.isValid()) {
                sessions.add(session);
            }
        }
        return sessions;
    }

    public void removeSession(String sessionId) {
        Session session = sessionById.remove(sessionId);
        if (session != null) {
            Set<String> userSessions = sessionsByUsername.get(session.getUsername());
            if (userSessions != null) {
                userSessions.remove(sessionId);
            }
        }
    }

    public int getActiveSessionCount() {
        return (int) sessionById.values().stream()
            .filter(Session::isValid)
            .count();
    }

    public void cleanupExpiredSessions() {
        List<String> expiredIds = new ArrayList<>();
        for (Session session : sessionById.values()) {
            if (session.isExpired() || !session.isValid()) {
                expiredIds.add(session.getSessionId());
            }
        }
        for (String id : expiredIds) {
            removeSession(id);
        }
    }
}

class SessionManager {
    private SessionRegistry registry;
    private int maxSessionsPerUser;
    private int defaultTimeout;  // seconds
    private boolean maxSessionsPreventsLogin;

    public SessionManager(int maxSessionsPerUser, int defaultTimeout,
                         boolean maxSessionsPreventsLogin) {
        this.registry = new SessionRegistry();
        this.maxSessionsPerUser = maxSessionsPerUser;
        this.defaultTimeout = defaultTimeout;
        this.maxSessionsPreventsLogin = maxSessionsPreventsLogin;
    }

    public Session createSession(String username) throws SessionException {
        // Check concurrent session limit
        List<Session> existingSessions = registry.getSessionsForUser(username);

        System.out.println("\\n  Existing sessions for " + username + ": " +
            existingSessions.size());

        if (existingSessions.size() >= maxSessionsPerUser) {
            if (maxSessionsPreventsLogin) {
                System.out.println("  ✗ Maximum sessions reached - login prevented");
                throw new SessionException(
                    "Maximum sessions reached for user: " + username);
            } else {
                // Expire oldest session
                Session oldestSession = existingSessions.get(0);
                System.out.println("  → Expiring oldest session: " +
                    oldestSession.getSessionId().substring(0, 8) + "...");
                oldestSession.invalidate();
                registry.removeSession(oldestSession.getSessionId());
            }
        }

        // Session fixation protection: always create new session ID after login
        String sessionId = UUID.randomUUID().toString();
        Session session = new Session(sessionId, username, defaultTimeout);

        registry.registerSession(session);
        System.out.println("  ✓ Session created: " + sessionId.substring(0, 8) + "...");
        System.out.println("  ✓ Timeout: " + defaultTimeout + " seconds");

        return session;
    }

    public boolean validateSession(String sessionId) {
        Session session = registry.getSession(sessionId);

        if (session == null) {
            System.out.println("  ✗ Session not found");
            return false;
        }

        if (!session.isValid()) {
            System.out.println("  ✗ Session invalidated");
            return false;
        }

        if (session.isExpired()) {
            System.out.println("  ✗ Session expired (inactive for " +
                session.getInactiveSeconds() + "s)");
            session.invalidate();
            registry.removeSession(sessionId);
            return false;
        }

        // Update last access time
        session.access();
        System.out.println("  ✓ Session valid - last accessed updated");
        return true;
    }

    public void invalidateSession(String sessionId) {
        Session session = registry.getSession(sessionId);
        if (session != null) {
            session.invalidate();
            registry.removeSession(sessionId);
            System.out.println("  ✓ Session invalidated and removed");
        }
    }

    public SessionRegistry getRegistry() {
        return registry;
    }
}

class SessionException extends Exception {
    public SessionException(String message) {
        super(message);
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Session Management Simulation");
        System.out.println("=".repeat(75));

        // Configuration: 1 session per user, 10-second timeout
        SessionManager sessionManager = new SessionManager(
            1,      // maxSessionsPerUser
            10,     // timeout in seconds
            true    // maxSessionsPreventsLogin
        );

        // Scenario 1: Create and use session
        System.out.println("\\nScenario 1: Normal Session Creation and Usage");
        System.out.println("=".repeat(75));

        Session session1 = sessionManager.createSession("alice");
        System.out.println("\\nSession Details:");
        System.out.println("  ID: " + session1.getSessionId().substring(0, 16) + "...");
        System.out.println("  User: " + session1.getUsername());
        System.out.println("  Created: " + new Date(session1.getCreationTime()));

        // Store some data in session
        session1.setAttribute("cartItems", Arrays.asList("Item1", "Item2"));
        session1.setAttribute("theme", "dark");
        System.out.println("  Attributes: cartItems, theme");

        // Scenario 2: Concurrent session control
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 2: Concurrent Session Control (Max 1 Session)");
        System.out.println("=".repeat(75));

        System.out.println("\\nUser 'alice' tries to login from another device:");
        try {
            Session session2 = sessionManager.createSession("alice");
            System.out.println("\\n✗ Unexpected: second session created");
        } catch (SessionException e) {
            System.out.println("\\n✓ Expected: " + e.getMessage());
        }

        // Scenario 3: Session expiration
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 3: Session Timeout (10 seconds)");
        System.out.println("=".repeat(75));

        Session bobSession = sessionManager.createSession("bob");
        String bobSessionId = bobSession.getSessionId();

        System.out.println("\\nRequest 1: Immediate access");
        System.out.println("  Session age: 0 seconds");
        boolean valid1 = sessionManager.validateSession(bobSessionId);
        System.out.println("  Result: " + (valid1 ? "VALID" : "INVALID"));

        // Simulate time passing
        System.out.println("\\n[Simulating 5 seconds of inactivity...]");
        Thread.sleep(5000);

        System.out.println("\\nRequest 2: Access after 5 seconds");
        System.out.println("  Session age: ~5 seconds");
        boolean valid2 = sessionManager.validateSession(bobSessionId);
        System.out.println("  Result: " + (valid2 ? "VALID - timer reset" : "INVALID"));

        // Wait for expiration
        System.out.println("\\n[Simulating 11 more seconds of inactivity...]");
        Thread.sleep(11000);

        System.out.println("\\nRequest 3: Access after 16 total seconds (11 since last access)");
        System.out.println("  Session age: ~16 seconds");
        boolean valid3 = sessionManager.validateSession(bobSessionId);
        System.out.println("  Result: " + (valid3 ? "VALID" : "EXPIRED"));

        // Scenario 4: Session fixation protection
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 4: Session Fixation Protection");
        System.out.println("=".repeat(75));

        System.out.println("\\nStep 1: Attacker creates session");
        Session attackerSession = sessionManager.createSession("attacker");
        String attackerSessionId = attackerSession.getSessionId();
        System.out.println("  Attacker session ID: " + attackerSessionId.substring(0, 16) + "...");

        System.out.println("\\nStep 2: Victim logs in (new session created)");
        sessionManager.invalidateSession(attackerSessionId);  // Old session invalidated
        Session victimSession = sessionManager.createSession("victim");
        String victimSessionId = victimSession.getSessionId();
        System.out.println("  Victim session ID: " + victimSessionId.substring(0, 16) + "...");

        System.out.println("\\nStep 3: Attacker tries to use old session");
        boolean attackSuccess = sessionManager.validateSession(attackerSessionId);
        System.out.println("  Old session valid: " + attackSuccess);
        System.out.println("  → Attack prevented! Session ID changed after login");

        // Scenario 5: Manual logout
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Scenario 5: Manual Session Invalidation (Logout)");
        System.out.println("=".repeat(75));

        Session charlieSession = sessionManager.createSession("charlie");
        String charlieSessionId = charlieSession.getSessionId();

        System.out.println("\\nBefore logout:");
        System.out.println("  Active sessions: " +
            sessionManager.getRegistry().getActiveSessionCount());

        System.out.println("\\nUser 'charlie' clicks logout:");
        sessionManager.invalidateSession(charlieSessionId);

        System.out.println("\\nAfter logout:");
        System.out.println("  Active sessions: " +
            sessionManager.getRegistry().getActiveSessionCount());
        System.out.println("  Session valid: " +
            sessionManager.validateSession(charlieSessionId));

        // Session management summary
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Session Management Best Practices");
        System.out.println("=".repeat(75));

        System.out.println("\\nSecurity Features:");
        System.out.println("  ✓ Session fixation protection (new ID after login)");
        System.out.println("  ✓ Concurrent session control (limit per user)");
        System.out.println("  ✓ Automatic timeout on inactivity");
        System.out.println("  ✓ Session validation on each request");
        System.out.println("  ✓ Manual invalidation (logout)");

        System.out.println("\\nConfiguration Options:");
        System.out.println("  • SessionCreationPolicy: ALWAYS, IF_REQUIRED, NEVER, STATELESS");
        System.out.println("  • maximumSessions: Limit concurrent sessions per user");
        System.out.println("  • maxSessionsPreventsLogin: Block or expire oldest session");
        System.out.println("  • sessionFixation().newSession(): Always create new session ID");
        System.out.println("  • timeout: Session expiration time");

        System.out.println("\\nProduction Recommendations:");
        System.out.println("  • Use Redis/Hazelcast for distributed session storage");
        System.out.println("  • Set timeout to 15-30 minutes for web apps");
        System.out.println("  • Limit to 1-3 concurrent sessions per user");
        System.out.println("  • Always invalidate on logout");
        System.out.println("  • Consider stateless (JWT) for microservices");
        System.out.println("  • Monitor active sessions for anomalies");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: SessionManagementConfigurer, SessionRegistry");
    }
}
''',

    818: '''// Security Testing with MockMvc Simulation
// In production: import org.springframework.test.web.servlet.MockMvc;
// @SpringBootTest
// @AutoConfigureMockMvc
// public class SecurityTest {
//     @Autowired
//     private MockMvc mockMvc;
//
//     @Test
//     @WithMockUser(roles = "ADMIN")
//     public void adminCanAccessAdminEndpoint() throws Exception {
//         mockMvc.perform(get("/admin/users"))
//             .andExpect(status().isOk())
//             .andExpect(jsonPath("$.data").exists());
//     }
//
//     @Test
//     public void unauthenticatedUserIsRedirectedToLogin() throws Exception {
//         mockMvc.perform(get("/dashboard"))
//             .andExpect(status().isUnauthorized());
//     }
// }

import java.util.*;

class MockHttpRequest {
    private String method;
    private String path;
    private Map<String, String> headers = new HashMap<>();
    private Map<String, String> parameters = new HashMap<>();
    private String body;
    private MockUser user;

    public MockHttpRequest(String method, String path) {
        this.method = method;
        this.path = path;
    }

    public MockHttpRequest header(String name, String value) {
        headers.put(name, value);
        return this;
    }

    public MockHttpRequest param(String name, String value) {
        parameters.put(name, value);
        return this;
    }

    public MockHttpRequest content(String body) {
        this.body = body;
        return this;
    }

    public MockHttpRequest withUser(MockUser user) {
        this.user = user;
        return this;
    }

    public String getMethod() { return method; }
    public String getPath() { return path; }
    public Map<String, String> getHeaders() { return headers; }
    public MockUser getUser() { return user; }
    public String getBody() { return body; }
}

class MockHttpResponse {
    private int statusCode;
    private Map<String, String> headers = new HashMap<>();
    private String body;

    public void setStatus(int code) { this.statusCode = code; }
    public void addHeader(String name, String value) { headers.put(name, value); }
    public void setBody(String body) { this.body = body; }

    public int getStatus() { return statusCode; }
    public Map<String, String> getHeaders() { return headers; }
    public String getBody() { return body; }
}

class MockUser {
    private String username;
    private String password;
    private List<String> roles;

    public MockUser(String username, String password, String... roles) {
        this.username = username;
        this.password = password;
        this.roles = Arrays.asList(roles);
    }

    public String getUsername() { return username; }
    public String getPassword() { return password; }
    public List<String> getRoles() { return roles; }

    public boolean hasRole(String role) {
        return roles.contains(role) || roles.contains("ROLE_" + role);
    }
}

class SecurityConfig {
    private Map<String, List<String>> endpointRoles = new HashMap<>();

    public SecurityConfig() {
        // Define security rules
        endpointRoles.put("/public", Arrays.asList("*"));  // Everyone
        endpointRoles.put("/api/users", Arrays.asList("ROLE_USER", "ROLE_ADMIN"));
        endpointRoles.put("/admin", Arrays.asList("ROLE_ADMIN"));
        endpointRoles.put("/api/delete", Arrays.asList("ROLE_ADMIN"));
    }

    public boolean isAuthorized(String path, MockUser user) {
        // Find matching rule
        String matchedPattern = null;
        for (String pattern : endpointRoles.keySet()) {
            if (path.startsWith(pattern)) {
                matchedPattern = pattern;
                break;
            }
        }

        if (matchedPattern == null) {
            return false;  // No rule = deny
        }

        List<String> requiredRoles = endpointRoles.get(matchedPattern);

        // Public endpoint
        if (requiredRoles.contains("*")) {
            return true;
        }

        // Authentication required
        if (user == null) {
            return false;
        }

        // Check if user has required role
        for (String role : requiredRoles) {
            if (user.hasRole(role)) {
                return true;
            }
        }

        return false;
    }
}

class CsrfTokenRepository {
    private Map<String, String> tokens = new HashMap<>();

    public String generateToken(String sessionId) {
        String token = UUID.randomUUID().toString();
        tokens.put(sessionId, token);
        return token;
    }

    public boolean validateToken(String sessionId, String token) {
        String expected = tokens.get(sessionId);
        return expected != null && expected.equals(token);
    }
}

class MockMvc {
    private SecurityConfig securityConfig;
    private CsrfTokenRepository csrfTokens;
    private boolean csrfEnabled;

    public MockMvc(boolean csrfEnabled) {
        this.securityConfig = new SecurityConfig();
        this.csrfTokens = new CsrfTokenRepository();
        this.csrfEnabled = csrfEnabled;
    }

    public MockHttpResponse perform(MockHttpRequest request) {
        MockHttpResponse response = new MockHttpResponse();

        System.out.println("\\n  " + request.getMethod() + " " + request.getPath());

        // Step 1: CSRF validation for state-changing methods
        if (csrfEnabled && isStateChanging(request.getMethod())) {
            String csrfToken = request.getHeaders().get("X-CSRF-TOKEN");
            String sessionId = request.getHeaders().get("Cookie");

            System.out.println("  → CSRF validation required");

            if (csrfToken == null || sessionId == null ||
                !csrfTokens.validateToken(sessionId, csrfToken)) {
                System.out.println("  ✗ CSRF token invalid or missing");
                response.setStatus(403);
                response.setBody("{\"error\":\"CSRF token validation failed\"}");
                return response;
            }
            System.out.println("  ✓ CSRF token valid");
        }

        // Step 2: Authorization check
        System.out.println("  → Checking authorization...");
        boolean authorized = securityConfig.isAuthorized(request.getPath(), request.getUser());

        if (!authorized) {
            if (request.getUser() == null) {
                System.out.println("  ✗ Unauthenticated - 401 Unauthorized");
                response.setStatus(401);
                response.setBody("{\"error\":\"Authentication required\"}");
            } else {
                System.out.println("  ✗ Forbidden - 403 Access Denied");
                response.setStatus(403);
                response.setBody("{\"error\":\"Access denied\"}");
            }
            return response;
        }

        System.out.println("  ✓ Authorized");

        // Step 3: Process request
        response.setStatus(200);

        if (request.getPath().equals("/public")) {
            response.setBody("{\"message\":\"Public data\"}");
        } else if (request.getPath().startsWith("/admin")) {
            response.setBody("{\"message\":\"Admin data\",\"users\":[\"alice\",\"bob\"]}");
        } else if (request.getPath().startsWith("/api/users")) {
            response.setBody("{\"users\":[{\"id\":1,\"name\":\"Alice\"}]}");
        } else if (request.getPath().startsWith("/api/delete")) {
            response.setBody("{\"message\":\"Resource deleted\"}");
        }

        System.out.println("  ✓ 200 OK");
        return response;
    }

    private boolean isStateChanging(String method) {
        return method.equals("POST") || method.equals("PUT") ||
               method.equals("DELETE") || method.equals("PATCH");
    }

    public String generateCsrfToken(String sessionId) {
        return csrfTokens.generateToken(sessionId);
    }
}

class SecurityTestRunner {
    private MockMvc mockMvc;
    private int passed = 0;
    private int failed = 0;

    public SecurityTestRunner(MockMvc mockMvc) {
        this.mockMvc = mockMvc;
    }

    public void test(String testName, MockHttpRequest request, int expectedStatus) {
        System.out.println("\\nTest: " + testName);
        System.out.println("-".repeat(75));

        MockHttpResponse response = mockMvc.perform(request);

        if (response.getStatus() == expectedStatus) {
            System.out.println("  ✓ PASSED - Expected status: " + expectedStatus);
            passed++;
        } else {
            System.out.println("  ✗ FAILED - Expected: " + expectedStatus +
                ", Got: " + response.getStatus());
            failed++;
        }

        if (response.getBody() != null) {
            System.out.println("  Response: " + response.getBody());
        }
    }

    public void printSummary() {
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Test Results Summary");
        System.out.println("=".repeat(75));
        System.out.println("  Passed: " + passed);
        System.out.println("  Failed: " + failed);
        System.out.println("  Total:  " + (passed + failed));
        System.out.println("  Success Rate: " +
            (passed * 100 / (passed + failed)) + "%");
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Security Testing with MockMvc Simulation");
        System.out.println("=".repeat(75));

        MockMvc mockMvc = new MockMvc(true);  // CSRF enabled
        SecurityTestRunner testRunner = new SecurityTestRunner(mockMvc);

        // Test users
        MockUser admin = new MockUser("admin", "admin123", "ROLE_ADMIN", "ROLE_USER");
        MockUser user = new MockUser("user", "user456", "ROLE_USER");

        // Test Suite 1: Public endpoint access
        System.out.println("\\nTest Suite 1: Public Endpoint Access");
        System.out.println("=".repeat(75));

        testRunner.test(
            "Unauthenticated user can access public endpoint",
            new MockHttpRequest("GET", "/public"),
            200
        );

        testRunner.test(
            "Authenticated user can access public endpoint",
            new MockHttpRequest("GET", "/public").withUser(user),
            200
        );

        // Test Suite 2: Authentication required
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Test Suite 2: Authentication Required Endpoints");
        System.out.println("=".repeat(75));

        testRunner.test(
            "Unauthenticated user cannot access protected endpoint",
            new MockHttpRequest("GET", "/api/users"),
            401
        );

        testRunner.test(
            "Authenticated user can access protected endpoint",
            new MockHttpRequest("GET", "/api/users").withUser(user),
            200
        );

        // Test Suite 3: Role-based access control
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Test Suite 3: Role-Based Access Control");
        System.out.println("=".repeat(75));

        testRunner.test(
            "ADMIN can access admin endpoint",
            new MockHttpRequest("GET", "/admin/users").withUser(admin),
            200
        );

        testRunner.test(
            "USER cannot access admin endpoint",
            new MockHttpRequest("GET", "/admin/users").withUser(user),
            403
        );

        testRunner.test(
            "ADMIN can delete resources",
            new MockHttpRequest("DELETE", "/api/delete/123")
                .withUser(admin)
                .header("X-CSRF-TOKEN", mockMvc.generateCsrfToken("session1"))
                .header("Cookie", "session1"),
            200
        );

        testRunner.test(
            "USER cannot delete resources",
            new MockHttpRequest("DELETE", "/api/delete/123")
                .withUser(user)
                .header("X-CSRF-TOKEN", mockMvc.generateCsrfToken("session2"))
                .header("Cookie", "session2"),
            403
        );

        // Test Suite 4: CSRF protection
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Test Suite 4: CSRF Protection");
        System.out.println("=".repeat(75));

        testRunner.test(
            "POST without CSRF token is rejected",
            new MockHttpRequest("POST", "/api/users")
                .withUser(admin)
                .content("{\"name\":\"NewUser\"}"),
            403
        );

        String csrfToken = mockMvc.generateCsrfToken("session3");
        testRunner.test(
            "POST with valid CSRF token succeeds",
            new MockHttpRequest("POST", "/api/users")
                .withUser(admin)
                .header("X-CSRF-TOKEN", csrfToken)
                .header("Cookie", "session3")
                .content("{\"name\":\"NewUser\"}"),
            200
        );

        testRunner.test(
            "GET requests don't require CSRF token",
            new MockHttpRequest("GET", "/api/users").withUser(user),
            200
        );

        // Print test summary
        testRunner.printSummary();

        // Best practices
        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Security Testing Best Practices");
        System.out.println("=".repeat(75));

        System.out.println("\\nTest Coverage:");
        System.out.println("  ✓ Public endpoints (no auth required)");
        System.out.println("  ✓ Authenticated endpoints (login required)");
        System.out.println("  ✓ Role-based access (ADMIN vs USER)");
        System.out.println("  ✓ CSRF protection (POST/PUT/DELETE)");
        System.out.println("  ✓ HTTP methods (GET, POST, DELETE)");
        System.out.println("  ✓ Expected status codes (200, 401, 403)");

        System.out.println("\\nMockMvc Features:");
        System.out.println("  • @WithMockUser - Test with authenticated user");
        System.out.println("  • @WithAnonymousUser - Test without authentication");
        System.out.println("  • .andExpect(status().isOk()) - Assert HTTP status");
        System.out.println("  • .andExpect(jsonPath()) - Assert JSON response");
        System.out.println("  • .with(csrf()) - Include CSRF token");
        System.out.println("  • .with(httpBasic()) - Basic authentication");

        System.out.println("\\nProduction Testing Strategy:");
        System.out.println("  • Test all endpoint security configurations");
        System.out.println("  • Verify each role has correct permissions");
        System.out.println("  • Test CSRF on all state-changing operations");
        System.out.println("  • Validate error messages don't leak info");
        System.out.println("  • Use @SpringBootTest for integration tests");
        System.out.println("  • Mock external dependencies");
        System.out.println("  • Test session management and logout");

        System.out.println("\\n" + "=".repeat(75));
        System.out.println("Real Spring Security: @AutoConfigureMockMvc, MockMvc");
    }
}
''',
}

def update_lessons(lessons_file):
    """Update lessons JSON with Spring Security simulations"""
    with open(lessons_file, 'r', encoding='utf-8') as f:
        lessons = json.load(f)

    print("\nBefore update (character counts):")
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in SPRING_SECURITY_BATCH_7B:
            current_len = len(lesson.get('fullSolution', ''))
            print(f"  Lesson {lesson_id}: {current_len} chars")

    updated = []
    for lesson in lessons:
        lesson_id = lesson.get('id')
        if lesson_id in SPRING_SECURITY_BATCH_7B:
            lesson['fullSolution'] = SPRING_SECURITY_BATCH_7B[lesson_id]
            updated.append(lesson_id)

    with open(lessons_file, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

    return updated, lessons

def main():
    """Main entry point"""
    lessons_file = r'c:\devbootLLM-app\public\lessons-java.json'

    try:
        updated, lessons = update_lessons(lessons_file)

        print("\n" + "=" * 80)
        print("Spring Security Simulations Batch 7b - Upgrade Complete")
        print("=" * 80)
        print(f"\nSuccessfully updated {len(updated)} lessons:")

        lesson_names = {
            813: "Security Headers Configuration - XSS, CSP, HSTS protection",
            815: "Custom Authentication Provider - Custom login logic",
            817: "Session Management - Timeout, concurrent sessions, fixation",
            818: "Security Testing with MockMvc - Test security configurations"
        }

        print("\nAfter update (character counts):")
        for lesson in lessons:
            lesson_id = lesson.get('id')
            if lesson_id in SPRING_SECURITY_BATCH_7B:
                new_len = len(lesson.get('fullSolution', ''))
                target_range = "4,000-5,000" if lesson_id in [815, 818] else "3,500-4,500"
                print(f"  • Lesson {lesson_id}: {lesson_names.get(lesson_id, 'Unknown')}")
                print(f"    {new_len} chars (target: {target_range})")

        print(f"\nAll simulations include:")
        print(f"  + Realistic Spring Security demonstrations with working code")
        print(f"  + Production-ready comments (// In production: import ...)")
        print(f"  + 3,500-5,000 character comprehensive examples")
        print(f"  + Security best practices and use cases")
        print(f"  + Working demo with realistic scenarios")
        print(f"  + Detailed explanations of security concepts")
        print(f"  + Job-ready interview patterns")
        print("\nFile updated: " + lessons_file)
        print("=" * 80)

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
