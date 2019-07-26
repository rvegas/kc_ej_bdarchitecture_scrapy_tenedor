import config as cfc
import csv

with open(cfc.csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=';')

    for row in reader:
        print(row[0]) # ID
        print(row[40]) # Cód postal
        print(row[39]) # Provincia
        print(row[38]) # Ciudad
        print(row[43]) # Cód País
        print(row[44]) # Nombre País
        print(row[45]) # Latitud
        print(row[46]) # Longitud
        