#importamos las librerias necesarias 
from tkinter import Scrollbar
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
        self.bienvenida()
    
    def configuracion(self):
        """Configuración de la ventana """
        self.title("Sistemas Numericos")
        self.geometry("1024x600")
        w,h = 1024, 600
        utl.centrar_ventana(self, w, h)
        
    def paneles(self):
        """Creación de los paneles que dividiran la interfaz """
        
        #Creacion de panel del menu
        self.barra_menu = tk.Frame(self, bg="grey")
        self.barra_menu.pack(side=tk.LEFT, fill="both", expand=False)
        
        #CReacion del panel del area de trabajo
        self.AreaTrabajo = tk.Frame(self, bg="light grey")
        self.AreaTrabajo.pack(side=tk.RIGHT, fill="both", expand=True)
        
        #Creacion de canvas
        self.canv = tk.Canvas(self.barra_menu, bg="grey", width=235)
        self.canv.pack(side="left", fill="both", expand = 1)
        
        #Declaracion de la barra de scroll
        self.scroll = Scrollbar(self.barra_menu, orient="vertical", command=self.canv.yview)
        self.scroll.pack(side="right", fill="y")
        
        #configuracion de canvas
        self.canv.configure(yscrollcommand=self.scroll.set)
        self.canv.bind('<Configure>', lambda e: self.canv.configure(scrollregion = self.canv.bbox("all")))
        
        #crear otro frame en el canvas 
        self.menu = tk.Frame(self.canv, bg="grey", width=310)
        
        #Agregar el nuevo frame al canvas
        self.canv.create_window((0,0), window = self.menu, anchor="nw")
        
        #Configuracion del scroll en el opanel
        self.scroll.config(command=self.barra_menu)

    def menuop(self):
        """Creación de menu lateral por medio de un ciclo para mejorar la eficiencia del código"""

        #datos del menu lateral
        ancho_menu = 16
        alto_menu = 2
        font_awesome = font.Font = ("Arial", 15, "bold")
        
        #Creacion de los bordes para lso botones
        self.bordeCal = tk.LabelFrame(self.menu)
        self.bordefig = tk.LabelFrame(self.menu)
        self.bordered = tk.LabelFrame(self.menu)
        self.bordeerr = tk.LabelFrame(self.menu)
        self.bordefun = tk.LabelFrame(self.menu)
        self.bordesem = tk.LabelFrame(self.menu)
        self.bordecon = tk.LabelFrame(self.menu)
        
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
            (self.bordeCal, " 1) Calculadora ",self.calculadora, self.cal),
            (self.bordefig, " 2) Figuras \nGeometricas ", self.figuras, self.limpiarPanel),
            (self.bordered, " 3) Redendeo \ny Truncamiento ", self.redondeo, self.limpiarPanel),
            (self.bordeerr, " 4) Error Absoluto \ny Relativo ", self.error, self.limpiarPanel),
            (self.bordefun, " 5) Funciones ", self.funciones, self.cambiarMenu),
            (self.bordesem, " 6) Semilla ",self.semilla, self.limpiarPanel),
            (self.bordecon, " 7) Converción \n Numerica ", self.convercion, self.limpiarPanel)
        ]
        
        #Configuracion de los botones
        for borde, text, boton, comando in button_info:
            self.config_boton_menu(borde, boton, text, font_awesome, ancho_menu, alto_menu, comando)
        
    def menufun(self):
        """Creacióm de menu latertal por mediuo de un cilo para mejorar la eficiencia del codigo"""

        #datos del menu lateral
        ancho_menu = 16
        alto_menu = 2
        font_awesome = font.Font = ("Arial", 15, "bold")
        
        #Creacion de los bordes para lso botones
        self.bordepoli = tk.LabelFrame(self.menu)
        self.borderaci = tk.LabelFrame(self.menu)
        self.borderadi = tk.LabelFrame(self.menu)
        self.bordeexpo = tk.LabelFrame(self.menu)
        self.bordeloga = tk.LabelFrame(self.menu)
        self.bordeVol = tk.LabelFrame(self.menu)
        
        #Creacion de los botones
        self.polinomicas = tk.Button(self.bordepoli)
        self.racionales = tk.Button(self.borderaci)
        self.radicales = tk.Button(self.borderadi)
        self.exponenciales = tk.Button(self.bordeexpo)
        self.logaritmica = tk.Button(self.bordeloga)
        self.volver = tk.Button(self.bordeVol)
        
        #informacion de los botones
        button_info = [
            (self.bordepoli, " 1) Funciones \nPolinomicas",self.polinomicas, self.limpiarPanel),
            (self.borderaci, " 2) Funciones \nRacionales", self.racionales, self.limpiarPanel),
            (self.borderadi, " 3) Funciones \nRadicales", self.radicales, self.limpiarPanel),
            (self.bordeexpo, " 4) Funciones\n Exponenciales", self.exponenciales, self.limpiarPanel),
            (self.bordeloga, " 5) Funciones\n Logaritmicas", self.logaritmica, self.limpiarPanel),
            (self.bordeVol, " 6) Volver",self.volver, self.volvermenup)
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
        
    def CalculadoraPanel(self):
        pass
    
    def limpiarPanel(self, panel):
        """Funcion para Destrio todos los hijos de panel gracias al winfo _children que se le indique limpiando el panel que baya encontrando por eso se encientra en un bucle parea que se pueda hubicar otro panel diferente """
        for widget in panel.winfo_children():
            widget.destroy()
    
    def cambiarMenu(self):
        self.limpiarPanel(self.barra_menu)
        self.menufun()
        
    def volvermenup(self):
        self.limpiarPanel(self.barra_menu)
        self.menuop()

    def bienvenida(self):
        texto = tk.Label(self.AreaTrabajo, text="Bienvenido", font = ("Arial", 35, "bold"))
        texto.pack(side=tk.TOP, fill="both", expand=True)
        
    def cal(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
# if __name__ == "__main__":
#     main()
