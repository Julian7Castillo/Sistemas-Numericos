#importamos librerias
import tkinter as tk

#from Controlador.controladorBotones import red, error, fsemilla

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

def bienvenida(self):
    texto = tk.Label(self.AreaTrabajo, text="Bienvenido", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)

def CalculadoraPanel(self):
    texto = tk.Label(self.AreaTrabajo, text="Calculadora", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)

def Fracciones(self):
    texto = tk.Label(self.AreaTrabajo, text="Fracciones", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)
    
    #etiquetas de titulos de fracciones 
    tk.Label(self.AreaTrabajo, text="Fraccio 1:").place(x=48, y=8)
    tk.Label(self.AreaTrabajo, text="Fraccio 2:").place(x=198, y=8)
    
    #FRACCION 1
    #frame para la fraccion
    ffrac1 = tk.Frame(self.AreaTrabajo, width=100, height = 60)
    ffrac1.place(x=20, y=35)
    
    #frame para la entrada del entero
    fx1 = tk.Frame(ffrac1, width=42, height=27)
    fx1.grid(row=0, column=0, rowspan=2) 
    
    #label y entrada de texto 
    tk.Label(fx1, text="Ent").pack(side="left")
    self.txt1E = tk.Entry(fx1, width=4)
    self.txt1E.pack(side="right")
    
    #dos entradas de texto y un label indicando que son dfe la fraccionfuera del tercer frame 
    tk.Label(ffrac1, text="Num").grid(row=0, column=2)
    tk.Label(ffrac1, text="den").grid(row=1, column=2)
    
    self.txt1N = tk.Entry (ffrac1, width=4)
    self.txt1D = tk.Entry (ffrac1, width=4)
    self.txt1N.grid(row=0, column=1)
    self.txt1D.grid(row=1, column=1)
    
    #FRACCION 2
    #frame para la fraccion
    ffrac2 = tk.Frame(self.AreaTrabajo, width=100, height = 60)
    ffrac2.place(x=180, y=35)
    
    #frame para la entrada del entero
    fx2 = tk.Frame(ffrac2, width=42, height=27)
    fx2.grid(row=0, column=0, rowspan=2) 
    
    #label y entrada de texto 
    tk.Label(fx2, text="Ent").pack(side="left")
    self.txt2E = tk.Entry(fx2, width=4)
    self.txt2E.pack(side="right")
    
    #dos entradas de texto y un label indicando que son dfe la fraccionfuera del tercer frame 
    tk.Label(ffrac2, text="Num").grid(row=0, column=2)
    tk.Label(ffrac2, text="den").grid(row=1, column=2)
    
    self.txt2N = tk.Entry (ffrac2, width=4)
    self.txt2D = tk.Entry (ffrac2, width=4)
    self.txt2N.grid(row=0, column=1)
    self.txt2D.grid(row=1, column=1)
    
    #Textos aparte de las fracciones para indicar las operaciones y el resultado
    tk.Label(self.AreaTrabajo, text="Operacion:").place(x=30, y=150)
    tk.Label(self.AreaTrabajo, text="Resultado: ").place(x=30, y=90)
    
    #combobox
    self.opciones = ["Suma","Resta","Multiplicación","División", "Son Iguales"]
    self.cmbOpciones = tk.Combobox(self, width="10", value=self.opciones, state="readonly")
    self.cmbOpciones.place(x=100, y="150")
    self.cmbOpciones.current(0)

def figurasGeometricas(self):
    texto = tk.Label(self.AreaTrabajo, text="Figuras geometricas", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)

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

def errorabcoluto(self):
    """Frame del area de trabajo con la interfaz del error absoluto"""

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Error Absoluto y Relativo", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)
    tk.Label(self.AreaTrabajo, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="light gray").place(x=50,y=150)#.grid(column=1, row=1)
    valor = tk.Entry(self.AreaTrabajo, font= ("Arial", 20))
    valor.place(x=350,y=160)#.grid(column=1, row=2)

