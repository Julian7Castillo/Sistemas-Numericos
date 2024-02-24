#importamos librerias
import tkinter as tk

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 35, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    valor = tk.Entry(self.AreaTrabajo, font= ("Arial", 25))
    valor.pack(side=tk.TOP, expand=True)
    
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 25, "bold"), justify="center", bg="light gray").pack(side=tk.TOP, expand=True)
    
    valor = tk.Entry(self.AreaTrabajo, font= ("Arial", 25))
    valor.pack(side=tk.TOP, expand=True)
