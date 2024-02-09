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
    pass
    
def redondeoTruncamiento(root):
    """Frame del area de trabajo de redondeo y truncamiento"""
    #creacion del frame para ubicar los widgets 
    frmprt = tk.Frame(root, height=625, width=760, bg='dark grey')
    frmprt.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(frmprt, text="Redondeo y Truncamiento", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    tk.Label(frmprt, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=30,y=110)#.grid(column=1, row=1)
    x = tk.Entry(frmprt, font= ("Arial", 20))
    x.place(x=350,y=120)#.grid(column=1, row=2)
    tk.Label(frmprt, text="Seleccione los decimales: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=30,y=180)
    #dec = ttk.Combobox(frmprt, text="Decimales", values=[1,2,3,4,5], height=5, width=5, font= ("Arial",20, "bold"))
    #dec.place(x=830,y=190)

    #botones de truncamienot y de redondeo 
    borderlineal = tk.LabelFrame(frmprt, bd = 6, bg = "DodgerBlue2", padx= 10, pady=10)
    borderlineal.place(x=130,y=250)#.grid(column=1, row=1)
    #botonlineal = Button(borderlineal, text = "Redendear y Truncar", bg="light grey",width = 20, height= 1, font = ("Arial", 30, "bold"), cursor = "circle", command =  lambda: [red(frmprt, x, dec)])
    #botonlineal.pack()

def errorabcoluto(root):
    """Frame del area de trabajo con la interfaz del error absoluto"""
    #creacion del frame para ubicar los widgets 
    frmpea = tk.Frame(root, height=625, width=760, bg='dark grey')
    frmpea.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(frmpea, text="Error Absoluto y Relativo", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    tk.Label(frmpea, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=50,y=150)#.grid(column=1, row=1)
    valor = tk.Entry(frmpea, font= ("Arial", 20))
    valor.place(x=350,y=160)#.grid(column=1, row=2)

def semilla(root):
    """Funcion de interfaz de frame para hallar la semilla de una funcion """
    #creacion del frame para ubicar los widgets 
    frmps = tk.Frame(root, height=625, width=760, bg='dark grey')
    frmps.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    tk.Label(frmps, text="Semilla de una Funcion", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    tituloInicio = tk.Label(frmps, text = " Escriba la función para hallar la semilla ", font=('Arial',20,'bold'), pady = 10, bg="dark gray")
    tituloInicio.place(x = 20, y = 80)
    fx = tk.Label(frmps, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 5, y = 140)
    fxentry = tk.Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry.place(x = 120, y = 150)
    fx = tk.Label(frmps, text = "x^3 +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 200, y = 140)
    fxentry2 = tk.Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry2.place(x = 320, y = 150)
    fx = tk.Label(frmps, text = "x^2 +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 400, y = 140)
    fxentry3 = tk.Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry3.place(x = 520, y = 150)
    fx = tk.Label(frmps, text = "x +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 600, y = 140)
    fxentry4 = tk.Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry4.place(x = 670, y = 150)

    #tabla de valores en x
    l11 = tk.Entry(frmps, borderwidth=3, font=('Arial',20,'bold'))
    l11.insert(0, "   X ")
    l11.configure(state = 'disabled')
    l11.place(x = 20, y = 290, width=70, height = 70)
    l12 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l12.place(x = 90, y = 290, width=70, height = 70)
    l13 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l13.place(x = 160, y = 290, width=70, height = 70)
    l14 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l14.place(x = 230, y = 290, width=70, height = 70)
    l15 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l15.place(x = 300, y = 290, width=70, height = 70)
    l16 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l16.place(x = 370, y = 290, width=70, height = 70)
    l17 = tk.Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l17.place(x = 440, y = 290, width=70, height = 70)

    #tabla valores en y
    l21 = tk.Entry(frmps, fg='red', borderwidth=3, font=('Arial',20,'bold'))
    l21.insert(0, "   Y ")
    l21.configure(state = 'disabled')
    l21.place(x = 20, y = 220, width=70, height = 70)
    l22 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 90, y = 220, width=70, height = 70)
    l23 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 160, y = 220, width=70, height = 70)
    l24 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 230, y = 220, width=70, height = 70)
    l25 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 300, y = 220, width=70, height = 70)
    l26 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 370, y = 220, width=70, height = 70)
    l27 = tk.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 440, y = 220, width=70, height = 70) 

    #marco y boton para graficar
    borderlineal = tk.LabelFrame(frmps, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 530, y = 250)    
    #botonlineal = Button(borderlineal, text = " Graficar ", width = 10, height= 1, font = ("Arial", 20, "bold"), cursor = "circle" , command = lambda: fsemilla(frmps, fxentry, fxentry2, fxentry3, fxentry4, l12, l13, l14, l15, l16 ,l17))
    #botonlineal.pack()
