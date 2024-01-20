#importamos las librerias necesarias 
from tkinter import Tk
from time import time

#contador de ejecucion del programa
tiempo_inicial=time()

#creacion de la funcion principal main
def main():
    """Funcion del inicio de la aplicacion con al bienvenida y el menu principal establecido """
    #creacion de ventana de nivel superior root (vetana principal)
    root = Tk()
    root.title("Sistemas Numericos")
    root.geometry("1060x550")
    #icon = PhotoImage(file="D://User//Documents//PROYECTOS//Proyectos_Python//Analisis_Numericos//Vista//Image//logo.png")
    #root.iconphoto(True, icon)
    root.resizable(width= 0, height=0)

    #loop de inicio ejecuta la ventana
    root.mainloop()
    
if __name__ == "__main__":
    main()

#finalizacion de la ejecucion
tiempo_final=time()

#calculo de tiempo de ejecucion
tiempo_ejecucion = tiempo_final - tiempo_inicial

#mostrar tiempo de ejececion 
print("El tiempo de ejecucion segundos fue: ",tiempo_ejecucion)#segundos
print("El tiempo de ejecucion milisegundos fue: ",tiempo_ejecucion * 1000)#milisegundos