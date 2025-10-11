import tkinter as tk

class Etiqueta(tk.Label):
    """
    Clase para crear widgets de etiquetas.
    """
    def __init__(self, ventana, texto):
        super().__init__(ventana, text=texto)

class Boton(tk.Button):
    """
    Clase para crear widgets de botones.
    """
    def __init__(self, ventana, texto, comando):
        super().__init__(ventana, text=texto, command=comando)

class VentanaSecundaria(tk.Toplevel):
    """
    Clase para la ventana secundaria.
    """
    def __init__(self, ventana):
        super().__init__(ventana)
        self.title("Ventana Secundaria")
        self.geometry("300x200+550+210") #definir tamaño y posición
        self.configure(bg="lightyellow")

        # Usar la clase Etiqueta para el contenido de la ventana secundaria
        etiqueta_secundaria = Etiqueta(self, "¡Esta es la ventana secundaria!")
        etiqueta_secundaria.pack(pady=20)
        
        # Usar la clase Boton para el botón de cerrar
        boton_cerrar = Boton(self, "Cerrar", self.destroy)
        boton_cerrar.pack()

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi primera ventana")
        self.ventana.geometry("400x350+60+60")
        self.ventana.configure(bg="lightgray")

        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta = Etiqueta(self.ventana, "¡Hola, mundo!")
        self.etiqueta.pack(pady=10)
        self.boton_abrir = Boton(self.ventana, "Abrir Ventana Secundaria", self.abrir_ventana_secundaria)
        self.boton_abrir.pack(pady=10)
        self.boton_salir = Boton(self.ventana, "Salir", self.ventana.destroy)
        self.boton_salir.pack(pady=10)
    
    def abrir_ventana_secundaria(self):
        self.ventana_secundaria = VentanaSecundaria(self.ventana)


if __name__ == "__main__":
    root = tk.Tk() # Crear la ventana principal
    app = Aplicacion(root) # Crear una instancia de la aplicación y le pasamos la ventana principal para que maneje esa ventana 
    root.mainloop() # Iniciar el bucle principal de la ventana