import tkinter as tk
import widgets as wd
from child_window import Child_Window

class Main_Window:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Principal")
        self.master.geometry("600x400+100+100")
        self.master.configure(bg="lightblue")

        # Uso de las clases personalizadas desde widgets.py
        etiqueta = wd.Etiqueta(self.master, text="Hola, esta es una etiqueta personalizada", bg="lightblue", font=("Arial", 16))
        etiqueta.pack(pady=20)

        boton_abrir = wd.Boton(self.master, text="Abrir Ventana Hija", command=self.abrir_ventana_hija)
        boton_abrir.pack(pady=10)

        boton_salir = wd.Boton(self.master, text="Salir", command=self.master.destroy)
        boton_salir.pack(pady=10)

    # Método para abrir la ventana hija desde child_window.py
    def abrir_ventana_hija(self):
        ventana_secundaria = Child_Window(self.master, bg="lightyellow", padx=10, pady=10, relief="raised", borderwidth=2)
        wd.Etiqueta(ventana_secundaria, text="Etiqueta en main.py", bg="lightyellow", font=("Arial", 12)).pack(pady=5)
        wd.Boton(ventana_secundaria, text="Cerrar en main.py", bg="lightcoral", command=ventana_secundaria.destroy).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = Main_Window(root)
    root.mainloop()