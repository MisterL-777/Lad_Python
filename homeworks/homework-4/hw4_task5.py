# Задача 5 (звёздочка). Валидация e-mail и телефона без регулярных выражений.
# Используем только методы строк из семинара 4:
# count, split, strip, isdigit, isalpha, endswith, len и оператор in.


def is_valid_email(email: str) -> bool:
    """True, если e-mail похож на корректный (проверка без регулярных выражений).

    Пример:
        is_valid_email("student@example.com") -> True
        is_valid_email("student@example")     -> False
    """
    # 1) Ровно один @ — count считает вхождения подстроки.
    if email.count("@") != 1:
        return False

    # split("@") делит строку на две части: до @ и после @.
    local, domain = email.split("@")

    # 2) Слева и справа от @ есть непробельные символы.
    #    strip() убирает пробелы по краям: если после этого часть пустая —
    #    значит слева/справа от @ ничего осмысленного нет.
    if not local.strip() or not domain.strip():
        return False

    # 3) В доменной части есть точка.
    if "." not in domain:
        return False

    # 4) Домен заканчивается минимум на две буквы.
    #    Берём последние два символа и проверяем, что это буквы.
    if not domain[-2:].isalpha():
        return False

    # 5) Дополнительно (в задании этого нет, но иначе "@ " внутри пройдёт):
    #    пробелов внутри e-mail быть не должно.
    return " " not in email


def is_valid_phone(phone: str) -> bool:
    """True, если телефон в формате +7-XXX-XXX-XX-XX.

    Пример:
        is_valid_phone("+7-999-123-45-67") -> True
    """
    # Разбиваем по дефису: должно получиться ровно 5 частей.
    parts = phone.split("-")
    if len(parts) != 5:
        return False

    # Первая часть — строго код страны +7.
    if parts[0] != "+7":
        return False

    # Остальные части: только цифры и нужной длины (3, 3, 2, 2).
    # zip идёт по двум коллекциям параллельно: часть — её длина.
    for part, length in zip(parts[1:], (3, 3, 2, 2)):
        if not part.isdigit() or len(part) != length:
            return False

    return True


print("=== E-MAIL ===")
emails = [
    "student@example.com",      # True
    "a.b@mail.ru",              # True
    "student@example",          # False: в домене нет точки
    "student@@example.com",     # False: два @
    "@example.com",             # False: слева от @ пусто
    "student@",                 # False: справа от @ пусто
    "student@example.c",        # False: домен не заканчивается на 2 буквы
    "student@example.1",        # False: домен заканчивается цифрой
    "student @example.com",     # False: пробел внутри
]
for email in emails:
    print(f"{email} -> {is_valid_email(email)}")

print("\n=== ТЕЛЕФОН ===")
phones = [
    "+7-999-123-45-67",         # True
    "+7-999-123-45",            # False: 4 части вместо 5
    "+7-999-123-45-678",        # False: последняя часть длиннее двух цифр
    "8-999-123-45-67",          # False: должно быть +7
    "+7-99a-123-45-67",         # False: буква вместо цифры
]
for phone in phones:
    print(f"{phone} -> {is_valid_phone(phone)}")
