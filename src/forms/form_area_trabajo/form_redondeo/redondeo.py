#importamos librerias
import tkinter as tk
from tkinter.ttk import Combobox

def logic(self):
    
    x = float(self.entrada.get())
    
    if(self.cmbOpciones.get() == "1 decima"):
        dec = 1
    elif(self.cmbOpciones.get() == "2 decimas"):
        dec = 2
    elif(self.cmbOpciones.get() == "3 decimas"):
        dec = 3
    elif(self.cmbOpciones.get() == "4 decimas"):
        dec = 4
        
    #procesdo de redondeado
    redo = round(x, dec)

    #proceso de truncamiento
    trun = int(x * (10**dec))/(10**dec)

    self.resultadoredo.configure(state = "normal")
    self.resultadoredo.delete(0, "end")
    self.resultadoredo.insert(0, redo)
    self.resultadoredo.configure(state = "disable")
    
    self.resultadotrun.configure(state = "normal")
    self.resultadotrun.delete(0, "end")
    self.resultadotrun.insert(0, trun)
    self.resultadotrun.configure(state = "disabel")
    
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

    self.entrada = tk.Entry(fnum, font = ("Arial", 25, "bold"))
    self.entrada.pack(side=tk.RIGHT, expand=True)
    
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
    
    self.resultadoredo = tk.Entry(fres, font = ("Arial", 25, "bold"), state="readonly")
    self.resultadoredo.pack(side=tk.RIGHT, expand=True)
    
    #frame para unir texto y entradade resultado de truncamiento
    fres = tk.Frame(self.AreaTrabajo, bg="light grey")
    fres.pack(side=tk.TOP, expand=True)
    
    tn1 = tk.Label(fres, text="Truncamiento: ", font = ("Arial", 25, "bold"), bg="light grey")
    tn1.pack(side=tk.LEFT, expand=True)
    
    self.resultadotrun = tk.Entry(fres, font = ("Arial", 25, "bold"), state="readonly")
    self.resultadotrun.pack(side=tk.RIGHT, expand=True)

    #borde del boton 1
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold"), command= lambda: [logic(self)])
    calcular.pack()#, command =  lambda: [red(frmprt, x, dec)])
