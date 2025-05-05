def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")
x = get_int_input("Введите свою оценку: ")
if x == 5:
        print("Отлично")
elif x == 4:
        print("Хорошо")
elif x == 3:
        print("Удовлетворительно")
elif x == 2:
        print("Плохо")
else: 
        print("Ошибка: Введите число от 2 до 5.")