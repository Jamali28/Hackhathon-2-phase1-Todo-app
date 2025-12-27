# Data Model: Full Phase 1 TODO Application

## Entity: Task

### Fields
- **id**: int (required, unique, auto-incremented)
  - Validation: Must be a positive integer
  - Purpose: Unique identifier for each task
- **title**: str (required, non-empty)
  - Validation: Cannot be empty or contain only whitespace
  - Purpose: The main description/name of the task
- **description**: str (optional)
  - Validation: Can be empty string
  - Purpose: Additional details about the task
- **completed**: bool (optional, default False)
  - Validation: Must be boolean value
  - Purpose: Indicates whether the task is completed
- **priority**: str (optional, default "medium")
  - Validation: Must be one of "high", "medium", "low"
  - Purpose: Indicates the importance level of the task
- **tags**: list[str] (optional, default empty list)
  - Validation: Must be a list of strings, individual tags cannot be empty
  - Purpose: Categorization labels for the task
- **created_at**: datetime (optional, default current time)
  - Validation: Must be a valid datetime object
  - Purpose: Timestamp of when the task was created

### Relationships
- Task exists independently (no direct relationships with other entities)

### State Transitions
- **completed**: Can transition between True and False states through the mark_task_complete method
- **priority**: Can transition between "high", "medium", and "low" states through the update_task method
- **tags**: Can be added, removed, or modified through the update_task method

## Entity: TaskManager

### Fields
- **tasks**: List[Task] (required, default empty list)
  - Validation: Must be a list of Task objects
  - Purpose: In-memory storage for all tasks
- **next_id**: int (required, default 1)
  - Validation: Must be a positive integer
  - Purpose: Tracks the next ID to be assigned to a new task
- **current_sort**: str (optional, default "id")
  - Validation: Must be one of "id", "priority", "title", "status"
  - Purpose: Tracks the current sorting preference for task display

### Methods
- **add_task(title: str, description: str, priority: str, tags: list[str])**: int
  - Purpose: Creates and adds a new task to the collection
  - Returns: The ID of the newly created task
  - Validation: Title cannot be empty, priority must be valid, tags must be valid strings

- **list_tasks()**: List[Task]
  - Purpose: Returns all tasks, sorted according to current_sort setting
  - Returns: List of all Task objects in the requested sort order

- **get_task(task_id: int)**: Optional[Task]
  - Purpose: Retrieves a specific task by its ID
  - Returns: The Task object if found, None otherwise

- **update_task(task_id: int, title: Optional[str], description: Optional[str], priority: Optional[str], tags: Optional[list[str]])**: bool
  - Purpose: Updates properties of an existing task
  - Returns: True if the task was updated, False if task was not found
  - Validation: Priority must be valid if provided, tags must be valid if provided

- **delete_task(task_id: int)**: bool
  - Purpose: Removes a task from the collection
  - Returns: True if the task was deleted, False if task was not found

- **mark_task_complete(task_id: int, completed: bool)**: bool
  - Purpose: Updates the completion status of a task
  - Returns: True if the task status was updated, False if task was not found

- **search_tasks(keyword: str)**: List[Task]
  - Purpose: Finds tasks containing the keyword in title or description
  - Returns: List of Task objects that match the search criteria

- **filter_tasks(status: Optional[bool], priority: Optional[str], tag: Optional[str])**: List[Task]
  - Purpose: Filters tasks based on specified criteria
  - Returns: List of Task objects that match the filter criteria

- **set_sort_order(sort_by: str)**: None
  - Purpose: Sets the current sorting preference for task display
  - Validation: sort_by must be one of the allowed sort options

## Entity: CLI

### Fields
- **task_manager**: TaskManager (required)
  - Validation: Must be a valid TaskManager instance
  - Purpose: Reference to the task manager for performing operations

### Methods
- **display_menu()**: None
  - Purpose: Shows the main menu with all available options (1-8)

- **search_and_filter_tasks()**: None
  - Purpose: Handles user interaction for searching and filtering tasks

- **sort_tasks()**: None
  - Purpose: Handles user interaction for setting sort preferences

- **add_task()**: None
  - Purpose: Handles user interaction for adding a new task with priority and tags

- **update_task()**: None
  - Purpose: Handles user interaction for updating a task including priority and tags