# Feature Specification: Full Phase 1 TODO Application with Basic and Intermediate Features

**Feature Branch**: `1-todo-app-enhanced`
**Created**: 2025-12-27
**Status**: Draft
**Input**: User description: "Create a complete, updated, and detailed specification for the full Phase 1 Hackathon TODO application, covering both Basic Level (already implemented) and Intermediate Level features.

The application is a simple in-memory command-line Python console TODO tool. All existing Basic features must be preserved and seamlessly extended with the new Intermediate features for better organization and usability.

Basic Level features (for reference and continuity):
- Add Task
- Delete Task
- Update Task
- View Task List
- Mark as Complete/Incomplete

Intermediate Level features to add:
- Priorities & Tags/Categories: Assign priority levels (high/medium/low) and multiple tags/categories (e.g., work, home, personal)
- Search & Filter: Search by keywords (in title/description); filter by completion status, priority, and/or tags
- Sort Tasks: Sort the displayed task list by priority (high → medium → low), title (alphabetically), or creation order

All data remains stored only in memory (no persistence). The app runs as an interactive console loop until the user exits.

Output the full updated specification as a Markdown file suitable for the specs folder (e.g., specs/002-full-phase1-basic-plus-intermediate/spec.md or updated version).

Structure the specification clearly with the following sections:

### Feature Overview
Provide a concise summary: A polished, console-based, in-memory TODO application implementing core task management (Basic Level) plus enhanced organization through priorities, tags, search/filter, and sorting (Intermediate Level) – suitable as a complete Hackathon Phase 1 MVP.

### Functional Requirements

#### 1. Updated Task Model
Each task must have:
- Unique integer ID (auto-incremented, starting from 1)
- Title (string, required, non-empty)
- Description (string, optional)
- Completion status (boolean, default False)
- Priority (string: 'high', 'medium', 'low'; default 'medium')
- Tags (list of strings, optional, e.g., ['work', 'urgent', 'personal'])
- Creation timestamp (for potential future use, but not displayed unless needed)

Tasks are stored in a simple in-memory list (list of dicts or dataclasses).

#### 2. Add Task (Updated)
- Prompt user sequentially for:
  - Title (required)
  - Description (optional, press Enter to skip)
  - Priority (offer choices: high/medium/low, default medium)
  - Tags (comma-separated strings, optional, press Enter for none)
- Validate inputs (non-empty title, valid priority)
- Assign next ID and add to list
- Show confirmation with new task details

#### 3. View Task List (Updated)
- Display all tasks in a clean, aligned table-like format
- Columns/fields: ID, Status ([ ] or [x]), Priority (H/M/L or colored indicators if possible), Title, Tags (comma-separated), Description (truncated if long)
- If no tasks: display "No tasks yet. Add one to get started!"
- Apply current sort order (default: by ID/creation order)

#### 4. Update Task (Updated)
- Prompt for task ID (validate existence)
- Allow selective updates:
  - New title (Enter to keep)
  - New description (Enter to keep)
  - New priority (Enter to keep)
  - New tags (comma-separated, Enter to keep)
- Confirm changes made

#### 5. Delete Task
- Unchanged from Basic: prompt for ID, confirm deletion (y/n), remove if confirmed

#### 6. Mark as Complete/Incomplete
- Unchanged: prompt for ID, toggle status, confirm

#### 7. Search & Filter Tasks (New)
- Dedicated menu option
- Prompt user for:
  - Keyword search (optional: search in title and description)
  - Filter by status (all/complete/incomplete)
  - Filter by priority (all/high/medium/low)
  - Filter by tag (must contain specific tag)
- Display matching tasks using the same formatted view
- Show count of results (e.g., "Showing 5 of 12 tasks")

#### 8. Sort Tasks (New)
- Dedicated menu option
- Prompt user to choose sort order:
  1. By creation order (default)
  2. By priority (high → medium → low)
  3. By title (A → Z)
- Apply selected sort persistently until changed again
- Confirm sort applied; next View will reflect it

#### 9. Main Application Loop (Updated)
- Menu-driven with numbered options:
  1. Add task
  2. View tasks
  3. Update task
  4. Delete task
  5. Mark task as complete/incomplete
  6. Search & Filter tasks
  7. Sort tasks
  8. Exit
- Clear screen or separator between interactions (optional but nice)
- Handle invalid choices gracefully

