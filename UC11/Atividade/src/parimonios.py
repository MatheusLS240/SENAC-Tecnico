import mysql.connector as conn  # type: ignore

class Parimonios:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_patrimonios(self, numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por, atualizado_por):
        if type(numero_tombamento) != str or numero_tombamento.strip() == "":
            return "Não foi possível cadastrar o patrimônio: o número de tombamento está vazio ou contém caracteres inválidos."
        elif type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar o patrimônio: o nome está vazio ou contém caracteres inválidos."
        elif type(curso_id) != int or curso_id <= 0:
            return "Não foi possível cadastrar o patrimônio: informe um curso válido."
        elif type(local_id) != int or local_id <= 0:
            return "Não foi possível cadastrar o patrimônio: informe um local válido."
        elif type(categoria_id) != int or categoria_id <= 0:
            return "Não foi possível cadastrar o patrimônio: informe uma categoria válida."
        elif type(status) != str or status.strip() == "":
            return "Não foi possível cadastrar o patrimônio: informe um status válido."
        elif type(valor_aquisicao) not in [int, float] or valor_aquisicao < 0:
            return "Não foi possível cadastrar o patrimônio: informe um valor de aquisição válido."
        elif data_aquisicao is None:
            return "Não foi possível cadastrar o patrimônio: informe uma data de aquisição válida."
        elif type(criado_por) != int or criado_por <= 0:
            return "Não foi possível cadastrar o patrimônio: informe um usuário válido para o campo criado por."
        elif type(atualizado_por) != int or atualizado_por <= 0:
            return "Não foi possível cadastrar o patrimônio: informe um usuário válido para o campo atualizado por."
        return None

    def cadastrar_patrimonio(self, numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por):
        erro = self.validar_patrimonios(numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por, criado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM patrimonios WHERE numero_tombamento=%s"
        self.cursor.execute(sql_select, (numero_tombamento,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Patrimônio já cadastrado. Por favor, cadastre outro!"
        sql_insert = "INSERT INTO patrimonios(numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql_insert, (numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por))
        self.conexao.commit()
        return "Patrimônio cadastrado com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por, atualizado_por, criado_em, atualizado_em FROM usuarios"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, criado_por, atualizado_por, criado_em, atualizado_em FROM usuarios WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_patrimonio(self, id, numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, atualizado_por, atualizado_em):
        erro = self.validar_patrimonios(numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, atualizado_por, atualizado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM patrimonios WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Patrimônio não encontrado. Por favor, digite outro ID!"
        sql_select_tombamento = "SELECT id FROM patrimonios WHERE numero_tombamento=%s AND id != %s"
        self.cursor.execute(sql_select_tombamento, (numero_tombamento, id))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Já existe outro patrimônio com esse número de tombamento. Por favor, informe outro!"
        sql_update = "UPDATE patrimonios SET numero_tombamento=%s, nome=%s, curso_id=%s, local_id=%s, categoria_id=%s, status=%s, valor_aquisicao=%s, data_aquisicao=%s, atualizado_por=%s, atualizado_em=%s WHERE id=%s"
        self.cursor.execute(sql_update, (numero_tombamento, nome, curso_id, local_id, categoria_id, status, valor_aquisicao, data_aquisicao, atualizado_por, atualizado_em, id))
        self.conexao.commit()
        return "Patrimônio atualizado com sucesso!"

    def deletar_patrimonio(self, id):
        sql_delete = "DELETE FROM patrimonios WHERE id=%s"
        self.cursor.execute(sql_delete, (id,))
        self.conexao.commit()
        return "Patrimônio excluído com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()