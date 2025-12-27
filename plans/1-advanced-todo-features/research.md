# Research Document: Advanced TODO Features

## Decision: Date Format Standards

**Rationale**: For the best user experience and unambiguous parsing, the system will use standardized formats:
- **Date format**: YYYY-MM-DD (ISO 8601 inspired) - e.g., 2025-12-31
- **Time format**: HH:MM 24-hour format - e.g., 14:30
- **Combined format**: YYYY-MM-DD HH:MM - e.g., 2025-12-31 14:30

**Justification**: These formats are unambiguous (no confusion between MM/DD vs DD/MM), widely understood, and easily parsed using Python's datetime.strptime(). The ISO 8601 format is internationally recognized and prevents confusion across different regions.

## Decision: Month-End Recurrence Handling

**Rationale**: When recurring monthly from a day that doesn't exist in the target month, the system will advance to the last day of that month.

**Examples**:
- January 31 → February 28 (or 29 in leap years) → March 31 → April 30 → May 31 → June 30, etc.
- January 29 → February 28 (or 29 in leap years) → March 29 → April 29, etc.

**Implementation**: Use calendar module to determine the number of days in each month, and if the target day exceeds the available days, use the last day of the month instead.

## Decision: Background Thread Implementation

**Rationale**: A background thread for periodic reminder checking provides real-time notifications during application usage while maintaining non-blocking behavior.

**Implementation Details**:
- Use `threading.Thread(daemon=True)` to ensure thread doesn't prevent program exit
- Thread will check every 60 seconds for tasks that have become due/overdue
- Thread will print alerts to console when conditions are met
- Proper cleanup with thread.join() or rely on daemon behavior for automatic cleanup
- Configuration option to disable if needed for performance

## Decision: Date Calculation Strategy

**Rationale**: For accurate and reliable date calculations without external dependencies, use Python's built-in datetime and timedelta for most operations, with manual month handling for complex cases.

**Implementation**:
- Daily recurrence: `current_date + timedelta(days=1)`
- Weekly recurrence: `current_date + timedelta(days=7)`
- Monthly recurrence: Manual calculation using `calendar.monthrange()` to handle month-end cases
- Use `datetime.replace()` with exception handling for month-end cases

## Decision: Error Handling Strategy

**Rationale**: Provide clear, helpful error messages for invalid inputs while maintaining application stability.

**Implementation**:
- For invalid date/time input: Show clear error message and reprompt
- For invalid recurrence patterns: Validate immediately and show options
- For month-end calculations: Handle automatically without user intervention
- For background thread errors: Log quietly without disrupting main functionality