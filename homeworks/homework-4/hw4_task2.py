# Красивый заголовок

dirty_text = "     чем больше     'работаешь' ,    тем мешьше   'получаешь'!!!!  "

clean_string = dirty_text.replace("'", "").replace(",", "").replace("!", "")    # Убираем знаки

words = clean_string.split()     # Переводим очищенную строку в список слов

capitalized_words = []     # Капитализируем в цикле
for word in words:
    capitalized_words.append(word.capitalize())

clean_text = " ".join(capitalized_words)   # Собираем обратно

print(clean_text)
