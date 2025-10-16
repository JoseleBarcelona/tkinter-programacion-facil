import tkinter as tk

# Clase para crear etiquetas
class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold")
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen")
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow")

        # Posicionamiento absoluto con place
        self.etiqueta1.place(x=10, y=10, width=100, height=30) # x e y son las coordenadas absolutas en píxeles, width y height son el ancho y alto en píxeles
        self.etiqueta2.place(x=120, y=10, width=100, height=30)
        self.etiqueta3.place(x=10, y=50, width=100, height=30)
        self.etiqueta4.place(x=120, y=50, width=100, height=30)


# Clase principal de la aplicación
class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("400x400")

        self.etiqueta = Etiqueta(self.root)
        

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

