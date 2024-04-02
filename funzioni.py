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
                Callorie=input("Le calorie: ")
                Proteine=input("Le proteine: ")
                Carboidrati=input("I carboidrati: ")
                Grassi=input("I Grassi: ")

                alimento=Alimento(Nome,Callorie,Proteine,Carboidrati,Grassi)
                pasto=Pasto(NomeP,Quando,alimento)

                diario.aggAlimento(pasto)  
                diario.saveAlimento()

            elif scelta == '2':
                         
            elif scelta == '3':
                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)
                salone.delUtente(appuntamento)  

                print("Adesso Re-inserisci i dati: ")

                Nome=input("Inserisci il nome: ")
                Cognome=input("Inserisci il cognome: ")
                Email=input("Inserisci il email: ")
                Data=input("Inserisci il la data: ")
                Ora=input("Inserisci l'ora: ")
                Servizio=input("Inserisci il tipo di servizio: ")

                cliente=Cliente(Nome,Cognome,Email)
                appuntamento=Appuntamento(Data,Ora,Servizio,cliente)

                salone.aggUtente(appuntamento)  
                salone.saveUtente()

            elif scelta == '4':
                print("Uscita dal programma.")
                break

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()