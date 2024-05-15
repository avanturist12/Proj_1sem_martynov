# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figyra:
    def __init__(self, shirina, visota):
        self.shirina = shirina
        self.visota = visota

    def Plohad(self):
        return self.shirina * self.visota

    def Perimetr(self):
        return 2 * (self.shirina + self.visota)


class Prymoygolnik(Figyra):
    def __init__(self, shirina, visota):
        super().__init__(shirina, visota)


class Kvadrat(Figyra):

    def __init__(self, shirina, visota):
        super().__init__(shirina, visota)


kva = Kvadrat(5, 5)


def chet(kva):
    print("Площадь квадрата:", kva.Plohad())
    print("Периметр квадрата:", kva.Perimetr())


chet(kva)
