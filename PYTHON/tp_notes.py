#Volé sur mon github https://github.com/MythMega/sandbox/blob/master/python_random_projects/StringVerif.py
def removeBadChar(mon_string):
    x = ""
    y = ""
    z = "-, _'.;!?"
    mytable = mon_string.maketrans(x, y, z)
    resultat = mon_string.translate(mytable)
    return resultat

verif = False
while not verif:
    try:
        nbrMatiere = int(input("Entrez un nombre de matière : "))
    except:
        print("Cette valeur n'est pas un nombre entier, réessayez")
    else:
        if nbrMatiere < 1 or nbrMatiere > 12:
            print("Nombre de matière incorrect, veillez à choisir une valeur entre 1 & 12")
        else:
            verif=True

listMatiere = []
for i in range(nbrMatiere):
    libelleMatiere = ""
    while len(libelleMatiere) < 5:
        libelleMatiere = input("le nom de la matière : ")
        if len(libelleMatiere) < 5:
            print("Ce nom est trop court")
    libelleMatiere = removeBadChar(libelleMatiere.upper())
    listMatiere.append(libelleMatiere)
    print(f'{libelleMatiere} à bien été ajouté !\n---------------')

nbrNoteParMatiere = {} #Va stocker uniquement le nombre de note pour chaque matière
fullListNote = {} #va stocker un tableau de note associé à chaque matière


#DEFINITION DU NOMBRE DE NOTE PAR MATIERE
for i in listMatiere:
    print("------------")
    print("--", i, "--")

    verif = False
    while not verif:
        try:
            nbrNoteForThis = int(input("nombre de note : "))
        except:
            print("Cette valeur n'est pas un nombre entier, réessayez")
        else:
            verif = True

    nbrNoteParMatiere[i] = nbrNoteForThis

print("----------------")

#DEFINITIONS DU TABLEAU DE NOTE POUR CHAQUE MATIERE
for key in nbrNoteParMatiere:
    nbrNoteDansCetteMatiere = nbrNoteParMatiere[key]
    print("matière : ", key)
    notesDeCetteMatiere = []

    for i in range(nbrNoteDansCetteMatiere):
        print(" note n° : ", i + 1)
        verif = False
        while not verif:
            try:
                uneNote = float(input("Entrez : "))
            except:
                print("Cette valeur n'est pas un nombre, réessayez")
            else:
                verif = True

        notesDeCetteMatiere.append(uneNote)
    fullListNote[key] = notesDeCetteMatiere


#FOR THE BEST NOTE, I WILL TAKE ONLY THE BEST OF EACH
monDicoAvecLesNoteHautes = {}
monDicoAvecLesNoteBasses = {}
maListeAvecToutesLesNotes = []


#On va faire un Dico avec les notes max, et un dico avec les note min (oui c'est honteux)
for key in fullListNote:
    maList = fullListNote[key]
    for i in maList:
        maListeAvecToutesLesNotes.append(i)
    maxi = max(maList)
    mini = min(maList)
    monDicoAvecLesNoteHautes[key] = maxi
    monDicoAvecLesNoteBasses[key] = mini

#MAXIMUM
max_value = max(monDicoAvecLesNoteHautes.values())
max_keys = [k for k, v in monDicoAvecLesNoteHautes.items() if v == max_value]

#MINIMUM
min_value = min(monDicoAvecLesNoteBasses.values())
min_keys = [k for k, v in monDicoAvecLesNoteBasses.items() if v == min_value]

#AVERAGE
SUM = 0
for i in maListeAvecToutesLesNotes:
    SUM+=i

AVG = SUM / len(maListeAvecToutesLesNotes)

for _ in range(5):
    print("------------------------")
print("-------RESULTS--------\n")
print(f"La note maximale est de {max_value}, obtenue en {max_keys} \n La note minimale est de {min_value}, obtenue en {min_keys} \nEt pour FInir la Moyenne globale est de {AVG} ")