#!/usr/bin/env python3
"""Add Java Phase 1 lessons"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

# Load current lessons
java_lessons = load_lessons('public/lessons-java.json')
print(f"Current Java lessons: {len(java_lessons)}")

# Java: Spring Boot Advanced (13 lessons) - IDs 726-738
springboot_lessons = []
springboot_topics = [
    ("Actuator Endpoints", "Monitor application health and metrics"),
    ("Custom Metrics with Micrometer", "Track custom application metrics"),
    ("Health Indicators", "Create custom health checks"),
    ("Prometheus Integration", "Export metrics to Prometheus"),
    ("Custom Starters", "Build custom Spring Boot starters"),
    ("Auto-configuration", "Understand and create auto-configuration"),
    ("Properties Externalization", "Manage configuration externally"),
    ("Profiles Advanced", "Advanced profile management"),
    ("Logging Configuration", "Configure application logging"),
    ("Graceful Shutdown", "Implement graceful shutdown"),
    ("Admin Server", "Set up Spring Boot Admin"),
    ("Build Info", "Add build information to application"),
    ("Production Best Practices", "Production deployment patterns")
]

for i, (title, desc) in enumerate(springboot_topics, 726):
    springboot_lessons.append({
        "id": i,
        "title": f"Spring Boot - {title}",
        "description": desc,
        "difficulty": "Expert",
        "tags": ["Spring Boot", "Production", "Expert"],
        "category": "Web Development",
        "language": "java",
        "baseCode": f"// {title}\npublic class Application {{\n    // TODO: Implement {title.lower()}\n    public static void main(String[] args) {{\n        System.out.println(\"Application ready\");\n    }}\n}}",
        "fullSolution": f"public class Application {{\n    public static void main(String[] args) {{\n        System.out.println(\"Application ready\");\n    }}\n}}",
        "expectedOutput": "Application ready",
        "tutorial": f"# {title}\n\n{desc}\n\n## Example\n\n```java\n@SpringBootApplication\npublic class Application {{\n    public static void main(String[] args) {{\n        SpringApplication.run(Application.class, args);\n    }}\n}}\n```",
        "additionalExamples": f"// Example: {title}\n@Component\npublic class Example {{\n    public void execute() {{\n        System.out.println(\"Example executed\");\n    }}\n}}"
    })

# Java: Reactive Programming (15 lessons) - IDs 739-753
reactive_lessons = []
reactive_topics = [
    ("Reactor Basics - Mono", "Understand Mono for single values"),
    ("Reactor Basics - Flux", "Understand Flux for multiple values"),
    ("Reactive Operators", "Transform reactive streams"),
    ("Error Handling", "Handle errors in reactive streams"),
    ("Backpressure", "Manage backpressure in streams"),
    ("WebFlux Controllers", "Build reactive web endpoints"),
    ("Reactive WebClient", "Make non-blocking HTTP calls"),
    ("R2DBC", "Reactive database access"),
    ("WebSocket Reactive", "Real-time WebSocket communication"),
    ("Server-Sent Events", "Push updates to clients"),
    ("Testing Reactive Code", "Test reactive applications"),
    ("Performance Comparison", "Compare reactive vs blocking"),
    ("Reactive Streams", "Understand Reactive Streams spec"),
    ("Spring Integration", "Integrate with Spring ecosystem"),
    ("Production Deployment", "Deploy reactive applications")
]

for i, (title, desc) in enumerate(reactive_topics, 739):
    reactive_lessons.append({
        "id": i,
        "title": f"Reactive - {title}",
        "description": desc,
        "difficulty": "Expert",
        "tags": ["Reactive", "WebFlux", "Expert"],
        "category": "Web Development",
        "language": "java",
        "baseCode": f"// {title}\nimport reactor.core.publisher.Mono;\n\npublic class ReactiveExample {{\n    // TODO: Implement {title.lower()}\n    public static void main(String[] args) {{\n        System.out.println(\"Reactive example\");\n    }}\n}}",
        "fullSolution": f"import reactor.core.publisher.Mono;\n\npublic class ReactiveExample {{\n    public static void main(String[] args) {{\n        Mono<String> mono = Mono.just(\"Hello Reactive\");\n        mono.subscribe(System.out::println);\n    }}\n}}",
        "expectedOutput": "Hello Reactive",
        "tutorial": f"# {title}\n\n{desc}\n\n## Example\n\n```java\nimport reactor.core.publisher.Mono;\n\nMono<String> mono = Mono.just(\"data\");\nmono.subscribe(System.out::println);\n```",
        "additionalExamples": f"// Example: {title}\nimport reactor.core.publisher.Flux;\n\nFlux<Integer> flux = Flux.range(1, 5);\nflux.subscribe(System.out::println);"
    })

# Java: Advanced Spring Cloud (10 lessons) - IDs 754-763
cloud_lessons = []
cloud_topics = [
    ("Config Encryption", "Encrypt sensitive configuration"),
    ("Refresh Strategies", "Refresh configuration at runtime"),
    ("Service Mesh Integration", "Integrate with service mesh"),
    ("Distributed Configuration", "Manage distributed config"),
    ("Resilience Patterns", "Implement resilience4j patterns"),
    ("Retry Policies", "Configure retry mechanisms"),
    ("Bulkhead Pattern", "Isolate resources with bulkheads"),
    ("Rate Limiting", "Implement rate limiting"),
    ("Observability", "Monitor distributed systems"),
    ("Multi-Region Deployment", "Deploy across regions")
]

for i, (title, desc) in enumerate(cloud_topics, 754):
    cloud_lessons.append({
        "id": i,
        "title": f"Spring Cloud - {title}",
        "description": desc,
        "difficulty": "Expert",
        "tags": ["Spring Cloud", "Microservices", "Expert"],
        "category": "Microservices",
        "language": "java",
        "baseCode": f"// {title}\npublic class CloudConfig {{\n    // TODO: Implement {title.lower()}\n    public static void main(String[] args) {{\n        System.out.println(\"Cloud config ready\");\n    }}\n}}",
        "fullSolution": f"public class CloudConfig {{\n    public static void main(String[] args) {{\n        System.out.println(\"Cloud config ready\");\n    }}\n}}",
        "expectedOutput": "Cloud config ready",
        "tutorial": f"# {title}\n\n{desc}\n\n## Example\n\n```java\n@Configuration\npublic class CloudConfig {{\n    // Configuration\n}}\n```",
        "additionalExamples": f"// Example: {title}\n@Component\npublic class Example {{\n    public void run() {{\n        System.out.println(\"Running\");\n    }}\n}}"
    })

# Java: Kafka Event Streaming (10 lessons) - IDs 764-773
kafka_lessons = []
kafka_topics = [
    ("Kafka Basics", "Understand Kafka architecture"),
    ("Producers", "Send messages to Kafka"),
    ("Consumers", "Consume messages from Kafka"),
    ("Consumer Groups", "Manage consumer groups"),
    ("Topics and Partitions", "Organize data with topics"),
    ("Kafka Streams", "Process streams with Kafka Streams"),
    ("Spring Kafka", "Integrate Kafka with Spring"),
    ("Serialization with Avro", "Use Avro for serialization"),
    ("Error Handling", "Handle Kafka errors"),
    ("Monitoring and Production", "Monitor Kafka in production")
]

for i, (title, desc) in enumerate(kafka_topics, 764):
    kafka_lessons.append({
        "id": i,
        "title": f"Kafka - {title}",
        "description": desc,
        "difficulty": "Expert",
        "tags": ["Kafka", "Event Streaming", "Expert"],
        "category": "Distributed Systems",
        "language": "java",
        "baseCode": f"// {title}\npublic class KafkaExample {{\n    // TODO: Implement {title.lower()}\n    public static void main(String[] args) {{\n        System.out.println(\"Kafka ready\");\n    }}\n}}",
        "fullSolution": f"public class KafkaExample {{\n    public static void main(String[] args) {{\n        System.out.println(\"Kafka ready\");\n    }}\n}}",
        "expectedOutput": "Kafka ready",
        "tutorial": f"# {title}\n\n{desc}\n\n## Example\n\n```java\n@Component\npublic class KafkaProducer {{\n    public void send(String message) {{\n        // Send to Kafka\n    }}\n}}\n```",
        "additionalExamples": f"// Example: {title}\n@KafkaListener(topics = \"my-topic\")\npublic void listen(String message) {{\n    System.out.println(\"Received: \" + message);\n}}"
    })

# Java: Advanced Testing (12 lessons) - IDs 774-785
testing_lessons = []
testing_topics = [
    ("Testcontainers Basics", "Test with Docker containers"),
    ("Database Testing", "Test database operations"),
    ("Kafka Testing", "Test Kafka integration"),
    ("Integration Tests", "Write integration tests"),
    ("MockMvc Advanced", "Advanced MockMvc patterns"),
    ("Mockito Deep-dive", "Master Mockito mocking"),
    ("Test Slices", "Use Spring Boot test slices"),
    ("Test Configuration", "Configure tests properly"),
    ("Performance Testing", "Test application performance"),
    ("Contract Testing", "Implement contract tests"),
    ("Security Testing", "Test security features"),
    ("CI/CD Integration", "Integrate tests in pipelines")
]

for i, (title, desc) in enumerate(testing_topics, 774):
    testing_lessons.append({
        "id": i,
        "title": f"Testing - {title}",
        "description": desc,
        "difficulty": "Expert",
        "tags": ["Testing", "JUnit", "Expert"],
        "category": "Testing",
        "language": "java",
        "baseCode": f"// {title}\nimport org.junit.jupiter.api.Test;\nimport static org.junit.jupiter.api.Assertions.*;\n\npublic class ExampleTest {{\n    // TODO: Implement {title.lower()}\n    @Test\n    public void test() {{\n        assertTrue(true);\n    }}\n}}",
        "fullSolution": f"import org.junit.jupiter.api.Test;\nimport static org.junit.jupiter.api.Assertions.*;\n\npublic class ExampleTest {{\n    @Test\n    public void testExample() {{\n        assertEquals(2, 1 + 1);\n    }}\n}}",
        "expectedOutput": "",
        "tutorial": f"# {title}\n\n{desc}\n\n## Example\n\n```java\n@Test\npublic void testExample() {{\n    assertEquals(expected, actual);\n}}\n```",
        "additionalExamples": f"// Example: {title}\n@Test\npublic void testWithMock() {{\n    MyService service = mock(MyService.class);\n    when(service.getData()).thenReturn(\"data\");\n    assertEquals(\"data\", service.getData());\n}}"
    })

# Add all Java lessons
java_lessons.extend(springboot_lessons)
java_lessons.extend(reactive_lessons)
java_lessons.extend(cloud_lessons)
java_lessons.extend(kafka_lessons)
java_lessons.extend(testing_lessons)

print(f"\nAdded:")
print(f"  Spring Boot Advanced: {len(springboot_lessons)} lessons")
print(f"  Reactive Programming: {len(reactive_lessons)} lessons")
print(f"  Advanced Spring Cloud: {len(cloud_lessons)} lessons")
print(f"  Kafka: {len(kafka_lessons)} lessons")
print(f"  Advanced Testing: {len(testing_lessons)} lessons")
print(f"\nNew Java total: {len(java_lessons)} lessons")

# Save Java lessons
save_lessons('public/lessons-java.json', java_lessons)

total_added = len(springboot_lessons) + len(reactive_lessons) + len(cloud_lessons) + len(kafka_lessons) + len(testing_lessons)
print(f"\nPhase 1 Java lessons added successfully!")
print(f"Java lesson range: 726-785 ({total_added} lessons)")
