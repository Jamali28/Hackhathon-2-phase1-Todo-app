# Advanced TODO Application

A sophisticated console-based in-memory TODO application that provides comprehensive task management with intelligent automation features. This application extends the basic functionality with advanced features including recurring tasks, due date management, and proactive reminders.

## Features

### Basic Features
- **Add Tasks**: Create tasks with titles, descriptions, priorities, and tags
- **View Tasks**: See all your tasks with status indicators
- **Update Tasks**: Modify existing task details
- **Delete Tasks**: Remove tasks you no longer need
- **Mark Complete/Incomplete**: Track your progress by toggling task completion status

### Intermediate Features
- **Priority Levels**: Assign priority levels (high, medium, low) to organize importance
- **Tags System**: Categorize tasks with multiple tags for better organization
- **Search & Filter**: Find tasks by keywords, status, priority, or tags
- **Sorting Options**: Sort tasks by ID, priority, title, or status

### Advanced Features
- **Due Dates**: Assign due dates and optional times to tasks
- **Recurring Tasks**: Set up recurring tasks (daily, weekly, monthly) that automatically generate the next occurrence when completed
- **Overdue Detection**: Automatic identification of overdue tasks with visual indicators
- **Reminder System**: Startup banner showing overdue and upcoming tasks
- **Real-time Notifications**: Background thread that periodically checks for due/overdue tasks
- **Advanced Filtering**: Filter by overdue status, due today, and recurring tasks
- **Due Date Sorting**: Sort tasks by due date with overdue tasks appearing first

## Prerequisites

- Python 3.13 or higher
- No external dependencies required

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is installed: `python --version`

## Running the Application

```bash
python -m src.main
```

## Usage Guide

### Getting Started
When you start the application, you'll see a main menu with the following options:
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Mark task as complete/incomplete
6. Search & Filter tasks
7. Sort tasks
8. Exit

### Adding Tasks
Choose option 1 to add a new task. You'll be prompted to enter:
- **Title**: Required task title
- **Description**: Optional task description
- **Priority**: High, medium, or low (defaults to medium)
- **Tags**: Comma-separated tags for categorization (optional)
- **Due Date**: Optional due date in YYYY-MM-DD format
- **Due Time**: Optional due time in HH:MM format (if date provided)
- **Recurrence**: None, daily, weekly, or monthly (for recurring tasks)

### Viewing Tasks
Choose option 2 to see all your tasks. The display includes:
- Task ID
- Completion status ([ ] or [x])
- Priority (H, M, L)
- Tags
- Due date (with **[OVERDUE]** marker if applicable)
- Recurrence indicator (🔁 for recurring tasks)
- Title
- Description

### Updating Tasks
Choose option 3 to modify an existing task. You'll need to provide the task ID and can update any of the task properties.

### Deleting Tasks
Choose option 4 to remove a task. You'll need to provide the task ID and confirm deletion.

### Marking Tasks Complete
Choose option 5 to toggle a task's completion status. For recurring tasks, marking complete will create the next occurrence automatically.

### Searching and Filtering
Choose option 6 to search and filter your tasks. You can:
- Search by keyword in title or description
- Filter by completion status
- Filter by priority
- Filter by specific tags
- Filter by overdue status
- Filter by due today status
- Filter by recurring status

### Sorting Tasks
Choose option 7 to sort your tasks by:
- ID (creation order)
- Priority (high to low)
- Title (alphabetical)
- Status (incomplete first)
- Due date (overdue first, then by due date)

## Advanced Features Explained

### Recurring Tasks
When adding or updating a task, you can set a recurrence pattern:
- **Daily**: Creates a new occurrence every day
- **Weekly**: Creates a new occurrence every 7 days
- **Monthly**: Creates a new occurrence every month (handles month-end cases correctly)

When you mark a recurring task as complete, the application automatically creates the next occurrence based on the recurrence pattern.

### Due Date Management
Tasks can have due dates and optional times. The system will:
- Show overdue tasks with a **[OVERDUE]** marker
- Highlight tasks due today
- Sort tasks by due date with overdue tasks appearing first

### Reminder System
The application provides two types of reminders:
1. **Startup Reminders**: Shows a banner when you start the application with counts of overdue, due today, and due soon tasks
2. **Real-time Reminders**: Background thread that checks every minute for new due/overdue tasks

### Month-end Handling
For monthly recurring tasks, the application handles month-end edge cases:
- Tasks scheduled for January 31st will recur on February 28th (or 29th in leap years)
- March 31st → April 30th → May 31st, etc.

## Examples

### Adding a Recurring Task
```
Menu: 1 (Add task)
Title: Daily Exercise
Description: Go for a 30-minute walk
Priority: high
Tags: health,exercise
Due Date: 2025-01-01
Due Time: 07:00
Recurrence: daily
```

### Adding a Due Date Task
```
Menu: 1 (Add task)
Title: Submit Report
Description: Quarterly financial report
Priority: high
Tags: work,report
Due Date: 2025-01-15
Due Time: 17:00
Recurrence: none
```

### Filtering Overdue Tasks
```
Menu: 6 (Search & Filter)
Keyword: (press Enter to skip)
Status: All tasks
Priority: All priorities
Tag: (press Enter to skip)
Overdue status: 2 (Overdue tasks only)
Due today status: 1 (All tasks)
Recurring status: 1 (All tasks)
```

## Technical Details

- **Architecture**: Console-based, in-memory storage
- **Language**: Python 3.13+
- **Storage**: In-memory (tasks are lost when application closes)
- **Dependencies**: Standard library only (no external dependencies)
- **Platform**: Cross-platform compatible

## Testing

Run the unit tests with:

```bash
python -m unittest discover tests/
```

## Architecture

The application follows a modular architecture with clear separation of concerns:

- `src/models.py`: Task dataclass definition with fields for ID, title, description, completion status, priority, tags, due_datetime, recurrence, and recurrence_parent_id
- `src/task_manager.py`: Core business logic for task operations including advanced features
- `src/cli.py`: Command-line interface and user interaction with enhanced prompts and displays
- `src/main.py`: Application entry point with reminder system implementation

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.