# Tasks: Advanced TODO Features - Recurring Tasks and Due Date Reminders

**Feature**: Advanced TODO Features: Recurring Tasks and Due Date Reminders
**Branch**: 1-advanced-todo-features
**Generated**: 2025-12-28

## Implementation Strategy

Implement in phases following the user story priority order (P1, P2, P3, etc.). Each user story should be independently testable and deliver value. Start with MVP (User Story 1) and incrementally add features.

## Dependencies

- User Story 1 (Recurring Tasks) must be completed before User Story 2 (Due Date Management) and User Story 3 (Filter/Sort Enhancement)
- User Story 2 and User Story 3 can be developed in parallel after User Story 1
- User Story 4 (Reminder System) depends on User Story 1 and User Story 2

## Parallel Execution Examples

- T005-T009 can be developed in parallel (different model methods)
- T015-T017 can be developed in parallel (different TaskManager methods)
- T022-T024 can be developed in parallel (different CLI methods)

## Phase 1: Setup

- [ ] T001 Set up project structure with extended models and updated tests directories
- [ ] T002 Verify existing Basic + Intermediate features are working correctly
- [ ] T003 Create test files for comprehensive Advanced feature testing

## Phase 2: Foundational Updates

- [X] T004 [P] Update Task dataclass in src/models.py to include due_datetime, recurrence, and recurrence_parent_id fields
- [X] T005 [P] Add validation for due_datetime field (datetime or None) in src/models.py
- [X] T006 [P] Add validation for recurrence field (none/daily/weekly/monthly) in src/models.py
- [X] T007 [P] Add recurrence_parent_id field to Task dataclass in src/models.py
- [X] T008 [P] Update docstrings for Task class in src/models.py
- [X] T009 [P] Add type hints to Task class in src/models.py

## Phase 3: [US1] Recurring Tasks Implementation

**User Story**: As a user, I want to create recurring tasks so that I don't have to manually add repetitive tasks like daily exercise, weekly team meetings, or monthly bill payments.

**Independent Test**: Can be fully tested by creating recurring tasks with different patterns (daily/weekly/monthly), completing them, and verifying that the next occurrence is created correctly with appropriate due dates, delivering the core value of automated task repetition.

- [X] T010 [P] [US1] Update add_task method in src/task_manager.py to accept due_datetime and recurrence parameters
- [X] T011 [P] [US1] Add validation for due_datetime parameter in add_task method in src/task_manager.py
- [X] T012 [P] [US1] Add validation for recurrence parameter in add_task method in src/task_manager.py
- [X] T013 [P] [US1] Update update_task method in src/task_manager.py to handle due_datetime and recurrence updates
- [X] T014 [P] [US1] Add validation for due_datetime in update_task method in src/task_manager.py
- [X] T015 [P] [US1] Add validation for recurrence in update_task method in src/task_manager.py
- [X] T016 [P] [US1] Update CLI add_task method in src/cli.py to prompt for due date
- [X] T017 [P] [US1] Update CLI add_task method in src/cli.py to prompt for due time
- [X] T018 [P] [US1] Update CLI add_task method in src/cli.py to prompt for recurrence pattern
- [X] T019 [P] [US1] Update CLI update_task method in src/cli.py to handle due_datetime changes
- [X] T020 [P] [US1] Update CLI update_task method in src/cli.py to handle recurrence changes
- [X] T021 [P] [US1] Implement calculate_next_occurrence method in src/task_manager.py for recurrence calculations
- [X] T022 [P] [US1] Implement create_next_recurrence method in src/task_manager.py for creating next task instances
- [X] T023 [P] [US1] Update mark_task_complete method in src/task_manager.py to handle recurring tasks
- [X] T024 [P] [US1] Add month-end edge case handling for monthly recurrence in src/task_manager.py
- [X] T025 [P] [US1] Update CLI mark_task_complete method in src/cli.py to show recurrence completion message
- [ ] T026 [US1] Add unit tests for adding recurring tasks with due dates in tests/test_task_manager.py
- [ ] T027 [US1] Add unit tests for updating recurring tasks in tests/test_task_manager.py
- [ ] T028 [US1] Add unit tests for recurring task completion and next occurrence creation in tests/test_task_manager.py
- [ ] T029 [US1] Add integration tests for recurring task workflows in tests/test_task_manager.py

## Phase 4: [US2] Due Date Management

**User Story**: As a user, I want to assign due dates to my tasks so that I can track deadlines and receive reminders.

**Independent Test**: Can be fully tested by adding tasks with due dates, viewing them to see due date indicators, and verifying that overdue tasks are properly identified, delivering the core value of deadline tracking.

