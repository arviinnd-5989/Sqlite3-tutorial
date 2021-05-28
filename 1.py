import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS CONTACT")

sql = '''CREATE TABLE CONTACT(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    ID INT
)'''
cursor.execute(sql)
print("table created successfully.................")

conn.commit()
conn.close()