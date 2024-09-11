import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from clientes import Clientes
from tkinter import filedialog
from reportlab.pdfgen import canvas
import os
import textwrap
from reportlab.lib.pagesizes import letter


class Janela:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Clientes")
        self.master.geometry("600x400")

        self.fontPadrao = ("Times", 15)

        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.msg1 = tk.Label(self.widget1, text="INFORME OS DADOS:")
        self.msg1['font'] = ("Times New Roman", 18, "bold")
        self.msg1.pack()

        self.idcliente = tk.Label(self.widget1, text="IdCliente:", width=10)
        self.idcliente['font'] = self.fontPadrao
        self.idcliente.pack(side=tk.LEFT)

        self.idcliente1 = tk.Entry(self.widget1)
        self.idcliente1.pack(side=tk.LEFT)

        self.buscar_btn = tk.Button(self.widget1, text="Buscar", font=self.fontPadrao, width=5,
                                    command=self.buscarCliente)
        self.buscar_btn.pack(side=tk.LEFT)

        self.widget2 = tk.Frame(master)
        self.widget2.pack()

        self.nome = tk.Label(self.widget2, text="Nome:", font=self.fontPadrao, width=10)
        self.nome.pack(side=tk.LEFT)
        self.nome1 = tk.Entry(self.widget2, width=30)
        self.nome1.pack(side=tk.LEFT)

        self.widget3 = tk.Frame(master)
        self.widget3.pack()

        self.cpf = tk.Label(self.widget3, text="CPF:", font=self.fontPadrao, width=10)
        self.cpf.pack(side=tk.LEFT)
        self.cpf1 = tk.Entry(self.widget3, width=30)
        self.cpf1.pack(side=tk.LEFT)

        self.widget4 = tk.Frame(master)
        self.widget4.pack()

        self.genero = tk.Label(self.widget4, text="Gênero:", font=self.fontPadrao, width=10)
        self.genero.pack(side=tk.LEFT)
        self.genero1 = tk.Entry(self.widget4, width=30)
        self.genero1.pack(side=tk.LEFT)

        self.widget5 = tk.Frame(master)
        self.widget5.pack()

        self.telefone = tk.Label(self.widget5, text="Telefone:", font=self.fontPadrao, width=10)
        self.telefone.pack(side=tk.LEFT)
        self.telefone1 = tk.Entry(self.widget5, width=30)
        self.telefone1.pack(side=tk.LEFT)

        self.widget6 = tk.Frame(master)
        self.widget6.pack()

        self.email = tk.Label(self.widget6, text="E-mail:", font=self.fontPadrao, width=10)
        self.email.pack(side=tk.LEFT)
        self.email1 = tk.Entry(self.widget6, width=30)
        self.email1.pack(side=tk.LEFT)

        self.widget7 = tk.Frame(master)
        self.widget7.pack()

        self.Nome_CID = tk.Label(self.widget7, text="Nome da Cidade:", font=self.fontPadrao, width=10)
        self.Nome_CID.pack(side=tk.LEFT)
        self.Nome_CID1 = ttk.Combobox(self.widget7, width=30)
        self.Nome_CID1.pack(side=tk.LEFT)
        self.carregarCidades()

        self.widget8 = tk.Frame(master)
        self.widget8.pack()

        self.endereco = tk.Label(self.widget8, text="Endereço:", font=self.fontPadrao, width=10)
        self.endereco.pack(side=tk.LEFT)
        self.endereco1 = tk.Entry(self.widget8, width=30)
        self.endereco1.pack(side=tk.LEFT)

        self.widget9 = tk.Frame(master)
        self.widget9.pack()

        self.inserir = tk.Button(self.widget9, text="Inserir", font=self.fontPadrao, width=5,
                                 command=self.inserirCliente)
        self.inserir.pack(side=tk.LEFT)

        self.alterar = tk.Button(self.widget9, text="Alterar", font=self.fontPadrao, width=5,
                                 command=self.alterarCliente)
        self.alterar.pack(side=tk.LEFT)

        self.excluir = tk.Button(self.widget9, text="Excluir", font=self.fontPadrao, width=5,
                                 command=self.excluirCliente)
        self.excluir.pack(side=tk.LEFT)

        self.fechar = tk.Button(self.widget9, text="Voltar", font=self.fontPadrao, width=5, command=self.master.quit)
        self.fechar.pack(side=tk.LEFT)

        # Criação do Treeview e carregamento dos dados
        self.janela12 = tk.Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12,
                                 columns=("IdCliente", "Nome", "CPF", "Gênero", "Telefone", "Email", "Nome da Cidade", "Endereço"),
                                 show='headings')
        self.tree.heading("IdCliente", text="IdCliente")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Gênero", text="Gênero")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Nome da Cidade", text="Nome da Cidade")
        self.tree.heading("Endereço", text="Endereço")
        self.tree.bind("<<TreeviewSelect>>", self.selecionaclientes)
        self.tree.pack()

        self.atualizarTabela()

        self.widget10 = tk.Frame(master)
        self.widget10.pack()

        self.inserir = tk.Button(self.widget10, text="Visualizar PDF", font="Times", width=30, command=self.visualizar_pdf)
        self.inserir.pack(side=tk.LEFT)

        self.inserir1 = tk.Button(self.widget10, text="Gerar PDF", font="Times", width=30, command=self.salvar_pdf)
        self.inserir1.pack(side=tk.LEFT)

    def selecionaclientes(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')

            self.idcliente1.delete(0, tk.END)
            self.idcliente1.insert(tk.END, values[0])
            self.nome1.delete(0, tk.END)
            self.nome1.insert(tk.END, values[1])
            self.cpf1.delete(0, tk.END)
            self.cpf1.insert(tk.END, values[2])
            self.genero1.delete(0, tk.END)
            self.genero1.insert(tk.END, values[3])
            self.telefone1.delete(0, tk.END)
            self.telefone1.insert(tk.END, values[4])
            self.email1.delete(0, tk.END)
            self.email1.insert(tk.END, values[5])
            self.Nome_CID1.set(values[6])
            self.endereco1.delete(0, tk.END)
            self.endereco1.insert(tk.END, values[7])

    def atualizarTabela(self):
        user = Clientes()
        clientes = user.selectAllClientes()
        self.tree.delete(*self.tree.get_children())  # Limpa a tabela antes de inserir novos dados

        for c in clientes:
            self.tree.insert("", "end", values=c)

    def buscarCliente(self):
        user = Clientes()
        idcliente = self.idcliente1.get()
        cliente = user.selectCliente(idcliente)

        if cliente["encontrado"]:
            self.nome1.delete(0, tk.END)
            self.nome1.insert(tk.END, cliente["nome"])
            self.cpf1.delete(0, tk.END)
            self.cpf1.insert(tk.END, cliente["cpf"])
            self.genero1.delete(0, tk.END)
            self.genero1.insert(tk.END, cliente["genero"])
            self.telefone1.delete(0, tk.END)
            self.telefone1.insert(tk.END, cliente["telefone"])
            self.email1.delete(0, tk.END)
            self.email1.insert(tk.END, cliente["email"])
            self.Nome_CID1.set(cliente["Nome_CID"])
            self.endereco1.delete(0, tk.END)
            self.endereco1.insert(tk.END, cliente["endereco"])
            messagebox.showinfo("Resultado da Busca", "Cliente encontrado!")
        else:
            messagebox.showwarning("Aviso", cliente["msg"])

    def inserirCliente(self):
        user = Clientes(
            nome=self.nome1.get(),
            cpf=self.cpf1.get(),
            genero=self.genero1.get(),
            telefone=self.telefone1.get(),
            email=self.email1.get(),
            Nome_CID=self.Nome_CID1.get(),
            endereco=self.endereco1.get()
        )
        msg = user.inserCliente()
        messagebox.showinfo("Resultado da Inserção", msg)
        self.atualizarTabela()
        self.limparCampos()

    def alterarCliente(self):
        user = Clientes(
            idcliente=self.idcliente1.get(),
            nome=self.nome1.get(),
            cpf=self.cpf1.get(),
            genero=self.genero1.get(),
            telefone=self.telefone1.get(),
            email=self.email1.get(),
            Nome_CID=self.Nome_CID1.get(),
            endereco=self.endereco1.get()
        )
        msg = user.updateCliente()
        messagebox.showinfo("Resultado da Alteração", msg)
        self.atualizarTabela()
        self.limparCampos()

    def excluirCliente(self):
        user = Clientes(idcliente=self.idcliente1.get())
        msg = user.deleteCliente()
        messagebox.showinfo("Resultado da Exclusão", msg)
        self.atualizarTabela()
        self.limparCampos()

    def limparCampos(self):
        self.idcliente1.delete(0, tk.END)
        self.nome1.delete(0, tk.END)
        self.cpf1.delete(0, tk.END)
        self.genero1.delete(0, tk.END)
        self.telefone1.delete(0, tk.END)
        self.email1.delete(0, tk.END)
        self.Nome_CID1.set('')
        self.endereco1.delete(0, tk.END)

    def carregarCidades(self):
        user = Clientes()  # Aqui, você deve usar a lógica correta para obter cidades
        cidades = user.selectCidades()
        self.Nome_CID1['values'] = cidades


    def salvar_pdf(self):
        user = Clientes()
        clientes = user.selectAllClientes()

        pdf_file = "relatorio_clientes.pdf"

        # Adiciona o título e define a fonte para o título
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, 750, "Relatório de Clientes")

        # Define a fonte para o corpo do texto
        c.setFont("Helvetica", 12)

        y_position = 725
        max_width = 85  # Define o número máximo de caracteres por linha

        for cliente in clientes:
            text = f"ID: {cliente[0]}  |  Nome: {cliente[1]}  |  CPF: {cliente[2]}  |  Gênero: {cliente[3]}  |  Telefone: {cliente[4]}  |  E-mail: {cliente[5]}  |  Cidade: {cliente[6]}  |  Endereço: {cliente[7]}"

            # Quebra o texto em várias linhas se exceder o limite de caracteres
            wrapped_text = textwrap.wrap(text, width=max_width)

            for line in wrapped_text:
                c.drawString(72, y_position, line)
                y_position -= 15

                # Verifica se a página precisa ser trocada
                if y_position < 72:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = 750

        c.save()
        messagebox.showinfo("Sucesso", "Relatório PDF gerado com sucesso.")

    def visualizar_pdf(self):
        pdf_file = "relatorio_clientes.pdf"

        # Verifica se o arquivo PDF existe
        if os.path.exists(pdf_file):
            try:
                # Abre o arquivo PDF no visualizador padrão do sistema
                os.startfile(pdf_file)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao abrir o PDF: {e}")
        else:
            messagebox.showerror("Erro", "O arquivo PDF não foi encontrado.")



if __name__ == "__main__":
    root = tk.Tk()
    app = Janela(root)
    root.state('zoomed')
    root.mainloop()
