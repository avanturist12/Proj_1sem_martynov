# Из исходного текстового файла (ip_address.txt) из раздела "Зарезервированные адреса" перенести
# в первый файл строки с ненулевым первым и вторым октетами, а во второй - все остальные. Посчитать
# количество полученных строк в каждом файле
import re


def split_ips(ip_file, reserved_file, other_file):
    """
    Разделяет IP-адреса из файла по октетам и записывает их в соответствующие файлы.

    Args:
        ip_file (str): Путь к исходному файлу с IP-адресами.
        reserved_file (str): Путь к файлу для записи зарезервированных IP-адресов.
        other_file (str): Путь к файлу для записи остальных IP-адресов.
    """

    reserved_count = 0
    other_count = 0

    with open(ip_file, "r") as f, open(reserved_file, "w") as reserved_f, open(other_file, "w") as other_f:
        for line in f:
            # Проверка пустой строки
            if not line.strip():
                continue

            # Извлечение IP-адреса с помощью регулярного выражения
            match = re.match(r"^(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}$", line)
            if not match:
                # Обработка некорректного IP-адреса
                print(f"Ошибка: Некорректный IP-адрес: {line}")
                continue

            # Разделение IP-адреса на октеты
            octets = match.groups()

            # Проверка первых двух октетов
            if int(octets[0]) != 0 and int(octets[1]) != 0:
                reserved_f.write(line)
                reserved_count += 1
            else:
                other_f.write(line)
                other_count += 1

            if int(octets[0]) != 0 or int(octets[1]) != 0:
                other_f.write(line)
                other_count += 1
            else:
                print(f"Ошибка: Некорректный IP-адрес: {line}")

    print(f"В файле '{reserved_file}' записано {reserved_count} строк.")
    print(f"В файле '{other_file}' записано {other_count} строк.")


# Пример использования
split_ips("ip_address.txt", "reserved_ips.txt", "other_ips.txt")
