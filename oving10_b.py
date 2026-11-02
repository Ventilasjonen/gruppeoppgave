import csv
from pathlib import Path
import matplotlib.pyplot as plt
import math

CSV_FIL = Path(__file__).resolve().parent / "oslo_blindern_1954_2025_med_makstemperatur.csv"

def main():

    sommerdager = [0]
    hoysommerdager = [0]
    tropedager = [0]
    aar = 0
    start_aar = []
    aar_x = []

    with open(CSV_FIL, "r", encoding="utf-8-sig", newline="") as fil:
        leser = csv.reader(fil, delimiter=";")

        next(leser, None)

        for rad in leser:

            if not rad[2]:
                continue

            start_aar.append(rad[2][-4:])
            if len(start_aar) != 1:
                if start_aar[-1] != start_aar[-2]:
                    aar += 1
                    sommerdager.append(0)
                    hoysommerdager.append(0)
                    tropedager.append(0)
                    aar_x.append(rad[2][-4:])
            else:
                aar_x.append(rad[2][-4:])

            if "-" in rad[3] or not rad[3]:
                continue

            maks_temp = float(rad[3].strip().replace(",", "."))

            if maks_temp > 30:
                tropedager[aar] += 1
            elif maks_temp > 25:
                hoysommerdager[aar] += 1
            elif maks_temp > 20:
                sommerdager[aar] += 1
            else:
                continue

    plt.plot(aar_x,tropedager,color="green", label="Tropedager")
    plt.plot(aar_x,hoysommerdager,color="blue", label="Høysommerdager")
    plt.plot(aar_x,sommerdager,color="red", label="Sommerdager")

    plt.title(f"Antall dager av forskjellige temperaturer hvert år ({aar_x[0]}-{aar_x[-1]})")
    plt.legend()

    plt.xlabel("År")
    plt.ylabel("Dager")

    plt.xticks(ticks=range(0,aar,math.ceil(aar/10)))

    plt.show()

if __name__ == "__main__":
    main()