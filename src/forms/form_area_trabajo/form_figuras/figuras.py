import tkinter as tk
from src.forms.form_area_trabajo.form_figuras.logic.areaPerimetro import CalcularResultado

def llamado(self, fig):
    l1 = int(self.l1.get())
    l2 = int(self.l2.get())
    #l3 = int(self.l3.get())
    area, perimetro = CalcularResultado(self, fig, l1, l2)
    
    self.r1.configure(state = 'normal')
    self.r1.delete(0,"end")
    self.r1.insert(0,area)
    self.r1.configure(state = 'disabled')
    
    self.r2.configure(state = 'normal')
    self.r2.delete(0,"end")
    self.r2.insert(0, perimetro)
    self.r2.configure(state = 'disabled')
    
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
    
    #Creacion predetermionada
    self.l1 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)
    self.l2 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3)
    self.l3 = tk.Entry(fig, font = ("Arial", 20, "bold"), width=3) 
    
    if(figura == 0):

        vfigura ="Cuadrado"
        varea = "Area = L1 * L2"
        vperimetro = "Perimetro = L1 + L2 + L3 + L4"
         
        #ajustes de ubicacion de la figura
        self.l1.grid(column=0, row=0)
        
        self.l = tk.Label(fig, height=2, bg="light grey")
        self.l.grid(column=0, row=1)
        
        imgfig = tk.Label(fig, image = self.img_Cuadrado, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)  
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=2)
         
        self.l2.grid(column=2, row=2)
    
    elif(figura == 1):
        vfigura ="Triangulo"
        varea = "Area = (B * A) / 2"
        vperimetro = "Perimetro = L1 + L2 + L3 "
        
        #configuracion de la figura
        imgfig = tk.Label(fig, image = self.img_Triangulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=2)
        
        self.l1.grid(column=2, row=2)
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=3)
        
        self.l2.grid(column=0, row=4)
    
    elif(figura == 2):
        vfigura ="Rectangulo"
        varea = "Area = B * A"
        vperimetro = "Perimetro = L1 + L2 + L3 + L4"
        
        #configuracion de la figura
        self.l1.grid(column=0, row=0)
        
        self.l = tk.Label(fig, height=2, bg="light grey")
        self.l.grid(column=0, row=1)
        
        imgfig = tk.Label(fig, image = self.img_Rectangulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=2)
          
        self.l2.grid(column=2, row=2)
    
    elif(figura == 3):
        vfigura ="Circulo"
        varea = "Area = pi * r**2 "
        vperimetro = "Perimetro = pi * d "
        
        #configuracion de la figura
        self.l1.grid(column=0, row=0)
        
        self.l = tk.Label(fig, height=2, bg="light grey")
        self.l.grid(column=0, row=1)
        
        imgfig = tk.Label(fig, image = self.img_Circulo, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=2)
        
        self.l2.grid(column=2, row=2)
    
    elif(figura == 4):
        vfigura ="Trapecio"
        varea = "Area = (h(B + b)) / 2"
        vperimetro = "Perimetro = B + b + h + h"
        
        #configuracion de la figura
        self.l1.grid(column=0, row=0)
        
        self.l = tk.Label(fig, height=1, bg="light grey")
        self.l.grid(column=0, row=1)
        
        imgfig = tk.Label(fig, image = self.img_Trapecio, padx=50, pady=50)  
        imgfig.grid(column=0, row=2)
        
        self.l = tk.Label(fig, width=3, bg="light grey")
        self.l.grid(column=1, row=2)
        
        self.l2.grid(column=2, row=2)
        
        self.l = tk.Label(fig, width=1, bg="light grey")
        self.l.grid(column=1, row=3)
          
        self.l3.grid(column=0, row=4)

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
    self.r1 =tk.Entry(ar, font = ("Arial", 20, "bold"), state="readonly")
    self.r1.pack(side=tk.RIGHT)
    
    per = tk.Frame(dat, bg="light grey")
    per.pack(side=tk.TOP, fill="both", expand=True)
    
    texfig = tk.Label(per, text="Perimetro:", font = ("Arial", 20, "bold"), bg="light grey")
    texfig.pack(side=tk.LEFT, fill="both", expand=True)
    self.r2 =tk.Entry(per, font = ("Arial", 20, "bold"), state="readonly")
    self.r2.pack(side=tk.RIGHT)
    
    l = tk.Label(fig, height=1, bg="light grey")
    l.grid(column=0, row=5)
    
    #borde del boton 1
    borderlineal = tk.LabelFrame(fig, bd = 6, bg = "DodgerBlue2")
    borderlineal.grid(column=0, row=6)
    calcular = tk.Button(borderlineal, text="Calcular", width=15, font = ("Arial", 15, "bold"), command=lambda: [llamado(self, figura)] )
    calcular.pack()