#!/usr/bin/python
from mysql.connector import MySQLConnection, Error

from Ejercicio.Query import query_with_fetchone as showTable
from Ejercicio.python_mysql_dbconfig import read_db_config


def insert_persona():
    nombre = input("Introduce un nombre")
    edad = input("Enter your Age")
    try:
        edad = int(edad)

        query = "insert into persona(name,edad) " \
                "values (%s,%s)"
        args = (nombre, edad)

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



    except ValueError:
        print("No.. input is not a number. It's a string")


def DeleteById():
    showTable()
    id = input("Introduce una id")
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # cursor.execute("select" + selectString+" from "+fromString+";")
        cursor.execute("delete from persona where id = " + id)
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
#TODO modificar  la query
def UpdateById(id):
    showTable()

    try:
        nombre = input("Introduce el nuevo nombre")
        age = input("Introduce la edad")
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # cursor.execute("select" + selectString+" from "+fromString+";")
        cursor.execute("update persona "
                       "set name= nombre , set edad = age  where id = " + id)
        conn.commit()
    except Error as error:
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
