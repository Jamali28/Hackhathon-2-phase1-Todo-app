"""
Task manager for the TODO application.

This module handles all core task operations with in-memory storage.
"""
from typing import List, Optional
from datetime import datetime, time, timedelta
import calendar
try:
    # When running as a module (python -m src.main)
    from .models import Task
except ImportError:
    # When running directly (python src/main.py)
    from models import Task


class TaskManager:
    """
    Manages tasks in-memory with core CRUD operations.

    Provides methods for adding, deleting, updating, viewing, and marking tasks complete.
    """

    def __init__(self):
        """Initialize the task manager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1
        self.current_sort: str = "id"  # Default sort order

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None,
                 due_datetime = None, recurrence: str = "none", recurrence_parent_id = None) -> int:
        """
        Add a new task with the given title, description, priority, tags, due date, and recurrence.

        Args:
            title: Required title for the task (must be non-empty)
            description: Optional description for the task
            priority: Priority level ('high', 'medium', 'low'; default 'medium')
            tags: List of tags for the task (default empty list)
            due_datetime: Optional datetime when the task is due (default None)
            recurrence: Recurrence pattern ('none', 'daily', 'weekly', 'monthly'; default 'none')
            recurrence_parent_id: ID of parent recurring task template (default None)

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If title is empty or contains only whitespace, or if priority/recurrence is invalid
        """
        if not title or title.strip() == "":
            raise ValueError("Task title cannot be empty")

        if priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be one of: 'high', 'medium', 'low'")

        if recurrence not in ["none", "daily", "weekly", "monthly"]:
            raise ValueError("Recurrence must be one of: 'none', 'daily', 'weekly', 'monthly'")

        if recurrence_parent_id is not None and not isinstance(recurrence_parent_id, int):
            raise ValueError("Recurrence parent ID must be an integer or None")

        if tags is None:
            tags = []
        elif not isinstance(tags, list):
            raise ValueError("Tags must be a list of strings")
        else:
            # Validate that all tags are strings
            for tag in tags:
                if not isinstance(tag, str):
                    raise ValueError("All tags must be strings")

        # Validate due_datetime if provided
        if due_datetime is not None and not hasattr(due_datetime, 'year'):
            raise ValueError("Due datetime must be a datetime object or None")

        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description.strip(),
            completed=False,
            priority=priority,
            tags=tags,
            due_datetime=due_datetime,
            recurrence=recurrence,
            recurrence_parent_id=recurrence_parent_id
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                   priority: Optional[str] = None, tags: Optional[List[str]] = None,
                   due_datetime = None, recurrence: Optional[str] = None,
                   recurrence_parent_id = None) -> bool:
        """
        Update the title, description, priority, tags, due date, and/or recurrence of an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional, None to keep current)
            description: New description (optional, None to keep current)
            priority: New priority (optional, None to keep current)
            tags: New tags (optional, None to keep current)
            due_datetime: New due datetime (optional, None to keep current)
            recurrence: New recurrence pattern (optional, None to keep current)
            recurrence_parent_id: New parent ID (optional, None to keep current)

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

        if priority is not None:
            if priority not in ["high", "medium", "low"]:
                raise ValueError("Priority must be one of: 'high', 'medium', 'low'")
            task.priority = priority

        if tags is not None:
            if not isinstance(tags, list):
                raise ValueError("Tags must be a list of strings")
            # Validate that all tags are strings
            for tag in tags:
                if not isinstance(tag, str):
                    raise ValueError("All tags must be strings")
            task.tags = tags

        if due_datetime is not None:
            # Validate due_datetime if provided
            if due_datetime is not None and not hasattr(due_datetime, 'year'):
                raise ValueError("Due datetime must be a datetime object or None")
            task.due_datetime = due_datetime

        if recurrence is not None:
            if recurrence not in ["none", "daily", "weekly", "monthly"]:
                raise ValueError("Recurrence must be one of: 'none', 'daily', 'weekly', 'monthly'")
            task.recurrence = recurrence

        if recurrence_parent_id is not None:
            if recurrence_parent_id is not None and not isinstance(recurrence_parent_id, int):
                raise ValueError("Recurrence parent ID must be an integer or None")
            task.recurrence_parent_id = recurrence_parent_id

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
        If the task is recurring and being marked as complete, create the next occurrence.

        Args:
            task_id: The ID of the task to update
            completed: Whether the task should be marked as completed (default True)

        Returns:
            bool: True if the task was updated, False if task was not found
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        # Store the original completion state to detect if we're marking as complete
        was_completed = task.completed
        task.completed = completed

        # If the task is recurring and we're marking it as complete (not incomplete)
        if task.recurrence != "none" and completed and not was_completed:
            # Create the next occurrence of the task
            self.create_next_recurrence(task)

        return True

    def get_next_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            int: The next ID that will be assigned to a new task
        """
        return self.next_id

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title and description.

        Args:
            keyword: The keyword to search for (case-insensitive)

        Returns:
            List[Task]: List of tasks that match the search criteria
        """
        if not keyword:
            return self.tasks.copy()

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self.tasks:
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[bool] = None, priority: Optional[str] = None,
                    tag: Optional[str] = None, is_overdue: Optional[bool] = None,
                    is_due_today: Optional[bool] = None, is_recurring: Optional[bool] = None) -> List[Task]:
        """
        Filter tasks by specified criteria.

        Args:
            status: Filter by completion status (True for complete, False for incomplete, None for all)
            priority: Filter by priority ('high', 'medium', 'low', None for all)
            tag: Filter by specific tag (task must contain this tag, None for all)
            is_overdue: Filter by overdue status (True for overdue, False for not overdue, None for all)
            is_due_today: Filter by due today status (True for due today, False for not due today, None for all)
            is_recurring: Filter by recurring status (True for recurring, False for non-recurring, None for all)

        Returns:
            List[Task]: List of tasks that match the filter criteria
        """
        filtered_tasks = []

        for task in self.tasks:
            # Check status filter
            if status is not None and task.completed != status:
                continue

            # Check priority filter
            if priority is not None and task.priority != priority:
                continue

            # Check tag filter
            if tag is not None and tag not in task.tags:
                continue

            # Check overdue filter
            if is_overdue is not None and is_overdue != self.is_overdue(task):
                continue

            # Check due today filter
            if is_due_today is not None and is_due_today != self.is_due_today(task):
                continue

            # Check recurring filter
            if is_recurring is not None and is_recurring != (task.recurrence != "none"):
                continue

            filtered_tasks.append(task)

        return filtered_tasks

    def parse_date_input(self, date_str: str) -> Optional[datetime]:
        """
        Parse date input string in YYYY-MM-DD format to datetime object.

        Args:
            date_str: Date string in YYYY-MM-DD format

        Returns:
            datetime object or None if input is empty/invalid
        """
        if not date_str or not isinstance(date_str, str):
            return None

        try:
            # Parse YYYY-MM-DD format
            date_parts = date_str.split('-')
            if len(date_parts) != 3:
                return None

            year, month, day = map(int, date_parts)
            # Create datetime object at midnight (00:00:00)
            return datetime(year, month, day)
        except (ValueError, TypeError):
            return None

    def parse_time_input(self, time_str: str) -> Optional[time]:
        """
        Parse time input string in HH:MM format to time object.

        Args:
            time_str: Time string in HH:MM format

        Returns:
            time object or None if input is empty/invalid
        """
        if not time_str or not isinstance(time_str, str):
            return None

        try:
            # Parse HH:MM format
            time_parts = time_str.split(':')
            if len(time_parts) != 2:
                return None

            hour, minute = map(int, time_parts)
            return time(hour, minute)
        except (ValueError, TypeError):
            return None

    def is_overdue(self, task: Task) -> bool:
        """
        Check if a task is overdue based on its due date.

        Args:
            task: The task to check

        Returns:
            bool: True if the task is overdue, False otherwise
        """
        if task.due_datetime is None:
            return False

        return task.due_datetime < datetime.now() and not task.completed

    def is_due_today(self, task: Task) -> bool:
        """
        Check if a task is due today.

        Args:
            task: The task to check

        Returns:
            bool: True if the task is due today, False otherwise
        """
        if task.due_datetime is None:
            return False

        today = datetime.now().date()
        task_due_date = task.due_datetime.date()
        return task_due_date == today and not task.completed

    def is_due_soon(self, task: Task, hours: int = 24) -> bool:
        """
        Check if a task is due within the specified number of hours.

        Args:
            task: The task to check
            hours: Number of hours to check (default 24)

        Returns:
            bool: True if the task is due within the specified hours, False otherwise
        """
        if task.due_datetime is None:
            return False

        now = datetime.now()
        due_soon_time = now + timedelta(hours=hours)
        return now < task.due_datetime <= due_soon_time and not task.completed

    def format_datetime_display(self, dt: datetime) -> str:
        """
        Format datetime object for display.

        Args:
            dt: The datetime to format

        Returns:
            str: Formatted datetime string
        """
        if dt is None:
            return ""

        # Format as "YYYY-MM-DD HH:MM" if it has time component, or "YYYY-MM-DD" if it's just a date
        if dt.hour == 0 and dt.minute == 0 and dt.second == 0:
            return dt.strftime("%Y-%m-%d")
        else:
            return dt.strftime("%Y-%m-%d %H:%M")

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks.

        Returns:
            List[Task]: List of overdue tasks
        """
        return [task for task in self.tasks if self.is_overdue(task)]

    def get_due_today_tasks(self) -> List[Task]:
        """
        Get all tasks due today.

        Returns:
            List[Task]: List of tasks due today
        """
        return [task for task in self.tasks if self.is_due_today(task)]

    def get_due_soon_tasks(self, hours: int = 24) -> List[Task]:
        """
        Get all tasks due within the specified number of hours.

        Args:
            hours: Number of hours to check (default 24)

        Returns:
            List[Task]: List of tasks due soon
        """
        return [task for task in self.tasks if self.is_due_soon(task, hours)]

    def calculate_next_occurrence(self, task: Task) -> Optional[datetime]:
        """
        Calculate the next occurrence datetime based on the task's recurrence pattern.

        Args:
            task: The recurring task

        Returns:
            datetime: The next occurrence datetime, or None if task is not recurring
        """
        if task.due_datetime is None or task.recurrence == "none":
            return None

        current_due = task.due_datetime
        if task.recurrence == "daily":
            return current_due + timedelta(days=1)
        elif task.recurrence == "weekly":
            return current_due + timedelta(days=7)
        elif task.recurrence == "monthly":
            # Calculate next month by adding 1 to the month
            year = current_due.year
            month = current_due.month + 1

            # Handle year overflow
            if month > 12:
                year += 1
                month = 1

            # Handle day overflow (e.g., Jan 31 -> Feb 28/29)
            max_day = calendar.monthrange(year, month)[1]
            day = min(current_due.day, max_day)

            # Preserve the time component
            return current_due.replace(year=year, month=month, day=day)
        else:
            # Should not happen due to validation, but just in case
            return None

    def create_next_recurrence(self, task: Task) -> Optional[int]:
        """
        Create the next occurrence of a recurring task.

        Args:
            task: The recurring task that was completed

        Returns:
            int: The ID of the new task, or None if task is not recurring
        """
        if task.recurrence == "none":
            return None

        next_due_datetime = self.calculate_next_occurrence(task)
        if next_due_datetime is None:
            return None

        # Create a new task with the same properties but updated due date
        new_task_id = self.add_task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            tags=task.tags.copy() if task.tags else [],
            due_datetime=next_due_datetime,
            recurrence=task.recurrence,
            recurrence_parent_id=task.id  # Link to the original task
        )

        return new_task_id

    def get_recurring_tasks(self) -> List[Task]:
        """
        Get all recurring tasks (tasks with recurrence != 'none').

        Returns:
            List[Task]: List of recurring tasks
        """
        return [task for task in self.tasks if task.recurrence != "none"]

    def set_sort_order(self, sort_by: str) -> None:
        """
        Set the current sort order for task display.

        Args:
            sort_by: The sort order ('id', 'priority', 'title', 'status', 'due_date')
        """
        valid_sort_orders = ['id', 'priority', 'title', 'status', 'due_date']
        if sort_by not in valid_sort_orders:
            raise ValueError(f"Sort order must be one of: {valid_sort_orders}")
        self.current_sort = sort_by

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks sorted by the current sort order.

        Returns:
            List[Task]: All tasks in the system sorted by the current sort order
        """
        tasks = self.tasks.copy()

        if self.current_sort == 'priority':
            # Sort by priority: high > medium > low
            priority_order = {'high': 0, 'medium': 1, 'low': 2}
            tasks.sort(key=lambda task: priority_order[task.priority])
        elif self.current_sort == 'title':
            tasks.sort(key=lambda task: task.title.lower())
        elif self.current_sort == 'status':
            # Sort by completion status: incomplete first, then complete
            tasks.sort(key=lambda task: task.completed)
        elif self.current_sort == 'due_date':
            # Sort by due date: overdue first, then by due date
            def due_date_sort_key(task):
                if task.due_datetime is None:
                    # Tasks without due dates go to the end
                    return (2, datetime.max)  # (priority, date) - 2 means no due date
                elif self.is_overdue(task):
                    # Overdue tasks come first (priority 0)
                    return (0, task.due_datetime)
                else:
                    # Non-overdue tasks come next (priority 1)
                    return (1, task.due_datetime)
            tasks.sort(key=due_date_sort_key)
        else:  # Default: sort by ID
            tasks.sort(key=lambda task: task.id)

        return tasks