### Non-Functional Requirements
- Pure Python standard library only (use `datetime` if needed for timestamps)
- Full type hints on all functions and classes
- Comprehensive docstrings for modules and public functions
- Graceful input validation and error messages (never crash)
- Consistent, readable console formatting (aligned columns where possible)
- Fast response times even with 100+ tasks

### Acceptance Criteria
- The application runs interactively and demonstrates all Basic + Intermediate features without errors
- All new fields (priority, tags) are correctly stored and displayed
- Search & Filter returns accurate subsets
- Sort applies correctly and persists across views
- Edge cases handled: empty list, no search matches, invalid inputs, canceling operations
- Code fully adheres to the project constitution (clean, modular, tested)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add and Manage Tasks with Enhanced Organization (Priority: P1)

As a user, I want to add tasks with priority levels and tags so that I can organize and categorize my work effectively.

**Why this priority**: This is the core functionality that enables users to create and organize tasks with enhanced features, forming the foundation for all other operations.

**Independent Test**: Can be fully tested by adding tasks with various priorities and tags, then viewing them to confirm they're stored and displayed correctly, delivering the core value of organized task management.

**Acceptance Scenarios**:
1. **Given** I am at the main menu, **When** I select "Add task" and provide title, priority (high/medium/low), and tags, **Then** the task is added to the list with the specified attributes
2. **Given** I have added tasks with different priorities and tags, **When** I view the task list, **Then** I see all attributes displayed clearly in a formatted table
3. **Given** I have added tasks with various attributes, **When** I update a task's priority or tags, **Then** the changes are reflected when viewing the task list

---

### User Story 2 - Search and Filter Tasks (Priority: P1)

As a user, I want to search and filter my tasks so that I can quickly find specific tasks based on keywords, status, priority, or tags.

**Why this priority**: This is essential for users with many tasks to efficiently locate and manage their work without manually scanning through all tasks.

**Independent Test**: Can be fully tested by adding multiple tasks with different attributes, then using search and filter functions to verify accurate results are returned, delivering the value of efficient task discovery.

**Acceptance Scenarios**:
1. **Given** I have multiple tasks with various titles and descriptions, **When** I use the search function with a keyword, **Then** only tasks containing that keyword are displayed
2. **Given** I have tasks with different priorities and completion statuses, **When** I filter by priority or status, **Then** only matching tasks are displayed
3. **Given** I have tasks with various tags, **When** I filter by a specific tag, **Then** only tasks with that tag are displayed

---

### User Story 3 - Sort Tasks for Better Organization (Priority: P2)

As a user, I want to sort my tasks by different criteria so that I can organize my view based on priority, alphabetical order, or creation sequence.

**Why this priority**: This enhances the user experience by allowing customization of task display order, making it easier to focus on important tasks or find specific items.

**Independent Test**: Can be fully tested by adding tasks with various priorities and titles, then applying different sort options to verify tasks are displayed in the correct order, delivering the value of organized task presentation.

**Acceptance Scenarios**:
1. **Given** I have tasks with mixed priorities, **When** I sort by priority, **Then** tasks are displayed with high priority first, followed by medium, then low
2. **Given** I have tasks with titles starting with different letters, **When** I sort alphabetically, **Then** tasks are displayed in A-Z order
3. **Given** I have applied a sort order, **When** I view tasks, **Then** the sort persists until I change it again

---

### User Story 4 - Core Task Management (Priority: P1)

As a user, I want to perform basic task operations (add, view, update, delete, mark complete) so that I can manage my tasks effectively.

**Why this priority**: This represents the fundamental functionality that users expect from any TODO application, providing the essential task management capabilities.

**Independent Test**: Can be fully tested by performing all basic operations on tasks and verifying they work correctly, delivering the core value of task management.

**Acceptance Scenarios**:
1. **Given** I have existing tasks, **When** I delete a task, **Then** it is removed from the list
2. **Given** I have an incomplete task, **When** I mark it complete, **Then** its status changes to complete
3. **Given** I have an existing task, **When** I update its details, **Then** the changes are saved and reflected in the view

---

### Edge Cases

