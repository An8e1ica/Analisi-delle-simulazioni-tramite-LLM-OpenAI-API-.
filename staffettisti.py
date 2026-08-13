import math
import random


class Staffettista:

    def __init__(self, nome, eta, x, y, presente=True):

        self.nome = nome
        self.eta = eta
        self.x = x
        self.y = y
        self.anni_di_servizio = self.calcola_anni()
        self.titolo_studio = self.calcola_titolo_studio()
        self.presente = presente


    def calcola_anni(self):
        massimo = self.eta - 18
        return random.randint(0, massimo)

    @property
    def posizione(self):
        return self.x, self.y

    def calcola_distanza(self, altro):
        return math.dist(self.posizione, altro.posizione)

    def calcola_titolo_studio(self):
        if self.eta < 21:
            titoli_possibili = ["licenza media", "diploma"]
        elif self.eta < 24:
            titoli_possibili = ["licenza media", "diploma", "laurea triennale"]
        else:
            titoli_possibili = ["licenza media", "diploma", "laurea triennale", "laurea magistrale"]

        return random.choice(titoli_possibili)


class Pacco:

    def __init__(self, nome, x_coord, y_coord):
        self.nome = nome
        self.x_coord = x_coord
        self.y_coord = y_coord

    @property
    def posizione(self):
        return self.x_coord, self.y_coord

    def calcola_distanza(self, altro):
        return math.dist(self.posizione, altro.posizione)


pacco_partenza = Pacco("pacco_partenza", 0, 7,)
pacco_destinazione = Pacco("pacco_destinazione", 8, 5)