# Даны текущие оценки студента по дисциплине "Основы програмирования" за
# месяц. Необходимо найти количество "2", "3", "4", "5", полученных студентом, и
# определить итоговую оценку за месяц

from random import randint


def student(grades):
    o_2 = grades.count(2)
    o_3 = grades.count(3)
    o_4 = grades.count(4)
    o_5 = grades.count(5)
    return o_2, o_3, o_4, o_5


otsenki = []
for i in range(10):
    otsenki.append(randint(2, 5))
o_2, o_3, o_4, o_5 = student(otsenki)

print("Количество оценок '2':", o_2)
print("Количество оценок '3':", o_3)
print("Количество оценок '4':", o_4)
print("Количество оценок '5':", o_5)

sr = sum(otsenki) / len(otsenki)

if sr >= 4.5:
    print("Итоговая оценка за месяц: 5")
elif sr >= 3.5:
    print("Итоговая оценка за месяц: 4")
elif sr >= 2.5:
    print("Итоговая оценка за месяц: 3")
else:
    print("Итоговая оценка за месяц: 2")
