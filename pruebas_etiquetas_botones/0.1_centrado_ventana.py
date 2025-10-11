import tkinter as tk

class VentanaCentrada:
    def __init__(self, master):
        self.master = master
        self.master.title("Ventana Centrada")
        
        # Obtener las dimensiones de la pantalla
        ancho_pantalla = self.master.winfo_screenwidth()
        alto_pantalla = self.master.winfo_screenheight()
        
        # Definir las dimensiones de la ventana
        ancho_ventana = 400
        alto_ventana = 300
        
        # Calcular la posición para centrar la ventana
        x_centrado = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_centrado = (alto_pantalla // 2) - (alto_ventana // 2)
        
        # Configurar el tamaño y la posición de la ventana
        self.master.geometry(f"{ancho_ventana}x{alto_ventana}+{x_centrado}+{y_centrado}")


if __name__ == "__main__":
    # Crear la ventana principal
    ventana = tk.Tk()    
    app = VentanaCentrada(ventana)
    ventana.mainloop()