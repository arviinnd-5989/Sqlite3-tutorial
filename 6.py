import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = 'M' ''')

cursor.execute('''SELECT * FROM EMPLOYEE''')

result = cursor.fetchall();
print(result)

conn.commit()
conn.close()