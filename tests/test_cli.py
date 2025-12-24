"""
Unit tests for the CLI class.

This module tests the command-line interface functionality.
"""
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from src.cli import CLI
from src.task_manager import TaskManager


class TestCLI(unittest.TestCase):
    """Test cases for the CLI class."""

    def setUp(self):
        """Set up a CLI instance with a mock task manager for each test."""
        self.task_manager = TaskManager()
        self.cli = CLI(self.task_manager)

    @patch('builtins.input', side_effect=['Test Title', 'Test Description'])
    @patch('builtins.print')
    def test_add_task_success(self, mock_print, mock_input):
        """Test adding a task through the CLI."""
        # Add a task
        self.cli.add_task()

        # Verify the task was added
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        task = tasks[0]
        self.assertEqual(task.title, 'Test Title')
        self.assertEqual(task.description, 'Test Description')
        self.assertFalse(task.completed)

    @patch('builtins.input', side_effect=['', 'Test Description'])
    @patch('builtins.print')
    def test_add_task_empty_title_error(self, mock_print, mock_input):
        """Test adding a task with empty title through the CLI."""
        # Try to add a task with empty title
        self.cli.add_task()

        # Verify no task was added
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_view_tasks_empty(self):
        """Test viewing tasks when no tasks exist."""
        # Capture printed output
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        self.cli.view_tasks()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("No tasks yet", output)

    def test_view_tasks_with_tasks(self):
        """Test viewing tasks when tasks exist."""
        # Add a task
        self.task_manager.add_task("Test Task", "Test Description")

        # Capture printed output
        import sys
        from io import StringIO

        captured_output = StringIO()
        sys.stdout = captured_output

        self.cli.view_tasks()

        # Restore stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Test Task", output)
        self.assertIn("[ ]", output)  # Incomplete status

        # Mark task as complete and test again
        self.task_manager.mark_task_complete(1, True)

        captured_output = StringIO()
        sys.stdout = captured_output

        self.cli.view_tasks()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn("[x]", output)  # Complete status

    @patch('builtins.input', side_effect=['1'])
    @patch('builtins.print')
    def test_get_task_by_id_found(self, mock_print, mock_input):
        """Test getting a task by ID."""
        # Add a task first
        task_id = self.task_manager.add_task("Test Task", "Test Description")

        # Mock input to enter the task ID
        with patch('builtins.input', side_effect=[str(task_id)]):
            # Test get_task method (we'll need to call it from a CLI method)
            task = self.task_manager.get_task(task_id)
            self.assertIsNotNone(task)
            self.assertEqual(task.title, "Test Task")

    @patch('builtins.input', side_effect=['999'])
    @patch('builtins.print')
    def test_get_task_by_id_not_found(self, mock_print, mock_input):
        """Test getting a non-existing task by ID."""
        # Mock input to enter a non-existing task ID
        with patch('builtins.input', side_effect=['999']):
            # Test get_task method
            task = self.task_manager.get_task(999)
            self.assertIsNone(task)


if __name__ == '__main__':
    unittest.main()