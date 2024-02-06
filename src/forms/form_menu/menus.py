#importamos librerias
from tkinter import *
import tkinter as tk

#importamos las demas funiones de los otros archvos
#from areaTrabajo import *
#from Funciones import *

def menuop(root):
    """Funcion de la interfaz del area de menu principal de los sistemas numericos"""
    #creacion del frame para el menu
    fmenu = tk.Frame(root, height=625, width=300, bg='grey', padx= 10, pady=10 )
    fmenu.place(x=0,y=0)#.pack(fill="x")

    #Creacion de los botones del menu
    borderlineal = LabelFrame(fmenu, bd = 6, bg = "grey", padx= 10, pady=17)
    borderlineal.pack()#.grid(column=1, row=1)
    botonlineal = tk.Button(borderlineal, text = "1) Redendeo \n y truncamiento", bg="light grey",width = 14, height= 2, font = ("Arial", 20, "bold"), cursor = "circle")#, command =  lambda:[redondeoTruncamiento(root)])
    botonlineal.pack()

    borderlineal = LabelFrame(fmenu, bd = 6, bg = "grey", padx= 10, pady=17)
    borderlineal.pack()#.grid(column=1, row=2)
    botonlineal = tk.Button(borderlineal, text = "2) Error Absoluto\n y Relativo", bg="light grey", width = 14, height= 2, font = ("Arial", 20, "bold"), cursor = "circle")#, command =  lambda:[errorabcoluto(root)] )
    botonlineal.pack()

    borderlineal = LabelFrame(fmenu, bd = 6, bg = "grey", padx= 10, pady=16)
    borderlineal.pack()#.grid(column=1, row=3)
    botonlineal = tk.Button(borderlineal, text = "3) Funciones", bg="light grey", width = 14, height= 2, font = ("Arial", 20, "bold"), cursor = "circle", command = lambda:[menufun(root),fmenu.destroy()])#(bo = False)])
    botonlineal.pack()

    borderlineal = LabelFrame(fmenu, bd = 6, bg = "grey", padx= 10, pady=16)
    borderlineal.pack()#.grid(column=1, row=4)
    botonlineal = tk.Button(borderlineal, text = "4) Semilla ", bg="light grey", width = 14, height= 2, font = ("Arial", 20, "bold"), cursor = "circle")#, command =  lambda:[semilla(root)] )
    botonlineal.pack()

def menufun(root):
    """frame de l sub menu secundario en el area de menu de opciones de solo los tipos de funciones"""
    #CReacion del frame
    fmenufun = tk.Frame(root, height=625, width=300, bg='grey', padx= 10, pady=10 )
    fmenufun.place(x=0,y=0)#.pack(fill="x")

    #creacion de los botones
    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=8)
    borderlineal.grid(column=1, row=1)
    botonlineal = tk.Button(borderlineal, text = "1) Funciones \nPolinomicas", bg="light grey", width = 20, height= 2, font = ("Arial", 15, "bold"), cursor = "circle")#, command =  lambda:[general(1,root)] )
    botonlineal.pack()

    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=8)
    borderlineal.grid(column=1, row=2)
    botonlineal = tk.Button(borderlineal, text = "2) Funciones \nRacionales", bg="light grey", width = 20, height= 2, font = ("Arial", 15, "bold"), cursor = "circle")#, command =  lambda:[general(2,root)])
    botonlineal.pack()

    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=8)
    borderlineal.grid(column=1, row=3)
    botonlineal = tk.Button(borderlineal, text = "3) Funciones \nRadicales", bg="light grey", width = 20, height= 2, font = ("Arial", 15, "bold"), cursor = "circle")#, command =  lambda:[general(3,root)] )
    botonlineal.pack()

    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=8)
    borderlineal.grid(column=1, row=4)
    botonlineal = tk.Button(borderlineal, text = "4) Funciones\n Exponenciales", bg="light grey", width = 20, height= 2, font = ("Arial", 15, "bold"), cursor = "circle")#, command =  lambda:[general(4,root)])
    botonlineal.pack()

    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=8)
    borderlineal.grid(column=1, row=5)
    botonlineal = tk.Button(borderlineal, text = "5) Funciones\n Logaritmicas", bg="light grey", width = 20, height= 2, font = ("Arial", 15, "bold"), cursor = "circle")#, command =  lambda:[general(5,root)] )
    botonlineal.pack()

    borderlineal = LabelFrame(fmenufun, bd = 6, bg = "grey", padx= 10, pady=6)
    borderlineal.grid(column=1, row=6)
    botonlineal = tk.Button(borderlineal, text = "6) Volver", bg="light grey", width = 20, height= 1, font = ("Arial", 15, "bold"), cursor = "circle", command =  lambda:[menuop(root), fmenufun.destroy()])#bo = True, return bo])
    botonlineal.pack()
