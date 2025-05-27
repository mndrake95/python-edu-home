
class Task:
    def __init__ (self, task_id, title, description, status):
        self._task_id = task_id
        self.title = title
        self.description = description
        self._status = status
    def display_info(self):
        print(f"Task ID: {self._task_id}, Title: {self.title}, Description: {self.description}, Status: {self._status}")
    def set_status(self, new_status):
        allowed_statuses = ["Pending", "In Progress", "Completed"]
        if new_status in allowed_statuses:
            self._status = new_status
            print(f"Status of task {self.title} updated to {new_status}.")
        else:
            print(f"Error: Invalid status '{new_status}'. Status not changed.")
    def get_status(self):
        return self._status

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

if __name__ == "__main__":
    my_task = Task()
    my_task_manager = TaskManager()
    ### Цикл для работы приложения ###
    while True:
        print ("\n")
        print ("Выберите желаемое действие")
        print ("----------------------")
        print ("1. Добавить задачу")
        print ("2. Удалить задачу")
        print ("3. Список задач")
        print ("4. Выход")

        choice = input("Введите номер действия: ")

        if (choice == "1"):
            my_task_manager.add_task()
        elif (choice == "2"):
            my_task_manager.delete_task()
        elif (choice == "3"):
            my_task_manager.list_task()
        elif (choice == "4"):
            break
        else:
            print ("Неверный ввод. Пожалуйста введите номер действия от 1 до 4.")

    print ("Вы вышли из программы.")
