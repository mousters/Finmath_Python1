class cursor:
    def __init__(self):
        self.queries=[]
    def execute(self,string):
        self.queries.append(string)

class connection:
    def __init__(self):
        self.committed = False
        self.closed = False
        self.curs = None

    def cursor(self):
        print("commited:" + str(self.committed))
        print("commited:" + str(self.closed))
        self.curs=cursor()
        return self.curs

    def commit(self):
        print("commited:" + str(self.committed))
        print("commited:" + str(self.closed))
        self.committed = True

    def close(self):
        print("commited:" + str(self.committed))
        print("commited:" + str(self.closed))
        self.closed = True

    def status(self):
        print("commited:" + str(self.committed))
        print("commited:" + str(self.closed))
        for q in self.curs.queries:
            print(q)



class sqlite3:
    @staticmethod
    def connect(dbfile):
        return connection()

conn=sqlite3.connect('mktdata_1.db')
c=conn.cursor()
c.execute('''create table students(
Id INTEGER NOT NULL,
Student CHAR(10) NOT NULL,
Grade REAL NOT NULL,
PRIMARY KEY(Id)
);''')
#conn.commit()
# Write the code here
c.execute("insert into students values (1,'Donald',10)")
c.execute("insert into students values (2,'Pluto',5)")
c.execute("insert into students values (3,'Mick',15)")
conn.commit()
conn.close()

conn.status()