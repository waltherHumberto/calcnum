
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
        self.calbut.clicked.connect(lambda: self.gera_interpolacao()) # Inicia a conexão do botão inicia com o evento 

    def gera_interpolacao(self):
        self.resposta_edit.append("L(x)=−12x2+52x−1 ")
        
    def sair():
        quit()
    
app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')
window = Ui()
app.exec_()

