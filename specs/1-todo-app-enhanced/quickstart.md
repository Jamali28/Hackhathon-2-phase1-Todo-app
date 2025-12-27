# Quickstart Guide: Full Phase 1 TODO Application

## Development Setup

1. **Prerequisites**
   - Python 3.13+
   - UV package manager

2. **Installation**
   ```bash
   # Clone the repository
   # Install dependencies
   uv sync
   ```

3. **Running the Application**
   ```bash
   # Run the application
   python -m src.main
   ```

## Architecture Overview

The application follows a clean architecture with clear separation of concerns:

```
src/
├── main.py              # Application entry point
├── cli.py               # Command-line interface (presentation layer)
├── task_manager.py      # Business logic (domain layer)
└── models.py            # Data models (domain entities)
```

## Key Components

### Task Model
- Enhanced dataclass with ID, title, description, completion status, priority, tags, and creation timestamp
- Priority values: "high", "medium", "low"
- Tags: List of strings for categorization

### TaskManager
- Core business logic for task operations
- In-memory storage using a list of Task objects
- New methods for search, filter, and sort functionality
- Persistent sort order setting

### CLI
- Menu-driven interface with 8 options
- Enhanced with search/filter and sort commands
- Formatted display including priority and tags

## Extension Points

The application is designed to be easily extended with new features while maintaining:

- Clean separation of concerns
- Testable business logic
- Type safety throughout
- Comprehensive error handling