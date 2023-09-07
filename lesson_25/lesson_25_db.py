import sqlite3

con = sqlite3.connect('Gurkinita.db')
cursor = con.cursor()

# Создание таблицы TopModels, если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS TopModels (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        nationality TEXT,
        earnings REAL,
        height INTEGER
    )
''')

cursor.execute("INSERT INTO TopModels (name, age, nationality, earnings, height) VALUES (?, ?, ?, ?, ?)",
               ("Adriana Lima", 40, "Brazilian", 10.5, 177))

cursor.execute("INSERT INTO TopModels (name, age, nationality, earnings, height) VALUES (?, ?, ?, ?, ?)",
               ("Candice Swanepoel", 33, "South African", 9.0, 180))

cursor.execute("INSERT INTO TopModels (name, age, nationality, earnings, height) VALUES (?, ?, ?, ?, ?)",
               ("Alessandra Ambrosio", 40, "Brazilian", 9.5, 175))

con.commit()
con.close()
