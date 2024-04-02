import json
from Pasto import *
from Alimento import *
class Diario:
    def __init__(self, locazioneFile) -> None:
        self.locazioneFile=locazioneFile
        self.pagina=[]


    def caricaAlimentazione(self):
        try:
            with open(self.locazioneFile, "r+") as a:
                stringaDalFile = a.read()
                jsonRecuperato = json.loads(stringaDalFile)

                for singoloPasto in jsonRecuperato:
                    alimento = Alimento(singoloPasto["nome"],singoloPasto["calorie"], singoloPasto["proteine"], singoloPasto["carboidrati", singoloPasto["grassi"]])
                    pasto = Pasto(singoloPasto["nome"], singoloPasto["quando"])
                    self.pagina.append(pasto, alimento)
                pass
        except FileNotFoundError:
            print("FILE NON TROVATO")

    def aggAlimento(self, appuntamento):
        self.pagina.append(appuntamento)

    def saveAlimento(self):
        stringaDaScrivere = self.getJSON()
        if(len(stringaDaScrivere)>0):
            with open(self.locazioneFile, "w+") as fileDaScrivere:
                fileDaScrivere.write(json.dumps(stringaDaScrivere, indent=4))
    
    def getJSON(self):
        risultato = []
        for Pasto in self.utente:
            risultato.append(
                {
                    Pasto.Quando:{
                        Pasto.nome:{
                            "nome":Alimento.nome,
                            "calorie":Alimento.calorie,
                            "proteine":Alimento.proteine,
                            "carboidrati":Alimento.carboidrati,
                            "grassi":Alimento.grassi
                        },
                        "pranzo":{
                            "nome":Alimento.nome,
                            "calorie":Alimento.calorie,
                            "proteine":Alimento.proteine,
                            "carboidrati":Alimento.carboidrati,
                            "grassi":Alimento.grassi
                        },
                        "cena":{
                            "nome":Alimento.nome,
                            "calorie":Alimento.calorie,
                            "proteine":Alimento.proteine,
                            "carboidrati":Alimento.carboidrati,
                            "grassi":Alimento.grassi
                        },
                    },
                }
            )
        return risultato