# Task Management API Contracts

**Date**: 2025-12-24
**Feature**: Basic Level TODO Application
**Branch**: 001-todo-app

## Core Task Operations

### Add Task
- **Function**: `add_task(title: str, description: str = "") -> int`
- **Input**:
  - title (required): string, non-empty
  - description (optional): string, can be empty
- **Output**: int (new task ID)
- **Success**: Task added to list with unique ID, returns ID
- **Errors**: ValueError if title is empty

### List Tasks
- **Function**: `list_tasks() -> List[Task]`
- **Input**: None
- **Output**: List of Task objects, sorted by ID
- **Success**: Returns all tasks in the system
- **Errors**: None

### Get Task by ID
- **Function**: `get_task(task_id: int) -> Optional[Task]`
- **Input**: task_id (int)
- **Output**: Task object or None if not found
- **Success**: Returns the requested Task or None
- **Errors**: None (returns None for invalid IDs)

### Update Task
- **Function**: `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool`
- **Input**:
  - task_id (int)
  - title (optional, None to keep current)
  - description (optional, None to keep current)
- **Output**: bool (True if successful, False if task not found)
- **Success**: Task updated, returns True
- **Errors**: Returns False if task doesn't exist

### Delete Task
- **Function**: `delete_task(task_id: int) -> bool`
- **Input**: task_id (int)
- **Output**: bool (True if successful, False if task not found)
- **Success**: Task removed, returns True
- **Errors**: Returns False if task doesn't exist

### Mark Task Complete
- **Function**: `mark_task_complete(task_id: int, completed: bool = True) -> bool`
- **Input**:
  - task_id (int)
  - completed (bool, default True)
- **Output**: bool (True if successful, False if task not found)
- **Success**: Task status updated, returns True
- **Errors**: Returns False if task doesn't exist

### Get Next ID
- **Function**: `get_next_id() -> int`
- **Input**: None
- **Output**: int (next available task ID)
- **Success**: Returns next ID to be used
- **Errors**: None