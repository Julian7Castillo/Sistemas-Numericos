#importamos librerias
import tkinter as tk

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="light gray").place(x=50,y=150)#.grid(column=1, row=1)
    valor = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    valor.place(x=350,y=160)#.grid(column=1, row=2)
