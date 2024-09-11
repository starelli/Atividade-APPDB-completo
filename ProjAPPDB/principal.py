
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import subprocess

def start_main_app():
    root = Tk()
    root.title('Programa XXXXX')
    root.state("zoomed")

    menubar = Menu(root)
    root.config(menu=menubar)

    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)

    menubar.add_cascade(label='Arquivo', menu=filemenu)
    menubar.add_cascade(label='Cadastros', menu=filemenu2)
    menubar.add_cascade(label='Ajuda', menu=filemenu3)

    def Open():
        filedialog.askopenfilename()

    def Save():
        filedialog.asksaveasfilename()

    def Quit():
        root.quit()

    def APP_usuarios():
        subprocess.run(['python', "APP_usuarios.py"])

    def APP_cidades():
        subprocess.run(['python', "APP_cidades.py"])

    def APP_clientes():
        subprocess.run(['python', "APP_clientes.py"])

    def Help():
        help_window = Toplevel(root)
        help_window.title('Ajuda')
        text = Text(help_window, wrap=WORD)
        text.pack(expand=1, fill=BOTH)
        text.insert('insert', 'Ao clicar no botão da\n'
                              'respectiva cor, o fundo da tela\n'
                              'aparecerá na cor escolhida.')

    filemenu.add_command(label='Abrir...', command=Open)
    filemenu.add_command(label='Salvar como...', command=Save)
    filemenu.add_separator()
    filemenu.add_command(label='Sair', command=Quit)

    filemenu2.add_command(label='Usuários', command=APP_usuarios)
    filemenu2.add_command(label='Cidades', command=APP_cidades)
    filemenu2.add_command(label='Clientes', command=APP_clientes)

    filemenu3.add_command(label='Ajuda', command=Help)

    root.mainloop()
