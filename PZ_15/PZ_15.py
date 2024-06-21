# Приложение УЧЁТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторых
# организации. БД должна содержать таблицу Канцелярия со следующей
# структурой записи: ФИО работника, отдел, вид расхода, сумма.

import tkinter as tk
from tkinter import messagebox
import sqlite3

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.conn = sqlite3.connect("office_expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Канцелярия (
                ФИО_работника TEXT,
                отдел TEXT,
                вид_расхода TEXT,
                сумма REAL
            );
        """)
        self.conn.commit()

        self.fio_label = tk.Label(self, text="ФИО работника")
        self.fio_label.pack(side="top")

        self.fio_entry = tk.Entry(self)
        self.fio_entry.pack(side="top")

        self.otdel_label = tk.Label(self, text="Отдел")
        self.otdel_label.pack(side="top")

        self.otdel_entry = tk.Entry(self)
        self.otdel_entry.pack(side="top")

        self.vid_rashoda_label = tk.Label(self, text="Вид расхода")
        self.vid_rashoda_label.pack(side="top")

        self.vid_rashoda_entry = tk.Entry(self)
        self.vid_rashoda_entry.pack(side="top")

        self.summa_label = tk.Label(self, text="Сумма")
        self.summa_label.pack(side="top")

        self.summa_entry = tk.Entry(self)
        self.summa_entry.pack(side="top")

        self.add_button = tk.Button(self)
        self.add_button["text"] = "Добавить расход"
        self.add_button["command"] = self.add_rashod
        self.add_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_rashod(self):
        fio = self.fio_entry.get()
        otdel = self.otdel_entry.get()
        vid_rashoda = self.vid_rashoda_entry.get()
        summa = self.summa_entry.get()

        if fio and otdel and vid_rashoda and summa:
            try:
                summa = float(summa)
                self.cursor.execute("""
                    INSERT INTO Канцелярия (ФИО_работника, отдел, вид_расхода, сумма)
                    VALUES (?, ?, ?, ?);
                """, (fio, otdel, vid_rashoda, summa))
                self.conn.commit()
                messagebox.showinfo("Успешно", "Расход добавлен")
                self.fio_entry.delete(0, tk.END)
                self.otdel_entry.delete(0, tk.END)
                self.vid_rashoda_entry.delete(0, tk.END)
                self.summa_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Ошибка", "Сумма должна быть числом")
        else:
            messagebox.showerror("Ошибка", "Все поля должны быть заполнены")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
