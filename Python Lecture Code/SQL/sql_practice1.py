import sqlite3
conn=sqlite3.connect('mktdata_1.db')
c=conn.cursor()
#create a new table
c.execute('''create table symbol_company(
                Symbol CHAR(10) NOT NULL,
                Company CHAR(10) NOT NULL,
                PRIMARY KEY(Symbol,Company)
            );''')

#saving
conn.commit()

#close
conn.close()
