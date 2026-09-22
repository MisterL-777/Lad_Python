# Программа создает таблицу "фактов о себе"

name = "Aleksey"     #str
age = 32             #int
height = 1.69        #float
like_number = 11     #int
love_python = True   #bool

# Используем f-строки для формирования
print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Рост: {height}")
print(f"Любимое число: {like_number}")
print(f"Люблю Python: {love_python}")

# Проверка типов данных
print(type(name))           #<class "str">
print(type(age))            #<class "int">
print(type(height))         #<class "float">
print(type(like_number))    #<class "int">
print(type(love_python))    #<class "bool">


# python -m venv создает исключительно изолированное виртуальное окружение, в то время как uv init инициализирует полноценную структуру Python-проекта. Использовать python -m venv, если мне нужно простое, чистое виртуальное окружение без привязки к конкретному менеджеру проектов. Использовать uv init, если я начинаю разработку нового приложения или библиотеки и хочу получить современный инструмент «всё в одном» (замена pip, venv, poetry и pyenv).
