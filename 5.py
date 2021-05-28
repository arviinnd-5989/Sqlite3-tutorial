import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''SELECT * FROM EMPLOYEE ORDER BY AGE''')

result = cursor.fetchall();
print(result)

conn.commit()
conn.close()