- What happens when a user tries to update/delete a task with an invalid ID? The system should display a helpful error message and return to the main menu.
- How does the system handle empty search results? The system should display "No matching tasks found" and return to the main menu.
- What happens when a user enters invalid priority values? The system should prompt for a valid priority choice (high/medium/low).
- How does the system handle tasks with very long titles or descriptions? The system should truncate long text appropriately in the display while preserving full content internally.
- What happens when a user tries to sort an empty task list? The system should handle this gracefully and display an appropriate message.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add new tasks with title, description, priority, and tags
- **FR-002**: System MUST assign a unique integer ID to each task (auto-incremented starting from 1)
- **FR-003**: System MUST validate task titles are non-empty strings
- **FR-004**: System MUST support priority levels: 'high', 'medium', 'low' with default 'medium'
- **FR-005**: System MUST support tags as a list of strings that can be assigned to tasks
- **FR-006**: System MUST allow users to delete tasks by ID
- **FR-007**: System MUST allow users to update task title, description, priority, and tags by ID
- **FR-008**: System MUST allow users to view all tasks in a formatted table-like display
- **FR-009**: System MUST display tasks with ID, status indicator ([ ] or [x]), priority (H/M/L), title, tags, and truncated description
- **FR-010**: System MUST allow users to mark tasks as complete/incomplete by ID
- **FR-011**: System MUST provide search functionality that searches in title and description fields
- **FR-012**: System MUST provide filter functionality by completion status (all/complete/incomplete)
- **FR-013**: System MUST provide filter functionality by priority (all/high/medium/low)
- **FR-014**: System MUST provide filter functionality by tags (tasks containing specific tag)
- **FR-015**: System MUST provide sort functionality by priority (high → medium → low)
- **FR-016**: System MUST provide sort functionality by title (A → Z)
- **FR-017**: System MUST provide sort functionality by creation order (default)
- **FR-018**: System MUST apply sort selections persistently until changed by the user
- **FR-019**: System MUST store all data in-memory only (no persistent storage)
- **FR-020**: System MUST provide an interactive CLI menu interface with numbered options (1-8)
- **FR-021**: System MUST handle invalid inputs gracefully with user-friendly error messages
- **FR-022**: System MUST display "No tasks yet. Add one to get started!" when task list is empty
- **FR-023**: System MUST show result count when displaying search/filter results (e.g., "Showing 5 of 12 tasks")
- **FR-024**: System MUST validate priority input and only accept 'high', 'medium', or 'low' values
- **FR-025**: System MUST handle comma-separated input for tags and convert to list format
- **FR-026**: System MUST truncate long descriptions appropriately in the display format
- **FR-027**: System MUST confirm actions when deleting tasks (y/n prompt)

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single TODO item with ID, title, description, completion status, priority, tags, and creation timestamp
- **TaskList**: Collection of Task entities managed in-memory with support for search, filter, and sort operations
- **Priority**: Enumeration of valid priority levels: 'high', 'medium', 'low'
- **Tag**: String identifier that can be associated with tasks for categorization and filtering

## Clarifications

### Session 2025-12-27

- Q: How should we handle existing tasks when extending the Task model with new fields? → A: Use dataclasses with default values for backward compatibility
- Q: Should we maintain existing Basic functionality while adding Intermediate features? → A: Extend existing functionality without breaking it
- Q: Where should new logic (search, filter, sort) be implemented? → A: All new logic in task_manager.py with helper functions
- Q: How should we handle testing during the extension? → A: Update existing tests to cover new functionality
- Q: How should the CLI menu be updated? → A: Expand CLI menu to 8 options while preserving current flow

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add, delete, update, view, search, filter, and sort tasks with sub-second response times even with 1000+ tasks
- **SC-002**: System handles up to 1000 tasks in memory without performance degradation for all operations including search and sort
- **SC-003**: All core operations (add, delete, update, list, mark complete, search, filter, sort) have unit test coverage of 80%+
- **SC-004**: CLI interface provides clear, consistent formatting with aligned columns and user-friendly error messages
- **SC-005**: Search and filter operations return accurate results that match the specified criteria 100% of the time
- **SC-006**: Sort operations correctly order tasks according to the selected criteria (priority, title, creation order)
- **SC-007**: System handles all edge cases gracefully without crashing, displaying appropriate error messages to users
- **SC-008**: All Basic Level features continue to work seamlessly after adding Intermediate Level features
- **SC-009**: Users can complete a full workflow of adding tasks with priorities/tags, organizing them, and managing their completion status