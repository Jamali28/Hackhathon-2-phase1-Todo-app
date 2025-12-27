"""
CLI interface for the TODO application.

This module handles all user input/output, menu display, prompts, and formatting.
"""
from typing import Optional
try:
    # When running as a module (python -m src.main)
    from .task_manager import TaskManager
except ImportError:
    # When running directly (python src/main.py)
    from task_manager import TaskManager


class CLI:
    """
    Command-line interface for the TODO application.

    Provides methods for displaying menus, getting user input, and formatting output.
    """

    def __init__(self, task_manager: TaskManager):
        """
        Initialize the CLI with a task manager instance.

        Args:
            task_manager: An instance of TaskManager to handle task operations
        """
        self.task_manager = task_manager

    def display_menu(self):
        """Display the main menu with available options."""
        print("\n" + "="*40)
        print("TODO Application")
        print("="*40)
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as complete/incomplete")
        print("6. Search & Filter tasks")
        print("7. Sort tasks")
        print("8. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's menu choice (1-8)
        """
        while True:
            try:
                choice = input("Enter your choice (1-8): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")
            except KeyboardInterrupt:
                print("\nExiting...")
                return '8'
            except EOFError:
                print("\nExiting...")
                return '8'

    def search_and_filter_tasks(self):
        """Handle searching and filtering tasks."""
        print("\n--- Search & Filter Tasks ---")

        # Get search keyword
        keyword = input("Enter search keyword (press Enter to skip search): ").strip()

        # Get status filter
        print("Filter by status:")
        print("1. All tasks")
        print("2. Complete tasks only")
        print("3. Incomplete tasks only")
        status_choice = input("Enter choice (1-3, press Enter for all): ").strip()

        status_filter = None
        if status_choice == '2':
            status_filter = True
        elif status_choice == '3':
            status_filter = False

        # Get priority filter
        print("Filter by priority:")
        print("1. All priorities")
        print("2. High priority")
        print("3. Medium priority")
        print("4. Low priority")
        priority_choice = input("Enter choice (1-4, press Enter for all): ").strip()

        priority_filter = None
        if priority_choice == '2':
            priority_filter = 'high'
        elif priority_choice == '3':
            priority_filter = 'medium'
        elif priority_choice == '4':
            priority_filter = 'low'

        # Get tag filter
        tag_filter = input("Enter specific tag to filter by (press Enter to skip): ").strip()
        if not tag_filter:
            tag_filter = None

        # Get overdue filter
        print("Filter by overdue status:")
        print("1. All tasks")
        print("2. Overdue tasks only")
        print("3. Not overdue tasks only")
        overdue_choice = input("Enter choice (1-3, press Enter for all): ").strip()

        is_overdue_filter = None
        if overdue_choice == '2':
            is_overdue_filter = True
        elif overdue_choice == '3':
            is_overdue_filter = False

        # Get due today filter
        print("Filter by due today status:")
        print("1. All tasks")
        print("2. Due today only")
        print("3. Not due today only")
        due_today_choice = input("Enter choice (1-3, press Enter for all): ").strip()

        is_due_today_filter = None
        if due_today_choice == '2':
            is_due_today_filter = True
        elif due_today_choice == '3':
            is_due_today_filter = False

        # Get recurring filter
        print("Filter by recurring status:")
        print("1. All tasks")
        print("2. Recurring tasks only")
        print("3. Non-recurring tasks only")
        recurring_choice = input("Enter choice (1-3, press Enter for all): ").strip()

        is_recurring_filter = None
        if recurring_choice == '2':
            is_recurring_filter = True
        elif recurring_choice == '3':
            is_recurring_filter = False

        # Perform search
        if keyword:
            tasks = self.task_manager.search_tasks(keyword)
        else:
            tasks = self.task_manager.list_tasks()

        # Apply all filters
        filtered_tasks = []
        for task in tasks:
            # Check status filter
            if status_filter is not None and task.completed != status_filter:
                continue
            # Check priority filter
            if priority_filter is not None and task.priority != priority_filter:
                continue
            # Check tag filter
            if tag_filter is not None and tag_filter not in task.tags:
                continue
            # Check overdue filter
            if is_overdue_filter is not None and is_overdue_filter != self.task_manager.is_overdue(task):
                continue
            # Check due today filter
            if is_due_today_filter is not None and is_due_today_filter != self.task_manager.is_due_today(task):
                continue
            # Check recurring filter
            if is_recurring_filter is not None and is_recurring_filter != (task.recurrence != "none"):
                continue
            filtered_tasks.append(task)
        tasks = filtered_tasks

        # Display results
        print(f"\n--- Search & Filter Results ({len(tasks)} of {len(self.task_manager.tasks)} tasks) ---")

        if not tasks:
            print("No matching tasks found.")
            return

        print(f"{'ID':<3} {'Status':<8} {'Priority':<8} {'Tags':<15} {'Due':<12} {'Rec':<4} {'Title':<20} {'Description'}")
        print("-" * 100)
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            if self.task_manager.is_overdue(task) and not task.completed:
                status += " **[OVERDUE]**"
            priority = task.priority.upper()[0]  # H, M, L
            tags_str = ", ".join(task.tags) if task.tags else "None"
            due_str = self.task_manager.format_datetime_display(task.due_datetime) if task.due_datetime else ""
            if self.task_manager.is_overdue(task) and not task.completed:
                due_str += " **[OVERDUE]**"
            recurrence_indicator = "🔁" if task.recurrence != "none" else ""
            title = task.title if len(task.title) <= 19 else task.title[:17] + ".."
            description = task.description if len(task.description) <= 25 else task.description[:23] + ".."
            print(f"{task.id:<3} {status:<8} {priority:<8} {tags_str:<15} {due_str:<12} {recurrence_indicator:<4} {title:<20} {description}")

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title (required): ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()

        # Get priority
        print("Enter priority (high/medium/low, press Enter for 'medium'):")
        priority_input = input().strip().lower()
        if not priority_input:
            priority_input = "medium"

        # Get tags
        tags_input = input("Enter tags (comma-separated, press Enter for none): ").strip()
        tags = []
        if tags_input:
            # Split tags and clean them
            tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

        # Get due date
        due_date_input = input("Enter due date (YYYY-MM-DD, press Enter to skip): ").strip()
        due_datetime = None
        if due_date_input:
            due_datetime = self.task_manager.parse_date_input(due_date_input)
            if due_datetime is None:
                print("Error: Invalid date format. Please use YYYY-MM-DD format.")
                return

            # Get due time if date was provided
            due_time_input = input("Enter due time (HH:MM, press Enter for 00:00): ").strip()
            if due_time_input:
                due_time = self.task_manager.parse_time_input(due_time_input)
                if due_time is None:
                    print("Error: Invalid time format. Please use HH:MM format.")
                    return
                # Combine date and time
                due_datetime = due_datetime.replace(hour=due_time.hour, minute=due_time.minute)

        # Get recurrence
        print("Enter recurrence pattern (none/daily/weekly/monthly, press Enter for 'none'):")
        recurrence_input = input().strip().lower()
        if not recurrence_input:
            recurrence_input = "none"

        if recurrence_input not in ["none", "daily", "weekly", "monthly"]:
            print("Error: Invalid recurrence pattern. Must be one of: none, daily, weekly, monthly.")
            return

        try:
            task_id = self.task_manager.add_task(title, description, priority_input, tags, due_datetime, recurrence_input)
            print(f"Task added successfully with ID: {task_id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks(self):
        """Handle viewing all tasks."""
        print("\n--- Task List ---")
        tasks = self.task_manager.list_tasks()

        if not tasks:
            print("No tasks yet.")
            return

        print(f"{'ID':<3} {'Status':<8} {'Priority':<8} {'Tags':<15} {'Due':<12} {'Rec':<4} {'Title':<20} {'Description'}")
        print("-" * 100)
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            if self.task_manager.is_overdue(task) and not task.completed:
                status += " **[OVERDUE]**"
            priority = task.priority.upper()[0]  # H, M, L
            tags_str = ", ".join(task.tags) if task.tags else "None"
            due_str = self.task_manager.format_datetime_display(task.due_datetime) if task.due_datetime else ""
            if self.task_manager.is_overdue(task) and not task.completed:
                due_str += " **[OVERDUE]**"
            recurrence_indicator = "🔁" if task.recurrence != "none" else ""
            title = task.title if len(task.title) <= 19 else task.title[:17] + ".."
            description = task.description if len(task.description) <= 25 else task.description[:23] + ".."
            print(f"{task.id:<3} {status:<8} {priority:<8} {tags_str:<15} {due_str:<12} {recurrence_indicator:<4} {title:<20} {description}")

    def update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        try:
            task_id = int(input("Enter task ID to update: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        print(f"Current title: {task.title}")
        new_title = input("Enter new title (press Enter to keep current): ").strip()
        if new_title == "":
            new_title = None  # Keep current value

        print(f"Current description: {task.description}")
        new_description = input("Enter new description (press Enter to keep current): ").strip()
        if new_description == "":
            new_description = None  # Keep current value

        print(f"Current priority: {task.priority}")
        new_priority = input("Enter new priority (high/medium/low, press Enter to keep current): ").strip().lower()
        if new_priority == "":
            new_priority = None  # Keep current value

        print(f"Current tags: {', '.join(task.tags) if task.tags else 'None'}")
        new_tags_input = input("Enter new tags (comma-separated, press Enter to keep current): ").strip()
        if new_tags_input == "":
            new_tags = None  # Keep current value
        else:
            # Split tags and clean them
            new_tags = [tag.strip() for tag in new_tags_input.split(',') if tag.strip()]

        print(f"Current due date: {self.task_manager.format_datetime_display(task.due_datetime) if task.due_datetime else 'None'}")
        new_due_date = input("Enter new due date (YYYY-MM-DD, press Enter to keep current): ").strip()
        if new_due_date == "":
            new_due_datetime = None  # Keep current value
        elif new_due_date.lower() == "none":
            new_due_datetime = None  # Set to None
        else:
            new_due_datetime = self.task_manager.parse_date_input(new_due_date)
            if new_due_datetime is None:
                print("Error: Invalid date format. Please use YYYY-MM-DD format.")
                return

            # Get due time if date was provided
            due_time_input = input("Enter due time (HH:MM, press Enter for 00:00): ").strip()
            if due_time_input:
                due_time = self.task_manager.parse_time_input(due_time_input)
                if due_time is None:
                    print("Error: Invalid time format. Please use HH:MM format.")
                    return
                # Combine date and time
                new_due_datetime = new_due_datetime.replace(hour=due_time.hour, minute=due_time.minute)

        print(f"Current recurrence: {task.recurrence}")
        new_recurrence = input("Enter new recurrence (none/daily/weekly/monthly, press Enter to keep current): ").strip().lower()
        if new_recurrence == "":
            new_recurrence = None  # Keep current value
        elif new_recurrence not in ["none", "daily", "weekly", "monthly"]:
            print("Error: Invalid recurrence pattern. Must be one of: none, daily, weekly, monthly.")
            return

        try:
            if self.task_manager.update_task(task_id, new_title, new_description, new_priority, new_tags, new_due_datetime, new_recurrence):
                print("Task updated successfully.")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
        if confirm in ['y', 'yes']:
            if self.task_manager.delete_task(task_id):
                print("Task deleted successfully.")
            else:
                print("Failed to delete task.")
        else:
            print("Deletion cancelled.")

    def mark_task_complete(self):
        """Handle marking a task as complete/incomplete."""
        print("\n--- Mark Task Complete/Incomplete ---")
        try:
            task_id = int(input("Enter task ID: "))
        except ValueError:
            print("Error: Please enter a valid task ID (number).")
            return

        task = self.task_manager.get_task(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return

        current_status = "complete" if task.completed else "incomplete"
        target_status = "incomplete" if task.completed else "complete"

        confirm = input(f"Mark task '{task.title}' as {target_status}? (Y/n): ").strip().lower()
        if confirm in ['', 'y', 'yes']:
            # Check if this is a recurring task that will create a next occurrence
            if task.recurrence != "none" and not task.completed:
                success = self.task_manager.mark_task_complete(task_id, True)
                if success:
                    # Calculate next occurrence date for message
                    next_occurrence = self.task_manager.calculate_next_occurrence(task)
                    if next_occurrence:
                        next_date_str = self.task_manager.format_datetime_display(next_occurrence)
                        print(f"Task marked as complete. Next occurrence scheduled for {next_date_str}.")
                    else:
                        print("Task marked as complete.")
                else:
                    print("Failed to update task status.")
            else:
                success = self.task_manager.mark_task_complete(task_id, not task.completed)
                if success:
                    new_status = "complete" if not task.completed else "incomplete"
                    print(f"Task marked as {new_status}.")
                else:
                    print("Failed to update task status.")
        else:
            print("Operation cancelled.")

    def sort_tasks(self):
        """Handle sorting tasks."""
        print("\n--- Sort Tasks ---")
        print("Sort by:")
        print("1. ID (creation order)")
        print("2. Priority (high to low)")
        print("3. Title (A to Z)")
        print("4. Status (incomplete first)")
        print("5. Due date (overdue first, then by due date)")

        choice = input("Enter choice (1-5): ").strip()

        sort_mapping = {
            '1': 'id',
            '2': 'priority',
            '3': 'title',
            '4': 'status',
            '5': 'due_date'
        }

        if choice in sort_mapping:
            try:
                self.task_manager.set_sort_order(sort_mapping[choice])
                print(f"Tasks will now be sorted by {sort_mapping[choice]}.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    def run(self):
        """Run the main application loop."""
        print("Welcome to the TODO Application!")
        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_complete()
            elif choice == '6':
                self.search_and_filter_tasks()
            elif choice == '7':
                self.sort_tasks()
            elif choice == '8':
                print("Goodbye!")
                break

            # Pause to let user see the result before showing menu again
            if choice != '8':
                input("\nPress Enter to continue...")