class Pasto:
    def __init__(self, Nome, Quando, Alimento):
        self.Quando=Quando
        self.Nome=Nome
        self.Alimento=Alimento
        self.listaDiPasti=[]

    def aggiungiPasto(self, aggiungi):
        self.listaDiPasti.append(aggiungi)