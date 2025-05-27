
class Task:
    def __init__ (self, task_id, title, description, status):
        self._task_id = task_id
        self.title = title
        self.description = description
        self._status = status
    def display_info(self):
        print(f"Task ID: {self._task_id}, Title: {self.title}, Description: {self.description}, Status: {self._status}")
    def mark_as_completed(self):
        self._status = "Completed"
        print(f"Task {self._task_id} marked as completed.")
    def get_status(self):
        return self._status
    def set_status(self, new_status):
        allowed_statuses = ["Pending", "In Progress", "Completed"]
        if new_status in allowed_statuses:
            self.status = new_status
            print(f"Status of task {self.title} updated to {new_status}.")
        else:
            print(f"Error: Invalid status '{new_status}'. Status not changed.")

task1 = Task(1, "Buy milk", "Buy 2 liters of milk", "Pending")
task2 = Task(2, "Write plan", "Write a plan for tomorrow", "In Progress")
task3 = Task(3, "Read article", "Read an article about Python", "Completed")

print(f"Task ID: {task1._task_id}, Title: {task1.title}, Description: {task1.description}, Status: {task1._status}")

task2.set_status("Completed")
print(task2.get_status())

print(f"Task ID: {task2._task_id}, Title: {task2.title}, Description: {task2.description}, Status: {task2._status}")

task3.display_info()
task1.mark_as_completed()
task1.display_info()