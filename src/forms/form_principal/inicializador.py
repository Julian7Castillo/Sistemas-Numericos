#importamos las librerias necesarias 
import tkinter as tk
from tkinter import  font
import src.util.utilidades as utl
from src.forms.form_menu.menus import menuop, menufun

class FormPrincipal(tk.Tk):
    
    def __init__(self):
        """Constructor de la ventana principal que contendra los elementos visuales"""
        super().__init__()
        self.configuracion()
        self.paneles()
        self.menuop()
    
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

    def menuop(self):
        """Creacióm de menu latertal por mediuo de un cilo para mejorar la eficiencia del codigo"""
        
        #datos del menu lateral
        ancho_menu = 16
        alto_menu = 2
        font_awesome = font.Font = ("Arial", 15, "bold")
        
        #Creacion de los bordes para lso botones
        self.bordeCal = tk.LabelFrame(self.barra_menu)
        self.bordefig = tk.LabelFrame(self.barra_menu)
        self.bordered = tk.LabelFrame(self.barra_menu)
        self.bordeerr = tk.LabelFrame(self.barra_menu)
        self.bordefun = tk.LabelFrame(self.barra_menu)
        self.bordesem = tk.LabelFrame(self.barra_menu)
        self.bordecon = tk.LabelFrame(self.barra_menu)
        
        #Creacion de los botones
        self.calculadora = tk.Button(self.bordeCal)
        self.figuras = tk.Button(self.bordefig)
        self.redondeo = tk.Button(self.bordered)
        self.error = tk.Button(self.bordeerr)
        self.funciones = tk.Button(self.bordefun)
        self.semilla = tk.Button(self.bordesem)
        self.convercion = tk.Button(self.bordecon)
        
        #informacion de los botones
        button_info = [
            (self.bordeCal, " 1) Calculadora ",self.calculadora, self.limpiarPanel),
            (self.bordefig, " 2) Figuras \nGeometricas ", self.figuras, self.limpiarPanel),
            (self.bordered, " 3) Redendeo \ny Truncamiento ", self.redondeo, self.limpiarPanel),
            (self.bordeerr, " 4) Error Absoluto \ny Relativo ", self.error, self.limpiarPanel),
            (self.bordefun, " 5) Funciones ", self.funciones, self.limpiarPanel),
            (self.bordesem, " 6) Semilla ",self.semilla, self.limpiarPanel),
            (self.bordecon, " 7) Converción \n Numerica ", self.convercion, self.limpiarPanel)
        ]
        
        #Configuracion de los botones
        for borde, text, boton, comando in button_info:
            self.config_boton_menu(borde, boton, text, font_awesome, ancho_menu, alto_menu, comando)
            
    def config_boton_menu(self, borde, boton, text, font_awesome, ancho_menu, alto_menu, comando):
        """Configuracion de los bordes y los botones del menu lateral"""
        borde.config(bd = 6, bg = "grey", padx=10, pady=17)
        borde.pack(side=tk.TOP)
    
        boton.config(text=f"{text}", ancho="w", font=font_awesome, bd=0, bg="light grey", width=ancho_menu, height=alto_menu, cursor = "circle", command = comando)
        boton.pack(side=tk.TOP)
    
    def limpiarPanel(self, panel):
        """Funcion para Destrio todos los hijos de panel gracias al winfo _children que se le indique limpiando el panel que baya encontrando por eso se encientra en un bucle parea que se pueda hubicar otro panel diferente """
        for widget in panel.winfo_children():
            widget.destroy()
            
# if __name__ == "__main__":
#     main()
