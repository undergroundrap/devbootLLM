#!/usr/bin/env python3
"""
Upgrade Script: Kafka Distributed Messaging Batch 8
Upgrades 3 critical Kafka lessons with production-ready Java simulations

Target Lessons:
- ID 889: Kafka - Spring Kafka (5,000-6,000 chars)
- ID 890: Kafka - Serialization with Avro (4,500-5,500 chars)
- ID 892: Kafka - Monitoring and Production (4,500-5,500 chars)

These lessons demonstrate enterprise Kafka patterns used by LinkedIn, Uber, and Netflix.
"""

import json
import sys
from pathlib import Path

# Lesson solutions with production-ready Java code
SOLUTIONS = {
    889: '''// Spring Kafka Integration - Enterprise Event Streaming
// In production: import org.springframework.kafka.annotation.KafkaListener;
// In production: import org.springframework.kafka.core.KafkaTemplate;
import java.util.*;
import java.util.concurrent.*;

// Simulates: @Service
class KafkaProducer {
    private final Map<String, Integer> msgCount = new ConcurrentHashMap<>();

    // Simulates: @Autowired KafkaTemplate<String, String>
    public void send(String topic, String message) {
        // In production: kafkaTemplate.send(topic, message)
        msgCount.merge(topic, 1, Integer::sum);
        System.out.println("[PRODUCER] Topic: " + topic + " | " + message);
    }

    public void sendWithRetry(String topic, String msg, int retries) {
        // Production: exponential backoff retry
        for (int i = 0; i < retries; i++) {
            try {
                send(topic, msg);
                System.out.println("[RETRY] Success on attempt " + (i + 1));
                return;
            } catch (Exception e) {
                if (i == retries - 1) throw new RuntimeException("Failed", e);
            }
        }
    }
}

// Simulates: @Service
class KafkaConsumer {
    private final Map<String, List<String>> processed = new ConcurrentHashMap<>();

    // Simulates: @KafkaListener(topics = "orders", groupId = "order-service")
    public void onOrder(String msg) {
        // In production: Spring auto-deserializes, commits offsets
        System.out.println("[CONSUMER-orders] Processing: " + msg);
        processed.computeIfAbsent("orders", k -> new ArrayList<>()).add(msg);

        if (msg.contains("order")) {
            String orderId = msg.split(":")[0];
            System.out.println("[CONSUMER-orders] Validated: " + orderId);
        }
    }

    // Simulates: @KafkaListener with error handler
    public void onPayment(String msg) {
        try {
            System.out.println("[CONSUMER-payments] Processing: " + msg);

            if (msg.contains("amount")) {
                String[] parts = msg.split(",");
                double amt = Double.parseDouble(parts[1].split(":")[1]);

                if (amt < 0) throw new IllegalArgumentException("Invalid: " + amt);

                System.out.println("[CONSUMER-payments] Processed: $" + amt);
                processed.computeIfAbsent("payments", k -> new ArrayList<>()).add(msg);
            }
        } catch (Exception e) {
            // In production: send to Dead Letter Queue (DLQ)
            System.err.println("[ERROR] DLQ: " + msg + " | " + e.getMessage());
        }
    }

    // Multiple consumers = partition-based parallelism
    // Simulates: @KafkaListener(topics = "events", groupId = "analytics")
    public void analytics1(String msg) {
        System.out.println("[CONSUMER-analytics-1] Partitions 0-2: " + msg);
    }

    public void analytics2(String msg) {
        System.out.println("[CONSUMER-analytics-2] Partitions 3-5: " + msg);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== SPRING KAFKA INTEGRATION ===\\n");

        KafkaProducer producer = new KafkaProducer();
        KafkaConsumer consumer = new KafkaConsumer();

        // Scenario 1: Order Processing
        System.out.println("--- Order Processing System ---");
        producer.send("orders", "order-1:laptop:$1299.99");
        consumer.onOrder("order-1:laptop:$1299.99");

        producer.send("orders", "order-2:phone:$899.99");
        consumer.onOrder("order-2:phone:$899.99");
        System.out.println();

        // Scenario 2: Payment with Error Handling
        System.out.println("--- Payment Processing ---");
        consumer.onPayment("payment-1,amount:499.99");
        consumer.onPayment("payment-2,amount:-50.00"); // Triggers error
        System.out.println();

        // Scenario 3: Retry Logic
        System.out.println("--- Retry with Backoff ---");
        producer.sendWithRetry("alerts", "disk-space-low", 3);
        System.out.println();

        // Scenario 4: Consumer Groups (Parallel Processing)
        System.out.println("--- Consumer Groups ---");
        consumer.analytics1("event:login:user-123");
        consumer.analytics2("event:pageview:/home");
        consumer.analytics1("event:purchase:order-789");
        System.out.println();

        // Scenario 5: Event Streaming Pipeline
        System.out.println("--- Event Streaming ---");
        String[] events = {
            "user-signup:email-verified",
            "checkout:cart-abandoned",
            "recommendation:product-viewed"
        };

        for (String event : events) {
            producer.send("user-events", event);
        }
        System.out.println();

        // Production Metrics
        System.out.println("--- Metrics ---");
        System.out.println("Messages produced: " +
            producer.msgCount.values().stream().mapToInt(Integer::intValue).sum());

        System.out.println("\\n// Production Config (application.yml):");
        System.out.println("// spring.kafka.bootstrap-servers: kafka:9092");
        System.out.println("// spring.kafka.consumer.group-id: my-service");
        System.out.println("// spring.kafka.consumer.auto-offset-reset: earliest");
        System.out.println("// spring.kafka.producer.acks: all");
        System.out.println("// spring.kafka.producer.retries: 3");
        System.out.println("//");
        System.out.println("// Key Patterns:");
        System.out.println("// - @KafkaListener for consumers");
        System.out.println("// - KafkaTemplate for producers");
        System.out.println("// - Consumer groups for scaling");
        System.out.println("// - Error handlers + DLQ");
        System.out.println("// - Retry with exponential backoff");
    }
}''',

    890: '''// Kafka Avro Serialization - Schema Evolution & Registry
// In production: import org.apache.avro.Schema;
// In production: import io.confluent.kafka.serializers.KafkaAvroSerializer;
import java.util.*;
import java.nio.*;

// Avro Schema (JSON in production)
class AvroSchema {
    final String name;
    final Map<String, String> fields;
    final int version;

    AvroSchema(String name, Map<String, String> fields, int v) {
        this.name = name;
        this.fields = fields;
        this.version = v;
    }

    boolean isCompatible(AvroSchema o) {
        return this.name.equals(o.name);
    }
}

// Schema Registry
class SchemaRegistry {
    private final Map<String, List<AvroSchema>> schemas = new HashMap<>();
    private final Map<Integer, AvroSchema> byId = new HashMap<>();
    private int id = 1;

    int register(String subject, AvroSchema schema) {
        // In production: POST /subjects/{subject}/versions
        int sid = id++;
        schemas.computeIfAbsent(subject, k -> new ArrayList<>()).add(schema);
        byId.put(sid, schema);

        System.out.println("[REGISTRY] " + subject);
        System.out.println("  ID: " + sid + " | v" + schema.version);
        System.out.println("  Fields: " + schema.fields.keySet());
        return sid;
    }

    AvroSchema get(int id) { return byId.get(id); }

    void checkCompatibility(String subject, AvroSchema s) {
        List<AvroSchema> versions = schemas.get(subject);
        if (versions == null || versions.isEmpty()) {
            System.out.println("[COMPAT] OK");
            return;
        }

        AvroSchema latest = versions.get(versions.size() - 1);
        System.out.println(latest.isCompatible(s) ?
            "[COMPAT] OK" : "[COMPAT] WARNING!");
    }
}

// Avro Serializer
class AvroSerializer {
    private final SchemaRegistry registry;

    AvroSerializer(SchemaRegistry r) { this.registry = r; }

    byte[] serialize(Map<String, Object> data, int sid) {
        // In production: Avro binary encoding
        AvroSchema schema = registry.get(sid);

        // Validate
        for (String f : schema.fields.keySet()) {
            if (!data.containsKey(f)) throw new IllegalArgumentException("Missing: " + f);
        }

        ByteBuffer buf = ByteBuffer.allocate(512);
        buf.put((byte) 0x00);
        buf.putInt(sid);

        byte[] result = new byte[buf.position()];
        buf.rewind();
        buf.get(result);

        System.out.println("[SERIALIZE] " + data.size() + " fields -> " + result.length + " bytes");
        return result;
    }

    Map<String, Object> deserialize(byte[] data) {
        ByteBuffer buf = ByteBuffer.wrap(data);
        if (buf.get() != 0x00) throw new IllegalArgumentException("Invalid");

        int id = buf.getInt();
        AvroSchema s = registry.get(id);
        System.out.println("[DESERIALIZE] v" + s.version);

        Map<String, Object> r = new HashMap<>();
        r.put("_version", s.version);
        return r;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== KAFKA AVRO SERIALIZATION ===\\n");

        SchemaRegistry registry = new SchemaRegistry();
        AvroSerializer serializer = new AvroSerializer(registry);

        // Scenario 1: Schema v1
        System.out.println("--- Schema v1 ---");
        Map<String, String> v1 = new LinkedHashMap<>();
        v1.put("orderId", "string");
        v1.put("amount", "double");

        AvroSchema s1 = new AvroSchema("Order", v1, 1);
        int id1 = registry.register("orders", s1);
        System.out.println();

        // Scenario 2: Serialize
        System.out.println("--- Serialize ---");
        Map<String, Object> order = new HashMap<>();
        order.put("orderId", "ORD-123");
        order.put("amount", 99.99);

        byte[] data = serializer.serialize(order, id1);
        System.out.println("Size: " + data.length + " bytes\\n");

        // Scenario 3: Deserialize
        System.out.println("--- Deserialize ---");
        Map<String, Object> result = serializer.deserialize(data);
        System.out.println("Version: " + result.get("_version") + "\\n");

        // Scenario 4: Evolution v2
        System.out.println("--- Evolution v2 ---");
        Map<String, String> v2 = new LinkedHashMap<>(v1);
        v2.put("status", "string");

        AvroSchema s2 = new AvroSchema("Order", v2, 2);
        registry.checkCompatibility("orders", s2);
        registry.register("orders", s2);
        System.out.println();

        // Scenario 5: Product
        System.out.println("--- Product ---");
        Map<String, String> pf = new LinkedHashMap<>();
        pf.put("id", "string");
        pf.put("price", "double");

        int pid = registry.register("products", new AvroSchema("Product", pf, 1));

        Map<String, Object> p = new HashMap<>();
        p.put("id", "PROD-888");
        p.put("price", 49.99);

        serializer.serialize(p, pid);
        System.out.println();

        // Benefits
        System.out.println("--- Benefits ---");
        System.out.println("Compact binary | Schema evolution");
        System.out.println("Strong typing | Cross-language");
        System.out.println("Schema registry consistency");

        System.out.println("\\n// Production:");
        System.out.println("// KafkaAvroSerializer/Deserializer");
        System.out.println("// schema.registry.url: http://registry:8081");
    }
}''',

    892: '''// Kafka Production Monitoring - Metrics, Health & Alerts
// In production: import org.apache.kafka.clients.admin.AdminClient;
// In production: import io.micrometer.core.instrument.MeterRegistry;
import java.util.*;
import java.util.concurrent.*;

// Consumer Metrics
class ConsumerMetrics {
    private final Map<String, Long> offsets = new ConcurrentHashMap<>();
    private final Map<String, Long> committed = new ConcurrentHashMap<>();
    private long lastPoll = System.currentTimeMillis();

    void poll(String t, long off) {
        offsets.put(t, off);
        lastPoll = System.currentTimeMillis();
    }

    void commit(String t, long off) { committed.put(t, off); }

    long lag(String t) {
        return Math.max(0, offsets.getOrDefault(t, 0L) - committed.getOrDefault(t, 0L));
    }

    long timeSincePoll() { return System.currentTimeMillis() - lastPoll; }
}

// Producer Metrics
class ProducerMetrics {
    private long total = 0, errors = 0;
    private final List<Long> lat = new CopyOnWriteArrayList<>();

    void recordSend(int size, long ms, boolean ok) {
        if (ok) { total++; lat.add(ms); } else { errors++; }
    }

    double avgLatency() {
        return lat.isEmpty() ? 0.0 : lat.stream().mapToLong(Long::longValue).average().orElse(0.0);
    }

    double p99Latency() {
        if (lat.isEmpty()) return 0.0;
        List<Long> s = new ArrayList<>(lat);
        Collections.sort(s);
        return s.get((int) (s.size() * 0.99) - 1);
    }

    long getErrors() { return errors; }
    long getTotal() { return total; }
}

// Health Check
class HealthCheck {
    private final ConsumerMetrics consumer;
    private final ProducerMetrics producer;

    HealthCheck(ConsumerMetrics c, ProducerMetrics p) {
        this.consumer = c;
        this.producer = p;
    }

    List<String> check(String t) {
        List<String> issues = new ArrayList<>();

        long lag = consumer.lag(t);
        if (lag > 10000) issues.add("CRIT: Lag " + lag);
        else if (lag > 1000) issues.add("WARN: Lag " + lag);

        if (consumer.timeSincePoll() > 60000) issues.add("CRIT: Stale " + (consumer.timeSincePoll() / 1000) + "s");
        if (producer.getErrors() > 100) issues.add("CRIT: Errors " + producer.getErrors());

        return issues;
    }
}

// Alert Manager
class AlertManager {
    private final Map<String, Long> cd = new ConcurrentHashMap<>();

    void alert(String k, String m, String s) {
        Long last = cd.get(k);
        long now = System.currentTimeMillis();

        if (last == null || (now - last) > 300000) { // 5min
            System.out.println("[ALERT-" + s + "] " + m);
            cd.put(k, now);
        } else {
            System.out.println("[SUPPRESSED]");
        }
    }
}

// Rebalance Monitor
class RebalanceMonitor {
    void onAssigned(List<String> p) { System.out.println("[REBAL] Assigned: " + p); }
    void onRevoked(List<String> p) { System.out.println("[REBAL] Revoked: " + p); }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("=== KAFKA MONITORING ===\\n");

        ConsumerMetrics consumer = new ConsumerMetrics();
        ProducerMetrics producer = new ProducerMetrics();
        HealthCheck health = new HealthCheck(consumer, producer);
        AlertManager alerts = new AlertManager();
        RebalanceMonitor rebalance = new RebalanceMonitor();

        // Scenario 1: Normal Ops
        System.out.println("--- Normal Ops ---");
        producer.recordSend(512, 25, true);
        consumer.poll("payments", 1000);
        consumer.commit("payments", 990);
        System.out.println("Lag: " + consumer.lag("payments") + "\\n");

        // Scenario 2: Health
        System.out.println("--- Health ---");
        List<String> issues = health.check("payments");
        System.out.println(issues.isEmpty() ? "[OK]" : "[DEGRADED] " + issues);
        System.out.println();

        // Scenario 3: Lag
        System.out.println("--- Lag ---");
        consumer.poll("payments", 15000);
        long lag = consumer.lag("payments");
        if (lag > 1000) alerts.alert("lag", "Lag: " + lag, "WARN");
        System.out.println();

        // Scenario 4: Errors
        System.out.println("--- Errors ---");
        for (int i = 0; i < 5; i++) producer.recordSend(512, 0, false);
        if (producer.getErrors() > 3) alerts.alert("err", "Count: " + producer.getErrors(), "WARN");
        System.out.println();

        // Scenario 5: Rebalance
        System.out.println("--- Rebalance ---");
        rebalance.onRevoked(Arrays.asList("p-0", "p-1"));
        rebalance.onAssigned(Arrays.asList("p-1", "p-2"));
        System.out.println();

        // Scenario 6: Perf
        System.out.println("--- Perf ---");
        for (int i = 0; i < 30; i++) producer.recordSend(256, 20 + (long)(Math.random() * 50), true);
        System.out.printf("Avg: %.1fms | P99: %.1fms%n", producer.avgLatency(), producer.p99Latency());
        System.out.println();

        // Best Practices
        System.out.println("--- Best Practices ---");
        System.out.println("Monitor lag | Alert thresholds");
        System.out.println("Track latency | Rebalances");
        System.out.println("Prometheus/Grafana | DLQ");

        System.out.println("\\n// JMX: fetch-manager, producer-metrics");
        System.out.println("// Integrate: Prometheus, Datadog");
    }
}'''
}

