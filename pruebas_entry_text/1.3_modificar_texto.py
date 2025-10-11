import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400+100+100")

# Widget Text
texto = tk.Text(ventana, height=10, width=30)
texto.pack(pady=20)

# Función para modificar texto
def modificar_texto():
    texto.delete("1.0", tk.END)  # Eliminar todo el texto
    texto.insert(tk.END, "Texto modificado")  # Insertar nuevo texto

def modificar_texto_seleccionado():
    try:
        texto.delete(tk.SEL_FIRST, tk.SEL_LAST)  # Eliminar texto seleccionado
        texto.insert(tk.INSERT, "Texto modificado")  # Insertar nuevo texto en la posición del cursor
    except tk.TclError as e:
        print("No hay texto seleccionado, el error es:", e)

    # Si no hay texto seleccionado, esto lanzará un error

def reemplazar_seleccion():
    try:
        texto_modificado = "Nuevo Texto"
        texto.replace(tk.SEL_FIRST, tk.SEL_LAST, texto_modificado)
    except tk.TclError as e:
        print("No hay texto seleccionado, el error es:", e)
    # Reemplaza el texto seleccionado con "Nuevo Texto"
    # Si no hay texto seleccionado, esto lanzará un error
    
# Botón para modificar texto
boton_modificar = tk.Button(ventana, text="Modificar texto", padx=20, command=modificar_texto)
boton_modificar.pack(pady=5)

# Botón para modificar texto seleccionado
boton_modificar_seleccionado = tk.Button(ventana, text="Modificar texto seleccionado", padx=20, command=modificar_texto_seleccionado)
boton_modificar_seleccionado.pack(pady=5)

# Botón para reemplazar texto seleccionado
boton_reemplazar_seleccion = tk.Button(ventana, text="Reemplazar texto seleccionado", padx=20, command=reemplazar_seleccion)
boton_reemplazar_seleccion.pack(pady=5)

# Iniciar el bucle principal
ventana.mainloop()