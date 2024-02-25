#importamos librerias
import tkinter as tk

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 35, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Valor Exacto: ", font= ("Arial", 20, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    valEx = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    valEx.pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Valor Aproximado: ", font= ("Arial", 20, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    valApx = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    valApx.pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Error Absoluto: ", font= ("Arial", 20, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    errAb = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    errAb.pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Error Relativo: ", font= ("Arial", 20, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    errRl = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    errRl.pack(side=tk.TOP, expand=True)
    
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack(side=tk.TOP, expand=True)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold") )
    calcular.pack()

