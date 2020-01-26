from mysql.connector import (connection)


cnx = connection.MySQLConnection(user='root', password='password',
                                 host='127.0.0.1',
                                 database='market')
                                 

cursor = cnx.cursor()

query = ("SELECT * FROM accout")

cursor.execute(query)
