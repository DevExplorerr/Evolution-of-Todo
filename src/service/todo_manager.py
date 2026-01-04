from typing import List, Optional
from src.model.task import Task, TaskStatus, Priority

class TodoManager:
    def __init__(self) -> None:
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, description: str, priority: Priority = Priority.MEDIUM) -> Task:
        if not description.strip():
            raise ValueError("Description cannot be empty")
        
        task = Task(
            id=self._next_id,
            description=description,
            priority=priority
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks)  # Return a copy

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, description: Optional[str] = None, status: Optional[TaskStatus] = None, priority: Optional[Priority] = None) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        
        if description is not None:
            if not description.strip():
                 raise ValueError("Description cannot be empty")
            task.description = description
        
        if status is not None:
            task.status = status
            
        if priority is not None:
            task.priority = priority
            
        return True

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        
        self._tasks.remove(task)
        return True