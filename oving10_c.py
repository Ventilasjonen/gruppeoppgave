import csv
import matplotlib.pyplot as plt

navn = ["Oslo Blindern", "Røros", "Sinnes", "Tromsø", "Værnes", "Venabu"]

filer = [
    "gruppeoppgave/oslo_blindern_1954_2025_med_makstemperatur.csv",
    "gruppeoppgave/roeros_1954_2025_med_makstemperatur.csv",
    "gruppeoppgave/sinnes_2014_2025_med_makstemperatur.csv",
    "gruppeoppgave/tromsoe_1954_2025_med_makstemperatur.csv",
    "gruppeoppgave/vaernes_1954_2025_med_makstemperatur.csv",
    "gruppeoppgave/venabu_1954_2025_med_makstemperatur.csv",
]


def snitt_per_aar(filnavn):
    temp_per_aar = {}

    with open(filnavn, "r", encoding="UTF-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)

        for rad in leser:
            try:
                aar = int(rad[2][-4:])
                temp = float(rad[4].replace(",", "."))
            except (ValueError, IndexError):
                continue

            if aar not in temp_per_aar:
                temp_per_aar[aar] = []
            temp_per_aar[aar].append(temp)

    aar_liste = []
    snitt_liste = []
    for aar in sorted(temp_per_aar):
        temperaturer = temp_per_aar[aar]
        if len(temperaturer) >= 300: 
            aar_liste.append(aar)
            snitt_liste.append(sum(temperaturer) / len(temperaturer))

    return aar_liste, snitt_liste


plt.figure(figsize=(12, 9))

for i in range(len(filer)):
    aar, snitt = snitt_per_aar(filer[i])

    plt.subplot(3, 2, i + 1)
    plt.plot(aar, snitt)
    plt.title(navn[i])
    plt.xlabel("År")
    plt.ylabel("Temperatur")
    plt.grid()

plt.suptitle("Årlig gjennomsnittstemperatur")
plt.tight_layout()
plt.show()