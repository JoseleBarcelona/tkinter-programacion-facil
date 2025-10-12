import tkinter as tk

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("Rellenar Marcos")
        self.master.geometry("400x200")
        self.master.configure(bg = "lightgray")

        # Crear etiquetas y rellenar el espacio que lo contiene con el atributo fill
        self.etiqueta1 = tk.Label(self.master, bg = "red", text = "Marco 1")
        self.etiqueta2 = tk.Label(self.master, bg = "blue", text = "Marco 2")
        self.etiqueta3 = tk.Label(self.master, bg = "green", text = "Marco 3")
        self.etiqueta4 = tk.Label(self.master, bg = "gray", text = "Marco 4")

        # Empaquetamos las etiques con pack, expandemos las que queramos y rellenamos las que queramos también

        self.etiqueta1.pack(fill = "x", expand = True)
        self.etiqueta2.pack(fill = "both", expand = True)
        self.etiqueta3.pack(fill = "y", expand= True)
        self.etiqueta4.pack(fill = "x")

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()