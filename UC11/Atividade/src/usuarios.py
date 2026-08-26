import mysql.connector as conn  # type: ignore

class Usuarios:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_usuario(self, nome, email, senha_hash, perfil, ativo):
        if type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar o usuário: o nome está vazio ou contém caracteres inválidos."
        elif type(email) != str or email.strip() == "":
            return "Não foi possível cadastrar o usuário: informe um e-mail válido."
        elif type(senha_hash) != str or senha_hash.strip() == "":
            return "Não foi possível cadastrar o usuário: a senha não foi informada."
        elif type(perfil) != str or perfil not in ["Administrador", "Coordenador", "Assistente"]:
            return "Não foi possível cadastrar o usuário: informe um perfil válido (Administrador, Coordenador ou Assistente)."
        elif type(ativo) != bool:
            return "Não foi possível cadastrar o usuário: o campo ativo deve ser verdadeiro ou falso."
        return None

    def cadastrar_usuario(self, nome, email, senha_hash, perfil, ativo):
        erro = self.validar_usuario(nome, email, senha_hash, perfil, ativo)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM usuarios WHERE nome=%s"
        self.cursor.execute(sql_select, (nome,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Usuário já cadastrado. Por favor, cadastre outro!"
        sql_insert = "INSERT INTO usuarios(nome, email, senha_hash, perfil, ativo) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql_insert, (nome, email, senha_hash, perfil, ativo))
        self.conexao.commit()
        return "Usuário cadastrado com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, nome, email, senha_hash, perfil, ativo FROM usuarios"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT id, nome, email, senha_hash, perfil, ativo FROM usuarios WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_usuario(self, nome, email, senha_hash, perfil, ativo, id_usuario):
        erro = self.validar_usuario(nome, email, senha_hash, perfil, ativo)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM usuarios WHERE id=%s"
        self.cursor.execute(sql_select, (id_usuario,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Usuário não encontrado. Por favor, digite outro ID!"
        sql_select_nome = "SELECT id FROM usuarios WHERE nome=%s AND id != %s"
        self.cursor.execute(sql_select_nome, (nome, id_usuario))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Já existe outro usuário com esse nome. Por favor, escolha outro!"
        sql_update = "UPDATE usuarios SET nome=%s, email=%s, senha_hash=%s, perfil=%s, ativo=%s WHERE id=%s"
        self.cursor.execute(sql_update, (nome, email, senha_hash, perfil, ativo, id_usuario))
        self.conexao.commit()
        return "Usuário atualizado com sucesso!"

    def deletar_usuario(self, id_usuario):
        sql_delete = "DELETE FROM usuarios WHERE id=%s"
        self.cursor.execute(sql_delete, (id_usuario,))
        self.conexao.commit()
        return "Usuário excluído com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()