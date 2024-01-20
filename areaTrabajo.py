#importamos librerias
from tkinter import Frame, Label,PhotoImage, Entry,LabelFrame, Button, ttk
#import tkinter as tk

#from Controlador.controladorBotones import red, error, fsemilla

def bienvenida(root):
    """Frame del menu principal en el area de trabajo con la bienvenida al usuario """
    #creacion del frame principal con la bienvenida al usuario
    frmpb = Frame(root, height=550, width=760, bg='dark grey')
    frmpb.place(x=300, y=0)

    #creacion de texto(label) 
    mensaje = Label(frmpb, text="Bienvenido \nPor favor eliga su opción ", font = ("Arial", 40, "bold"), justify="center", bg="dark gray")
    mensaje.place(x=20,y=10)

    #imagen
    #img = PhotoImage(file="D://User//Documents//PROYECTOS//Proyectos_Python//Analisis_Numericos//Vista//Image//logo.png")
    #l = Label(frmpb, image = img)
    #l.place(x=170,y=170,width=350, height=350)

def redondeoTruncamiento(root):
    """Frame del area de trabajo de redodneo y truncamiento"""
    #creacion del frame para ubicar los widgets 
    frmprt = Frame(root, height=625, width=760, bg='dark grey')
    frmprt.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    Label(frmprt, text="Redondeo y Truncamiento", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    Label(frmprt, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=30,y=110)#.grid(column=1, row=1)
    x = Entry(frmprt, font= ("Arial", 20))
    x.place(x=350,y=120)#.grid(column=1, row=2)
    Label(frmprt, text="Seleccione los decimales: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=30,y=180)
    dec = ttk.Combobox(text="Decimales", values=[1,2,3,4,5], height=5, width=5, font= ("Arial",20, "bold")).place(x=830,y=190)

    #botones de truncamienot y de redondeo 
    borderlineal = LabelFrame(frmprt, bd = 6, bg = "DodgerBlue2", padx= 10, pady=10)
    borderlineal.place(x=130,y=250)#.grid(column=1, row=1)
    #botonlineal = Button(borderlineal, text = "Redendear y Truncar", bg="light grey",width = 20, height= 1, font = ("Arial", 30, "bold"), cursor = "circle", command =  lambda: [red(frmprt, x, dec)])
    #botonlineal.pack()

def errorabcoluto(root):
    """Frame del area de trabajo con la interfaz del error absoluto"""
    #creacion del frame para ubicar los widgets 
    frmpea = Frame(root, height=625, width=760, bg='dark grey')
    frmpea.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    Label(frmpea, text="Error Absoluto y Relativo", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    Label(frmpea, text="Digite el valor: ", font= ("Arial", 30, "bold"), justify="center", bg="dark gray").place(x=50,y=150)#.grid(column=1, row=1)
    valor = Entry(frmpea, font= ("Arial", 20))
    valor.place(x=350,y=160)#.grid(column=1, row=2)

def semilla(root):
    """Funcion de interfaz de frame para hallar la semilla de una funcion """
    #creacion del frame para ubicar los widgets 
    frmps = Frame(root, height=625, width=760, bg='dark grey')
    frmps.place(x=300, y=0)

    # texto del tituo y de digitar el valor con un campo de texto para digitar valores
    Label(frmps, text="Semilla de una Funcion", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
    tituloInicio = Label(frmps, text = " Escriba la función para hallar la semilla ", font=('Arial',20,'bold'), pady = 10, bg="dark gray")
    tituloInicio.place(x = 20, y = 80)
    fx = Label(frmps, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 5, y = 140)
    fxentry = Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry.place(x = 120, y = 150)
    fx = Label(frmps, text = "x^3 +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 200, y = 140)
    fxentry2 = Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry2.place(x = 320, y = 150)
    fx = Label(frmps, text = "x^2 +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 400, y = 140)
    fxentry3 = Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry3.place(x = 520, y = 150)
    fx = Label(frmps, text = "x +", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 600, y = 140)
    fxentry4 = Entry(frmps, highlightthickness=2, width= 3, font= ("Arial", 30))
    fxentry4.place(x = 670, y = 150)

    #tabla de valores en x
    l11 = Entry(frmps, borderwidth=3, font=('Arial',20,'bold'))
    l11.insert(0, "   X ")
    l11.configure(state = 'disabled')
    l11.place(x = 20, y = 290, width=70, height = 70)
    l12 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l12.place(x = 90, y = 290, width=70, height = 70)
    l13 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l13.place(x = 160, y = 290, width=70, height = 70)
    l14 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l14.place(x = 230, y = 290, width=70, height = 70)
    l15 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l15.place(x = 300, y = 290, width=70, height = 70)
    l16 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l16.place(x = 370, y = 290, width=70, height = 70)
    l17 = Entry(frmps, fg='black', borderwidth=3, font=('Arial',16,'bold'))
    l17.place(x = 440, y = 290, width=70, height = 70)

    #tabla valores en y
    l21 = Entry(frmps, fg='red', borderwidth=3, font=('Arial',20,'bold'))
    l21.insert(0, "   Y ")
    l21.configure(state = 'disabled')
    l21.place(x = 20, y = 220, width=70, height = 70)
    l22 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 90, y = 220, width=70, height = 70)
    l23 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 160, y = 220, width=70, height = 70)
    l24 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 230, y = 220, width=70, height = 70)
    l25 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 300, y = 220, width=70, height = 70)
    l26 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 370, y = 220, width=70, height = 70)
    l27 = Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')).place(x = 440, y = 220, width=70, height = 70) 

    #marco y boton para graficar
    borderlineal = LabelFrame(frmps, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 530, y = 250)    
    #botonlineal = Button(borderlineal, text = " Graficar ", width = 10, height= 1, font = ("Arial", 20, "bold"), cursor = "circle" , command = lambda: fsemilla(frmps, fxentry, fxentry2, fxentry3, fxentry4, l12, l13, l14, l15, l16 ,l17))
    #botonlineal.pack()
