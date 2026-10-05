# Поиск по блогу

def build_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")
    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    return result.strip("-")


posts = [
    "Как настроить Django под продакшен",
    "Python и Django: с чего начать",
    "Почему Python любят backend-разработчики",
    "Введение в REST API",
    "Ошибки новичков в Python!",
]

print("=== ПОСТЫ ПРО PYTHON ===")

found = 0

for title in posts:
    if "Python" in title:
        found += 1
        print(title)
        print(f"  slug: {build_slug(title)}")

print(f"\nНайдено постов про Python: {found}")