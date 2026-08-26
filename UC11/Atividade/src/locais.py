import mysql.connector as conn  # type: ignore

class Locais:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_local(self, nome, descricao, criado_por):
        if type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar o local: o nome está vazio ou contém caracteres inválidos."
        elif type(descricao) != str or descricao.strip() == "":
            return "Não foi possível cadastrar o local: a descrição está vazia ou contém caracteres inválidos."
        elif type(criado_por) != int or criado_por <= 0:
            return "Não foi possível cadastrar o local: informe um usuário válido para o campo criado por."
        return None

    def cadastrar_local(self, nome, descricao, criado_por):
        erro = self.validar_local(nome, descricao, criado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM locais WHERE nome=%s"
        self.cursor.execute(sql_select, (nome,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Local já cadastrado. Por favor, cadastre outro!"
        sql_insert = "INSERT INTO locais(nome, descricao, criado_por) VALUES (%s, %s, %s)"
        self.cursor.execute(sql_insert, (nome, descricao, criado_por))
        self.conexao.commit()
        return "Local cadastrado com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, nome, descricao, criado_por FROM locais"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT id, nome, descricao, criado_por FROM locais WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_local(self, nome, descricao, criado_por, id_local):
        erro = self.validar_local(nome, descricao, criado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM locais WHERE id=%s"
        self.cursor.execute(sql_select, (id_local,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Local não encontrado. Por favor, digite outro ID!"
        sql_select_nome = "SELECT id FROM locais WHERE nome=%s AND id != %s"
        self.cursor.execute(sql_select_nome, (nome, id_local))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Já existe outro local com esse nome. Por favor, escolha outro!"
        sql_update = "UPDATE locais SET nome=%s, descricao=%s, criado_por=%s WHERE id=%s"
        self.cursor.execute(sql_update, (nome, descricao, criado_por, id_local))
        self.conexao.commit()
        return "Local atualizado com sucesso!"

    def deletar_local(self, id_local):
        sql_delete = "DELETE FROM locais WHERE id=%s"
        self.cursor.execute(sql_delete, (id_local,))
        self.conexao.commit()
        return "Local excluído com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()