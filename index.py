#importamos librerias
from tkinter import *
import tkinter as tk

#importamos funciones del menu
from menus import *
from areaTabajo import *
from eje import *

def fInicio():
    """Funcion del inicio de la aplicacion con al bienvenida y el menu principal establecido """
    #creacion de ventana de nivel superior root (vetana principal)
    root = Tk()
    root.title("Sistemas Numericos")
    root.geometry("1060x550")
    icon = PhotoImage(file="D://User//Documents//PROYECTOS//Proyectos_Python//Analisis_Numericos//Vista//Image//logo.png")
    root.iconphoto(True, icon)
    root.resizable(width= 0, height=0)

    #creacion del marco (frame) en la ventana root con un tañaño de 10
    menuop(root)
    Inicio(root)

    #loop de inicio ejecuta la ventana
    root.mainloop()
