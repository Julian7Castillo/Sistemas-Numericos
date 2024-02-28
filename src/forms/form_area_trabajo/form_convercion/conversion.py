#importamos librerias
import tkinter as tk
from tkinter.ttk import Combobox

def conversionNumerica(self):
    texto = tk.Label(self.AreaTrabajo, text="Conversión numérica", font = ("Arial", 35, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, expand=True)
    
    #combobox
    self.opciones = ["Binario","Octal","Decimal","Haxadecimal"]
    self.cmbOpciones = Combobox(self.AreaTrabajo, width="8", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones.pack(side=tk.TOP, expand=True)
    self.cmbOpciones.current(0)
    
    #frame para unir texto y entrada del valor
    fnum = tk.Frame(self.AreaTrabajo, bg="light grey")
    fnum.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fnum, text="Número: ", font = ("Arial", 35, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)

    entrada = tk.Entry(fnum, font = ("Arial", 25, "bold"))
    entrada.pack(side=tk.RIGHT, expand=True)

    #Combo box 
    self.opciones = ["Binario","Octal","Decimal","Haxadecimal"]
    self.cmbOpciones = Combobox(self.AreaTrabajo, width="8", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones.pack(side=tk.TOP, expand=True)
    self.cmbOpciones.current(0)
    
    #frame para unir texto y entrada del valor
    fres = tk.Frame(self.AreaTrabajo, bg="light grey")
    fres.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fres, text="Resultado: ", font = ("Arial", 35, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)
    
    resultado = tk.Entry(fres, font = ("Arial", 25, "bold"), state="readonly")
    resultado.pack(side=tk.RIGHT, expand=True)
    
    #borde del boton 1
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold") )
    calcular.pack()
