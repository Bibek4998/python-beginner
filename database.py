import sqlite3
conn=sqlite3.connect("test.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, AGE INTEGER NOT NULL)")
cursor.execute("INSERT INTO USERS (NAME, AGE) VALUES (?,?)", ('Bibek', 16))
conn.commit()
def view():
    cursor.execute("SELECT * FROM USERS")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
view()
