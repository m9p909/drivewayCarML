import sqlite3

con = sqlite3.connect('carml.db')
print("Opened database successfully")

cur = con.cursor()

cur.execute(''' create table images 
(id integer primary key autoincrement,image text not null, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, clean_score integer check(clean_score >= 1 and clean_score <=5 ))''')

con.commit()
con.close()
