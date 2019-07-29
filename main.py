import config as cfc
import csv
from apartment import *

def main():
    miApartamento = None
    listaApartamentos = []

    with open(cfc.csvpath) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            miApartamento = Apartment(pId = row[0], pCodPosta = row[40], pProvincia = row[39], pCiudad = row[38], 
                pCodPais = row[43], pNombrePais = row[44], pLatitud = row[45], pLongitud = row[45])

            listaApartamentos.append(miApartamento)

if __name__ == "__main__":
    main()
        