def semilla(self):
    """Funcion de interfaz de frame para hallar la semilla de una funcion """

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(self.AreaTrabajo, text="Semilla de una Funcion", font= ("Arial", 40, "bold"), justify="center", bg="light grey").place(x=20,y=20)#.grid(column=1, row=1)
    tituloInicio = tk.Label(self.AreaTrabajo, text = " Escriba la función para hallar la semilla ", font=('Arial',20,'bold'), pady = 10, bg="light grey")
    tituloInicio.place(x = 20, y = 80)
    fx = tk.Label(self.AreaTrabajo, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 5, y = 140)
    fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry.place(x = 120, y = 150)
    fx = tk.Label(self.AreaTrabajo, text = "x^3 +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 200, y = 140)
    fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry2.place(x = 320, y = 150)
    fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 400, y = 140)
    fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry3.place(x = 520, y = 150)
    fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 600, y = 140)
    fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry4.place(x = 670, y = 150)

    #tabla de valores en x
    l11 = tk.Entry(self.AreaTrabajo, borderwidth=3, font=('Arial',20,'bold'))
    l11.insert(0, "   X ")
    l11.configure(state = 'disabled')
    l11.place(x = 20, y = 290, width=70, height = 70)
    l12 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l12.place(x = 90, y = 290, width=70, height = 70)
    l13 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l13.place(x = 160, y = 290, width=70, height = 70)
    l14 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l14.place(x = 230, y = 290, width=70, height = 70)
    l15 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l15.place(x = 300, y = 290, width=70, height = 70)
    l16 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l16.place(x = 370, y = 290, width=70, height = 70)
    l17 = tk.Entry(self.AreaTrabajo, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l17.place(x = 440, y = 290, width=70, height = 70)

    #tabla valores en y
    l21 = tk.Entry(self.AreaTrabajo, fg='red', borderwidth=3, font=('Arial',20,'bold'))
    l21.insert(0, "   Y ")
    l21.configure(state = 'disabled')
    l21.place(x = 20, y = 220, width=70, height = 70)
    l22 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 90, y = 220, width=70, height = 70)
    l23 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 160, y = 220, width=70, height = 70)
    l24 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 230, y = 220, width=70, height = 70)
    l25 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 300, y = 220, width=70, height = 70)
    l26 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 370, y = 220, width=70, height = 70)
    l27 = tk.Entry(self.AreaTrabajo, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 440, y = 220, width=70, height = 70) 

    #marco y boton para graficar
    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 530, y = 250)    
    #botonlineal = Button(borderlineal, text = " Graficar ", width = 10, height= 1, font = ("Arial", 20, "bold"), cursor = "circle" , command = lambda: fsemilla(frmps, fxentry, fxentry2, fxentry3, fxentry4, l12, l13, l14, l15, l16 ,l17))
    #botonlineal.pack()

