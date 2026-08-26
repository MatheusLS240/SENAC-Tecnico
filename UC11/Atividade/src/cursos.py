import mysql.connector as conn  # type: ignore

class Cursos:
    def __init__(self, param_host="127.0.0.1", param_port=3306, param_user="root", param_password="", param_database=""):
        self.conexao = conn.connect(host=param_host, port=param_port, user=param_user, password=param_password, database=param_database)
        self.cursor = self.conexao.cursor()

    def validar_curso(self, nome, sigla, criado_por):
        if type(nome) != str or nome.strip() == "":
            return "Não foi possível cadastrar o curso: o nome está vazio ou contém caracteres inválidos."
        elif type(sigla) != str or sigla.strip() == "":
            return "Não foi possível cadastrar o curso: a sigla está vazia ou contém caracteres inválidos."
        elif type(criado_por) != int or criado_por <= 0:
            return "Não foi possível cadastrar o curso: informe um usuário válido para o campo criado por."
        return None

    def cadastrar_curso(self, nome, sigla, criado_por):
        erro = self.validar_curso(nome, sigla, criado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM cursos WHERE nome=%s"
        self.cursor.execute(sql_select, (nome,))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Curso já cadastrado. Por favor, cadastre outro!"
        sql_insert = "INSERT INTO cursos(nome, sigla, criado_por) VALUES (%s, %s, %s)"
        self.cursor.execute(sql_insert, (nome, sigla, criado_por))
        self.conexao.commit()
        return "Curso cadastrado com sucesso!"

    def selecionar_todos(self):
        sql_select = "SELECT id, nome, sigla, criado_por FROM cursos"
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def selecionar_id(self, id):
        sql_select = "SELECT id, nome, sigla, criado_por FROM cursos WHERE id=%s"
        self.cursor.execute(sql_select, (id,))
        return self.cursor.fetchone()

    def atualizar_curso(self, nome, sigla, criado_por, id_curso):
        erro = self.validar_curso(nome, sigla, criado_por)
        if erro != None:
            return erro
        sql_select = "SELECT id FROM cursos WHERE id=%s"
        self.cursor.execute(sql_select, (id_curso,))
        rs = self.cursor.fetchone()
        if rs == None:
            return "Curso não encontrado. Por favor, digite outro ID!"
        sql_select_nome = "SELECT id FROM cursos WHERE nome=%s AND id != %s"
        self.cursor.execute(sql_select_nome, (nome, id_curso))
        rs = self.cursor.fetchone()
        if rs != None:
            return "Já existe outro curso com esse nome. Por favor, escolha outro!"
        sql_update = "UPDATE cursos SET nome=%s, sigla=%s, criado_por=%s WHERE id=%s"
        self.cursor.execute(sql_update, (nome, sigla, criado_por, id_curso))
        self.conexao.commit()
        return "Curso atualizado com sucesso!"

    def deletar_curso(self, id_curso):
        sql_delete = "DELETE FROM cursos WHERE id=%s"
        self.cursor.execute(sql_delete, (id_curso,))
        self.conexao.commit()
        return "Curso excluído com sucesso!"

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()