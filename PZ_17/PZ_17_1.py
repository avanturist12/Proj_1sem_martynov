import tkinter as tk
from tkinter import ttk

# Функция для обработки нажатия кнопки "Данные подтверждаю"
def submit():
    print("Данные подтверждены")

# Функция для обработки нажатия кнопки "Отменить ввод"
def cancel():
    root.destroy()

# Создаем главное окно
root = tk.Tk()
root.title("Форма")

# Метки и поля ввода для имени
tk.Label(root, text="Ваше имя:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Метки и поля ввода для пароля
tk.Label(root, text="Пароль:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Метки и поля ввода для возраста
tk.Label(root, text="Возраст:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Радиокнопки для выбора пола
tk.Label(root, text="Пол:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Мужской", variable=gender_var, value="Мужской").grid(row=3, column=1, sticky=tk.W)
tk.Radiobutton(root, text="Женский", variable=gender_var, value="Женский").grid(row=3, column=2, sticky=tk.W)

# Флажки для выбора увлечений
tk.Label(root, text="Ваши увлечения:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
music_var = tk.BooleanVar()
video_var = tk.BooleanVar()
drawing_var = tk.BooleanVar()
tk.Checkbutton(root, text="Музыка", variable=music_var).grid(row=4, column=1, sticky=tk.W)
tk.Checkbutton(root, text="Видео", variable=video_var).grid(row=4, column=2, sticky=tk.W)
tk.Checkbutton(root, text="Рисование", variable=drawing_var).grid(row=4, column=3, sticky=tk.W)

# Выпадающие списки для выбора страны и города
tk.Label(root, text="Ваша страна:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
country_var = tk.StringVar()
country_combo = ttk.Combobox(root, textvariable=country_var)
country_combo['values'] = ("Country1", "Country2", "Country3")  # Здесь замените на реальные значения
country_combo.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Ваш город:").grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
city_var = tk.StringVar()
city_combo = ttk.Combobox(root, textvariable=city_var)
city_combo['values'] = ("City1", "City2", "City3")  # Здесь замените на реальные значения
city_combo.grid(row=6, column=1, padx=10, pady=5)

# Поле для краткого описания о себе
tk.Label(root, text="Кратко о себе:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
about_text = tk.Text(root, width=30, height=5)
about_text.grid(row=7, column=1, columnspan=3, padx=10, pady=5)

# Метка и поле ввода для решения примера
tk.Label(root, text="Решите пример, запишите результат в поле ниже:").grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
example_entry = tk.Entry(root)
example_entry.grid(row=8, column=1, padx=10, pady=5)

# Кнопки "Данные подтверждаю" и "Отменить ввод"
submit_button = tk.Button(root, text="Данные подтверждаю", command=submit)
submit_button.grid(row=9, column=2, padx=10, pady=10)

cancel_button = tk.Button(root, text="Отменить ввод", command=cancel)
cancel_button.grid(row=9, column=1, padx=10, pady=10)

# Запуск главного цикла обработки событий
root.mainloop()