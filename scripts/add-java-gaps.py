#!/usr/bin/env python3
"""Add 58 Java gap-filling lessons"""

import json
import sys
sys.path.insert(0, 'scripts')

from add_gap_filling_lessons import generate_comprehensive_tutorial, generate_comprehensive_examples

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

print('='*60)
print('ADDING JAVA GAP-FILLING LESSONS (58 total)')
print('='*60)

# Load Java lessons
java_lessons = load_lessons('public/lessons-java.json')
print(f'\nCurrent: {len(java_lessons)} Java lessons')

# Mockito Advanced (10 lessons, IDs 828-837)
mockito_topics = [
    ('Mockito Basics Review', 'Review Mockito fundamentals', ['Mocks', 'Stubs', 'Verify']),
    ('Argument Matchers', 'Use flexible argument matching', ['Matchers', 'any()', 'eq()']),
    ('Spies vs Mocks', 'When to use spies', ['Spies', 'Partial mocking', 'Real objects']),
    ('Mockito Annotations', 'Use @Mock, @InjectMocks', ['Annotations', 'Dependency injection', 'Setup']),
    ('Verification Modes', 'Verify method calls', ['Verification', 'times()', 'never()']),
    ('Stubbing Consecutive Calls', 'Different returns per call', ['Stubbing', 'thenReturn', 'Sequence']),
    ('Mockito with Exceptions', 'Mock exception throwing', ['Exceptions', 'thenThrow', 'Error testing']),
    ('Capturing Arguments', 'Capture method arguments', ['ArgumentCaptor', 'Verification', 'Testing']),
    ('Mocking Static Methods', 'Mock static methods', ['Static mocking', 'PowerMock', 'Mockito 3.4+']),
    ('Mockito Best Practices', 'Production testing patterns', ['Best practices', 'Testing', 'Patterns']),
]

# Testcontainers (9 lessons, IDs 838-846)
testcontainers_topics = [
    ('Testcontainers Basics', 'Docker containers for testing', ['Containers', 'Integration tests', 'Docker']),
    ('Database Testing', 'Test with real databases', ['PostgreSQL', 'MySQL', 'Database testing']),
    ('Kafka Testing', 'Test Kafka integrations', ['Kafka', 'Messaging', 'Integration tests']),
    ('Redis Testing', 'Test Redis operations', ['Redis', 'Caching', 'Testing']),
    ('Docker Compose Integration', 'Multi-container tests', ['docker-compose', 'Multi-container', 'Integration']),
    ('Testcontainers with Spring Boot', 'Spring Boot integration', ['Spring Boot', 'Auto-configuration', 'Testing']),
    ('Parallel Test Execution', 'Run tests in parallel', ['Parallel', 'Performance', 'CI/CD']),
    ('Custom Containers', 'Build custom test containers', ['Custom containers', 'Dockerfile', 'Configuration']),
    ('Testcontainers Best Practices', 'Production testing patterns', ['Best practices', 'Performance', 'CI/CD']),
]

# Spring Security Advanced (12 lessons, IDs 847-858)
security_topics = [
    ('Spring Security Architecture', 'Security filter chain', ['Architecture', 'Filter chain', 'Security context']),
    ('Custom Authentication', 'Custom auth providers', ['Authentication', 'Custom providers', 'User details']),
    ('OAuth2 Resource Server', 'Protect APIs with OAuth2', ['OAuth2', 'Resource server', 'JWT']),
    ('JWT Token Validation', 'Validate JWT tokens', ['JWT', 'Token validation', 'Claims']),
    ('Method Security', 'Secure methods with annotations', ['@PreAuthorize', '@Secured', 'Method security']),
    ('Custom Security Filters', 'Add custom filters', ['Custom filters', 'Filter chain', 'Security']),
    ('CORS Configuration', 'Configure CORS properly', ['CORS', 'Cross-origin', 'Configuration']),
    ('CSRF Protection', 'Implement CSRF protection', ['CSRF', 'Token', 'Protection']),
    ('Session Management', 'Manage user sessions', ['Sessions', 'Concurrency', 'Session fixation']),
    ('Password Encoding', 'Secure password storage', ['BCrypt', 'Password hashing', 'Security']),
    ('Remember Me', 'Implement remember me', ['Remember me', 'Token', 'Persistence']),
    ('Security Testing', 'Test security configurations', ['Testing', 'MockMvc', 'Security tests']),
]

