#importamos librerias
import tkinter as tk

def error(self):
    
    valor_exacto =  float(self.valEx.get())
    valor_aproximado =  float(self.valApx.get())

    error_Absoluto = abs(valor_exacto - valor_aproximado)
    error_Relativo = abs(error_Absoluto / valor_exacto)
    
    self.errAb.configure(state = 'normal')
    self.errAb.delete(0,"end")
    self.errAb.insert(0,error_Absoluto)
    self.errAb.configure(state = 'disabled')
    
    self.errRl.configure(state = 'normal')
    self.errRl.delete(0,"end")
    self.errRl.insert(0,error_Relativo)
    self.errRl.configure(state = 'disabled')

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 35, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
     
    f1 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f1.pack(side=tk.TOP, expand=True)
    tk.Label(f1, text="Valor Exacto: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    self.valEx = tk.Entry(f1, font= ("Arial", 25))
    self.valEx.pack(side=tk.RIGHT, expand=True)
    
    f2 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f2.pack(side=tk.TOP, expand=True)
    tk.Label(f2, text="Valor Aproximado: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    self.valApx = tk.Entry(f2, font= ("Arial", 25))
    self.valApx.pack(side=tk.RIGHT, expand=True)
    
    f3 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f3.pack(side=tk.TOP, expand=True)
    tk.Label(f3, text="Error Absoluto: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    self.errAb = tk.Entry(f3, font= ("Arial", 25), state="readonly")
    self.errAb.pack(side=tk.RIGHT, expand=True)
    
    f4 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f4.pack(side=tk.TOP, expand=True)
    tk.Label(f4, text="Error Relativo: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    self.errRl = tk.Entry(f4, font= ("Arial", 25), state="readonly")
    self.errRl.pack(side=tk.RIGHT, expand=True)
    
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold"), command = lambda : [error(self)])
    calcular.pack()
