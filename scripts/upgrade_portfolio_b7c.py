#!/usr/bin/env python3
"""
Upgrade Script: Batch 7c - Java Portfolio Projects
Upgrades 2 critical portfolio projects with production-ready implementations
"""

import json
import sys
from pathlib import Path

# Lesson implementations
LESSON_802_CONTENT = r'''
# Portfolio: Todo List REST API

In this portfolio project, you'll build a **production-ready REST API** for managing a todo list. This project demonstrates your ability to design and implement a complete backend system with proper architecture, validation, error handling, and RESTful principles - skills that are essential in professional software development.

## 🎯 Learning Objectives
By completing this project, you will:
- Design and implement a complete REST API with full CRUD operations
- Build a multi-layer architecture (Controller → Service → Repository)
- Implement proper input validation and error handling
- Use appropriate HTTP status codes and response formats
- Manage application state with in-memory data storage
- Handle edge cases and invalid requests gracefully
- Write production-quality code that follows industry best practices

## 📚 Concept: REST API Architecture

A **REST API** (Representational State Transfer API) is a set of endpoints that allow clients to interact with server resources using standard HTTP methods. Professional REST APIs follow a layered architecture:

**Controller Layer**: Handles HTTP requests and responses
- Defines API endpoints (routes)
- Parses request data
- Returns appropriate HTTP status codes
- Delegates business logic to the service layer

**Service Layer**: Contains business logic
- Validates input data
- Implements application rules
- Coordinates data operations
- Throws exceptions for error cases

**Repository/Data Layer**: Manages data persistence
- Stores and retrieves data
- Provides data access methods
- Abstracts storage implementation

**Common HTTP Methods**:
- `GET`: Retrieve resources
- `POST`: Create new resources
- `PUT`: Update existing resources
- `DELETE`: Remove resources

**Standard HTTP Status Codes**:
- `200 OK`: Successful GET/PUT/DELETE
- `201 Created`: Successful POST
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Resource doesn't exist
- `500 Internal Server Error`: Server error

## 💡 Real-World Application

REST APIs are the backbone of modern web applications:
- **Mobile Apps**: Todo apps like Todoist, Microsoft To Do
- **Web Applications**: Trello, Asana, JIRA (task management)
- **Microservices**: Breaking large applications into smaller services
- **Third-Party Integrations**: Allowing other apps to interact with your service

Companies like Google, Amazon, and Facebook use REST APIs to enable billions of requests per day across their platforms.

## 🔨 Implementation

In this project, we simulate a Spring Boot REST API using Java's standard libraries. In a real Spring Boot application, you would use annotations like `@RestController`, `@GetMapping`, `@PostMapping`, etc., but here we demonstrate the core concepts and logic.

```java
import java.time.LocalDate;
import java.time.format.DateTimeParseException;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;

// ============================================================================
// MODEL LAYER
// ============================================================================

/**
 * Todo entity representing a task in the system.
 * In Spring Boot, this would be annotated with @Entity for JPA persistence.
 */
class Todo {
    private Long id;
    private String title;
    private String description;
    private TodoStatus status;
    private LocalDate dueDate;
    private LocalDate createdAt;

    public Todo() {
        this.createdAt = LocalDate.now();
        this.status = TodoStatus.PENDING;
    }

    public Todo(Long id, String title, String description, LocalDate dueDate) {
        this();
        this.id = id;
        this.title = title;
        this.description = description;
        this.dueDate = dueDate;
    }

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public TodoStatus getStatus() { return status; }
    public void setStatus(TodoStatus status) { this.status = status; }

    public LocalDate getDueDate() { return dueDate; }
    public void setDueDate(LocalDate dueDate) { this.dueDate = dueDate; }

    public LocalDate getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDate createdAt) { this.createdAt = createdAt; }

    @Override
    public String toString() {
        return String.format("Todo{id=%d, title='%s', status=%s, dueDate=%s}",
            id, title, status, dueDate);
    }
}

/**
 * Enum representing the lifecycle states of a todo item.
 */
enum TodoStatus {
    PENDING,
    IN_PROGRESS,
    COMPLETED
}

/**
 * DTO (Data Transfer Object) for creating new todos.
 * Separates API input from internal entity model.
 */
class CreateTodoRequest {
    private String title;
    private String description;
    private String dueDate; // String to handle parsing and validation

    public CreateTodoRequest(String title, String description, String dueDate) {
        this.title = title;
        this.description = description;
        this.dueDate = dueDate;
    }

    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public String getDueDate() { return dueDate; }
}

/**
 * DTO for updating existing todos.
 */
class UpdateTodoRequest {
    private String title;
    private String description;
    private String status;
    private String dueDate;

    public UpdateTodoRequest(String title, String description, String status, String dueDate) {
        this.title = title;
        this.description = description;
        this.status = status;
        this.dueDate = dueDate;
    }

    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public String getStatus() { return status; }
    public String getDueDate() { return dueDate; }
}

/**
 * Standard API response wrapper.
 * Provides consistent response format across all endpoints.
 */
class ApiResponse<T> {
    private boolean success;
    private T data;
    private String message;
    private int statusCode;

    public ApiResponse(boolean success, T data, String message, int statusCode) {
        this.success = success;
        this.data = data;
        this.message = message;
        this.statusCode = statusCode;
    }

    public static <T> ApiResponse<T> success(T data, int statusCode) {
        return new ApiResponse<>(true, data, null, statusCode);
    }

    public static <T> ApiResponse<T> error(String message, int statusCode) {
        return new ApiResponse<>(false, null, message, statusCode);
    }

    public boolean isSuccess() { return success; }
    public T getData() { return data; }
    public String getMessage() { return message; }
    public int getStatusCode() { return statusCode; }
}

// ============================================================================
// REPOSITORY LAYER
// ============================================================================

/**
 * Repository for Todo data access.
 * In Spring Boot, this would be an interface extending JpaRepository.
 * Here we use an in-memory HashMap to simulate database operations.
 */
class TodoRepository {
    private final Map<Long, Todo> database = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    /**
     * Save a new todo or update an existing one.
     */
    public Todo save(Todo todo) {
        if (todo.getId() == null) {
            todo.setId(idGenerator.getAndIncrement());
        }
        database.put(todo.getId(), todo);
        return todo;
    }

    /**
     * Find todo by ID.
     */
    public Optional<Todo> findById(Long id) {
        return Optional.ofNullable(database.get(id));
    }

    /**
     * Find all todos.
     */
    public List<Todo> findAll() {
        return new ArrayList<>(database.values());
    }

    /**
     * Find todos by status.
     */
    public List<Todo> findByStatus(TodoStatus status) {
        return database.values().stream()
            .filter(todo -> todo.getStatus() == status)
            .collect(Collectors.toList());
    }

    /**
     * Delete todo by ID.
     */
    public boolean deleteById(Long id) {
        return database.remove(id) != null;
    }

    /**
     * Check if todo exists.
     */
    public boolean existsById(Long id) {
        return database.containsKey(id);
    }
}

// ============================================================================
// SERVICE LAYER
// ============================================================================

/**
 * Service layer containing business logic for todo operations.
 * In Spring Boot, this would be annotated with @Service.
 */
class TodoService {
    private final TodoRepository repository;

    public TodoService(TodoRepository repository) {
        this.repository = repository;
    }

    /**
     * Create a new todo with validation.
     */
    public Todo createTodo(CreateTodoRequest request) {
        // Validate required fields
        if (request.getTitle() == null || request.getTitle().trim().isEmpty()) {
            throw new ValidationException("Title is required");
        }

        if (request.getTitle().length() > 100) {
            throw new ValidationException("Title must be 100 characters or less");
        }

        // Parse and validate due date
        LocalDate dueDate = null;
        if (request.getDueDate() != null && !request.getDueDate().isEmpty()) {
            try {
                dueDate = LocalDate.parse(request.getDueDate());
                if (dueDate.isBefore(LocalDate.now())) {
                    throw new ValidationException("Due date cannot be in the past");
                }
            } catch (DateTimeParseException e) {
                throw new ValidationException("Invalid date format. Use YYYY-MM-DD");
            }
        }

        // Create and save todo
        Todo todo = new Todo();
        todo.setTitle(request.getTitle().trim());
        todo.setDescription(request.getDescription() != null ? request.getDescription().trim() : "");
        todo.setDueDate(dueDate);

        return repository.save(todo);
    }

    /**
     * Get all todos.
     */
    public List<Todo> getAllTodos() {
        return repository.findAll();
    }

    /**
     * Get todo by ID.
     */
    public Todo getTodoById(Long id) {
        return repository.findById(id)
            .orElseThrow(() -> new TodoNotFoundException("Todo not found with id: " + id));
    }

    /**
     * Get todos filtered by status.
     */
    public List<Todo> getTodosByStatus(TodoStatus status) {
        return repository.findByStatus(status);
    }

    /**
     * Update an existing todo.
     */
    public Todo updateTodo(Long id, UpdateTodoRequest request) {
        Todo todo = getTodoById(id); // Throws if not found

        // Update title if provided
        if (request.getTitle() != null) {
            if (request.getTitle().trim().isEmpty()) {
                throw new ValidationException("Title cannot be empty");
            }
            if (request.getTitle().length() > 100) {
                throw new ValidationException("Title must be 100 characters or less");
            }
            todo.setTitle(request.getTitle().trim());
        }

        // Update description if provided
        if (request.getDescription() != null) {
            todo.setDescription(request.getDescription().trim());
        }

        // Update status if provided
        if (request.getStatus() != null) {
            try {
                TodoStatus status = TodoStatus.valueOf(request.getStatus().toUpperCase());
                todo.setStatus(status);
            } catch (IllegalArgumentException e) {
                throw new ValidationException("Invalid status. Must be PENDING, IN_PROGRESS, or COMPLETED");
            }
        }

        // Update due date if provided
        if (request.getDueDate() != null && !request.getDueDate().isEmpty()) {
            try {
                LocalDate dueDate = LocalDate.parse(request.getDueDate());
                if (dueDate.isBefore(LocalDate.now()) && todo.getStatus() != TodoStatus.COMPLETED) {
                    throw new ValidationException("Due date cannot be in the past for incomplete todos");
                }
                todo.setDueDate(dueDate);
            } catch (DateTimeParseException e) {
                throw new ValidationException("Invalid date format. Use YYYY-MM-DD");
            }
        }

        return repository.save(todo);
    }

    /**
     * Delete a todo by ID.
     */
    public void deleteTodo(Long id) {
        if (!repository.existsById(id)) {
            throw new TodoNotFoundException("Todo not found with id: " + id);
        }
        repository.deleteById(id);
    }
}

// ============================================================================
// EXCEPTION CLASSES
// ============================================================================

class TodoNotFoundException extends RuntimeException {
    public TodoNotFoundException(String message) {
        super(message);
    }
}

class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}

// ============================================================================
// CONTROLLER LAYER
// ============================================================================

/**
 * REST Controller for Todo API endpoints.
 * In Spring Boot, this would be annotated with @RestController and @RequestMapping("/api/todos").
 * Methods would use @GetMapping, @PostMapping, @PutMapping, @DeleteMapping.
 */
class TodoController {
    private final TodoService service;

    public TodoController(TodoService service) {
        this.service = service;
    }

    /**
     * GET /api/todos
     * Get all todos, optionally filtered by status.
     */
    public ApiResponse<List<Todo>> getAllTodos(String status) {
        try {
            List<Todo> todos;
            if (status != null && !status.isEmpty()) {
                TodoStatus todoStatus = TodoStatus.valueOf(status.toUpperCase());
                todos = service.getTodosByStatus(todoStatus);
            } else {
                todos = service.getAllTodos();
            }
            return ApiResponse.success(todos, 200);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error("Invalid status parameter", 400);
        } catch (Exception e) {
            return ApiResponse.error("Internal server error", 500);
        }
    }

    /**
     * GET /api/todos/{id}
     * Get a specific todo by ID.
     */
    public ApiResponse<Todo> getTodoById(Long id) {
        try {
            Todo todo = service.getTodoById(id);
            return ApiResponse.success(todo, 200);
        } catch (TodoNotFoundException e) {
            return ApiResponse.error(e.getMessage(), 404);
        } catch (Exception e) {
            return ApiResponse.error("Internal server error", 500);
        }
    }

    /**
     * POST /api/todos
     * Create a new todo.
     */
    public ApiResponse<Todo> createTodo(CreateTodoRequest request) {
        try {
            Todo todo = service.createTodo(request);
            return ApiResponse.success(todo, 201);
        } catch (ValidationException e) {
            return ApiResponse.error(e.getMessage(), 400);
        } catch (Exception e) {
            return ApiResponse.error("Internal server error", 500);
        }
    }

    /**
     * PUT /api/todos/{id}
     * Update an existing todo.
     */
    public ApiResponse<Todo> updateTodo(Long id, UpdateTodoRequest request) {
        try {
            Todo todo = service.updateTodo(id, request);
            return ApiResponse.success(todo, 200);
        } catch (TodoNotFoundException e) {
            return ApiResponse.error(e.getMessage(), 404);
        } catch (ValidationException e) {
            return ApiResponse.error(e.getMessage(), 400);
        } catch (Exception e) {
            return ApiResponse.error("Internal server error", 500);
        }
    }

    /**
     * DELETE /api/todos/{id}
     * Delete a todo.
     */
    public ApiResponse<Void> deleteTodo(Long id) {
        try {
            service.deleteTodo(id);
            return ApiResponse.success(null, 200);
        } catch (TodoNotFoundException e) {
            return ApiResponse.error(e.getMessage(), 404);
        } catch (Exception e) {
            return ApiResponse.error("Internal server error", 500);
        }
    }
}

// ============================================================================
// DEMO APPLICATION
// ============================================================================

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Todo List REST API Demo ===\n");

        // Initialize application layers
        TodoRepository repository = new TodoRepository();
        TodoService service = new TodoService(repository);
        TodoController controller = new TodoController(service);

        // Demo 1: Create todos (POST /api/todos)
        System.out.println("1. Creating todos (POST /api/todos):");

        CreateTodoRequest req1 = new CreateTodoRequest(
            "Complete project documentation",
            "Write comprehensive README and API docs",
            "2025-12-15"
        );
        ApiResponse<Todo> response1 = controller.createTodo(req1);
        printResponse("POST /api/todos", response1);

        CreateTodoRequest req2 = new CreateTodoRequest(
            "Review pull requests",
            "Review and merge pending PRs from team",
            "2025-12-10"
        );
        ApiResponse<Todo> response2 = controller.createTodo(req2);
        printResponse("POST /api/todos", response2);

        CreateTodoRequest req3 = new CreateTodoRequest(
            "Fix authentication bug",
            "Users unable to login with Google OAuth",
            "2025-12-05"
        );
        ApiResponse<Todo> response3 = controller.createTodo(req3);
        printResponse("POST /api/todos", response3);

        // Demo 2: Validation errors
        System.out.println("\n2. Testing validation (POST with invalid data):");

        CreateTodoRequest invalidReq = new CreateTodoRequest("", "No title", "2025-12-01");
        ApiResponse<Todo> errorResponse = controller.createTodo(invalidReq);
        printResponse("POST /api/todos (empty title)", errorResponse);

        CreateTodoRequest pastDateReq = new CreateTodoRequest(
            "Past due date",
            "Testing past date",
            "2020-01-01"
        );
        ApiResponse<Todo> pastResponse = controller.createTodo(pastDateReq);
        printResponse("POST /api/todos (past date)", pastResponse);

        // Demo 3: Get all todos (GET /api/todos)
        System.out.println("\n3. Retrieving all todos (GET /api/todos):");
        ApiResponse<List<Todo>> allTodos = controller.getAllTodos(null);
        printResponse("GET /api/todos", allTodos);
        if (allTodos.isSuccess()) {
            allTodos.getData().forEach(todo ->
                System.out.println("  - " + todo)
            );
        }

        // Demo 4: Get specific todo (GET /api/todos/{id})
        System.out.println("\n4. Retrieving specific todo (GET /api/todos/2):");
        ApiResponse<Todo> specificTodo = controller.getTodoById(2L);
        printResponse("GET /api/todos/2", specificTodo);

        // Demo 5: Update todo status (PUT /api/todos/{id})
        System.out.println("\n5. Updating todo status (PUT /api/todos/1):");
        UpdateTodoRequest updateReq = new UpdateTodoRequest(null, null, "IN_PROGRESS", null);
        ApiResponse<Todo> updateResponse = controller.updateTodo(1L, updateReq);
        printResponse("PUT /api/todos/1", updateResponse);

        System.out.println("\n6. Marking todo as completed (PUT /api/todos/3):");
        UpdateTodoRequest completeReq = new UpdateTodoRequest(null, null, "COMPLETED", null);
        ApiResponse<Todo> completeResponse = controller.updateTodo(3L, completeReq);
        printResponse("PUT /api/todos/3", completeResponse);

        // Demo 6: Filter by status (GET /api/todos?status=PENDING)
        System.out.println("\n7. Filtering by status (GET /api/todos?status=PENDING):");
        ApiResponse<List<Todo>> pendingTodos = controller.getAllTodos("PENDING");
        printResponse("GET /api/todos?status=PENDING", pendingTodos);
        if (pendingTodos.isSuccess()) {
            pendingTodos.getData().forEach(todo ->
                System.out.println("  - " + todo)
            );
        }

        // Demo 7: Update multiple fields
        System.out.println("\n8. Updating multiple fields (PUT /api/todos/2):");
        UpdateTodoRequest multiUpdateReq = new UpdateTodoRequest(
            "Review and merge pull requests",
            "Priority: High priority PRs need review today",
            "IN_PROGRESS",
            "2025-12-08"
        );
        ApiResponse<Todo> multiUpdateResponse = controller.updateTodo(2L, multiUpdateReq);
        printResponse("PUT /api/todos/2", multiUpdateResponse);

        // Demo 8: Error handling - not found
        System.out.println("\n9. Testing error handling (GET /api/todos/999):");
        ApiResponse<Todo> notFound = controller.getTodoById(999L);
        printResponse("GET /api/todos/999", notFound);

        // Demo 9: Delete todo (DELETE /api/todos/{id})
        System.out.println("\n10. Deleting todo (DELETE /api/todos/3):");
        ApiResponse<Void> deleteResponse = controller.deleteTodo(3L);
        printResponse("DELETE /api/todos/3", deleteResponse);

        // Demo 10: Verify deletion
        System.out.println("\n11. Verifying deletion (GET /api/todos):");
        ApiResponse<List<Todo>> finalTodos = controller.getAllTodos(null);
        printResponse("GET /api/todos", finalTodos);
        if (finalTodos.isSuccess()) {
            System.out.println("Remaining todos: " + finalTodos.getData().size());
            finalTodos.getData().forEach(todo ->
                System.out.println("  - " + todo)
            );
        }

        System.out.println("\n=== Demo Complete ===");
    }

    private static <T> void printResponse(String endpoint, ApiResponse<T> response) {
        System.out.printf("  %s -> Status: %d, Success: %s%n",
            endpoint, response.getStatusCode(), response.isSuccess());
        if (!response.isSuccess()) {
            System.out.println("  Error: " + response.getMessage());
        }
    }
}
```

## 🎓 What You've Learned

This portfolio project demonstrates several professional software development skills:

1. **Layered Architecture**: Separation of concerns with Controller, Service, and Repository layers
2. **RESTful Design**: Proper use of HTTP methods and status codes
3. **Input Validation**: Comprehensive validation of user input with meaningful error messages
4. **Error Handling**: Graceful handling of exceptions with appropriate HTTP responses
5. **Data Modeling**: Well-designed entity and DTO classes
6. **Business Logic**: Status transitions, date validation, and business rules
7. **Clean Code**: Readable, well-documented code following Java conventions

## 💼 Interview Talking Points

When discussing this project in interviews, highlight:
- "Implemented a complete REST API with full CRUD operations"
- "Designed a three-layer architecture following separation of concerns"
- "Added comprehensive input validation and error handling"
- "Used DTOs to separate API contracts from internal models"
- "Implemented proper HTTP status codes (200, 201, 400, 404)"
- "Validated business rules like preventing past due dates"

## 🚀 Extensions

Enhance this project further:
1. Add pagination for large todo lists
2. Implement sorting (by due date, status, creation date)
3. Add todo categories/tags
4. Implement search functionality
5. Add user authentication and authorization
6. Persist data to a database using JPA
7. Add unit tests with JUnit and Mockito
8. Deploy as a real Spring Boot application
9. Add API documentation with Swagger/OpenAPI
10. Implement rate limiting and security headers
'''

