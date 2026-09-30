raw_age = input("Сколько тебе лет ").strip()
if raw_age.isdigit():
    age = int(raw_age)
    print(f"Вы ввели ваш возраст - {age}")
else:
    print("Ошибка: возраст должен быть числом")

login = input("Введите ваш логин ").strip()
if login and login.isalnum():
    print(f"Логин принят: {login}" )
else:
    print("Логин должен содержать буквы и цифры")

full_name = input("Ваше полное ФИО ").strip()
parts = full_name.split()
if len(parts) == 3:
    surname, name, midlename = parts
    print(f"Фамилия: {surname}, Имя: {name}, Отчество: {midlename}")
else:
    print("Введите ваше полное ФИО ")
