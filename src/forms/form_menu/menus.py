#importamos librerias
from tkinter import *
import tkinter as tk
from src.forms.form_area_trabajo.form_informacion.informacion import InfoDesign

#importamos las demas funiones de los otros archvos
#from areaTrabajo import *
#from Funciones import *

def menuop(self):
    """Creación de menu lateral por medio de un ciclo para mejorar la eficiencia del código"""

    #datos del menu lateral
    ancho_menu = 16
    alto_menu = 2
    font_awesome = font = ("Arial", 15, "bold")
    
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
    
    #informacion de los botones
    button_info = [
        (self.bordeCal, " 1)  Calculadora ",self.calculadora, self.cal),
        (self.bordefra, " 2)  Fracciones ",self.fracciones, self.fra),
        (self.bordefig, " 3)  Figuras      \nGeometricas", self.figuras, self.figGeo),
        (self.bordered, " 4)  Redendeo  y \n Truncamiento ", self.redondeo, self.red),
        (self.bordeerr, " 5)  Error Absoluto \n y Relativo ", self.error, self.errorab),
        (self.bordefun, " 6)  Funciones ", self.funciones, self.cambiarMenu),
        (self.bordesem, " 7)  Semilla ",self.semilla, self.sem),
        (self.bordecon, " 8)  Converción \n Numerica ", self.convercion, self.connum),
        (self.bordeop, " 9)  Opciones ", self.opciones, self.opci)
    ]
    
    #Configuracion de los botones
    for borde, text, boton, comando in button_info:
        self.config_boton_menu(borde, boton, text, font_awesome, ancho_menu, alto_menu, comando)
    
def menufun(self):
    """Creacióm de menu latertal por mediuo de un cilo para mejorar la eficiencia del codigo"""

    #datos del menu lateral
    ancho_menu = 16
    alto_menu = 2
    font_awesome = font = ("Arial", 15, "bold")
    
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
        (self.bordepoli, " 1)  Funciones    \nPolinomicas",self.polinomicas, self.funPolinomica),
        (self.borderaci, " 2)  Funciones    \nRacionales", self.racionales, self.funRacional),
        (self.borderadi, " 3)  Funciones    \nRadicales", self.radicales, self.funRadical),
        (self.bordeexpo, " 4)  Funciones    \nExponenciales", self.exponenciales, self.funExponencial),
        (self.bordeloga, " 5)  Funciones    \nLogaritmicas", self.logaritmica, self.funLogaritmica),
        (self.bordeVol, " 6)  Volver",self.volver, self.volvermenup)
    ]
    
    #Configuracion de los botones
    for borde, text, boton, comando in button_info:
        self.config_boton_menu(borde, boton, text, font_awesome, ancho_menu, alto_menu, comando)
        
    