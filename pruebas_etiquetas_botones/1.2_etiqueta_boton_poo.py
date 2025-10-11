import tkinter as tk

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
        Crea y configura los widgets de la ventana principal.
        """
        self.etiqueta1 = tk.Label(self.ventana, text="¡Hola, Mundo!", font=("Times", 16, "italic", "underline"), bg="lightblue", fg="purple", cursor="hand2", bd=5)
        self.etiqueta2 = tk.Label(self.ventana, text="¡Hola, Mundo!", font=("Impact", 16, "italic", "underline"), bg="lightblue", fg="purple", cursor="hand2", bd=5)
        self.etiqueta1.pack(pady=10)
        self.etiqueta2.pack(pady=10)

        # Botón para abrir la ventana secundaria
        self.boton_abrir = tk.Button(self.ventana, text="Abrir Ventana Secundaria", font=("Arial", 14), bd=5, command=self.abrir_ventana_secundaria, cursor="hand2", bg="lightgreen", fg="black", activebackground="green", activeforeground="white", relief="ridge")
        self.boton_abrir.pack(pady=10)

        # Botón para salir
        self.boton_salir = tk.Button(self.ventana, text="Pulsa para salir", font=("Arial", 14), bd=5, command=self.ventana.destroy, cursor="hand2", bg="lightcoral", fg="black", activebackground="red", activeforeground="white")
        self.boton_salir.pack(pady=10)

    def abrir_ventana_secundaria(self):
        """
        Función para crear y mostrar la ventana secundaria.
        """
        ventana_secundaria = tk.Toplevel(self.ventana)
        ventana_secundaria.title("Ventana Secundaria")
        ventana_secundaria.geometry("300x200+550+210")
        ventana_secundaria.configure(bg="lightyellow")

        etiqueta_secundaria = tk.Label(ventana_secundaria, text="¡Esta es la ventana secundaria!", font=("Arial", 12))
        etiqueta_secundaria.pack(pady=20)
        
        boton_cerrar = tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy)
        boton_cerrar.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

'''

Veo que has escrito un código de Tkinter y quieres que lo revise. El código que me proporcionas es una buena base para una aplicación simple, pero presenta un problema importante: la ventana secundaria se crea y se muestra inmediatamente en cuanto se ejecuta el programa, lo cual no es el comportamiento ideal. Generalmente, una ventana secundaria debe aparecer solo cuando el usuario realiza una acción, como hacer clic en un botón.

He refactorizado tu código para solucionar este problema y hacerlo más modular, siguiendo los principios de la programación orientada a objetos que te comenté anteriormente.

Código de Ejemplo Mejorado

En este nuevo código, he envuelto la creación de la ventana secundaria en un método separado, abrir_ventana_secundaria, que se llama solo cuando se hace clic en el botón "Abrir Ventana Secundaria". Esto te da un control mucho mayor sobre el flujo de tu aplicación.

Aplicación Modular de Tkinter
8 sept, 23:05

¿Qué he cambiado?

    Eliminé la creación de la ventana secundaria del constructor __init__. Ahora, la ventana secundaria no se crea al iniciar la aplicación.

    Creé un método abrir_ventana_secundaria. Este método es el encargado de instanciar y configurar el objeto tk.Toplevel.

    Asocié este nuevo método al botón self.boton_abrir. El command del botón ahora es self.abrir_ventana_secundaria, lo que asegura que la ventana solo se abra cuando el usuario haga clic.

    Añadí un botón de "Cerrar" a la ventana secundaria. Esto permite al usuario cerrar la ventana emergente de forma independiente.

Este enfoque mejora significativamente la experiencia de usuario y la estructura de tu código.

'''