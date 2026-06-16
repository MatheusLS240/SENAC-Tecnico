from sys import argv

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
)
from PyQt6.QtGui import QPixmap


class Caixa(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150, 50, 1600, 900)

        # Layout principal
        layout_principal = QHBoxLayout()

        # =========================
        # Coluna esquerda
        # =========================
        coluna_esquerda = QWidget()
        coluna_esquerda.setStyleSheet("background-color: #660000;")
        coluna_esquerda.setFixedWidth(800)

        layout_esquerda = QVBoxLayout()

        logo = QLabel()
        logo.setPixmap(QPixmap("/home/senac/Documentos/Programacao/Language-Py/src/img/logo.png").scaled(400, 200))
        logo.setScaledContents(True)

        coluna_esquerda.setLayout(layout_esquerda)
        label_cod_produto = QLabel("Código do Produto:")
        label_cod_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_cod_produto = QLineEdit()
        edit_cod_produto.setStyleSheet("font-size: 14px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")
        
        label_nome_produto = QLabel("Nome do Produto:")
        label_nome_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_nome_produto = QLineEdit()
        edit_nome_produto.setStyleSheet("font-size: 14px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")

        label_nome_produto = QLabel("Nome do Produto:")
        label_nome_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_nome_produto = QLineEdit()
        edit_nome_produto.setStyleSheet("font-size: 14px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")

        layout_esquerda.addWidget(logo)
        layout_esquerda.addWidget(label_cod_produto)
        layout_esquerda.addWidget(edit_cod_produto)
        layout_esquerda.addWidget(label_nome_produto)
        layout_esquerda.addWidget(edit_nome_produto)

        # =========================
        # Coluna direita
        # =========================
        coluna_direita = QWidget()
        coluna_direita.setStyleSheet("background-color: #A6A6A6;")

        layout_direita = QVBoxLayout()

        titulo = QLabel("Coluna Direita")
        layout_direita.addWidget(titulo)

        coluna_direita.setLayout(layout_direita)

        # =========================
        # Adiciona colunas
        # =========================
        layout_principal.addWidget(coluna_esquerda)
        layout_principal.addWidget(coluna_direita)

        self.setLayout(layout_principal)


app = QApplication(argv)

janela = Caixa()
janela.show()

app.exec()