import tkinter as tk

ventana = tk.Tk()
ventana.title("Etiquetas con place y grid")
ventana.geometry("400x200")

# Crear marcos
marco1 = tk.Frame(ventana, bd=2, relief="sunken", padx=5, pady=5)
marco2 = tk.Frame(ventana, bd=2, relief="sunken", padx=5, pady=5)

# Posicionar marcos
marco1.place(relx=0, rely=0, relwidth=0.48, relheight=1)
marco2.place(relx=0.52, rely=0, relwidth=0.48, relheight=1)

# Crear etiquetas
etiqueta1 = tk.Label(marco1, text="Etiqueta 1", bg="blue", fg="white")
etiqueta2 = tk.Label(marco1, text="Etiqueta 2", bg="purple", fg="white")
etiqueta3 = tk.Label(marco1, text="Etiqueta 3", bg="gray", fg="white")
etiqueta4 = tk.Label(marco1, text="Etiqueta 4", bg="red", fg="white")

etiqueta5 = tk.Label(marco2, text="Etiqueta 5", bg="yellow", fg="black")
etiqueta6 = tk.Label(marco2, text="Etiqueta 6", bg="lightpink", fg="black")
etiqueta7 = tk.Label(marco2, text="Etiqueta 7", bg="coral", fg="black")
etiqueta8 = tk.Label(marco2, text="Etiqueta 8", bg="cyan", fg="white")

# Etiquetas colocadas en grid() en el primer marco           
etiqueta1.grid(row=0, column=0, sticky="nsew")
etiqueta2.grid(row=0, column=1, sticky="nsew")
etiqueta3.grid(row=1, column=0, sticky="nsew")
etiqueta4.grid(row=1, column=1, sticky="nsew")

marco1.grid_rowconfigure(0, weight=1)
marco1.grid_rowconfigure(1, weight=1)
marco1.grid_columnconfigure(0, weight=1)
marco1.grid_columnconfigure(1, weight=1)

# Etiquetas en pack() en el segundo marco
etiqueta5.pack(fill="both", expand=True)
etiqueta6.pack(fill="both", expand=True)
etiqueta7.pack(fill="both", expand=True)
etiqueta8.pack(fill="both", expand=True)

ventana.mainloop()