from dataclasses import dataclass
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "Pending"
    DONE = "Done"

class Priority(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus = TaskStatus.PENDING
    priority: Priority = Priority.MEDIUM