"""
Main entry point for the TODO application.

This module initializes the application components and runs the main loop.
"""
from .task_manager import TaskManager
from .cli import CLI


def main():
    """
    Main function to run the TODO application.

    Initializes the task manager and CLI, then starts the main application loop.
    """
    # Initialize the task manager and CLI
    task_manager = TaskManager()
    cli = CLI(task_manager)

    # Run the application
    cli.run()


if __name__ == "__main__":
    main()