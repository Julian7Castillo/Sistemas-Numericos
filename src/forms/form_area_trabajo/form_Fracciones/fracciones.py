import tkinter as tk
from tkinter.ttk import Combobox

def Fracciones(self):
    texto = tk.Label(self.AreaTrabajo, text="Fracciones", font = ("Arial", 35, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, fill="x", expand=True)
    
    #Frame de fraccione
    ff = tk.Frame(self.AreaTrabajo, padx=20, pady=10, bg="light grey")
    ff.pack(side=tk.TOP, fill="x", expand=True)
    
    #FRACCION 1
    #frame para la fraccion
    ffrac1 = tk.Frame(ff, padx=20, pady=20, bg="light grey")
    ffrac1.pack(side=tk.LEFT, fill="x", expand=True)
    
    #etiquetas de titulos de fracciones 
    tk.Label(ffrac1, text="Fraccion 1:", font = ("Arial", 25), bg="light grey").grid(row=0, column=0, rowspan=2)
    
    #frame para la entrada del entero
    fx1 = tk.Frame(ffrac1, padx=20, pady=20, bg="light grey")
    fx1.grid(row=3, column=0)
    
    #label y entrada de texto 
    tk.Label(fx1, text="Ent", font = ("Arial", 25), bg="light grey").pack(side="left")
    self.txt1E = tk.Entry(fx1, width=3, font = ("Arial", 25))
    self.txt1E.pack(side="right", expand=True)
    
    #dos entradas de texto y un label indicando que son dfe la fraccionfuera del tercer frame 
    tk.Label(ffrac1, text="Num", font = ("Arial", 25), bg="light grey").grid(row=3, column=2)
    tk.Label(ffrac1, text="den", font = ("Arial", 25), bg="light grey").grid(row=4, column=2)
    
    self.txt1N = tk.Entry (ffrac1, width=3, font = ("Arial", 25))
    self.txt1D = tk.Entry (ffrac1, width=3, font = ("Arial", 25))
    self.txt1N.grid(row=3, column=1)
    self.txt1D.grid(row=4, column=1)
    
    #FRACCION 2
    #frame para la fraccion
    ffrac2 = tk.Frame(ff, padx=20, pady=20, bg="light grey")
    ffrac2.pack(side=tk.RIGHT, fill="x", expand=True)
    
    #etiquetas de titulos de fracciones
    tk.Label(ffrac2, text="Fraccion 2:", font = ("Arial", 25), bg="light grey").grid(row=0, column=0)
    
    #frame para la entrada del entero
    fx2 = tk.Frame(ffrac2, padx=20, pady=20, bg="light grey")
    fx2.grid(row=3, column=0) 
    
    #label y entrada de texto 
    tk.Label(fx2, text="Ent", font = ("Arial", 25), bg="light grey").pack(side="left", expand=True)
    self.txt2E = tk.Entry(fx2, width=3, font = ("Arial", 25))
    self.txt2E.pack(side="right", expand=True)
    
    #dos entradas de texto y un label indicando que son dfe la fraccionfuera del tercer frame 
    tk.Label(ffrac2, text="Num", font = ("Arial", 25), bg="light grey").grid(row=3, column=2)
    tk.Label(ffrac2, text="den", font = ("Arial", 25), bg="light grey").grid(row=4, column=2)
    
    self.txt2N = tk.Entry (ffrac2, width=3, font = ("Arial", 25))
    self.txt2D = tk.Entry (ffrac2, width=3, font = ("Arial", 25))
    self.txt2N.grid(row=3, column=1)
    self.txt2D.grid(row=4, column=1)
    
    #parte del error
    #frame de tipo de operacion 
    ff1 = tk.Frame(self.AreaTrabajo, padx=200, pady=10, bg="light grey")
    ff1.pack(side=tk.TOP, fill="x", expand=True)
    
    #Textos aparte de las fracciones para indicar las operaciones y el resultado
    tk.Label(ff1, text="Operacion:", font = ("Arial", 25), bg="light grey").pack(side=tk.LEFT)
    
    #combobox
    self.opciones = ["Suma","Resta","Multiplicación","División", "Son Iguales"]
    self.cmbOpciones = Combobox(ff1, width="8", value=self.opciones, state="readonly", font = ("Arial", 25))
    self.cmbOpciones.pack(side=tk.RIGHT, expand=True)
    self.cmbOpciones.current(0)
    
    #frame de tipo de operacion 
    ff2 = tk.Frame(self.AreaTrabajo, padx=200, bg="light grey", pady=10)
    ff2.pack(side=tk.TOP, fill="x", expand=True)
    
    tk.Label(ff2, text="Resultado: ", font = ("Arial", 25), bg="light grey").pack(side=tk.LEFT)
    
    #campo de texto para el resultado
    self.txtRes = tk.Entry(ff2, width=9, font = ("Arial", 25))
    self.txtRes.pack(side=tk.RIGHT, expand=True)

    #borde del boton
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.BOTTOM)
    
    #Boton para hacer las operaciones
    self.btnCalcular = tk.Button(borderlineal, text="Calcular", font = ("Arial", 25))#, command = self.fCalcular)
    self.btnCalcular.pack()
