class Alimento:
    def __init__(self, nome, calorie, proteine, carboidrati, grassi):
        self.nome=nome
        self.calorie=calorie
        self.proteine=proteine
        self.carboidrati=carboidrati
        self.grassi=grassi

    def newNome(self, newNome):
        self.nome=newNome

    def newCalorie(self, newCalorie):
        self.calorie=newCalorie

    def newProteine(self, newProteine):
        self.proteine=newProteine

    def newCarboidrati(self, newCarboidrati):
        self.carboidrati=newCarboidrati

    def newGrassi(self, newGrassi):
        self.grassi=newGrassi