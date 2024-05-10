# Создать класс "товар" с атрибутами "название","цена" и "колличество". Напишите метод,
# который выводит информацию о товаре в формате "Название:название, Цена:цена, Колличество: колличество".

class tovar:

    def __init__(self, name, price, kolvo):
        self.name = name
        self.price = price
        self.kolvo = kolvo

    def my_tovar(self):
        print(f"Название: {self.name},"
              f"\nЦена: {self.price}"
              f"\nКолличество: {self.kolvo}")


tovar1 = tovar("Флешка", 1000, 10)
tovar1.my_tovar()

import pickle
with open("User.bin", "wb ")as file:
    pickle.dump(User.file)

with open("User.bin", "rd")as file:
    user = pickle.load(file)

a = User(10, "Max")
a.get values()