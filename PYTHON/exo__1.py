from datetime import date
now = date.today()
exo = int(input("numero d'exo : "))
print("======================")
if exo == 1:
    prenom = input("Votre prenom : ")
    nom = input("Votre nom : ")
    annee = int(input("Votre année de naissance : "))
    age = now.year - annee
    print(f"Bonjour {prenom} {nom}, vous avez {age} ans")
if exo == 2:
    nombre_un = int(input("Donnez un nombre : "))
    nombre_deux = int(input("Donnez un nombre : "))
    nombre_trois = int(input("Donnez un nombre : "))
    resultat = nombre_un + nombre_deux + nombre_trois
    print(f"La somme est {resultat}")
if exo == 3:
    mon_nombre = int(input("Entrez un nombre : "))
    mon_nombre = mon_nombre ** 3
    print(f"Le cube de ce nombre est {mon_nombre}")
if exo == 4:
    mon_nombre = int(input("Entrez un nombre à convertir en binaire puis en Hexa : "))
    binaire = bin(mon_nombre)[2:]
    hexa = hex(mon_nombre)[2:]
    print(f"Ton nombre est {mon_nombre}, en binaire c'est {binaire}, et en hexa, c'est {hexa}")
if exo == 5:
    print("Pour ce qui est des String on a :")
    print(dir(type("Chaine de caractères")))
    print("Pour ce qui est des Integer on a :")
    print(dir(type(5)))
if exo == 6:
    print(len(input("Phrase dont vous voulez calculer la longueur :")))
if exo == 7:
    liste = []
    for _ in range(4):
        liste.append((int(input("Entrez un nombre : "))))
    print(f"le Minimum est {min(liste)} et le maximum est {max(liste)}")