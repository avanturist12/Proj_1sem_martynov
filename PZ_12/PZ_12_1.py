# Даны текущие оценки студента по дисциплине "Основы програмирования" за
# месяц. Необходимо найти количество "2", "3", "4", "5", полученных студентом, и
# определить итоговую оценку за месяц
import random


def get_arithmetic_mean(args: list[int]) -> int:
    replaced_list = list(dict.fromkeys(args))

    for i in args:
        if i not in replaced_list:
            continue
        else:
            print(f"Всего оценок {i} - {args.count(i)}")
            replaced_list.remove(i)

    return round(sum(args) / len(args))


title = [random.randint(2, 5) for i in range(10)]
print(get_arithmetic_mean(title))
