# Data Model: Advanced TODO Features

## Entity: Task

### Current Fields (Basic + Intermediate)
- **id**: int - Unique identifier for the task
- **title**: str - Required title of the task
- **description**: str - Optional description (default: "")
- **completed**: bool - Completion status (default: False)
- **priority**: str - Priority level (high, medium, low) (default: "medium")
- **tags**: List[str] - List of tags for categorization (default: [] in __post_init__)

### New Fields (Advanced)
- **due_datetime**: Optional[datetime] - Combined date and time when task is due (default: None)
- **recurrence**: str - Recurrence pattern (none, daily, weekly, monthly) (default: "none")
- **recurrence_parent_id**: Optional[int] - Links to parent recurring task template (default: None)

### Complete Task Definition
```python
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"  # 'high', 'medium', 'low'
    tags: List[str] = None   # Default to [] in __post_init__
    due_datetime: Optional[datetime] = None  # Combined date and time
    recurrence: str = "none"  # 'none', 'daily', 'weekly', 'monthly'
    recurrence_parent_id: Optional[int] = None  # Links to original recurring template

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.recurrence not in ['none', 'daily', 'weekly', 'monthly']:
            raise ValueError("Recurrence must be one of: 'none', 'daily', 'weekly', 'monthly'")
        # Validate due_datetime if provided
        if self.due_datetime is not None and not isinstance(self.due_datetime, datetime):
            raise ValueError("due_datetime must be a datetime object or None")
```

## Validation Rules

### Field Validation
- **id**: Must be a positive integer
- **title**: Must be non-empty string
- **completed**: Must be boolean
- **priority**: Must be one of ['high', 'medium', 'low']
- **tags**: Must be a list of strings
- **due_datetime**: Must be datetime object or None
- **recurrence**: Must be one of ['none', 'daily', 'weekly', 'monthly']
- **recurrence_parent_id**: Must be positive integer or None

### Business Logic Validation
- **Due Date Validation**: If recurrence is set, due_datetime should typically be set
- **Recurrence Chain Validation**: recurrence_parent_id must point to an existing task
- **Recurrence Consistency**: Recurring tasks maintain the same recurrence pattern in their chain

## State Transitions

### Task Completion with Recurrence
1. **Initial State**: Task with recurrence != 'none' and completed = False
2. **Action**: Mark task as complete
3. **Transition**:
   - Original task: completed = True
   - New task created: same properties except new ID, calculated due_datetime, recurrence_parent_id = original task ID
4. **Final State**: Original task completed, new instance scheduled

### Task Creation States
1. **New Task**: id assigned, completed = False, all other fields from input
2. **Recurring Task**: Follows same pattern but with recurrence != 'none' and due_datetime set

## Relationships

### Recurrence Chain
- **Parent-Child Relationship**: Tasks with recurrence_parent_id point to their template
- **Chain Structure**: Each recurring task creates a new instance when completed
- **Root Task**: Tasks with recurrence_parent_id = None are original templates

### Data Integrity
- **Referential Integrity**: recurrence_parent_id must reference existing task ID
- **Cascade Considerations**: Deleting a recurring task may affect its chain (implementation dependent)