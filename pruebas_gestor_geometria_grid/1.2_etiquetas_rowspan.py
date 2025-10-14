import tkinter as tk

class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue", width=20, height=2) # Creamos las etiquetas con un tamaño fijo
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold", width=20, height=2)
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen", width=20, height=2)
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow", width=20, height=2)
        self.etiqueta5 = tk.Label(root, text="Etiqueta 5", bg="lightcoral", width=20, height=2)
        self.etiqueta6 = tk.Label(root, text="Etiqueta 6", bg="lightpink", width=20, height=2)
        self.etiqueta7 = tk.Label(root, text="Etiqueta 7", bg="lightgray", width=20, height=2)
        self.etiqueta8 = tk.Label(root, text="Etiqueta 8", bg="cyan", width=20, height=2)

        self.etiqueta1.grid(row=0, column=0)
        self.etiqueta2.grid(row=0, column=1, rowspan=3, sticky="ns") # rowspan se expande 3 filas y con sticky='ns' le decimos que expanda de norte a sur
        self.etiqueta3.grid(row=0, column=2)
        self.etiqueta4.grid(row=1, column=0)
        self.etiqueta5.grid(row=1, column=2)
        self.etiqueta6.grid(row=2, column=0)
        self.etiqueta7.grid(row=2, column=2)
        self.etiqueta8.grid(row=3, column=0, columnspan=3, sticky="ew") # colspan se expande 3 columnas de este a oeste


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("800x200")

        self.etiqueta = Etiqueta(self.root) # Pasamos la ventana principal al constructor de la clase Etiqueta

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

