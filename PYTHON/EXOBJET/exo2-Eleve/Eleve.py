import utilsJM

class Eleve:

    global les_sections
    les_sections = ["CE1", "CE2", "CM1", "CM2", "ANCIEN"]

    def __init__(self, last_name, first_name, years_old):
        self._last_name = last_name
        self._first_name = first_name
        self._years_old = years_old
        self._section = "NONE"

    def initailizeSection(self):
        yo = self._years_old
        if yo < 8:
            self._section = "CE1"
        elif yo == 8:
            self._section = "CE2"
        elif yo == 9:
            self._section = "CM1"
        elif yo == 10:
            self._section = "CM2"
        elif yo > 10:
            self._section = "ANCIENS"

    def _getSection(self):
        return self._section
    def _getLastName(self):
        return self._last_name
    def _getFirstName(self):
        return self._first_name
    def _getYearsOld(self):
        return self._years_old

    def _setSection(self, section="none"):
        #global les_sections
        section = section.upper()
        if section in les_sections:
            old_section = self._section
            self._section = section
            print(f"L'élève a bien été transféré de {old_section} vers {section}")

    def anniversaire(self):
        print(f"L'age de {self._first_name} {self._last_name[0]} passe de {self._years_old} à {self._years_old+1}")
        self._years_old += 1
        old_section = self._section
        index = les_sections.index(self._section)
        if self._section != "ANCIEN":
            self._section = les_sections[index+1]
        print(f"\nCet élève est passé de {old_section} à {self._section}")


    def getAllInfos(self):
        return "[" + self._section + "] " + self._last_name + " " + self._first_name


def getAllSection():
    return les_sections