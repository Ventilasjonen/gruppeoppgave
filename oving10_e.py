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


def skidager_per_sesong(filnavn):
    antall_data = {}  
    antall_ski = {}

    with open(filnavn, "r", encoding="UTF-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)

        for rad in leser:
            try:
                dato = rad[2]
                maaned = int(dato[3:5])
                aar = int(dato[-4:])
                snoe = float(rad[7].replace(",", "."))
            except (ValueError, IndexError):
                continue

            if maaned >= 11:
                sesong = aar
            elif maaned <= 4:
                sesong = aar - 1
            else:
                continue

            if sesong not in antall_data:
                antall_data[sesong] = 0
                antall_ski[sesong] = 0

            antall_data[sesong] += 1
            if snoe > 20:
                antall_ski[sesong] += 1

    sesong_liste = []
    ski_liste = []
    for sesong in sorted(antall_data):
        if antall_data[sesong] >= 90:
            sesong_liste.append(sesong)
            ski_liste.append(antall_ski[sesong])

    return sesong_liste, ski_liste


plt.figure(figsize=(12, 6))

for i in range(len(filer)):
    sesonger, skidager = skidager_per_sesong(filer[i])
    plt.plot(sesonger, skidager, label=navn[i])

plt.title("Antall dager med skiføre per sesong")
plt.xlabel("Sesong")
plt.ylabel("Dager med skiføre")
plt.grid()
plt.legend()
plt.show()