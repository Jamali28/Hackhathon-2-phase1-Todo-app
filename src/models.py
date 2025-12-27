"""
Task model for the TODO application.

This module defines the Task dataclass that represents a single TODO item.
"""
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime


@dataclass
class Task:
    """
    Represents a single TODO item with ID, title, description, completion status, priority, tags, creation timestamp, due date, recurrence, and parent ID.

    Attributes:
        id (int): Unique integer identifier for the task
        title (str): Required string title of the task (non-empty)
        description (str): Optional string description of the task
        completed (bool): Boolean indicating whether the task is completed (default False)
        priority (str): Priority level of the task (high, medium, low; default medium)
        tags (List[str]): List of tags associated with the task (default empty list)
        created_at (datetime): Timestamp of when the task was created (default current time)
        due_datetime (Optional[datetime]): Optional datetime when the task is due (default None)
        recurrence (str): Recurrence pattern of the task ('none', 'daily', 'weekly', 'monthly'; default 'none')
        recurrence_parent_id (Optional[int]): ID of the parent recurring task template (default None)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"
    tags: List[str] = None
    created_at: datetime = None
    due_datetime: Optional[datetime] = None
    recurrence: str = "none"
    recurrence_parent_id: Optional[int] = None

    def __post_init__(self):
        """
        Initialize default values for mutable defaults and validate fields.

        Sets up the tags list, creation timestamp, and validates all fields including new due date and recurrence fields.
        """
        # Validate priority
        if self.priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be one of: 'high', 'medium', 'low'")

        # Validate recurrence
        if self.recurrence not in ["none", "daily", "weekly", "monthly"]:
            raise ValueError("Recurrence must be one of: 'none', 'daily', 'weekly', 'monthly'")

        # Validate recurrence_parent_id if provided
        if self.recurrence_parent_id is not None and not isinstance(self.recurrence_parent_id, int):
            raise ValueError("Recurrence parent ID must be an integer or None")

        # Initialize tags if None
        if self.tags is None:
            self.tags = []

        # Validate tags
        if not isinstance(self.tags, list):
            raise ValueError("Tags must be a list of strings")
        for tag in self.tags:
            if not isinstance(tag, str):
                raise ValueError("All tags must be strings")

        # Validate due_datetime if provided
        if self.due_datetime is not None and not isinstance(self.due_datetime, datetime):
            raise ValueError("Due datetime must be a datetime object or None")

        if self.created_at is None:
            self.created_at = datetime.now()