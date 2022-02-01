import JMUtils
from UsersClass import *
from Banque import *
from Prenium import *


global database_users_accounts
database_users_accounts = [Users("Admin", "admin")]
database_bank_list = [Banque("banq")]

def getBankOfClient(client):
    for i in database_bank_list:
        liste_client = i.getListClient()
        for j in liste_client:
            if client == j:
                return i

def niceId(id):
    for i in database_users_accounts:
        if i.get_Id() == id:
            return False
    return True

def nicePw(pw):
    if len(pw) > 7:
        return True
    else:
        return False



user_connected = None
while True:
    JMUtils.wait(1)
    JMUtils.clearConsole()
    JMUtils.wait(1)
    print("Que souhaitez vous faire ?")
    answer = int(input("1 : Se connecter\n2 : Se créer un compte\n3 : Quitter\n\n"))
    if answer == 1:
        user_connected = None
        id = input("Votre id : ")
        pw = input("Votre pw : ")
        for i in database_users_accounts:
            goodId = False

            while not goodId:
                if i.get_Id() == id:
                    incorrectPassword = True
                    while incorrectPassword:
                        if i.get_pw() == pw:
                            user_connected = i
                            print("Connexion reussie")
                            incorrectPassword = False
                            goodId = True
                        else:
                            print("incorrect password, please retry")
                            JMUtils.wait(1)
                            JMUtils.clearConsole()
                            pw = input("Votre pw (écrivez quit pour quitter) : ")
                            if pw == "quit":
                                JMUtils.closeProgram()
                else:
                    print("Mauvais Id, celui ci n'existe pas")
                    id = input("Veuillez réessayer : ")
        JMUtils.waitInput(True)

        if user_connected.isAccountLess():
            answer = int(input("Voulez vous créer un compte ?\n1 : Oui\n2 :Non\n"))
            if answer == 1:
                JMUtils.wait(0.5)
                name = input("Votre nom : ")
                fname = input("Votre prénom : ")
                print("Choississez votre banque :")
                for i in range(len(database_bank_list)):
                    print(f"{i} : {database_bank_list[i]}\n")
                bank = int(input("Votre choix : "))
                account_name = f"{name} {fname}"
                user_connected.creerCompte(account_name, 0, database_bank_list[bank].getName())
                database_bank_list[bank].ajouterClient(user_connected)
        else:
            working = True
            while working:
                action = int(input("Que souhaitez vous faire ?\n1 : Retirer\n2 : Déposer\n3 : Afficher\n\n(regular account only)\n4 : devenir prenium\n\n(prenium account only)\n5 : faire un emprunt\n6 : payer une mensualité\n0 : quitter\n"))
                if action == 1:
                    amount = int(input("Combien ?\n"))
                    user_connected.getAccount().dediter(amount)
                elif action == 2:
                    amount = int(input("Combien ?\n"))
                    user_connected.getAccount().crediter(amount)
                elif action == 3:
                    user_connected.getAccount().afficher()
                elif action == 4:
                    nouveauPremium = Prenium(user_connected.get_Id(), user_connected.get_pw(), user_connected.getAccount())
                    database_users_accounts.pop(database_users_accounts.index(user_connected))
                    database_users_accounts.append(nouveauPremium)
                    user_connected = nouveauPremium
                elif action == 5:
                    if not user_connected.isPrenium():
                        print("Error, you are not prenium")
                    else:
                        if user_connected.getMensualite() > 0:
                            print("Erreur, tu as deja un crédit en cours, commence par rembourser tes dettes")
                        else:
                            amount_money = int(input("Combien voulez vous emprunter ?"))
                            bank_of_user = getBankOfClient(user_connected)
                            bank_of_user.decisionBanque(amount_money)
                            if bank_of_user.peutPreterArgent(amount_money):
                                amount_month = int(input("En combien de mois voulez vous rembourser ?"))
                                print(f"Vous aurez à rembourser un total de {amount_money}€ soit {amount_money/amount_month}€ par mois pendant {amount_month}")
                                user_connected.faireCredit(amount_money, amount_month)
                            JMUtils.wait()
                            JMUtils.clearConsole()
                            JMUtils.waitInput(True)
                elif action == 0:
                    working = False

    elif answer == 2:
        user_connected = None
        good = False
        id_good = False
        pw_good = False
        while not id_good:
            id = input("choissisez votre id : ")
            if niceId(id):
                id_good = True
            else:
                print("Id deja existant")
        while not pw_good:
            pw = input("Choississez votre pw : ")
            if nicePw(pw):
                pw_good = True
            else:
                print("Password trop court")
        user_connected = Users(id, pw)
        database_users_accounts.append(user_connected)
        print("Ajouté à la base de donnée")
        JMUtils.waitInput(True)
    elif answer == 3:
        JMUtils.wait(1)
        JMUtils.closeProgram(3)
    elif answer == 4:
        JMUtils.cleanClearConsole()
        print("---------DEBUG MODE---------")
        print("What do you want to do ?")
        action = int(input("1 : Print database\n2 : print Database as object"))
        if action == 1:
            for i in database_users_accounts:
                print("\n")
                i.afficherInformations()
                print(f"mot de passe :{i.debug_get_password()}")
        elif action == 2:
            print(database_users_accounts)
        JMUtils.waitInput(True)