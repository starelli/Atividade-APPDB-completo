
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import principal

class Login:
    def __init__(self, master=None):
        self.janela = tk.Frame(master)
        self.fontePadrao = ("Times", 12)
        self.janela.pack()

        self.titulo = tk.Label(self.janela, text="LOGIN")
        self.titulo["font"] = ("Times New Roman", 20, "bold")
        self.titulo.pack()

        # Carregando a imagem
        image = Image.open("images.png")
        photo = ImageTk.PhotoImage(image)
        self.imagem = tk.Label(self.janela, image=photo)
        self.imagem.image = photo
        self.imagem.pack()

        # Estilizando o contêiner
        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        # Estilizando o nome
        self.nome = tk.Label(self.janela2, text="Nome:", font=self.fontePadrao)
        self.nome.pack(side=tk.LEFT)
        self.nomeR = tk.Entry(self.janela2)
        self.nomeR["width"] = 30
        self.nomeR["font"] = self.fontePadrao
        self.nomeR.pack(side=tk.LEFT)

        # Estilizando o contêiner 2
        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        # Estilizando a senha
        self.senha = tk.Label(self.janela3, text="Senha:", font=self.fontePadrao)
        self.senha.pack(side=tk.LEFT)
        self.senhaR = tk.Entry(self.janela3)
        self.senhaR["width"] = 30
        self.senhaR["font"] = self.fontePadrao
        self.senhaR["show"] = "*"
        self.senhaR.pack(side=tk.LEFT)

        # Estilizando o contêiner 3
        self.janela4 = tk.Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        # Criando o botão
        self.autenticar = tk.Button(self.janela4, text="Autenticar", font=self.fontePadrao, command=self.verificaSenha)
        self.autenticar.pack()

    # Verificação de senha
    def verificaSenha(self):
        usuario = self.nomeR.get()
        senha = self.senhaR.get()
        if usuario == "Ellen" and senha == "12345":
            messagebox.showinfo("Autenticação", "Autenticado!")
            self.janela.master.destroy()  # Fecha a janela de login
            principal.start_main_app()  # Abre a aplicação principal
        else:
            messagebox.showerror("Erro", "Erro na autenticação!")

root = tk.Tk()
Login(root)
root.state('zoomed')
root.mainloop()