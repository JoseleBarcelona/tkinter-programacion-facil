import tkinter as tk

class Etiqueta(tk.Label):
    """
    Clase para un widget de etiqueta.
    """
    def __init__(self, ventana, texto, fuente, color_fondo, color_texto, borde):
        super().__init__(ventana, text=texto, font=fuente, bg=color_fondo, fg=color_texto, cursor="hand2", bd=borde)


class Boton(tk.Button):
    """
    Clase para un widget de botón.
    """
    def __init__(self, ventana, texto, fuente, color_fondo, color_texto, borde, comando):
        super().__init__(ventana, text=texto, font=fuente, bg=color_fondo, fg=color_texto, cursor="hand2", bd=borde, command=comando, relief="ridge")


class VentanaSecundaria(tk.Toplevel):
    """
    Clase para la ventana secundaria.
    """
    def __init__(self, ventana):
        super().__init__(ventana)
        self.title("Ventana Secundaria")
        self.geometry("300x200+550+210")
        self.configure(bg="lightyellow")

        # Usar la clase Etiqueta para el contenido de la ventana secundaria
        etiqueta_secundaria = Etiqueta(self, "¡Esta es la ventana secundaria!", ("Arial", 12), "lightyellow", "black", 0)
        etiqueta_secundaria.pack(pady=20)
        
        # Usar la clase Boton para el botón de cerrar
        boton_cerrar = Boton(self, "Cerrar", ("Arial", 12), "lightcoral", "white", 5, self.destroy)
        boton_cerrar.pack()


class Aplicacion:
    """
    Clase principal de la aplicación, maneja la ventana raíz.
    """
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi primera ventana")
        self.ventana.geometry("400x350+60+60")
        self.ventana.configure(bg="lightgray")

        self.crear_widgets()

    def crear_widgets(self):
        """
        Crea y configura los widgets de la ventana principal usando las clases modulares.
        """
        # Creación de etiquetas usando la clase Etiqueta
        self.etiqueta1 = Etiqueta(self.ventana, "¡Hola, Mundo!", ("Times", 16, "italic", "underline"), "lightblue", "purple", 5)
        self.etiqueta2 = Etiqueta(self.ventana, "¡Hola, Mundo!", ("Impact", 16, "italic", "underline"), "lightblue", "purple", 5)
        self.etiqueta1.pack(pady=10)
        self.etiqueta2.pack(pady=10)

        # Creación de botones usando la clase Boton
        self.boton_abrir = Boton(self.ventana, "Abrir Ventana Secundaria", ("Arial", 14), "lightgreen", "black", 5, self.abrir_ventana_secundaria)
        self.boton_abrir.pack(pady=10)

        self.boton_salir = Boton(self.ventana, "Pulsa para salir", ("Arial", 14), "lightcoral", "black", 5, self.ventana.destroy)
        self.boton_salir.pack(pady=10)

    def abrir_ventana_secundaria(self):
        """
        Función para crear y mostrar la ventana secundaria.
        """
        self.ventana_secundaria = VentanaSecundaria(self.ventana)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


'''
Si quieres hacer el código aún más modular, como te sugerí en mi respuesta anterior, podemos refactorizarlo para que los widgets (etiquetas y botones) y la ventana secundaria estén en sus propias clases, tal y como me pediste en tu primera consulta. Esto hace que el código sea más limpio, reutilizable y fácil de entender.

Aquí tienes la nueva versión de tu archivo app.py con esta estructura modular.

Código de ejemplo con clases modulares

Cambios y mejoras

    Clases de Widgets (Etiqueta y Boton): He creado clases específicas para Etiqueta y Boton que heredan de tk.Label y tk.Button respectivamente. En sus constructores, definen los parámetros de estilo por defecto. Ahora, cuando creas un widget en la clase Aplicacion, es mucho más legible y los parámetros están bien definidos.

    Clase de Ventana Secundaria (VentanaSecundaria): La ventana secundaria ahora también es una clase, lo que encapsula su propia lógica y sus propios widgets. Esto evita que la lógica de la ventana secundaria se mezcle con la de la ventana principal.

Este nuevo enfoque es más escalable y te permitirá reutilizar las clases de Boton y Etiqueta en cualquier parte de tu aplicación de manera consistente.

'''