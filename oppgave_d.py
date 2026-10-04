import csv
import datetime
import matplotlib.pyplot as plt

FILNAVN = "sinnes_2014_2025.csv"

snodybder = []
datoer = []
nedborer = []
middeltemper = []
hoyest_middelvinder = []

year = int(input("Skriv inn en et år: "))

with open(FILNAVN, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)

    for row in reader:
        try:
            dato = datetime.datetime.strptime(row[2], "%d.%m.%Y").date()
            snodybde = float(row[6].replace(",", "."))
            nedbor = float(row[4].replace(",", "."))
            middeltemp = float(row[3].replace(",", "."))
            hoyest_middelvind = float(row[5].replace(",", "."))
        except (ValueError, IndexError):
            continue

        if dato.year == year:
            datoer.append(dato)
            snodybder.append(snodybde)
            nedborer.append(nedbor)
            middeltemper.append(middeltemp)
            hoyest_middelvinder.append(hoyest_middelvind)


    plt.plot(datoer, hoyest_middelvinder)
    plt.plot(datoer, middeltemper)
    plt.plot(datoer, nedborer)
    plt.plot(datoer, snodybder)
    plt.show()