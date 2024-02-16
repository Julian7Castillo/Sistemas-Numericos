#importamos librerias
import tkinter as tk

def redondeoTruncamiento(self):
    """Frame del area de trabajo de redondeo y truncamiento"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Redondeo y Truncamiento", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="light gray").place(x=30,y=110)#.grid(column=1, row=1)
    x = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    x.place(x=350,y=120)#.grid(column=1, row=2)
    tk.Label(self.AreaTrabajo, text="Seleccione los decimales: ", font= ("Arial", 30, "bold"), justify="center", bg="light gray").place(x=30,y=180)
    #dec = ttk.Combobox(frmprt, text="Decimales", values=[1,2,3,4,5], height=5, width=5, font= ("Arial",20, "bold"))
    #dec.place(x=830,y=190)

    #botones de truncamienot y de redondeo 
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2", padx= 10, pady=10)
    borderlineal.place(x=130,y=250)#.grid(column=1, row=1)
    #botonlineal = Button(borderlineal, text = "Redendear y Truncar", bg="light grey",width = 20, height= 1, font = ("Arial", 30, "bold"), cursor = "circle", command =  lambda: [red(frmprt, x, dec)])
    #botonlineal.pack()
