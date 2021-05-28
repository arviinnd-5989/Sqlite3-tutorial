import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''SELECT * FROM EMPLOYEE INNER JOIN CONTACT ON EMPLOYEE.FIRST_NAME = CONTACT.FIRST_NAME''')

result = cursor.fetchall();
print(result)
conn.commit()
conn.close()