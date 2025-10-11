import tkinter as tk
import random


def cambiar_color_rgb(ventana, etiqueta):
    """Cambia el fondo a un color predefinido RGB y actualiza la etiqueta."""
    colores = ["red", "green", "blue", "yellow", "purple", "orange"]
    color_aleatorio = random.choice(colores)
    ventana.config(bg=color_aleatorio)
    etiqueta.config(text=f"Color RGB: {color_aleatorio}")


def cambiar_color_hex(ventana, etiqueta):
    """Cambia el fondo a un color aleatorio en formato hexadecimal y actualiza la etiqueta."""
    color_aleatorio = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    ventana.config(bg=color_aleatorio)
    etiqueta.config(text=f"Color Hexadecimal: {color_aleatorio}")


def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Mi primera ventana")
    ventana.geometry("400x300")
    ventana.config(bg="lightgray")  # Color de fondo inicial

    # Widgets
    etiqueta_rgb = tk.Label(ventana, text="Color RGB:", font=("Arial", 12, "bold"))
    etiqueta_rgb.pack(pady=10)

    etiqueta_hex = tk.Label(ventana, text="Color Hexadecimal:", font=("Arial", 12, "bold"))
    etiqueta_hex.pack(pady=10)

    boton_rgb = tk.Button(
        ventana,
        text="Cambiar Color Fondo RGB",
        command=lambda: cambiar_color_rgb(ventana, etiqueta_rgb)
    )
    boton_rgb.pack(pady=10)

    boton_hex = tk.Button(
        ventana,
        text="Cambiar Color Fondo Hexadecimal",
        command=lambda: cambiar_color_hex(ventana, etiqueta_hex)
    )
    boton_hex.pack(pady=10)

    return ventana


if __name__ == "__main__":
    app = crear_ventana()
    app.mainloop()



'''
¿Por qué en el anterior código el command se le pasa una lambda si ya hemos definido una función para poder ser llamada?

La diferencia está en cómo se pasan los argumentos al command en tkinter.

1. Cuando la función NO necesita parámetros

Puedes pasar la referencia de la función directamente, sin paréntesis:

boton = tk.Button(ventana, text="Haz clic", command=mi_funcion)

⚠️ Importante: si escribes command=mi_funcion(), la función se ejecuta en ese mismo momento y no cuando pulses el botón.

2. Cuando la función SÍ necesita parámetros

command no acepta directamente funciones con argumentos. Por eso usamos lambda o functools.partial.

Ejemplo con lambda:

boton = tk.Button(
    ventana,
    text="Cambiar color",
    command=lambda: cambiar_color_rgb(ventana, etiqueta)
)

Aquí, lambda crea una función anónima sin parámetros que, al ejecutarse, llama a cambiar_color_rgb(ventana, etiqueta).
Es como un “puente” para pasar argumentos.

3. En la versión con clase

Como las funciones (self.cambiar_color_rgb) ya tienen acceso a los atributos (self.root, self.etiqueta_rgb), no necesitan argumentos externos → entonces ya no hace falta lambda:

self.boton_rgb = tk.Button(
    self.root,
    text="Cambiar Color Fondo RGB",
    command=self.cambiar_color_rgb  # sin lambda, directo
)
🔑 Resumiendo:

Si la función no requiere parámetros → command=mi_funcion.

Si requiere parámetros → command=lambda: mi_funcion(arg1, arg2).

En una clase muchas veces basta con command=self.mi_metodo, porque los atributos (self.etiqueta_rgb, etc.) ya están dentro del objeto.

'''