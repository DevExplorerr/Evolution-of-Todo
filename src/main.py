from src.service.todo_manager import TodoManager
from src.ui.cli import CLI

def main():
    manager = TodoManager()
    cli = CLI(manager)
    cli.run()

if __name__ == "__main__":
    main()
