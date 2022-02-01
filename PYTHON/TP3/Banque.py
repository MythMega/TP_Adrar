

class Banque:

    def __init__(self, name, pecule = 0):
        self._name = name
        self._pecule = pecule
        self._customers = []

    def setPecule(self, amount):
        pass

    def getName(self):
        return self._name

    def getPecule(self):
        return self._pecule

    def peutPreterArgent(self, amount):
        if self._pecule >= amount:
            return True
        else:
            return False

    def decisionBanque(self, amount):
        if self.peutPreterArgent(amount):
            print("Pret accepté par la banque")
        else:
            print("pret refusé par la banque")

    def preterArgent(self, amount):
        if self.peutPreterArgent(amount):
            pass #calculs nécessaires

    def ajouterClient(self, client):
        self._customers.append((client))

    def getListClient(self):
        return self._customers