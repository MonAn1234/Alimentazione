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
                    alimento=Alimento(singoloPasto["alimenti"]["nome"],singoloPasto["alimenti"]["calorie"],singoloPasto["alimenti"]["proteine"],singoloPasto["alimenti"]["carboidrati"],singoloPasto["alimenti"]["grassi"])                    
                    pasto=Pasto(singoloPasto["NomeP"],singoloPasto["Quando"],alimento)
                    self.pagina.append(pasto)
                pass
        except FileNotFoundError:
            print("FILE NON TROVATO")
        except Exception as e:
            print("eccezzione generica: "+ e)
            pass

    def aggAlimento(self, appuntamento):
        self.pagina.append(appuntamento)

    def saveAlimento(self):
        stringaDaScrivere = self.getJSON()
        if(len(stringaDaScrivere)>0):
            with open(self.locazioneFile, "w+") as fileDaScrivere:
                fileDaScrivere.write(json.dumps(stringaDaScrivere, indent=4))
    
    def getJSON(self):
        risultato = []
        for pasto in self.pagina:
            risultato.append(
                {
                    "Quando": pasto.Quando,
                    "NomeP": pasto.NomeP,
                    "alimenti": {
                        "nome": pasto.Alimento.nome,
                        "carboidrati":pasto.Alimento.carboidrati,
                        "proteine": pasto.Alimento.proteine,
                        "grassi": pasto.Alimento.grassi,
                        "calorie": pasto.Alimento.calorie
                     
                     36   }
                }
            )
        return risultato