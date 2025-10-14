import tkinter as tk

class Etiqueta:
    def __init__(self, root):
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue", width=20, height=2)
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold", width=20, height=2)
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen", width=20, height=2)
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow", width=20, height=2)
        self.etiqueta5 = tk.Label(root, text="Etiqueta 5", bg="lightcoral", width=20, height=2)
        self.etiqueta6 = tk.Label(root, text="Etiqueta 6", bg="lightpink", width=20, height=2)

        self.etiqueta1.grid(row=0, column=0)
        self.etiqueta2.grid(row=0, column=1, columnspan=2) # colspan se expande 2 columnas
        self.etiqueta3.grid(row=0, column=3)
        self.etiqueta4.grid(row=1, column=0)
        self.etiqueta5.grid(row=1, column=1)
        self.etiqueta6.grid(row=1, column=2)


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("800x200")

        self.etiqueta = Etiqueta(self.root)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

