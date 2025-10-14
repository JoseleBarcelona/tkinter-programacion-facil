import tkinter as tk

class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold")
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen")
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow")
        self.etiqueta5 = tk.Label(root, text="Etiqueta 5", bg="lightpink")
        self.etiqueta6 = tk.Label(root, text="Etiqueta 6", bg="lightgray")

        self.etiqueta1.grid(row=0, column=0, sticky="nsew") # sticky="nsew" hace que la etiqueta se expanda en todas las direcciones (norte, sur, este, oeste)
        self.etiqueta2.grid(row=0, column=1, sticky="nsew")
        self.etiqueta3.grid(row=1, column=0, sticky="nsew")
        self.etiqueta4.grid(row=1, column=1, sticky="nsew")
        self.etiqueta5.grid(row=2, column=0, sticky="nsew")
        self.etiqueta6.grid(row=2, column=1, sticky="nsew")


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("400x400")

        self.etiqueta = Etiqueta(self.root)

        self.root.rowconfigure([0, 1, 2], weight=1) # Configura las filas para que se expandan (responsive), pasando una lista de índices de filas
        self.root.columnconfigure([0, 1], weight=1) # Configura las columnas para que se expandan (responsive), pasando una lista de índices de columnas
        

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

