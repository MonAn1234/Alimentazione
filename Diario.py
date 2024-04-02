import json
from Pasto import *
from Alimento import *

class Diario:
    def __init__(self, locazioneFile) -> None:
        # Inizializzazione della classe Diario con la locazione del file JSON
        self.locazioneFile = locazioneFile
        self.pagina = []  # Lista dei pasti nel diario

    def caricaAlimentazione(self):
        try:
            # Provo ad aprire il file JSON in modalità lettura
            with open(self.locazioneFile, "r") as file:
                # Leggo il contenuto del file e lo converto in formato JSON
                stringaDalFile = file.read()
                jsonRecuperato = json.loads(stringaDalFile)
                # Itero su ogni pasto recuperato dal file
                for singoloPasto in jsonRecuperato:
                    # Creo un'istanza di Alimento e di Pasto utilizzando i dati recuperati dal file
                    alimento = Alimento(singoloPasto["alimenti"]["nome"], singoloPasto["alimenti"]["calorie"],
                                        singoloPasto["alimenti"]["proteine"], singoloPasto["alimenti"]["carboidrati"],
                                        singoloPasto["alimenti"]["grassi"])
                    pasto = Pasto(singoloPasto["NomeP"], singoloPasto["Quando"], alimento)
                    # Aggiungo il pasto alla lista della pagina
                    self.pagina.append(pasto)
        except FileNotFoundError:
            print("FILE NON TROVATO")
        except Exception as e:
            print("Eccezione generica:", e)

    def aggAlimento(self, appuntamento):
        # Aggiunge un nuovo pasto alla lista della pagina
        self.pagina.append(appuntamento)

    def saveAlimento(self):
        # Ottiene il contenuto JSON della lista dei pasti
        stringaDaScrivere = self.getJSON()
        if len(stringaDaScrivere) > 0:
            # Scrive il contenuto JSON nel file
            with open(self.locazioneFile, "w") as fileDaScrivere:
                fileDaScrivere.write(json.dumps(stringaDaScrivere, indent=4))
    
    def getJSON(self):
        # Ottiene il contenuto JSON della lista dei pasti
        risultato = []
        for pasto in self.pagina:
            # Crea un dizionario per rappresentare il pasto in formato JSON
            risultato.append(
                {
                    "Quando": pasto.Quando,
                    "NomeP": pasto.NomeP,
                    "alimenti": {
                        "nome": pasto.Alimento.nome,
                        "carboidrati": pasto.Alimento.carboidrati,
                        "proteine": pasto.Alimento.proteine,
                        "grassi": pasto.Alimento.grassi,
                        "calorie": pasto.Alimento.calorie
                    }
                }
            )
        return risultato

    def getCalorie(self):
        somma_calorie = 0
        somma_proteine = 0
        somma_carboidrati = 0
        somma_grassi = 0
        with open(self.locazioneFile, "r") as file:
            # Apre il file JSON in modalità di lettura
            jsonRecuperato = json.load(file)
            a=input("che giorno della settimana vuoi controllare? ")
            for singoloPasto in jsonRecuperato:
                ## Controlla se il giorno del pasto corrisponde al giorno specificato dall'utente
                if singoloPasto["Quando"] == a:
                    # Calcola la somma totale delle calorie, proteine, carboidrati e grassi di tutti i pasti
                    alimento = Alimento(singoloPasto["alimenti"]["nome"], singoloPasto["alimenti"]["calorie"],
                                        singoloPasto["alimenti"]["proteine"], singoloPasto["alimenti"]["carboidrati"],
                                        singoloPasto["alimenti"]["grassi"])
                    somma_calorie += alimento.calorie
                    somma_proteine += alimento.proteine
                    somma_carboidrati += alimento.carboidrati
                    somma_grassi += alimento.grassi
        # Restituisce la somma totale delle calorie, proteine, carboidrati e grassi
        return somma_calorie + somma_proteine + somma_carboidrati + somma_grassi
            
    def visualizzaTutto(self):
        with open(self.locazioneFile, "r") as file:
            # Apre il file JSON in modalità di lettura
            jsonRecuperato = json.load(file)
            for singoloPasto in jsonRecuperato:
                # Stampa le informazioni di ogni pasto
                print("Quando:", singoloPasto["Quando"])
                print("NomeP:", singoloPasto["NomeP"])
                print("Alimento:")
                print("  Nome:", singoloPasto["alimenti"]["nome"])
                print("  Calorie:", singoloPasto["alimenti"]["calorie"])
                print("  Proteine:", singoloPasto["alimenti"]["proteine"])
                print("  Carboidrati:", singoloPasto["alimenti"]["carboidrati"])
                print("  Grassi:", singoloPasto["alimenti"]["grassi"])