#importamos librerias
import tkinter as tk

def bienvenida(self):
    texto = tk.Label(self.AreaTrabajo, text="Bienvenido", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)

def panel_Constuccion(self):
    self.barra_superior = tk.Frame(self.AreaTrabajo)
    self.barra_superior.pack(side=tk.TOP, fill= tk.X, expand=False)
    
    self.barra_inferior = tk.Frame(self.AreaTrabajo)
    self.barra_inferior.pack(side=tk.BOTTOM, fill="both", expand=True)
    
    self.labelTitulo = tk.Label(self.barra_superior, text = " Panel en cosntrucción")
    self.labelTitulo.config(fg = "#222d33", font=("Roboto", 30), bg="light grey")
    self.labelTitulo.pack(side=tk.TOP, fill="both", expand=True)
    
    self.label_Imagebn = tk.Label(self.barra_inferior, image=self.img_sitio_construccion)
    self.label_Imagebn.place(x = 0, y = 0, relwidth=1, relheight=1)
    self.label_Imagebn.config(fg = "#fff", font=("Roboto", 10), bg="light grey")
