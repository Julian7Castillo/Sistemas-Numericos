#importamos las librerias necesarias 
from time import time
from src.forms.form_principal.inicializador import FormPrincipal

#contador de ejecucion del programa
tiempo_inicial=time()

app = FormPrincipal()
app.mainloop()

#finalizacion de la ejecucion
tiempo_final=time()

#calculo de tiempo de ejecucion
tiempo_ejecucion = tiempo_final - tiempo_inicial

#mostrar tiempo de ejececion 
print("El tiempo de ejecucion segundos fue: ",tiempo_ejecucion)#segundos
print("El tiempo de ejecucion milisegundos fue: ",tiempo_ejecucion * 1000)#milisegundos