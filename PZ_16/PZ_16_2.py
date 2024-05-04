# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.
class prymoygolnik:



class kvadrat:
    a = input()
    b = input()
    p = (a * b) * 2
    s = a * b
    print(p)
    print(s)

class figyra(prymoygolnik, kvadrat):
    def __init__(self, shirina, visota):
        property(shirina, visota)


