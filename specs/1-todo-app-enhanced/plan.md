# Implementation Plan: Full Phase 1 TODO Application with Basic and Intermediate Features

**Plan Version**: 1.0.0
**Created**: 2025-12-27
**Status**: Draft
**Feature**: Full Phase 1 TODO Application with Basic and Intermediate Features
**Branch**: 1-todo-app-enhanced

## Technical Context

- **Project Type**: Console-based, in-memory TODO application with CLI interface
- **Programming Language**: Python 3.13+
- **Dependencies**: Standard library only (no external packages)
- **Current State**: Basic TODO features (Add, Delete, Update, View, Mark Complete) partially implemented
- **Target State**: Full application with Intermediate features (Priorities/Tags, Search/Filter, Sort)
- **Architecture**: Modular design with separation of concerns (models, business logic, CLI)
- **Data Storage**: In-memory using dataclasses for task representation

**NEEDS CLARIFICATION**: What is the current state of the existing implementation? Do we have working Basic features or just the initial project structure?

**NEEDS CLARIFICATION**: Should the existing codebase be examined and extended, or should we implement from scratch based on the spec?

## Architecture Sketch

Provide a high-level overview of the final application structure:
- Clear separation of concerns: data model, core business logic, and CLI presentation
- In-memory storage using a list of task dictionaries or dataclasses with extended fields (priority, tags)
- Pure functions in task_manager for easy testing
- CLI handles all input/output and delegates to task_manager
- Persistent sort order stored in the manager instance

```
main.py → cli.py → task_manager.py
    ↕
models.py (Task definition)
```

## Section Structure (Proposed Final Project Layout)

Detail the exact file and folder structure:
```
src/
├── __init__.py
├── main.py              # Entry point: creates TaskManager instance and runs interactive loop
├── cli.py               # Menu display, input handling, prompts, formatted output
├── task_manager.py      # Core logic: storage, add/update/delete/mark, search/filter/sort
└── models.py            # Task dataclass or TypedDict with all fields (id, title, description, complete, priority, tags)
tests/
├── __init__.py
├── test_task_manager.py # Comprehensive unit tests for all logic
└── test_cli.py          # Optional light integration tests
```

## Implementation Approach

- Strictly incremental: Extend existing Basic implementation without breaking it
- Prioritize test-driven additions where possible
- Use dataclasses for Task model (cleaner than dicts for new fields)
- Keep task_manager methods pure or with minimal side effects for testability
- Use standard library only (datetime not needed since no due date in final spec)
- Implement sort as a persistent setting; search/filter as on-demand views

## Constitution Check

### Alignment with Core Principles
- **Simplicity First**: The modular architecture with clear separation of concerns ensures code remains simple and readable. We'll avoid over-engineering while implementing the Intermediate features.
- **Spec-Driven Development**: This plan follows directly from the specification, ensuring systematic development aligned with requirements.
- **Clean Code**: We'll use dataclasses with type hints, follow PEP 8, keep functions short with single responsibility, and include comprehensive docstrings.
- **Performance Efficiency**: In-memory storage with efficient data structures will ensure sub-second response times even with 1000+ tasks.
- **Error Handling and User Experience**: Comprehensive input validation with user-friendly error messages will ensure the application never crashes.
- **Test-Driven Development**: We'll aim for 80%+ test coverage of business logic with comprehensive edge case testing.

### Gate Evaluation
- ✅ Architecture supports clean separation of concerns (models, logic, presentation)
- ✅ Performance requirements can be met with in-memory data structures
- ✅ Error handling strategy aligns with constitution requirements
- ✅ Modular design enables comprehensive testing
- ✅ Type hints and docstrings will be implemented throughout

## Key Decisions and Tradeoffs

List and justify important choices:
1. **Task representation: Dictionary vs. dataclass**
   - Decision: Use dataclass for type safety and readability with new fields
   - Rationale: Dataclasses provide better type hints, are more readable, and easier to maintain than dictionaries when working with multiple attributes
   - Alternative: Dictionaries would be simpler but less type-safe

2. **Tags storage: List[str] vs. comma-separated string**
   - Decision: Use List[str] for easier manipulation and filtering
   - Rationale: Easier to search for specific tags, add/remove tags, and validate tag formats
   - Alternative: Comma-separated string would require parsing for operations

3. **Sort persistence: Global variable vs. attribute on TaskManager**
   - Decision: Use instance attribute for clean encapsulation
   - Rationale: Maintains state within the appropriate object, making it easier to manage and test
   - Alternative: Global variable would make testing harder and violate encapsulation

4. **Search & Filter implementation: Single combined method vs. separate functions**
   - Decision: Use modular helper functions (filter_by_status, filter_by_priority, etc.) for reusability
   - Rationale: Enables combination of filters and easier testing of individual components
   - Alternative: Single combined method would be less flexible

5. **Menu structure: Flat numbered options vs. sub-menus**
   - Decision: Keep flat (8 options) for simplicity and speed in Hackathon context
   - Rationale: Simple interface is easier to navigate and fits the MVP approach
   - Alternative: Sub-menus would add complexity without significant benefit

## Testing Strategy

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

## Implementation Phases

Organize work into clear, sequential phases:

### Phase 0: Research and Setup
- Examine existing codebase to understand current implementation state
- Resolve all "NEEDS CLARIFICATION" items
- Set up testing framework and development environment

### Phase 1: Model & Foundation Update
- Introduce Task dataclass in models.py with all fields (id, title, description, complete, priority, tags, creation_timestamp)
- Update task_manager.py to use Task objects instead of dicts (if applicable)
- Migrate existing add/list functions to work with new data model
- Write initial unit tests for the basic data model

### Phase 2: Intermediate Feature Logic
- Implement priority and tags handling in add/update methods
- Add search, filter, and sort methods with helper functions
- Add persistent sort setting to TaskManager class
- Write and pass comprehensive unit tests progressively for all new functionality

### Phase 3: CLI Enhancements
- Expand menu to 8 options as specified in the feature requirements
- Add new prompts for priority/tags input during task creation
- Implement Search & Filter and Sort command handlers
- Update display formatting to include priority and tags in task listings

### Phase 4: Integration & Polish
- Connect all components in main.py
- Ensure smooth flow between all modules with clear messages and input validation
- Add helpful indicators like current sort order displayed in view
- Implement error handling and graceful recovery from invalid inputs

### Phase 5: Final Validation
- Run full interactive session verifying all Basic + Intermediate features work correctly
- Confirm adherence to constitution (clean code, type hints, docstrings)
- Verify all acceptance criteria from the specification are met
- Update README.md with complete feature list and demo instructions

## Dependencies and Risks

### Dependencies
- Python 3.13+ standard library only
- No external dependencies required

### Risks
1. **Integration Risk**: New Intermediate features might break existing Basic functionality
   - Mitigation: Use test-driven development and ensure all existing tests continue to pass
2. **Performance Risk**: Search and sort operations might become slow with large datasets
   - Mitigation: Implement efficient algorithms and test with up to 1000 tasks
3. **Complexity Risk**: Adding new features might make the codebase overly complex
   - Mitigation: Follow clean code principles and maintain separation of concerns

## Success Criteria Verification

Each phase will verify these success criteria from the specification:
- Users can add, delete, update, view, search, filter, and sort tasks with sub-second response times
- All new fields (priority, tags) are correctly stored and displayed
- Search & Filter returns accurate subsets
- Sort applies correctly and persists across views
- Edge cases handled: empty list, no search matches, invalid inputs, canceling operations
- Code fully adheres to the project constitution