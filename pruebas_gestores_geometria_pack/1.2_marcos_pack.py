import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Marcos Empaquetados con pack()")
ventana.geometry("400x400")
ventana.configure(bg="lightgray")

# Crear marcos, instanciar los atributos en el propio objeto y empaquetarlos
marco1 = tk.Frame(ventana, width=200, height=100, bg="red", relief=tk.RAISED, borderwidth=3)
marco1.pack(pady=10)

marco2 = tk.Frame(ventana, width=200, height=100, bg="blue", relief=tk.RAISED, borderwidth=3)
marco2.pack(pady=10)

marco3 = tk.Frame(ventana, width=200, height=100, bg="green", relief=tk.RAISED, borderwidth=3)
marco3.pack(pady=10)


# Iniciar el bucle principal de la aplicación
ventana.mainloop()

'''
El gestor de geometría pack() en Tkinter es una de las tres herramientas principales para organizar widgets en la ventana de una aplicación, junto con grid() y place(). Su característica principal es que empaqueta los widgets en bloques antes de colocarlos en la ventana, lo que lo hace útil para diseños simples y lineales.

Características principales

    Empaquetado y apilado: pack() trata a los widgets como bloques rectangulares y los apila uno al lado del otro. La dirección en la que se apilan se puede controlar con la opción side. Si no se especifica, se apilan verticalmente de arriba a abajo de forma predeterminada.

    Diseño adaptable: Una de sus mayores ventajas es que es relativamente fácil de usar para crear interfaces que se adaptan automáticamente a diferentes tamaños de ventana. Esto se debe a que el gestor redimensiona y mueve los widgets según las dimensiones del contenedor.

    Opciones de configuración: pack() ofrece varias opciones para personalizar el comportamiento del empaquetado:

        side: Controla el lado del contenedor en el que se colocará el widget ('top', 'bottom', 'left', 'right'). Por ejemplo, widget.pack(side='left') colocará el widget en el lado izquierdo del contenedor.

        fill: Determina si el widget debe expandirse para ocupar el espacio disponible. Puede ser 'x' (horizontalmente), 'y' (verticalmente), 'both' o 'none'.

        expand: Si se establece en True, el widget se expandirá para ocupar cualquier espacio libre en el contenedor, lo que es útil para que los elementos se estiren cuando la ventana se redimensiona.

        pady/padx: Añade espacio extra, o "padding", alrededor del widget en los ejes Y (vertical) o X (horizontal).

    Sencillez y limitaciones: pack() es ideal para diseños de una sola columna o fila y es muy intuitivo para principiantes. Sin embargo, no es la mejor opción para diseños complejos o basados en tablas, ya que puede volverse difícil de manejar cuando se necesitan ubicaciones precisas o cuando los widgets deben alinearse en una cuadrícula. En esos casos, grid() o place() son más apropiados.

'''