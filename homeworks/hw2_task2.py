# Проверка доступа к посту

# Данные поста
is_published = True    # опубликован ли пост
is_premium = False   # премиум-контент или нет
text = "Алексей супер нуб в Python"    # содержимое поста

# Данные пользователя
has_subscription = True    # есть ли у пользователя подписка

# Проверяем, есть ли вообще текст (непуская строка)
has_text = bool(text)

# Условие доступа:
# пост виден, если:
#    - есть текст (has_text)
#    - и пост опубликован (is_published)
#    - и (не премиум ИЛИ есть подписка)
can_show = has_text and is_published and (not is_premium or has_subscription)

if can_show:
    print("Пост виден: ")
    print(text)
else:
    print("Пост скрыт")
