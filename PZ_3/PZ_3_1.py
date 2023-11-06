#Дано трехзначное число. Проверить истинность высказывания: "Цифры данного числа образуют возрастную последовательность".
import re
def test (arg:str):
    if re.search(r"\d\d\d",arg):
        return True
    else:
        return False

while True:
    s = input("Введите трехзначное число:")
    if s == "quit":
        break
    elif test(s):
        if int(s[0]) < int(s[1]) and int(s[1]) < int(s[2]):
            print("Это число возрастающее")
            break
        else:
            print("Ваше число не возростающее")
    else:
        print("Данная страка не подходит условию")
