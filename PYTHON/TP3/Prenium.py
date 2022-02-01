from UsersClass import *

class Prenium(Users):

    def __init__(self, nom, pw, account):
        super().__init__(nom, pw, account)
        self._emprunt = {"Amount":0, "mensualites":0, "echeance":0}

    def faireCredit(self,amount,echeance):
        self.getAccount().crediter(amount)
        self._emprunt["Amount"] = amount
        self._emprunt["echeance"] = echeance
        self._emprunt["mensualites"] = amount/echeance

    def getRestantAPayer(self):
        return self._emprunt["Amount"]

    def getNombreEcheance(self):
        return self._emprunt["echeance"]

    def getMensualite(self):
        return self._emprunt["mensualites"]

    def payerEcheance(self):
        self._emprunt["Amount"] -= self.getMensualite()
        self._emprunt["echeance"] -= 1

    # retourne True si le crédit est remboursé
    def isRefund(self):
        if self.getMensualite() < 1:
            return True
        else:
            return False