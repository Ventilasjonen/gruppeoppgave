#Skiføre: Hvis vi antar at det er skiføre så lenge snødybden er minst 20cm, la brukeren
#skrive inn et årstall og regn ut for et oppgitt år hvor mange dager det var skiføre den
#skisesongen. En skisesong strekker seg fra november forrige år til mai dette året.

filnavn = "DAT120/Innlevering/Gruppeprosjekt/gruppeoppgave/sinnes_2014_2025.csv"

try:
    with open(filnavn, "r", encoding="utf-8") as fil:
        fil.readline()  # Hopp over header
        skifore_dager = 0
        arstall_input = int(input("Skriv inn et årstall (f.eks. 2020): "))
        
        for line in fil:
            if line.strip():  # Skip tomme linjer
                komponenter = line.split(";")

                if komponenter[2] != "":
                    arstall = int(komponenter[2][-4:])
                    maaned = int(komponenter[2][3:5])
                    dag = int(komponenter[2][:2])

                

                if not "-" in komponenter[6] and komponenter[6] != "":
                    snoverdi = int(komponenter[6])

                
                if (arstall == arstall_input-1 and maaned >= 11) or (arstall == arstall_input and maaned <= 5):
                    if snoverdi >= 20:
                        skifore_dager += 1

    print(f"Antall dager med skiføre i skisesongen: {skifore_dager}")
except FileNotFoundError:
    print(f"Filen '{filnavn}' ble ikke funnet.")