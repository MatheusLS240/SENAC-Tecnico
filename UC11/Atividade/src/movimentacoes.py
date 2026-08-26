import mysql.connector as conn  # type: ignore

class Movimentacoes:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_movimentacao(self, patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes):
        if type(patrimonio_id) != int or patrimonio_id <= 0:
            return "Não foi possível cadastrar a movimentação: informe um patrimônio válido."
        elif type(usuario_registro) != int or usuario_registro <= 0:
            return "Não foi possível cadastrar a movimentação: informe um usuário válido."
        elif type(tipo_movimentacao) != str or tipo_movimentacao.strip() == "":
            return "Não foi possível cadastrar a movimentação: informe um tipo de movimentação válido."
        elif type(responsavel_destino) != str or responsavel_destino.strip() == "":
            return "Não foi possível cadastrar a movimentação: informe o responsável pelo destino."
        elif type(documento_responsavel) != str or documento_responsavel.strip() == "":
            return "Não foi possível cadastrar a movimentação: informe o documento do responsável."
        elif data_saida is None:
            return "Não foi possível cadastrar a movimentação: informe a data de saída."
        elif data_prevista_retorno is None:
            return "Não foi possível cadastrar a movimentação: informe a data prevista de retorno."
        elif data_retorno_efetivo is not None and data_retorno_efetivo < data_saida:
            return "Não foi possível cadastrar a movimentação: a data de retorno não pode ser anterior à data de saída."
        elif observacoes is not None and type(observacoes) != str:
            return "Não foi possível cadastrar a movimentação: as observações devem ser um texto válido."
        return None

    def cadastrar_movimentacao(self, patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes):
        erro = self.validar_movimentacao(patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM movimentacoes WHERE patrimonio_id=%s AND data_retorno_efetivo IS NULL"
        self.cursor.execute(sql_select, (patrimonio_id,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Este patrimônio já possui uma movimentação em aberto."
        sql_insert = "INSERT INTO movimentacoes(patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql_insert, (patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes))
        self.conexao.commit()
        return "Movimentação cadastrada com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes FROM movimentacoes"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes FROM movimentacoes WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_movimentacao(self, id, patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes):
        erro = self.validar_movimentacao(patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM movimentacoes WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Movimentação não encontrada. Por favor, digite outro ID!"
        sql_update = "UPDATE movimentacoes SET patrimonio_id=%s, usuario_registro=%s, tipo_movimentacao=%s, responsavel_destino=%s, documento_responsavel=%s, data_saida=%s, data_prevista_retorno=%s, data_retorno_efetivo=%s, observacoes=%s WHERE id=%s"
        self.cursor.execute(sql_update, (patrimonio_id, usuario_registro, tipo_movimentacao, responsavel_destino, documento_responsavel, data_saida, data_prevista_retorno, data_retorno_efetivo, observacoes, id))
        self.conexao.commit()
        return "Movimentação atualizada com sucesso!"

    def deletar_movimentacao(self, id):
        sql_delete = "DELETE FROM movimentacoes WHERE id=%s"
        self.cursor.execute(sql_delete, (id,))
        self.conexao.commit()
        return "Movimentação excluída com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()