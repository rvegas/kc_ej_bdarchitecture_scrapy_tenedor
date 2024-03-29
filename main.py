import config as cfc
import csv
from apartment import *
from restaurant import *

def main():
    miApartamento = None
    listaApartamentos = []
    i = 0

    with open(cfc.csvpath) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        for row in reader:
            if i > 0:
                miApartamento = Apartment(pId = row[0], pCodPosta = row[40], pProvincia = row[39], pCiudad = row[38], 
                    pCodPais = row[43], pNombrePais = row[44], pLatitud = row[45], pLongitud = row[46])

                listaApartamentos.append(miApartamento)

            i += 1

    # Una vez tenemos la lista de apartamentos, la filtramos si así está configurado
    if cfc.filtroPais != '*':
        listaApartamentos = [x for x in listaApartamentos if x.codPais() == cfc.filtroPais]

    # Obtenemos los datos de la app El Tenedor
    i = 0
    for ap in listaApartamentos:
        if i == 0:
            miRest = Restaurant()
            miRest.setData(pApartamento=ap)
            miRest.empieza()

        i += 1

if __name__ == "__main__":
    main()
        