from Account import *
import JMUtils


class Users:

    def __init__(self, name, pw, account=None):
        self._nom = name
        self._password = pw
        self._account = account
        self._isPrenium = False

    def afficherInformations(self):
        print(self)

    def get_Id(self):
        return self._nom

    def get_pw(self):
        return self._password

    def isAccountLess(self):
        if self._account == None:
            return True
        else:
            return False
    def getAccount(self):
        return self._account


    def creerCompte(self, leNom, montant, banque):
        if self._account is None:
            sonPassWord = input("C'est quoi ton password ?\n")
            if sonPassWord != self._password:
                print("Error, wrong password, please try later\n")
                return
            sonFuturCompte = Account(leNom, montant, banque)
            self._account = sonFuturCompte
        else:
            print("Error, you already have an account\n")

    def debug_get_password(self):
        return self._password

    # def devenirPrenium(self):
    #     futurPremium = Prenium.Prenium(self._nom, self._password, self._account)
    #     self._isPrenium = True
    #     return futurPremium

    def isPrenium(self):
        return self._isPrenium

    def __repr__(self):
        if self._account is not None :
            return f"Compte {self._nom}, infos du compte :\nNom banque :{self._account.bankname}\nsolde {self._account.getSolde()}€\n"
        else :
            return f"Compte {self._nom}, infos du compte :\nAucune banque associée\n"