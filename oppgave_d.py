import csv
import datetime
import matplotlib.pyplot as plt

FILNAVN = "sinnes_2014_2025.csv"

snodybder = []
datoer = []
nedborer = []
middeltemper = []
hoyest_middelvinder = []

year = int(input("Skriv inn en dato på format: dd.mm.åååå: "))

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







# def til_tall(verdi):
#     if verdi == "-":
#         return None
#     return float(verdi.replace(",", "."))
#
#
# def les_data(filnavn):
#     dager = []
#     with open(filnavn, encoding="utf-8") as fil:
#         leser = csv.reader(fil, delimiter=";")
#         next(leser)
#         for rad in leser:
#             try:
#                 dato = datetime.datetime.strptime(rad[2], "%d.%m.%Y").date()
#             except (ValueError, IndexError):
#                 continue
#             dager.append({
#                 "dato": dato,
#                 "middeltemperatur": til_tall(rad[3]),
#                 "nedbor": til_tall(rad[4]),
#                 "vind": til_tall(rad[5]),
#                 "snodybde": til_tall(rad[6]),
#             })
#     return dager
#
#
# def plot_aar(dager, aar):
#     aar_data = sorted((d for d in dager if d["dato"].year == aar), key=lambda d: d["dato"])
#
#     datoer = [d["dato"] for d in aar_data]
#     snodybde = [d["snodybde"] for d in aar_data]
#     nedbor = [d["nedbor"] for d in aar_data]
#     temperatur = [d["middeltemperatur"] for d in aar_data]
#     vind = [d["vind"] for d in aar_data]
#
#     fig, akser = plt.subplots(2, 2, figsize=(12, 8))
#     fig.suptitle(f"Værdata for Sinnes {aar}")
#
#     akser[0, 0].plot(datoer, snodybde, color="tab:blue")
#     akser[0, 0].set_title("Snødybde (cm)")
#
#     akser[0, 1].plot(datoer, nedbor, color="tab:green")
#     akser[0, 1].set_title("Nedbør (mm)")
#
#     akser[1, 0].plot(datoer, temperatur, color="tab:red")
#     akser[1, 0].set_title("Middeltemperatur (°C)")
#
#     akser[1, 1].plot(datoer, vind, color="tab:orange")
#     akser[1, 1].set_title("Høyeste middelvind (m/s)")
#
#     for rad in akser:
#         for akse in rad:
#             akse.grid(True, alpha=0.3)
#
#     fig.autofmt_xdate()
#     plt.tight_layout()
#     plt.show()
#
#
# def main():
#     dager = les_data(FILNAVN)
#     tilgjengelige_aar = sorted({d["dato"].year for d in dager})
#
#     while True:
#         try:
#             aar = int(input(f"Skriv inn et årstall ({tilgjengelige_aar[0]}-{tilgjengelige_aar[-1]}): "))
#         except ValueError:
#             print("Du må skrive inn et gyldig årstall.")
#             continue
#         if aar not in tilgjengelige_aar:
#             print(f"Ingen data for {aar}. Prøv igjen.")
#             continue
#         break
#
#     plot_aar(dager, aar)
#
#
# if __name__ == "__main__":
#     main()
