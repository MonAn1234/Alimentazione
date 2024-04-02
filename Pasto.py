class Pasto:
    def __init__(self, NomeP, Quando, Alimento):
        # Inizializzazione degli attributi del pasto
        self.Quando = Quando  # Data del pasto
        self.NomeP = NomeP  # Nome del pasto
        self.Alimento = Alimento  # Oggetto Alimento associato al pasto
        self.listaDiPasti = []  # Lista di pasti

    def aggiungiPasto(self, aggiungi):
        # Metodo per aggiungere un pasto alla lista di pasti
        self.listaDiPasti.append(aggiungi)