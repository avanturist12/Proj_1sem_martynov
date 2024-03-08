#Дана строка"апельсины 45 991 100 12 яблоки 13 47 26 0 16",
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти  максимальные продажи по
#каждому виду продукции, результаты вывести на экран.

def get_max_value(string: str):
    current_item = str
    title = string.split()
    _dict = {}

    for i in title:
        if not i.isdigit():
            current_item = i
            _dict[current_item] = []
        else:
            _dict[current_item].append(int(i))

    for k, v in _dict.items():
        print(k, max(v), sep=": ")


if __name__ == "__main__":
    string = "апельсины  45 991 100 12 яблоки 13 47 26 0 16"
    get_max_value(string)