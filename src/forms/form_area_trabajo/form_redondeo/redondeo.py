#importamos librerias
import tkinter as tk
from tkinter.ttk import Combobox

def redondeoTruncamiento(self):
    """Frame del area de trabajo de redondeo y truncamiento"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Redondeo y Truncamiento", font= ("Arial", 35, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    #frame para unir texto y entrada del valor
    fnum = tk.Frame(self.AreaTrabajo, bg="light grey")
    fnum.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fnum, text="Número: ", font = ("Arial", 25, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)

    entrada = tk.Entry(fnum, font = ("Arial", 25, "bold"))
    entrada.pack(side=tk.RIGHT, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Seleccione los decimales: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    #combobox
    self.opciones = ["1 decima","2 decimas","3 decimas","4 decimas"]
    self.cmbOpciones = Combobox(self.AreaTrabajo, width="8", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones.pack(side=tk.TOP, expand=True)
    self.cmbOpciones.current(0)
    
    #frame para unir texto y entrada del resultado del Redondeo
    fres = tk.Frame(self.AreaTrabajo, bg="light grey")
    fres.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fres, text="Redondeo: ", font = ("Arial", 25, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)
    
    resultado = tk.Entry(fres, font = ("Arial", 25, "bold"))
    resultado.pack(side=tk.RIGHT, expand=True)
    
    #frame para unir texto y entradade resultado de truncamiento
    fres = tk.Frame(self.AreaTrabajo, bg="light grey")
    fres.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fres, text="Truncamiento: ", font = ("Arial", 25, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)
    
    resultado = tk.Entry(fres, font = ("Arial", 25, "bold"))
    resultado.pack(side=tk.RIGHT, expand=True)

    #borde del boton 1
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold") )
    calcular.pack()#, command =  lambda: [red(frmprt, x, dec)])