def general(self, tip):
    """Funcion se seleccion de tipo de funcion a mostrar por pantalla en el area de tabajdo"""

    #variables de loso campos d las funciones    
    fxentry2 = 0
    fxentry3 = 0 
    fxentry4 = 0 
    fxentry5 = 0 
    fxentry6 = 0
        
    if tip == 1:
        # texto del tituo
        tk.Label(self.AreaTrabajo, text="1) Funciones Polinomicas", font= ("Arial", 35, "bold"), justify="center", bg="light grey").place(x=20,y=20)#.grid(column=1, row=1)
        fx = tk.Label(self.AreaTrabajo, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light grey").place(x = 5, y = 170)
        fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry.place(x = 120, y = 180)
        fx = tk.Label(self.AreaTrabajo, text = "x^3 +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 200, y = 150)
        fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry2.place(x = 320, y = 180)
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 400, y = 150)
        fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry3.place(x = 520, y = 180)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), pady = 30, bg="light grey").place(x = 600, y = 150)
        fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry4.place(x = 670, y = 180)
        
    elif tip == 2:
       # texto del tituo
        tk.Label(self.AreaTrabajo, text="2) Funciones Racionales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)
        #objetos y pociciones de la formula 
        fx = tk.Label(self.AreaTrabajo, text = "f(x) = ", pady = 10, font= ("Arial", 35), bg="light gray").place(x = 20, y = 240)
        fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 160) 
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 250, y = 160)
        fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 400, y = 160)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 500, y = 160)
        fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 600, y = 160)
        linea = tk.Label(self.AreaTrabajo, text = "_____________________", font= ("Arial", 35), bg="light gray").place(x = 160, y = 230) 
        fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=1, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 150, y = 330)
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 250, y = 330)
        fxentry5 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry5.place(x = 400, y = 330)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 500, y = 330)
        fxentry6 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry6.place(x = 600, y = 330)
        
    elif  tip == 3:
        # texto del tituo
        tk.Label(self.AreaTrabajo, text="3) Funciones Radicales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)
        fx = tk.Label(self.AreaTrabajo, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 10, y = 160)
        fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=1, width= 1, font= ("Arial", 25))
        fxentry4.place(x = 130, y = 150)
        fx = tk.Label(self.AreaTrabajo, text = "√", font= ("Arial", 50), bg="light gray").place(x = 155, y = 160)
        linea = tk.Label(self.AreaTrabajo, text = "___________________", font= ("Arial", 35), bg="light gray").place(x = 195, y = 108) 
        fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 205, y = 180)
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 295, y = 180)
        fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 425, y = 180)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 515, y = 180)
        fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 595, y = 180)
        
    elif  tip == 4:
        # texto del tituo
        tk.Label(self.AreaTrabajo, text="4) Funciones Exponenciales", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=10,y=20)#.grid(column=1, row=1
        fx = tk.Label(self.AreaTrabajo, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 20, y = 180)
        fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 190)
        fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 250, y = 150)
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 340, y = 150)
        fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 470, y = 150)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), bg="light gray").place(x =560, y = 150)
        fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 640, y = 150)
        
    elif  tip == 5:
        """Frame del area de trabajo con las funciones Logaritmicas"""
        # texto del tituo
        tk.Label(self.AreaTrabajo, text="5) Funciones Logaritmicas", font= ("Arial", 40, "bold"), justify="center", bg="light gray").place(x=20,y=20)#.grid(column=1, row=1)

        fx = tk.Label(self.AreaTrabajo, text = "f(x)= Log", font= ("Arial", 35), pady = 10, bg="light gray").place(x = 10, y = 140)
        fxentry = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry.place(x = 230, y = 170)
        fxentry2 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry2.place(x = 300, y = 150)
        fx = tk.Label(self.AreaTrabajo, text = "x^2 +", font= ("Arial", 35), bg="light gray").place(x = 370, y = 150)
        fxentry3 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry3.place(x = 510, y = 150)
        fx = tk.Label(self.AreaTrabajo, text = "x +", font= ("Arial", 35), bg="light gray").place(x = 580, y = 150)
        fxentry4 = tk.Entry(self.AreaTrabajo, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry4.place(x = 660, y = 150)

    borderlineal = tk.LabelFrame(self.AreaTrabajo, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 150, y = 440)
    botonlineal = tk.Button(borderlineal, text = " Graficar ", width = 15, height= 1, font = ("Arial", 30, "bold"), cursor = "circle" )#, command = lambda: [veri(tip, fxentry, fxentry2, fxentry3, fxentry4, fxentry5, fxentry6)])
    botonlineal.pack()
    
def conversionNumerica(self):
    texto = tk.Label(self.AreaTrabajo, text="Conversion numerica", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)

def Opciones(self):
    texto = tk.Label(self.AreaTrabajo, text="Opciones de Configuración ", font = ("Arial", 35, "bold"))
    texto.pack(side=tk.TOP, fill="both", expand=True)