#!/usr/bin/python

import time

from Ejercicio.DBMethods import DeleteById as delete
from Ejercicio.DBMethods import UpdateById as update
from Ejercicio.DBMethods import insert_persona as insertar
from Ejercicio.Query import query_with_fetchone as get


def Addpersona():
    insertar()
    print(2)
    ShowMenu()


def ShowPersonajes():
    get()


def ShowMenu():
    print("#################################################################")
    print("#####################Star wars pedia#############################")
    print("#################################################################")
    print("######################Creado por Daniel C########################")
    print("#################################################################")
    sel = input("Seleccione una opcion\n"
                "1) Mostrar todos los personajes \n"
                "2) Añadir Personaje"
                "3) Eliminar Personaje\n"
                "4) Modificar Personaje\n"
                "5) Salir\n"
                "#################################################################\n"
                "#################################################################\n")
    print(sel)
    if sel == "1":
        ShowPersonajes()
        print("hola?")
    if sel == "2":
        insertar()
    if sel == "3":
        delete()
        ShowPersonajes()
        time.sleep(10)
        ShowMenu()
    if sel == "4":
        ShowPersonajes()
        id = input("Introduce la id del Personaje a modificar")
        update(id)


ShowMenu()


def main():
    ShowMenu()


if __name__ == '__main__':
    main()
