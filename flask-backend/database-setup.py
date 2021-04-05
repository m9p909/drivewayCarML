import sqlite3

con = sqlite3.connect('carml.db')
print("Opened database successfully")

cur = con.cursor()

cur.execute(''' create table images 
(id integer primary key autoincrement,image blob not null, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, numcars integer check(numcars >= 0 and numcars <=4 ))''')

con.commit()