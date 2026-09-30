# Калькулятор характера числа

while True:
    user_input = input("Введите целое число: ")
    try:
        num = int(user_input)
        break # Ввод успешен, выходим из цикла
    except ValueError:
        print("Ошибка: нужно ввести именно целое число. Попробуйте ещё раз.")

# Четное или нечетное
if num % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

# Положительное, отрицательное или ноль
if num > 0:
    sign = "положительное"
elif num < 0:
    sign = "отрицательное"
else:
    sign = "ноль"

# Больше ли оно 100
if num > 100:
    compared = "больше 100"
elif num == 100:
    compared = "равно 100"
else:
    compared = "меньше 100"

print(f"Число {num}: {parity}, {sign}, {compared}. ")

