<!--
Sync Impact Report:
- Version change: 1.1.0 → 2.0.0
- Modified principles: Updated principles to include Advanced Level features (Recurring tasks, Due dates, Console-based reminders)
- Added sections: Enhanced Core Principles to include recurring tasks and due date features, updated Technical Stack to include datetime and threading guidance, updated Code Quality Standards, Testing Requirements, and User Experience Guidelines for Advanced features
- Removed sections: N/A
- Templates requiring updates: ✅ Updated all relevant templates
- Follow-up TODOs: None
-->
# Hackathon Phase 1 TODO Application Constitution

## Project Overview

This is Phase 1 of a Hackathon TODO application - a smart, console-based TODO tool that implements the core CRUD operations plus completion toggle (Basic Level), enhanced organization features including priorities/tags, search/filter, and sorting (Intermediate Level), and intelligent features with recurring tasks and due date reminders (Advanced Level). The application provides comprehensive task management functionality through an interactive command-line interface, with all data stored in memory only (no persistent storage). The final product is an impressive, polished Hackathon MVP with advanced scheduling capabilities and reminder systems.

## Core Principles

### Simplicity First
This is a Hackathon MVP that prioritizes quick implementation, readability, and minimalism. The codebase must avoid over-engineering, unnecessary abstractions, or extra features beyond the core functions: Add, Delete, Update, View, Mark Complete, Priorities/Tags, Search/Filter, Sort, Recurring Tasks, and Due Date Reminders. The focus is on delivering a working solution that meets the Basic, Intermediate, and Advanced requirements efficiently while maintaining the original foundation. Advanced features must remain easy to understand and demo, avoiding over-complexity (e.g., no full cron, no external notification libs).

### Incremental Extension
All new code must build safely on the existing working codebase without breaking or rewriting Basic/Intermediate features. New Advanced features (recurring tasks, due dates) must integrate seamlessly with existing functionality. No rewriting of working code is allowed unless strictly necessary to accommodate new features safely.

### Spec-Driven Development
All code must derive from specifications created via the Spec-Kit Plus workflow. Implementation must follow the sequence: specification → plan → tasks → implementation. No features or code changes should be made without proper specification, planning, and task breakdown first. This ensures systematic development aligned with requirements for Basic, Intermediate, and Advanced features.

### Clean Code
The codebase must follow PEP 8 style guidelines. All functions should have meaningful names, be kept short with single responsibility, include type hints for all parameters and return values, and contain docstrings for all public functions and modules. Code readability and maintainability are prioritized over premature optimization. New Advanced features must integrate cleanly with existing Basic and Intermediate features without breaking existing functionality. Prefer @dataclass for Task with proper defaults and immutable-style where possible; careful mutation for recurrence.

### Performance Efficiency
The application must use efficient in-memory data structures (list of dictionaries or dataclasses) to achieve O(1) average-case operations where possible. Since it's console-based and in-memory, all operations must complete in sub-second response times for up to 1000 tasks. The focus is on algorithmic efficiency and avoiding unnecessary computational overhead, especially for search and sort operations on larger datasets. Background reminder threads (if implemented) must be lightweight and efficient.

### Error Handling and User Experience
The application must handle errors gracefully with user-friendly messages and never crash on invalid input. Input validation must be comprehensive for new Advanced features (date formats, recurrence rules, invalid dates), with clear error messages that guide users toward correct usage. The CLI interface must be intuitive and consistent in its formatting and behavior across all features. No timezone handling — use local naive datetime. Graceful handling of invalid dates is essential.

### Test-Driven Development
All functionality must be covered by unit tests using Python's built-in unittest module. Testing must follow TDD practices where tests are written before implementation. Test coverage should aim for at least 80% of business logic, with special attention to edge cases like invalid IDs, empty lists, duplicate operations, and new Advanced features such as recurrence rules (daily/weekly/monthly, including month-end edge cases), next occurrence date calculation, overdue/today/upcoming detection, reminder logic, and background reminder thread safety.

## Technical Stack

