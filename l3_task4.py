posts = {
    "теория взрыва",
    "новая генетика",
    "анатомия страсти",
}
print("Свежие посты")


for number, title in enumerate(posts, start=1):
    print(f"{number}. {title}")

print("\nКарточка  статьи")
for title in posts:
    print(f"{title} - {len(title)} символов")

print("\nПоиск")
if "новая генетика" in posts:
    print("Пост про 'новая генетика' есть в списке")
else:
    print("Такой статьи нет")