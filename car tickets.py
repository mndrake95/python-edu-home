def get_name_input(prompt):
    """
    Запрашивает у пользователя ввод имени с заданным сообщением и проверяет его на корректность.

    Имя считается допустимым, если оно:
    - состоит только из букв, пробелов, символов `-` или `` ` `` (обратная кавычка),
    - имеет длину от 2 до 16 символов включительно.

    Параметры:
        prompt (str): Сообщение, отображаемое пользователю при запросе ввода.

    Возвращает:
        str: Корректная строка имени, введённая пользователем.
    """
    while True:
        text = input(prompt).strip()
        if all(c.isalpha() or c.isspace() or c == "`" or c == "-" for c in text) and len(text) >= 2 and len(text) <= 16:
            return text
        print("Ошибка: Введите только буквы и пробелы.")
name = get_name_input("Введите имя: ")
def get_int_input(prompt, min_value = 0, max_value = 250):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                print(f"Ошибка: Значение должно быть не меньше {min_value} и не больше {max_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: Введите скорость в пределах от 0 до 250 км/ч.")
limit = get_int_input("Введите ограничение скорости: ")
speed = get_int_input("Введите скорость: ")
over_speed = speed - limit
def calculate_penalty(over_speed):
    if over_speed <= 10:
        return "Вы получили предупреждение"
    elif over_speed > 10 and over_speed <= 20:
        return "Вы получили штраф 5 000 тенге"
    elif over_speed > 20 and over_speed <= 40:
        return "Вы получили штраф 10 000 тенге"
    elif over_speed > 40:
        return "Вы получили штраф 20 000 тенге и лишение прав на 3 месяца"
if over_speed > 0:
    print(f"{name} превысил скорость на {over_speed} км/ч")
    print(calculate_penalty(over_speed))
else:
    print(f"{name} ехал в пределах разрешённой скорости")