from datetime import *

class Sportif:
    def __init__(self, firstname, name, birthyear, categorie = ""):
        self._name = name
        self._firstname = firstname
        self._birthyear = birthyear
        self._mail = f"{firstname[0].upper()}.{name}@baton-rouge.fr"
        self._categorie = ""
    

    def attribuerCategorie(self):
        result = ""
        age_premier_janvier = datetime.now().year - self._birthyear
        if age_premier_janvier < 6 or age_premier_janvier > 40:
            result = "Non Admis"
        elif age_premier_janvier < 12:
            result = "Poussin"
        elif age_premier_janvier < 18:
            result = "Cadet"
        elif age_premier_janvier < 24:
            result = "Junior"
        elif age_premier_janvier < 30:
            result = "Semi-pro"
        elif age_premier_janvier <= 40:
            result = "Pro"
        self._categorie = result