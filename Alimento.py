class Alimento:
    def __init__(self, nome, calorie, proteine, carboidrati, grassi):
        # Inizializzazione degli attributi dell'alimento
        self.nome = nome  # Nome dell'alimento
        self.calorie = calorie  # Quantità di calorie
        self.proteine = proteine  # Quantità di proteine
        self.carboidrati = carboidrati  # Quantità di carboidrati
        self.grassi = grassi  # Quantità di grassi

    def newNome(self, newNome):
        # Metodo per modificare il nome dell'alimento
        self.nome = newNome

    def newCalorie(self, newCalorie):
        # Metodo per modificare le calorie dell'alimento
        self.calorie = newCalorie

    def newProteine(self, newProteine):
        # Metodo per modificare le proteine dell'alimento
        self.proteine = newProteine

    def newCarboidrati(self, newCarboidrati):
        # Metodo per modificare i carboidrati dell'alimento
        self.carboidrati = newCarboidrati

    def newGrassi(self, newGrassi):
        # Metodo per modificare i grassi dell'alimento
        self.grassi = newGrassi