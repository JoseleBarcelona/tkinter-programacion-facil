import tkinter as tk

# Clase para crear etiquetas
class Etiqueta:
    def __init__(self, root): # root es la ventana principal
        self.etiqueta1 = tk.Label(root, text="Etiqueta 1", bg="lightblue")
        self.etiqueta2 = tk.Label(root, text="Etiqueta 2", bg="gold")
        self.etiqueta3 = tk.Label(root, text="Etiqueta 3", bg="lightgreen")
        self.etiqueta4 = tk.Label(root, text="Etiqueta 4", bg="lightyellow")

        # Posicionamiento absoluto con place
        self.etiqueta1.place(relx=0, rely=0, relwidth=0.25, relheight=0.25) # relx y rely son coordenadas relativas al tamaño de la ventana (del 0 a 1) 
        self.etiqueta2.place(relx=0.3, rely=0, relwidth=0.25, relheight=0.25) # relwidth y relheight son tamaños relativos al tamaño de la ventana (del 0 a 1)
        self.etiqueta3.place(relx=0, rely=0.3, relwidth=0.25, relheight=0.25) 
        self.etiqueta4.place(relx=0.3, rely=0.3, relwidth=0.55, relheight=0.55) 
        '''
        self.etiqueta4.place(relx=0.3, rely=0.3, relwidth=0.55, relheight=0.55) indica que la etiqueta 4 empieza en el 30% del ancho y el 30% del alto de la ventana
        y ocupa el 55% del ancho y el 55% del alto de la ventana.
        Esto hace que la etiqueta 4 ocupe el espacio restante en la esquina inferior derecha, dejando un espacio del 15% en el ancho y el alto.
        '''

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

