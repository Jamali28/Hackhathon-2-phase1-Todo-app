---
id: 2
title: "Update Constitution with Advanced Features"
stage: constitution
date_iso: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app-enhanced
branch: master
user: user
command: sp.constitution
labels: ["constitution", "todo", "advanced-features", "recurring-tasks", "due-dates"]
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

Create an updated project constitution for the Hackathon TODO application, now extended to include Advanced Level intelligent features on top of the complete Basic + Intermediate implementation.

The application is a command-line Python console-based in-memory TODO tool with:
- Basic: Add, Delete, Update, View, Mark Complete
- Intermediate: Priorities, Tags, Search/Filter, Sort
- Advanced: Recurring tasks (daily/weekly/monthly auto-reschedule), Due dates with console-based reminders and overdue indicators

All data remains in memory only. The current codebase (Basic + Intermediate) is fully working, tested, and clean.

Output the updated constitution as a complete Markdown file (versioned or overwriting .specify/memory/constitution.md).

Update all relevant sections to support the new scope while reinforcing existing principles.

Key updates and guidelines:

### Project Overview
Describe the final app as a smart, console-based TODO with recurring tasks and due date reminders — an impressive, polished Hackathon MVP.

### Core Principles
- Simplicity First: Advanced features must remain easy to understand and demo. Avoid over-complexity (e.g., no full cron, no external notification libs).
- Incremental Extension: All new code must build safely on the existing working codebase without breaking or rewriting Basic/Intermediate features.
- Spec-Driven Development: Mandatory for all additions.

### Technical Stack
- Python 3.13+
- UV for management
- Standard library only: heavily use datetime; optional threading.Thread for simple background reminders
- No external dependencies

### Code Quality Standards
- Prefer @dataclass for Task with proper defaults
- Immutable-style where possible; careful mutation for recurrence
- Pure functions for date calculations and recurrence logic
- Comprehensive input validation for dates (user-friendly error messages)
- No timezone handling — use local naive datetime

### Testing Requirements
- Extend existing unittest suite
- Add rigorous tests for:
  - Recurrence rules (daily/weekly/monthly, including month-end edge cases)
  - Next occurrence date calculation
  - Overdue/today/upcoming detection
  - Reminder logic on startup
  - Background reminder thread (if implemented) safety
- Test that marking recurring task complete creates correct next instance

### User Experience Guidelines
- Clear feedback on recurrence scheduling and due reminders
- Non-intrusive reminders (console print banners, not beeps/popups)
- Graceful handling of invalid dates

### Development Governance
- All Advanced additions must go through full Spec-Kit Plus flow
- Prioritize safety: no infinite loops from recurrence, no crashes on bad dates
- Background features (e.g., periodic checks) must be optional and simple
- Final demo must show recurring task in action and reminder alerts

## Response Text

Successfully updated the project constitution to include Advanced Level features (recurring tasks and due date reminders) while maintaining all existing Basic and Intermediate features. The constitution version was updated from 1.1.0 to 2.0.0 to reflect the addition of significant new functionality. Key updates include:

- Enhanced Project Overview to describe the smart, console-based TODO with recurring tasks and due date reminders
- Added Incremental Extension principle to ensure new features build safely on existing codebase
- Updated Technical Stack to include datetime and threading guidance
- Enhanced Code Quality Standards to include requirements for date calculations and recurrence logic
- Expanded Testing Requirements to include rigorous tests for recurrence rules, due date detection, and reminder logic
- Updated User Experience Guidelines to include feedback on recurrence scheduling and reminders
- Enhanced Governance section with safety requirements for recurrence and background features

## Outcome

✅ Impact: Successfully updated constitution to include Advanced Level features (recurring tasks, due dates) while maintaining all existing principles
🧪 Tests: Constitution updated with comprehensive testing requirements for new features
📁 Files: Updated .specify/memory/constitution.md with version 2.0.0
🔁 Next prompts: Create specification for Advanced features (recurring tasks and due dates)
🧠 Reflection: Constitution properly extended to support Advanced features while maintaining backward compatibility principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for constitution update
- Prompt variant (if applicable): Standard constitution update
- Next experiment (smallest change to try): Create specification for recurring tasks and due dates implementation