# importo della classe Diario
from Diario import *

def main():
    # Creo la funzione main che sarà la parte integrante dell'esercizio
    while True:
        try:
            # Menu di scelta delle azioni
            print("1) Aggiungere un pasto")
            print("2) Mostra alimentazione di un giorno")
            print("3) Mostra tutti i giorni")
            print("4) EXIT")
            # Scelta dell'azione da parte dell'utente
            scelta = input("Inserisci il numero corrispondente all'azione desiderata: ")
            # Inizializzo un'istanza della classe Diario con il file "file.json"
            diario = Diario("file.json")
            # Carico i dati alimentari dal file JSON
            diario.caricaAlimentazione()

            # Scelta 1: Aggiungere un pasto
            if scelta == '1':
                Quando = input("Che giorno della settimana: ")
                NomeP = input("Quando è il pasto: ")
                Nome = input("Come si chiama il pasto: ")
                Calorie = int(input("Le calorie: "))
                Proteine = int(input("Le proteine: "))
                Carboidrati = int(input("I carboidrati: "))
                Grassi = int(input("I Grassi: "))

                # Creo un'istanza di Alimento e di Pasto con i dati inseriti dall'utente
                alimento = Alimento(Nome, Calorie, Proteine, Carboidrati, Grassi)
                pasto = Pasto(NomeP, Quando, alimento)

                # Aggiungo il pasto al diario e salvo le modifiche sul file JSON
                diario.aggAlimento(pasto)
                diario.saveAlimento()

            # Scelta 2: Mostrare il totale delle calorie
            elif scelta == '2':
                # Stampare il totale delle calorie
                print("Le calorie totali sono: ", diario.getCalorie())

            # Scelta 3: Mostrare tutti i pasti
            elif scelta == '3':
                # Stampare tutti i pasti presenti nel file JSON
                diario.visualizzaTutto()

            # Scelta 4: Uscire dal programma
            elif scelta == '4':
                print("Uscita dal programma.")
                break

            else:
                print("Scelta non valida. Riprova.")

        except Exception as e:
            print("Si è verificato un errore:", e)

if __name__ == "__main__":
    main()