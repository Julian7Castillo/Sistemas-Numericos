import tkinter as tk

def figurasGeometricas(self, figura):
    texto = tk.Label(self.AreaTrabajo, text="Figuras geometricas", font = ("Arial", 30, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, fill="x", expand=True)
    
    if(figura == 0):
        #texto de la figura 
        texfig = tk.Label(self.AreaTrabajo, text="Cuadrado", font = ("Arial", 20, "bold"), bg="light grey")
        texfig.pack(side=tk.LEFT, fill="y", expand=True)
        
        #frame donde se mostrara la figura y los campos a llenar 
        fig = tk.Frame(self.AreaTrabajo, bg="light grey")
        fig.pack(side=tk.RIGHT, fill="both", expand=True)
        
        l1 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)
        l1.grid(column=0, row=0)
        
        cua = tk.Label(fig, image = self.img_Cuadrado, padx=50, pady=50)  
        cua.grid(column=0, row=2)  
        
        l2 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)   
        l2.grid(column=1, row=2)
        
        #borde del boton 1
        borderlineal = tk.LabelFrame(fig, bd = 6, bg = "DodgerBlue2")
        borderlineal.grid(column=0, row=4)
        calcular = tk.Button(borderlineal, text="Calcular" )
        calcular.pack()
    
    elif(figura == 1):
        texfig = tk.Label(self.AreaTrabajo, text="Triangulo", font = ("Arial", 20, "bold"), bg="light grey")
        texfig.pack(side=tk.TOP, fill="x", expand=True)
    
    elif(figura == 2):
        texfig = tk.Label(self.AreaTrabajo, text="Rectangulo", font = ("Arial", 20, "bold"), bg="light grey")
        texfig.pack(side=tk.TOP, fill="x", expand=True)
    
    elif(figura == 3):
        texfig = tk.Label(self.AreaTrabajo, text="Circulo", font = ("Arial", 20, "bold"), bg="light grey")
        texfig.pack(side=tk.TOP, fill="x", expand=True)
    
    elif(figura == 4):
        texfig = tk.Label(self.AreaTrabajo, text="Paralelogramo", font = ("Arial", 20, "bold"), bg="light grey")
        texfig.pack(side=tk.TOP, fill="x", expand=True)
