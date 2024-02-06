#Дано трехзначное число. Проверить истинность высказывания: "Цифры данного числа образуют возрастную последовательность".
number = input("введите число:")
title = list(number)

status = True

if len(title) == 3:
    for i in number:
        try:
            if int(number[0]) < int(number[1]) and int(number[1]) < int(number[2]):
                continue
            else:
                status = not status
                break
        except:
            status = 3
    else:
        status

    if status == True:
        print("число возрастающее")
    elif not status:
        print("122")
    else:
        print("не число")
