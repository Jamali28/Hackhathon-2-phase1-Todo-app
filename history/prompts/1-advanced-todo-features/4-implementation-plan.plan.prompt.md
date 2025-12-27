---
id: 4
title: "Implementation Plan"
stage: plan
date_iso: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: advanced-todo-features
branch: 1-advanced-todo-features
user: user
command: sp.plan
labels: ["plan", "todo", "advanced-features", "architecture", "implementation"]
links:
  spec: specs/1-advanced-todo-features/spec.md
  plan: plans/1-advanced-todo-features/plan.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "plans/1-advanced-todo-features/plan.md"
  - "plans/1-advanced-todo-features/research.md"
  - "plans/1-advanced-todo-features/data-model.md"
  - "plans/1-advanced-todo-features/quickstart.md"
tests_yaml: []
---

## Prompt Text

Create a complete, updated technical plan for implementing the Advanced Level features on top of the current fully working codebase that already implements Basic + Intermediate Levels.

Important context:
- The current /src codebase is complete, tested, and working for Basic + Intermediate.
- Task model uses @dataclass with fields: id, title, description, complete, priority, tags (and possibly others).
- Core logic is in task_manager.py, CLI in cli.py, entry point in main.py.
- Unit tests exist and pass.
- All implementation MUST be strictly incremental — extend and modify existing code safely without breaking or rewriting existing functionality.

Now add Advanced Level features: Recurring tasks (daily/weekly/monthly) and Due dates with console reminders.

Output the full updated plan as a Markdown file (e.g., plans/003-advanced-level/plan.md).

Structure the plan clearly with the following sections:

### Architecture Sketch
Provide an updated high-level overview:
- Extend the existing Task dataclass with due_datetime and recurrence fields
- Add recurrence logic and reminder logic primarily in task_manager.py
- Optional simple background thread in main.py or task_manager.py for periodic checks
- Keep CLI responsible only for input/output and displaying reminders

Include a simple ASCII diagram showing updated relationships:
main.py → cli.py → task_manager.py
↕
models.py (extended Task dataclass)
↕
optional: threading (background reminders)
text### Section Structure (Updated Project Layout)
Confirm and detail any minor additions:
src/
├── init.py
├── main.py              # Updated: startup reminders + optional background thread
├── cli.py               # Updated: new prompts, enhanced display with due/overdue/recurrence
├── task_manager.py      # Heavily updated: recurrence generation, reminder helpers, date calculations
└── models.py            # Updated: Task dataclass with due_datetime and recurrence fields
tests/
├── test_task_manager.py # Extended with new advanced tests
└── others if present
text### Implementation Approach
- Strictly incremental and test-driven
- Use standard library datetime (naive local times only)
- Recurrence logic: pure functions where possible for testability
- Background reminders: optional, simple threading.Thread with sleep loop (daemon thread)
- Graceful handling: invalid dates → reprompt, month-end adjustments

### Key Decisions and Tradeoffs
List and justify:
1. Due date storage: datetime.datetime vs. separate date/time fields
   - Choose datetime.datetime (None if no due) for simplicity and sorting
2. Recurrence implementation: Store rule string vs. more complex rrule
   - Simple string ('daily'/'weekly'/'monthly') with custom calculation — sufficient and lightweight
3. Next occurrence calculation: Manual date math vs. dateutil.rrule
   - Manual (datetime + timedelta + manual month handling) — no external deps
4. Background reminders: Implement vs. startup-only
   - Implement simple optional thread — impressive for demo but keep non-blocking
5. Overdue highlighting: ANSI colors vs. text markers
   - Text markers (e.g., **[OVERDUE]**) — works everywhere

### Testing Strategy
- Extend existing unittest suite
- Critical new tests:
  - Recurrence: daily (+1 day), weekly (+7), monthly (same day, handle 31→28/30, Feb leap)
  - Marking recurring task complete creates correct next instance and keeps original complete
  - Reminder detection: overdue, due today, due soon
  - Startup reminder banner accuracy
  - Background thread alerts (if implemented) without blocking
  - Invalid date input handling
- Ensure all existing Basic + Intermediate tests still pass

### Implementation Phases
Clear sequential phases:
1. Model Extension
   - Add due_datetime: Optional[datetime.datetime] and recurrence: str to Task dataclass
   - Update existing code to handle new fields with defaults
   - Write initial tests for new fields
2. Due Date Logic
   - Update Add/Update in CLI to prompt/parse due date/time
   - Add overdue/today detection helpers in task_manager
   - Implement startup reminder banner in main.py
3. Recurring Task Logic
   - Implement next_occurrence calculation (pure function)
   - Update Mark Complete to handle recurrence: create next task if needed
   - Test all recurrence frequencies thoroughly
4. Display Enhancements
   - Update View to show due date, overdue marker, recurrence symbol
   - Update Search/Filter and Sort to support due-based options
5. Optional Background Reminders
   - Add simple daemon thread that checks every 60s and prints alerts
   - Ensure clean shutdown
6. Polish & Validation
   - Full interactive testing: demo recurring task completion and reminders
   - Confirm no regressions in Basic/Intermediate features
   - Update README.md with Advanced feature demo instructions

## Response Text

Successfully created a comprehensive technical implementation plan for the Advanced TODO features. The plan includes:

- Detailed technical context with current architecture and unknowns requiring clarification
- Constitution check ensuring compliance with project principles
- Gates and compliance verification
- Research document addressing date formats, month-end recurrence handling, and background thread implementation
- Complete data model specification for the extended Task entity
- Quickstart guide for implementation reference
- Detailed implementation phases with specific tasks
- Comprehensive testing strategy
- Key implementation decisions and tradeoffs

The plan follows the required structure and ensures strict incremental extension of the existing codebase without breaking functionality. All Advanced features (recurring tasks and due date reminders) are properly addressed with clear implementation steps.

## Outcome

✅ Impact: Successfully created comprehensive implementation plan for Advanced Level features (recurring tasks, due dates) that extends existing functionality safely
🧪 Tests: Plan includes detailed testing strategy for all new functionality
📁 Files: Created plans/1-advanced-todo-features/plan.md, research.md, data-model.md, quickstart.md
🔁 Next prompts: Create implementation tasks based on this plan
🧠 Reflection: Plan properly structured with all required sections and maintains compatibility with existing features

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A for plan creation
- Prompt variant (if applicable): Standard plan creation
- Next experiment (smallest change to try): Create implementation tasks based on this plan