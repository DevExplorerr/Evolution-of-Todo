import sys
from src.service.todo_manager import TodoManager
from src.model.task import Priority

from src.model.task import Priority, TaskStatus

class CLI:
    def __init__(self, manager: TodoManager):
        self.manager = manager

    def display_menu(self):
        print("\n--- Todo App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.handle_add_task()
                elif choice == "2":
                    self.handle_view_tasks()
                elif choice == "3":
                    self.handle_update_task()
                elif choice == "4":
                    self.handle_complete_task()
                elif choice == "5":
                    self.handle_delete_task()
                elif choice == "6":
                    print("Exiting...")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def handle_add_task(self):
        description = input("Enter description: ")
        
        # Priority Input
        print("Priorities: High, Medium, Low")
        priority_input = input("Enter priority (Default: Medium): ").strip().upper()
        
        priority = Priority.MEDIUM
        if priority_input == "HIGH":
            priority = Priority.HIGH
        elif priority_input == "LOW":
            priority = Priority.LOW
        
        try:
            task = self.manager.add_task(description, priority)
            print(f"Task added: {task.id} - {task.description} [{task.priority.value}]")
        except ValueError as e:
            print(f"Error adding task: {e}")

    def handle_view_tasks(self):
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return

        print("\nID  | Status  | Priority | Description")
        print("-" * 40)
        for task in tasks:
            print(f"{task.id:<3} | {task.status.value:<7} | {task.priority.value:<8} | {task.description}")

    def handle_update_task(self):
        try:
            task_id = int(input("Enter Task ID to update: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return

        new_description = input("Enter new description (leave empty to keep current): ")
        
        if self.manager.update_task(task_id, description=new_description if new_description else None):
             print(f"Task {task_id} updated successfully.")
        else:
             print(f"Task {task_id} not found.")

    def handle_complete_task(self):
        try:
            task_id = int(input("Enter Task ID to complete: "))
        except ValueError:
             print("Invalid ID. Please enter a number.")
             return
        
        if self.manager.update_task(task_id, status=TaskStatus.DONE):
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Task {task_id} not found.")

    def handle_delete_task(self):
        try:
            task_id = int(input("Enter Task ID to delete: "))
        except ValueError:
             print("Invalid ID. Please enter a number.")
             return
        
        if self.manager.delete_task(task_id):
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Task {task_id} not found.")
