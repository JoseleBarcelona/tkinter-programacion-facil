import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.state('zoomed')  # Maximizar la ventana
ventana.state('normal')  # Restaurar la ventana a su tamaño normal
ventana.state('withdrawn')  # Ocultar la ventana
ventana.state('iconic')  # Minimizar la ventana

ventana.mainloop()