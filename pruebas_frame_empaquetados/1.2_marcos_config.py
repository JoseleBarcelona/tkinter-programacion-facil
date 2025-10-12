import tkinter as tk

ventana = tk.Tk()
ventana.title("Marcos configurados con config()")
ventana.geometry("400x400")

# Crear marcos
marco1 = tk.Frame(ventana)
marco2 = tk.Frame(ventana)
marco3 = tk.Frame(ventana)

# Configurar los atributos de los marcos usando config()
marco1.config(bg="red", width=200, height=100)
marco2.config(bg="blue", width=200, height=100)
marco3.config(bg="green", width=200, height=100)

# Empaquetar los marcos
marco1.pack(pady=10)
marco2.pack(pady=10)
marco3.pack(pady=10)

ventana.mainloop()