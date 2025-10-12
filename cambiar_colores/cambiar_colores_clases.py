import tkinter as tk
import random

class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi primera ventana")
        self.root.geometry("400x300")  # Establecer tamaño inicial de la ventana
        self.root.config(bg="lightgray")  # Color de fondo inicial

        self.etiqueta_rgb = tk.Label(self.root, text="Color RGB:", font=("Arial", 12, "bold"))
        self.etiqueta_rgb.pack(pady=10)

        self.etiqueta_hex = tk.Label(self.root, text="Color Hexadecimal:", font=("Arial", 12, "bold"))
        self.etiqueta_hex.pack(pady=10)

        self.boton_rgb = tk.Button(self.root, text="Cambiar Color Fondo", command=self.cambiar_color_fondo_rgb)
        self.boton_rgb.pack(pady=10)

        self.boton_hex = tk.Button(self.root, text="Cambiar Color Fondo Hexadecimal", command=self.cambiar_color_fondo_hexadecimal)
        self.boton_hex.pack(pady=10)

    def cambiar_color_fondo_rgb(self):
        colores = ["red", "green", "blue", "yellow", "purple", "orange"]
        color_aleatorio = random.choice(colores)
        self.root.config(bg=color_aleatorio)
        self.etiqueta_rgb.config(text=f"Color RGB: {color_aleatorio}")

    def cambiar_color_fondo_hexadecimal(self):
        color_aleatorio = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.root.config(bg=color_aleatorio)
        self.etiqueta_hex.config(text=f"Color Hexadecimal: {color_aleatorio}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()