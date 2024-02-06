# Дана строка, изображающая целое положительное число. Вывесли сумму цифр этого числа.

while True:

    try:
        integer = input('введите своё число: ')

        if integer == '/quit':
            break
        else:
            integer = int(integer)

    except:
        print('введите целое число')
        break
    else:
        if integer > 0:
            string_integer = str(integer)
            result = 0
            for i in string_integer:
                result += int(i)

            print(f'введенное число: {result}')
        else:
            print('оно не целое')
            break