#!/usr/bin/python

from Ejercicio.DBMethods import insert_persona as insertar
from Ejercicio.Query import query_with_fetchone as get

def Addpersona():

    insertar()
    print(2)
    ShowMenu()


def ShowPersonajes():
    get()
    ShowMenu()


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
    if sel == 1:
        ShowPersonajes()
    if sel == 2:
        Addpersona()
    # if sel == 3:

    ShowMenu()


def main():
    ShowMenu()


if __name__ == '__main__':
    main()
