from math import sqrt
from math import log
from re import L
from matplotlib import pyplot 
import numpy as np

#importacion de librerias para parte grafica 
import tkinter
import tkinter as tk

domin = 1
dom2 = 0
dom5 = 0
j=1
i=0
colorbg="dark gray"
    
def f(tip, x, fun, fun2, fun3, fun4, fun5, fun6):

    global domin
    global dom2
    global dom5
    global j 
    global i
    
    if tip == 1:        
        return(fun*x**3) + (fun2*x**2) + (fun3*x) + (fun4)

    if tip == 2:        
        x = int(x * (10**1)) / (10**1)
        
        try:
            r = ((fun*x**2) + (fun2*x) + (fun3)) / ((fun4*x**2) + (fun5*x) + (fun6))
            return r 
        
        except ZeroDivisionError:
            domin = 2        
            if j == 1 :
                dom2 = x
                j=2
                domin = 2

            elif j == 2:
                dom5 = x
                
                if dom2 == dom5 :
                    domin =2
                    
                else:
                    j = 3 
                    domin = 3
                    
            elif j == 3:
                dom5 = x
                domin=4
                i = i + 1
                
            if i > 200:
                dom5 = x
                domin = 5         
    
    if tip == 3:
        if fun4 == 2:
            x = int(x * (10**1)) / (10**1)
            
            try:
                r = sqrt((fun*x**2) + (fun2*x)  +(fun3))
                return r 
            
            except ValueError:
                domin = 2          
                if j == 1 :
                    dom2 = x
                    j=2
                    domin = 2

                elif j == 2:
                    dom5 = x
                    print("1",j)
                    j = 3 
                    print("2",j)
                    domin = 3
                elif j == 3:
                    dom5 = x
                    domin=4
                    i = i + 1
                if i > 200:
                    dom5 = x
                    domin = 5
                    
        if fun4 == 3:
            x = int(x * (10**1)) / (10**1)
            
            try:
                r = np.cbrt((fun*x**2) + (fun2*x) + (fun3)) 
                return r 
            
            except ValueError:
                domin = 2          
                if j == 1 :
                    dom2 = x
                    j=2
                    domin = 2

                elif j == 2:
                    dom5 = x
                    j = 3 
                    domin = 3
                elif j == 3:
                    dom5 = x
                    domin=4
                    i = i + 1
                if i > 200:
                    dom5 = x
                    domin = 5

    if tip == 4:
        x = int(x * (10**1)) / (10**1)
        
        try:
            r = (fun**((fun2*x**2) + (fun3*x) + (fun4)))
            return r 
        
        except ValueError:#OverflowError:
            #falta otro except
            domin = 2
            print(i)           
            if j == 1 :
                print("entro al 2")
                dom2 = x
                print("1",j)
                j=2
                print("2",j)
                domin = 2

            elif j == 2:
                print("entro al 3")
                dom5 = x
                print("1",j)
                j = 3 
                print("2",j)
                domin = 3
            elif j == 3:
                print("entro al 4")
                dom5 = x
                domin=4
                i = i + 1
            if i > 200:
                #error con los huecos pero si funciona con las raices y no con exponentes 
                print("entro al 5")
                dom5 = x
                domin = 5
            domin = 1
                
        except OverflowError:
            domin = 2
            print(i)           
            if j == 1 :
                print("entro al 2")
                dom2 = x
                print("1",j)
                j=2
                print("2",j)
                domin = 2

            elif j == 2:
                print("entro al 3")
                dom5 = x
                print("1",j)
                j = 3 
                print("2",j)
                domin = 3
            elif j == 3:
                print("entro al 4")
                dom5 = x
                domin=4
                i = i + 1
            if i > 200:
                #error con los huecos pero si funciona con las raices y no con exponentes 
                print("entro al 5")
                dom5 = x
                domin = 5
            domin = 1
    
    if tip == 5:
        x = int(x * (10**1))/(10**1)
        
        try:
            r = log(((fun2*x**2) + (fun3*x) + (fun4)), fun)
            return r 
        
        except ValueError:
            domin = 2          
            if j == 1 :
                dom2 = x
                j=2
                domin = 2

            elif j == 2:
                dom5 = x
                j = 3 
                domin = 3
            elif j == 3:
                dom5 = x
                domin=4
                i = i + 1
            if i > 200:
                dom5 = x
                domin = 5

