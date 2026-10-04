import csv
import datetime

FILNAVN = "sinnes_2014_2025_med_makstemperatur.csv"

sommerdager = {
    "sommerdager": 0,
    "hoysommerdager": 0,
    "tropedager": 0
}

year = int(input("Skriv inn en et år: "))

with open(FILNAVN, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)

    for row in reader:
        try:
            dato = datetime.datetime.strptime(row[2], "%d.%m.%Y").date()

            if (dato.year == year) and (25 >= float(row[3].replace(",", ".")) > 20):
                sommerdager["sommerdager"] += 1
            elif (dato.year == year) and (30 >= float(row[3].replace(",", ".")) > 25):
                sommerdager["hoysommerdager"] += 1
            elif (dato.year == year) and (float(row[3].replace(",", ".")) > 30):
                        sommerdager["tropedager"] += 1
        except (ValueError, IndexError):
             continue

    print(sommerdager)
