from datetime import *

class Account:

    def __init__(self, owner, solde=0, bankname="LafonMoney", ajd=datetime.now().date()):
        self._date_creation = ajd
        self._bankname = bankname
        self._owner = owner
        self._solde = solde

    def crediter(self, montant):
        self._solde += montant
        self.afficher()

    def debiter(self, montant):
        self._solde -= montant
        self.afficher()

    def getSolde(self):
        return self._solde

    def afficher(self):
        print(f"Le solde du compte est le suivant : {self.getSolde()} €")
