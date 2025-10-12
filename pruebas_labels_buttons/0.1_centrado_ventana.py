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
        x_centrado = round((ancho_pantalla / 2) - (ancho_ventana / 2))
        y_centrado = round((alto_pantalla / 2) - (alto_ventana / 2))
        
        # Configurar el tamaño y la posición de la ventana
        self.master.geometry(f"{ancho_ventana}x{alto_ventana}+{x_centrado}+{y_centrado}")

        print(f"Ancho pantalla: {ancho_pantalla}, Alto pantalla: {alto_pantalla}")
        print(f"Ancho ventana: {ancho_ventana}, Alto ventana: {alto_ventana}")
        print(f"Posición X centrado: {x_centrado}, Posición Y centrado: {y_centrado}")
        

if __name__ == "__main__":
    # Crear el objeto para crear la ventana principal
    ventana = tk.Tk()    
    app = VentanaCentrada(ventana)
    ventana.mainloop()