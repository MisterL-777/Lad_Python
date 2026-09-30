# Таблица умножения

while True:
    user_input = input("Введите число n: ")
    try:
        n = int(user_input)
        break  # ввод успешен, выходим из цикла
    except ValueError:
        print("Ошибка: нужно ввести именно целое число. Попробуйте ещё раз.")

for i in range(1, 11):  # от 1 до 10 включительно
    print(f"{n} * {i} = {n * i}")