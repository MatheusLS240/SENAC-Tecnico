from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class janela2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minha janela")
        self.setGeometry(10,20,800,400)
        self.texto = QLabel("Olá, seja bem-vindo a minha janela")
        self.botao = QPushButton("Clique aqui")
        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(self.botao)
        self.setLayout(layout)

app = QApplication(sys.argv)
tela = janela2()
tela.show()
app.exec()       