def get_cats_info(path):
    try:
        cats = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Видаляємо зайві пробіли та розділяємо рядок за комою
                parts = line.strip().split(',')
                if len(parts) == 3:  # Перевірка на валідність даних
                    cat_id, name, age = parts
                    # Створюємо словник для кожного кота
                    cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання
cats_info = get_cats_info("cats.txt")
print(cats_info)
