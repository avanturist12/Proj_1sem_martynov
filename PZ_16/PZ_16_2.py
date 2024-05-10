# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class figyra:
    def __init__(self, shirina, visota):
        self.shirina = shirina
        self.visota = visota


class prymoygolnik(figyra):
    def __init__(self, shirina, visota):
        super().__init__(shirina, visota)


class kvadrat(figyra):
    def __init__(self, shirina, visota):
        super().__init__(shirina, visota)

    def plohad(self):
        return self.shirina * self.visota

    def perimetr(self):
        return 2 * (self.shirina + self.visota)


kva = kvadrat(5, 5)


def chet(kva):
    print("Площадь квадрата:", kva.plohad())
    print("Периметр квадрата", kva.perimetr())
