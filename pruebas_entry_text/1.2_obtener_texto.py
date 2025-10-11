import tkinter as tk

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400+100+100")

# Widget Text
texto = tk.Text(ventana, height=10, width=30)
texto.pack(pady=20)

# Función para obtener texto
def obtener_texto():
    contenido = texto.get("1.0", tk.END) 
    print(f"Contenido del Text:\n{contenido}")

    # tk.END es una constante que representa el final del texto
    # Desde el inicio (1.0 linea 1 caracter 0) hasta el final (tk.END)
    # contenido = texto.get("1.0", "end") también funciona

# Función para obtener la primera línea
def obtener_primera_linea():
    primera_linea = texto.get("1.0", "1.end") 
    print(f"Primera línea del Text:\n{primera_linea}")

    # Desde el inicio (1.0 linea 1 caracter 0) hasta el final de la línea 1 (1.end)

# Función para obtener el texto seleccionado
def obtener_seleccion():
    try:
        seleccion = texto.get(tk.SEL_FIRST, tk.SEL_LAST)
        print(f"Texto seleccionado:\n{seleccion}")
    except tk.TclError as e:
        print("No hay texto seleccionado, el error es:", e)

    # tk.SEL_FIRST y tk.SEL_LAST son constantes que representan el inicio y el final del texto seleccionado
    # Si no hay texto seleccionado, esto lanzará un error
    # seleccion = texto.get("sel.first", "sel.last") también funciona

# Botón para obtener texto
boton_obtener = tk.Button(ventana, text="Obtener todo el texto", padx=20, command=obtener_texto)
boton_obtener.pack(pady=5)

# Botón para obtener la primera línea
boton_primera_linea = tk.Button(ventana, text="Obtener primera línea", padx=20, command=obtener_primera_linea)
boton_primera_linea.pack(pady=5)

# Botón para obtener el texto seleccionado
boton_seleccion = tk.Button(ventana, text="Obtener texto seleccionado", padx=20, command=obtener_seleccion)
boton_seleccion.pack(pady=5)

ventana.mainloop()
