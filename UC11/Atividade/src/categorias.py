import mysql.connector as conn  # type: ignore

class Categorias:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_categoria(self, nome, descricao):
        if type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar a categoria: o nome está vazio ou contém caracteres inválidos."
        elif type(descricao) != str or descricao.strip() == "":
            return "Não foi possível cadastrar a categoria: a descrição está vazia ou contém caracteres inválidos."
        return None

    def cadastrar_categoria(self, nome, descricao):
        erro = self.validar_categoria(nome, descricao)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM categorias WHERE nome=%s"
        self.cursor.execute(sql_select, (nome,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Categoria já cadastrada. Por favor, cadastre outra!"
        sql_insert = "INSERT INTO categorias(nome, descricao) VALUES (%s, %s)"
        self.cursor.execute(sql_insert, (nome, descricao))
        self.conexao.commit()
        return "Categoria cadastrada com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, nome, descricao FROM categorias"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT id, nome, descricao FROM categorias WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_categoria(self, nome, descricao, id_categoria):
        erro = self.validar_categoria(nome, descricao)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM categorias WHERE id=%s"
        self.cursor.execute(sql_select, (id_categoria,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Categoria não encontrada. Por favor, digite outro ID!"
        sql_select_nome = "SELECT id FROM categorias WHERE nome=%s AND id != %s"
        self.cursor.execute(sql_select_nome, (nome, id_categoria))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Já existe outra categoria com esse nome. Por favor, escolha outra!"
        sql_update = "UPDATE categorias SET nome=%s, descricao=%s WHERE id=%s"
        self.cursor.execute(sql_update, (nome, descricao, id_categoria))
        self.conexao.commit()
        return "Categoria atualizada com sucesso!"

    def deletar_categoria(self, id_categoria):
        sql_delete = "DELETE FROM categorias WHERE id=%s"
        self.cursor.execute(sql_delete, (id_categoria,))
        self.conexao.commit()
        return "Categoria excluída com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()