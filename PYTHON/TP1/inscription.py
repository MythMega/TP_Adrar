from Sportif import *
from datetime import * 

now = datetime.now()

def verifierErreur(infos):
    #je sais pas quoi tester sur ces deux infos :3
    #name = infos.split()[0]
    #fname = infos.split()[1]
    if len(infos.split()) != 3:
        raise ValueError("Une information est manquante, ou en trop")
    try:
        year = int(infos.split()[2])
    except ValueError:
        raise ValueError("Ceci n'est pas une année valide")
    if len(str(year)) < 4:
        raise ValueError("Une année doit être composée de 4 chiffres")
    if not year < 2100 or not year > 1900:
        raise ValueError("Une erreur s'est surement glissée dans la saisie de l'année")

sessionFinished = False
mon_equipe = []

doc_name = f"inscrits-{str(now.year)}-{str(now.month)}-{str(now.day)}.csv"
document = open(doc_name, "a+")
print(document.read())

if input("\n\n\nKeep old content ? y/n  ").upper() == "N":
        open(doc_name, 'w').close()

looped = True

while looped:
    infos = input("\nEnter informations like this format : Firstname Name Year (Abcdef Ghijk 1234)\n")
    verifierErreur(infos)
    name = infos.split()[0]
    fname = infos.split()[1]
    year = int(infos.split()[2])
    monSportif = Sportif(name, fname, year)
    mon_equipe.append(monSportif)
    if input("\n\n\nContinue ? y/n  ").upper() == "N":
        looped = False

    
for i in mon_equipe:
    i.attribuerCategorie()

for i in mon_equipe:
    document.write(f"{i._firstname},{i._name},{i._birthyear},{i._mail},{i._categorie}\n")
    print(f"Le sportif {i._firstname} {i._name}, né en {i._birthyear}, a pour adresse mail {i._mail}, et il est dans la catégorie {i._categorie}")
document.close()

