import json

from mongoengine.errors import NotUniqueError

from models import Author, Quote



# Завантажуємо дані
with open('authors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for el in data:
    fullname = el.get('fullname')
    if not fullname:  # пропускаємо порожні записи
        continue

    # Шукаємо автора
    author = Author.objects(fullname=fullname).first()
    if author:
        print(f"Автор {fullname} вже існує")
        continue

    # Створюємо нового автора
    author = Author(
        fullname=fullname,
        born_date=el.get('born_date', ''),
        born_location=el.get('born_location', ''),
        description=el.get('description', '')
    )
    author.save()
    print(f"Автор {fullname} доданий")