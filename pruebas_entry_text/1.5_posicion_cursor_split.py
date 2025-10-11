import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400+100+100")

# Widget Text
texto = tk.Text(ventana, height=10, width=30)
texto.pack(pady=20)


def posicion_cursor(event=None):
    # Obtener la posición del cursor
    posicion_cursor = texto.index(tk.INSERT)
    linea, caracter = posicion_cursor.split('.')
    print(f"Posición del cursor: {posicion_cursor}\n")
    # Obtener la línea y el carácter a través de la función split
    print(f"Línea: {linea}, Carácter: {caracter}\n")
    print(event)
    
# Vincular el evento de tecla para actualizar la posición del cursor
texto.bind("<KeyRelease>", posicion_cursor)

ventana.mainloop()