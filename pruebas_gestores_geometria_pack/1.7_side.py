import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Uso de padx, pdy ipadx, ipady")
        self.root.geometry("400x200")

        self.label1 = tk.Label(root, text = "Arriba", bg="lightblue") 
        self.label2 = tk.Label(root, text = "Derecha", bg="lightpink")
        self.label3 = tk.Label(root, text = "Izquierda", bg="lightgreen")
        self.label4 = tk.Label(root, text = "Abajo", bg="lightyellow")

        self.label1.pack(side = "top") # side indica la posición de la etiqueta en el contenedor
        self.label2.pack(side = "right")
        self.label3.pack(side = "left") 
        self.label4.pack(side = "bottom")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()