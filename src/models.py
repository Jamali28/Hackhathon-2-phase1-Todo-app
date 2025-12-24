"""
Task model for the TODO application.

This module defines the Task dataclass that represents a single TODO item.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single TODO item with ID, title, description, and completion status.

    Attributes:
        id: Unique integer identifier for the task
        title: Required string title of the task (non-empty)
        description: Optional string description of the task
        completed: Boolean indicating whether the task is completed (default False)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False