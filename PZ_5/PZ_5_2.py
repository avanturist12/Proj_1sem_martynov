# Описать функцию Mean(X,Y, AMean, GMean), вычисляющую среднее
# арифметическое AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух
# положительных чисел X и Y (X и Y - входные, AMean B GMean - выходные 
# параметры вещественного типа). С помщью этой функции найти среднее 
# арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
# A, B, C, D.
def mean(x, y):
    if x > 0 and y > 0:
        a_mean: float = float((x + y) / 2)
        g_mean = float(y / x * y)

        return a_mean, g_mean
    else:
        return "You must use only positive numbers to get the result"


try:
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    c = int(input("Input c: "))
    d = int(input("Input d: "))

    print(mean(a, b))
    print(mean(a, c))
    print(mean(a, d))
except:
    print('You must be input integer numbers!')
