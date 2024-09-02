import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os

# Nombre del archivo donde se guardarán los datos
archivo_datos = 'sueldos_y_fechas.csv'

# Función para cargar los datos del archivo
def cargar_datos():
    if os.path.exists(archivo_datos):
        with open(archivo_datos, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fecha, sueldo = row
                sueldos_y_fechas.append((fecha, float(sueldo)))

# Función para guardar los datos en el archivo
def guardar_datos():
    with open(archivo_datos, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sueldos_y_fechas)

# Función para generar la gráfica
def generar_grafica(sueldos_y_fechas):
    df = pd.DataFrame(sueldos_y_fechas, columns=["Fecha", "Sueldo"])
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y-%m-%d')
    df = df.sort_values(by='Fecha')

    plt.figure(figsize=(10, 6))
    plt.plot(df['Fecha'], df['Sueldo'], marker='o', linestyle='-', color='b')
    plt.xlabel('Fecha')
    plt.ylabel('Sueldo')
    plt.title('Comparación de lo Ganado Cada Día')
    plt.grid(True)
    plt.show()

# Función para añadir la entrada a la lista y limpiar los campos
def agregar_dato():
    fecha = entry_fecha.get()
    sueldo = entry_sueldo.get()
    
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
        sueldo = float(sueldo)
        sueldos_y_fechas.append((fecha, sueldo))
        guardar_datos()
        entry_fecha.delete(0, tk.END)
        entry_sueldo.delete(0, tk.END)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una fecha válida (YYYY-MM-DD) y un sueldo numérico.")

# Función para generar la gráfica con los datos introducidos
def mostrar_grafica():
    if sueldos_y_fechas:
        generar_grafica(sueldos_y_fechas)
    else:
        messagebox.showwarning("Advertencia", "No hay datos para generar la gráfica.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Gráficas de Sueldos")
ventana.geometry("300x200")

# Lista para almacenar los sueldos y fechas
sueldos_y_fechas = []

# Cargar los datos existentes desde el archivo
cargar_datos()

# Etiqueta y campo de entrada para la fecha
label_fecha = tk.Label(ventana, text="Fecha (YYYY-MM-DD):")
label_fecha.pack(pady=5)
entry_fecha = tk.Entry(ventana)
entry_fecha.pack(pady=5)

# Etiqueta y campo de entrada para el sueldo
label_sueldo = tk.Label(ventana, text="Sueldo:")
label_sueldo.pack(pady=5)
entry_sueldo = tk.Entry(ventana)
entry_sueldo.pack(pady=5)

# Botón para añadir los datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón para generar la gráfica
boton_grafica = tk.Button(ventana, text="Generar Gráfica", command=mostrar_grafica)
boton_grafica.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
