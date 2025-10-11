import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Ventana")
ventana.geometry("500x400+100+100")
ventana.configure(background="lightblue")
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Configuración del widget Entry
entrada = tk.Entry(ventana, justify="center",
                    foreground="blue",
                    background="lightgray",
                    font=("Arial", 10, "italic"),
                    cursor="gumby",
                    relief="groove",
                    bd=3)
entrada.pack(pady=20)

# Configuración del widget Text
texto = tk.Text(ventana, height=10, width=30,
                foreground="blue",
                background="lightgray",
                font=("Arial", 10, "italic"),
                cursor="mouse",
                relief="groove",
                bd=3)
texto.pack()

print("Ancho de la pantalla:", ancho_pantalla)
print("Alto de la pantalla:", alto_pantalla)
ventana.after(100, lambda: print("Ancho ventana:", ventana.winfo_width(), "Alto ventana:", ventana.winfo_height()))


ventana.mainloop()

'''
.after() espera el tiempo indicado (en milisegundos) y luego ejecuta la función. Esto permite que Tkinter tenga tiempo de dibujar la ventana, calcular su tamaño real, y entonces tú puedes obtenerlo correctamente.
Suele dar valor 1 porque estás consultando el tamaño de la ventana antes de que se haya renderizado completamente. Tkinter no calcula el tamaño real de la ventana hasta que entra en el bucle principal o se actualiza manualmente. Por eso, cuando llamas a winfo_width() o winfo_height() justo después de crear la ventana, te devuelve 1. La solución es usar after() para retrasar la consulta hasta que la ventana esté completamente renderizada.

'''