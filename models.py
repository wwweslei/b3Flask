from mysql.connector import errorcode
import mysql.connector
import config


try:
    cnx = mysql.connector.connect(**config.config_db)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
cursor = cnx.cursor()


def query_view_position():
    query_view = ("select * from market.position")
    cursor.execute(query_view)
    cnx.close()
    return [list(position) for position in cursor]


def query_view_position_date():
    query_view = ("select * from market.position_date")
    cursor.execute(query_view)
    cnx.close()
    return [list(position) for position in cursor]


if __name__ == "__main__":
    # print(query_view_position())
    print(query_view_position_date())
