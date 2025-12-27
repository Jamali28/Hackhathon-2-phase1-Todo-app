# Advanced TODO Features: Recurring Tasks and Due Date Reminders

## Feature Overview

A smart, console-based in-memory TODO application delivering:
- Core task management (Basic Level – already implemented)
- Powerful organization (Intermediate Level – already implemented)
- Intelligent automation with recurring tasks and due date reminders (Advanced Level – new)
— resulting in an impressive, complete Hackathon MVP.

The application extends the existing TODO functionality with intelligent automation features that help users manage repetitive tasks and stay on top of their deadlines. The new features include recurring tasks that automatically generate the next occurrence when completed, and due date reminders that alert users to overdue and upcoming tasks.

## User Scenarios

### Scenario 1: Creating a Recurring Task
As a user, I want to create a recurring task so that I don't have to manually add repetitive tasks like daily exercise, weekly team meetings, or monthly bill payments.
- User navigates to "Add task" option
- User enters task details (title, description, priority, tags)
- User specifies due date and time (optional)
- User selects recurrence pattern (daily, weekly, monthly, or none)
- System creates the task and displays confirmation
- When task is marked complete, system automatically creates the next occurrence

### Scenario 2: Managing Due Dates
As a user, I want to assign due dates to my tasks so that I can track deadlines and receive reminders.
- User adds a task with a due date and optional time
- User views task list to see due date indicators
- System highlights overdue tasks and shows upcoming due tasks
- On startup, system displays reminder banner showing overdue and due-soon tasks

### Scenario 3: Filtering and Sorting by Due Dates
As a user, I want to filter and sort my tasks by due dates so that I can focus on urgent tasks first.
- User navigates to search/filter options
- User selects filter for overdue tasks, tasks due today, or recurring tasks
- User chooses to sort by due date to see tasks in chronological order
- System displays filtered/sorted results

## Functional Requirements

### 1. Updated Task Model (Extend Existing)
The system must extend the current Task dataclass with new fields to support advanced features:
- `due_datetime`: Optional[datetime.datetime] = None - Combines date and optional time
- `recurrence`: str = 'none' - Choices: 'none', 'daily', 'weekly', 'monthly'
- `recurrence_parent_id`: Optional[int] = None - Links instances to original recurring template

### 2. Add Task (Updated)
The system must extend the existing task creation functionality to include due dates and recurrence:
- When adding a task, the system prompts for due date (strict YYYY-MM-DD format only, optional, press Enter to skip)
- If date is provided, the system prompts for due time (HH:MM, optional)
- The system prompts for recurrence pattern (none/daily/weekly/monthly, default none)
- The system parses dates/times safely with user-friendly error messages for invalid inputs
- The system stores the new fields in the task record
- If an invalid date is entered, the system shows a clear error message and allows re-entry

### 3. Update Task (Updated)
The system must allow modification of due date/time and recurrence settings:
- When updating a task, the system allows modifying due date/time and recurrence
- User can press Enter to keep current values
- The system validates new date/time inputs and shows appropriate error messages
- Changes are saved to the task record

### 4. View Task List (Updated)
The system must display additional information for tasks with due dates and recurrence:
- The system adds a "Due" column showing formatted date/time (e.g., "2025-12-30" or "2025-12-30 14:30")
- The system marks overdue tasks with **[OVERDUE]** text indicator (visible in all terminals)
- The system indicates recurring tasks with 🔁 or "(repeats)" symbol
- The system ensures current sort options still work
- The display remains readable and properly formatted even with additional columns

