from sys import argv
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Janela(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro")
        self.setWindowIcon(QIcon("Language-Py/src/icons/icone2.png"))
        self.setGeometry(150, 50, 1000, 600)
        self.setFixedSize(1000, 600)
        
        # Coluna esquerda
        self.coluna_esquerda = QWidget()
        self.coluna_esquerda.setStyleSheet("background-color: #FFFFFF;")

        self.layout_esquerda = QVBoxLayout()

        self.cachorro = QLabel()
        self.cachorro.setPixmap(QPixmap("Language-Py/src/img/cachorro.jpeg"))
        self.cachorro.setScaledContents(True)

        self.layout_esquerda.addWidget(self.cachorro)
        self.coluna_esquerda.setLayout(self.layout_esquerda)

        # Coluna direita
        self.coluna_direita = QWidget()
        self.coluna_direita.setStyleSheet("background-color: #FFFFFF;")

        self.label_title = QLabel("Seja voluntário!")
        self.label_title.setStyleSheet("font-size: 24px; font-weight: bold; color: #FF5C00;")

        self.label_descricao = QLabel("E ajude um aumigo encontrar um lar")
        self.label_descricao.setStyleSheet("font-size: 16px; ")

        self.label_nome = QLabel("Seu nome:")
        self.label_nome.setStyleSheet("font-weight: bold")
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("padding: 10px 20px; border-radius: 5px; border: 2px solid #e0e0e0;")

        self.label_email = QLabel("Seu email:")
        self.label_email.setStyleSheet("font-weight: bold")
        self.edit_email = QLineEdit()
        self.edit_email.setStyleSheet("padding: 10px 20px; border-radius: 5px; border: 2px solid #e0e0e0;")

        self.label_senha = QLabel("Sua senha:")
        self.label_senha.setStyleSheet("font-weight: bold")
        self.edit_senha = QLineEdit()
        self.edit_senha.setStyleSheet("padding: 10px 20px; border-radius: 5px; border: 2px solid #e0e0e0;")
        self.edit_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.button_cadastrar = QPushButton("Cadastrar")
        self.button_cadastrar.setStyleSheet("""
                                                QPushButton {
                                                    background-color: #FF5C00; 
                                                    border: none; 
                                                    color: #FFFFFF; 
                                                    padding: 10px 20px;
                                                    border-radius: 5px;
                                                }
                                            
                                                QPushButton:hover {
                                                    background-color: #689f38;
                                                }
                                            """)
        self.button_cad_google = QPushButton("Continuar com Google")
        self.button_cad_google.setStyleSheet("""
                                                QPushButton {
                                                    background-color: #c62828; 
                                                    border: none; 
                                                    color: #FFFFFF; 
                                                    padding: 10px 20px;
                                                    border-radius: 5px;
                                                }
                                            
                                                QPushButton:hover {
                                                    background-color: #f44336;
                                                }
                                            """)
        self.button_cad_facebook = QPushButton("Continuar com Facebook")
        self.button_cad_facebook.setStyleSheet("""
                                                QPushButton {
                                                    background-color: #01579b; 
                                                    border: none; 
                                                    color: #FFFFFF; 
                                                    padding: 10px 20px;
                                                    border-radius: 5px;
                                                }
                                            
                                                QPushButton:hover {
                                                    background-color: #0288d1;
                                                }
                                            """)

        self.layout_direita = QVBoxLayout()
        self.layout_direita.addWidget(self.label_title)
        self.layout_direita.addWidget(self.label_descricao)
        self.layout_direita.addWidget(self.label_nome)
        self.layout_direita.addWidget(self.edit_nome)
        self.layout_direita.addWidget(self.label_email)
        self.layout_direita.addWidget(self.edit_email)
        self.layout_direita.addWidget(self.label_senha)
        self.layout_direita.addWidget(self.edit_senha)
        self.layout_direita.addWidget(self.button_cadastrar)
        self.layout_direita.addWidget(self.button_cad_google)
        self.layout_direita.addWidget(self.button_cad_facebook)
        self.layout_direita.setAlignment(self.label_title, Qt.AlignmentFlag.AlignCenter)
        self.layout_direita.setAlignment(self.label_descricao, Qt.AlignmentFlag.AlignCenter)
        self.coluna_direita.setLayout(self.layout_direita)

        # Janela
        self.layoutH = QHBoxLayout()
        self.layoutH.addWidget(self.coluna_esquerda)
        self.layoutH.addWidget(self.coluna_direita)
        self.layoutH.setSpacing(0)

        self.setStyleSheet("background-color: #FF5C00;")
        self.setLayout(self.layoutH)


app = QApplication(argv)
janela = Janela()
janela.show()
app.exec()