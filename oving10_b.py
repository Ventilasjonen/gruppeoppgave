import csv
from pathlib import Path
import matplotlib.pyplot as plt
import math

CSV_FIL = Path(__file__).resolve().parent / "oslo_blindern_1954_2025_med_makstemperatur.csv"

def main():
    sommerdager = [0]
    hoysommerdager = [0]
    tropedager = [0]
    aar_index = 0
    aar_sjekk = []
    aar_array = []

    with open(CSV_FIL, "r", encoding="utf-8-sig", newline="") as fil:
        leser = csv.reader(fil, delimiter=";")

        next(leser, None)

        for rad in leser:

            if not rad[2]:
                continue

            aar_sjekk.append(rad[2][-4:])
            if len(aar_sjekk) != 1:
                if aar_sjekk[-1] != aar_sjekk[-2]:
                    aar_index += 1
                    sommerdager.append(0)
                    hoysommerdager.append(0)
                    tropedager.append(0)
                    aar_array.append(rad[2][-4:])
            else:
                aar_array.append(rad[2][-4:])

            if "-" in rad[3] or not rad[3]:
                continue

            maks_temp = float(rad[3].strip().replace(",", "."))

            if maks_temp > 30:
                tropedager[aar_index] += 1
            elif maks_temp > 25:
                hoysommerdager[aar_index] += 1
            elif maks_temp > 20:
                sommerdager[aar_index] += 1
            else:
                continue

    plt.plot(aar_array,tropedager,color="green", label="Tropedager")
    plt.plot(aar_array,hoysommerdager,color="blue", label="Høysommerdager")
    plt.plot(aar_array,sommerdager,color="red", label="Sommerdager")

    plt.title(f"Antall dager av forskjellige temperaturer hvert år ({aar_array[0]}-{aar_array[-1]})")
    plt.legend()

    plt.xlabel("År")
    plt.ylabel("Dager")

    plt.xticks(ticks=range(0,aar_index,math.ceil(aar_index/10)))

    plt.show()

if __name__ == "__main__":
    main()