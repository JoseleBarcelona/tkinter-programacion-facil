import tkinter as tk

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("Expandir Marcos")
        self.master.geometry("400x400")
        self.master.configure(bg="lightgray")

        '''
        expand=True para que el espacio que contiene al botón se expanda y ocupe el espacio 
        restante de la ventana,repartiéndoselo con el espacio que contiene a los demás botones.
        
        '''
        # Crear botones y expander el espacio que lo contiene con el atributo expand
        self.boton1 = tk.Button(self.master, bg="red", text="Marco 1")
        self.boton1.pack(expand=True) 
        self.boton2 = tk.Button(self.master, bg="blue", text="Marco 2")
        self.boton2.pack(expand=True)
        self.boton3 = tk.Button(self.master, bg="green", text="Marco 3")
        self.boton3.pack(expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()