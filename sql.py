import sqlite3

# Подключение к базе данных (если она существует) или создание новой базы
db_connection = sqlite3.connect('expenses.db')
db_cursor = db_connection.cursor()

# Создание таблицы пользователей
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        first_name TEXT,
        reg_date DATE
    )
''')

# Создание таблицы возможных расходов
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExpensesList (
        expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense_name TEXT
    )
''')

# Создание таблицы типов расходов и их стоимости
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExpenseTypes (
        expense_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense_id INTEGER,
        expense_type_name TEXT,
        expense_cost REAL,
        FOREIGN KEY (expense_id) REFERENCES ExpensesList(expense_id)
    )
''')

# Закрытие курсора и сохранение изменений
db_connection.commit()
db_cursor.close()
db_connection.close()

print("База данных успешно создана и таблицы добавлены.")
