import tkinter as tk
import widgets as wd

class Child_Window(tk.Toplevel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.title("Ventana Hija")
        self.geometry("400x300+350+350")

        etiqueta_hija = wd.Etiqueta(self, text="Etiqueta en child_window.py", font=("Arial", 14), bg="lightyellow")
        etiqueta_hija.pack(pady=20)
        boton_cerrar = wd.Boton(self, text="Imprimir en child_window.py", bg="lightcoral", command=lambda: print("Botón en child_window.py presionado"))
        boton_cerrar.pack(pady=10)
