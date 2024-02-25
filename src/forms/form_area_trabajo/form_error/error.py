#importamos librerias
import tkinter as tk

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 35, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
     
    f1 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f1.pack(side=tk.TOP, expand=True)
    tk.Label(f1, text="Valor Exacto: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    valEx = tk.Entry(f1, font= ("Arial", 25))
    valEx.pack(side=tk.RIGHT, expand=True)
    
    f2 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f2.pack(side=tk.TOP, expand=True)
    tk.Label(f2, text="Valor Aproximado: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    valApx = tk.Entry(f2, font= ("Arial", 25))
    valApx.pack(side=tk.RIGHT, expand=True)
    
    f3 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f3.pack(side=tk.TOP, expand=True)
    tk.Label(f3, text="Error Absoluto: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    errAb = tk.Entry(f3, font= ("Arial", 25))
    errAb.pack(side=tk.RIGHT, expand=True)
    
    f4 = tk.Frame(self.AreaTrabajo, bg = "light gray")
    f4.pack(side=tk.TOP, expand=True)
    tk.Label(f4, text="Error Relativo: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.LEFT, expand=True)
    errRl = tk.Entry(f4, font= ("Arial", 25))
    errRl.pack(side=tk.RIGHT, expand=True)
    
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold") )
    calcular.pack()

