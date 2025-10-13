import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Uso de padx, pdy ipadx, ipady")
        self.root.geometry("400x300")

        self.label1 = tk.Label(root, text = "Etiqueta 1", bg="lightblue") # Si usamos padx y pady aquí, actuará como relleno interior
        self.label2 = tk.Label(root, text = "Etiqueta 2", bg="lightpink")
        self.label3 = tk.Label(root, text = "Etiqueta 3", bg="lightgreen")
        self.label4 = tk.Label(root, text = "Etiqueta 4", bg="lightyellow")

        self.label1.pack(pady = 20) # Esto es como un margin en CSS (Margen exterior)
        self.label2.pack(pady = 20)
        self.label3.pack(ipadx=70, ipady=10) # Esto es como un padding en CSS (Relleno interior)
        self.label4.pack(ipadx=70, ipady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()