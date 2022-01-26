class Banque:

    def __init__(self, name):
        self._name = name
        self._pecule = 0
        self._customers = []

    def setPecule(self, amount):
        pass

    def getPecule(self):
        return self._pecule

    def peutPreterArgent(self, amount):
        if self._pecule >= amount:
            return True
        else:
            return False

    def preterArgent(self, amount):
        if self.peutPreterArgent():
            print("Pret accepté par la banque")
        else:
            print("pret refusé par la banque")