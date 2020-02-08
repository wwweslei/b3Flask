from mysql.connector import errorcode
import mysql.connector
from collections import namedtuple


config = {
    'user': 'root',
    'password': 'password',
    'database': 'market',
    'raise_on_warnings': True,
    'auth_plugin': 'mysql_native_password'
}

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
cursor = cnx.cursor()


def position():
    positions = namedtuple(
        'positions', ['id', 'ticket', 'amount', 'average', 'total'])
    query = ("select * from market.position")
    cursor.execute(query)
    # cursor.close()
    cnx.close()
    return [positions._make(ticket) for ticket in cursor]


if __name__ == "__main__":
    print(position())
