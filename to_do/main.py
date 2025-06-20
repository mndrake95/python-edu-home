import json
import os 
from datetime import datetime
from datetime import timezone
class Task:
    def __init__ (self, task_id, title, description, status):
        self._task_id = task_id
        self.title = title
        self.description = description
        self._status = status
        self.created_at = datetime.now(timezone.utc)
        self.completion_time = None
    def display_info(self):
        if self._status in ("Pending", "In Progress"):
            print(f"Task ID: {self._task_id}, Title: {self.title}, Description: {self.description}, Status: {self._status}, Created: {self.created_at.strftime('%d-%m-%Y')}")
        elif self._status == "Completed":
            completed_str = self.completion_time.strftime('%d-%m-%Y') if self.completion_time else "N/A"
            print(f"Task ID: {self._task_id}, Title: {self.title}, Description: {self.description}, Status: {self._status}, Completed: {completed_str}")
    def set_status(self, new_status):
        allowed_statuses = ["Pending", "In Progress", "Completed"]
        if new_status in allowed_statuses:
            self._status = new_status
            print(f"Status of task {self.title} updated to {new_status}.")
        else:
            print(f"Error: Invalid status '{new_status}'. Status not changed.")
        if new_status == "Completed":
            self.completion_time = datetime.now(timezone.utc)
        elif self._status == "Completed" and new_status != "Completed":
            self.completion_time = None

    def get_status(self):
        return self._status
    def to_dict(self):
        return {'id': self._task_id, 'title': self.title, 'description': self.description, 'status': self._status, 'created_at': self.created_at.strftime('%d-%m-%Y'), 'completed_at': self.completion_time.strftime('%d-%m-%Y') if self.completion_time else None}

class TaskManager:
    def __init__ (self):
        self._tasks_list = []
        self._next_task_id = 1
    def add_task(self):
        task_title = input("Enter task title: ")
        task_description = input("Enter task description: ")
        task = Task(self._next_task_id, task_title, task_description, "Pending")
        self._tasks_list.append(task)
        self._next_task_id += 1
        print(f"Task '{task_title}' added with ID {task._task_id}.")
    def list_task(self):
        if not self._tasks_list:
            print("Task list is empty.")
        else:
            print("Task list: ")
            for task in self._tasks_list:
                task.display_info()
    def delete_task(self):
        self.list_task()
        try:
            task_to_delete = int(input("Enter the task number you want to delete: "))
            index = task_to_delete -1
            if index >= 0 and index < len(self._tasks_list):
                deleted_task = self._tasks_list.pop(index)
                print(f"Task '{deleted_task.title}' with ID {deleted_task._task_id} deleted from the task list.")
            else:
                print(f"Task with number {task_to_delete} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    def task_status_change(self):
        self.list_task()
        try:
            task_to_change = int(input("Enter the task number you want to change status: "))
            index = task_to_change - 1
            if index >= 0 and index < len(self._tasks_list):
                new_status = input("Enter new status (Pending, In Progress, Completed): ")
                self._tasks_list[index].set_status(new_status)
            else:
                print(f"Task with number {task_to_change} not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    def save_task_to_file(self, filename):
        task_to_save = [task.to_dict() for task in self._tasks_list]
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_dir, filename)
        with open(output_file_path, 'w') as file:
            json.dump(task_to_save, file, indent=4)
            print(f"Tasks saved to {output_file_path}")
    def load_task_from_file(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_file_path = os.path.join(script_dir, filename)
        with open(output_file_path, 'r') as file:
            json.load
        


if __name__ == "__main__":
    my_task_manager = TaskManager()
    ### Цикл для работы приложения ###
    while True:
        print ("\n")
        print ("Choose an action:")
        print ("----------------------")
        print ("1. Add task")
        print ("2. Delete task")
        print ("3. List tasks")
        print ("4. Change task status")
        print ("5. Exit")

        choice = input("Choose # of action: ")

        if (choice == "1"):
            my_task_manager.add_task()
        elif (choice == "2"):
            my_task_manager.delete_task()
        elif (choice == "3"):
            my_task_manager.list_task()
        elif (choice == "4"):
            my_task_manager.task_status_change()
        elif (choice == "5"):
            break
        else:
            print ("Invalid input. Please enter # of action from 1 to 5.")

    print ("You exited.")
