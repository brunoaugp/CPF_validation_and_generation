# converter arquivo PyQT5 para .py: digitar no terminal: pyuic5 design2.ui -o design2.py
# p terminal deve estar na pasta que o arquivo está

import sys
from validacpf import valida_cpf
from gerador_cpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design2

print(gera_cpf())

class GeraValidaCPF(QMainWindow, design2.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGeraCPF.clicked.connect(self.gera_cpf)  # atribui a funcao de gerar cpf ao botao
        self.btnValidaCPF.clicked.connect(self.valida_cpf)  # atribui a funcao de validar cpf ao botao

    def gera_cpf(self): #escreve o retono da funcao gera_cpf na label no app
        self.labelRetorno.setText(
            str(gera_cpf())  # escreve na label de retorno do app a resposta da funcao cpf
        )

    def valida_cpf(self):
        cpf = self.inputValidaCPF.text()  # atibui o input na label na variavel cpf
        self.labelRetorno.setText(
            str(valida_cpf(cpf))  # escreve na label de retorno do app a resposta da funcao cpf
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
