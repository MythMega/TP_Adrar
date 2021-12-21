from random import *
import time

match_termine = False
SCORE_DE_BASE = 5
les_scores = {}
les_equipes = []
eq_alias = {}

def displayScore(mes_scores):
    for i in range(5): print(" ")
    print("-LES SCORES SONT LES SUIVANTS-")
    for cle, valeur in mes_scores.items():
        print("Pour l'équipe ", cle, " : ", valeur, " points restants")
    time.sleep(1)

for _ in range(2):
    tout_est_good = False
    while not tout_est_good:
        une_equipe = input("Entrez le nom de l'équipê équipe :")
        if len(une_equipe) < 5:
            print("Votre nom n'est pas valable, entrez un nom plus long")
        elif len(une_equipe) > 25:
            print("Votre nom n'est pas valable, entrez un nom plus court")
        else:
            print("----------------------\n-----C'est validé-----\n----------------------")
            tout_est_good = True
    les_scores[une_equipe] = SCORE_DE_BASE
    les_equipes.append(une_equipe)
time.sleep(1)
for i in range(5): print(" ")
print("debut du match !\n----------------")

while not match_termine:
    #####Selection de qui va être le perdant
    displayScore(les_scores)
    aleatoire = randint(0,1)
    loser = les_equipes[aleatoire]
    les_scores[loser] -= 1
    for i in les_scores:
        if les_scores[i] < 1:
            match_termine = True

for i in range(10): print(" ")
print("Les scores finaux sont tombés !")
time.sleep(1)
displayScore(les_scores)
loser = ""
winner = ""
for i, j in les_scores.items():
    if j == 0:
        loser = i
    if j != 0:
        winner = i

for i in range(10): print(" ")
print("--------------------------------------")
print(f"Les vainqueurs sont donc les {winner}")
print("--------------------------------------")
