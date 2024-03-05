#importamos librerias
from tkinter import ttk
import tkinter as tk

#Importamos las las funciones del paquete graficas
from src.forms.form_area_trabajo.form_funciones.logic.graficas import grafica, graficasem

def red(frmprt, x, dec):
    print(x)
    print(dec)
    xv = float(x.get())
    decv = int(dec.__getattribute__)
    print(xv)
    print(decv)

    redo = round(x.get(), dec)

    #proceso de truncamiento
    trun = int(x * (10**dec))/(10**dec)

    #mensaje dee salida
    print(f" el numero truncado es : {trun}")
    print(f" el numero redondeado es : {redo}")
    print("hola mundo redondeo")

    #texto de resultados
    redondeo = tk.Label(frmprt, text="La Respuesta es:", font = ("Arial", 30, "bold"), bg="dark gray")
    redondeo.place(x=50,y=400)
    redondeo = tk.Label(frmprt, text=redo, font = ("Arial", 30, "bold"), bg="dark gray")
    redondeo.place(x=400,y=400)
    truncamiento = tk.Label(frmprt, text="La Respuesta es:", font = ("Arial", 30, "bold"), bg="dark gray")
    truncamiento.place(x=50,y=450)
    truncamiento = tk.Label(frmprt, text=trun, font = ("Arial", 30, "bold"), bg="dark gray")
    truncamiento.place(x=400,y=450)

def error():
    #Solicitud de datos
    v = float(input("Digite el número verdadero: "))
    decimal = int(input("Indique cuantos decimales desea tener cuando se realice la operación: "))

    #Proceso truncamiento
    trunk = int(v * (10**decimal))/(10**decimal)

    #Proceso redondeio
    redo = round(v, decimal)

    #error absoluto
    abstru = abs(v-trunk)
    absred = abs(v-redo)

    #error relativo
    reltru = (abs(v-trunk))/v
    relred = (abs(v-redo))/v

    #Mensajes de salida
    print(f"\nEl número truncado es: {trunk}")
    print(f"El número redondeado es: {redo}")

    #formacientifica
    fcienabtrun = "{:e}".format(abstru)
    fcientabred = "{:e}".format(absred)
    print(f"\nEl error absoluto truncado es: abstru {fcienabtrun}")
    print(f"El error absoluto redondeado es: absred  {fcientabred}")

    fcienretrun = "{:e}".format(reltru)
    fcientrered ="{:e}".format(relred)
    print(f"\nEl error relativo truncado es: {fcienretrun }")
    print(f"El error relativo redondeado es: {fcientrered}")

def fsemilla(frmps, fxentry, fxentry2, fxentry3, fxentry4, l12, l13, l14, l15, l16 ,l17):
    fun = 0
    fun2 = 0
    fun3 = 0
    fun4 = 0
    r1 = 0
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0

    fun = int(fxentry.get())
    if fxentry2 != 0:
        fun2 =  int(fxentry2.get())
        if fxentry3 != 0:
            fun3 = int(fxentry3.get())
            if fxentry4 != 0:
                fun4 = int(fxentry4.get())

    #las variables de los entry las convertimos a entros
    r1 = int(l12.get())
    r2 = int(l13.get())
    r3 = int(l14.get())
    r4 = int(l15.get())
    r5 = int(l16.get())
    r6 = int(l17.get()) 

    graficasem(frmps, fun, fun2, fun3, fun4, r1, r2, r3, r4, r5, r6)

def veri(tip, fxentry, fxentry2, fxentry3, fxentry4, fxentry5, fxentry6):
    fun = 0
    fun2 = 0
    fun3 = 0
    fun4 = 0
    fun5 = 0
    fun6 = 0
    
    fun = int(fxentry.get())
    if fxentry2 != 0:
        fun2 =  int(fxentry2.get())
        if fxentry3 != 0:
            fun3 = int(fxentry3.get())
            if fxentry4 != 0:
                fun4 = int(fxentry4.get())
                if fxentry5 != 0:
                    fun5 = int(fxentry5.get())
                    if fxentry6 != 0:
                        fun6 = int(fxentry6.get())
            
    grafica(tip, fun, fun2, fun3, fun4, fun5, fun6)
