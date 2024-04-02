from Diario import *
def main():
    while True:
        try:
            print("1) Aggiungere un pasto")
            print("2) Mostra alimentazione di un giorno")
            print("3) Mostra tutti i giorni")
            print("4) EXIT")
            scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")

            diario = Diario("file.json")

            diario.caricaAlimentazione()

            if scelta == '1':
                Quando=input("Che giorno della settimana: ")
                NomeP=input("Quando è il pasto: ")
                Nome=input("Come si chiama il pasto: ")
                Callorie=int(input("Le calorie: "))
                Proteine=int(input("Le proteine: "))
                Carboidrati=int(input("I carboidrati: "))
                Grassi=int(input("I Grassi: "))

                alimento=Alimento(Nome,Callorie,Proteine,Carboidrati,Grassi)
                pasto=Pasto(NomeP,Quando,alimento)

                diario.aggAlimento(pasto)  
                diario.saveAlimento()

            elif scelta == '2':
                print("le calorie totali sono: " + diario.getCalorie())         
            elif scelta == '3':
                print(diario.visualizzaTutto())
            elif scelta == '4':
                print("Uscita dal programma.")
                break

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()