import tkinter as tk

class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue", width=20, height=2)
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold", width=20, height=2)
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen", width=20, height=2)
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow", width=20, height=2)

        self.etiqueta1.grid(row=0)
        self.etiqueta2.grid(row=1)
        self.etiqueta3.grid(row=2)
        self.etiqueta4.grid(row=3)


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("400x300")

        self.etiqueta = Etiqueta(self.root)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

