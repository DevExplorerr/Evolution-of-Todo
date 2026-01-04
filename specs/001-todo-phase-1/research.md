# Research & Design Decisions - Evolution of Todo Phase I

**Feature**: 001-todo-phase-1
**Date**: 2026-01-04

## 1. Data Structure Choice: Dataclasses
**Decision**: Use standard library `dataclasses` for the `Task` model.
**Rationale**: 
- Adheres to "Minimize Dependencies" constraint.
- Provides sufficient immutability and type hinting support for Phase I.
- Pydantic is powerful but introduces an external dependency not strictly required for a simple in-memory list.
**Alternatives Considered**:
- `TypedDict`: Too loose, lacks method support.
- `Pydantic`: Overkill for Phase I, saved for Phase II (FastAPI migration).

## 2. ID Generation Strategy
**Decision**: State-managed Auto-Increment.
**Rationale**:
- `TodoManager` will maintain a `_next_id` counter.
- Simple, thread-safe (for this single-threaded app), and guarantees uniqueness within the session.
- UUIDs are harder to type for CLI users.

## 3. UI Interaction
**Decision**: Standard `input()` loop with `match/case` (Python 3.10+).
**Rationale**:
- Native to Python.
- "Rich" library is permitted but will be reserved for Phase 1.5 (polish) to ensure core logic is robust first without display dependencies.
