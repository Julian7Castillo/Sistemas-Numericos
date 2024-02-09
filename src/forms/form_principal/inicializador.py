#importamos las librerias necesarias 
from tkinter import Scrollbar
import tkinter as tk
import src.util.utilidades as utl
from src.forms.form_barra_superior.formBarraSuperior import barraSuperior
from src.forms.form_menu.menus import menuop, menufun
from src.forms.form_area_trabajo.areaTrabajo import *

class FormPrincipal(tk.Tk):
    
    def __init__(self):
        """Constructor de la ventana principal que contendra los elementos visuales"""
        super().__init__()
        
        #imagenes necesaria precargadas
        self.img_sitio_construccion = utl.leer_imagen("./Sistemas-Numericos/src/img/sitio_construccion.png", (400, 400))
        
        #funciones necesaria para la visualización de todo
        self.configuracion()
        self.paneles()
        barraSuperior(self)
        menuop(self)
        bienvenida(self)
    
    def configuracion(self):
        """Configuración de la ventana """
        self.title("Sistemas Numericos")
        self.geometry("1024x600")
        w,h = 1024, 600
        utl.centrar_ventana(self, w, h)
        
    def paneles(self):
        """Creación de los paneles que dividiran la interfaz """
        #crear paneles: barra superior, menu lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg="#2A3138", height=50)
        self.barra_superior.pack(side=tk.TOP, fill="both")
        
        #Creacion de panel del menu
        self.barra_menu = tk.Frame(self, bg="grey")
        self.barra_menu.pack(side=tk.LEFT, fill="both", expand=False)
        
        #Creacion de canvas menu
        self.canvmenu = tk.Canvas(self.barra_menu, bg="grey", width=235)
        self.canvmenu.pack(side="left", fill="both", expand = 1)
        
        #Declaracion de la barra de scroll del menu
        self.scrollmenu = Scrollbar(self.barra_menu, orient="vertical", command=self.canvmenu.yview)
        self.scrollmenu.pack(side="right", fill="y")
        
        #configuracion de canvas del menu
        self.canvmenu.configure(yscrollcommand=self.scrollmenu.set)
        self.canvmenu.bind('<Configure>', lambda e: self.canvmenu.configure(scrollregion = self.canvmenu.bbox("all")))
        
        #crear otro frame en el canvas del menu
        self.menu = tk.Frame(self.canvmenu)
        
        #Agregar el nuevo frame al canvas del menu
        self.canvmenu.create_window((0,0), window = self.menu, anchor="nw")
        
        #CReacion del panel del area de trabajo
        self.AreaTrabajo = tk.Frame(self, bg="light grey")
        self.AreaTrabajo.pack(side=tk.RIGHT, fill="both", expand=True)
        
        #codigo ocmentado del scrop para el area de trabajo 
        #Creacion de canvas trabajo
        #self.canvtrab = tk.Canvas(self.AreaTrabajo, bg="grey")
        #self.canvtrab.place(relx=0.001, rely=0.001, relwidth=0.99, relheight=0.999)
        #self.canvtrab.pack(side="left", fill="both", expand = 1)
        
        #Declaracion de la barra de scrolldel area de trabajo
        #self.scrolltrab = Scrollbar(self.AreaTrabajo, orient="vertical", command=self.canvtrab.yview)
        #self.scrolltrab.place(relx=0.98, rely=0.001, relwidth=0.02, relheight=0.999)
        #self.scrolltrab.pack(side="right", fill="y")
        
        #configuracion de canvas del area de trabajo
        #self.canvtrab.configure(yscrollcommand=self.scrolltrab.set)
        #self.canvtrab.bind('<Configure>', lambda e: self.canvtrab.configure(scrollregion = self.canvtrab.bbox("all")))
        
        #crear otro frame en el canvas del area de trabajo
        #self.trab = tk.Frame(self.canvtrab)
        
        #Agregar el nuevo frame al canvas del area de trabajo
        #self.canvtrab.create_window((0,0), window = self.trab, anchor="nw")

    def toggle_panel(self):
        """Alterar la visiblidad del menu lateral si esta visible lo retira en la visibilidad y si no se encuentra visible, lo ajusta al lado derecho en el eje y para pocisionarlo """
        if self.barra_menu.winfo_ismapped():
            self.barra_menu.pack_forget()
        else:
            self.barra_menu.pack(side=tk.LEFT, fill="y")
    
    def config_boton_menu(self, borde, boton, text, font_awesome, ancho_menu, alto_menu, comando):
        """Configuracion de los bordes y los botones del menu lateral"""
        borde.config(bd = 6, bg = "#2A3138", padx=10, pady=17)#grey
        borde.pack(side=tk.TOP)
    
        boton.config(text=f"{text}", ancho="w", font=font_awesome, bd=0, bg="#32404F", fg="white", width=ancho_menu, height=alto_menu, cursor = "circle", command = comando) #light grey
        boton.pack(side=tk.TOP)
        
    def limpiarPanel(self, panel):
        """Funcion para Destrio todos los hijos de panel gracias al winfo _children que se le indique limpiando el panel que baya encontrando por eso se encientra en un bucle parea que se pueda hubicar otro panel diferente """
        for widget in panel.winfo_children():
            widget.destroy()

    def cal(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        CalculadoraPanel(self)
    
    def fra(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
    
    def figGeo(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
    
    def red(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        redondeoTruncamiento(self)
        
    def errorab(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        errorabcoluto(self)
    
    def cambiarMenu(self):
        """Cambiar el menu principal de opciones por el menu de funciones"""
        self.limpiarPanel(self.menu)
        menufun(self)
        
    def volvermenup(self):
        """Cambiar el menu de funciones por el menu principal de opciones"""
        self.limpiarPanel(self.menu)
        menuop(self)
        
    def funPolinomica(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def funRacional(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def funRadical(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def funExponencial(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def funLogaritmica(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def sem(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        semilla(self)
        
    def connum(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def opci(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
    def infor(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        panel_Constuccion(self)
        
# if __name__ == "__main__":
#     main()
