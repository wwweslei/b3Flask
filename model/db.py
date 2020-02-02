import datetime
import mysql.connector
from collections import namedtuple

class Db:
    def __init__(self):
        self.cnx = mysql.connector.connect(
        user='root', password='password', database='market')
        self.cursor = self.cnx.cursor()
    
    def closeDb(self):
        self.cursor.close()
        self.cnx.close()

    def position(self):
        self.positions = namedtuple('positions', ['id', 'ticket', 'amount', 'average', 'total'])
        self.query = ("select * from market.position")
        self.cursor.execute(self.query)
        self.closeDb
        return [self.positions._make(x) for x in self.cursor]
        

if __name__ == "__main__":
    db = Db()
    print(db.position())

