
SCORE_DE_BASE = 20

les_scores = {}
eq_alias = {}

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
    les_scores[une_equipe] = 20


