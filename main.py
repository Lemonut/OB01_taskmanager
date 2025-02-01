class Task:
    def __init__ (self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False #по умолчанию задача не выполнена

    def mark_complete(self):
        self.completed = True

    def info(self):
        status = "Completed" if self.completed else "Not completed"
        print(f"Task: {self.description}\n, Deadline: {self.deadline}\n, Status: {status}\n")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def show_pending_tasks(self):
        print("Current tasks: ")
        for task in self.tasks:
            if not task.completed:
                task.info()

    def mark_task_complete(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_complete()
                print(f"Task {task_description} is marked completed")
                return
        print("Task isn't found")

#Example of use
manager = TaskManager()
manager.add("Купить продукты", "01.02.2025")
manager.add("Сделать домашнее задание", "02.02.2025")
manager.show_pending_tasks()
manager.mark_task_complete("Купить продукты")
manager.show_pending_tasks()


