import tkinter as tk
from tkinter import messagebox

def registrar_persona():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    direccion = direccion_entry.get()

    if nombre and edad and direccion:
        mensaje = f"Nombre: {nombre}\nEdad: {edad}\nDirección: {direccion}"
        messagebox.showinfo("Registro Exitoso", mensaje)
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos")

# Crear la ventana principal
root = tk.Tk()
root.title("Registro de Persona")

# Frame para los campos de entrada
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Etiqueta y campo de entrada para el nombre
nombre_label = tk.Label(input_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)
nombre_entry = tk.Entry(input_frame)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para la edad
edad_label = tk.Label(input_frame, text="Edad:")
edad_label.grid(row=1, column=0, padx=5, pady=5)
edad_entry = tk.Entry(input_frame)
edad_entry.grid(row=1, column=1, padx=5, pady=5)

# Etiqueta y campo de entrada para la dirección
direccion_label = tk.Label(input_frame, text="Dirección:")
direccion_label.grid(row=2, column=0, padx=5, pady=5)
direccion_entry = tk.Entry(input_frame)
direccion_entry.grid(row=2, column=1, padx=5, pady=5)

# Botón para registrar
registrar_btn = tk.Button(root, text="Registrar", command=registrar_persona)
registrar_btn.pack(pady=5)

# Ejecutar el bucle de la aplicación
root.mainloop()