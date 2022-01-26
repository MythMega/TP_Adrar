from datetime import *

class Compte:

    def __init__(self, owner_name):
        self._creation = datetime.now().date()
        self._solde = 0
        self._owner = owner_name
        self._bank = "Lafon"


    def crediterArgent(self, amount):
        self._solde = self._solde + amount
        print("Opération réussie.")
        self.afficherArgent()

    def debiterArgent(self, amount):
        if self._solde < amount:
            print("Erreur, vous n'avez pas assez d'argent.")
        else:
            self._solde = self._solde - amount
            print("Opération réussie.")
        self.afficherArgent()

    def afficherArgent(self):
        print(f"Votre solde s'élève à {self._solde}")

    def debug(self):
        print(f"Votre compte a été crée le {self._creation}\nVotre compte est au nom de {self._owner}\nVotre solde s'élève à {self._solde}\nVotre compte est dans la banque {self._bank}")