### 5. Mark as Complete (Updated for Recurring)
The system must handle recurring tasks differently when marked complete:
- If recurrence == 'none': Normal completion behavior
- If recurrence is set:
  - The system marks current task as complete
  - The system automatically creates a new task (next occurrence) with:
    - Same title, description, priority, tags, recurrence
    - New due_datetime calculated:
      - daily → +1 day
      - weekly → +7 days
      - monthly → +1 month (preserve day; if target day doesn't exist, use last day of target month - e.g., Jan 31 → Feb 28/29 → Mar 31 → Apr 30)
    - New unique ID
  - The system displays message: "Task completed. Next occurrence scheduled for [new date]."
- The system prevents infinite task creation loops

### 6. Due Dates & Reminders (New)
The system must provide reminder functionality based on due dates:
- On application startup, the system scans tasks and prints a clear reminder banner showing:
  - Number of overdue tasks (with list of titles)
  - Tasks due today
  - Tasks due within next 24 hours (if time set)
- The system implements a background thread with daemon configuration that checks every 60 seconds and prints new alerts if a task becomes due/overdue during the session
- The system uses only standard library (datetime, threading if needed)
- The reminder thread uses daemon configuration and does not block application exit

### 7. Search & Filter (Updated)
The system must extend search and filter functionality to include due date and recurrence criteria:
- The system adds filter options for overdue tasks
- The system adds filter options for tasks due today
- The system adds filter options for recurring tasks only
- The system maintains all existing search and filter functionality
- The new filters work correctly with existing filters (can combine multiple criteria)

### 8. Sort Tasks (Updated)
The system must extend sorting functionality to include due date sorting:
- The system adds sort by due date (soonest first, overdue at top)
- The system maintains all existing sort functionality
- The sort options are clearly presented to the user
- Sorting by due date correctly handles tasks without due dates (e.g., places them at the end)

### 9. Main Application Loop
The system must integrate reminder functionality into the main application flow:
- The system maintains current menu structure
- Reminders are shown automatically on startup
- Reminders may be shown after commands if urgent tasks are detected
- The system does not require new menu options unless it improves UX
- The main loop continues to function normally with all existing features

## Non-Functional Requirements

### Technical Constraints
- The system uses pure standard library only (datetime, optional threading)
- The system implements safe date parsing and calculation (handle month-end gracefully)
- The system prevents infinite task creation loops
- Background reminder thread must be simple and not block exit
- Performance remains fast with reasonable number of tasks

### Security & Reliability
- The system handles all invalid inputs gracefully without crashing
- The system validates all date and recurrence inputs with appropriate error messages
- The system maintains data integrity when creating recurring task instances
- The system ensures proper cleanup of background threads on exit

### Usability
- The system provides clear, user-friendly error messages for invalid inputs
- The system maintains consistent UI/UX patterns with existing functionality
- The system provides clear feedback when recurring tasks are created
- The system ensures new features do not complicate the interface unnecessarily

## Key Entities

### Task
- **Description**: The core entity representing a TODO item
- **Attributes**:
  - id: Unique identifier
  - title: Task title
  - description: Task description
  - completed: Completion status
  - priority: Priority level (high/medium/low)
  - tags: List of tags
  - due_datetime: Optional due date and time
  - recurrence: Recurrence pattern (none/daily/weekly/monthly)
  - recurrence_parent_id: Link to parent recurring task template (when this is a recurrence instance, points to the original recurring task)

### Recurrence Pattern
- **Description**: Defines how often a task repeats
- **Values**: none, daily, weekly, monthly
- **Behavior**: Determines when next occurrence is created

### Due Date
- **Description**: Date and time when a task is due
- **Format**: datetime object with date and optional time
- **Behavior**: Used for overdue detection and reminder notifications

## Success Criteria

### Primary Objectives
- **Feature Integration**: 100% of existing Basic + Intermediate features remain fully functional after Advanced features are added
- **Recurring Task Accuracy**: Recurring tasks correctly generate next instances on completion for all frequencies (daily, weekly, monthly)
- **Reminder Effectiveness**: Due date reminders accurately display on startup and during session as specified
- **Overdue Visibility**: Overdue indicators display correctly and are clearly visible to users

### Performance Metrics
- **Response Time**: All operations complete in under 1 second even with up to 1000 tasks
- **Startup Time**: Application starts and displays reminders within 3 seconds
- **Memory Usage**: Application memory usage remains reasonable with recurring tasks (under 100MB for 1000 tasks)

### User Experience
- **Task Creation Flow**: Users can add tasks with due dates and recurrence in under 30 seconds
- **Reminder Clarity**: 95% of users understand the reminder banner and overdue indicators on first use
- **Feature Discovery**: Users can discover and use new features without extensive training

### Quality Measures
- **Test Coverage**: All new logic is covered by extended unit tests with minimum 80% coverage
- **Edge Case Handling**: System handles all specified edge cases (invalid dates, February 30, etc.) gracefully
- **Code Quality**: Implementation follows the updated constitution and coding standards

## Assumptions

- The existing Basic and Intermediate features are stable and fully functional
- The system will be used by a single user (no multi-user requirements)
- All data remains in memory only (no persistent storage requirements)
- Users will interact with the application through the console interface
- Background reminder thread is optional and can be disabled if needed
- The application runs on a local machine with reliable timekeeping
- Users understand basic date formats (YYYY-MM-DD) and time formats (HH:MM)

## Clarifications

### Session 2025-12-28

- Q: Should the system implement the optional background thread for ongoing reminders, or should we focus only on startup reminders? → A: Implement background thread with daemon configuration for real-time notifications
- Q: For monthly recurrence, when recurring from a day that doesn't exist in the target month (e.g., Jan 31 → Feb), what's the exact behavior? → A: January 31 → February 28/29 → March 31 → April 30 (use last day when target invalid)
- Q: What format should be used for overdue task indicators in the display? → A: Text marker: **[OVERDUE]** (works everywhere, clear)
- Q: When a recurring task creates a new instance after completion, what's the parent-child relationship? → A: New task has recurrence_parent_id = original task ID
- Q: What date/time input format should be supported for due dates? → A: Strict YYYY-MM-DD format only (unambiguous)

## Acceptance Criteria

### Core Functionality
- [ ] Existing Basic + Intermediate features remain 100% functional after Advanced features are added
- [ ] Recurring tasks correctly generate next instances on completion for all frequencies (daily, weekly, monthly)
- [ ] Due date reminders accurately show on startup as specified
- [ ] Overdue indicators display correctly in task list view with **[OVERDUE]** text markers
- [ ] All new logic is fully covered by extended unit tests

### Edge Case Handling
- [ ] Invalid dates are handled gracefully with appropriate error messages
- [ ] February 30th dates are adjusted to 28th or 29th appropriately
- [ ] Month-end edge cases are handled (e.g., January 31st recurring monthly becomes February 28th/29th, using last day when target day doesn't exist)
- [ ] Tasks without due dates sort and filter correctly with new options
- [ ] Background thread cleans up properly on exit

### User Interface
- [ ] New task creation prompts are clear and user-friendly
- [ ] Due date and recurrence information displays clearly in task list with **[OVERDUE]** indicators
- [ ] Filter and sort options for new features work correctly
- [ ] Reminder banner is informative and not overwhelming
- [ ] Help text and error messages are clear and helpful
- [ ] Date input accepts only YYYY-MM-DD format with clear validation

### Technical Implementation
- [ ] Code follows the updated constitution guidelines
- [ ] Implementation uses only standard library as required
- [ ] No infinite task creation loops occur
- [ ] Performance remains acceptable with new features
- [ ] All new functionality is properly documented
- [ ] Background reminder thread implemented with daemon configuration for real-time notifications
- [ ] Recurring task instances maintain parent-child relationship via recurrence_parent_id