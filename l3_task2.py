from random import randint

secret = randint(1, 10)
attempt = 0

while True:
    guess = int(input("Введите загаданное число от 1 до 10: "))

    # Проверка диапазона
    if guess < 1 or guess > 10:
        print("Число должно быть от 1 до 10!")
        continue

    attempt += 1

    if guess < secret:
        print(f"Пользователь ввел число {guess}, оно меньше загаданного")
        continue

    if guess > secret:
        print(f"Пользователь ввел число {guess}, оно больше загаданного")
        continue

    print(f"Пользователь угадал число за {attempt} попыток")
    break
