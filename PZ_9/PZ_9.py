# Дана строка"апельсины 45 991 100 12 яблоки 13 47 26 0 16",
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти  максимальные продажи по
# каждому виду продукции, результаты вывести на экран.

data = "апельсины 45 991 100 12 яблоки 13 47 26 0 16"

# Разделение строки на отдельные слова и числа
items = data.split()

# Создание словаря
dict_data = {}
current_item = None

for item in items:
    # Если слово является названием продукта
    if not item.isdigit():
        current_item = item
        dict_data[current_item] = []
    else:
        # Добавление значения продажи в текущий список продаж продукта
        dict_data[current_item].append(int(item))

# Нахождение максимальных продаж по каждому продукту и вывод результатов
for item, sales in dict_data.items():
    max_sales = max(sales)
    print(f"Максимальные продажи {item}: {max_sales}")
