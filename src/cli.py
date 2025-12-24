"""
CLI interface for the TODO application.

This module handles all user input/output, menu display, prompts, and formatting.
"""
from typing import Optional
from .task_manager import TaskManager


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
        print("6. Exit")
        print("="*40)

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's menu choice (1-6)
        """
        while True:
            try:
                choice = input("Enter your choice (1-6): ").strip()
                if choice in ['1', '2', '3', '4', '5', '6']:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except KeyboardInterrupt:
                print("\nExiting...")
                return '6'
            except EOFError:
                print("\nExiting...")
                return '6'

    def add_task(self):
        """Handle adding a new task."""
        print("\n--- Add New Task ---")
        title = input("Enter task title (required): ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()
        try:
            task_id = self.task_manager.add_task(title, description)
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

        print(f"{'ID':<3} {'Status':<8} {'Title':<20} {'Description'}")
        print("-" * 60)
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            title = task.title if len(task.title) <= 19 else task.title[:17] + ".."
            description = task.description if len(task.description) <= 25 else task.description[:23] + ".."
            print(f"{task.id:<3} {status:<8} {title:<20} {description}")

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

        try:
            if self.task_manager.update_task(task_id, new_title, new_description):
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
            success = self.task_manager.mark_task_complete(task_id, not task.completed)
            if success:
                new_status = "complete" if not task.completed else "incomplete"
                print(f"Task marked as {new_status}.")
            else:
                print("Failed to update task status.")
        else:
            print("Operation cancelled.")

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
                print("Goodbye!")
                break

            # Pause to let user see the result before showing menu again
            if choice != '6':
                input("\nPress Enter to continue...")