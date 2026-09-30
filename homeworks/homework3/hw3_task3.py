# Оценки по порогам
grades = [95, 88, 60, 42, 100]

for grade in grades:
    if grade >= 90:
        verdict = "отлично"
    elif grade >= 70:
        verdict = "хорошо"
    elif grade >= 50:
        verdict = "удовлетворительно"
    else:
        verdict = "неудовлетворительно"

    print(f"{grade}: {verdict}")