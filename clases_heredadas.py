import tkinter as tk
from tkinter import ttk

class VentanaBase(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Base")
        self.center_window(400, 300)
        self.icon()
        self.widgets()

        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def icon(self):
        icon = tk.PhotoImage(file="icono.png")
        self.iconphoto(True, icon)

    def widgets(self):
        label = ttk.Label(self, text="Hola, Mundo!")
        label.pack(pady=20)

        boton = ttk.Button(self, text="Cerrar", command=self.destroy)
        boton.pack(pady=10)

        ventana_hija = tk.Toplevel(self)
        ventana_hija.title("Ventana Hija")
        ventana_hija.geometry("200x150+50+50")

if __name__ == "__main__":
    VentanaBase()