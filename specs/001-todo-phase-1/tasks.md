# Implementation Tasks: Evolution of Todo - Phase I

**Feature**: Evolution of Todo - Phase I
**Spec**: [specs/001-todo-phase-1/spec.md](specs/001-todo-phase-1/spec.md)
**Plan**: [specs/001-todo-phase-1/plan.md](specs/001-todo-phase-1/plan.md)
**Status**: Pending

## Phase 1: Setup
**Goal**: Initialize the Python project structure and environment managed by `uv`.

- [ ] T001 Initialize `uv` project and create directory structure (`src/model`, `src/service`, `src/ui`) in `pyproject.toml` and root
- [ ] T002 Create empty `__init__.py` files in all subdirectories to make them Python packages

## Phase 2: Foundational
**Goal**: Implement the core data model and base service logic required for all user stories.

- [ ] T003 Implement `TaskStatus` and `Priority` Enums in `src/model/task.py`
- [ ] T004 Implement `Task` dataclass with `id`, `description`, `status`, and `priority` fields in `src/model/task.py`
- [ ] T005 Create `TodoManager` class with empty `_tasks` list and `_next_id` counter in `src/service/todo_manager.py`

## Phase 3: User Story 1 - Add & View Tasks (P1)
**Goal**: Enable users to add new tasks and view the list of existing tasks.
**Story**: [User Story 1 - Add & View Tasks](specs/001-todo-phase-1/spec.md#user-story-1---add--view-tasks-priority-p1)
**Independent Test**: Launch app, add a task, verify it appears in list.

- [ ] T006 [P] [US1] Create unit tests for `add_task` and `get_all_tasks` in `tests/test_todo_manager.py`
- [ ] T007 [US1] Implement `add_task` method in `src/service/todo_manager.py` handling ID generation
- [ ] T008 [US1] Implement `get_all_tasks` method in `src/service/todo_manager.py` returning list copy
- [ ] T009 [US1] Implement `CLI` class with `run` loop and main menu display in `src/ui/cli.py`
- [ ] T010 [US1] Implement "Add Task" menu handler in `src/ui/cli.py`
- [ ] T011 [US1] Implement "View Tasks" menu handler in `src/ui/cli.py`
- [ ] T012 [US1] Wire up `main.py` to instantiate `TodoManager` and start `CLI.run()`

## Phase 4: User Story 2 - Complete & Update Tasks (P2)
**Goal**: Allow modifying task details and status.
**Story**: [User Story 2 - Complete & Update Tasks](specs/001-todo-phase-1/spec.md#user-story-2---complete--update-tasks-priority-p2)
**Independent Test**: Add task, update it, mark complete, verify changes.

- [ ] T013 [P] [US2] Add unit tests for `update_task` logic in `tests/test_todo_manager.py`
- [ ] T014 [US2] Implement `update_task` method (handling description/status updates) in `src/service/todo_manager.py`
- [ ] T015 [US2] Implement "Update Task" menu handler with ID input validation in `src/ui/cli.py`
- [ ] T016 [US2] Implement "Complete Task" menu handler (wrapping update_task) in `src/ui/cli.py`

## Phase 5: User Story 3 - Delete Tasks (P3)
**Goal**: Enable removal of tasks.
**Story**: [User Story 3 - Delete Tasks](specs/001-todo-phase-1/spec.md#user-story-3---delete-tasks-priority-p3)
**Independent Test**: Add task, delete it, verify removal.

- [ ] T017 [P] [US3] Add unit tests for `delete_task` in `tests/test_todo_manager.py`
- [ ] T018 [US3] Implement `delete_task` method in `src/service/todo_manager.py`
- [ ] T019 [US3] Implement "Delete Task" menu handler in `src/ui/cli.py`

## Phase 6: Polish & Cross-Cutting
**Goal**: Finalize UX, error handling, and code quality.

- [ ] T020 [P] Implement robust `try-except ValueError` blocks for all numeric inputs in `src/ui/cli.py`
- [ ] T021 Run `mypy` and fix any strict type hinting errors across all files
- [ ] T022 Manual verify: Application loop continues until explicit "Exit" command
- [ ] T023 Manual verify: Application data resets (is empty) upon restart

## Dependencies

- **T001-T005** (Setup/Foundation) MUST complete before **T006** (US1).
- **T007-T008** (Service Logic) MUST complete before **T010-T011** (UI Wiring) within US1.
- **US1** tasks SHOULD complete before **US2** to ensure base app structure exists.
- **US2** and **US3** are technically independent but logically follow sequential implementation.

## Parallel Execution Opportunities

- **T006, T013, T017** (Tests) can be written in parallel with their respective service implementations if TDD is strictly followed.
- **T020** (Error handling) can be implemented alongside UI tasks if developers are careful, but typically safer as a polish pass.

## Implementation Strategy

1.  **MVP (Phase 1-3)**: Focus on getting the app running with Add/View capabilities first. This proves the core loop and data model work.
2.  **Increment (Phase 4)**: Add the ability to modify state (Update/Complete).
3.  **Complete (Phase 5-6)**: Add deletion and finalize strictness checks.
