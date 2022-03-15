import tkinter as tk


class Application():
    def __init__(self):
        self.root = tk.Tk()

        self.config_tela()
        self.criando_frames()
        self.criando_butoes()
        self.criando_campos()
        self.root.mainloop()

    def config_tela(self) -> None:
        """Configurações da tela pricinpal do programa"""
        self.root.title('Cadastro de Clientes')
        self.root.geometry('600x480')
        self.root.configure(background='gray50')
        self.root.resizable(True, True)
        self.root.minsize(width=800, height=600)

    def criando_frames(self) -> None:
        """Criar os 2 frames de trabalho na tela principal"""
        self.frame1 = tk.Frame(
            self.root,
            bg='#CCFFE5',
            highlightbackground='gray90',
            highlightthickness=2)
        self.frame1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        self.frame2 = tk.Frame(
            self.root,
            bg='#CCFFFF',
            highlightbackground='gray90',
            highlightthickness=2)
        self.frame2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.49)

    def criando_butoes(self) -> None:
        """Criar os butoes da aplicação"""
        pass

    def criando_campos(self) -> None:
        """Criar os campos de input de informações (nome, telefoen, etc...)"""
        pass


Application()
