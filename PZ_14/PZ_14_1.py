# Из исходного текстового файла (ip_address.txt) из раздела "Зарезервированные адреса" перенести
# в первый файл строки с ненулевым первым и вторым октетами, а во второй - все остальные. Посчитать
# количество полученных строк в каждом файле
import re


def process_ip_addresses(filename):

    with open(filename, "r") as file:
        lines = file.readlines()

    non_zero_ips = []
    zero_ips = []
    count_non_zero = 0
    count_zero = 0

    for line in lines:
        match = re.search(r"\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/", line)
        if match:
            ip_address = match.group(1)
            first_octet, second_octet = map(int, ip_address.split(".")[0:2])
            if first_octet != 0 and second_octet != 0:
                non_zero_ips.append(line)
                count_non_zero += 1
            else:
                zero_ips.append(line)
                count_zero += 1

    with open("non_zero_ips.txt", "w") as f:
        f.writelines(non_zero_ips)
    with open("zero_ips.txt", "w") as f:
        f.writelines(zero_ips)

    print(f"Количество строк с ненулевыми октетами: {count_non_zero}")
    print(f"Количество строк с нулевыми или пустыми октетами: {count_zero}")


process_ip_addresses("ip_address.txt")