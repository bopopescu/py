#!/usr/bin/python
from mysql.connector import MySQLConnection, Error

from Ejercicio.python_mysql_dbconfig import read_db_config


def insert_persona():
    nombre = input("Introduce un nombre")
    edad = input.int("Introduce una edad")
    print("funciona")
    query = "insert into persona(nombre,edad) " \
            "values (%s,%s)"
    args = (self, nombre, edad)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('Last insert id not found')

        conn.commit()
    except  Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


class DBMethods:
    pass


def main():
    insert_persona()


if __name__ == '__main__':
    main()