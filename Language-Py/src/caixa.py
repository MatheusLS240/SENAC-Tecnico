from sys import argv

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTableWidget,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Caixa(QWidget):
    def __init__(self):
        super().__init__()

        # Configurações da janela
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
        logo.setPixmap(QPixmap("img/logo.png"))
        logo.setScaledContents(True)

        coluna_esquerda.setLayout(layout_esquerda)
        label_cod_produto = QLabel("Código do Produto:")
        label_cod_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_cod_produto = QLineEdit()
        edit_cod_produto.setStyleSheet("""
                                        QLineEdit {
                                            font-size: 14px; 
                                            padding: 5px; 
                                            background-color: 
                                            rgba(255, 255, 255, 128); 
                                            color: #000000; 
                                            border: none; 
                                            border-radius: 5px;
                                        }
                                       
                                        QLineEdit:focus {
                                            background-color: #FFFFFF;
                                        }                                         
                                                """)    
            
        label_nome_produto = QLabel("Nome do Produto:")
        label_nome_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_nome_produto = QLineEdit()
        edit_nome_produto.setStyleSheet("""
                                            QLineEdit {
                                                font-size: 14px; 
                                                padding: 5px; 
                                                background-color: 
                                                rgba(255, 255, 255, 128); 
                                                color: #000000; 
                                                border: none; 
                                                border-radius: 5px;
                                            }
                                        
                                            QLineEdit:focus {
                                                background-color: #FFFFFF;
                                            }                                         
                                        """)
        
        label_descricao_produto = QLabel("Descricao do Produto:")
        label_descricao_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_descricao_produto = QLineEdit()
        edit_descricao_produto.setFixedHeight(80)
        edit_descricao_produto.setStyleSheet("""
                                                QLineEdit {
                                                    font-size: 14px; 
                                                    padding: 5px; 
                                                    background-color: 
                                                    rgba(255, 255, 255, 128); 
                                                    color: #000000; 
                                                    border: none; 
                                                    border-radius: 5px;
                                                }
                                             
                                                QLineEdit:focus {
                                                    background-color: #FFFFFF;
                                                }                                         
                                            """)
        
        label_qtd_produto = QLabel("Quantidade do Produto:")
        label_qtd_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_qtd_produto = QLineEdit()
        edit_qtd_produto.setStyleSheet("""
                                        QLineEdit {
                                            font-size: 14px; 
                                            padding: 5px; 
                                            background-color: 
                                            rgba(255, 255, 255, 128); 
                                            color: #000000; 
                                            border: none; 
                                            border-radius: 5px;
                                        }
                                       
                                        QLineEdit:focus {
                                            background-color: #FFFFFF;
                                        }                                         
                                    """)
        
        label_preco_unitario_produto = QLabel("Preço unitário do Produto:")
        label_preco_unitario_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_preco_unitario_produto = QLineEdit()
        edit_preco_unitario_produto.setStyleSheet("""
                                                    QLineEdit {
                                                        font-size: 14px; 
                                                        padding: 5px; 
                                                        background-color: 
                                                        rgba(255, 255, 255, 128); 
                                                        color: #000000; 
                                                        border: none; 
                                                        border-radius: 5px;
                                                    }
                                                  
                                                    QLineEdit:focus {
                                                        background-color: #FFFFFF;
                                                    }                                         
                                                """)

        label_subtotal_produto = QLabel("Sub Total:")
        label_subtotal_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        edit_subtotal_produto = QLineEdit("Pressione F3 para calcular o subtotal")
        edit_subtotal_produto.setStyleSheet("font-size: 14px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")
        edit_subtotal_produto.setEnabled(False)

        layout_esquerda.addWidget(logo)
        layout_esquerda.addWidget(label_cod_produto)
        layout_esquerda.addWidget(edit_cod_produto)
        layout_esquerda.addWidget(label_nome_produto)
        layout_esquerda.addWidget(edit_nome_produto)
        layout_esquerda.addWidget(label_descricao_produto)
        layout_esquerda.addWidget(edit_descricao_produto)
        layout_esquerda.addWidget(label_qtd_produto)
        layout_esquerda.addWidget(edit_qtd_produto)
        layout_esquerda.addWidget(label_preco_unitario_produto)
        layout_esquerda.addWidget(edit_preco_unitario_produto)
        layout_esquerda.addWidget(label_subtotal_produto)
        layout_esquerda.addWidget(edit_subtotal_produto)

        # =========================
        # Coluna direita
        # =========================
        coluna_direita = QWidget()

        layout_direita = QVBoxLayout()

        table_produtos = QTableWidget()
        table_cabecalho = ["Cod. Produto", "Nome do Produto", "Quantidade", "Preço", "Sub Total"]
        table_produtos.setColumnCount(5)
        table_produtos.setHorizontalHeaderLabels(table_cabecalho)
        table_produtos.setRowCount(20)

        label_total_pagar = QLabel("Total a pagar:")
        label_total_pagar.setStyleSheet("font-size: 60px;")
        edit_total_pagar = QLineEdit("0,00")
        edit_total_pagar.setStyleSheet("font-size: 60px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")
        edit_total_pagar.setEnabled(False)

        layout_direita.addWidget(table_produtos)
        layout_direita.addWidget(label_total_pagar)
        layout_direita.addWidget(edit_total_pagar)
    

        coluna_direita.setLayout(layout_direita)

        # =========================
        # Adiciona colunas
        # =========================
        layout_principal.addWidget(coluna_esquerda)
        layout_principal.addWidget(coluna_direita)

        self.setLayout(layout_principal)

        # =========================
        # Criando as funções
        # =========================
        self.keyPressEvent = self.keyPressEvent
    
    def keyPressEvent(self, e):
        if(e.key() == Qt.Key.f3):
            print("VC DIGITOU F3")

app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()