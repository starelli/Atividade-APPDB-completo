import sqlite3

class Banco_USU:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableUSU()

    def createTableUSU(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
            IdUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT
        )""")
        self.conexao.commit()
        c.close()

class Banco_CID:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableCID()

    def createTableCID(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_cidades (
            IdCidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            UF TEXT
        )""")
        self.conexao.commit()
        c.close()

class Banco_CLI:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTableCLI()

    def createTableCLI(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_clientes (
            IdCliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT,
            genero TEXT,
            telefone TEXT,
            email TEXT,
            Nome_CID INTEGER,
            endereco TEXT,
            CONSTRAINT fk_NomeCID FOREIGN KEY (Nome_CID) REFERENCES tbl_cidades(IdCidade)
        )""")
        self.conexao.commit()
        c.close()
