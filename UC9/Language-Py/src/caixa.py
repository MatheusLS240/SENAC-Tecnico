from sys import argv

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class Caixa(QWidget):
    def __init__(self):
        super().__init__()
        self.linha = 0
        self.valor_total = 0.0

        # Configurações da janela
        self.setWindowTitle("Caixa da Padaria")
        self.setGeometry(150, 50, 1600, 900)
        self.setWindowIcon(QIcon("Language-Py/src/icons/icone.png"))

        # Layout principal
        self.layout_principal = QHBoxLayout()

        # =========================
        # Coluna esquerda
        # =========================
        self.coluna_esquerda = QWidget()
        self.coluna_esquerda.setStyleSheet("background-color: #590504;")
        self.coluna_esquerda.setFixedWidth(800)

        self.layout_esquerda = QVBoxLayout()

        self.logo = QLabel()
        self.logo.setPixmap(QPixmap("Language-Py/src/img/logo.png").scaled(400, 400))
        self.logo.setScaledContents(True)

        self.coluna_esquerda.setLayout(self.layout_esquerda)
        self.label_cod_produto = QLabel("Código do Produto:")
        self.label_cod_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_cod_produto = QLineEdit()
        self.edit_cod_produto.setStyleSheet("""
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
            
        self.label_nome_produto = QLabel("Nome do Produto:")
        self.label_nome_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_nome_produto = QLineEdit()
        self.edit_nome_produto.setStyleSheet("""
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
        
        self.label_descricao_produto = QLabel("Descricao do Produto:")
        self.label_descricao_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_descricao_produto = QLineEdit()
        self.edit_descricao_produto.setFixedHeight(80)
        self.edit_descricao_produto.setStyleSheet("""
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
        
        self.label_qtd_produto = QLabel("Quantidade do Produto:")
        self.label_qtd_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_qtd_produto = QLineEdit()
        self.edit_qtd_produto.setStyleSheet("""
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
        
        self.label_preco_unitario_produto = QLabel("Preço unitário do Produto:")
        self.label_preco_unitario_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_preco_unitario_produto = QLineEdit()
        self.edit_preco_unitario_produto.setStyleSheet("""
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

        self.label_subtotal_produto = QLabel("Sub Total:")
        self.label_subtotal_produto.setStyleSheet("font-weight: bold; font-size: 16px; color: #ffffff;")
        self.edit_subtotal_produto = QLineEdit("Pressione F3 para calcular o subtotal")
        self.edit_subtotal_produto.setStyleSheet("font-size: 14px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")
        self.edit_subtotal_produto.setEnabled(False)

        self.layout_esquerda.addWidget(self.logo)
        self.layout_esquerda.addWidget(self.label_cod_produto)
        self.layout_esquerda.addWidget(self.edit_cod_produto)
        self.layout_esquerda.addWidget(self.label_nome_produto)
        self.layout_esquerda.addWidget(self.edit_nome_produto)
        self.layout_esquerda.addWidget(self.label_descricao_produto)
        self.layout_esquerda.addWidget(self.edit_descricao_produto)
        self.layout_esquerda.addWidget(self.label_qtd_produto)
        self.layout_esquerda.addWidget(self.edit_qtd_produto)
        self.layout_esquerda.addWidget(self.label_preco_unitario_produto)
        self.layout_esquerda.addWidget(self.edit_preco_unitario_produto)
        self.layout_esquerda.addWidget(self.label_subtotal_produto)
        self.layout_esquerda.addWidget(self.edit_subtotal_produto)

        # =========================
        # Coluna direita
        # =========================
        self.coluna_direita = QWidget()

        self.layout_direita = QVBoxLayout()

        self.table_produtos = QTableWidget()
        self.table_cabecalho = ["Cod. Produto", "Nome do Produto", "Quantidade", "Preço", "Sub Total"]
        self.table_produtos.setColumnCount(5)
        self.table_produtos.setHorizontalHeaderLabels(self.table_cabecalho)
        self.table_produtos.setRowCount(20)

        self.label_total_pagar = QLabel("Total a pagar:")
        self.label_total_pagar.setStyleSheet("font-size: 60px;")
        self.edit_total_pagar = QLineEdit("0,00")
        self.edit_total_pagar.setStyleSheet("font-size: 60px; padding: 5px; background-color: #ffffff; color: #000000; border: 1px solid #cccccc; border-radius: 5px;")
        self.edit_total_pagar.setEnabled(False)

        self.layout_direita.addWidget(self.table_produtos)
        self.layout_direita.addWidget(self.label_total_pagar)
        self.layout_direita.addWidget(self.edit_total_pagar)
    
        self.coluna_direita.setLayout(self.layout_direita)

        # =========================
        # Adiciona colunas
        # =========================
        self.layout_principal.addWidget(self.coluna_esquerda)
        self.layout_principal.addWidget(self.coluna_direita)

        self.setLayout(self.layout_principal)

        self.keyPressEvent = self.keyPressEvent
    
    def keyPressEvent(self, e):
        if(e.key() == Qt.Key.Key_F3):
            sub = float(self.edit_qtd_produto.text()) * float(self.edit_preco_unitario_produto.text())
            self.edit_subtotal_produto.setText(str(sub))
            
            self.table_produtos.setItem(self.linha, 0, QTableWidgetItem(self.edit_cod_produto.text()))
            self.table_produtos.setItem(self.linha, 1, QTableWidgetItem(self.edit_nome_produto.text()))
            self.table_produtos.setItem(self.linha, 2, QTableWidgetItem(self.edit_qtd_produto.text()))
            self.table_produtos.setItem(self.linha, 3, QTableWidgetItem(self.edit_preco_unitario_produto.text()))
            self.table_produtos.setItem(self.linha, 4, QTableWidgetItem(self.edit_subtotal_produto.text()))

            self.linha += 1
            self.valor_total += sub

            self.edit_total_pagar.setText(str(self.valor_total))

            self.edit_cod_produto.clear()
            self.edit_nome_produto.clear()
            self.edit_descricao_produto.clear()
            self.edit_qtd_produto.clear()
            self.edit_preco_unitario_produto.clear()
            self.edit_subtotal_produto.setText("Pressione F3 para calcular o subtotal")

app = QApplication(argv)
janela = Caixa()
janela.show()
app.exec()