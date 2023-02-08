#!/usr/bin/python
# -*- coding: latin-1 -*-

# En este ejercicio, tendr�is que crear un archivo py donde cre�is
# un archivo txt, lo abr�is y escrib�is dentro del archivo.
# Para ello, tendr�is que acceder dos veces a ese archivo.
import os.path as path
nombre = ""


def crear(n):
    if not path.exists(n):
        f = open(n, 'x')
        f.close()


def escribir(n, d):
    f = open(n, 'wt')
    f.write(d)
    f.close()


def pedir_nombre():
    global nombre
    nombre = input('Introduce el nombre del fichero con la extensi�n: ',)
    crear(nombre)


def pedir_datos():
    print('Escribe lo que quieres a�adir al fichero:')
    datos = input()
    escribir(nombre, datos)


def menu():
    option = 1
    while option != 0:
        print()
        print('Menu de opciones')
        print('----------------')
        print('1.- Crear/Abrir Fichero')
        print('2.- Escribir texto en ese fichero')
        print('0.- Salir')
        print()
        option = int(input('Elige una opci�n (0-2): ',))
        if option == 1:
            pedir_nombre()
        elif option == 2:
            if nombre == "":
                print("Debes Crear/Abrir el fichero primero.")
                pedir_nombre()
            pedir_datos()
        elif option == 0:
            break


def main():
    menu()


if __name__ == '__main__':
    main()
