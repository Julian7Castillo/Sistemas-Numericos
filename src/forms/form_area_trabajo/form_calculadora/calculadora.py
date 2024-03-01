#importamos librerias
import tkinter as tk
from tkinter import font
from config import constants as cons

def CalculadoraPanel(self):
    texto = tk.Label(self.AreaTrabajo, text="Calculadora", font = ("Arial", 35, "bold"), bg="light grey")
    texto.pack(side=tk.TOP, fill="x", expand=True)
    
    place = tk.Frame(self.AreaTrabajo, bg="light grey")
    place.pack(side=tk.TOP, fill="both", expand=True)
    
    #configurtacion de interfaz
    #etiqueta para mostrar la operacion solicitada
    self.operation_label = tk.Label(place, text="",bg="light grey", font=('Arial', 16), fg=cons.COLOR_DE_TEXTO_DARK, justify='right')
    self.operation_label.grid(row=0, column=3, padx=10, pady=10)

    #pantalla de operacion
    self.entry = tk.Entry(place, width=12, font=('Arial', 40), bd=0, fg=cons.COLOR_DE_TEXTO_DARK, bg=cons.COLOR_CAJA_TEXTO_DARK, justify='right')
    self.entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
    
    #lista de botones
    buttons = [
        'C','%','<','/',
        '7','8','9','*',
        '4','5','6','-',
        '1','2','3','+',
        '0','.','=',
    ]

    row_val = 2 #ajusteado para dejar espacio para la etiqueta de operacion
    col_val = 0
    
    #configurar la tipografia "Roboto" para botones
    roboto_font = font.Font(family="Roboto", size=16)

    for button in buttons:

        #establecer el color de fondo de los botones especiales
        if button in ['=','*','/','-','+','C','<','%']:
            color_fondo = cons.COLOR_BOTONES_ESPECIALES_DARK

            #ajustar el tamaño de la fuente solo para esros botones
            button_font = font.Font(size=16, weight='bold')

        else:
            color_fondo = cons.COLOR_BOTONES_DARK
            button_font = roboto_font

        #ajuste para el boton de '=' abarqeu dos columnas en una fila 
        if button  == '=':
            tk.Button(place, text=button, width=11, height=2, 
                        command=lambda bar=button: on_button_click(self, bar), bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, overrelief='flat').grid(row=row_val, column=col_val, columnspan=2, pady=5)

            col_val += 1
        
        else:
            tk.Button(place, text=button, width=5, height=2,
                        command=lambda bar=button: on_button_click(self, bar), bg=color_fondo, fg=cons.COLOR_DE_TEXTO_DARK, relief=tk.FLAT, font=button_font, padx=5, pady=5, bd=0, borderwidth=0, highlightthickness=0, overrelief='flat').grid(row=row_val, column=col_val, pady=5)

            col_val += 1

        if col_val > 3:
            col_val = 0
            row_val += 1    

def on_button_click(self, value):
        """Funcion de eventos para botones"""

        if value == "=":
            try:
                #intentar guardar el valor del entry en una exprecion 
                expression = self.entry.get().replace('%', '/100')
                #funciuon de evaluacion
                result = eval(expression)

                #inserter el valor resultado en el entry 
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))

                #La operacion se pone en el label como resultado anterior
                operation = expression + " " + value
                self.operation_label.config(text=operation)

            except Exception as e:
                #en caso de error se mostrara un mensaje al usuario
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.operation_label.config(text="")

        elif value == 'C':
            #al usar el boton de c lo qeu ara es limpiar la entrada
            self.entry.delete(0, tk.END)
            self.operation_label.config(text="")

        elif value == '<':
            #almacenar el valor de la entrada
            current_text = self.entry.get()

            if current_text:
                #se creara un nuevo tedxto en el cual se elimino el ultimo caracter
                new_text = current_text[:-1]#elimina el ultimo caracter
                #Se elimina lo anterior en la entrada y se sustituye con el nuevo texto
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, new_text)

                #actualiza la etiquta de operacion
                self.operation_label.config(text=new_text + "")

        else:
            #en el caso de qeu se precione un valor qeu no se ael igual se almacenara el valor en el entry y se insertara ahora con el nuevo valor
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + value)

            if value == '=':
                self.operation_label.config(text="")