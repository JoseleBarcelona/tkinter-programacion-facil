import tkinter as tk

# Clase para crear etiquetas
class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold")
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen")
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow")
        self.etiqueta5 = tk.Label(root, text="Etiqueta 5", bg="lightpink")

        # Posicionamiento absoluto con place
        self.etiqueta1.place(relx=0, rely=0, width=160, height=50, anchor="nw") # relx y rely son coordenadas relativas al tamaño de la ventana (del 0 a 1) 
        self.etiqueta2.place(relx=1, rely=0, width=160, height=50, anchor="ne") 
        self.etiqueta3.place(relx=0, rely=1, width=160, height=50, anchor="sw") 
        self.etiqueta4.place(relx=1, rely=1, width=160, height=50, anchor="se") 
        self.etiqueta5.place(relx=0.5, rely=0.5, width=160, height=50, anchor="center")

# Clase principal de la aplicación
class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Etiquetas en Grid")
        self.root.geometry("400x200")

        self.etiqueta = Etiqueta(self.root)
        

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()

