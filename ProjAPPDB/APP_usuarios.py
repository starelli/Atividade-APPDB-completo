import sqlite3
import tkinter as tk
from usuarios import Usuarios
from tkinter import ttk,messagebox
import principal
from reportlab.pdfgen import canvas
import os
import textwrap
from reportlab.lib.pagesizes import letter

class Janela:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Usuários")
        self.master.geometry("600x400")

        self.fontPadrao = ("Times", 15)

        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.msg1 = tk.Label(self.widget1, text="INFORME OS DADOS:")
        self.msg1['font'] = ("Times New Roman", 18, "bold")
        self.msg1.pack()

        self.idUsuario = tk.Label(self.widget1, text="IdUsuário:", width=10)
        self.idUsuario['font'] = self.fontPadrao
        self.idUsuario.pack(side=tk.LEFT)

        self.idUsuario1 = tk.Entry(self.widget1)
        self.idUsuario1.pack(side=tk.LEFT)

        self.buscar_btn = tk.Button(self.widget1, text="Buscar", font=self.fontPadrao, width=5, command=self.buscarUsuario)
        self.buscar_btn.pack(side=tk.LEFT)

        self.widget2 = tk.Frame(master)
        self.widget2.pack()

        self.nome = tk.Label(self.widget2, text="Nome:", font=self.fontPadrao, width=10)
        self.nome.pack(side=tk.LEFT)
        self.nome1 = tk.Entry(self.widget2, width=30)
        self.nome1.pack(side=tk.LEFT)

        self.widget3 = tk.Frame(master)
        self.widget3.pack()

        self.telefone = tk.Label(self.widget3, text="Telefone:", font=self.fontPadrao, width=10)
        self.telefone.pack(side=tk.LEFT)
        self.telefone1 = tk.Entry(self.widget3, width=30)
        self.telefone1.pack(side=tk.LEFT)

        self.widget4 = tk.Frame(master)
        self.widget4.pack()

        self.email = tk.Label(self.widget4, text="E-mail:", font=self.fontPadrao, width=10)
        self.email.pack(side=tk.LEFT)
        self.email1 = tk.Entry(self.widget4, width=30)
        self.email1.pack(side=tk.LEFT)

        self.widget5 = tk.Frame(master)
        self.widget5.pack()

        self.usuario = tk.Label(self.widget5, text="Usuário:", font=self.fontPadrao, width=10)
        self.usuario.pack(side=tk.LEFT)
        self.usuario1 = tk.Entry(self.widget5, width=30)
        self.usuario1.pack(side=tk.LEFT)

        self.widget6 = tk.Frame(master)
        self.widget6.pack()

        self.senha = tk.Label(self.widget6, text="Senha:", font=self.fontPadrao, width=10)
        self.senha.pack(side=tk.LEFT)
        self.senha1 = tk.Entry(self.widget6, show="*", width=30)
        self.senha1.pack(side=tk.LEFT)

        self.widget7 = tk.Frame(master)
        self.widget7.pack()

        self.inserir = tk.Button(self.widget7, text="Inserir", font=self.fontPadrao, width=5, command=self.inserirUsuario)
        self.inserir.pack(side=tk.LEFT)

        self.alterar = tk.Button(self.widget7, text="Alterar", font=self.fontPadrao, width=5, command=self.alterarUsuario)
        self.alterar.pack(side=tk.LEFT)

        self.excluir = tk.Button(self.widget7, text="Excluir", font=self.fontPadrao, width=5, command=self.excluirUsuario)
        self.excluir.pack(side=tk.LEFT)

        self.fechar = tk.Button(self.widget7, text="Voltar", font=self.fontPadrao, width=5, command=self.widget1.quit)
        self.fechar.pack(side=tk.LEFT)

        self.lblmsg = tk.Label(master, text="", font=self.fontPadrao)
        self.lblmsg.pack()

        # Criação do Treeview e carregamento dos dados
        self.create_treeview(master)
        self.populate_treeview()

        self.widget8 = tk.Frame(master)
        self.widget8.pack()

        self.inserir = tk.Button(self.widget8, text="Visualizar PDF", font="Times", width=30, command=self.visualizar_pdf)
        self.inserir.pack(side=tk.LEFT)

        self.inserir1 = tk.Button(self.widget8, text="Gerar PDF", font="Times", width=30, command=self.salvar_pdf)
        self.inserir1.pack(side=tk.LEFT)


    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idUsuario1.get()
        msg = user.selectUser(idusuario)

        if msg=="Busca feita com sucesso!":
            self.nome1.delete(0, tk.END)
            self.nome1.insert(tk.END, user.nome)
            self.telefone1.delete(0, tk.END)
            self.telefone1.insert(tk.END, user.telefone)
            self.email1.delete(0, tk.END)
            self.email1.insert(tk.END, user.email)
            self.usuario1.delete(0, tk.END)
            self.usuario1.insert(tk.END, user.usuario)
            self.senha1.delete(0, tk.END)
            self.senha1.insert(tk.END, user.senha)
            messagebox.showinfo("Resultado da Busca", "Usuário encontrado!")
        else:
            messagebox.showwarning("Aviso", "Usuário não encontrado!")


    def inserirUsuario(self):
        user = Usuarios(
            nome=self.nome1.get(),
            telefone=self.telefone1.get(),
            email=self.email1.get(),
            usuario=self.usuario1.get(),
            senha=self.senha1.get()
        )
        msg = user.insertUser()
        messagebox.showinfo("Resultado da Inserção", msg)
        self.lblmsg["text"] = msg
        self.limparCampos()
        self.populate_treeview()  # Atualizar Treeview após inserção

    def alterarUsuario(self):
        user = Usuarios(
            idusuario=self.idUsuario1.get(),
            nome=self.nome1.get(),
            telefone=self.telefone1.get(),
            email=self.email1.get(),
            usuario=self.usuario1.get(),
            senha=self.senha1.get()
        )
        msg = user.updateUser()
        messagebox.showinfo("Resultado da Alteração", msg)
        self.lblmsg["text"] = msg
        self.limparCampos()
        self.populate_treeview()  # Atualizar Treeview após alteração

    def excluirUsuario(self):
        user = Usuarios(idusuario=self.idUsuario1.get())
        msg = user.deleteUser()
        messagebox.showinfo("Resultado da Exclusão", msg)
        self.lblmsg["text"] = msg
        self.limparCampos()
        self.populate_treeview()  # Atualizar Treeview após exclusão


    def limparCampos(self):
        self.idUsuario1.delete(0, tk.END)
        self.nome1.delete(0, tk.END)
        self.telefone1.delete(0, tk.END)
        self.email1.delete(0, tk.END)
        self.usuario1.delete(0, tk.END)
        self.senha1.delete(0, tk.END)

    def create_treeview(self, master):
        self.columns = ("ID", "Nome", "Telefone", "Email", "Usuário")
        self.treeview = ttk.Treeview(master, columns=self.columns, show='headings')
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def populate_treeview(self):
        data = self.fetch_data()
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for row in data:
            self.treeview.insert("", "end", values=row)

    def fetch_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_usuarios")
        rows = cursor.fetchall()
        conn.close()
        return rows


    def salvar_pdf(self):
        user = Usuarios()
        usuarios = user.selectalluser()

        pdf_file = "relatorio_usuarios.pdf"

        # Adiciona o título e define a fonte para o título
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, 750, "Relatório de Clientes")

        # Define a fonte para o corpo do texto
        c.setFont("Helvetica", 12)

        y_position = 725
        max_width = 85  # Define o número máximo de caracteres por linha

        for usu in usuarios:
            text = f"ID: {usu[0]}  |  Nome: {usu[1]}  |  Telefone: {usu[2]}  |  Email: {usu[3]}  |  Usuário: {usu[4]}"

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
        pdf_file = "relatorio_usuarios.pdf"

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

