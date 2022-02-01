import csv
import sqlite3
import time


class DataReport:
    def __init__(self, csvdata):
        with open(csvdata, 'r') as csvfile:
            data = [d for d in csv.reader(csvfile)]
            self.column = data[0]
            self.data = data[1:]

    def show(self):
        print(self.column)
        print((self.data))

class DB:
    def __init__(self, DataReport):
        self.dr = DataReport
        self.conn = sqlite3.connect("testDB.db")

    def crdbt(self, tname='test00'):
        self.tname = tname
        print(", ".join(d for d in self.dr.column))
        s = f'''CREATE TABLE {tname}({", ".join( f'"{d}"' for d in self.dr.column)});'''
        print(s, 55555)
        try:
            self.conn.cursor().execute(s)
            self.conn.commit()
        except:
            print('crdbt')

    def wrd(self):
        s = ''
        c = 0
        for line in self.dr.data:
            print(line)

            line1 = [f'"{d}"' for d in line]
            # 補""，避免長度不相符
            while len(self.dr.column) > len(line1):
                line1.append('""')
            s2 = ",".join(line1)
            # 單行寫入，寫入效率太差。
            '''
            s2 = ",".join(line1)
            print(s2)
            s += f'INSERT INTO {self.tname} ({s1}) VALUES ({s2});'
            print()
            print(s, "success")
            '''

            '''
                except:
                s = f'INSERT INTO {self.tname} ("{col}") VALUES ("");'
                self.conn.execute(s)
            '''

            if c == 0:
                col = [f'"{l}"' for l in self.dr.column]
                s1 = ",".join(col)
                print(s1)
                s += f'INSERT INTO {self.tname} ({s1}) VALUES ({s2})'
                c += 1
            elif c <= 5000:
                s += f',({s2})'
                c += 1
            else:
                s += f',({s2})'
                self.conn.execute(s)
                self.conn.commit()
                s = ''
                c = 0
        self.conn.execute(s)
        self.conn.commit()

    def dedbt(self, tname='test00'):
        s = f'drop table {tname}'
        try:
            self.conn.execute(s)
        except:
            print('dedbt')

    def search(self, tname='test00'):
        s = f'SELECT * FROM　{tname}'
        self.conn.execute(s)
        print(row for row in self.conn.cursor)
        print(1111122)

csvdata = 'testcsv.csv'
dr = DataReport(csvdata)
# dr.show()

a = time.time()
db = DB(dr)
db.dedbt()
db.crdbt()
db.wrd()
b = time.time()
print('時間', b-a)
# db.dedbt()
# db.search()

