
from banco import Banco_USU

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco_USU()
        try:
            c = banco.conexao.cursor()
            c.execute("""INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha) 
                          VALUES (?, ?, ?, ?, ?)""",
                       (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        banco = Banco_USU()
        try:
            c = banco.conexao.cursor()
            c.execute("""UPDATE tbl_usuarios 
                          SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? 
                          WHERE IdUsuario = ?""",
                       (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        banco = Banco_USU()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_usuarios WHERE IdUsuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"

    def selectUser(self, idusuario):
        banco = Banco_USU()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios WHERE IdUsuario = ?", (idusuario,))
            row = c.fetchone()
            if row:
                self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha = row
                return "Busca feita com sucesso!"
            else:
                return "Usuário não encontrado!"
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"

    def selectalluser(self):
        banco = Banco_USU()
        c = banco.conexao.cursor()
        c.execute("SELECT * FROM tbl_usuarios")
        row = c.fetchall()
        return row