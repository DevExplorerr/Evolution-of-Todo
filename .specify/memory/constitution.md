<!-- 
Sync Impact Report:
- Version change: Template → 1.0.0
- List of modified principles: Defined I through V based on user input.
- Added sections: Technology Standards, System Constraints.
- Templates requiring updates:
  - .specify/templates/spec-template.md (Ensure Python/CLI focus)
  - .specify/templates/plan-template.md (Ensure Architecture checks align with Ephemeral/In-Memory)
- Follow-up TODOs: None.
-->

# Evolution of Todo - Phase I: In-Memory Python Console Application Constitution

## Core Principles

### I. Spec-Driven Strictness
Implementation must strictly follow the defined spec. No improvisation is permitted. Any deviation from the agreed-upon specification requires a formal amendment to the spec before code implementation.

### II. Ephemeral Architecture
Data persistence is strictly in-memory (using Python Lists or Dictionaries). No external database files (SQLite, JSON files, etc.) or SQL are allowed for Phase I. The system state resets upon termination.

### III. Separation of Concerns
Business logic must be decoupled from the CLI interface layer. This is critical to allow for a smooth migration to a FastAPI-based web architecture in Phase II without rewriting core logic.

### IV. Zero-Manual-Edit
The generated code must be executable immediately without manual syntax correction. The output of the development process is working, runnable code.

### V. Resilient User Experience
The CLI must handle invalid inputs gracefully (e.g., entering text for a numeric ID) without crashing. Error messages should be informative and guide the user back to a valid state.

## Technology Standards

**Language & Style**
- **Language**: Python 3.10+
- **Code Style**: PEP 8 compliant.
- **Typing**: Comprehensive Type Hinting (Strict) is required for all function signatures and class definitions.
- **Documentation**: All functions and classes must have Python docstrings explaining purpose, arguments, and return values.

**Data Structures**
- Task definitions and core entities must use Python **Dataclasses** or **Pydantic models** to ensure structured data handling.

**Success Criteria**
- The application runs explicitly in the console.
- Data is retained successfully as long as the script is running.
- All "Basic Level" (CRUD) and "Intermediate Level" (Filter/Priority) features are functional.
- The code passes a static type check (e.g., mypy) without errors.

## System Constraints

**Interface & Dependencies**
- **UI Interface**: Command Line Interface (CLI) loop only.
- **External Dependencies**: Minimize. Use the standard library where possible. Third-party libraries 'rich' or 'typer' are permitted only if necessary for advanced formatting or CLI parsing.

**State Management**
- Use a **Global variable** or a **Singleton class instance** to hold the list of tasks during runtime. This centralization simplifies the "in-memory" constraint implementation.

## Governance

This Constitution supersedes all other technical practices or preferences.
- **Amendments**: Require documentation, justification, and a migration plan if code is already in flight.
- **Compliance**: All Pull Requests and Code Reviews must verify compliance with strict type hinting, PEP 8, and the separation of concerns principle.
- **Runtime Guidance**: Refer to `GEMINI.md` and `.specify/memory/constitution.md` as the authoritative sources of truth.

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04