# Docker (10 lessons, IDs 859-868)
docker_java_topics = [
    ('Docker for Java Apps', 'Containerize Java applications', ['Docker', 'Java', 'Containers']),
    ('Multi-Stage Builds', 'Optimize Docker images', ['Multi-stage', 'Optimization', 'Image size']),
    ('JIB for Docker', 'Build images without Docker', ['JIB', 'Google', 'Build tools']),
    ('Distroless Images', 'Use minimal base images', ['Distroless', 'Security', 'Size']),
    ('Docker Compose for Java', 'Multi-container Java apps', ['docker-compose', 'Services', 'Networks']),
    ('JVM in Containers', 'Optimize JVM for containers', ['JVM', 'Container limits', 'Memory']),
    ('Docker Debugging', 'Debug containerized apps', ['Debugging', 'Logs', 'Shell access']),
    ('Docker Networking', 'Container networking', ['Networking', 'Bridge', 'Host']),
    ('Docker Secrets', 'Manage secrets securely', ['Secrets', 'Security', 'Environment']),
    ('Docker Production', 'Deploy Java apps with Docker', ['Production', 'Deployment', 'Best practices']),
]

# gRPC (10 lessons, IDs 869-878)
grpc_topics = [
    ('gRPC Basics', 'Protocol Buffers and gRPC', ['gRPC', 'Protocol Buffers', 'RPC']),
    ('Service Definition', 'Define gRPC services', ['protobuf', 'Service definition', 'IDL']),
    ('Unary RPC', 'Simple request-response', ['Unary', 'Request-response', 'Basic']),
    ('Server Streaming', 'Stream responses to client', ['Server streaming', 'Streaming', 'Real-time']),
    ('Client Streaming', 'Stream requests to server', ['Client streaming', 'Streaming', 'Upload']),
    ('Bidirectional Streaming', 'Two-way streaming', ['Bidirectional', 'Full duplex', 'Chat']),
    ('Error Handling', 'Handle gRPC errors', ['Errors', 'Status codes', 'Error handling']),
    ('Interceptors', 'Add cross-cutting concerns', ['Interceptors', 'Middleware', 'Logging']),
    ('Authentication', 'Secure gRPC services', ['Authentication', 'TLS', 'Security']),
    ('gRPC Production', 'Deploy gRPC in production', ['Production', 'Load balancing', 'Monitoring']),
]

# Quarkus (7 lessons, IDs 879-885)
quarkus_topics = [
    ('Quarkus Basics', 'Cloud-native Java with Quarkus', ['Quarkus', 'Cloud-native', 'Fast startup']),
    ('Quarkus DI', 'Dependency injection in Quarkus', ['CDI', 'Dependency injection', 'Arc']),
    ('Quarkus REST', 'Build REST APIs with Quarkus', ['REST', 'JAX-RS', 'RESTEasy']),
    ('Quarkus Data Access', 'Panache for data access', ['Panache', 'Hibernate', 'Database']),
    ('Dev Mode', 'Use Quarkus dev mode', ['Dev mode', 'Hot reload', 'Development']),
    ('Native Images', 'Build native executables', ['GraalVM', 'Native', 'Fast startup']),
    ('Quarkus Testing', 'Test Quarkus applications', ['Testing', '@QuarkusTest', 'CI/CD']),
]

all_java_gaps = []
next_id = 828

