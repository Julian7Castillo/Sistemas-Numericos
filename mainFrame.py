from tkinter import Tk, Frame
from menus import menuop
from areaTrabajo import bienvenida

class MainFrame(Frame):
    
    #Constructor
    def __init__(self, master = None):
        super().__init__(master, width=1060, height=550, bg="dark grey")
        self.master = master
        self.pack(expand=True, fill="both")
        self.create_widgets()
        
    def create_widgets(self):
        menuop(self)
        bienvenida(self)
        