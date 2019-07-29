class Apartment():
    def __init__(self, pId, pCodPosta, pProvincia, pCiudad, pCodPais, pNombrePais, pLatitud, pLongitud):
        self.__idApartamento = pId
        self.__codPostal = pCodPosta
        self.__nombreProvincia = pProvincia
        self.__nombreCiudad = pCiudad
        self.__codPais = pCodPais
        self.__nombrePais = pNombrePais
        self.__latitud = pLatitud
        self.__longitud = pLongitud

    def idApartamento(self, valor = None):
        if valor == None:
            return self.__idApartamento
        else :
            self.__idApartamento = valor
        
    def codPostal(self, valor = None):
        if valor == None:
            return self.__codPostal
        else :
            self.__codPostal = valor

    def nombreProvincia(self, valor = None):
        if valor == None:
            return self.__nombreProvincia
        else :
            self.__nombreProvincia = valor

    def nombreCiudad(self, valor = None):
        if valor == None:
            return self.__nombreCiudad
        else :
            self.__nombreCiudad = valor

    def codPais(self, valor = None):
        if valor == None:
            return self.__codPais
        else :
            self.__codPais = valor

    def nombrePais(self, valor = None):
        if valor == None:
            return self.__nombrePais
        else :
            self.__nombrePais = valor

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