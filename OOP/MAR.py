#class Car:
#       print("Машина стоит")

#my_car = Car()
#my_car1 = Car()

#my_car.move()
#my_car.stop()

# print(type(my_car))
# print(isinstance(my_car, Car))
# print(isinstance(my_car, object))
# print(my_car == my_car1)
# print(id(my_car), id(my_car1))

class Note:
    def __init__(self, iscompleted):
        self.iscompleted = 0

    def reset_coint(self,reset_task):
        self.reset = 1

 #   def upcount(self):
 #       self.count += 1



note3 = Note("для задачи")
#note1 = Note("Задача 1")
#note2 = Note("Задача 2")
#print(note1.__dict__)
#print(dir(note1))
#print()
print(note3.__dict__)
#note1.upcount()
#print(note1.count)
#note2.upcount()
#print(note2.count)



#print(note1.upcount)
#print(Note.upcount)





