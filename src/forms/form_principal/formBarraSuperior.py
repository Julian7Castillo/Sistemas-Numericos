import tkinter as tk

def barraSuperior(self):
    #boton de menu lateral
        buttonMenuLateral = tk.Button(self.barra_superior, text="\uf012", font = ("Arial", 15, "bold"), command=self.toggle_panel, bd=0, bg="#2A3138", fg="white")#\uf012 \uf013 \uf014
        buttonMenuLateral.pack(side=tk.LEFT)
        
        titulo = tk.Label(self.barra_superior, text="Sistemas numericos                     ", fg="white",bg="#2A3138", font = ("Arial", 35, "bold"))
        titulo.pack(side=tk.RIGHT)
        