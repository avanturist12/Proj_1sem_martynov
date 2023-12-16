# Найти сумму чисел ряда 1,2,3,4,...,60 с использованием функции нахождения суммы.
# Использовать локальные переменные
def get_sum():
    result = 0
    for i in range(1, 60):
        result += i

    return result


print(get_sum())
