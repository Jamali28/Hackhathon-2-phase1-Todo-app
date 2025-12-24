"""
Unit tests for the TaskManager class.

This module tests all core task operations from the task_manager module.
"""
import unittest
from src.task_manager import TaskManager
from src.models import Task


class TestTaskManager(unittest.TestCase):
    """Test cases for the TaskManager class."""

    def setUp(self):
        """Set up a fresh TaskManager instance for each test."""
        self.task_manager = TaskManager()

    def test_add_task_success(self):
        """Test adding a task with valid title and description."""
        title = "Test Task"
        description = "Test Description"
        task_id = self.task_manager.add_task(title, description)

        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.task_manager.tasks), 1)
        task = self.task_manager.tasks[0]
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, title)
        self.assertEqual(task.description, description)
        self.assertEqual(task.completed, False)

    def test_add_task_optional_description(self):
        """Test adding a task with only a title (no description)."""
        title = "Test Task"
        task_id = self.task_manager.add_task(title)

        self.assertEqual(task_id, 1)
        task = self.task_manager.tasks[0]
        self.assertEqual(task.title, title)
        self.assertEqual(task.description, "")

    def test_add_task_empty_title_error(self):
        """Test that adding a task with empty title raises ValueError."""
        with self.assertRaises(ValueError):
            self.task_manager.add_task("")

        with self.assertRaises(ValueError):
            self.task_manager.add_task("   ")  # Only whitespace

    def test_list_tasks_empty(self):
        """Test listing tasks when no tasks exist."""
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 0)

    def test_list_tasks_with_tasks(self):
        """Test listing tasks when tasks exist."""
        # Add some tasks
        id1 = self.task_manager.add_task("Task 1", "Description 1")
        id2 = self.task_manager.add_task("Task 2", "Description 2")

        tasks = self.task_manager.list_tasks()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, id1)
        self.assertEqual(tasks[1].id, id2)

    def test_get_task_found(self):
        """Test getting an existing task by ID."""
        task_id = self.task_manager.add_task("Test Task", "Test Description")
        task = self.task_manager.get_task(task_id)

        self.assertIsNotNone(task)
        self.assertEqual(task.id, task_id)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")

    def test_get_task_not_found(self):
        """Test getting a non-existing task by ID."""
        task = self.task_manager.get_task(999)
        self.assertIsNone(task)

    def test_update_task_success(self):
        """Test updating an existing task."""
        task_id = self.task_manager.add_task("Original Title", "Original Description")

        result = self.task_manager.update_task(task_id, "New Title", "New Description")

        self.assertTrue(result)
        updated_task = self.task_manager.get_task(task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "New Description")

    def test_update_task_partial(self):
        """Test updating only title or description of a task."""
        task_id = self.task_manager.add_task("Original Title", "Original Description")

        # Update only the title
        result = self.task_manager.update_task(task_id, title="New Title")
        self.assertTrue(result)

        updated_task = self.task_manager.get_task(task_id)
        self.assertEqual(updated_task.title, "New Title")
        self.assertEqual(updated_task.description, "Original Description")  # Should remain unchanged

    def test_update_task_not_found(self):
        """Test updating a non-existing task."""
        result = self.task_manager.update_task(999, "New Title")
        self.assertFalse(result)

    def test_update_task_empty_title_error(self):
        """Test that updating a task with empty title raises ValueError."""
        task_id = self.task_manager.add_task("Original Title")

        with self.assertRaises(ValueError):
            self.task_manager.update_task(task_id, title="")

        with self.assertRaises(ValueError):
            self.task_manager.update_task(task_id, title="   ")  # Only whitespace

    def test_delete_task_success(self):
        """Test deleting an existing task."""
        task_id = self.task_manager.add_task("Test Task")
        initial_count = len(self.task_manager.tasks)

        result = self.task_manager.delete_task(task_id)

        self.assertTrue(result)
        self.assertEqual(len(self.task_manager.tasks), initial_count - 1)
        self.assertIsNone(self.task_manager.get_task(task_id))

    def test_delete_task_not_found(self):
        """Test deleting a non-existing task."""
        result = self.task_manager.delete_task(999)
        self.assertFalse(result)

    def test_mark_task_complete_success(self):
        """Test marking a task as complete."""
        task_id = self.task_manager.add_task("Test Task")
        task = self.task_manager.get_task(task_id)
        self.assertFalse(task.completed)  # Should be initially incomplete

        result = self.task_manager.mark_task_complete(task_id, True)

        self.assertTrue(result)
        updated_task = self.task_manager.get_task(task_id)
        self.assertTrue(updated_task.completed)

    def test_mark_task_incomplete_success(self):
        """Test marking a task as incomplete."""
        task_id = self.task_manager.add_task("Test Task")
        # First mark as complete
        self.task_manager.mark_task_complete(task_id, True)
        task = self.task_manager.get_task(task_id)
        self.assertTrue(task.completed)  # Should be initially complete

        result = self.task_manager.mark_task_complete(task_id, False)

        self.assertTrue(result)
        updated_task = self.task_manager.get_task(task_id)
        self.assertFalse(updated_task.completed)

    def test_mark_task_not_found(self):
        """Test marking a non-existing task."""
        result = self.task_manager.mark_task_complete(999, True)
        self.assertFalse(result)

    def test_get_next_id(self):
        """Test getting the next available task ID."""
        initial_id = self.task_manager.get_next_id()
        self.assertEqual(initial_id, 1)

        # Add a task
        self.task_manager.add_task("Test Task")

        next_id = self.task_manager.get_next_id()
        self.assertEqual(next_id, 2)

    def test_id_uniqueness(self):
        """Test that task IDs are unique and sequential."""
        id1 = self.task_manager.add_task("Task 1")
        id2 = self.task_manager.add_task("Task 2")
        id3 = self.task_manager.add_task("Task 3")

        self.assertEqual(id1, 1)
        self.assertEqual(id2, 2)
        self.assertEqual(id3, 3)

        # Verify all tasks have unique IDs
        tasks = self.task_manager.list_tasks()
        ids = [task.id for task in tasks]
        self.assertEqual(len(ids), len(set(ids)))  # All IDs should be unique


if __name__ == '__main__':
    unittest.main()