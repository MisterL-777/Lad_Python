# Только чётные. Вывести все чётные числа от 1 до 100
for number in range(1, 101):
    if number % 2 != 0:
        continue
    print(number)