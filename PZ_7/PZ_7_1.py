# Дана строка, изображающая целое положительное число. Вывесли сумму цифр этого числа.

while True:

    try:
        integer = input('Input your integer number: ')

        if integer == '/quit':
            break
        else:
            integer = int(integer)

    except:
        print('You input other symbols, but this is not integer nubmer!')
        break
    else:
        if integer > 0:
            string_integer = str(integer)
            result = 0
            for i in string_integer:
                result += int(i)

            print(f'The sum of the digits of this number will be {result}')
        else:
            print('This is not integer')
            break