---
id: 1
title: "Update Constitution with Intermediate Features"
stage: constitution
date_iso: 2025-12-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: sp.constitution
labels: ["constitution", "features", "intermediate-level"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

## Prompt Text

Create an updated project constitution for the Hackathon Phase 1 TODO application, now incorporating both Basic and Intermediate Levels. The app remains a simple command-line Python console-based in-memory TODO tool.

The Basic Level features (already implemented) include:
- Add Task (create new tasks with title and description)
- Delete Task (remove by ID)
- Update Task (modify title/description by ID)
- View Task List (display all tasks with ID, title, description, and completion status)
- Mark as Complete (toggle completion status by ID)

Now add Intermediate Level features for organization and usability:
- Priorities & Tags/Categories: Assign priority levels (high/medium/low) and tags/labels (e.g., work/home) to tasks
- Search & Filter: Search tasks by keywords in title/description; filter by status (complete/incomplete), priority, or date (if dates are added, e.g., due date)
- Sort Tasks: Sort the task list by due date, priority, or alphabetically by title

All data is still stored in memory only (no files or databases). The app runs as an interactive console loop until exit. Build upon the existing Basic implementation without breaking it.

Output the updated constitution as a complete Markdown file content for `.specify/memory/constitution.md` (overwriting or versioning as needed).

Structure it clearly with sections. Use bullet points or numbered lists for principles. Update all relevant sections to incorporate the new features while maintaining the original principles.

Key sections and content guidelines:

### Project Overview
Briefly describe the updated project: Phase 1 of a Hackathon TODO app – in-memory console TODO with core CRUD + completion toggle (Basic) plus priorities/tags, search/filter, and sorting (Intermediate) for improved organization and usability.

### Core Principles
- Simplicity First: Still an MVP, but now polished with usability features. Prioritize incremental addition without over-complicating the Basic foundation.
- Spec-Driven Development: All new features must derive from updated specifications via Spec-Kit Plus. Never implement without updating specs, plans, and tasks.
- Clean Code: Follow PEP 8. Use meaningful names, short functions (single responsibility), type hints everywhere, and docstrings for public functions/modules. Ensure new features integrate cleanly.

### Technical Stack
- Python 3.13+
- Package manager: UV
- No external dependencies beyond standard library (keep it pure Python)
- In-memory storage: Extend the existing list of dictionaries or dataclasses to include new fields like priority, tags, due_date
- CLI: Built with standard input()/print(), interactive loop – expand menu with new options

### Code Quality Standards
- Use type hints with Python 3.13 features (e.g., | for unions)
- Modular structure: Update /src with additional methods in existing modules (e.g., add to task_manager.py for new logic, cli.py for new commands)
- Functions should be pure where possible; keep side effects minimal
- Graceful error handling: Validate inputs for new fields (e.g., valid priority levels), user-friendly messages, no crashes

### Testing Requirements
- Use Python's built-in `unittest` module
- Update tests to cover new features: priorities/tags assignment, search/filter correctness, sorting orders
- Include edge cases: filtering empty results, invalid priorities, sorting with mixed data
- Aim for high coverage of all business logic, including integrations between Basic and Intermediate

### User Experience Guidelines
- Intuitive CLI: Expand menu-driven options to include new commands (e.g., set priority/tag, search, filter, sort)
- Consistent formatting: Update task list display to include priority, tags, due date (if added)
- Helpful messages and prompts for new interactions (e.g., multi-select for tags)

### Development Governance
- Use Spec-Kit Plus exclusively: Update Constitution → Specify → Clarify → Plan → Tasks → Implement for Intermediate additions
- Track all specification versions in a specs history folder, noting updates for Intermediate
- Git commits: Clear, atomic messages; branch for Intermediate if needed
- README.md: Update with new features, setup with UV, running instructions, demo of all features (Basic + Intermediate)
- Decisions prioritize speed and correctness for Hackathon demo, ensuring seamless integration

Ensure the constitution enforces consistency in AI-generated code (via Claude) and guides the project to a working, demonstrable MVP with enhanced usability.
MarkdownUse this prompt with the /sp.specify command in your Claude Code session to update the specification for including the Intermediate Level features.

Create an updated, detailed specification for the full Phase 1 TODO application, now including both Basic Level (already specified) and Intermediate Level features.

The application is a simple in-memory command-line Python console TODO tool. Retain all Basic features and add the Intermediate ones seamlessly.

Basic features (for reference):
- Add Task: Create a new task with required title and optional description
- Delete Task: Remove a task by its unique ID
- Update Task: Modify the title and/or description of an existing task by ID
- View Task List: Display all tasks with clear formatting
- Mark as Complete: Toggle the completion status of a task by ID

Intermediate features to add:
- Priorities & Tags/Categories: Assign priority (high/medium/low) and tags (list of strings, e.g., ['work', 'home']) to tasks during add/update
- Search & Filter: Search by keywords in title/description; filter by completion status, priority, or due date (add due date field if needed for filtering/sorting)
- Sort Tasks: Sort displayed list by due date, priority (high>medium>low), or alphabetically by title

All data must be stored only in memory. The app runs as an interactive console loop until exit. Update the task model and commands accordingly.

Output the full updated specification as a Markdown file suitable for saving in the specs folder (e.g., specs/002-intermediate-level/spec.md or an updated version).

Structure the specification clearly with the following sections:

### Feature Overview
Provide a concise summary: A console-based, in-memory TODO list with Basic CRUD/completion plus Intermediate organization features (priorities/tags, search/filter, sort) for a polished Hackathon MVP.

### Functional Requirements

#### 1. Updated Task Model
- Each task must now have:
  - Unique integer ID (auto-incremented, starting from 1)
  - Title (string, required, non-empty)
  - Description (string, optional)
  - Completion status (boolean, default False)
  - Priority (string: 'high', 'medium', 'low'; default 'medium')
  - Tags (list of strings, optional, e.g., ['work', 'urgent'])
  - Due Date (optional datetime.date, for filtering/sorting)
- Tasks stored in a simple in-memory list.

#### 2. Add Task (Updated)
- Prompt for title (required), description (optional), priority (select from options), tags (comma-separated input), due date (optional, format YYYY-MM-DD)
- Validate inputs (e.g., valid priority, parse date)
- Assign ID and add to list
- Confirm success

#### 3. View Task List (Updated)
- Display all tasks in a clean format, now including priority, tags, due date
- If no tasks, show message
- Default sort by ID

#### 4. Update Task (Updated)
- Prompt for ID
- Allow updating title, description, priority, tags, due date (Enter to skip)
- Validate and confirm

#### 5. Delete Task
- Unchanged, but ensure it handles updated model

#### 6. Mark as Complete/Incomplete
- Unchanged

#### 7. Set Priority/Tags (or integrate into Update)
- If separate, prompt for ID and new priority/tags

#### 8. Search & Filter
- New command: Prompt for search keyword (optional) and filters (status: complete/incomplete, priority: high/medium/low, due date range)
- Display matching tasks in formatted list
- Combine search and filters (AND logic)

#### 9. Sort Tasks
- New command: Prompt for sort criteria (due date ascending/descending, priority descending, title alphabetical)
- Apply sort to the next View command or have a persistent sort option

#### 10. Main Application Loop (Updated)
- Expand menu:
  1. Add task
  2. View tasks
  3. Update task
  4. Delete task
  5. Mark task
  6. Search/Filter tasks
  7. Sort tasks
  8. Exit
- Handle invalid inputs

### Non-Functional Requirements
- Pure standard library (use datetime for dates)
- Full type hints and docstrings
- Graceful error handling
- Consistent output

### Acceptance Criteria
- App runs and demonstrates all Basic + Intermediate features
- Data persists in session only
- Edge cases handled for new fields
- Code follows constitution

## Response Text

I have successfully updated the project constitution for the Hackathon Phase 1 TODO application to incorporate both Basic and Intermediate Level features. The updated constitution (version 1.1.0) now includes:

- Enhanced Project Overview that describes both Basic and Intermediate features
- Updated Core Principles that account for Intermediate features while maintaining the original foundation
- Expanded Technical Stack section with new requirements for priorities, tags, and search/filter/sort functionality
- Updated Code Quality Standards that include requirements for the new Intermediate features
- Enhanced Testing Requirements that cover both Basic and Intermediate features
- Improved User Experience Guidelines that address the expanded CLI with new features
- Updated governance section with the new version

The constitution now properly supports the full application with Basic features (Add, Delete, Update, View, Mark Complete) and Intermediate features (Priorities/Tags, Search/Filter, Sort) while maintaining the in-memory console-based design. The version has been incremented from 1.0.0 to 1.1.0 to reflect the addition of Intermediate Level features.

## Outcome

The constitution file `.specify/memory/constitution.md` has been successfully updated with version 1.1.0, incorporating all requested Intermediate Level features while preserving the existing Basic Level functionality. The file includes comprehensive guidelines for implementing priorities, tags, search, filter, and sort features in a way that integrates cleanly with the existing codebase.

## Evaluation

The updated constitution successfully meets all requirements specified in the prompt:
- ✅ Incorporates both Basic and Intermediate Level features
- ✅ Maintains existing Basic functionality while adding new features
- ✅ Follows the required structure with appropriate sections
- ✅ Includes all requested content guidelines
- ✅ Properly formatted as a Markdown file
- ✅ Version incremented appropriately from 1.0.0 to 1.1.0