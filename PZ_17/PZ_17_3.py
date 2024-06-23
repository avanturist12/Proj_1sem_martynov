import os
import random

# I
os.chdir('../PZ_11')

files = [f for f in os.listdir() if os.path.isfile(f)]
print("Список файлов в каталоге PZ11:", files)

# II
os.chdir('../PZ_6')

os.makedirs('test/test1', exist_ok=True)

os.rename('PZ_6/file.txt', 'test/file.txt')
os.rename('PZ_6/file2.txt', 'test/file2.txt')

os.rename('PZ_7/file3.txt', 'test/test1/test.txt')

test_files = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
for file in test_files:
    size = os.path.getsize(os.path.join('test', file))
    print(f"Размер файла {file}: {size} байт")

# III
os.chdir('PZ_11')

shortest_name = min([f for f in os.listdir() if os.path.isfile(f)], key=len)
print("Файл с самым коротким именем:", os.path.basename(shortest_name))

# IV
os.chdir('../reports')

pdf_file = [f for f in os.listdir() if f.endswith('.pdf')]
os.startfile(pdf_file[random.randint(0, len(pdf_file)-1)])

# V
os.chdir('../test/test1')

os.remove('test.txt')
print("Файл test.txt был удален")