#importamos librerias
import tkinter as tk
#from Controlador.controladorBotones import red, error, fsemilla

def general(self, tip):
    """Funcion se seleccion de tipo de funcion a mostrar por pantalla en el area de trabajo"""

    #variables de loso campos d las funciones    
    fxentry2 = 0
    fxentry3 = 0 
    fxentry4 = 0 
    fxentry5 = 0 
    fxentry6 = 0
    
    frameg = tk.Frame(self.AreaTrabajo, bg="light grey")
        
    if tip == 1:
        # texto del tituo
        tk.Label(self.AreaTrabajo, text="1) Funciones Polinomicas", font= ("Arial", 40, "bold"), justify="center", bg="light grey").pack(side=tk.TOP)#.place(x=20,y=20)#.grid(column=1, row=1)
        frameg.pack(side=tk.TOP, fill="both", expand=True)
        
        fx = tk.Label(frameg, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 5, y = 120)
        fxentry = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry.place(x = 120, y = 130)
        fx = tk.Label(frameg, text = "x^3 +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 200, y = 100)
        fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry2.place(x = 320, y = 130)
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 400, y = 100)
        fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry3.place(x = 520, y = 130)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 600, y = 100)
        fxentry4 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry4.place(x = 670, y = 130)
        
    elif tip == 2:
       # texto del tituo
        tk.Label(frameg, text="2) Funciones Racionales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").pack(side=tk.TOP)#.grid(column=1, row=1)
        #objetos y pociciones de la formula 
        frameg.pack(side=tk.TOP, fill="both", expand=True)
        
        fx = tk.Label(frameg, text = "f(x) = ", pady = 10, font= ("Arial", 35), bg="light gray").place(x = 20, y = 190)
        fxentry = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 110) 
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 250, y = 110)
        fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 400, y = 110)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 500, y = 110)
        fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 600, y = 110)
        linea = tk.Label(frameg, text = "_____________________", font= ("Arial", 35), bg="light gray").place(x = 160, y = 180) 
        fxentry4 = tk.Entry(frameg, highlightthickness=1, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 150, y = 280)
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 250, y = 280)
        fxentry5 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry5.place(x = 400, y = 280)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 500, y = 280)
        fxentry6 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry6.place(x = 600, y = 280)
        
    elif  tip == 3:
        # texto del tituo
        tk.Label(frameg, text="3) Funciones Radicales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").pack(side=tk.TOP)#.grid(column=1, row=1)
        frameg.pack(side=tk.TOP, fill="both", expand=True)
        
        fx = tk.Label(frameg, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 10, y = 160)
        fxentry4 = tk.Entry(frameg, highlightthickness=1, width= 1, font= ("Arial", 25))
        fxentry4.place(x = 130, y = 150)
        fx = tk.Label(frameg, text = "√", font= ("Arial", 50), bg="light gray").place(x = 155, y = 160)
        linea = tk.Label(frameg, text = "___________________", font= ("Arial", 35), bg="light gray").place(x = 195, y = 108) 
        fxentry = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 205, y = 180)
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 295, y = 180)
        fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 425, y = 180)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 515, y = 180)
        fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 595, y = 180)
        
    elif  tip == 4:
        # texto del tituo
        tk.Label(frameg, text="4) Funciones Exponenciales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").pack(side=tk.TOP)#.grid(column=1, row=1
        frameg.pack(side=tk.TOP, fill="both", expand=True)
        
        fx = tk.Label(frameg, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 20, y = 180)
        fxentry = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 190)
        fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 250, y = 150)
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 340, y = 150)
        fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 470, y = 150)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), bg="light gray").place(x =560, y = 150)
        fxentry4 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 640, y = 150)
        
    elif  tip == 5:
        """Frame del area de trabajo con las funciones Logaritmicas"""
        # texto del tituo
        tk.Label(frameg, text="5) Funciones Logaritmicas", font= ("Arial", 40, "bold"), justify="center", bg="light gray").pack(side=tk.TOP)#.grid(column=1, row=1)
        frameg.pack(side=tk.TOP, fill="both", expand=True)
        
        fx = tk.Label(frameg, text = "f(x)= Log", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 10, y = 140)
        fxentry = tk.Entry(frameg, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry.place(x = 230, y = 170)
        fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry2.place(x = 300, y = 150)
        fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 370, y = 150)
        fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry3.place(x = 510, y = 150)
        fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 580, y = 150)
        fxentry4 = tk.Entry(frameg, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry4.place(x = 660, y = 150)

    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.pack()#.place(x = 130, y = 440)
    botonlineal = tk.Button(borderlineal, text = " Graficar ", width = 15, height= 1, font = ("Arial", 30, "bold"), cursor = "circle" )#, command = lambda: [veri(tip, fxentry, fxentry2, fxentry3, fxentry4, fxentry5, fxentry6)])
    botonlineal.pack()
   
def semilla(self):
    """Funcion de interfaz de frame para hallar la semilla de una funcion """

    frameg = tk.Frame(self.AreaTrabajo, bg="light grey")
    
    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Semilla de una Funcion", font= ("Arial", 40, "bold"), justify="center", bg="light grey").pack(side=tk.TOP)#.place(x=20,y=20)#.grid(column=1, row=1)
    frameg.pack(side=tk.TOP, fill="both", expand=True)
        
    tituloInicio = tk.Label(frameg, text = " Escriba la función para hallar la semilla ", font=('Arial',20,'bold'), pady = 10, bg="light grey")
    tituloInicio.place(x = 20, y = 30)
    fx = tk.Label(frameg, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 5, y = 90)
    fxentry = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry.place(x = 120, y = 100)
    fx = tk.Label(frameg, text = "x^3 +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 200, y = 90)
    fxentry2 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry2.place(x = 320, y = 100)
    fx = tk.Label(frameg, text = "x^2 +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 400, y = 90)
    fxentry3 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry3.place(x = 520, y = 100)
    fx = tk.Label(frameg, text = "x +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 600, y = 90)
    fxentry4 = tk.Entry(frameg, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry4.place(x = 670, y = 100)

    #tabla de valores en x
    l11 = tk.Entry(frameg, borderwidth=3, font=('Arial',20,'bold'))
    l11.insert(0, "   X ")
    l11.configure(state = 'disabled')
    l11.place(x = 20, y = 240, width=70, height = 70)
    l12 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l12.place(x = 90, y = 240, width=70, height = 70)
    l13 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l13.place(x = 160, y = 240, width=70, height = 70)
    l14 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l14.place(x = 230, y = 240, width=70, height = 70)
    l15 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l15.place(x = 300, y = 240, width=70, height = 70)
    l16 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l16.place(x = 370, y = 240, width=70, height = 70)
    l17 = tk.Entry(frameg, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l17.place(x = 440, y = 240, width=70, height = 70)

    #tabla valores en y
    l21 = tk.Entry(frameg, fg='red', borderwidth=3, font=('Arial',20,'bold'))
    l21.insert(0, "   Y ")
    l21.configure(state = 'disabled')
    l21.place(x = 20, y = 170, width=70, height = 70)
    l22 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 90, y = 170, width=70, height = 70)
    l23 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 160, y = 170, width=70, height = 70)
    l24 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 230, y = 170, width=70, height = 70)
    l25 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 300, y = 170, width=70, height = 70)
    l26 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 370, y = 170, width=70, height = 70)
    l27 = tk.Entry(frameg, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 440, y = 170, width=70, height = 70) 

    #marco y boton para graficar
    borderlineal = tk.LabelFrame(frameg, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 530, y = 200)    
    botonlineal = tk.Button(borderlineal, text = " Graficar ", width = 10, height= 1, font = ("Arial", 20, "bold"), cursor = "circle" )#, command = lambda: fsemilla(frmps, fxentry, fxentry2, fxentry3, fxentry4, l12, l13, l14, l15, l16 ,l17))
    botonlineal.pack()
