from banco import Banco_CLI,Banco_CID

class Clientes:
    def __init__(self, idcliente=0, nome="", cpf="", genero="", telefone="", email="", Nome_CID="", endereco=""):
        self.idcliente = idcliente
        self.nome = nome
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.Nome_CID = Nome_CID
        self.endereco = endereco

    def inserCliente(self):
        banco = Banco_CLI()
        try:
            c = banco.conexao.cursor()
            c.execute("""INSERT INTO tbl_clientes (nome, cpf, genero, telefone, email, Nome_CID, endereco) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (self.nome, self.cpf, self.genero, self.telefone, self.email, self.Nome_CID, self.endereco))
            banco.conexao.commit()
            c.close()
            return "Cliente cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do cliente: {e}"

    def updateCliente(self):
        banco = Banco_CLI()
        try:
            c = banco.conexao.cursor()
            c.execute("""UPDATE tbl_clientes
                          SET nome = ?, cpf = ?, genero = ?, telefone = ?, email = ?, Nome_CID = ?, endereco = ? 
                          WHERE idcliente = ?""",
                       (self.nome, self.cpf, self.genero, self.telefone, self.email, self.Nome_CID, self.endereco, self.idcliente))
            banco.conexao.commit()
            c.close()
            return "Cliente atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do cliente: {e}"

    def deleteCliente(self):
        banco = Banco_CLI()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_clientes WHERE idcliente = ?", (self.idcliente,))
            banco.conexao.commit()
            c.close()
            return "Cliente excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do cliente: {e}"

    def selectCliente(self, idcliente):
        banco = Banco_CLI()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes WHERE idcliente = ?", (idcliente,))
            row = c.fetchone()
            if row:
                self.idcliente, self.nome, self.cpf, self.genero, self.telefone, self.email, self.Nome_CID, self.endereco = row
                return {
                    "encontrado": True,
                    "nome": self.nome,
                    "cpf": self.cpf,
                    "genero": self.genero,
                    "telefone": self.telefone,
                    "email": self.email,
                    "Nome_CID": self.Nome_CID,
                    "endereco": self.endereco
                }
            else:
                return {"encontrado": False, "msg": "Cliente não encontrado!"}
        except Exception as e:
            return {"encontrado": False, "msg": f"Ocorreu um erro na busca do cliente: {e}"}

    def selectAllClientes(self):
        banco = Banco_CLI()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_clientes")
            rows = c.fetchall()
            c.close()
            return rows
        except Exception as e:
            return f"Ocorreu um erro na seleção de todos os clientes: {e}"

    def selectCidades(self):
        banco = Banco_CID()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT nome FROM tbl_cidades")
            cidades = c.fetchall()
            c.close()
            return [cidade[0] for cidade in cidades]  # Retorna uma lista de nomes de cidades
        except Exception as e:
            return f"Ocorreu um erro na recuperação das cidades: {e}"
