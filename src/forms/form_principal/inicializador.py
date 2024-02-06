#importamos las librerias necesarias 
import tkinter as tk
import src.util.utilidades as utl
from src.forms.form_menu.menus import menuop, menufun

class FormPrincipal(tk.Tk):
    
    def __init__(self):
        """Constructor de la ventana principal que contendra los elementos visuales"""
        super().__init__()
        self.configuracion()
        self.paneles()
        menuop(self)
    
    def configuracion(self):
        """Configuración de la ventana """
        self.title("Sistemas Numericos")
        self.geometry("1024x600")
        w,h = 1024, 600
        utl.centrar_ventana(self, w, h)
        
    def paneles(self):
        """Creación de los paneles que dividiran la interfaz """
        self.barra_menu = tk.Frame(self, bg="grey", width=310)
        self.barra_menu.pack(side=tk.LEFT, fill="both", expand=False)
        
        self.AreaTrabajo = tk.Frame(self, bg="light grey")
        self.AreaTrabajo.pack(side=tk.RIGHT, fill="both", expand=True)

# if __name__ == "__main__":
#     main()
