import tkinter as tk

ventana = tk.Tk()
ventana.title("Marcos Empaquetados")
ventana.geometry("400x400")
ventana.configure(bg="lightgray")

# Crear marcos y empaquetarlos
marco1 = tk.Frame(ventana, bg="red")
marco1.pack(pady=10)

boton1 = tk.Button(marco1, text="Botón1 corto ", bg="white")
boton2 = tk.Button(marco1, text="Botón2 al que se adapta el frame ", bg="white")

boton1.pack()
boton2.pack()

ventana.mainloop()