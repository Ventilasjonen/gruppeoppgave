import csv

FILNAVN = "gruppeoppgave/sinnes_2014_2025_med_makstemperatur.csv"

def finn_rekke_nuller(array):
    rekke = 0
    lengste_rekke = 0
    index_lengste_array = []
    index_array = []

    for i in range(len(array)):
        if(array[i]) == "0":
            rekke += 1
            index_array.append(i)
        else:
            if(rekke > lengste_rekke):
                lengste_rekke = rekke
                index_lengste_array = index_array

            rekke = 0
            index_array = []

    return lengste_rekke, index_lengste_array
            

with open(FILNAVN, "r", encoding="UTF-8") as file:
    leser = csv.reader(file, delimiter=";")
    next(leser)

    datoer = []
    nedboer_verdier = []

    for line in leser:
        dato = line[2]
        nedboer_verdi = line[5].replace(",", ".")

        nedboer_verdier.append(nedboer_verdi)
        datoer.append(dato)

    lengste_rekke, index_array = finn_rekke_nuller(nedboer_verdier)
    print(f"Den lengste reekken uten nedboer var {lengste_rekke} dager")
    print(f"Den gikk fra {datoer[index_array[0]]} til {datoer[index_array[-1]]}")