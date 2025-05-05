def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")

hours = get_int_input("Введите часы работы: ")
days = get_int_input("Введите дни работы: ")
rate = get_int_input("Введите ставку: ")

print(f"Заработная плата: {(hours * days) * rate}")