class Pasto:
    def __init__(self, NomeP, Quando, Alimento):
        self.Quando=Quando
        self.NomeP=NomeP
        self.Alimento=Alimento
        self.listaDiPasti=[]

    def aggiungiPasto(self, aggiungi):
        self.listaDiPasti.append(aggiungi)