import csv
import matplotlib.pyplot as plt

filnavn = "gruppeoppgave/oslo_blindern_1954_2025_med_makstemperatur.csv"


def median(liste):
    sortert = sorted(liste)
    n = len(sortert)
    midten = n // 2

    if n % 2 == 1:
        return sortert[midten]
    else:
        return (sortert[midten - 1] + sortert[midten]) / 2


vind_per_maaned = []
for i in range(12):
    vind_per_maaned.append([])

with open(filnavn, "r", encoding="UTF-8") as fil:
    leser = csv.reader(fil, delimiter=";")
    next(leser)

    for rad in leser:
        try:
            maaned = int(rad[2][3:5])
            vind = float(rad[6].replace(",", "."))
        except (ValueError, IndexError):
            continue

        vind_per_maaned[maaned - 1].append(vind)

minimum = []
medianer = []
maksimum = []

for i in range(12):
    verdier = vind_per_maaned[i]
    minimum.append(min(verdier))
    medianer.append(median(verdier))
    maksimum.append(max(verdier))

maaneder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

plt.figure(figsize=(10, 6))
plt.plot(maaneder, minimum, label="Minimum")
plt.plot(maaneder, medianer, label="Median")
plt.plot(maaneder, maksimum, label="Maksimum")

plt.title("Vindstyrke per måned, Oslo Blindern")
plt.xlabel("Måned")
plt.ylabel("Vindstyrke (m/s)")
plt.xticks(maaneder)
plt.grid()
plt.legend()
plt.show()