- [X] T030 [P] [US2] Add parse_date_input utility function in src/task_manager.py for date parsing
- [X] T031 [P] [US2] Add parse_time_input utility function in src/task_manager.py for time parsing
- [X] T032 [P] [US2] Add is_overdue helper method in src/task_manager.py for overdue detection
- [X] T033 [P] [US2] Add is_due_today helper method in src/task_manager.py for due today detection
- [X] T034 [P] [US2] Add is_due_soon helper method in src/task_manager.py for due soon detection
- [X] T035 [P] [US2] Implement get_overdue_tasks method in src/task_manager.py
- [X] T036 [P] [US2] Implement get_due_today_tasks method in src/task_manager.py
- [X] T037 [P] [US2] Implement get_due_soon_tasks method in src/task_manager.py
- [X] T038 [P] [US2] Add format_datetime_display utility in src/task_manager.py for date formatting
- [X] T039 [P] [US2] Update CLI add_task method in src/cli.py to validate and parse due date input
- [X] T040 [P] [US2] Update CLI update_task method in src/cli.py to validate and parse due date input
- [ ] T041 [US2] Add unit tests for due date parsing and validation in tests/test_task_manager.py
- [ ] T042 [US2] Add unit tests for overdue detection in tests/test_task_manager.py
- [ ] T043 [US2] Add unit tests for due date/time helper functions in tests/test_task_manager.py
- [ ] T044 [US2] Add integration tests for due date management in tests/test_task_manager.py

## Phase 5: [US3] Enhanced Filter and Sort by Due Dates

**User Story**: As a user, I want to filter and sort my tasks by due dates so that I can focus on urgent tasks first.

**Independent Test**: Can be fully tested by adding tasks with various due dates, then using search/filter and sort functions to verify accurate results are returned in the correct order, delivering the value of organized task presentation based on deadlines.

- [X] T045 [P] [US3] Update filter_tasks method in src/task_manager.py to support overdue filtering
- [X] T046 [P] [US3] Update filter_tasks method in src/task_manager.py to support due today filtering
- [X] T047 [P] [US3] Update filter_tasks method in src/task_manager.py to support recurring tasks filtering
- [X] T048 [P] [US3] Implement sort by due date functionality in src/task_manager.py
- [X] T049 [P] [US3] Update set_sort_order method in src/task_manager.py to support due date sorting
- [ ] T050 [P] [US3] Add overdue detection to search_tasks method in src/task_manager.py
- [X] T051 [P] [US3] Add search and filter menu option to CLI in src/cli.py
- [X] T052 [P] [US3] Implement sort_tasks method in src/cli.py to include due date sorting
- [X] T053 [P] [US3] Update CLI search_and_filter_tasks method to support due date filters
- [ ] T054 [US3] Add unit tests for due date filtering in tests/test_task_manager.py
- [ ] T055 [US3] Add unit tests for due date sorting in tests/test_task_manager.py
- [ ] T056 [US3] Add integration tests for combined due date filtering and sorting in tests/test_task_manager.py

## Phase 6: [US4] Reminder System Implementation

**User Story**: As a user, I want to receive reminders about overdue and upcoming tasks so that I stay on top of my deadlines.

**Independent Test**: Can be fully tested by adding tasks with due dates, starting the application to see startup reminders, and verifying that the reminder system accurately identifies and displays overdue and upcoming tasks, delivering the core value of proactive deadline awareness.

- [X] T057 [P] [US4] Implement startup reminder banner in src/main.py to display overdue/due tasks
- [X] T058 [P] [US4] Add reminder display logic to main application loop in src/main.py
- [X] T059 [P] [US4] Implement optional background reminder thread in src/main.py
- [X] T060 [P] [US4] Add thread cleanup and shutdown logic in src/main.py
- [X] T061 [P] [US4] Update CLI view_tasks method in src/cli.py to show overdue indicators
- [X] T062 [P] [US4] Update CLI view_tasks method in src/cli.py to show recurrence symbols
- [X] T063 [P] [US4] Update task display formatting to include due date and recurrence indicators in src/cli.py
- [X] T064 [P] [US4] Add reminder banner to CLI initialization in src/cli.py
- [ ] T065 [US4] Add unit tests for reminder system logic in tests/test_task_manager.py
- [ ] T066 [US4] Add integration tests for startup reminder functionality in tests/test_task_manager.py
- [ ] T067 [US4] Add tests for background reminder thread (if implemented) in tests/test_task_manager.py

## Phase 7: Polish & Cross-Cutting Concerns

- [X] T068 Update main menu options to reflect reminder system in src/cli.py
- [X] T069 Update display_menu method to show reminder information in src/cli.py
- [X] T070 Add input validation for due date format in CLI in src/cli.py
- [X] T071 Add input validation for recurrence selection in CLI in src/cli.py
- [ ] T072 Update README.md with Advanced feature list and demo instructions
- [X] T073 Add comprehensive docstrings to all new methods in src/task_manager.py
- [X] T074 Add comprehensive docstrings to all new methods in src/cli.py
- [X] T075 Add type hints to all new methods in src/task_manager.py
- [X] T076 Add type hints to all new methods in src/cli.py
- [ ] T077 Perform full integration testing of all Advanced features together
- [ ] T078 Run performance tests with 1000+ tasks to ensure sub-second response times
- [ ] T079 Update test coverage to 80%+ for all modules
- [ ] T080 Perform final acceptance testing of all acceptance criteria from spec