def grafica(tip, fun, fun2, fun3, fun4, fun5, fun6):
    global domin
    global dom2
    global dom5
    global j
    global i
            
    #cuadricula de fondo
    pyplot.grid()
    
    # Valores del eje X que toma el gráfico.
    x = np.arange(-50, 50, 0.1)

    # Graficar ambas funciones. 
    pyplot.plot(x, [f(tip, i, fun, fun2, fun3, fun4, fun5, fun6) for i in x])
        
    if domin == 1:
        #plt.title(r"Grafico de $f(x)=\sqrt{x + 2}$")
        pyplot.title("Dominio : R (-oo,oo^+)")
        
    elif domin == 2:
        pyplot.title(f"Dominio : R (-oo,{dom2}) y ({dom2},oo^+)")

    elif domin == 3:
        pyplot.title(f"Dominio : R (-oo,{dom2}) y ({dom2}, {dom5})y ({dom5},oo^+)")
        
    elif domin == 4:
        pyplot.title(f"Dominio : R (-oo,{dom2}) y ({dom5},oo^+)")
    
    elif domin == 5:
        pyplot.title(f"Dominio : R ({dom5},oo^+)")
        
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)

    # Guardar gráfico como imágen PNG.
    pyplot.savefig("output.png")

    # Mostrarlo.
    pyplot.show()
    
#Desde aqui es solo semila 
a = 0
b = 0
a2 = 0
b2 = 0
a3 = 0
b3 = 0
cseml = 0
sem = 0
sem2 = 0
sem3 = 0

