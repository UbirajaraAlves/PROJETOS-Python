import tkinter as tk
from tkinter import ttk


class Funcs():
    def limpar_tela(self) -> None:
        self.et_codigo.delete(0, tk.END)
        self.et_nome.delete(0, tk.END)
        self.et_telefone.delete(0, tk.END)
        self.et_cidade.delete(0, tk.END)


class Application(Funcs):
    def __init__(self):
        self.root = tk.Tk()
        self.cor = ['#FFFFE0', '#FFFACD', '#FFF8DC', '#F5DEB3', '#FFEBCD']

        self.config_tela()
        self.criando_frames()
        self.criando_botoes()
        self.criando_campos()
        self.criando_lista_registros()
        self.root.mainloop()

    def config_tela(self) -> None:
        """Configurações da tela pricinpal do programa"""
        self.root.title('Cadastro de Clientes')
        self.root.geometry('800x600')
        self.root.configure(background=self.cor[3])
        self.root.resizable(True, True)
        self.root.minsize(width=800, height=600)

    def criando_frames(self) -> None:
        """Criar os 2 frames de trabalho na tela principal"""
        self.frame1 = tk.Frame(
            self.root,
            background=self.cor[2],
            highlightbackground='black',
            highlightthickness=1)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        self.frame2 = tk.Frame(
            self.root,
            background=self.cor[2],
            highlightbackground='black',
            highlightthickness=1)
        self.frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.49)

    def criando_botoes(self) -> None:
        """Criar os butoes da aplicação"""
        self.bt_limpar = tk.Button(self.frame1, text='Limpar', bd=2, bg=self.cor[1],
                                   font=('Arial', 12), command=self.limpar_tela)
        self.bt_limpar.place(relx=0.25, rely=0.1, relwidth=0.1, relheight=0.12)

        self.bt_buscar = tk.Button(
            self.frame1, text='Buscar', bd=2, bg=self.cor[1], font=('Arial', 12))
        self.bt_buscar.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.12)

        self.bt_novo = tk.Button(
            self.frame1, text='Novo', bd=2, bg=self.cor[1], font=('Arial', 12))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.12)

        self.bt_alterar = tk.Button(
            self.frame1, text='Alterar', bd=2, bg=self.cor[1], font=('Arial', 12))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.12)

        self.bt_apagar = tk.Button(
            self.frame1, text='Apagar', bd=2, bg=self.cor[1], font=('Arial', 12))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.12)

    def criando_campos(self) -> None:
        """Criar os campos de label e input (nome, telefoen, etc...)"""
        self.lb_codigo = tk.Label(
            self.frame1, text='Código', bg=self.cor[2], font=('Arial', 12))
        self.lb_codigo.place(relx=0.1, rely=0, relwidth=0.1, relheight=0.1)
        self.et_codigo = tk.Entry(self.frame1, font=('Arial', 12))
        self.et_codigo.place(relx=0.1, rely=0.1, relwidth=0.12, relheight=0.1)

        self.lb_nome = tk.Label(
            self.frame1, text='Nome', bg=self.cor[2], font=('Arial', 12))
        self.lb_nome.place(relx=0.1, rely=0.35, relwidth=0.1, relheight=0.1)
        self.et_nome = tk.Entry(self.frame1, font=('Arial', 12))
        self.et_nome.place(relx=0.1, rely=0.45, relwidth=0.80, relheight=0.1)

        self.lb_telefone = tk.Label(
            self.frame1, text='Telefone', bg=self.cor[2], font=('Arial', 12))
        self.lb_telefone.place(relx=0.1, rely=0.65,
                               relwidth=0.1, relheight=0.1)
        self.et_telefone = tk.Entry(self.frame1, font=('Arial', 12))
        self.et_telefone.place(relx=0.1, rely=0.75,
                               relwidth=0.35, relheight=0.1)

        self.lb_cidade = tk.Label(
            self.frame1, text='Cidade', bg=self.cor[2], font=('Arial', 12))
        self.lb_cidade.place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.1)
        self.et_cidade = tk.Entry(self.frame1, font=('Arial', 12))
        self.et_cidade.place(relx=0.5, rely=0.75, relwidth=0.4, relheight=0.1)

    def criando_lista_registros(self) -> None:
        self.lista_reg = ttk.Treeview(
            self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))

        self.lista_reg.heading('#0', text='')
        self.lista_reg.heading('#1', text='Código')
        self.lista_reg.heading('#2', text='Nome')
        self.lista_reg.heading('#3', text='Telefone')
        self.lista_reg.heading('#4', text='Cidade')

        self.lista_reg.column('#0', width=1)
        self.lista_reg.column('#1', width=50)
        self.lista_reg.column('#2', width=200)
        self.lista_reg.column('#3', width=150)
        self.lista_reg.column('#4', width=150)

        self.lista_reg.place(relx=0.05, rely=0.05,
                             relwidth=0.85, relheight=0.9)

        self.scroll_lista = tk.Scrollbar(self.frame2, orient='vertical')
        self.lista_reg.configure(yscroll=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.9, rely=0.05,
                                relwidth=0.05, relheight=0.9)


if __name__ == '__main__':
    Application()
