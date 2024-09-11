
from banco import Banco_CID

class Cidades:
    def __init__(self, idcidade=0, nome="", UF=""):
        self.banco = Banco_CID()
        self.idcidade = idcidade
        self.nome = nome
        self.UF = UF

    def insertCity(self):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("""INSERT INTO tbl_cidades (nome, UF) 
                          VALUES (?, ?)""",
                       (self.nome, self.UF))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCity(self):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("""UPDATE tbl_cidades 
                          SET nome = ?, UF = ?
                          WHERE IdCidade = ?""",
                       (self.nome, self.UF))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {e}"

    def deleteCity(self):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidades WHERE IdCidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {e}"

    def selectCity(self, idcidade):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades WHERE IdCidade = ?", (idcidade,))
            row = c.fetchone()
            if row:
                self.idcidade, self.nome, self.UF = row
                return "Busca feita com sucesso!"
            else:
                return "Cidade não encontrado!"
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {e}"

    def selectAllCids(self):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidades")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            return f"Ocorreu um erro na recuperação das cidades: {e}"