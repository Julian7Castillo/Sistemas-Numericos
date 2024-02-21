import tkinter as tk

def figurasGeometricas(self, figura):
    texto = tk.Label(self.AreaTrabajo, text="Figuras geometricas", font = ("Arial", 30, "bold"), bg="light grey", pady=20)
    texto.pack(side=tk.TOP, fill="x")
    
    #datos 
    dat = tk.Frame(self.AreaTrabajo, bg="light grey")
    dat.pack(side=tk.LEFT, fill="y", expand=True)
    
    #frame donde se mostrara la figura y los campos a llenar 
    fig = tk.Frame(self.AreaTrabajo, bg="light grey", padx=10)
    fig.pack(side=tk.RIGHT, fill="both", expand=True)
        
    vfigura = ""
    varea = ""
    vperimetro = ""
    
    if(figura == 0):

        vfigura ="Cuadrado"
        varea = "Area = L * L"
        vperimetro = "Perimetro = L + L + L + L"
         
        #ajustes de ubicacion de la figura
        l1 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)
        l1.grid(column=0, row=0)
        
        l = tk.Label(fig, height=2, bg="light grey")
        l.grid(column=0, row=1)
        
        imgfig = tk.Label(fig, image = self.img_Cuadrado, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)  
        
        l = tk.Label(fig, width=3, bg="light grey")
        l.grid(column=1, row=2)
        
        l2 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)   
        l2.grid(column=2, row=2)
        
        l = tk.Label(fig, height=3, bg="light grey")
        l.grid(column=0, row=3)
    
    elif(figura == 1):
        vfigura ="Triangulo"
        varea = "Area = (B * A) / 2"
        vperimetro = "Perimetro = L1 + L2 + L3 "
        
        #configuracion de la figura
        imgfig = tk.Label(fig, image = self.img_Triangulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
    
    elif(figura == 2):
        vfigura ="Rectangulo"
        varea = "Area = B * A"
        vperimetro = "Perimetro = L1 + L2 + L3 + L4"
        
        #configuracion de la figura
        imgfig = tk.Label(fig, image = self.img_Rectangulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
    
    elif(figura == 3):
        vfigura ="Circulo"
        varea = "Area = "
        vperimetro = "Perimetro = "
        
        #configuracion de la figura
        imgfig = tk.Label(fig, image = self.img_Circulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
    
    elif(figura == 4):
        vfigura ="Paralelogramo"
        varea = "Area = "
        vperimetro = "Perimetro = "
        
        #configuracion de la figura
        imgfig = tk.Label(fig, image = self.img_Paralelogramo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)

    #texto de la figura 
    texfig = tk.Label(dat, text=vfigura, font = ("Arial", 20, "bold"), bg="light grey")
    texfig.pack(side=tk.TOP, fill="both", expand=True)
    
    #Formula usada para la figura 
    texarea = tk.Label(dat, text=varea, font = ("Arial", 20, "bold"), bg="light grey")
    texarea.pack(side=tk.TOP, fill="both", expand=True)
    
    texper = tk.Label(dat, text=vperimetro, font = ("Arial", 20, "bold"), bg="light grey")
    texper.pack(side=tk.TOP, fill="both", expand=True)
    
    resultado = tk.Label(dat, text="Resultado", font = ("Arial", 20, "bold"), bg="light grey")
    resultado.pack(side=tk.TOP, fill="both", expand=True)
    
    #frame para mostrar en linea los resultados del area y del perimetro
    ar = tk.Frame(dat, padx=10, bg="light grey")
    ar.pack(side=tk.TOP, fill="both", expand=True)
    
    texfig = tk.Label(ar, text="Area:", font = ("Arial", 20, "bold"), bg="light grey")
    texfig.pack(side=tk.LEFT, fill="both", expand=True)
    r1 =tk.Entry(ar, font = ("Arial", 20, "bold"))
    r1.pack(side=tk.RIGHT)
    
    per = tk.Frame(dat, bg="light grey")
    per.pack(side=tk.TOP, fill="both", expand=True)
    
    texfig = tk.Label(per, text="Perimetro:", font = ("Arial", 20, "bold"), bg="light grey")
    texfig.pack(side=tk.LEFT, fill="both", expand=True)
    r2 =tk.Entry(per, font = ("Arial", 20, "bold"))
    r2.pack(side=tk.RIGHT)
        
    #borde del boton 1
    borderlineal = tk.LabelFrame(fig, bd = 6, bg = "DodgerBlue2")
    borderlineal.grid(column=0, row=4)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold") )
    calcular.pack()