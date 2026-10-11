import csv
import datetime

FILEPATH = "sinnes_2014_2025_med_makstemperatur.csv"

total_plantevekst = 0

year = int(input("Skriv in et år: "))

with open(FILEPATH, "r", encoding="UTF-8") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)

    for row in reader:
        try:
            dato = datetime.datetime.strptime(row[2], "%d.%m.%Y").date()

            if year == dato.year:
                temp = float(row[4].replace(",", "."))
                makstemp = float(row[3].replace(",", "."))
                if makstemp >= 5:
                    total_plantevekst += makstemp-temp

        except(ValueError, IndexError):
            continue

    print(total_plantevekst)