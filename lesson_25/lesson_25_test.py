import sqlite3

con = sqlite3.connect('Gurkinita.db')
cursor = con.cursor()


cursor.execute("INSERT INTO TopModels (name, height) VALUES ('Alessandra', 177)")


cursor.execute("UPDATE TopModels SET height = 180 WHERE name = 'Alessandra'")


cursor.execute("DELETE FROM TopModels WHERE name = 'Alessandra'")

con.commit()


cursor.execute("SELECT * FROM TopModels")


result = cursor.fetchall()
print(result)


for row in result:
    print(row)

con.close()
