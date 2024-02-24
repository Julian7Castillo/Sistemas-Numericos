#importamos las librerias necesarias 
from tkinter import Scrollbar
import tkinter as tk
import src.util.utilidades as utl
from src.forms.form_barra_superior.formBarraSuperior import barraSuperior
from src.forms.form_menu.menus import menuop, menufun, menufiguras
from src.forms.form_area_trabajo.form_bienvenida_construccion.bienvenida import bienvenida, panel_Constuccion
from src.forms.form_area_trabajo.form_calculadora.calculadora import CalculadoraPanel
from src.forms.form_area_trabajo.form_Fracciones.fracciones import Fracciones
from src.forms.form_area_trabajo.form_redondeo.redondeo import redondeoTruncamiento
from src.forms.form_area_trabajo.form_error.error import errorabcoluto
from src.forms.form_area_trabajo.form_convercion.conversion import conversionNumerica
from src.forms.form_area_trabajo.form_figuras.figuras import figurasGeometricas
from src.forms.form_area_trabajo.form_funciones.funciones import general, semilla
from src.forms.form_area_trabajo.form_opciones.opciones import Opciones

class FormPrincipal(tk.Tk):
    
    def __init__(self):
        """Constructor de la ventana principal que contendra los elementos visuales"""
        super().__init__()
        
        #imagenes necesaria precargadas
        self.img_sitio_construccion = utl.leer_imagen("./src/img/sitio_construccion.png", (200, 200))
        self.img_Cuadrado = utl.leer_imagen("./src/img/cuadrado.png", (200, 200))
        self.img_Triangulo = utl.leer_imagen("./src/img/Triangulo.png", (200, 200))
        self.img_Rectangulo = utl.leer_imagen("./src/img/Rectangulo.png", (200, 200))
        self.img_Circulo = utl.leer_imagen("./src/img/Circulo.png", (200, 200))
        self.img_Trapecio = utl.leer_imagen("./src/img/Trapecio.png", (200, 200))
        
        #variable de tema
        self.vteme = "Claro"
        
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
        self.AreaTrabajo = tk.Frame(self, bg="light grey", width=780, padx=10, pady=20)
        self.AreaTrabajo.pack(side=tk.RIGHT, fill="both", expand=True)

    def toggle_panel(self):
        """Alterar la visiblidad del menu lateral si esta visible lo retira en la visibilidad y si no se encuentra visible, lo ajusta al lado derecho en el eje y para pocisionarlo """
        if self.barra_menu.winfo_ismapped():
            self.barra_menu.pack_forget()
        else:
            self.barra_menu.pack(side=tk.LEFT, fill="y")
    
    def cambienvenida(self):
        self.limpiarPanel(self.AreaTrabajo)
        bienvenida(self)
    
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
        panel_Constuccion(self)
    
    def fra(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        Fracciones(self)
    
    def figGeo(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.menu)
        menufiguras(self)
        
    def cuad(self):
        self.limpiarPanel(self.AreaTrabajo)
        figurasGeometricas(self,0)
    
    def triang(self):
        self.limpiarPanel(self.AreaTrabajo)
        figurasGeometricas(self,1)
    
    def rectan(self):
        self.limpiarPanel(self.AreaTrabajo)
        figurasGeometricas(self,2)
    
    def circ(self):
        self.limpiarPanel(self.AreaTrabajo)
        figurasGeometricas(self,3)
    
    def trapecio(self):
        self.limpiarPanel(self.AreaTrabajo)
        figurasGeometricas(self,4)
    
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
        general(self, 1)
        
    def funRacional(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        general(self, 2)
        
    def funRadical(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        general(self, 3)
        
    def funExponencial(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        general(self, 4)
        
    def funLogaritmica(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        general(self, 5)
        
    def sem(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        semilla(self)
        
    def connum(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        conversionNumerica(self)
        
    def opci(self):
        """Funcion para limpiar el panel y llamar la funcion asignada en el arera de trabajo desde el script de area de trabajo"""
        self.limpiarPanel(self.AreaTrabajo)
        Opciones(self)
        
# if __name__ == "__main__":
#     main()
