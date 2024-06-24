#Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив символы третей строки их числовыми
#кодами.
with open('text18-22.txt', 'r') as f:
    text = f.read()

print("Original text:")
print(text)

uppercase_count = sum(1 for c in text if c.isupper())
print(f"Uppercase letters: {uppercase_count}")

# Split the text into lines
lines = text.split('\n')

# Replace characters in the third line with their numerical codes
third_line_chars = [str(ord(c)) for c in lines[2]]
lines[2] = ' '.join(third_line_chars)

# Join the lines back into a single string
poetic_text = '\n'.join(lines)

# Write the poetic text to a new file
with open('poetic_text.txt', 'w',encoding='utf-8') as f:
    f.write(poetic_text)

print("Poetic text written to poetic_text.txt")