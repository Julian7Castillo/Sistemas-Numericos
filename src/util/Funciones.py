#importamos librerias
from tkinter import *
import tkinter as tk

#from Controlador.controladorBotones import veri

def general(tip, root):
    """Funcion se seleccion de tipo de funcion a mostrar por pantalla en el area de tabajdo"""
    #creacion del frame para ubicar los widgets 
    frmpf = tk.Frame(root, height=625, width=760, bg='dark grey')
    frmpf.place(x=300, y=0)

    #variables de loso campos d las funciones    
    fxentry2 = 0
    fxentry3 = 0 
    fxentry4 = 0 
    fxentry5 = 0 
    fxentry6 = 0
        
    if tip == 1:
        # texto del tituo
        tk.Label(frmpf, text="1) Funciones Polinomicas", font= ("Arial", 35, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
        fx = tk.Label(frmpf, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 5, y = 170)
        fxentry = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry.place(x = 120, y = 180)
        fx = tk.Label(frmpf, text = "x^3 +", font= ("Arial", 35), pady = 30, bg="dark gray").place(x = 200, y = 150)
        fxentry2 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry2.place(x = 320, y = 180)
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), pady = 30, bg="dark gray").place(x = 400, y = 150)
        fxentry3 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry3.place(x = 520, y = 180)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), pady = 30, bg="dark gray").place(x = 600, y = 150)
        fxentry4 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 30))
        fxentry4.place(x = 670, y = 180)
        
    elif tip == 2:
       # texto del tituo
        tk.Label(frmpf, text="2) Funciones Racionales", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
        #objetos y pociciones de la formula 
        fx = tk.Label(frmpf, text = "f(x) = ", pady = 10, font= ("Arial", 35), bg="dark gray").place(x = 20, y = 240)
        fxentry = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 160) 
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), bg="dark gray").place(x = 250, y = 160)
        fxentry2 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 400, y = 160)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), bg="dark gray").place(x = 500, y = 160)
        fxentry3 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 600, y = 160)
        linea = tk.Label(frmpf, text = "_____________________", font= ("Arial", 35), bg="dark gray").place(x = 160, y = 230) 
        fxentry4 = Entry(frmpf, highlightthickness=1, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 150, y = 330)
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), bg="dark gray").place(x = 250, y = 330)
        fxentry5 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry5.place(x = 400, y = 330)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), bg="dark gray").place(x = 500, y = 330)
        fxentry6 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry6.place(x = 600, y = 330)
        
    elif  tip == 3:
        # texto del tituo
        tk.Label(frmpf, text="3) Funciones Radicales", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)
        fx = tk.Label(frmpf, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 10, y = 160)
        fxentry4 = Entry(frmpf, highlightthickness=1, width= 1, font= ("Arial", 25))
        fxentry4.place(x = 130, y = 150)
        fx = tk.Label(frmpf, text = "√", font= ("Arial", 50), bg="dark gray").place(x = 155, y = 160)
        linea = tk.Label(frmpf, text = "___________________", font= ("Arial", 35), bg="dark gray").place(x = 195, y = 108) 
        fxentry = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 205, y = 180)
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), bg="dark gray").place(x = 295, y = 180)
        fxentry2 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 425, y = 180)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), bg="dark gray").place(x = 515, y = 180)
        fxentry3 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 595, y = 180)
        
    elif  tip == 4:
        # texto del tituo
        tk.Label(frmpf, text="4) Funciones Exponenciales", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=10,y=20)#.grid(column=1, row=1
        fx = tk.Label(frmpf, text = "f(x) = ", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 20, y = 180)
        fxentry = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry.place(x = 150, y = 190)
        fxentry2 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry2.place(x = 250, y = 150)
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), bg="dark gray").place(x = 340, y = 150)
        fxentry3 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry3.place(x = 470, y = 150)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), bg="dark gray").place(x =560, y = 150)
        fxentry4 = Entry(frmpf, highlightthickness=2, width= 3, font= ("Arial", 35))
        fxentry4.place(x = 640, y = 150)
        
    elif  tip == 5:
        """Frame del area de trabajo con las funciones Logaritmicas"""
        # texto del tituo
        tk.Label(frmpf, text="5) Funciones Logaritmicas", font= ("Arial", 40, "bold"), justify="center", bg="dark gray").place(x=20,y=20)#.grid(column=1, row=1)

        fx = tk.Label(frmpf, text = "f(x)= Log", font= ("Arial", 35), pady = 10, bg="dark gray").place(x = 10, y = 140)
        fxentry = Entry(frmpf, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry.place(x = 230, y = 170)
        fxentry2 = Entry(frmpf, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry2.place(x = 300, y = 150)
        fx = tk.Label(frmpf, text = "x^2 +", font= ("Arial", 35), bg="dark gray").place(x = 370, y = 150)
        fxentry3 = Entry(frmpf, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry3.place(x = 510, y = 150)
        fx = tk.Label(frmpf, text = "x +", font= ("Arial", 35), bg="dark gray").place(x = 580, y = 150)
        fxentry4 = Entry(frmpf, highlightthickness=2, width= 2, font= ("Arial", 35))
        fxentry4.place(x = 660, y = 150)

    borderlineal = LabelFrame(frmpf, bd = 6, bg = "DodgerBlue2")
    borderlineal.place(x = 150, y = 440)
    #botonlineal = tk.Button(borderlineal, text = " Graficar ", width = 15, height= 1, font = ("Arial", 30, "bold"), cursor = "circle" , command = lambda: [veri(tip, fxentry, fxentry2, fxentry3, fxentry4, fxentry5, fxentry6)])
    #botonlineal.pack()