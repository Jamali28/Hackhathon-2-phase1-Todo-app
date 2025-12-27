# Quickstart Guide: Advanced TODO Features

## Overview
This guide provides a quick reference for implementing the Advanced TODO features including recurring tasks and due date reminders.

## Prerequisites
- Python 3.13+
- Current working Basic + Intermediate features in /src
- Understanding of existing architecture (models.py, task_manager.py, cli.py, main.py)

## Implementation Steps

### 1. Extend Task Model
Update the Task dataclass in `models.py`:
```python
# Add these fields to the existing Task class
due_datetime: Optional[datetime] = None
recurrence: str = "none"  # 'none', 'daily', 'weekly', 'monthly'
recurrence_parent_id: Optional[int] = None
```

### 2. Update TaskManager Logic
In `task_manager.py`, implement:
- Due date parsing and validation
- Recurrence calculation functions
- Reminder detection methods
- Enhanced task operations

### 3. Enhance CLI Interface
In `cli.py`, update:
- Add task prompts to include due date/time and recurrence
- View display to show due dates and recurrence indicators
- Filter/sort options for new criteria

### 4. Add Startup Reminders
In `main.py`, implement:
- Startup reminder banner
- Optional background thread for ongoing notifications

## Key Implementation Notes

### Date/Time Handling
- Use datetime.datetime for combined date and time storage
- Validate input formats: YYYY-MM-DD for dates, HH:MM for times
- Handle month-end recurrence edge cases automatically

### Recurrence Logic
- Implement pure functions for date calculations
- Handle daily (+1 day), weekly (+7 days), monthly (same day) patterns
- For month-end cases, use last day of month when target day doesn't exist

### Testing Focus Areas
- Test all recurrence patterns thoroughly
- Validate month-end edge cases
- Verify reminder detection accuracy
- Ensure backward compatibility

## Verification Checklist
- [ ] Task model extended with new fields
- [ ] Date/time parsing works correctly
- [ ] Recurrence creates next tasks properly
- [ ] Due date reminders display accurately
- [ ] All existing tests still pass
- [ ] New functionality is well-tested