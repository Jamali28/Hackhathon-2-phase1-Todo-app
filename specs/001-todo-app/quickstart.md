# Quickstart Guide: Basic Level TODO Application

**Date**: 2025-12-24
**Feature**: Basic Level TODO Application
**Branch**: 001-todo-app

## Getting Started

### Prerequisites
- Python 3.13 or higher
- No external dependencies required

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is installed: `python --version`

### Running the Application
```bash
python -m src.main
```

### Basic Usage
1. Run the application with the command above
2. Use the numbered menu options (1-6) to interact:
   - Option 1: Add a new task
   - Option 2: View all tasks
   - Option 3: Update a task
   - Option 4: Delete a task
   - Option 5: Mark task as complete/incomplete
   - Option 6: Exit the application
3. Follow the prompts for each operation

### Example Workflow
1. Start the application: `python -m src.main`
2. Add a task (Option 1): Enter title and optional description
3. View tasks (Option 2): See all tasks with status indicators
4. Mark a task complete (Option 5): Enter task ID
5. Exit (Option 6): Close the application

### Testing
Run the unit tests with:
```bash
python -m unittest discover tests/
```