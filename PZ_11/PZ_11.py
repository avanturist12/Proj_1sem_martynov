# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма положительных элементов:


# Create two text files with sequences of integers
with open("file1.txt", "w") as f:
    f.write("1 2 3 4 5 6 7 8 9 10")

with open("file2.txt", "w") as f:
    f.write("-1 -2 -3 -4 -5 -6 -7 -8 -9 -10")

# Read the files and process the data
with open("file1.txt", "r") as f:
    seq1 = [int(x) for x in f.read().split()]

with open("file2.txt", "r") as f:
    seq2 = [int(x) for x in f.read().split()]

# Calculate the required statistics
even1 = [x for x in seq1 if x % 2 == 0]
even2 = [x for x in seq2 if x % 2 == 0]
odd1 = [x for x in seq1 if x % 2 != 0]
odd2 = [x for x in seq2 if x % 2 != 0]
avg1 = sum(seq1) / len(seq1)
avg2 = sum(seq2) / len(seq2)
pos2 = [x for x in seq2 if x > 0]

# Create the new file
with open("result.txt", "w") as f:
    f.write("Pervuy fail:\n")
    f.write(" ".join(map(str, seq1)) + "\n")
    f.write("chetnye elementy:\n")
    f.write(" ".join(map(str, even1)) + "\n")
    f.write("kol-vo chetnye elementov: {}\n".format(len(even1)))
    f.write("crednee arifmeticheskoe: {}\n".format(avg1))
    f.write("\nSoderjimoe 2 faila:\n")
    f.write(" ".join(map(str, seq2)) + "\n")
    f.write("nechetnye elementy:\n")
    f.write(" ".join(map(str, odd2)) + "\n")
    f.write("kol-vo nechetnyx elementov: {}\n".format(len(odd2)))
    f.write("symma polojitelnyx elementov: {}\n".format(sum(pos2)))
