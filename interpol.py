from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QPixmap
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('calc.ui', self)
        self.show()
        self.resposta_edit.clear()
        
        self.lista_x = []
        self.lista_y = []

        self.calbut.clicked.connect(lambda: self.metodo_newton())

        # PUC logo
        self.label_logo_puc = QLabel(self)
        self.label_logo_puc.setGeometry(QRect(393, 25, 20, 20))
        self.logo_puc = QPixmap("puclogo.png")
        self.label_logo_puc.setPixmap(self.logo_puc)

    def conta_quantos_pontos(self):
        i = 0 
        if (self.edit_x.text()== "" or self.edit_y.text()== ""):
            return i
        self.lista_x.clear()
        self.lista_y.clear()
        self.lista_x.append(float(self.edit_x.text())) 
        self.lista_y.append(float(self.edit_y.text())) 
        i=i+1
        if (self.edit_x_2.text()== "" or self.edit_y_2.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_2.text())) 
        self.lista_y.append(float(self.edit_y_2.text())) 
        i=i+1
        if (self.edit_x_3.text()== "" or self.edit_y_3.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_3.text())) 
        self.lista_y.append(float(self.edit_y_3.text())) 

        i=i+1
        if (self.edit_x_4.text()== "" or self.edit_y_4.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_4.text())) 
        self.lista_y.append(float(self.edit_y_4.text())) 

        i=i+1
        if (self.edit_x_5.text()== "" or self.edit_y_5.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_5.text())) 
        self.lista_y.append(float(self.edit_y_5.text())) 

        i=i+1
        if (self.edit_x_6.text()== "" or self.edit_y_6.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_6.text())) 
        self.lista_y.append(float(self.edit_y_6.text())) 

        i=i+1
        if (self.edit_x_7.text()== "" or self.edit_y_7.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_7.text())) 
        self.lista_y.append(float(self.edit_y_7.text())) 

        i=i+1
        if (self.edit_x_8.text()== "" or self.edit_y_8.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_8.text())) 
        self.lista_y.append(float(self.edit_y_8.text())) 

        i=i+1
        if (self.edit_x_9.text()== "" or self.edit_y_9.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_9.text())) 
        self.lista_y.append(float(self.edit_y_9.text())) 

        i=i+1
        if (self.edit_x_10.text()== "" or self.edit_y_10.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_10.text())) 
        self.lista_y.append(float(self.edit_y_10.text()))
        
        i=i+1
        if (self.edit_x_11.text()== "" or self.edit_y_11.text()== ""):
            return i
        self.lista_x.append(float(self.edit_x_11.text())) 
        self.lista_y.append(float(self.edit_y_11.text()))
        i=i+1

        return i


    def metodo_newton(self):
        try:
            self.resposta_edit.clear()
            quant_pontos = self.conta_quantos_pontos()
            print(quant_pontos)
            self.resposta_edit.append(str(quant_pontos) + " Ponto(s)")
            pontos_x,pontos_y= [],[]
            tabela = []

            for i in range(quant_pontos):
                valor_x = float (self.lista_x[i])
                valor_y = float (self.lista_y[i])
                pontos_x.append(valor_x)
                pontos_y.append(valor_y)
            tabela.append(pontos_y)
            x  = float(self.x_estipulado.text())

            passo = 1
            for n in range (quant_pontos-1):
                ordem =[]
                for m in range (len(tabela[n])-1):
                    dif_dividida =((tabela[n][m+1]-tabela[n][m])/(pontos_x[m+passo]-pontos_x[m]))
                    ordem.append(dif_dividida)
                tabela.append(ordem)
                passo +=1

            Valor = 0
            grau = 0

            for i in range(len(tabela)):
                fator= tabela[i][0]
                for j in range(grau):
                    fator*= (x-pontos_x[j])
                grau +=1
                Valor += fator
            self.resposta_edit.append("f("+str(x)+ ") = " +str(Valor))
        except :
            self.resposta_edit.append("Algum Erro Foi Encontrado")


    def sair():
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle('Fusion')
    app.exec_()
