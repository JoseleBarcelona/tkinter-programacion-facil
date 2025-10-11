import tkinter as tk

class EstablecerAncla:
    def __init__(self, master):
        self.master = master
        self.master.title("Marcos con Ancla")
        self.master.geometry("400x400")
        self.master.configure(bg="lightgray")

        # Crear botones y empaquetarlo
        self.boton0 = tk.Button(self.master, text="Botón0")
        self.boton1 = tk.Button(self.master, text="Botón1")
        self.boton2 = tk.Button(self.master, text="Botón2")
        self.boton3 = tk.Button(self.master, text="Botón3")
        self.boton4 = tk.Button(self.master, text="Botón4")

        self.boton0.pack()
        self.boton1.pack()
        self.boton2.pack(after=self.boton0) # Empaquetar después del botón0
        self.boton3.pack()
        self.boton4.pack(before=self.boton3) # Empaquetar antes del botón3

        # Crear botones con ancla
        self.boton5 = tk.Button(self.master, text="Botón5").pack(anchor='sw')
        self.boton6 = tk.Button(self.master, text="Botón6").pack(anchor='center')
        self.boton7 = tk.Button(self.master, text="Botón7").pack(anchor='e')
        self.boton8 = tk.Button(self.master, text="Botón8").pack(anchor=tk.W)
        self.boton9 = tk.Button(self.master, text="Botón9").pack(anchor=tk.N)

    
if __name__ == "__main__":
    root = tk.Tk()
    app = EstablecerAncla(root)
    root.mainloop()