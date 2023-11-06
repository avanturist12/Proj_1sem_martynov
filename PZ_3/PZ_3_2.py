#Даны два числа, выведите большее из них
print("Введите два числа:")
while True:
    try:
        a, b = input(), input()
        if int(a) > int(b):
            print("Число " + a + " больше", sep=" ")
            break
        else:
            print("Число " + b + " больше", sep=" ")
            break
    except ValueError:
           print("Это не число, попробуйте число:")
