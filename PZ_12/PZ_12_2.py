# Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

s = '--msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"'

result = ''.join(char for char in s if char in string.punctuation)
print(result)
