#!/usr/bin/python
# -*- coding: latin-1 -*-


# En este segundo ejercicio, tendr�is que crear un archivo py y dentro crear�is
# una clase Veh�culo, har�is un objeto de ella, lo guardar�is en un archivo
# y luego lo cargamos.

import pickle


class Vehiculo:
    marca = ""
    modelo = ""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'


coche = None
cargado = None


def guardar():
    f = open('vehiculo.dat', 'w+b')
    pickle.dump(coche, f)
    f.close()


def cargar():
    global cargado
    f = open('vehiculo.dat', 'rb')
    cargado = pickle.load(f)
    f.close()


def main():
    global coche
    coche = Vehiculo("Seat", "Leon")
    print(coche)
    guardar()
    cargar()
    print(cargado)


if __name__ == '__main__':
    main()
