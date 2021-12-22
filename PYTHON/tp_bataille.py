from random import *
from time import *

global liste_carte_joueur1, liste_carte_joueur2, score_j1, score_j2,card_as_level

card_as_level = ["deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "valet", "dame", "roi", "as"]



liste_carte_joueur1 = []
liste_carte_joueur2 = []
score_j1 = 0
score_j2 = 0

differente_cartes = card_as_level.copy()
differente_cartes.extend(differente_cartes)
differente_cartes.extend(differente_cartes)


shuffle(differente_cartes)



def bataille():
    global liste_carte_joueur1, liste_carte_joueur2, score_j1, score_j2, card_as_level
    print(f"C'est une égalite !\n\nC'est l'heure de la bataille !!")
    #en cas de bataille, les cartes "-1" sont egales des deux cotés
    #donc les cartes "-2" ne sont pas utilisées, et c'est les cartes "-3" qui
    #déterminent si l'un remporte
    counter = 0
    winner = False
    while not winner:
        counter += 3
        liste_carte_joueur1.pop()
        liste_carte_joueur2.pop()
        liste_carte_joueur1.pop()
        liste_carte_joueur2.pop()
        valeur_card_J1 = card_as_level.index(liste_carte_joueur1[-1])
        valeur_card_J2 = card_as_level.index(liste_carte_joueur2[-1])
        if valeur_card_J2 > valeur_card_J1:
            print(f"le {liste_carte_joueur2[-1]} bat le {liste_carte_joueur1[-1]} \n\nLe joueur 2 remporte la bataille! (+{counter} points !)")
            score_j2 += counter
            winner = True
        elif valeur_card_J1 > valeur_card_J2:
            print(f"le {liste_carte_joueur1[-1]} bat le {liste_carte_joueur2[-1]} \n\nLe joueur 1 remporte la bataille! (+{counter} points !)")
            score_j1 += counter
            winner = True





for i in range(0, len(differente_cartes), 2):
    liste_carte_joueur1.append(differente_cartes[-1])
    differente_cartes.pop()
    liste_carte_joueur2.append(differente_cartes[-1])
    differente_cartes.pop()




while len(liste_carte_joueur1) > 0 and len(liste_carte_joueur2) > 0  :
    print(f"J1 ► {liste_carte_joueur1[-1]}   VS    {liste_carte_joueur2[-1]} ◄ J2")
    valeur_card_J1 = card_as_level.index(liste_carte_joueur1[-1])
    valeur_card_J2 = card_as_level.index(liste_carte_joueur2[-1])
    if valeur_card_J2 > valeur_card_J1:
        print(f"le {liste_carte_joueur2[-1]} bat le {liste_carte_joueur1[-1]} \n\nLe joueur 2 remporte 1 point !")
        score_j2 += 1
    elif valeur_card_J1 > valeur_card_J2:
        print(f"le {liste_carte_joueur1[-1]} bat le {liste_carte_joueur2[-1]} \n\nLe joueur 1 remporte 1 point !")
        score_j1 += 1
    else:
        bataille()
    print(f"Les scores sont :      J1 > {score_j1} - {score_j2} < J2\n\n")
    sleep(0.5)
    print("prochain tour !")
    liste_carte_joueur1.pop()
    liste_carte_joueur2.pop()
print("Partie Terminée !!")
sleep(2)
print(f"\n\n\n\nLes scores finaux sont :      J1 > {score_j1} - {score_j2} < J2")
if score_j1 > score_j2:
    print("Victoire de Joueur 1 !!")
elif score_j2 > score_j1:
    print("Victoire de Joueur 2 !!")
else:
    print("Egalité ! Dommage !")