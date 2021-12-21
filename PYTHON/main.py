import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox

def etat_change(etat):
    print("action sur la case")
    if etat == Qt.Checked:
        print("coche")
    else:
        print("decoche")

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

case = QCheckBox("Voici ma premiere case a  cocher")
case.stateChanged.connect(etat_change)
case.show()

app.exec_()