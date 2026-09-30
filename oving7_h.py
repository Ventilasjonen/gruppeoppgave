import csv
from pathlib import Path

CSV_FIL = Path(__file__).resolve().parent / "sinnes_2014_2025_med_makstemperatur.csv"

def les_data(valgt_aar):

    sommerdager = 0
    hoysommerdager = 0
    tropedager = 0

    with open(CSV_FIL, "r", encoding="utf-8-sig", newline="") as fil:
        leser = csv.reader(fil, delimiter=";")

        next(leser, None)

        for rad in leser:

            if "-" in rad[3] or not rad[3]:
                continue

            aar = rad[2][-4:]

            maks_temp = float(rad[3].strip().replace(",", "."))


            if aar != valgt_aar:
                continue

            if maks_temp > 30:
                tropedager += 1
            elif maks_temp > 25:
                hoysommerdager += 1
            elif maks_temp > 20:
                sommerdager += 1
            else:
                continue
    print(f"Sommerdager: {sommerdager}, høysommerdager: {hoysommerdager}, tropedager: {tropedager}")

def main():

    valgt_aar = input("Skriv inn år (YYYY): ").strip()

    les_data(valgt_aar)

if __name__ == "__main__":
    main()