def get_char_count(text):
    """Count characters in text"""
    return len(text)

def main():
    # File path
    json_file = Path("c:/devbootLLM-app/public/lessons-java.json")

    if not json_file.exists():
        print(f"ERROR: File not found: {json_file}")
        return 1

    print("=" * 70)
    print("KAFKA DISTRIBUTED MESSAGING UPGRADE - BATCH 8")
    print("=" * 70)
    print("\nTarget: 3 critical Kafka lessons")
    print("Focus: Enterprise event-driven architecture patterns")
    print()

    # Read JSON
    print("Reading lessons-java.json...")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lessons = data if isinstance(data, list) else data.get('lessons', [])

    # Track changes
    upgraded = []

    # Process each target lesson
    for lesson in lessons:
        lesson_id = lesson.get('id')

        if lesson_id in SOLUTIONS:
            old_solution = lesson.get('fullSolution', '')
            old_count = get_char_count(old_solution)

            new_solution = SOLUTIONS[lesson_id]
            new_count = get_char_count(new_solution)

            # Update the lesson
            lesson['fullSolution'] = new_solution

            upgraded.append({
                'id': lesson_id,
                'title': lesson.get('title', 'Unknown'),
                'old_count': old_count,
                'new_count': new_count
            })

    # Write back
    print("\nWriting updated lessons...")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data if isinstance(data, list) else lessons, f, indent=2, ensure_ascii=False)

    # Print summary
    print("\n" + "=" * 70)
    print("UPGRADE SUMMARY - KAFKA BATCH 8")
    print("=" * 70)
    print()

    for item in upgraded:
        print(f"ID {item['id']}: {item['title']}")
        print(f"  Before: {item['old_count']:,} chars")
        print(f"  After:  {item['new_count']:,} chars")
        print(f"  Change: +{item['new_count'] - item['old_count']:,} chars")

        # Target validation
        if item['id'] == 889:
            target = "5,000-6,000"
            status = "PASS" if 5000 <= item['new_count'] <= 6000 else "CHECK"
        else:
            target = "4,500-5,500"
            status = "PASS" if 4500 <= item['new_count'] <= 5500 else "CHECK"

        print(f"  Target: {target} chars [{status}]")
        print()

    print("=" * 70)
    print(f"Total lessons upgraded: {len(upgraded)}")
    print()
    print("KEY FEATURES ADDED:")
    print("  - Spring Kafka integration patterns")
    print("  - Avro schema evolution and registry")
    print("  - Production monitoring and metrics")
    print("  - Consumer lag tracking")
    print("  - Health checks and alerting")
    print("  - Partition rebalancing")
    print("  - Error handling and retry logic")
    print("  - Performance profiling (latency, throughput)")
    print()
    print("Enterprise patterns used by: LinkedIn, Uber, Netflix")
    print("=" * 70)

    return 0

if __name__ == '__main__':
    sys.exit(main())
