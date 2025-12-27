---
id: 2
title: "Create Plan for Enhanced TODO App"
stage: plan
date_iso: 2025-12-27
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-app-enhanced
branch: 1-todo-app-enhanced
user: user
command: sp.plan
labels: ["plan", "todo-app", "features", "intermediate-level"]
links:
  spec: specs/1-todo-app-enhanced/spec.md
  plan: specs/1-todo-app-enhanced/plan.md
  ticket: null
  adr: null
  pr: null
files_yaml:
  - "specs/1-todo-app-enhanced/plan.md"
  - "specs/1-todo-app-enhanced/research.md"
  - "specs/1-todo-app-enhanced/data-model.md"
  - "specs/1-todo-app-enhanced/contracts/todo-contracts.md"
  - "specs/1-todo-app-enhanced/quickstart.md"
tests_yaml: []
---

## Prompt Text

Create a complete, updated technical plan for implementing the full Phase 1 Hackathon TODO application, which now includes both Basic Level (already partially or fully implemented) and Intermediate Level features (priorities/tags, search & filter, sort).

The plan must guide incremental, AI-assisted implementation to extend the existing codebase cleanly while producing a polished, modular, testable, and demonstrable console application.

Output the full updated plan as a Markdown file suitable for the plans folder (e.g., plans/002-full-basic-plus-intermediate/plan.md).

Structure the plan clearly with the following sections:

### Architecture Sketch
Provide a high-level overview of the final application structure:
- Clear separation of concerns: data model, core business logic, and CLI presentation
- In-memory storage using a list of task dictionaries or dataclasses with extended fields (priority, tags)
- Pure functions in task_manager for easy testing
- CLI handles all input/output and delegates to task_manager
- Persistent sort order stored in the manager instance

Include a simple ASCII or Mermaid diagram showing module relationships:
main.py → cli.py → task_manager.py
↕
models.py (Task definition)
text### Section Structure (Proposed Final Project Layout)
Detail the exact file and folder structure:
src/
├── init.py
├── main.py              # Entry point: creates TaskManager instance and runs interactive loop
├── cli.py               # Menu display, input handling, prompts, formatted output
├── task_manager.py      # Core logic: storage, add/update/delete/mark, search/filter/sort
└── models.py            # Task dataclass or TypedDict with all fields (id, title, description, complete, priority, tags)
tests/
├── init.py
├── test_task_manager.py # Comprehensive unit tests for all logic
└── test_cli.py          # Optional light integration tests
text### Implementation Approach
- Strictly incremental: Extend existing Basic implementation without breaking it
- Prioritize test-driven additions where possible
- Use dataclasses for Task model (cleaner than dicts for new fields)
- Keep task_manager methods pure or with minimal side effects for testability
- Use standard library only (datetime not needed since no due date in final spec)
- Implement sort as a persistent setting; search/filter as on-demand views

### Key Decisions and Tradeoffs
List and justify important choices:
1. Task representation: Dictionary vs. dataclass
   - Evaluate options and select dataclass for type safety and readability with new fields
2. Tags storage: List[str] vs. comma-separated string
   - Choose list for easier manipulation and filtering
3. Sort persistence: Global variable vs. attribute on TaskManager
   - Choose instance attribute for clean encapsulation
4. Search & Filter implementation: Single combined method vs. separate functions
   - Choose modular helper functions (filter_by_status, filter_by_priority, etc.) for reusability
5. Menu structure: Flat numbered options vs. sub-menus
   - Keep flat (8 options) for simplicity and speed in Hackathon context

### Testing Strategy
- Use built-in unittest module
- Extend existing tests to cover all new functionality and interactions
- Key test areas:
  - Task creation with priority and multiple tags
  - Accurate search (case-insensitive keyword in title/description)
  - Correct filtering by status, priority, and tag presence
  - All sort orders (creation, priority descending, title ascending)
  - Combinations (filter + sort)
  - Edge cases: empty list, no matches, empty tags, invalid inputs
- Aim for near-100% coverage of task_manager logic
- Manual acceptance testing: Full interactive demo of all menu options

### Implementation Phases
Organize work into clear, sequential phases:
1. Model & Foundation Update
   - Introduce Task dataclass in models.py with all fields
   - Update task_manager.py to use Task objects instead of dicts
   - Migrate existing add/list functions
2. Intermediate Feature Logic
   - Implement priority and tags handling in add/update
   - Add search, filter, and sort methods with helpers
   - Add persistent sort setting
   - Write and pass comprehensive unit tests progressively
3. CLI Enhancements
   - Expand menu to 8 options
   - Add new prompts for priority/tags input
   - Implement Search & Filter and Sort commands
   - Update display formatting to include priority and tags
4. Integration & Polish
   - Connect everything in main.py
   - Ensure smooth flow, clear messages, input validation
   - Add helpful hints (e.g., current sort order displayed in view)
5. Final Validation
   - Run full interactive session verifying all Basic + Intermediate features
   - Confirm adherence to constitution (clean code, type hints, docstrings)
   - Verify all acceptance criteria met
   - Update README.md with complete feature list and demo instructions

## Response Text

I have successfully created a complete technical implementation plan for the enhanced TODO application that includes both Basic and Intermediate Level features. The plan includes:

- Technical Context section with analysis of current implementation state
- Architecture Sketch showing the module relationships
- Section Structure detailing the final project layout
- Implementation Approach with incremental methodology
- Constitution Check verifying alignment with project principles
- Key Decisions and Tradeoffs section with justifications
- Testing Strategy covering all new functionality
- Implementation Phases organized sequentially

I also created the supporting documents:
- Research.md: Resolved clarifications about current implementation state
- Data-model.md: Detailed entity definitions and relationships
- Contracts/todo-contracts.md: Method signatures and API contracts
- Quickstart.md: Development setup and architecture overview

The plan follows the existing codebase structure and extends it to add Intermediate features (priorities/tags, search & filter, sort) while maintaining backward compatibility with existing Basic features. The architecture maintains clear separation of concerns with data models, business logic, and CLI presentation layers.

## Outcome

The implementation plan is complete and ready for the next phase of development. All required supporting documents have been created to guide the implementation of the enhanced TODO application with both Basic and Intermediate features.

## Evaluation

The plan successfully meets all requirements specified in the prompt:
- ✅ Architecture sketch with clear separation of concerns
- ✅ Detailed project layout structure
- ✅ Implementation approach with incremental methodology
- ✅ Key decisions with justifications
- ✅ Comprehensive testing strategy
- ✅ Sequential implementation phases
- ✅ All supporting documents created (research, data model, contracts, quickstart)
- ✅ Alignment with constitution principles verified