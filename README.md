# Evolution of Todo 🚀

> **Hackathon II Submission**
> *From Console App to Cloud-Native AI Chatbot*

## 📖 Project Overview

**Evolution of Todo** is a progressive software engineering project built for the **Mastering Spec-Driven Development & Cloud Native AI Hackathon**.

The goal is to master the art of building applications iteratively—starting from a simple in-memory console app (Phase I) and evolving it into a fully-featured, cloud-native AI chatbot deployed on Kubernetes (Phase V). This project strictly follows **Spec-Driven Development (SDD)** principles, using AI agents to generate implementation based on rigorous specifications.

---

## ⚡ Current Status: Phase I Completed

**✅ Phase I: In-Memory Python Console App**

A robust, text-based Task Manager that runs entirely in the terminal. It features a modular architecture separating business logic from the UI, designed to be scalable for future web migration.

### Key Features (Phase I)
* **Create**: Add new tasks with title, priority (High/Medium/Low), and status.
* **Read**: View all tasks or filter by ID.
* **Update**: Modify task details or toggle "Completed" status.
* **Delete**: Remove tasks by ID.
* **In-Memory Storage**: Data persists only during the runtime session (Python Lists/Dictionaries).
* **Type Safety**: Built with Python 3.13+ using Pydantic/Dataclasses and strict type hinting.

---

## 🛠️ Installation & Usage

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

### Prerequisites
* Python 3.13+
* `uv` installed

### Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/evolution-of-todo.git](https://github.com/YOUR_USERNAME/evolution-of-todo.git)
    cd evolution-of-todo
    ```

2.  **Install dependencies:**
    ```bash
    uv sync
    ```

3.  **Run the Application:**
    ```bash
    uv run -m src.main
    ```

4.  **Run Tests:**
    ```bash
    python -m unittest discover tests
    ```

---

## 🗺️ Development Roadmap

| Phase | Description | Tech Stack | Status |
| :--- | :--- | :--- | :--- |
| **I** | **In-Memory Console App** | Python, Spec-Kit Plus | ✅ **Completed** |
| **II** | Full-Stack Web Application | Next.js, FastAPI, SQLModel, Neon DB | ⏳ Pending |
| **III** | AI-Powered Todo Chatbot | OpenAI ChatKit, Agents SDK | 🔒 Locked |
| **IV** | Local Kubernetes Deployment | Docker, Minikube, Helm | 🔒 Locked |
| **V** | Advanced Cloud Deployment | Kafka, Dapr, DigitalOcean DOKS | 🔒 Locked |

---

## 🏗️ Project Structure

```text
evolution-of-todo/
├── src/
│   ├── model/         # Data definitions (Task, Priority, Status)
│   ├── service/       # Business logic (TodoManager)
│   ├── ui/            # CLI User Interface logic
│   └── main.py        # Application entry point
├── tests/             # Unit tests
├── pyproject.toml     # Dependencies managed by uv
└── README.md
```

## 🧠 Development Philosophy

### This project is built using Spec-Driven Development. No code is written manually.

* **Constitution**: Define core principles and constraints.
* **Spec**: Define exact functional requirements.
* **Plan**: Architecture and step-by-step execution plan.
* **Generate**: AI Agent (Claude Code/Gemini CLI) implements the code.
