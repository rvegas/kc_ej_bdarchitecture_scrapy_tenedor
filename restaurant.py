from apartment import *

class Restaurant():
    def __init__(self, pApartamento = Apartment):
        self.__idApartamento = pApartamento.idApartamento()
        self.__idRestaurante = ''
        self.__nombrePais = pApartamento.nombrePais()
        self.__nombreCiudad = pApartamento.nombreCiudad()
        self.__latitud = pApartamento.latitud()
        self.__longitud = pApartamento.longitud()

        

    def idApartamento(self, valor = None):
        if valor == None:
            return self.__idApartamento
        else :
            self.__idApartamento = valor

    def idRestaurante(self, valor = None):
        if valor == None:
            return self.__idRestaurante
        else :
            self.__idRestaurante = valor

    def nombrePais(self, valor = None):
        if valor == None:
            return self.__nombrePais
        else :
            self.__nombrePais = valor

    def nombreCiudad(self, valor = None):
        if valor == None:
            return self.__nombreCiudad
        else :
            self.__nombreCiudad = valor

    def latitud(self, valor = None):
        if valor == None:
            return self.__latitud
        else :
            self.__latitud = valor

    def longitud(self, valor = None):
        if valor == None:
            return self.__longitud
        else :
            self.__longitud = valor

    #def getRestaurantes(self):
