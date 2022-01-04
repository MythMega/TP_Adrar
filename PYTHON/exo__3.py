from time import *
from datetime import *
import re

def obtenirAge(uneAnnee):
    if not isinstance(uneAnnee, int):
        return "Error"
    else :
        return datetime.now().year - uneAnnee

def multiplier(n1, n2):
    return n1*n2

def verifierMail(email):
    #les taille minimale "a@b.cc"
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


print(obtenirAge(input("\n\n\nEntrez une année :\n")))
print(multiplier(input("\n\n\nEntrez un nombre 1 :\n"), input("\nEntrez un nombre 2 :\n")))
print(verifierMail(input("\n\n\nEntrez un email :\n")))
















#def verifierMail_sansRegex(email):
    ##verfier si c'est un string (héhé pas d'erreur si simple)
    #if not isinstance(email, str):
    #    return False
    ## step 1, verifier l'absence d'espace
    #if email == email.split()[0]:
    #    return False
    #arobase = False
    #dot = False
    ## step 2, verifier le @
    #for i in email:
    #    if i == "@":
    #        arobase = True
    #if arobase == False:
    #    return False
    ##diviser le mail en deux partie
    #part_1_of_email = email.split("@")[0]
    #part_2_of_email = email.split("@")[1]
    ##verifier le point dans la partie deux
    #for i in part_2_of_email:
    #    if i == ".":
    #        dot == True
    #if dot == False:
    #    return False
    ##diviser la deuxieme partie
    #part_2_1_of_email = part_2_of_email.split(".")[0]
    #part_2_2_of_email = part_2_of_email.split(".")[1]
    #if len(part_1_of_email) < 3 or len(part_1_of_email) > 20:
    #    return False
    #if len(part_2_1_of_email) < 2 or len(part_2_2_of_email) < 20:
    #    return False