def biseccion(frmps, sem, sem2, sem3,fun1,fun2,fun3,fun4, a, b, a2, b2, a3, b3 ):    
    i=0
    salir = False
    salir2 = False
    salir3 = False
    sem12 = 0
    sem22 = 0
    sem32 = 0
    
    while(salir == False):
        print("a = ", a)
        print("b = ", b)
        print("semilla = ",sem)
        raiz = (fun1*sem**3) + (fun2*sem**2) + (fun3*sem) + (fun4)
        print(raiz)
        apri = (fun1*a**3) + (fun2*a**2) + (fun3*a) + (fun4)
        bpri = (fun1*b**3) + (fun2*b**2) + (fun3*b) + (fun4)
        print(apri," ", bpri)
        
        if(raiz >= 0 and ((apri <= 0 and bpri >= 0))):
            print("entro1")
            sem12 = (((sem) + (a))/2)
            a = a
            b = sem
            
        elif(raiz <= 0 and ((apri <= 0 and bpri >= 0))):
            print("entro 2")
            sem12 = (((sem) + (b))/2)
            a = sem
            b = b
        if(raiz >= 0 and ((apri >= 0 and bpri <= 0))):
            print("entro1")
            sem12 = (((sem) + (b))/2)
            a = sem
            b = b
            
        elif(raiz <= 0 and ( (apri >= 0 and bpri <= 0))):
            print("entro 2")
            sem12 = (((sem) + (a))/2)
            a = a
            b = sem
        print(sem12)
            
        if(sem == sem12):
            salir=True
            
        else:
            sem=sem12
                        
        i = i+1  
        print ("termino ",i)    
    x1 = tkinter.Label(frmps, text = " i = cantidad de iteraciones ", font=('Arial',13,'bold'), bg=colorbg).place(x = 490, y = 370)
    raiz = tkinter.Label(frmps, text = "Raiz 1  = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 420, y = 415)
    x1 = tkinter.Label(frmps, text = "x", font=('Arial',13,'bold'), bg=colorbg).place(x = 490, y = 415)
    x2 = tkinter.Label(frmps, text = i, font=('Arial',13,'bold'), bg=colorbg).place(x = 510, y = 415)
    x1 = tkinter.Label(frmps, text = " i = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 530, y = 415)
    traiz = tkinter.Label(frmps, text = sem12, font=('Arial',13,'bold'), bg=colorbg).place(x = 560, y = 415)
    print("termino la primera raiz \n")
    sem12 = 0
    apri = 0
    bpri = 0
    raiz=0
    i=0  
    
    while(salir2 == False):
        print("a = ", a2)
        print("b = ", b2)
        print("semilla = ",sem2)
        raiz2 = (fun1*sem2**3) + (fun2*sem2**2) + (fun3*sem2) + (fun4)
        print(raiz2)
        apri2 = (fun1*a2**3) + (fun2*a2**2) + (fun3*a2) + (fun4)
        bpri2 = (fun1*b2**3) + (fun2*b2**2) + (fun3*b2) + (fun4)
        print(apri2," ", bpri2)
        
        if(raiz2 >= 0 and ((apri2 <= 0 and bpri2 >= 0))):
            print("entro1")
            sem22 = (((sem2) + (a2))/2)
            a2 = a2
            b2 = sem2
            
        elif(raiz2 <= 0 and ((apri2 <= 0 and bpri2 >= 0))):
            print("entro 2")
            sem22 = (((sem2) + (b2))/2)
            a2 = sem2
            b2 = b2
        if(raiz2 >= 0 and ((apri2 >= 0 and bpri2 <= 0))):
            print("entro1")
            sem22 = (((sem2) + (b2))/2)
            a2 = sem2
            b2 = b2
            
        elif(raiz2 <= 0 and ((apri2 >= 0 and bpri2 <= 0))):
            print("entro 2")
            sem22 = (((sem2) + (a2))/2)
            a2 = a2
            b2 = sem2
        print(sem22)
            
        if(sem2 == sem22):
            salir2=True
            
        else:
            sem2=sem22
                        
        i = i+1  
        print ("termino ",i)    
              
    raiz = tkinter.Label(frmps, text = "Raiz 2 = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 420, y = 440)
    x1 = tkinter.Label(frmps, text = "x", font=('Arial',13,'bold'), bg=colorbg).place(x = 490, y = 440)
    x2 = tkinter.Label(frmps, text = i, font=('Arial',13,'bold'), bg=colorbg).place(x = 510, y = 440)
    x1 = tkinter.Label(frmps, text = " i = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 530, y = 440)
    traiz = tkinter.Label(frmps, text = sem22, font=('Arial',13,'bold'), bg=colorbg).place(x = 560, y = 440)
    print("termino la segunda raiz \n")
    sem22 = 0
    apri2 = 0
    bpri2 = 0
    raiz2=0
    i=0
    
    while(salir3 == False):
        print("a = ", a3)
        print("b = ", b3)
        print("semilla = ",sem3)
        raiz3 = (fun1*sem3**3) + (fun2*sem3**2) + (fun3*sem3) + (fun4)
        print(raiz3)
        apri3 = (fun1*a3**3) + (fun2*a3**2) + (fun3*a3) + (fun4)
        bpri3 = (fun1*b3**3) + (fun2*b3**2) + (fun3*b3) + (fun4)
        print(apri3," ", bpri3)
        
        if(raiz3 >= 0 and ((apri3 <= 0 and bpri3 >= 0))):
            print("entro1")
            sem32 = (((sem3) + (a3))/2)
            a3 = a3
            b3 = sem3
            
        elif(raiz3 <= 0 and ((apri3 <= 0 and bpri3 >= 0))):
            print("entro 2")
            sem32 = (((sem3) + (b3))/2)
            a3 = sem3
            b3 = b3
        if(raiz3 >= 0 and ((apri3 >= 0 and bpri3 <= 0))):
            print("entro1")
            sem32 = (((sem3) + (b3))/2)
            a3 = sem3
            b3 = b3
            
        elif(raiz3 <= 0 and ((apri3 >= 0 and bpri3 <= 0))):
            print("entro 2")
            sem32 = (((sem3) + (a3))/2)
            a3 = a3
            b3 = sem3
        print(sem32)
            
        if(sem3 == sem32):
            salir3=True
            
        else:
            sem3=sem32
                        
        i = i+1  
        print ("termino ",i)    
              
    raiz = tkinter.Label(frmps, text = "Raiz 3 = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 420, y = 465)
    x1 = tkinter.Label(frmps, text = "x", font=('Arial',13,'bold'), bg=colorbg).place(x = 490, y = 465)
    x2 = tkinter.Label(frmps, text = i, font=('Arial',13,'bold'), bg=colorbg).place(x = 510, y = 465)
    x1 = tkinter.Label(frmps, text = " i = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 530, y = 465)
    traiz = tkinter.Label(frmps, text = sem32, font=('Arial',13,'bold'), bg=colorbg).place(x = 560, y = 465)
    print("termino la tercera raiz \n")
    sem32 = 0
    apri3 = 0
    bpri3 = 0
    i=0
    raiz3=0
    
    msg = tkinter.Label(frmps, text = " Presición de 0.000000000000001 ", font=('Arial',13,'bold'), bg=colorbg).place(x = 470, y = 500)

def calcularsem(fun1, x, fun2, fun3, fun4, r1, r2, r3, r4, r5, r6):
    """" funcion para calcular todos los valores en x"""
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    est1 = True
    est2 = True
    est3 = True
    est4 = True
    est5 = True
    est6 = True

    #truncamos x
    x = int(x * (10**1))/(10**1)
    
    #operamos los valores de x en la funcion 
    r = (fun1*x**3) + (fun2*x**2) + (fun3*x) + (fun4)
    
    #truncamos los valores que se escojieron y e resultado ej 0.0
    r1 = int(r1 * (10**1))/(10**1)
    r2 = int(r2 * (10**1))/(10**1)
    r3 = int(r3 * (10**1))/(10**1)
    r4 = int(r4 * (10**1))/(10**1)
    r5 = int(r5 * (10**1))/(10**1)
    r6 = int(r6 * (10**1))/(10**1)
    r20 = int(r * (10**1))/(10**1)

    #guardamos las variables ne las x que seleccionamos
    if est1 == True:
        if(r1 == x):
            g1 = r20
            est1 = False
    if est2 == True:
        if(r2 == x):
            g2 = r20
            est2 = False
    if est3 == True:
        if(r3 == x):
            g3 = r20
            est3 = False
    if est4 == True:
        if(r4 == x):
            g4 = r20
            est4 = False
    if est5 == True:
        if(r5 == x):
            g5 = r20
            est5 = False
    if est6 == True:
        if(r6 == x):
            g6 = r20
            est6 = False

    return r

def graficasem(frmps, fun1,fun2,fun3,fun4, r1, r2, r3, r4, r5, r6):
    """funcion para graficar las funciones"""
    global a
    global b
    global a2
    global b2
    global a3
    global b3
    global cseml
    global sem
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global generalFrame
    
    #cuadricula de fondo
    pyplot.grid()
    
    # Valores del eje X que toma el gráfico.
    x = np.arange(-50, 50, 0.1)

    # Graficar ambas funciones. 
    pyplot.plot(x, [calcularsem(fun1, i, fun2,fun3,fun4, r1, r2, r3, r4, r5, r6) for i in x])
        
    # Establecer el color de los ejes.
    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")

    # Limitar los valores de los ejes.
    pyplot.xlim(-10, 10)
    pyplot.ylim(-10, 10)

    # Guardar gráfico como imágen PNG.
    #pyplot.savefig("output.png")
    #labes para indicar los puntos a b y la semilla 
    
    #en la interfaz ponemos los valores que nos dio y con las x seleccionadas
    l22 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold'))
    l22.configure(state = 'normal')
    l22.insert(0, g1)
    l22.configure(state = 'disabled')
    l22.place(x = 90, y = 220, width=70, height = 70)
    
    l23 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold'))
    l23.configure(state = 'normal')
    l23.insert(0, g2)
    l23.configure(state = 'disabled')
    l23.place(x = 160, y = 220, width=70, height = 70)
    
    l24 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold'))
    l24.configure(state = 'normal')
    l24.insert(0, g3)
    l24.configure(state = 'disabled')
    l24.place(x = 230, y = 220, width=70, height = 70)
    
    l25 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold'))
    l25.configure(state = 'normal')
    l25.insert(0, g4)
    l25.configure(state = 'disabled')
    l25.place(x = 300, y = 220, width=70, height = 70)
    
    l26 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold'))
    l26.configure(state = 'normal')
    l26.insert(0, g5)
    l26.configure(state = 'disabled')
    l26.place(x = 370, y = 220, width=70, height = 70)
    
    l27 = tkinter.Entry(frmps, state="readonly", borderwidth=3, fg='blue', font=('Arial',16,'bold')) 
    l27.configure(state = 'normal')
    l27.insert(0, g6)
    l27.configure(state = 'disabled')
    l27.place(x = 440, y = 220, width=70, height = 70)
    
    if (g1 < 0  and g2 >= 0) or (g1 > 0  and g2 <= 0):
        cseml = cseml + 1
        if cseml == 1:
            a = r1
            b = r2
        elif cseml == 2:
            a2 = r1
            b2 = r2
        elif cseml == 3:
            a3 = r1
            b3 = r2
        
    if (g2 < 0  and g3 >= 0) or (g2 > 0  and g3 <= 0):
        cseml = cseml + 1
        if cseml == 1:
            a = r2
            b = r3
        elif cseml == 2:
            a2 = r2
            b2 = r3
        elif cseml == 3:
            a3 = r2
            b3 = r3
        
    if (g3 < 0  and g4 >= 0) or (g3 > 0  and g4 <= 0):
        cseml = cseml + 1
        if cseml == 1:
            a = r3
            b = r4
        elif cseml == 2:
            a2 = r3
            b2 = r4
        elif cseml == 3:
            a3 = r3
            b3 = r4
        
    if (g4 < 0  and g5 >= 0) or (g4 > 0  and g5 <= 0):
        cseml = cseml + 1
        if cseml == 1:
            a = r4
            b = r5
        elif cseml == 2:
            a2 = r4
            b2 = r5
        elif cseml == 3:
            a3 = r4
            b3 = r5
        
    if g5 < 0  and g6 >= 0 or g5 > 0  and g6 <= 0:
        cseml = cseml + 1
        if cseml == 1:
            a = r5
            b = r6
        elif cseml == 2:
            a2 = r5
            b2 = r6
        elif cseml == 3:
            a3 = r1
            b3 = r2        
        
#if cseml == 1 or cseml == 2 or cseml == 3:
    ta1 = tkinter.Label(frmps, text = "a = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 10, y = 430)
    la1 = tkinter.Label(frmps, text = a, font=('Arial',13,'bold'), bg=colorbg).place(x = 40, y = 430)
    tb1 = tkinter.Label(frmps, text = "b = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 80, y = 430)
    lb1 = tkinter.Label(frmps, text = b,  font=('Arial',13,'bold'), bg=colorbg).place(x = 110, y = 430)
    
    sem = (a + b)/2
    sem11 = tkinter.Label(frmps, text = "Semilla 1 = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 10, y = 460)
    tsem1 = tkinter.Label(frmps, text = sem, font=('Arial',13,'bold'), bg=colorbg).place(x = 100, y = 460)
    
#if cseml == 2 or cseml == 3:
    ta2 = tkinter.Label(frmps, text = "a = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 140, y = 430)
    la2 = tkinter.Label(frmps, text = a2, font=('Arial',13,'bold'), bg=colorbg).place(x = 170, y = 430)
    tb2 = tkinter.Label(frmps, text = "b = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 200, y = 430)
    lb2 = tkinter.Label(frmps, text = b2,  font=('Arial',13,'bold'), bg=colorbg).place(x = 230, y = 430)
    
    sem2 = (a2 + b2)/2
    sem12 = tkinter.Label(frmps, text = "Semilla 2 = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 140, y = 460)
    tsem2 = tkinter.Label(frmps, text = sem2, font=('Arial',13,'bold'), bg=colorbg).place(x = 230, y = 460)
    
#if cseml == 3:
    ta3 = tkinter.Label(frmps, text = "a = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 270, y = 430)
    la3 = tkinter.Label(frmps, text = a3, font=('Arial',13,'bold'), bg=colorbg).place(x = 300, y = 430)
    tb3 = tkinter.Label(frmps, text = "b = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 340, y = 430)
    lb3 = tkinter.Label(frmps, text = b3,  font=('Arial',13,'bold'), bg=colorbg).place(x = 370, y = 430)
    
    sem3 = (a3 + b3)/2
    sem13 = tkinter.Label(frmps, text = "Semilla 3 = ", font=('Arial',13,'bold'), bg=colorbg).place(x = 270, y = 460)
    tsem3 = tkinter.Label(frmps, text = sem3, font=('Arial',13,'bold'), bg=colorbg).place(x = 360, y = 460)
    
    biseccion(frmps, sem, sem2, sem3,fun1,fun2,fun3,fun4, a, b, a2, b2, a3, b3)

    # Mostrarlo.
    pyplot.show()
    a = 0
    b = 0
    a2 = 0
    b2 = 0
    a3 = 0
    b3 = 0
    cseml = 0
