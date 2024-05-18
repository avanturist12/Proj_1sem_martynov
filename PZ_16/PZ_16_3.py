# Для задачи из блока 1 создать две функции, save_dev,и load_dev, которые позволяют
# сохранять информацию из экземпляров класса (3шт.) в файл и загрушать её обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

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
def save_dev():
    with open("User.bin", "wb ")as file:
        pickle.dump(save_dev.tovar)

def load_dev():
    with open("User.bin", "rd")as file:
        user = pickle.load(tovar)

a = save_dev(10, "Max")
a.get. load_dev()