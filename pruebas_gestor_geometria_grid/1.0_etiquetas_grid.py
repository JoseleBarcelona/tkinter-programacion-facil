import tkinter as tk

class Etiqueta:
    def __init__(self, root):
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="lightpink")
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen")
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow")

        self.etiqueta1.grid(row=0, column=0) # Definimos la posición en la cuadrícula, fila y columna de cada etiqueta
        self.etiqueta2.grid(row=0, column=1)
        self.etiqueta3.grid(row=1, column=0)
        self.etiqueta4.grid(row=1, column=1)


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("400x200")

        self.etiqueta = Etiqueta(self.root) # Pasamos la ventana principal al constructor de Etiqueta

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

