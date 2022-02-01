import sqlite3 as lite
import csv
class DB:
    def __init__(self, *args):
        self.args = args
        # 連接資料庫
        self.conn = lite.connect('testDB.db').cursor()

    def __str__(self):
        return "123"

    def createtb(self, data):
        if data[0][0] == 'Index':
            try:
                self.conn.execute('DROP TABLE DDD;')
            except:
                pass
            self.conn.execute('CREATE TABLE DDD(ID INTEGER);')
            for col in data[0]:
                print(col)
                self.conn.execute(f'Alter TABLE DDD Add "{col}" text;')


            sql_str =\
            f'''
            CREATE TABLE DDD
            '''
    def show(self):
        command = "select * from DDD"
        a = self.conn.execute(command)
        return (self.conn.fetchall())



with open("testcsv.csv", 'r') as csvfile:
    rows = csv.reader(csvfile)
    data = [row for row in rows]

db = DB(1, 32)
print(data[0])
print(db.createtb(data))
print(db.show())

