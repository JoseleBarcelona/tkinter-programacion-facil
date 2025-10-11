import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400+100+100")

# Widget Text
texto = tk.Text(ventana, height=10, width=30)
texto.pack(pady=20)

# Se le pasa el parámetro event para que no de error al llamarla desde el bind porque el bind le pasa un parámetro
def posicion_cursor(event=None):
    # Obtener la posición del cursor
    posicion_cursor = texto.index(tk.INSERT)
    print(f"Posición del cursor: {posicion_cursor}")
    print("Evento pasado:", event)

# Vincular el evento de tecla para actualizar la posición del cursor
texto.bind("<KeyRelease>", posicion_cursor)

ventana.mainloop()

'''
La función .bind() en Tkinter sirve para asociar eventos del usuario (como teclas, clics o movimientos del ratón) con funciones específicas que tú defines. Es como decir: “cuando el usuario haga esto, ejecuta esta función”.

widget.bind("<evento>", funcion)
- <evento>: Es una cadena que describe el evento que quieres capturar. Por ejemplo, "<Button-1>" para un clic izquierdo del ratón, "<KeyPress>" para una tecla presionada, o "<KeyRelease>" para una tecla liberada.
- funcion: Es la función que quieres que se ejecute cuando ocurra el evento. Esta función debe aceptar al menos un argumento, que es el objeto del evento.

🎯 Ejemplos de eventos comunes
Evento	Descripción
<Button-1>	Clic izquierdo del ratón
<Button-3>	Clic derecho del ratón
<Double-Button-1>	Doble clic izquierdo
<Key>	Cualquier tecla presionada
<Return>	Tecla Enter
<Motion>	Movimiento del ratón
<Enter>	Cursor entra en el widget
<Leave>	Cursor sale del widget

'''