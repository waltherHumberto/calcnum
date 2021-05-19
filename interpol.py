
from PyQt5 import QtWidgets, uic
import time
import pyautogui
import keyboard
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('calc.ui', self)
        self.show()
        self.resposta_edit.clear()
        self.comboBox.currentIndexChanged.connect(lambda: self.escolhe_metodo()) # Inicia a conexão do botão inicia com o evento 

    def escolhe_metodo(self):
        if(self.comboBox.currentText()== "Newton"):
            self.calbut.disconnect()
            self.calbut.clicked.connect(lambda: self.escolhe_metodo()) # Inicia a conexão do botão inicia com o evento 
        if(self.comboBox.currentText()== "Lagrange"):
            self.calbut.disconnect()
            self.calbut.clicked.connect(lambda: self.escolhe_metodo()) # Inicia a conexão do botão inicia com o evento 
        if(self.comboBox.currentText()== "Gregory-Newton"):
            self.calbut.disconnect()
            self.calbut.clicked.connect(lambda: self.escolhe_metodo()) # Inicia a conexão do botão inicia com o evento 

    def sair():
        quit()
    
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = Ui()
app.exec_()

