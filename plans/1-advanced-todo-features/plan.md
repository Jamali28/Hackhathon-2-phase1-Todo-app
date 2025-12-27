# Advanced TODO Features: Implementation Plan

## Technical Context

**Feature**: Advanced TODO Features: Recurring Tasks and Due Date Reminders
**Spec File**: specs/1-advanced-todo-features/spec.md
**Current Codebase Status**: Basic + Intermediate features fully implemented and tested
**Target Architecture**: Console-based in-memory TODO application
**Technology Stack**: Python 3.13+, standard library only (datetime, threading)
**Development Approach**: Strictly incremental - extend existing code safely

### Current System Architecture
- **models.py**: Task @dataclass with id, title, description, completed, priority, tags
- **task_manager.py**: Core business logic for task operations
- **cli.py**: Command-line interface and user interaction
- **main.py**: Entry point and application loop
- **tests/**: Unit tests for all functionality

### Unknowns Requiring Clarification
- NEEDS CLARIFICATION: Specific datetime format requirements for user input
- NEEDS CLARIFICATION: Exact behavior for month-end recurrence edge cases
- NEEDS CLARIFICATION: Background thread implementation details and shutdown behavior

## Constitution Check

Based on .specify/memory/constitution.md, this implementation must:
- ✅ Follow incremental extension principle - build safely on existing codebase
- ✅ Use standard library only (datetime, threading) - no external dependencies
- ✅ Maintain performance efficiency - sub-second response times
- ✅ Implement clean code practices - type hints, docstrings, PEP 8
- ✅ Include comprehensive error handling and user-friendly messages
- ✅ Follow test-driven development with 80%+ coverage
- ✅ Maintain backward compatibility with Basic/Intermediate features

## Gates & Compliance

### Gate 1: Architecture Compatibility
- [X] Solution extends existing architecture without breaking changes
- [X] Uses only approved technology stack (standard library)
- [X] Maintains performance requirements

### Gate 2: Constitution Compliance
- [X] Follows incremental extension principle
- [X] Maintains backward compatibility
- [X] Uses only standard library components
- [X] Includes error handling and validation

### Gate 3: Requirements Coverage
- [X] All functional requirements from spec are addressable
- [X] Non-functional requirements are achievable
- [X] Success criteria are measurable

## Phase 0: Research & Analysis

### Research Tasks

#### Task 0.1: Date Format Standards
**Research**: Determine optimal date/time input formats for user experience
**Decision**: Use YYYY-MM-DD for dates and HH:MM for times (ISO 8601 inspired)
**Rationale**: These formats are unambiguous, widely understood, and easily parsed
**Alternatives**: MM/DD/YYYY, DD/MM/YYYY (ambiguous), natural language (complex parsing)

#### Task 0.2: Month-End Recurrence Handling
**Research**: Best practices for handling month-end recurrence edge cases
**Decision**: When recurring monthly from day 31, advance to month's last day
**Rationale**: Most user-friendly approach that prevents invalid dates
**Example**: January 31 → February 28/29 → March 31 → April 30 → May 31, etc.

#### Task 0.3: Background Thread Implementation
**Research**: Safe implementation of background reminder thread
**Decision**: Use daemon thread with periodic check and proper cleanup
**Rationale**: Non-blocking, automatic cleanup on main program exit
**Implementation**: threading.Thread(daemon=True) with sleep loop

## Phase 1: Data Model & API Design

### Data Model: Extended Task Entity

```python
@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"  # 'high', 'medium', 'low'
    tags: List[str] = None   # Default to empty list in __post_init__
    due_datetime: Optional[datetime] = None  # Combined date and time
    recurrence: str = "none"  # 'none', 'daily', 'weekly', 'monthly'
    recurrence_parent_id: Optional[int] = None  # Links to original recurring template
```

### Validation Rules
- `due_datetime`: Must be a valid datetime or None
- `recurrence`: Must be one of ['none', 'daily', 'weekly', 'monthly']
- `recurrence_parent_id`: Must be a valid task ID or None

### API Contracts

#### TaskManager Methods
- `add_task(title, description="", priority="medium", tags=None, due_datetime=None, recurrence="none") -> int`
- `update_task(task_id, title=None, description=None, priority=None, tags=None, due_datetime=None, recurrence=None) -> bool`
- `get_overdue_tasks() -> List[Task]`
- `get_due_today_tasks() -> List[Task]`
- `get_due_soon_tasks(hours=24) -> List[Task]`
- `calculate_next_occurrence(task: Task) -> Optional[datetime]`
- `create_next_recurrence(task: Task) -> Optional[int]`
- `get_recurring_tasks() -> List[Task]`

#### Date Utility Functions
- `parse_date_input(date_str: str) -> Optional[datetime]`
- `parse_time_input(time_str: str) -> Optional[time]`
- `is_overdue(task: Task) -> bool`
- `is_due_today(task: Task) -> bool`
- `format_datetime_display(dt: datetime) -> str`

## Phase 2: Implementation Strategy

### Implementation Approach
- **Strictly incremental**: Extend existing code without breaking functionality
- **Test-driven**: Write tests before implementation
- **Pure functions**: For date calculations and recurrence logic (testable)
- **Standard library only**: datetime for date handling, threading for background tasks
- **Graceful handling**: Invalid dates → reprompt, month-end adjustments → last day of month

### Key Implementation Decisions

#### 1. Due Date Storage
- **Choice**: datetime.datetime (None if no due)
- **Rationale**: Simplifies sorting and comparison operations
- **Alternative**: Separate date/time fields (more complex)

#### 2. Recurrence Implementation
- **Choice**: Simple string ('daily'/'weekly'/'monthly') with custom calculation
- **Rationale**: Lightweight, no external dependencies, sufficient for requirements
- **Alternative**: Complex rrule library (overkill for simple patterns)

#### 3. Next Occurrence Calculation
- **Choice**: Manual (datetime + timedelta + manual month handling)
- **Rationale**: No external dependencies, full control over edge cases
- **Alternative**: dateutil.rrule (requires external dependency)

#### 4. Background Reminders
- **Choice**: Implement simple optional thread
- **Rationale**: Impressive for demo, keeps functionality while maintaining non-blocking behavior
- **Alternative**: Startup-only reminders (less impressive)

#### 5. Overdue Highlighting
- **Choice**: Text markers (e.g., **[OVERDUE]**)
- **Rationale**: Works everywhere, no terminal compatibility issues
- **Alternative**: ANSI colors (may not work in all terminals)

## Phase 3: Testing Strategy

### Testing Approach
- Extend existing unittest suite in tests/test_task_manager.py
- Test-driven development for all new functionality
- Focus on edge cases and date calculations

### Critical New Tests

#### Recurrence Tests
- Daily recurrence: +1 day calculation accuracy
- Weekly recurrence: +7 days calculation accuracy
- Monthly recurrence: Same day preservation, month-end handling (31→28/30, Feb leap)
- Invalid recurrence patterns: Proper validation

#### Task Completion Tests
- Marking recurring task complete creates correct next instance
- Original task marked as complete
- Next instance has correct recurrence rule and due date
- Non-recurring tasks behave normally

#### Reminder Detection Tests
- Overdue task detection accuracy
- Due today detection (within 24 hours of midnight)
- Due soon detection (within specified hours)
- Startup reminder banner accuracy

#### Background Thread Tests
- Thread starts and stops cleanly
- Alerts trigger correctly without blocking main program
- Thread cleanup on program exit

#### Input Validation Tests
- Invalid date input handling (reprompt behavior)
- Invalid time input handling
- Invalid recurrence pattern handling

#### Compatibility Tests
- All existing Basic + Intermediate tests still pass
- No regression in performance
- Backward compatibility maintained

## Phase 4: Implementation Phases

### Phase 4.1: Model Extension
- [ ] Add due_datetime: Optional[datetime.datetime] and recurrence: str to Task dataclass
- [ ] Add recurrence_parent_id: Optional[int] field
- [ ] Update __post_init__ to handle new field defaults
- [ ] Write initial tests for new fields
- [ ] Update type hints throughout codebase

### Phase 4.2: Due Date Logic
- [ ] Update Add/Update in CLI to prompt/parse due date/time
- [ ] Add date/time parsing utilities with error handling
- [ ] Add overdue/today detection helpers in task_manager
- [ ] Implement startup reminder banner in main.py
- [ ] Write tests for date parsing and validation

### Phase 4.3: Recurring Task Logic
- [ ] Implement next_occurrence calculation (pure function)
- [ ] Update Mark Complete to handle recurrence: create next task if needed
- [ ] Handle month-end edge cases correctly
- [ ] Test all recurrence frequencies thoroughly
- [ ] Write comprehensive recurrence tests

### Phase 4.4: Display Enhancements
- [ ] Update View to show due date, overdue marker, recurrence symbol
- [ ] Update Search/Filter to support due-based options
- [ ] Update Sort to support due date sorting
- [ ] Ensure display formatting remains readable
- [ ] Test display with various data combinations

### Phase 4.5: Optional Background Reminders
- [ ] Add simple daemon thread that checks every 60s and prints alerts
- [ ] Implement thread cleanup on exit
- [ ] Ensure non-blocking behavior
- [ ] Test thread safety and shutdown
- [ ] Add configuration option to disable if needed

### Phase 4.6: Polish & Validation
- [ ] Full interactive testing: demo recurring task completion and reminders
- [ ] Confirm no regressions in Basic/Intermediate features
- [ ] Performance testing with various task counts
- [ ] Update documentation with Advanced feature instructions
- [ ] Final integration testing

## Phase 5: Deployment & Validation

### Pre-Deployment Checklist
- [ ] All new functionality tested and working
- [ ] All existing tests pass (no regressions)
- [ ] Performance meets requirements
- [ ] Error handling comprehensive
- [ ] User experience validated
- [ ] Documentation updated

### Validation Steps
1. Interactive testing of all Advanced features
2. Stress testing with multiple recurring tasks
3. Edge case testing (month-end, invalid inputs)
4. Performance testing with 1000+ tasks
5. Regression testing for Basic/Intermediate features