# Generate all lessons
print(f'\nMockito Advanced (10 lessons, IDs {next_id}-{next_id+9})...')
for i, (title, desc, topics) in enumerate(mockito_topics, next_id):
    lesson = {
        'id': i,
        'title': f'Mockito - {title}',
        'description': desc,
        'difficulty': 'Expert' if 'Best Practices' in title else 'Advanced',
        'tags': ['Mockito', 'Testing', topics[0], 'Advanced'],
        'category': 'Testing',
        'language': 'java',
        'baseCode': f'import org.mockito.*;\n\n// TODO: {desc}\npublic class Test {{\n    public void test() {{\n        System.out.println("Test");\n    }}\n}}',
        'fullSolution': f'import org.mockito.*;\nimport static org.mockito.Mockito.*;\n\npublic class Test {{\n    @Test\n    public void test() {{\n        List<String> mock = mock(List.class);\n        when(mock.size()).thenReturn(10);\n        assertEquals(10, mock.size());\n    }}\n}}',
        'expectedOutput': 'Test',
        'tutorial': generate_comprehensive_tutorial(f'Mockito - {title}', desc, 'Mockito', topics),
        'additionalExamples': generate_comprehensive_examples(f'Mockito - {title}', 'Mockito')
    }
    all_java_gaps.append(lesson)
next_id += 10

print(f'Testcontainers (9 lessons, IDs {next_id}-{next_id+8})...')
for i, (title, desc, topics) in enumerate(testcontainers_topics, next_id):
    lesson = {
        'id': i,
        'title': f'Testcontainers - {title}',
        'description': desc,
        'difficulty': 'Expert' if 'Best Practices' in title else 'Advanced',
        'tags': ['Testcontainers', 'Testing', 'Docker', 'Advanced'],
        'category': 'Testing',
        'language': 'java',
        'baseCode': f'import org.testcontainers.containers.*;\n\n// TODO: {desc}\npublic class Test {{\n    public void test() {{\n        System.out.println("Test");\n    }}\n}}',
        'fullSolution': f'import org.testcontainers.containers.PostgreSQLContainer;\n\npublic class Test {{\n    @Container\n    PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:15");\n    \n    @Test\n    public void test() {{\n        System.out.println("JDBC URL: " + postgres.getJdbcUrl());\n    }}\n}}',
        'expectedOutput': 'Test',
        'tutorial': generate_comprehensive_tutorial(f'Testcontainers - {title}', desc, 'Testcontainers', topics),
        'additionalExamples': generate_comprehensive_examples(f'Testcontainers - {title}', 'Testcontainers')
    }
    all_java_gaps.append(lesson)
next_id += 9

print(f'Spring Security Advanced (12 lessons, IDs {next_id}-{next_id+11})...')
for i, (title, desc, topics) in enumerate(security_topics, next_id):
    lesson = {
        'id': i,
        'title': f'Spring Security - {title}',
        'description': desc,
        'difficulty': 'Expert',
        'tags': ['Spring Security', 'Security', topics[0], 'Expert'],
        'category': 'Security',
        'language': 'java',
        'baseCode': f'import org.springframework.security.config.annotation.web.builders.*;\n\n// TODO: {desc}\npublic class SecurityConfig {{\n    public void configure(HttpSecurity http) {{\n        System.out.println("Security configured");\n    }}\n}}',
        'fullSolution': f'import org.springframework.security.config.annotation.web.builders.*;\n\n@Configuration\npublic class SecurityConfig {{\n    @Bean\n    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {{\n        http.authorizeHttpRequests(auth -> auth\n            .requestMatchers("/public/**").permitAll()\n            .anyRequest().authenticated()\n        );\n        return http.build();\n    }}\n}}',
        'expectedOutput': 'Security configured',
        'tutorial': generate_comprehensive_tutorial(f'Spring Security - {title}', desc, 'Spring Security', topics),
        'additionalExamples': generate_comprehensive_examples(f'Spring Security - {title}', 'Spring Security')
    }
    all_java_gaps.append(lesson)
next_id += 12

