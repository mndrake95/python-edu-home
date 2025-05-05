def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")
x = get_int_input("Введите число: ")
if x < 0:
    print("Отрицательное число")
elif x > 0:
    print("Положительное число")
if x / 2 == 0:
    print("Число четное")
elif x / 2 != 0:
    print("Число нечетное")
if x % 3 == 0:
    print("Число кратно 3")
if x % 5 == 0:
    print("Число кратно 5")