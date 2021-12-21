from time import *
from random import *

global LONGUEUR_DE_PISTE, SPEED
LONGUEUR_DE_PISTE = 25
SPEED = 50


def isThereAWinner(mes_participants):
    global LONGUEUR_DE_PISTE
    result = False
    for i, j in mes_participants.items():
        if j == LONGUEUR_DE_PISTE:
            result = True
    return result


def creer_participants(nbr_participants):
    result = {}
    for i in range(nbr_participants):
        result[i + 1] = 0
    return result


def faireAvancer(mes_participants):
    for i, j in mes_participants.items():
        mes_participants[i] += randint(0, 1)


def afficher_score(mes_participants, nbr_tour):
    global LONGUEUR_DE_PISTE, SPEED
    print("------ Tour numéro : ", nbr_tour, "------\n")
    for i, j in mes_participants.items():
        impression = str(i)
        impression += "[ "
        for _ in range(j - 1):
            impression += "-"
        impression += "%"
        for _ in range(LONGUEUR_DE_PISTE - j):
            impression += "-"
        impression += " ]"
        print(impression)
    sleep(1 / SPEED * 10)
    for _ in range(5): print("\n")


def afficher_score_sans_tours(mes_participants):
    global LONGUEUR_DE_PISTE, SPEED
    for i, j in mes_participants.items():
        impression = str(i)
        impression += "[ "
        for _ in range(j - 1):
            impression += "-"
        impression += "%"
        for _ in range(LONGUEUR_DE_PISTE - j):
            impression += "-"
        impression += " ]"
        print(impression)
    sleep(1 / SPEED * 10)



def finir(mes_participants):
    for i in range(100): print("\n")
    print("Finito\n")
    result = ""
    for i, j in mes_participants.items():
        if j == LONGUEUR_DE_PISTE:
            result = i
    print(f"Le vainqueur est le {result} !\n\nLes Scores sont les suivants :")
    afficher_score_sans_tours(mes_participants)
    print("Fin de la session")



pas_derreur = False
while not pas_derreur:
    try:
        nbr_participants = int(input("Nombre de participants : "))
    except:
        print("Une erreur est survenue")
    else:
        pas_derreur = True

mes_participants = creer_participants(nbr_participants)
finished = False
nbr_tour = 0
while not finished:
    nbr_tour += 1
    if isThereAWinner(mes_participants):
        finished = True
    else:
        faireAvancer(mes_participants)
    afficher_score(mes_participants, nbr_tour)


finir(mes_participants)
