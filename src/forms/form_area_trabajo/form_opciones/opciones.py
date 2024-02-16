#importamos librerias
import tkinter as tk
from src.forms.form_area_trabajo.form_opciones.informacion import InfoDesign

def Opciones(self):
    
    texto = tk.Label(self.AreaTrabajo, text="Opciones de Configuración ", font = ("Arial", 35, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, fill="x")
    
    #frame para el tema 
    ftema = tk.Frame(self.AreaTrabajo, padx=30, pady=50, bg="light grey")
    ftema.pack(side=tk.TOP, fill="both", expand=True)
    
    tema = tk.Label(ftema, text=self.vteme, font = ("Arial", 35, "bold"), bg="light grey")
    tema.pack(side=tk.LEFT, fill="x")
    
    #borde del boton 1
    borderlineal = tk.LabelFrame(ftema, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.RIGHT, fill="x")
    #boton del tema
    bteme = tk.Button(borderlineal, text="Cambiar tema", font = ("Arial", 35, "bold"), command=lambda: [cambioTema(self)])
    bteme.pack()
    
    #borde del boton
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP)
    
    #boton de informacion
    info = tk.Button(borderlineal, text="Información", font = ("Arial", 35, "bold"), width=10,command=InfoDesign)
    info.pack()
    
def cambioTema(self):
    if self.vteme == "Claro":
        self.vteme = "Oscuro"
        self.limpiarPanel(self.AreaTrabajo)
        Opciones(self)
        
    elif self.vteme == "Oscuro":
        self.vteme = "Claro"
        self.limpiarPanel(self.AreaTrabajo)
        Opciones(self)
