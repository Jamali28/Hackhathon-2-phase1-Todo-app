# TODO Application

A simple in-memory command-line Python console TODO application with the following core features:
- Add Task: Create a new task with a required title and optional description
- Delete Task: Remove a task by its unique ID
- Update Task: Modify the title and/or description of an existing task by ID
- View Task List: Display all tasks with clear formatting
- Mark as Complete: Toggle the completion status of a task by ID

All data is stored only in memory (no files, no databases). The app runs as an interactive console loop that continues until the user chooses to exit.

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

## Basic Usage

1. Run the application with the command above
2. Use the numbered menu options (1-6) to interact:
   - Option 1: Add a new task
   - Option 2: View all tasks
   - Option 3: Update a task
   - Option 4: Delete a task
   - Option 5: Mark task as complete/incomplete
   - Option 6: Exit the application
3. Follow the prompts for each operation

## Example Workflow

1. Start the application: `python -m src.main`
2. Add a task (Option 1): Enter title and optional description
3. View tasks (Option 2): See all tasks with status indicators
4. Mark a task complete (Option 5): Enter task ID
5. Exit (Option 6): Close the application

## Testing

Run the unit tests with:

```bash
python -m unittest discover tests/
```

## Architecture

The application follows a modular architecture with clear separation of concerns:

- `src/models.py`: Task dataclass definition
- `src/task_manager.py`: Core business logic for task operations
- `src/cli.py`: Command-line interface and user interaction
- `src/main.py`: Application entry point

## Features

- In-memory storage using a simple list of Task objects
- Auto-incremented integer IDs starting from 1
- Menu-driven interface for intuitive navigation
- Input validation and user-friendly error messages
- Sub-second response times for all operations
- Support for up to 1000 tasks in memory