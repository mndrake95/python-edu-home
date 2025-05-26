class Task:
    def __init__ (self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
    def display_info(self):
        print(f"Task ID: {self.task_id}, Title: {self.title}, Description: {self.description}, Status: {self.status}")

task1 = Task(1, "Buy milk", "Buy 2 liters of milk", "Pending")
task2 = Task(2, "Write plan", "Write a plan for tomorrow", "In Progress")
task3 = Task(3, "Read article", "Read an article about Python", "Completed")

print(f"Task ID: {task1.task_id}, Title: {task1.title}, Description: {task1.description}, Status: {task1.status}")

task2.status = "Completed"

print(f"Task ID: {task2.task_id}, Title: {task2.title}, Description: {task2.description}, Status: {task2.status}")

task3.display_info()