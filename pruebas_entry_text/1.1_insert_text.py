import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")

# Configuración de la ventana para que ocupe toda la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

ventana.configure(background="lightgray")

contador = 0

# Instanciación del widget Text
texto = tk.Text(ventana, height=10, width=20)
texto.pack(pady=20)

#Función para insertar texto en el widget Text
def insertar_texto():
    global contador
    contador += 1
    texto.insert(tk.END, f"Texto {contador} insertado.\n")

# Instanciación del botón para insertar texto
boton_insertar = tk.Button(ventana, text="Insertar Texto", command=insertar_texto).pack()

# Instanciación del botón para borrar texto
boton_borrar = tk.Button(ventana, text="Borrar Texto", command=lambda: texto.delete('1.0', tk.END)).pack(pady=10)

# Instanciación del botón para borrar la última línea
boton_borrado_parcial = tk.Button(ventana, text="Borrar Última Línea", command=lambda: texto.delete('end-2l', 'end-1l')).pack()

# Instanciación del botón para borrar las primeras 5 letras
boton_borrar_porciones = tk.Button(ventana, text="Borrar 5 Primeras Letras", command=lambda: texto.delete('1.0', '1.5')).pack(pady=10)

print("Ancho de la pantalla:", ancho_pantalla)
print("Alto de la pantalla:", alto_pantalla)
ventana.after(100, lambda: print("Ancho:", ventana.winfo_width(), "Alto:", ventana.winfo_height()))

ventana.mainloop()