LESSON_998_CONTENT = r'''
# Final Capstone: Task Management System

Welcome to your **final capstone project** - a comprehensive task management system that showcases everything you've learned throughout this course. This is an **enterprise-grade application** that demonstrates your ability to build complex, production-ready software systems.

This project is your **ultimate portfolio piece** - the kind of project that impresses hiring managers and demonstrates you have real-world development skills.

## 🎯 Learning Objectives

By completing this capstone, you will:
- Design and implement a multi-entity system with complex relationships
- Build advanced features like user management, project organization, and role-based access
- Implement sophisticated business logic and workflow management
- Handle complex queries and data filtering
- Create comprehensive APIs for enterprise-level applications
- Demonstrate mastery of object-oriented design and software architecture
- Build a system that showcases professional development practices

## 📚 Concept: Enterprise Task Management Systems

**Task Management Systems** are sophisticated applications used by teams and organizations to organize work, track progress, and collaborate effectively. Unlike simple todo lists, these systems include:

**Multi-Entity Architecture**:
- **Users**: People who create and complete tasks
- **Projects**: Containers for organizing related tasks
- **Tasks**: Work items with detailed metadata
- **Comments**: Communication and collaboration on tasks

**Advanced Features**:
- **Role-Based Access Control (RBAC)**: Different permissions for different user roles
- **Priority Management**: Critical tasks get handled first
- **Workflow States**: Tasks move through defined stages
- **Assignment System**: Tasks are assigned to specific users
- **Deadline Tracking**: Monitor overdue and upcoming deadlines
- **Analytics**: Metrics on completion rates, productivity, etc.

**Business Logic**:
- Only assigned users can complete their tasks
- Managers can reassign tasks and change priorities
- Admins have full system access
- Notifications for overdue tasks
- Project completion tracking

## 💡 Real-World Application

This type of system powers applications used by millions daily:

**Project Management**:
- **JIRA** (Atlassian): Used by software teams worldwide
- **Asana**: Team collaboration and project tracking
- **Monday.com**: Work operating system for enterprises

**Development Tools**:
- **GitHub Projects**: Integrated task management for code repositories
- **Azure DevOps**: Microsoft's complete development platform
- **Linear**: Modern issue tracking for development teams

**Enterprise Software**:
- **ServiceNow**: IT service management
- **Smartsheet**: Collaborative work management
- **Wrike**: Professional project management

Companies from startups to Fortune 500 enterprises rely on these systems to manage billions of dollars in projects and coordinate thousands of employees.

## 🔨 Implementation

This capstone project simulates a Spring Boot enterprise application with multiple services, complex business logic, and advanced features. In production, this would use Spring Boot, Spring Data JPA, Spring Security, and a database like PostgreSQL.

```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.*;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;

// ============================================================================
// ENUMS AND CONSTANTS
// ============================================================================

enum UserRole {
    ADMIN,    // Full system access
    MANAGER,  // Can manage projects and reassign tasks
    USER      // Can work on assigned tasks
}

enum TaskPriority {
    LOW, MEDIUM, HIGH, CRITICAL
}

enum TaskStatus {
    TODO, IN_PROGRESS, IN_REVIEW, DONE, BLOCKED
}

// ============================================================================
// ENTITY MODELS
// ============================================================================

/**
 * User entity representing system users with roles and authentication.
 */
class User {
    private Long id;
    private String username;
    private String email;
    private String fullName;
    private UserRole role;
    private LocalDateTime createdAt;
    private boolean active;

    public User(Long id, String username, String email, String fullName, UserRole role) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.fullName = fullName;
        this.role = role;
        this.createdAt = LocalDateTime.now();
        this.active = true;
    }

    // Getters and setters
    public Long getId() { return id; }
    public String getUsername() { return username; }
    public String getEmail() { return email; }
    public String getFullName() { return fullName; }
    public UserRole getRole() { return role; }
    public void setRole(UserRole role) { this.role = role; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }

    @Override
    public String toString() {
        return String.format("%s (%s) - %s", fullName, username, role);
    }
}

/**
 * Project entity for organizing tasks into logical groups.
 */
class Project {
    private Long id;
    private String name;
    private String description;
    private Long ownerId;
    private LocalDate startDate;
    private LocalDate targetEndDate;
    private boolean active;
    private LocalDateTime createdAt;

    public Project(Long id, String name, String description, Long ownerId,
                   LocalDate startDate, LocalDate targetEndDate) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.ownerId = ownerId;
        this.startDate = startDate;
        this.targetEndDate = targetEndDate;
        this.active = true;
        this.createdAt = LocalDateTime.now();
    }

    // Getters and setters
    public Long getId() { return id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public Long getOwnerId() { return ownerId; }
    public LocalDate getStartDate() { return startDate; }
    public LocalDate getTargetEndDate() { return targetEndDate; }
    public void setTargetEndDate(LocalDate targetEndDate) { this.targetEndDate = targetEndDate; }
    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }
    public LocalDateTime getCreatedAt() { return createdAt; }

    @Override
    public String toString() {
        return String.format("Project[%d]: %s (Due: %s)", id, name, targetEndDate);
    }
}

/**
 * Task entity - the core work item in the system.
 */
class Task {
    private Long id;
    private String title;
    private String description;
    private Long projectId;
    private Long assigneeId;
    private Long creatorId;
    private TaskStatus status;
    private TaskPriority priority;
    private LocalDate dueDate;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
    private Integer estimatedHours;

    public Task(Long id, String title, String description, Long projectId,
                Long creatorId, TaskPriority priority, LocalDate dueDate) {
        this.id = id;
        this.title = title;
        this.description = description;
        this.projectId = projectId;
        this.creatorId = creatorId;
        this.priority = priority;
        this.dueDate = dueDate;
        this.status = TaskStatus.TODO;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }

    // Getters and setters
    public Long getId() { return id; }
    public String getTitle() { return title; }
    public void setTitle(String title) {
        this.title = title;
        this.updatedAt = LocalDateTime.now();
    }
    public String getDescription() { return description; }
    public void setDescription(String description) {
        this.description = description;
        this.updatedAt = LocalDateTime.now();
    }
    public Long getProjectId() { return projectId; }
    public Long getAssigneeId() { return assigneeId; }
    public void setAssigneeId(Long assigneeId) {
        this.assigneeId = assigneeId;
        this.updatedAt = LocalDateTime.now();
    }
    public Long getCreatorId() { return creatorId; }
    public TaskStatus getStatus() { return status; }
    public void setStatus(TaskStatus status) {
        this.status = status;
        this.updatedAt = LocalDateTime.now();
    }
    public TaskPriority getPriority() { return priority; }
    public void setPriority(TaskPriority priority) {
        this.priority = priority;
        this.updatedAt = LocalDateTime.now();
    }
    public LocalDate getDueDate() { return dueDate; }
    public void setDueDate(LocalDate dueDate) {
        this.dueDate = dueDate;
        this.updatedAt = LocalDateTime.now();
    }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public Integer getEstimatedHours() { return estimatedHours; }
    public void setEstimatedHours(Integer estimatedHours) {
        this.estimatedHours = estimatedHours;
        this.updatedAt = LocalDateTime.now();
    }

    public boolean isOverdue() {
        return dueDate != null &&
               dueDate.isBefore(LocalDate.now()) &&
               status != TaskStatus.DONE;
    }

    @Override
    public String toString() {
        String assignee = assigneeId != null ? "assigned to user " + assigneeId : "unassigned";
        String overdue = isOverdue() ? " [OVERDUE]" : "";
        return String.format("Task[%d]: %s - %s (%s, %s)%s",
            id, title, status, priority, assignee, overdue);
    }
}

/**
 * Comment entity for collaboration on tasks.
 */
class Comment {
    private Long id;
    private Long taskId;
    private Long userId;
    private String content;
    private LocalDateTime createdAt;

    public Comment(Long id, Long taskId, Long userId, String content) {
        this.id = id;
        this.taskId = taskId;
        this.userId = userId;
        this.content = content;
        this.createdAt = LocalDateTime.now();
    }

    public Long getId() { return id; }
    public Long getTaskId() { return taskId; }
    public Long getUserId() { return userId; }
    public String getContent() { return content; }
    public LocalDateTime getCreatedAt() { return createdAt; }

    @Override
    public String toString() {
        return String.format("Comment by user %d: %s", userId, content);
    }
}

// ============================================================================
// CUSTOM EXCEPTIONS
// ============================================================================

class UnauthorizedException extends RuntimeException {
    public UnauthorizedException(String message) {
        super(message);
    }
}

class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}

class ValidationException extends RuntimeException {
    public ValidationException(String message) {
        super(message);
    }
}

// ============================================================================
// REPOSITORY LAYER
// ============================================================================

class UserRepository {
    private final Map<Long, User> database = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public User save(User user) {
        database.put(user.getId(), user);
        return user;
    }

    public Optional<User> findById(Long id) {
        return Optional.ofNullable(database.get(id));
    }

    public Optional<User> findByUsername(String username) {
        return database.values().stream()
            .filter(u -> u.getUsername().equals(username))
            .findFirst();
    }

    public List<User> findAll() {
        return new ArrayList<>(database.values());
    }

    public List<User> findByRole(UserRole role) {
        return database.values().stream()
            .filter(u -> u.getRole() == role)
            .collect(Collectors.toList());
    }

    public Long getNextId() {
        return idGenerator.getAndIncrement();
    }
}

class ProjectRepository {
    private final Map<Long, Project> database = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public Project save(Project project) {
        database.put(project.getId(), project);
        return project;
    }

    public Optional<Project> findById(Long id) {
        return Optional.ofNullable(database.get(id));
    }

    public List<Project> findAll() {
        return new ArrayList<>(database.values());
    }

    public List<Project> findByOwnerId(Long ownerId) {
        return database.values().stream()
            .filter(p -> p.getOwnerId().equals(ownerId))
            .collect(Collectors.toList());
    }

    public List<Project> findActiveProjects() {
        return database.values().stream()
            .filter(Project::isActive)
            .collect(Collectors.toList());
    }

    public Long getNextId() {
        return idGenerator.getAndIncrement();
    }
}

class TaskRepository {
    private final Map<Long, Task> database = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public Task save(Task task) {
        database.put(task.getId(), task);
        return task;
    }

    public Optional<Task> findById(Long id) {
        return Optional.ofNullable(database.get(id));
    }

    public List<Task> findAll() {
        return new ArrayList<>(database.values());
    }

    public List<Task> findByProjectId(Long projectId) {
        return database.values().stream()
            .filter(t -> t.getProjectId().equals(projectId))
            .collect(Collectors.toList());
    }

    public List<Task> findByAssigneeId(Long assigneeId) {
        return database.values().stream()
            .filter(t -> assigneeId.equals(t.getAssigneeId()))
            .collect(Collectors.toList());
    }

    public List<Task> findByStatus(TaskStatus status) {
        return database.values().stream()
            .filter(t -> t.getStatus() == status)
            .collect(Collectors.toList());
    }

    public List<Task> findOverdueTasks() {
        return database.values().stream()
            .filter(Task::isOverdue)
            .collect(Collectors.toList());
    }

    public Long getNextId() {
        return idGenerator.getAndIncrement();
    }

    public boolean deleteById(Long id) {
        return database.remove(id) != null;
    }
}

class CommentRepository {
    private final Map<Long, Comment> database = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public Comment save(Comment comment) {
        database.put(comment.getId(), comment);
        return comment;
    }

    public List<Comment> findByTaskId(Long taskId) {
        return database.values().stream()
            .filter(c -> c.getTaskId().equals(taskId))
            .sorted(Comparator.comparing(Comment::getCreatedAt))
            .collect(Collectors.toList());
    }

    public Long getNextId() {
        return idGenerator.getAndIncrement();
    }
}

// ============================================================================
// SERVICE LAYER
// ============================================================================

/**
 * Service for user management and authentication simulation.
 */
class UserService {
    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User createUser(String username, String email, String fullName, UserRole role) {
        if (userRepository.findByUsername(username).isPresent()) {
            throw new ValidationException("Username already exists");
        }

        Long id = userRepository.getNextId();
        User user = new User(id, username, email, fullName, role);
        return userRepository.save(user);
    }

    public User getUserById(Long id) {
        return userRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("User not found"));
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public void updateUserRole(Long userId, UserRole newRole, User currentUser) {
        if (currentUser.getRole() != UserRole.ADMIN) {
            throw new UnauthorizedException("Only admins can change user roles");
        }

        User user = getUserById(userId);
        user.setRole(newRole);
        userRepository.save(user);
    }
}

/**
 * Service for project management.
 */
class ProjectService {
    private final ProjectRepository projectRepository;
    private final UserRepository userRepository;

    public ProjectService(ProjectRepository projectRepository, UserRepository userRepository) {
        this.projectRepository = projectRepository;
        this.userRepository = userRepository;
    }

    public Project createProject(String name, String description, Long ownerId,
                                LocalDate startDate, LocalDate targetEndDate, User currentUser) {
        if (currentUser.getRole() == UserRole.USER) {
            throw new UnauthorizedException("Only managers and admins can create projects");
        }

        userRepository.findById(ownerId)
            .orElseThrow(() -> new ResourceNotFoundException("Owner user not found"));

        Long id = projectRepository.getNextId();
        Project project = new Project(id, name, description, ownerId, startDate, targetEndDate);
        return projectRepository.save(project);
    }

    public Project getProjectById(Long id) {
        return projectRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("Project not found"));
    }

    public List<Project> getAllProjects() {
        return projectRepository.findAll();
    }

    public List<Project> getActiveProjects() {
        return projectRepository.findActiveProjects();
    }
}

/**
 * Service for task management with complex business logic.
 */
class TaskService {
    private final TaskRepository taskRepository;
    private final ProjectRepository projectRepository;
    private final UserRepository userRepository;

    public TaskService(TaskRepository taskRepository, ProjectRepository projectRepository,
                      UserRepository userRepository) {
        this.taskRepository = taskRepository;
        this.projectRepository = projectRepository;
        this.userRepository = userRepository;
    }

    public Task createTask(String title, String description, Long projectId,
                          TaskPriority priority, LocalDate dueDate, User creator) {
        projectRepository.findById(projectId)
            .orElseThrow(() -> new ResourceNotFoundException("Project not found"));

        if (title == null || title.trim().isEmpty()) {
            throw new ValidationException("Task title is required");
        }

        Long id = taskRepository.getNextId();
        Task task = new Task(id, title, description, projectId, creator.getId(), priority, dueDate);
        return taskRepository.save(task);
    }

    public Task getTaskById(Long id) {
        return taskRepository.findById(id)
            .orElseThrow(() -> new ResourceNotFoundException("Task not found"));
    }

    public List<Task> getAllTasks() {
        return taskRepository.findAll();
    }

    public List<Task> getTasksByProject(Long projectId) {
        return taskRepository.findByProjectId(projectId);
    }

    public List<Task> getTasksByAssignee(Long assigneeId) {
        return taskRepository.findByAssigneeId(assigneeId);
    }

    public List<Task> getTasksByStatus(TaskStatus status) {
        return taskRepository.findByStatus(status);
    }

    public List<Task> getOverdueTasks() {
        return taskRepository.findOverdueTasks();
    }

    public Task assignTask(Long taskId, Long assigneeId, User currentUser) {
        Task task = getTaskById(taskId);

        if (currentUser.getRole() == UserRole.USER &&
            !task.getCreatorId().equals(currentUser.getId())) {
            throw new UnauthorizedException("Users can only assign their own tasks");
        }

        userRepository.findById(assigneeId)
            .orElseThrow(() -> new ResourceNotFoundException("Assignee user not found"));

        task.setAssigneeId(assigneeId);
        return taskRepository.save(task);
    }

    public Task updateTaskStatus(Long taskId, TaskStatus newStatus, User currentUser) {
        Task task = getTaskById(taskId);

        // Business rule: only assigned user or managers/admins can update status
        if (currentUser.getRole() == UserRole.USER) {
            if (task.getAssigneeId() == null || !task.getAssigneeId().equals(currentUser.getId())) {
                throw new UnauthorizedException("You can only update tasks assigned to you");
            }
        }

        task.setStatus(newStatus);
        return taskRepository.save(task);
    }

    public Task updateTaskPriority(Long taskId, TaskPriority newPriority, User currentUser) {
        if (currentUser.getRole() == UserRole.USER) {
            throw new UnauthorizedException("Only managers and admins can change task priority");
        }

        Task task = getTaskById(taskId);
        task.setPriority(newPriority);
        return taskRepository.save(task);
    }

    public void deleteTask(Long taskId, User currentUser) {
        Task task = getTaskById(taskId);

        if (currentUser.getRole() == UserRole.USER &&
            !task.getCreatorId().equals(currentUser.getId())) {
            throw new UnauthorizedException("You can only delete your own tasks");
        }

        taskRepository.deleteById(taskId);
    }
}

/**
 * Service for analytics and reporting.
 */
class AnalyticsService {
    private final TaskRepository taskRepository;

    public AnalyticsService(TaskRepository taskRepository) {
        this.taskRepository = taskRepository;
    }

    public Map<String, Object> getProjectStatistics(Long projectId) {
        List<Task> projectTasks = taskRepository.findByProjectId(projectId);

        long totalTasks = projectTasks.size();
        long completedTasks = projectTasks.stream()
            .filter(t -> t.getStatus() == TaskStatus.DONE)
            .count();
        long overdueTasks = projectTasks.stream()
            .filter(Task::isOverdue)
            .count();

        double completionRate = totalTasks > 0 ? (completedTasks * 100.0 / totalTasks) : 0;

        Map<String, Object> stats = new HashMap<>();
        stats.put("totalTasks", totalTasks);
        stats.put("completedTasks", completedTasks);
        stats.put("overdueTasks", overdueTasks);
        stats.put("completionRate", String.format("%.1f%%", completionRate));

        return stats;
    }

    public Map<TaskPriority, Long> getTasksByPriority() {
        List<Task> allTasks = taskRepository.findAll();
        return allTasks.stream()
            .collect(Collectors.groupingBy(Task::getPriority, Collectors.counting()));
    }

    public Map<TaskStatus, Long> getTasksByStatus() {
        List<Task> allTasks = taskRepository.findAll();
        return allTasks.stream()
            .collect(Collectors.groupingBy(Task::getStatus, Collectors.counting()));
    }
}

/**
 * Service for comments and collaboration.
 */
class CommentService {
    private final CommentRepository commentRepository;
    private final TaskRepository taskRepository;

    public CommentService(CommentRepository commentRepository, TaskRepository taskRepository) {
        this.commentRepository = commentRepository;
        this.taskRepository = taskRepository;
    }

    public Comment addComment(Long taskId, String content, User user) {
        taskRepository.findById(taskId)
            .orElseThrow(() -> new ResourceNotFoundException("Task not found"));

        if (content == null || content.trim().isEmpty()) {
            throw new ValidationException("Comment content cannot be empty");
        }

        Long id = commentRepository.getNextId();
        Comment comment = new Comment(id, taskId, user.getId(), content);
        return commentRepository.save(comment);
    }

    public List<Comment> getTaskComments(Long taskId) {
        return commentRepository.findByTaskId(taskId);
    }
}

// ============================================================================
// MAIN DEMO APPLICATION
// ============================================================================

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Enterprise Task Management System ===\n");

        // Initialize repositories
        UserRepository userRepo = new UserRepository();
        ProjectRepository projectRepo = new ProjectRepository();
        TaskRepository taskRepo = new TaskRepository();
        CommentRepository commentRepo = new CommentRepository();

        // Initialize services
        UserService userService = new UserService(userRepo);
        ProjectService projectService = new ProjectService(projectRepo, userRepo);
        TaskService taskService = new TaskService(taskRepo, projectRepo, userRepo);
        AnalyticsService analyticsService = new AnalyticsService(taskRepo);
        CommentService commentService = new CommentService(commentRepo, taskRepo);

        // ===== DEMO 1: Create Users =====
        System.out.println("1. Creating users with different roles:");
        User admin = userService.createUser("admin", "admin@company.com", "Alice Admin", UserRole.ADMIN);
        User manager = userService.createUser("manager1", "bob@company.com", "Bob Manager", UserRole.MANAGER);
        User dev1 = userService.createUser("dev1", "carol@company.com", "Carol Developer", UserRole.USER);
        User dev2 = userService.createUser("dev2", "dave@company.com", "Dave Developer", UserRole.USER);

        System.out.println("  " + admin);
        System.out.println("  " + manager);
        System.out.println("  " + dev1);
        System.out.println("  " + dev2);

        // ===== DEMO 2: Create Projects =====
        System.out.println("\n2. Creating projects:");
        Project project1 = projectService.createProject(
            "E-Commerce Platform",
            "Build new online shopping platform",
            manager.getId(),
            LocalDate.of(2025, 11, 1),
            LocalDate.of(2026, 3, 31),
            manager
        );

        Project project2 = projectService.createProject(
            "Mobile App Development",
            "iOS and Android companion apps",
            manager.getId(),
            LocalDate.of(2025, 12, 1),
            LocalDate.of(2026, 6, 30),
            admin
        );

        System.out.println("  " + project1);
        System.out.println("  " + project2);

        // ===== DEMO 3: Create Tasks =====
        System.out.println("\n3. Creating tasks:");
        Task task1 = taskService.createTask(
            "Implement user authentication",
            "Set up OAuth2 with Google and GitHub providers",
            project1.getId(),
            TaskPriority.CRITICAL,
            LocalDate.of(2025, 12, 15),
            manager
        );

        Task task2 = taskService.createTask(
            "Design database schema",
            "Create ERD for products, orders, and users",
            project1.getId(),
            TaskPriority.HIGH,
            LocalDate.of(2025, 12, 10),
            manager
        );

        Task task3 = taskService.createTask(
            "Build shopping cart API",
            "REST endpoints for cart operations",
            project1.getId(),
            TaskPriority.MEDIUM,
            LocalDate.of(2025, 12, 20),
            manager
        );

        Task task4 = taskService.createTask(
            "Setup CI/CD pipeline",
            "Configure GitHub Actions for automated testing and deployment",
            project1.getId(),
            TaskPriority.HIGH,
            LocalDate.of(2025, 12, 8),
            manager
        );

        System.out.println("  " + task1);
        System.out.println("  " + task2);
        System.out.println("  " + task3);
        System.out.println("  " + task4);

        // ===== DEMO 4: Assign Tasks =====
        System.out.println("\n4. Assigning tasks to developers:");
        taskService.assignTask(task1.getId(), dev1.getId(), manager);
        taskService.assignTask(task2.getId(), dev1.getId(), manager);
        taskService.assignTask(task3.getId(), dev2.getId(), manager);
        taskService.assignTask(task4.getId(), dev2.getId(), manager);

        System.out.println("  Task 1 assigned to " + dev1.getFullName());
        System.out.println("  Task 2 assigned to " + dev1.getFullName());
        System.out.println("  Task 3 assigned to " + dev2.getFullName());
        System.out.println("  Task 4 assigned to " + dev2.getFullName());

        // ===== DEMO 5: Update Task Status =====
        System.out.println("\n5. Developers working on tasks:");
        taskService.updateTaskStatus(task1.getId(), TaskStatus.IN_PROGRESS, dev1);
        taskService.updateTaskStatus(task2.getId(), TaskStatus.DONE, dev1);
        taskService.updateTaskStatus(task4.getId(), TaskStatus.IN_PROGRESS, dev2);

        System.out.println("  " + taskService.getTaskById(task1.getId()));
        System.out.println("  " + taskService.getTaskById(task2.getId()));
        System.out.println("  " + taskService.getTaskById(task4.getId()));

        // ===== DEMO 6: Add Comments =====
        System.out.println("\n6. Team collaboration via comments:");
        commentService.addComment(task1.getId(), "Started working on OAuth integration", dev1);
        commentService.addComment(task1.getId(), "Google OAuth is working, GitHub next", dev1);
        commentService.addComment(task1.getId(), "Looks good! Remember to add error handling", manager);

        List<Comment> task1Comments = commentService.getTaskComments(task1.getId());
        System.out.println("  Comments on task 1:");
        task1Comments.forEach(c -> System.out.println("    - " + c));

        // ===== DEMO 7: Query Tasks by Status =====
        System.out.println("\n7. Querying tasks by status:");
        List<Task> inProgressTasks = taskService.getTasksByStatus(TaskStatus.IN_PROGRESS);
        System.out.println("  Tasks IN_PROGRESS:");
        inProgressTasks.forEach(t -> System.out.println("    - " + t));

        List<Task> todoTasks = taskService.getTasksByStatus(TaskStatus.TODO);
        System.out.println("  Tasks TODO:");
        todoTasks.forEach(t -> System.out.println("    - " + t));

        // ===== DEMO 8: Get User's Tasks =====
        System.out.println("\n8. Viewing tasks by assignee:");
        List<Task> dev1Tasks = taskService.getTasksByAssignee(dev1.getId());
        System.out.println("  " + dev1.getFullName() + "'s tasks:");
        dev1Tasks.forEach(t -> System.out.println("    - " + t));

        // ===== DEMO 9: Priority Management =====
        System.out.println("\n9. Manager updating task priorities:");
        taskService.updateTaskPriority(task3.getId(), TaskPriority.CRITICAL, manager);
        System.out.println("  Updated: " + taskService.getTaskById(task3.getId()));

        // ===== DEMO 10: Analytics =====
        System.out.println("\n10. Project analytics:");
        Map<String, Object> stats = analyticsService.getProjectStatistics(project1.getId());
        System.out.println("  Project: " + project1.getName());
        System.out.println("    Total tasks: " + stats.get("totalTasks"));
        System.out.println("    Completed: " + stats.get("completedTasks"));
        System.out.println("    Overdue: " + stats.get("overdueTasks"));
        System.out.println("    Completion rate: " + stats.get("completionRate"));

        // ===== DEMO 11: Role-Based Access Control =====
        System.out.println("\n11. Testing role-based access control:");
        try {
            taskService.updateTaskPriority(task1.getId(), TaskPriority.LOW, dev1);
            System.out.println("  ERROR: Should have thrown exception!");
        } catch (UnauthorizedException e) {
            System.out.println("  ✓ Access denied: " + e.getMessage());
        }

        try {
            projectService.createProject("Unauthorized Project", "Should fail",
                dev1.getId(), LocalDate.now(), LocalDate.now().plusMonths(1), dev1);
            System.out.println("  ERROR: Should have thrown exception!");
        } catch (UnauthorizedException e) {
            System.out.println("  ✓ Access denied: " + e.getMessage());
        }

        // ===== DEMO 12: System-wide Statistics =====
        System.out.println("\n12. System-wide statistics:");
        Map<TaskStatus, Long> statusBreakdown = analyticsService.getTasksByStatus();
        System.out.println("  Tasks by status:");
        statusBreakdown.forEach((status, count) ->
            System.out.println("    " + status + ": " + count));

        Map<TaskPriority, Long> priorityBreakdown = analyticsService.getTasksByPriority();
        System.out.println("  Tasks by priority:");
        priorityBreakdown.forEach((priority, count) ->
            System.out.println("    " + priority + ": " + count));

        System.out.println("\n=== Task Management System Demo Complete ===");
        System.out.println("This system demonstrates:");
        System.out.println("  ✓ Multi-entity architecture (Users, Projects, Tasks, Comments)");
        System.out.println("  ✓ Role-based access control (ADMIN, MANAGER, USER)");
        System.out.println("  ✓ Complex business logic and workflows");
        System.out.println("  ✓ Advanced querying and filtering");
        System.out.println("  ✓ Analytics and reporting");
        System.out.println("  ✓ Professional exception handling");
        System.out.println("  ✓ Production-ready architecture");
    }
}
```

## 🎓 What You've Learned

This capstone project demonstrates mastery of enterprise software development:

1. **Multi-Entity System Design**: Complex relationships between Users, Projects, Tasks, and Comments
2. **Role-Based Access Control**: Different permissions for ADMIN, MANAGER, and USER roles
3. **Advanced Business Logic**: Task assignment, workflow management, authorization rules
4. **Service Layer Architecture**: Clean separation of concerns across multiple services
5. **Complex Queries**: Filtering by status, assignee, project, priority, and overdue status
6. **Analytics and Reporting**: Statistics, completion rates, and data aggregation
7. **Exception Handling**: Custom exceptions for authorization, validation, and not-found cases
8. **Collaboration Features**: Comments system for team communication
9. **Professional Code Quality**: Clean, documented, production-ready code

## 💼 Interview Talking Points

When presenting this project to employers, emphasize:
- "Built an enterprise task management system with 4 interconnected entities"
- "Implemented role-based access control with 3 permission levels"
- "Designed complex business logic including task workflows and authorization rules"
- "Created analytics service for project completion rates and productivity metrics"
- "Developed advanced querying capabilities for filtering and searching"
- "Demonstrated understanding of multi-layer architecture (Controller-Service-Repository)"
- "Implemented collaboration features including commenting system"
- "Built comprehensive exception handling for security and validation"
- "This system is similar to enterprise tools like JIRA, Asana, or Azure DevOps"

## 🚀 Extensions

Take this capstone even further:
1. Add email notifications for task assignments and deadlines
2. Implement task dependencies (task B can't start until task A is done)
3. Add time tracking and work logs
4. Implement team management and project permissions
5. Add file attachments to tasks
6. Create sprint/iteration planning features
7. Build dashboard with charts and visualizations
8. Add task templates for common workflows
9. Implement audit logging for all changes
10. Add search with full-text capabilities
11. Integrate with external services (Slack, email, calendar)
12. Build REST API endpoints and deploy as Spring Boot application
13. Add frontend with React or Angular
14. Implement real database with PostgreSQL and JPA
15. Add Docker containerization and Kubernetes deployment

This capstone represents the culmination of your learning journey. You've built a sophisticated system that demonstrates professional software engineering skills. **Congratulations on completing this expert-level project!**
'''

