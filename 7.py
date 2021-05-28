import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''SELECT * FROM EMPLOYEE''')

result = cursor.fetchall();
print(result)

cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE >25''')
print("Contents after deletion")
cursor.execute("SELECT * FROM EMPLOYEE")
print(cursor.fetchall())

conn.commit()
conn.close()