print(f'Docker (10 lessons, IDs {next_id}-{next_id+9})...')
for i, (title, desc, topics) in enumerate(docker_java_topics, next_id):
    lesson = {
        'id': i,
        'title': f'Docker - {title}',
        'description': desc,
        'difficulty': 'Expert' if 'Production' in title else 'Advanced',
        'tags': ['Docker', 'DevOps', topics[0], 'Advanced'],
        'category': 'DevOps',
        'language': 'java',
        'baseCode': f'# Dockerfile\nFROM eclipse-temurin:17-jdk-alpine\n# TODO: {desc}\nCMD ["java", "-jar", "app.jar"]',
        'fullSolution': f'# Dockerfile\nFROM eclipse-temurin:17-jdk-alpine\nWORKDIR /app\nCOPY target/*.jar app.jar\nEXPOSE 8080\nCMD ["java", "-jar", "app.jar"]',
        'expectedOutput': 'Docker image built successfully',
        'tutorial': generate_comprehensive_tutorial(f'Docker - {title}', desc, 'Docker', topics),
        'additionalExamples': generate_comprehensive_examples(f'Docker - {title}', 'Docker')
    }
    all_java_gaps.append(lesson)
next_id += 10

print(f'gRPC (10 lessons, IDs {next_id}-{next_id+9})...')
for i, (title, desc, topics) in enumerate(grpc_topics, next_id):
    lesson = {
        'id': i,
        'title': f'gRPC - {title}',
        'description': desc,
        'difficulty': 'Expert' if 'Production' in title else 'Advanced',
        'tags': ['gRPC', 'RPC', topics[0], 'Advanced'],
        'category': 'Web/APIs',
        'language': 'java',
        'baseCode': f'import io.grpc.*;\n\n// TODO: {desc}\npublic class GrpcService {{\n    public void serve() {{\n        System.out.println("gRPC service");\n    }}\n}}',
        'fullSolution': f'import io.grpc.*;\n\npublic class GrpcService extends GreeterGrpc.GreeterImplBase {{\n    @Override\n    public void sayHello(HelloRequest req, StreamObserver<HelloReply> responseObserver) {{\n        HelloReply reply = HelloReply.newBuilder()\n            .setMessage("Hello " + req.getName())\n            .build();\n        responseObserver.onNext(reply);\n        responseObserver.onCompleted();\n    }}\n}}',
        'expectedOutput': 'gRPC service',
        'tutorial': generate_comprehensive_tutorial(f'gRPC - {title}', desc, 'gRPC', topics),
        'additionalExamples': generate_comprehensive_examples(f'gRPC - {title}', 'gRPC')
    }
    all_java_gaps.append(lesson)
next_id += 10

print(f'Quarkus (7 lessons, IDs {next_id}-{next_id+6})...')
for i, (title, desc, topics) in enumerate(quarkus_topics, next_id):
    lesson = {
        'id': i,
        'title': f'Quarkus - {title}',
        'description': desc,
        'difficulty': 'Expert',
        'tags': ['Quarkus', 'Cloud-native', topics[0], 'Expert'],
        'category': 'Web Development',
        'language': 'java',
        'baseCode': f'import javax.ws.rs.*;\n\n// TODO: {desc}\n@Path("/hello")\npublic class HelloResource {{\n    @GET\n    public String hello() {{\n        return "Hello";\n    }}\n}}',
        'fullSolution': f'import javax.ws.rs.*;\n\n@Path("/hello")\npublic class HelloResource {{\n    @GET\n    @Produces(MediaType.TEXT_PLAIN)\n    public String hello() {{\n        return "Hello from Quarkus!";\n    }}\n}}',
        'expectedOutput': 'Hello from Quarkus!',
        'tutorial': generate_comprehensive_tutorial(f'Quarkus - {title}', desc, 'Quarkus', topics),
        'additionalExamples': generate_comprehensive_examples(f'Quarkus - {title}', 'Quarkus')
    }
    all_java_gaps.append(lesson)

# Add to Java lessons
java_lessons.extend(all_java_gaps)

print(f'\n[OK] Generated {len(all_java_gaps)} Java gap-filling lessons')
print(f'New Java total: {len(java_lessons)} lessons')

# Save Java lessons
save_lessons('public/lessons-java.json', java_lessons)
print('[OK] Saved Java lessons')

print('\n' + '='*60)
print(f'JAVA GAP-FILLING COMPLETE! ({len(all_java_gaps)} lessons)')
print('='*60)
print(f'Total Java lessons: {len(java_lessons)}')