def load_lessons():
    """Load lessons from JSON file"""
    lessons_path = Path("c:/devbootLLM-app/public/lessons-java.json")
    print(f"Loading lessons from: {lessons_path}")

    with open(lessons_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def save_lessons(data):
    """Save lessons back to JSON file"""
    lessons_path = Path("c:/devbootLLM-app/public/lessons-java.json")
    print(f"Saving lessons to: {lessons_path}")

    with open(lessons_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=True)

def count_chars(text):
    """Count characters, ensuring ASCII encoding"""
    # Convert to ASCII, replacing non-ASCII characters
    ascii_text = text.encode('ascii', errors='replace').decode('ascii')
    return len(ascii_text)

def update_lesson(lesson, new_content):
    """Update a lesson with new content"""
    old_content = lesson.get('content', '')
    old_count = count_chars(old_content)
    new_count = count_chars(new_content)

    lesson['fullSolution'] = new_content

    return old_count, new_count

def main():
    print("=" * 80)
    print("JAVA PORTFOLIO PROJECTS UPGRADE - BATCH 7C")
    print("=" * 80)
    print()

    # Load lessons
    lessons = load_lessons()

    # Find target lessons
    lesson_802 = None
    lesson_998 = None

    for lesson in lessons:
        if lesson['id'] == 802:
            lesson_802 = lesson
        elif lesson['id'] == 998:
            lesson_998 = lesson

    if not lesson_802:
        print("ERROR: Could not find lesson 802")
        sys.exit(1)

    if not lesson_998:
        print("ERROR: Could not find lesson 998")
        sys.exit(1)

    print("Found target lessons:")
    print(f"  - Lesson 802: {lesson_802['title']}")
    print(f"  - Lesson 998: {lesson_998['title']}")
    print()

    # Update lessons
    print("Updating lessons with production-ready implementations...")
    print()

    # Lesson 802
    old_802, new_802 = update_lesson(lesson_802, LESSON_802_CONTENT)
    print(f"Lesson 802: Portfolio: Todo List REST API")
    print(f"  Before: {old_802:,} chars")
    print(f"  After:  {new_802:,} chars")
    change_802 = new_802 - old_802
    pct_802 = ((change_802 / old_802) * 100) if old_802 > 0 else float('inf')
    if old_802 > 0:
        print(f"  Change: +{change_802:,} chars ({pct_802:.1f}% increase)")
    else:
        print(f"  Change: +{change_802:,} chars (new content)")
    print()

    # Lesson 998
    old_998, new_998 = update_lesson(lesson_998, LESSON_998_CONTENT)
    print(f"Lesson 998: Final Capstone: Task Management System")
    print(f"  Before: {old_998:,} chars")
    print(f"  After:  {new_998:,} chars")
    change_998 = new_998 - old_998
    pct_998 = ((change_998 / old_998) * 100) if old_998 > 0 else float('inf')
    if old_998 > 0:
        print(f"  Change: +{change_998:,} chars ({pct_998:.1f}% increase)")
    else:
        print(f"  Change: +{change_998:,} chars (new content)")
    print()

    # Save updated lessons
    save_lessons(lessons)

    # Summary
    print("=" * 80)
    print("UPGRADE SUMMARY")
    print("=" * 80)
    print(f"Total lessons upgraded: 2")
    print(f"Total character increase: +{change_802 + change_998:,} chars")
    print()
    print("Portfolio enhancements:")
    print("  * Complete REST API implementations with full CRUD")
    print("  * Multi-layer architecture (Controller -> Service -> Repository)")
    print("  * Comprehensive input validation and error handling")
    print("  * Role-based access control (RBAC)")
    print("  * Complex business logic and workflows")
    print("  * Advanced querying and filtering")
    print("  * Analytics and reporting features")
    print("  * Production-ready code quality")
    print("  * Realistic demo scenarios")
    print("  * Interview talking points")
    print()
    print("These are now RESUME-WORTHY portfolio projects!")
    print("=" * 80)

if __name__ == "__main__":
    main()
