import mysql.connector as conn  # type: ignore

class BaixasPatrimoniais:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_baixa(self, patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa):
        if type(patrimonio_id) != int or patrimonio_id <= 0:
            return "Não foi possível cadastrar a baixa patrimonial: informe um patrimônio válido."
        elif type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar a baixa patrimonial: o nome está vazio ou contém caracteres inválidos."
        elif type(usuario_registro) != int or usuario_registro <= 0:
            return "Não foi possível cadastrar a baixa patrimonial: informe um usuário válido."
        elif type(tipo_baixa) != str or tipo_baixa.strip() == "":
            return "Não foi possível cadastrar a baixa patrimonial: informe um tipo de baixa válido."
        elif type(motivo) != str or motivo.strip() == "":
            return "Não foi possível cadastrar a baixa patrimonial: informe o motivo da baixa."
        elif type(valor_recuperado) not in [int, float] or valor_recuperado < 0:
            return "Não foi possível cadastrar a baixa patrimonial: informe um valor recuperado válido."
        elif type(documento_comprobatorio) != str or documento_comprobatorio.strip() == "":
            return "Não foi possível cadastrar a baixa patrimonial: informe o documento comprobatório."
        elif data_baixa is None:
            return "Não foi possível cadastrar a baixa patrimonial: informe uma data de baixa válida."
        return None

    def cadastrar_baixa(self, patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa):
        erro = self.validar_baixa(patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM baixas_patrimoniais WHERE patrimonio_id=%s"
        self.cursor.execute(sql_select, (patrimonio_id,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Este patrimônio já possui uma baixa patrimonial cadastrada."
        sql_insert = "INSERT INTO baixas_patrimoniais(patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql_insert, (patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa))
        self.conexao.commit()
        return "Baixa patrimonial cadastrada com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa FROM baixas_patrimoniais"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT id, patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa FROM baixas_patrimoniais WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_baixa(self, patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa, id_baixa):
        erro = self.validar_baixa(patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM baixas_patrimoniais WHERE id=%s"
        self.cursor.execute(sql_select, (id_baixa,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Baixa patrimonial não encontrada. Por favor, digite outro ID!"
        sql_select_patrimonio = "SELECT id FROM baixas_patrimoniais WHERE patrimonio_id=%s AND id != %s"
        self.cursor.execute(sql_select_patrimonio, (patrimonio_id, id_baixa))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Este patrimônio já possui outra baixa patrimonial cadastrada."
        sql_update = "UPDATE baixas_patrimoniais SET patrimonio_id=%s, nome=%s, usuario_registro=%s, tipo_baixa=%s, motivo=%s, valor_recuperado=%s, documento_comprobatorio=%s, data_baixa=%s WHERE id=%s"
        self.cursor.execute(sql_update, (patrimonio_id, nome, usuario_registro, tipo_baixa, motivo, valor_recuperado, documento_comprobatorio, data_baixa, id_baixa))
        self.conexao.commit()
        return "Baixa patrimonial atualizada com sucesso!"

    def deletar_baixa(self, id_baixa):
        sql_delete = "DELETE FROM baixas_patrimoniais WHERE id=%s"
        self.cursor.execute(sql_delete, (id_baixa,))
        self.conexao.commit()
        return "Baixa patrimonial excluída com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()  