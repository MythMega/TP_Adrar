from Compte import *

def clear_console():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def wait_reply():
    nothing = input('Appuyez sur "entrer" pour continuer')




print("-----BONJOUR-----")
print("création de votre compte...")
name = input("Veuillez nous donner votre nom :\n")
le_compte = Compte(name)
using = True
while using:
    clear_console()
    action = int(input("Que voulez vous faire ?\n1 : Afficher solde\n2 : Créditer solde\n3 : Débiter solde\n4 : Stop\n\n"))
    if action < 1 or action > 5 or type(action) is not int:
        print("une erreur est survenue")
        wait_reply()
    else:
        clear_console()
        if action == 1:
            le_compte.afficherArgent()
            wait_reply()
        if action == 2:
            amount = int(input("De combien souhaiteriez vous créditer votre solde ?\nEntrez ici : "))
            le_compte.crediterArgent(amount)
            wait_reply()
        if action == 3:
            amount = int(input("De combien souhaiteriez vous débiter votre solde ?\nEntrez ici : "))
            le_compte.debiterArgent(amount)
            wait_reply()
        if action == 4:
            using = False
        if action == 5:
            clear_console()
            print("debug mode")
            wait_reply()
            le_compte.debug()