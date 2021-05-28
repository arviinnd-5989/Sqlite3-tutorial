import sqlite3
conn = sqlite3.connect('example.db')

cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# cursor.execute('''CREATE TABLE EMPLOYEE(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT
# )''')

cursor.execute('''INSERT INTO CONTACT(FIRST_NAME, LAST_NAME, ID)
 VALUES ('RAMYA','RAMA PRIYA',12345)''')

# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#    VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')

# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#    VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')

# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#    VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')

# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
#    VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')
# print("table created successfully.................")

conn.commit()

print("Records inserted......................")
conn.close()