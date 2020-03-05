from mysql.connector import MySQLConnection, Error

from Ejercicio.python_mysql_dbconfig import read_db_config


def query_with_fetchone():

    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # cursor.execute("select" + selectString+" from "+fromString+";")
        cursor.execute("select * from persona")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


class Query:
    pass


if __name__ == '__main__':
    query_with_fetchone()
