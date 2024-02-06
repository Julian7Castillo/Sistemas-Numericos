#Importamos de la libreriaa pil o pillow lo necesario para escalar las imagenes
from PIL import ImageTk, Image

#funcion para escalar imagenes
def leer_imagen(path, size):
    """funcion para escalar imagenes"""
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

#funcion para centrar objetos en la ventana o la pantalla
def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    """Funcion para centrar las ventanas """
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho/2) - (aplicacion_ancho/2))
    y = int((pantalla_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")