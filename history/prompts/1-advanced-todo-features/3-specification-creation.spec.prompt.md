---
id: 3
title: "Specification Creation"
stage: spec
date_iso: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: advanced-todo-features
branch: 1-advanced-todo-features
user: user
command: sp.specify
labels: ["specification", "todo", "advanced-features", "recurring-tasks", "due-dates"]
links:
  spec: specs/1-advanced-todo-features/spec.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/1-advanced-todo-features/spec.md"
  - "specs/1-advanced-todo-features/checklists/requirements.md"
tests_yaml: []
---

## Prompt Text

This prompt clearly states that Basic + Intermediate Levels are already fully implemented in the current `/src` codebase, and we are now extending it with Advanced Level features.

Create a complete, updated specification for the final Phase 1 Hackathon TODO application, now adding Advanced Level intelligent features on top of the fully implemented and working Basic + Intermediate Levels.

Important context:
- The current codebase in /src already fully implements Basic Level (Add, Delete, Update, View, Mark Complete) and Intermediate Level (Priorities, Tags, Search & Filter, Sort).
- The Task model currently uses a @dataclass with fields: id, title, description, complete, priority, tags.
- The application is a menu-driven console app with 8 options, in-memory storage, unit tests, clean modular structure (main.py, cli.py, task_manager.py, models.py).
- All existing functionality is working, tested, and must remain fully intact.

Now extend this existing implementation with Advanced Level features:
- Recurring Tasks: Support repeating tasks (daily, weekly, monthly) that automatically create the next occurrence when marked complete.
- Due Dates & Reminders: Assign due date (and optional time); display overdue/today indicators; show console reminder summary on startup and optionally during the session.

Output the full updated specification as a Markdown file (e.g., specs/003-advanced-level/spec.md).

Structure it clearly with the following sections:

### Feature Overview
A smart, console-based in-memory TODO application delivering:
- Core task management (Basic Level – already implemented)
- Powerful organization (Intermediate Level – already implemented)
- Intelligent automation with recurring tasks and due date reminders (Advanced Level – new)
— resulting in an impressive, complete Hackathon MVP.

### Functional Requirements

#### 1. Updated Task Model (Extend Existing)
Extend the current Task dataclass with these new fields (use appropriate defaults):
- due_datetime: Optional[datetime.datetime] = None  # Combines date and optional time
- recurrence: str = 'none'  # Choices: 'none', 'daily', 'weekly', 'monthly'
- recurrence_parent_id: Optional[int] = None  # Optional: links instances to original recurring template

#### 2. Add Task (Updated)
- Extend existing prompts to also ask:
  - Due date (YYYY-MM-DD, optional, press Enter to skip)
  - Due time (HH:MM, optional if date provided)
  - Recurrence (none/daily/weekly/monthly, default none)
- Parse dates/times safely with user-friendly error messages if invalid
- Store in the new fields

#### 3. Update Task (Updated)
- Allow modifying due date/time and recurrence (Enter to keep current value)

#### 4. View Task List (Updated)
- Add columns/indicators:
  - Due: Show formatted date/time (e.g., "2025-12-30" or "2025-12-30 14:30")
  - Overdue tasks: Mark with **[OVERDUE]** or similar text highlight
  - Recurring tasks: Show 🔁 or "(repeats)" symbol
- Ensure current sort options still work; add "by due date" if not present

#### 5. Mark as Complete (Updated for Recurring)
- If recurrence == 'none': Normal completion
- If recurrence set:
  - Mark current task as complete
  - Automatically create a new task (next occurrence) with:
    - Same title, description, priority, tags, recurrence
    - New due_datetime calculated:
      - daily   → +1 day
      - weekly  → +7 days
      - monthly → +1 month (preserve day; if invalid, use last day of month)
    - New unique ID
  - Display message: "Task completed. Next occurrence scheduled for [new date]."

#### 6. Due Dates & Reminders (New)
- On application startup:
  - Scan tasks and print a clear reminder banner showing:
    - Number of overdue tasks (with list of titles)
    - Tasks due today
    - Tasks due within next 24 hours (if time set)
- Optional (nice-to-have): Simple background thread that checks every 60 seconds and prints new alerts if a task becomes due/overdue during the session
- Use only standard library (datetime, threading if needed)

#### 7. Search & Filter (Updated)
- Add filter options for:
  - Overdue tasks
  - Due today
  - Recurring tasks only

#### 8. Sort Tasks (Updated)
- Add sort by due date (soonest first, overdue at top)

#### 9. Main Application Loop
- Keep current menu structure; reminders shown automatically on start and after commands if urgent
- No new menu options needed unless it improves UX

### Non-Functional Requirements
- Pure standard library only (datetime, optional threading)
- Safe date parsing and calculation (handle month-end gracefully)
- No infinite task creation loops
- Background reminder thread must be simple and not block exit
- Performance remains fast with reasonable number of tasks

### Acceptance Criteria
- Existing Basic + Intermediate features remain 100% functional
- Recurring tasks correctly generate next instances on completion (test all frequencies)
- Due date reminders accurately show on startup and (if implemented) during session
- Overdue indicators display correctly
- All new logic is fully covered by extended unit tests
- Edge cases handled: invalid dates, February 30 → adjust to 28/29, time-only due, etc.
- Code follows the updated constitution

## Response Text

Successfully created a comprehensive specification for the Advanced Level features of the TODO application. The specification includes:

- Detailed feature overview describing the smart, console-based TODO with recurring tasks and due date reminders
- Complete user scenarios for creating recurring tasks, managing due dates, and filtering/sorting
- Comprehensive functional requirements covering updated Task model, Add/Update task functionality, View task list enhancements, Mark as Complete behavior for recurring tasks, Due date reminders, Search & Filter updates, Sort functionality, and Main application loop integration
- Non-functional requirements covering technical constraints, security/reliability, and usability
- Key entities definition for Task, Recurrence Pattern, and Due Date
- Success criteria with primary objectives, performance metrics, user experience goals, and quality measures
- Assumptions about the existing system and user interaction
- Detailed acceptance criteria covering core functionality, edge case handling, user interface, and technical implementation

The specification is fully aligned with the existing Basic and Intermediate features and maintains backward compatibility. It provides clear guidance for implementing the Advanced features while following the project constitution.

## Outcome

✅ Impact: Successfully created comprehensive specification for Advanced Level features (recurring tasks, due dates) that extends existing functionality
🧪 Tests: Specification includes detailed acceptance criteria for comprehensive testing
📁 Files: Created specs/1-advanced-todo-features/spec.md and checklists/requirements.md
🔁 Next prompts: Plan the implementation of Advanced features
🧠 Reflection: Specification properly structured with all required sections and maintains compatibility with existing features

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for specification creation
- Prompt variant (if applicable): Standard specification creation
- Next experiment (smallest change to try): Create implementation plan for Advanced features