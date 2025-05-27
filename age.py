def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число.")
x = get_int_input("Введите свой возраст: ")
if x < 18:
    print("Вы несовершеннолетний")
elif x == 18:
    print("Вы достигли совершеннолетия")
else: 
     print("Вы совершеннолетний")
