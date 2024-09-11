import sqlite3
import tkinter as tk
from cidades import *
from tkinter import ttk,messagebox
from tkinter import filedialog
from reportlab.pdfgen import canvas
import os
import textwrap
from reportlab.lib.pagesizes import letter



class Janela:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Cidades")
        self.master.geometry("600x400")

        self.fontPadrao = ("Times", 15)

        self.widget1 = tk.Frame(master)
        self.widget1.pack()

        self.msg1 = tk.Label(self.widget1, text="INFORME OS DADOS:")
        self.msg1['font'] = ("Times New Roman", 18, "bold")
        self.msg1.pack()

        self.idcidade = tk.Label(self.widget1, text="IdCidade:", width=10)
        self.idcidade['font'] = self.fontPadrao
        self.idcidade.pack(side=tk.LEFT)

        self.idcidade1 = tk.Entry(self.widget1)
        self.idcidade1.pack(side=tk.LEFT)

        self.buscar_btn = tk.Button(self.widget1, text="Buscar", font=self.fontPadrao, width=5, command=self.buscarCidade)
        self.buscar_btn.pack(side=tk.LEFT)

        self.widget2 = tk.Frame(master)
        self.widget2.pack()

        self.nome = tk.Label(self.widget2, text="Nome:", font=self.fontPadrao, width=10)
        self.nome.pack(side=tk.LEFT)
        self.nome1 = tk.Entry(self.widget2, width=30)
        self.nome1.pack(side=tk.LEFT)

        self.widget3 = tk.Frame(master)
        self.widget3.pack()

        self.UF = tk.Label(self.widget3, text="UF:", font=self.fontPadrao, width=10)
        self.UF.pack(side=tk.LEFT)

        # Combobox para selecionar UF
        self.UF_options = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB",
                           "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
        self.UF1 = ttk.Combobox(self.widget3, values=self.UF_options, width=30)
        self.UF1.pack(side=tk.LEFT)

        self.widget4 = tk.Frame(master)
        self.widget4.pack()

        self.widget7 = tk.Frame(master)
        self.widget7.pack()

        self.inserir = tk.Button(self.widget7, text="Inserir", font=self.fontPadrao, width=5, command=self.inserirCidade)
        self.inserir.pack(side=tk.LEFT)

        self.alterar = tk.Button(self.widget7, text="Alterar", font=self.fontPadrao, width=5, command=self.alterarCidade)
        self.alterar.pack(side=tk.LEFT)

        self.excluir = tk.Button(self.widget7, text="Excluir", font=self.fontPadrao, width=5, command=self.excluirCidade)
        self.excluir.pack(side=tk.LEFT)

        self.fechar = tk.Button(self.widget7, text="Voltar", font=self.fontPadrao, width=5, command= self.widget1.quit)
        self.fechar.pack(side=tk.LEFT)

        self.lblmsg = tk.Label(master, text="", font=self.fontPadrao)
        self.lblmsg.pack()


        self.janela12 = tk.Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Cidade", "UF"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.bind("<<TreeviewSelect>>", self.selecionacidade)
        self.tree.pack()

        #atualiza a tabela
        self.atualizarTabela()

        self.widget8 = tk.Frame(master)
        self.widget8.pack()

        self.inserir = tk.Button(self.widget8, text="Visualizar PDF", font="Times", width=30, command=self.visualizar_pdf)
        self.inserir.pack(side=tk.LEFT)

        self.inserir1 = tk.Button(self.widget8, text="Gerar PDF", font="Times", width=30, command=self.salvar_pdf)
        self.inserir1.pack(side=tk.LEFT)

    def selecionacidade(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            # Obtém o item selecionado
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')
            # Preenche os campos de entrada com os dados do item selecionado
            self.idcidade1.delete(0, tk.END)
            self.idcidade1.insert(tk.INSERT, values[0])
            self.nome1.delete(0, tk.END)
            self.nome1.insert(tk.INSERT, values[1])
            self.UF1.delete(0, tk.END)
            self.UF1.insert(tk.INSERT, values[2])

    def buscarCidade(self):
        user = Cidades()
        idcidade = self.idcidade1.get()
        msg = user.selectCity(idcidade)

        if msg == "Busca feita com sucesso!":
            self.nome1.delete(0, tk.END)
            self.nome1.insert(tk.END, user.nome)
            self.UF1.delete(0, tk.END)
            self.UF1.insert(tk.END, user.UF)
            messagebox.showinfo("Resultado da Busca", "Cidade encontrada!")
        else:
            messagebox.showwarning("Aviso", "Cidade não encontrada!")

    def inserirCidade(self):
        user = Cidades(
            nome=self.nome1.get(),
            UF=self.UF1.get(),

        )
        msg = user.insertCity()
        messagebox.showinfo("Resultado da Inserção", msg)

        self.atualizarTabela()
        self.limparCampos()


    def alterarCidade(self):
        user = Cidades(
            idcidade=self.idcidade1.get(),
            nome=self.nome1.get(),
            UF=self.UF.get()
        )

        msg = user.updateCity()
        messagebox.showinfo("Resultado da Alteração", msg)

        self.atualizarTabela()
        self.limparCampos()


    def excluirCidade(self):
        user = Cidades(idcidade=self.idcidade1.get())
        msg = user.deleteCity()
        messagebox.showinfo("Resultado da Exclusão", msg)

        self.atualizarTabela()
        self.limparCampos()


    def limparCampos(self):
        self.idcidade1.delete(0, tk.END)
        self.nome1.delete(0, tk.END)
        self.UF1.delete(0, tk.END)

    def create_treeview(self, master):
        self.columns = ("ID", "Nome", "UF")
        self.treeview = ttk.Treeview(master, columns=self.columns, show='headings')
        for col in self.columns:
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def fetch_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tbl_cidades")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def atualizarTabela(self):
        user = Cidades()
        cidades = user.selectAllCids()
        self.tree.delete(*self.tree.get_children())
        for c in cidades:
            self.tree.insert("", "end", values=(c[0], c[1], c[2]))


    def salvar_pdf(self):
        user = Cidades()
        cidades = user.selectAllCids()

        pdf_file = "relatorio_cidades.pdf"

        # Adiciona o título e define a fonte para o título
        c = canvas.Canvas(pdf_file, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, 750, "Relatório de Cidades")

        # Define a fonte para o corpo do texto
        c.setFont("Helvetica", 12)

        y_position = 725
        max_width = 85  # Define o número máximo de caracteres por linha

        for C in cidades:
            text = f"ID: {C[0]}  |  Nome: {C[1]}  |  UF: {C[2]}"

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
        pdf_file = "relatorio_cidades.pdf"

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