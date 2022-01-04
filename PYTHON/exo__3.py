from time import *
from datetime import *
import re

'''
Arg(s) :
uneAnnee, integer
return(s):
Boolean
'''
def obtenirAge(uneAnnee):
    if not isinstance(uneAnnee, int) or uneAnnee < 0 or uneAnnee > datetime.now().year:
        raise ValueError('Invalide')
    else :
        return datetime.now().year - uneAnnee


'''
Arg(s) :
n1, float, n2, float
return(s):
float
'''
def multiplier(n1, n2):
    if not isinstance(n1, float) and not isinstance(n2, float):
        raise ValueError('Invalide')
    else:
        return n1*n2


'''
Arg(s) :
email, string
return(s):
Boolean
'''
def verifierMail(email):
    if not isinstance(email, str):
        raise ValueError('Invalide')
    #les taille minimale "a@b.cc"
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


#print(obtenirAge(int(input("\n\n\nEntrez une année :\n"))))
#print(multiplier(float(input("\n\n\nEntrez un nombre 1 :\n")), float(input("\nEntrez un nombre 2 :\n"))))
print("OK" if verifierMail(input("\n\n\nEntrez un email :\n")) else "NOK")
