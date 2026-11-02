import csv
import datetime
import matplotlib.pyplot as plt

FILNAVN = "sinnes_2014_2025.csv"

snodybder = [0] * 12
nedborer = [0] * 12
min_middeltemper = [float("inf")] * 12
maks_middeltemper = [float("-inf")] * 12
hoyest_middelvinder = [0] * 12

antall_nedborer = [0] * 12

maaneder = []

for i in range(12):
    maaneder.append(i)




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
            maaned = dato.month - 1
            nedborer[maaned] += nedbor
            antall_nedborer[maaned] += 1

            if snodybde > snodybder[maaned]:
                snodybder[maaned] = snodybde

            if middeltemp < min_middeltemper[maaned]:
                min_middeltemper[maaned] = middeltemp

            if middeltemp > maks_middeltemper[maaned]:
                maks_middeltemper[maaned] = middeltemp

            if hoyest_middelvind > hoyest_middelvinder[maaned]:
                hoyest_middelvinder[maaned] = hoyest_middelvind

    # Sjekker om det er mer enn 20 målinger
    for maaling in range(12):
        if antall_nedborer[maaling] < 20:
            nedborer[maaling] = None

fig, ax = plt.subplots(5)

ax[0].plot(maaneder, hoyest_middelvinder)
ax[1].plot(maaneder, min_middeltemper)
ax[2].plot(maaneder, nedborer)
ax[3].plot(maaneder, snodybder)
ax[4].plot(maaneder, maks_middeltemper)

plt.tight_layout()
plt.show()