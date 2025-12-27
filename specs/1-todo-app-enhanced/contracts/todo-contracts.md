# API Contracts: Full Phase 1 TODO Application

## TaskManager Contracts

### Core Task Operations
- **add_task(title: str, description: str = "", priority: str = "medium", tags: list[str] = None) -> int**
  - Purpose: Add a new task with specified attributes
  - Parameters: title (required), description (optional), priority (optional, default "medium"), tags (optional, default empty list)
  - Returns: Task ID of newly created task
  - Raises: ValueError if title is empty or priority is invalid

- **list_tasks() -> list[Task]**
  - Purpose: Get all tasks in current sort order
  - Returns: List of all Task objects sorted according to current_sort setting

- **get_task(task_id: int) -> Task | None**
  - Purpose: Get a specific task by ID
  - Returns: Task object if found, None otherwise

- **update_task(task_id: int, title: str | None = None, description: str | None = None, priority: str | None = None, tags: list[str] | None = None) -> bool**
  - Purpose: Update properties of an existing task
  - Returns: True if updated, False if task not found
  - Raises: ValueError if priority is invalid

- **delete_task(task_id: int) -> bool**
  - Purpose: Delete a task by ID
  - Returns: True if deleted, False if task not found

- **mark_task_complete(task_id: int, completed: bool = True) -> bool**
  - Purpose: Mark a task as complete/incomplete
  - Returns: True if updated, False if task not found

### Intermediate Features
- **search_tasks(keyword: str) -> list[Task]**
  - Purpose: Search tasks by keyword in title/description
  - Returns: List of matching Task objects

- **filter_tasks(status: bool | None = None, priority: str | None = None, tag: str | None = None) -> list[Task]**
  - Purpose: Filter tasks by specified criteria
  - Returns: List of matching Task objects

- **set_sort_order(sort_by: str) -> None**
  - Purpose: Set the current sort order for task display
  - Parameters: sort_by (one of "id", "priority", "title", "status")

## CLI Contracts

### Menu Operations
- **display_menu() -> None**
  - Purpose: Display the main menu with 8 options

### Task Operations
- **add_task() -> None**
  - Purpose: Handle adding a new task with priority and tags

- **update_task() -> None**
  - Purpose: Handle updating an existing task including priority and tags

- **view_tasks() -> None**
  - Purpose: Display all tasks with priority and tags information

- **search_and_filter_tasks() -> None**
  - Purpose: Handle searching and filtering tasks based on user input

- **sort_tasks() -> None**
  - Purpose: Handle setting sort preferences based on user input