from random import *
from time import *

card_as_level = ["deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "valet", "dame", "roi", "as"]


liste_carte_joueur1 = []
liste_carte_joueur2 = []
score_j1 = 0
score_j2 = 0

differente_cartes = card_as_level.copy()
shuffle(differente_cartes)
differente_cartes.extend(differente_cartes)
differente_cartes.extend(differente_cartes)

for i in range(0, len(differente_cartes), 2):
    liste_carte_joueur1.append(differente_cartes[-1])
    differente_cartes.pop()
    liste_carte_joueur2.append(differente_cartes[-1])
    differente_cartes.pop()

for i in range(len(liste_carte_joueur1)):
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
        print(f"C'est une égalite !\n\nPersonne ne remporte de point !")
    print(f"Les scores sont :      J1 > {score_j1} - {score_j2} < J2\n\n")
    sleep(3)
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