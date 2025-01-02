def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        total = 0
        count = 0
        
        for line in lines:
            # Видаляємо пробіли та перенос рядка
            line = line.strip()
            if not line:
                continue  # Пропускаємо порожні рядки
            try:
                _, salary = line.split(',')
                total += int(salary)
                count += 1
            except ValueError:
                print(f"Помилка обробки рядка: {line}")
        
        if count == 0:
            return 0, 0  # Якщо немає даних
        
        average = total / count
        return total, average
    
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

# Приклад використання
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
