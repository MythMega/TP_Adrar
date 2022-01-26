from Eleve import *
import utilsJM

ecole = []

while True:
    user = input("Who are you ? \n (type prof or secr) \n")
    user = user.upper()
    if user != "PROF" and user != "SECR" and user != "DEBUG":
        utilsJM.retype()
    else:
        connected = True
        while connected :
            erroredAction = True
            utilsJM.clearConsole()
            if user == "SECR":
                while erroredAction:
                    action = int(input("\nwhat do you want to do ?\n1 : add new student\n2 : declare birthday\n3 : disconnect\n\n"))
                    if action < 1 or action > 3:
                        utilsJM.retype()
                    else:
                        erroredAction = False
                        utilsJM.clearConsole()
                if action == 3:
                    connected = False
                elif action == 2:
                    if len(ecole) < 1:
                        print("there's no student !")
                        utilsJM.waitInput(True)
                    else:
                        print("student list :\n\n")
                        for i in range(len(ecole)):
                            print(f"{i} : {ecole[i].getAllInfos()}\n")
                        id_eleve = int(input("de quel élève c'est l'anniversaire ?\n"))
                        ecole[id_eleve].anniversaire()
                        utilsJM.waitInput()
                elif action == 1:
                    futur_eleve_name = input("His name :")
                    futur_eleve_fname = input("His first name :")
                    futur_eleve_yo = int(input("His Years old :"))
                    futur_eleve = Eleve(futur_eleve_name, futur_eleve_fname, futur_eleve_yo)
                    futur_eleve.initailizeSection()
                    ecole.append(futur_eleve)
                    print("---success---")
                    utilsJM.waitInput(True)
                    utilsJM.clearConsole()
            if user == "PROF":
                action = int(input("\nwhat do you want to do ?\n1 : Change section of a student\n2 : disconnect\n\n"))
                print("student list :\n\n")
                for i in range(len(ecole)):
                    print(f"{i} : {ecole[i].getAllInfos()}\n")
                id_eleve = int(input("Choose a student?\n"))
                les_sections = getAllSection()
                utilsJM.clearConsole()
                for i in range(len(les_sections)):
                    print(f"{i} : {les_sections[i]}")
                choice = int(input("Choose a new section : "))
                ecole[id_eleve]._setSection(les_sections[choice])