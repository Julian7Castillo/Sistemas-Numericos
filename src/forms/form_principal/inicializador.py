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
        #crear paneles: barra superior, menu lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg="#2A3138", height=50)
        self.barra_superior.pack(side=tk.TOP, fill="both")
        
        titulo = tk.Label(self.barra_superior, text="Sistemas numericos", fg="white",bg="#2A3138", font = ("Arial", 35, "bold"))
        titulo.pack()
        
        #Creacion de panel del menu
        self.barra_menu = tk.Frame(self, bg="grey")
        self.barra_menu.pack(side=tk.LEFT, fill="both", expand=False)
        
        #Creacion de canvas menu
        self.canvmenu = tk.Canvas(self.barra_menu, bg="grey", width=235)
        self.canvmenu.pack(side="left", fill="both", expand = 1)
        
        #Declaracion de la barra de scroll del menu
        self.scrollmenu = Scrollbar(self.barra_menu, orient="vertical", command=self.canvmenu.yview)
        self.scrollmenu.pack(side="right", fill="y")
        
        #configuracion de canvas del menu
        self.canvmenu.configure(yscrollcommand=self.scrollmenu.set)
        self.canvmenu.bind('<Configure>', lambda e: self.canvmenu.configure(scrollregion = self.canvmenu.bbox("all")))
        
        #crear otro frame en el canvas del menu
        self.menu = tk.Frame(self.canvmenu)
        
        #Agregar el nuevo frame al canvas del menu
        self.canvmenu.create_window((0,0), window = self.menu, anchor="nw")
        
        #CReacion del panel del area de trabajo
        self.AreaTrabajo = tk.Frame(self, bg="light grey")
        self.AreaTrabajo.pack(side=tk.RIGHT, fill="both", expand=True)
        
        #codigo ocmentado del scrop para el area de trabajo 
        #Creacion de canvas trabajo
        #self.canvtrab = tk.Canvas(self.AreaTrabajo, bg="grey")
        #self.canvtrab.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.999)
        #self.canvtrab.pack(side="left", fill="both", expand = 1)
        
        #Declaracion de la barra de scrolldel area de trabajo
        #self.scrolltrab = Scrollbar(self.AreaTrabajo, orient="vertical", command=self.canvtrab.yview)
        #self.scrolltrab.place(relx=0.98, rely=0.001, relwidth=0.02, relheight=0.999)
        #self.scrolltrab.pack(side="right", fill="y")
        
        #configuracion de canvas del area de trabajo
        #self.canvtrab.configure(yscrollcommand=self.scrolltrab.set)
        #self.canvtrab.bind('<Configure>', lambda e: self.canvtrab.configure(scrollregion = self.canvtrab.bbox("all")))
        
        #crear otro frame en el canvas del area de trabajo
        #self.trab = tk.Frame(self.canvtrab)
        
        #Agregar el nuevo frame al canvas del area de trabajo
        #self.canvtrab.create_window((0,0), window = self.trab, anchor="nw")

    def menuop(self):
        """Creación de menu lateral por medio de un ciclo para mejorar la eficiencia del código"""

        #datos del menu lateral
        ancho_menu = 16
        alto_menu = 2
        font_awesome = font.Font = ("Arial", 15, "bold")
        
        #Creacion de los bordes para lso botones
        self.bordeCal = tk.LabelFrame(self.menu)
        self.bordefra = tk.LabelFrame(self.menu)
        self.bordefig = tk.LabelFrame(self.menu)
        self.bordered = tk.LabelFrame(self.menu)
        self.bordeerr = tk.LabelFrame(self.menu)
        self.bordefun = tk.LabelFrame(self.menu)
        self.bordesem = tk.LabelFrame(self.menu)
        self.bordecon = tk.LabelFrame(self.menu)
        self.bordeop = tk.LabelFrame(self.menu)
        self.bordeinfo = tk.LabelFrame(self.menu)
        
        #Creacion de los botones
        self.calculadora = tk.Button(self.bordeCal)
        self.fracciones = tk.Button(self.bordefra)
        self.figuras = tk.Button(self.bordefig)
        self.redondeo = tk.Button(self.bordered)
        self.error = tk.Button(self.bordeerr)
        self.funciones = tk.Button(self.bordefun)
        self.semilla = tk.Button(self.bordesem)
        self.convercion = tk.Button(self.bordecon)
        self.opciones = tk.Button(self.bordeop)
        self.informacion = tk.Button(self.bordeinfo)
        
        #informacion de los botones
        button_info = [
            (self.bordeCal, " 1)  Calculadora ",self.calculadora, self.cal),
            (self.bordefra, " 2)  Fracciones ",self.fracciones, self.fra),
            (self.bordefig, " 3)  Figuras      \nGeometricas", self.figuras, self.figGeo),
            (self.bordered, " 4)  Redendeo  y \n Truncamiento ", self.redondeo, self.red),
            (self.bordeerr, " 5)  Error Absoluto \n y Relativo ", self.error, self.error),
            (self.bordefun, " 6)  Funciones ", self.funciones, self.cambiarMenu),
            (self.bordesem, " 7)  Semilla ",self.semilla, self.sem),
            (self.bordecon, " 8)  Converción \n Numerica ", self.convercion, self.connum),
            (self.bordeop, " 9)  Opciones ", self.opciones, self.opci),
            (self.bordeinfo, " 10)  Información ", self.informacion, self.infor)
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
            (self.bordepoli, " 1)  Funciones    \nPolinomicas",self.polinomicas, self.limpiarPanel),
            (self.borderaci, " 2)  Funciones    \nRacionales", self.racionales, self.limpiarPanel),
            (self.borderadi, " 3)  Funciones    \nRadicales", self.radicales, self.limpiarPanel),
            (self.bordeexpo, " 4)  Funciones    \nExponenciales", self.exponenciales, self.limpiarPanel),
            (self.bordeloga, " 5)  Funciones    \nLogaritmicas", self.logaritmica, self.limpiarPanel),
            (self.bordeVol, " 6)  Volver",self.volver, self.volvermenup)
        ]
        
        #Configuracion de los botones
        for borde, text, boton, comando in button_info:
            self.config_boton_menu(borde, boton, text, font_awesome, ancho_menu, alto_menu, comando)
    
    def config_boton_menu(self, borde, boton, text, font_awesome, ancho_menu, alto_menu, comando):
        """Configuracion de los bordes y los botones del menu lateral"""
        borde.config(bd = 6, bg = "#2A3138", padx=10, pady=17)#grey
        borde.pack(side=tk.TOP)
    
        boton.config(text=f"{text}", ancho="w", font=font_awesome, bd=0, bg="#32404F", fg="white", width=ancho_menu, height=alto_menu, cursor = "circle", command = comando) #light grey
        boton.pack(side=tk.TOP)
        
    def CalculadoraPanel(self):
        pass
    
    def limpiarPanel(self, panel):
        """Funcion para Destrio todos los hijos de panel gracias al winfo _children que se le indique limpiando el panel que baya encontrando por eso se encientra en un bucle parea que se pueda hubicar otro panel diferente """
        for widget in panel.winfo_children():
            widget.destroy()
    
    def cambiarMenu(self):
        self.limpiarPanel(self.menu)
        self.menufun()
        
    def volvermenup(self):
        self.limpiarPanel(self.menu)
        self.menuop()

    def bienvenida(self):
        texto = tk.Label(self.AreaTrabajo, text="Bienvenido", font = ("Arial", 35, "bold"))
        texto.pack(side=tk.TOP, fill="both", expand=True)
        
    def cal(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
    
    def fra(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
    
    def figGeo(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
    
    def red(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    def error(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    def sem(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    def connum(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    def opci(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    def infor(self):
        self.limpiarPanel(self.AreaTrabajo)
        self.CalculadoraPanel()
        
    
# if __name__ == "__main__":
#     main()
