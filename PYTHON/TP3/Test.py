from Prenium import *
from Account import *

name = "Jean"
pw = "Eude"
accounts = Account(name, 254096, "LafonMoula")
mon_utilisateur = Prenium(name, pw, accounts)

mon_utilisateur.getAccount().debiter(200)