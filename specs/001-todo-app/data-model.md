# Data Model: Basic Level TODO Application

**Date**: 2025-12-24
**Feature**: Basic Level TODO Application
**Branch**: 001-todo-app

## Entity: Task

### Fields
- `id`: int (unique, auto-incremented, starting from 1)
- `title`: str (required, non-empty, max 200 characters)
- `description`: str (optional, can be empty, max 1000 characters)
- `completed`: bool (default False)

### Validation Rules
- `id`: Must be unique within the system, auto-generated sequentially
- `title`: Required field, must not be empty or contain only whitespace
- `description`: Optional field, can be empty string
- `completed`: Boolean value, defaults to False when creating new task

### State Transitions
- `incomplete` → `completed`: When user marks task as complete
- `completed` → `incomplete`: When user marks completed task as incomplete

## Entity: TaskList

### Fields
- `tasks`: List[Task] (collection of Task entities)
- `next_id`: int (counter for next available ID, starts at 1)

### Validation Rules
- `tasks`: Maintains order of insertion, IDs are unique within the list
- `next_id`: Incremented each time a new task is added

### Relationships
- One TaskList contains multiple Task entities
- Each Task belongs to exactly one TaskList during its lifetime