- Python 3.13+ with modern typing features (e.g., | for unions)
- Package manager: UV for dependency management
- No external dependencies beyond Python standard library (pure Python implementation)
- In-memory storage using list of dictionaries or dataclasses, extended to include priority, tags, due_date, and recurrence_rule fields
- CLI interface built with standard input()/print() functions and interactive loop - expanded menu options for new features
- Modular project structure with separate modules in `/src` directory
- datetime module heavily used for date handling in Advanced features
- Optional threading.Thread for simple background reminders if needed
- Standard library only - no external dependencies

## Code Quality Standards

- Use type hints with Python 3.13 features (e.g., | for unions) for all new Advanced features
- Modular structure: `/src` directory with separate modules (`tasks.py` for business logic, `cli.py` for interface, `main.py` as entry point) - enhanced with new methods for recurring tasks, due dates, and reminders
- Functions should be pure where possible; keep side effects minimal and well-defined for new features
- Consistent naming conventions following PEP 8 across all features
- Comprehensive docstrings for all public functions and modules, especially for new Advanced feature methods
- Meaningful variable and function names that clearly express intent for Basic, Intermediate, and Advanced features
- New task model must include ID, title, description, completion status, priority, tags, due_date, and recurrence_rule fields
- Pure functions for date calculations and recurrence logic
- Comprehensive input validation for dates (user-friendly error messages)

## Testing Requirements

- Use Python's built-in `unittest` module for all tests
- Write tests for all core task operations: add, delete, update, mark complete, and list (Basic features)
- Write tests for all Intermediate features: priorities/tags assignment, search/filter correctness, sorting orders
- Write tests for all Advanced features: recurrence rules (daily/weekly/monthly, including month-end edge cases), next occurrence date calculation, overdue/today/upcoming detection, reminder logic on startup, background reminder thread (if implemented) safety
- Include comprehensive edge case tests: empty list, invalid IDs, duplicate IDs (with prevention), boundary conditions
- Include edge case tests for new features: filtering empty results, invalid priorities, sorting with mixed data, invalid date formats, invalid recurrence rules, month-end edge cases for recurring tasks
- Aim for high coverage of business logic (minimum 80%) including integrations between Basic, Intermediate, and Advanced features
- Test that marking recurring task complete creates correct next instance
- Test both positive and negative scenarios for all features
- Ensure tests are fast, deterministic, and independent of each other
- Add rigorous tests for overdue/today/upcoming detection and reminder logic

## User Experience Guidelines

- Intuitive CLI with expanded menu-driven interface to include new Advanced features (set recurrence rule, set due date, view reminders)
- Consistent formatting for task display: ID, status indicator ([ ] or [x]), title, description, priority, tags, due date, recurrence indicator
- Clear, helpful messages and prompts that guide user actions for new features (e.g., multi-select for tags, date format instructions, recurrence rule selection)
- Consistent command structure and response format across all features
- Graceful handling of invalid inputs with helpful error messages for new Advanced features
- Clear indication of available commands and their usage in the expanded menu system
- Enhanced task list display to include priority, tags, due date, and recurrence information when viewing tasks
- Clear feedback on recurrence scheduling and due reminders
- Non-intrusive reminders (console print banners, not beeps/popups)
- Enhanced view to show overdue indicators and upcoming due tasks
- Clear status indicators for recurring tasks

## Governance

This constitution governs all development activities for the Hackathon Phase 1 TODO application. All code changes, architectural decisions, and feature implementations must align with these principles. Amendments to this constitution require explicit documentation of the change, its rationale, and approval from project stakeholders. All pull requests and code reviews must verify compliance with these principles before merging, ensuring Basic, Intermediate, and Advanced features are properly integrated and tested. All Advanced additions must go through full Spec-Kit Plus flow. Prioritize safety: no infinite loops from recurrence, no crashes on bad dates. Background features (e.g., periodic checks) must be optional and simple. Final demo must show recurring task in action and reminder alerts.

**Version**: 2.0.0 | **Ratified**: 2025-12-24 | **Last Amended**: 2025-12-28