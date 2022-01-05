from Sportif import *

sessionFinished = False
mon_equipe = []

while not sessionFinished:
    infos = input("\nEnter information like this format : Firstname Name Year (Abcdef Ghijk 1234)\nOr Type '/' to finish.\n")
    if infos != "/":
        name = infos.split()[0]
        fname = infos.split()[1]
        year = int(infos.split()[2])
        monSportif = Sportif(name, fname, year)
        mon_equipe.append(monSportif)
    else:
        sessionFinished = True
    
for i in mon_equipe:
    i.attribuerCategorie()


for i in mon_equipe:
    print(f"Le sportif {i._firstname} {i._name}, né en {i._birthyear}, a pour adresse mail {i._mail}, et il est dans la catégorie {i._categorie}")