#importamos librerias
import tkinter as tk
from tkinter.ttk import Combobox
from src.forms.form_area_trabajo.form_convercion.logic.logic_conversion import calConversion

def comunicacion(self):
    inicial = self.cmbOpciones1.get()
    if(inicial == "Decimal"):
        valor = int(self.entrada.get())
    else:
        valor = str(self.entrada.get())
        
    final = self.cmbOpciones2.get()
    
    resultado = calConversion(inicial, valor, final)
    print(resultado)
    
    self.resultado.configure(state = 'normal')
    self.resultado.delete(0,"end")
    self.resultado.insert(0, resultado)
    self.resultado.configure(state = 'disabled')

def conversionNumerica(self):
    texto = tk.Label(self.AreaTrabajo, text="Conversión numérica", font = ("Arial", 35, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, expand=True)
    
    #combobox
    self.opciones = ["Binario","Octal","Decimal","Haxadecimal"]
    self.cmbOpciones1 = Combobox(self.AreaTrabajo, width="12", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones1.pack(side=tk.TOP, expand=True)
    self.cmbOpciones1.current(0)
    
    #frame para unir texto y entrada del valor
    fnum = tk.Frame(self.AreaTrabajo, bg="light grey")
    fnum.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fnum, text="Número: ", font = ("Arial", 35, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)

    self.entrada = tk.Entry(fnum, font = ("Arial", 25, "bold"))
    self.entrada.pack(side=tk.RIGHT, expand=True)

    #Combo box 
    self.opciones = ["Binario","Octal","Decimal","Haxadecimal"]
    self.cmbOpciones2 = Combobox(self.AreaTrabajo, width="12", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones2.pack(side=tk.TOP, expand=True)
    self.cmbOpciones2.current(0)
    
    #frame para unir texto y entrada del valor
    fres = tk.Frame(self.AreaTrabajo, bg="light grey")
    fres.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fres, text="Resultado: ", font = ("Arial", 35, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)
    
    self.resultado = tk.Entry(fres, font = ("Arial", 25, "bold"), state="readonly")
    self.resultado.pack(side=tk.RIGHT, expand=True)
    
    #borde del boton 1
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold"), command=lambda: [comunicacion(self)] )
    calcular.pack()
