# Data Model & Interfaces - Evolution of Todo Phase I

## Entities

### Task
Represents a single work item.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `int` | Yes | Unique identifier (auto-generated) |
| `description` | `str` | Yes | Text description of the task |
| `status` | `TaskStatus` | Yes | Enum: `PENDING`, `DONE` |
| `priority` | `Priority` | No | Enum: `HIGH`, `MEDIUM`, `LOW` (Default: `MEDIUM`) |

## Internal Service Contract (`TodoManager`)

The `TodoManager` class acts as the internal API.

### Methods

#### `add_task`
- **Args**: `description: str`, `priority: Priority = Priority.MEDIUM`
- **Returns**: `Task` (The created task with assigned ID)
- **Raises**: `ValueError` if description is empty.

#### `get_task`
- **Args**: `task_id: int`
- **Returns**: `Optional[Task]`
- **Description**: Finds task by ID. Returns `None` if not found.

#### `get_all_tasks`
- **Args**: None
- **Returns**: `List[Task]`
- **Description**: Returns a copy of the internal list to prevent direct mutation.

#### `update_task`
- **Args**: `task_id: int`, `description: Optional[str]`, `status: Optional[TaskStatus]`, `priority: Optional[Priority]`
- **Returns**: `bool` (True if updated, False if ID not found)

#### `delete_task`
- **Args**: `task_id: int`
- **Returns**: `bool` (True if deleted, False if ID not found)
