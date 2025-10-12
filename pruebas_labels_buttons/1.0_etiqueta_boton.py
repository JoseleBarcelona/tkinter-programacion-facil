import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("400x350+60+60") #definir tamaño y posición
ventana.configure(bg="lightgray")

# Crear y configurar las etiquetas
etiqueta = tk.Label(ventana, text="¡Hola, Mundo!", font=("Times", 16, "italic", "underline"), bg="lightblue", fg="purple", cursor="hand2", bd=5)
etiqueta2 = tk.Label(ventana, text="¡Hola, Mundo!", font=("Impact", 16, "italic", "underline"), bg="lightblue", fg="purple", cursor="hand2", bd=5)
etiqueta.pack(pady=20)
etiqueta2.pack(pady=20)

# Crear y configurar los botones
boton1 = tk.Button(ventana, text="Haz clic aquí", font=("Arial", 14), bg="lightgreen", fg="black", cursor="hand2", bd=5, activebackground="green", activeforeground="white", relief="ridge")
boton2 = tk.Button(ventana, text="Pulsa para salir", font=("Arial", 14), bd=5, command=ventana.destroy, cursor="hand2", bg="lightcoral", fg="black", activebackground="red", activeforeground="white")
boton1.pack(pady=20)
boton2.pack(pady=20)

# Crear una ventana secundaria
ventana_secundaria = tk.Toplevel(ventana)
ventana_secundaria.title("Ventana Secundaria")
ventana_secundaria.geometry("300x200+550+210") #definir tamaño y posición
ventana_secundaria.configure(bg="lightyellow")


# Iniciar el bucle principal de la ventana
ventana.mainloop()