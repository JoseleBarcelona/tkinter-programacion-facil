import tkinter as tk
import random


class CrearMarco:
    def __init__(self, master, numero):
        colorAleatorioHex = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        self.marco = tk.Frame(master, width=200, height=100, bg=colorAleatorioHex)
        self.marco.pack()
        self.etiqueta = tk.Label(self.marco, text=f"Marco {numero}", bg=colorAleatorioHex)
        self.etiqueta.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

class Main:
    def __init__(self, master):
        self.master = master
        self.master.title("Crear Marcos Dinámicamente")
        self.master.geometry("400x700")
        self.boton = tk.Button(master, text="Crear Marco", command=self.crear_marco)
        self.boton.pack(pady=20)
        self.contador = 1

    def crear_marco(self):
        if self.contador <= 5:
            CrearMarco(self.master, self.contador)
            self.contador += 1
        else:
            self.boton.config(state="disabled")  # desactiva el botón

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Main(ventana)
    ventana.mainloop()