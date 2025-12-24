"""
Task manager for the TODO application.

This module handles all core task operations with in-memory storage.
"""
from typing import List, Optional
from .models import Task


class TaskManager:
    """
    Manages tasks in-memory with core CRUD operations.

    Provides methods for adding, deleting, updating, viewing, and marking tasks complete.
    """

    def __init__(self):
        """Initialize the task manager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task with the given title and optional description.

        Args:
            title: Required title for the task (must be non-empty)
            description: Optional description for the task

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        if not title or title.strip() == "":
            raise ValueError("Task title cannot be empty")

        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip(),
            completed=False
        )
        self.tasks.append(task)
        task_id = self.next_id
        self.next_id += 1
        return task_id

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks sorted by ID in ascending order.

        Returns:
            List[Task]: All tasks in the system sorted by ID
        """
        return sorted(self.tasks, key=lambda task: task.id)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task or None: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update the title and/or description of an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional, None to keep current)
            description: New description (optional, None to keep current)

        Returns:
            bool: True if the task was updated, False if task was not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        if title is not None:
            if title.strip() == "":
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if task was not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

    def mark_task_complete(self, task_id: int, completed: bool = True) -> bool:
        """
        Mark a task as complete or incomplete.

        Args:
            task_id: The ID of the task to update
            completed: Whether the task should be marked as completed (default True)

        Returns:
            bool: True if the task was updated, False if task was not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        task.completed = completed
        return True

    def get_next_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            int: The next ID that will be assigned to a new task
        """
        return self.next_id