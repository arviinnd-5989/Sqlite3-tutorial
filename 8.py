import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''DROP TABLE EMPLOYEE''')

conn.commit()
conn.close()