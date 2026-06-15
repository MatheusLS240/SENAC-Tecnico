from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QLabel, QPushButton, QVBoxLayout
import sys

class cadastroProduto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Produto")
        self.setGeometry(750,250,300,450)

        self.nomeL = QLabel("Nome do Produto:")
        self.nomeL.setStyleSheet("QLabel { font-size: 16px; font-weight: bold; }")
        self.nomeE = QLineEdit()

        self.tipoL = QLabel("Tipo do Produto:")
        self.tipoL.setStyleSheet("QLabel { font-size: 16px; font-weight: bold; }")
        self.tipoE = QLineEdit()

        self.precoL = QLabel("Preço do Produto:")
        self.precoL.setStyleSheet("QLabel { font-size: 16px; font-weight: bold; }")
        self.precoE = QLineEdit()

        self.cadastrarB = QPushButton("Cadastrar")
        self.cadastrarB.setStyleSheet("""
                                      QPushButton { 
                                        background-color: #4CAF50; 
                                        color: white; 
                                        border-radius: 10px; 
                                        padding: 5px 10px; 
                                        text-align: center; 
                                        font-size: 16px; 
                                      }
                                      
                                      QPushButton:hover { 
                                        background-color: #45a049;
                                      }
                                      """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(self.nomeL)
        layout.addWidget(self.nomeE)
        layout.addWidget(self.tipoL)
        layout.addWidget(self.tipoE)
        layout.addWidget(self.precoL)
        layout.addWidget(self.precoE)
        layout.addWidget(self.cadastrarB)

app = QApplication(sys.argv)
tela = cadastroProduto()
tela.show()
app.exec()       