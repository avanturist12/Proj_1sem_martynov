"""
Разработать программу с применением пакета tk, взяв в качестве условия одну
любую задачу из ПЗ №№ 2 – 9.
"""
import tkinter as tk
from tkinter import messagebox

def check():

        try:
            A = int(entry.get())
            if A < 1000:
                result = f"Число {A} неправельное число"
            else:
                y = A // 100
                A = y % 10
                result = f"Число {A} соответствует разряду сотен"
                messagebox.showinfo("Результат", result)
        except ValueError:
            print("Вы ввели не то, что нужно. Пожалуйста, попробуйте ещё раз!\n")


root = tk.Tk()
root.title("Проверка чётности числа")

label = tk.Label(root, text="Введите число более 999:")
label.pack(pady=10, padx=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Проверить", command=check)
button.pack(pady=20)

root.mainloop()