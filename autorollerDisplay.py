import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import autoroller


class InputFields(QWidget):
    def __init__(self, title):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        #Title of input field.
        self.label = QLabel()
        self.label.setText(title)
        layout.addWidget(self.label)
        
        #Input field.
        self.lineEdit = QLineEdit(self)
        #self.lineEdit.setValidator(QIntValidator)
        layout.addWidget(self.lineEdit)
        
        #Keeps the label and the input box scaled and put together.
        layout.addStretch()
        
        #Getter
    def GetInput(self):
        return int(self.lineEdit.text())
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Autoroller")
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        
        
        mainLayout = QVBoxLayout()
        centralWidget.setLayout(mainLayout)
        
        self.outputDisplay = QLabel("Result")
        self.outputDisplay.setWordWrap(True)
        self.outputDisplay.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainLayout.addWidget(self.outputDisplay, stretch=1)
        
        self.addIntInputsPanel(mainLayout)
        self.addButton(mainLayout)
        self.show()
        
    def addIntInputsPanel(self, parentLayout):
        hlayout = QHBoxLayout()
        self.numberOfAttacks = InputFields("Number of Attacks: ")
        self.ACToBeat = InputFields("AC to Beat: ")
        self.attackModifier = InputFields("Attack Bonus: ")
        self.damageModifier = InputFields("Damage Bonus: ")
        self.damageDice = InputFields("Dice Size: ")
        self.dicePerAttack = InputFields("Dice Amount: ")
        
        hlayout.addWidget(self.numberOfAttacks)
        hlayout.addWidget(self.ACToBeat)
        hlayout.addWidget(self.attackModifier)
        hlayout.addWidget(self.damageModifier)
        hlayout.addWidget(self.damageDice)
        hlayout.addWidget(self.dicePerAttack)
        
        parentLayout.addLayout(hlayout)
    
    def addButton(self, parentLayout):
        self.button = QPushButton("Roll!")
        self.button.clicked.connect(self.buttonAction)
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button)
        parentLayout.addLayout(hlayout)
    
    
    def buttonAction(self):
        numberOfAttacks = int(self.numberOfAttacks.GetInput())
        ACToBeat = int(self.ACToBeat.GetInput())
        attackModifier = int(self.attackModifier.GetInput())
        damageModifier = int(self.damageModifier.GetInput())
        damageDice = int(self.damageDice.GetInput())
        dicePerAttack = int(self.dicePerAttack.GetInput())
        
        output = autoroller.autoroller(numberOfAttacks, ACToBeat, attackModifier, damageModifier, damageDice, dicePerAttack)
        self.outputDisplay.setText(str("Total damage: {0}<br>Crits: {1}<br>Hits: {2}<br>Misses: {3}".format(output[1], output[2], output[3], output[4])))
        






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()