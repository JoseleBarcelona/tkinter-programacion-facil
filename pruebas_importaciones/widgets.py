import tkinter as tk

class Etiqueta(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        

class Boton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        



'''
Sintaxis	    Tipo de argumentos	    Se almacena como:
*args	        Posicionales	        Tupla
**kwargs	    De palabra clave	    Diccionario

🧩 ¿Qué hace **kwargs aquí?

En ambas clases (Etiqueta y Boton), **kwargs permite que el constructor acepte argumentos adicionales con clave y valor al crear el widget. Estos argumentos se pasan directamente a la clase base (Clase heredada, tk.Label o tk.Button) mediante super().__init__(master, **kwargs).

Esto hace que tus clases sean flexibles y reutilizables, porque puedes modificar propiedades del widget al momento de instanciarlo sin tener que cambiar el código de la clase, agregando los parametros (**kwargs = keyword arguments) que quieras sin importar el número.

'''
