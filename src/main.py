"""
Main entry point for the TODO application.

This module initializes the application components and runs the main loop.
"""
import threading
import time
try:
    # When running as a module (python -m src.main)
    from .task_manager import TaskManager
    from .cli import CLI
except ImportError:
    # When running directly (python src/main.py)
    from task_manager import TaskManager
    from cli import CLI


def print_startup_reminders(task_manager):
    """
    Print startup reminder banner showing overdue and upcoming tasks.

    Args:
        task_manager: The TaskManager instance to get task data from
    """
    print("\n" + "="*50)
    print("STARTUP REMINDERS")
    print("="*50)

    # Get overdue tasks
    overdue_tasks = task_manager.get_overdue_tasks()
    if overdue_tasks:
        print(f"[WARNING] {len(overdue_tasks)} OVERDUE TASK(S):")
        for task in overdue_tasks:
            due_str = task_manager.format_datetime_display(task.due_datetime)
            print(f"   - [{task.id}] {task.title} (due: {due_str})")
    else:
        print("[INFO] No overdue tasks")

    # Get tasks due today
    due_today_tasks = task_manager.get_due_today_tasks()
    if due_today_tasks:
        print(f"\n[TODAY] {len(due_today_tasks)} TASK(S) DUE TODAY:")
        for task in due_today_tasks:
            due_str = task_manager.format_datetime_display(task.due_datetime)
            print(f"   - [{task.id}] {task.title} (due: {due_str})")

    # Get tasks due soon (within 24 hours)
    due_soon_tasks = task_manager.get_due_soon_tasks(hours=24)
    # Filter out tasks that are already due today to avoid duplicates
    due_soon_tasks = [task for task in due_soon_tasks if task not in due_today_tasks and task not in overdue_tasks]
    if due_soon_tasks:
        print(f"\n[SOON] {len(due_soon_tasks)} TASK(S) DUE SOON (within 24 hours):")
        for task in due_soon_tasks:
            due_str = task_manager.format_datetime_display(task.due_datetime)
            print(f"   - [{task.id}] {task.title} (due: {due_str})")

    print("="*50)


def background_reminder_thread(task_manager):
    """
    Background thread that checks for new alerts every 60 seconds.

    Args:
        task_manager: The TaskManager instance to get task data from
    """
    while True:
        try:
            # Check for newly overdue tasks or tasks that became due soon
            time.sleep(60)  # Check every minute

            # Find tasks that are now overdue but weren't before (if we were tracking previous state)
            # For now, just print a simple message that the thread is running
            print("\n[REMINDER CHECK]: Checking for due tasks...")

            # Get currently overdue tasks
            overdue_tasks = task_manager.get_overdue_tasks()
            if overdue_tasks:
                print(f"[WARNING] {len(overdue_tasks)} OVERDUE TASK(S) - Please check your task list!")

        except Exception as e:
            # If there's an error, just continue the loop
            print(f"Background reminder thread error: {e}")
            time.sleep(60)  # Wait before next check


def main():
    """
    Main function to run the TODO application.

    Initializes the task manager and CLI, then starts the main application loop.
    """
    # Initialize the task manager and CLI
    task_manager = TaskManager()
    cli = CLI(task_manager)

    # Print startup reminders
    print_startup_reminders(task_manager)

    # Start background reminder thread if needed
    reminder_thread = threading.Thread(target=background_reminder_thread, args=(task_manager,), daemon=True)
    reminder_thread.start()

    # Run the application
    cli.run()


if __name__ == "__main__":
    main()