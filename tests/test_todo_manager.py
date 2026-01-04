import unittest
from src.service.todo_manager import TodoManager
from src.model.task import Task, TaskStatus, Priority

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        self.manager = TodoManager()

    def test_add_task_success(self):
        task = self.manager.add_task("Buy Groceries", Priority.HIGH)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Buy Groceries")
        self.assertEqual(task.status, TaskStatus.PENDING)
        self.assertEqual(task.priority, Priority.HIGH)

    def test_add_task_default_priority(self):
        task = self.manager.add_task("Walk Dog")
        self.assertEqual(task.priority, Priority.MEDIUM)

    def test_add_task_empty_description(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_get_all_tasks_empty(self):
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 0)

    def test_get_all_tasks_populated(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        tasks = self.manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].id, 1)
        self.assertEqual(tasks[1].id, 2)

    def test_update_task_success(self):
        task = self.manager.add_task("Original")
        result = self.manager.update_task(task.id, description="Updated", status=TaskStatus.DONE, priority=Priority.LOW)
        self.assertTrue(result)
        
        updated_task = self.manager.get_task(task.id)
        self.assertEqual(updated_task.description, "Updated")
        self.assertEqual(updated_task.status, TaskStatus.DONE)
        self.assertEqual(updated_task.priority, Priority.LOW)

    def test_update_task_partial(self):
        task = self.manager.add_task("Original")
        self.manager.update_task(task.id, description="Updated")
        
        updated_task = self.manager.get_task(task.id)
        self.assertEqual(updated_task.description, "Updated")
        self.assertEqual(updated_task.status, TaskStatus.PENDING)  # Should remain unchanged

    def test_update_task_not_found(self):
        result = self.manager.update_task(999, description="Ghost")
        self.assertFalse(result)

    def test_delete_task_success(self):
        task = self.manager.add_task("To Delete")
        result = self.manager.delete_task(task.id)
        self.assertTrue(result)
        self.assertIsNone(self.manager.get_task(task.id))
        self.assertEqual(len(self.manager.get_all_tasks()), 0)

    def test_delete_task_not_found(self):
        result = self.manager.delete_task(999)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
