users = {"Илья", "Ксения", "Алексей", "Михаил"}
scores = {97, 88, 73}

print("Список участников:")
for number, name in enumerate(users, start=1):
    print(f"{number}. {name}")

print("Результаты по паре: имя, оценка")
for name, score in zip(users, scores):
    print(f"{name}: {score}")