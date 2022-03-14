import tkinter as tk

class Application():
    def __init__(self):
        self.root = tk.Tk()

        self.root.mainloop()

    def _config_windows(self):
        self.root.geometry('440x800')

Application()