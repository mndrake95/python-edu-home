
tasks = []

def addTask():
    """ Добавляем задачу в список задач """
    task = input ("Введите задачу: ")
    tasks.append(task)
    print (f"Задача '{task}' добавлена в список задач.")
 
def listTasks():
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for index, task in enumerate(tasks):
            print(f" Задача номер {index+1}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Введите номер задачи, которую хотите удалить: "))
        index = taskToDelete - 1
        if index >= 0 and index < len(tasks):
            tasks.pop(index)
            print(f"Задача '{taskToDelete}' удалена из списка задач.")
        else:
            print(f"Задача с номером {taskToDelete} не найдена.")
    except:
        print("Неверный ввод.")
    
if __name__ == "__main__":
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
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print ("Неверный ввод. Пожалуйста введите номер действия от 1 до 4.")

    print ("Вы вышли из программы.")
