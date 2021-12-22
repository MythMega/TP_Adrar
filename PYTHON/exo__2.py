from datetime import *
def exo_un():
    value = int(input("Entrez un nombre : "))
    resultat = "Votre nombre " + str(value) + " est "
    if value%2==1:
        resultat += "impaire"
    else:
        resultat += "pair"
    print(resultat)

def exo_deux():
    now = datetime.today()
    me_years = int(input("Année de naissance (numérique) : "))
    me_month = int(input("Mois de naissance (numérique) : "))
    me_day = int(input("Jour de naissance (numérique) : "))
    birth = datetime(me_years, me_month, me_day, 0, 0, 0, 0)
    difference = now - birth
    if difference.days > (18*365.25):
        print("Effectivement, tu es majeur.")
    else:
        print(f"aie, tu n'es pas majeurs, tu dois attendre encore {(18*365.25)-difference.days} jours")


def exo_trois():
    TVA = 0.21
    nbr_article = int(input("Nombre d'article : "))
    total_price = 0
    for i in range(nbr_article):
        total_price += int(input(f"Quel est le prix de larticle numero {i+1} : ")) #deso pour ça
    print(f"Le prix total est de {total_price*(1+TVA)}")


def exo_quatre():
    nbr_notes = int(input("Entrez le nombre de notes : "))
    liste_de_notes = []
    somme = 0
    for i in range(nbr_notes):
        new_note = int(input("Entrer une note : "))
        liste_de_notes.append(new_note)
        somme += new_note
    print(f"La note minimale est {min(liste_de_notes)}, la note maximale est {max(liste_de_notes)}, et la moyenne est {somme/nbr_notes}")

def exo_quatre_version_fun():
    nbr_notes = int(input("Entrez le nombre de notes : "))
    liste_de_notes = []
    somme = 0
    for i in range(nbr_notes):
        new_note = int(input("Entrer une note : "))
        liste_de_notes.append(new_note)
        somme += new_note
    max = 99**99 * -1
    min = 99**99
    for i in liste_de_notes:
        if i > max:
            max = i
        else:
            min = i
    print(f"La note minimale est {min}, la note maximale est {max}, et la moyenne est {somme / nbr_notes}")

exo_quatre_version_fun()
