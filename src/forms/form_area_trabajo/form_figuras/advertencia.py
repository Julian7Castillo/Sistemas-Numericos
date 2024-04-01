import tkinter as tk
import src.util.utilidades as utl_ven

class advertencia(tk.Toplevel):

    #Constructor
    def __init__(self) -> None:
        super().__init__()
        self.configuracion_window()
        self.construirWidget()
        
    def configuracion_window(self):
        """Configuracion inicial de la ventana """
        self.title("Advertencia")
        w, h = 400, 100
        utl_ven.centrar_ventana(self, w, h)
        
    def construirWidget(self):
        """Creacion y ubicacion de objetos en la ventana"""
        self.labelVersion = tk.Label(self, text = "Los campos no pueden estar vacios")
        self.labelVersion.config(fg="#000000", font=("Roboto", 15), pady=10, width = 50)
        self.labelVersion.pack()
