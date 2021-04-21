import sqlite3

con = sqlite3.connect('carml.db')
print("Opened database successfully")

cur = con.cursor()

cur.execute('''
 create table images2 (
    id integer primary key autoincrement,
    image text not null, 
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    objects_on_counter integer,
    is_sink_empty boolean, 
    cupboards_open integer
    );
''')

cur.execute('''
    insert into images2 (id, image, timestamp)
        select id, image, timestamp from images;
    ''')

cur.execute("drop table images;")
cur.executescript("alter table images2 rename to images;")


con.commit()
con.close()
