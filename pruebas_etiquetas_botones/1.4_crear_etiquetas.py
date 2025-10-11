import tkinter as tk

class EtiquetaPersonalizada(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Arial", 16), fg="blue")

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación con Botones Personalizados")
        self.master.geometry("300x400")

        self.contador_clicks = 0  # contador de clics

        self.boton_creador = tk.Button(master, text="Crear etiquetas", command=self.crear_etiquetas)
        self.boton_creador.pack(pady=10)

    def crear_etiquetas(self):
        if self.contador_clicks < 2:
            for i in range(4):
                etiqueta = EtiquetaPersonalizada(self.master, text=f"Etiqueta {i+1}", bg="lightgray", relief="sunken", borderwidth=1)
                etiqueta.pack(pady=5)
            self.contador_clicks += 1
        else:
            self.boton_creador.config(state="disabled")  # desactiva el botón

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
