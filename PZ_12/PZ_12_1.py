# Даны текущие оценки студента по дисциплине "Основы програмирования" за
# месяц. Необходимо найти количество "2", "3", "4", "5", полученных студентом, и
# определить итоговую оценку за месяц

otsenki = int(input("какие отценки получал студент?"))

grades_count = {5: 0, 4: 0, 3: 0, 2: 0}
for otsenki in otsenki:
    grades_count[otsenki] += 1

for otsenki, count in grades_count.items():
    print(f'Оценка "{otsenki}": {count} шт.')

final_grade = grades_count.get(2, 0) * 2 + grades_count.get(3, 0) * 3 + grades_count.get(4, 0) * 4 + grades_count.get(5, 0) * 5
print(f'Итоговая оценка за месяц: {final_grade}')