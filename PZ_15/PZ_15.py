# Приложение УЧЁТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторых
# организации. БД должна содержать таблицу Канцелярия со следующей
# структурой записи: ФИО работника, отдел, вид расхода, сумма.

import sqlite3 as sq

with sq.connect('office_expenses.db') as c:
    con = c.cursor()
    con.execute("DROP TABLE IF EXISTS officeExpenses")
    con.execute("""CREATE TABLE IF NOT EXISTS officeExpenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullName VARCHAR,
                department VARCHAR,
                expenseType VARCHAR,
                amount REAL
                )""")
    c.commit()
    con.close()

def addExpense(fullName, department, expenseType, amount):
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''
    INSERT INTO officeExpenses (fullName, department, expenseType, amount)
    VALUES (?, ?, ?, ?)
    ''', (fullName, department, expenseType, amount))
    con.commit()
    con.close()

addExpense('Иванов И.И.', 'Канцелярия', 'Папир', 1000)
addExpense('Драгунов В.В.', 'Канцелярия', 'Тонер', 500)
addExpense('Менделеев Д.И.', 'Канцелярия', 'Канцелярские товары', 2000)
addExpense('Шелбузов А.И.', 'Канцелярия', 'Папир', 1500)
addExpense('Аванасов Ю.А.', 'Канцелярия', 'Тонер', 1000)
addExpense('Шестаков Д.И.', 'Канцелярия', 'Канцелярские товары', 2500)
addExpense('Гайдай В.Д.', 'Канцелярия', 'Папир', 1200)
addExpense('Макаридзе Д.О.', 'Канцелярия', 'Тонер', 800)
addExpense('Булыгин В.В.', 'Канцелярия', 'Канцелярские товары', 3000)
addExpense('Путин А.В.', 'Канцелярия', 'Папир', 1500)

def findByDepartment(department):
    """Поиск по отделу"""
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''SELECT * FROM officeExpenses WHERE department=?''', (department,))
    result = c.fetchall()
    con.close()
    return result

def findByExpenseType(expenseType):
    """Поиск по виду расхода"""
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''SELECT * FROM officeExpenses WHERE expenseType=?''', (expenseType,))
    result = c.fetchall()
    con.close()
    return result

def findByAmount(amount):
    """Поиск по сумме"""
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''SELECT * FROM officeExpenses WHERE amount=?''', (amount,))
    result = c.fetchall()
    con.close()
    return result

def deleteByNumber(id):
    """Удаление по номеру"""
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''DELETE FROM officeExpenses WHERE id=?''', (id, ))
    con.commit()
    con.close()

def updateByNumber(id, newAmount):
    """Обновление суммы по номеру"""
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('''UPDATE officeExpenses
                 SET amount = ?
                 WHERE id = ?''', (newAmount, id))
    con.commit()
    con.close()

def getExpenses():
    con = sq.connect("office_expenses.db")
    c = con.cursor()
    c.execute('SELECT * FROM officeExpenses')
    return c.fetchall()

for expense in getExpenses():
    print(expense)
