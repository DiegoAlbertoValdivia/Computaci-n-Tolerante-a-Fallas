# Generar un programa que sea capaz de restaurar el estado de ejecución. 

## (Application checkpointing)
## Checkpointing is a technique that provides fault tolerance for computing systems.

```javascript
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import csv
import os
```
Nota: importamos las librerias necesarios para poder tanto crear el archivo de respaldo, como poder generar la grafica

```javascript
archivo_datos = 'sueldos_y_fechas.csv'

def cargar_datos():
    if os.path.exists(archivo_datos):
        with open(archivo_datos, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fecha, sueldo = row
                sueldos_y_fechas.append((fecha, float(sueldo)))
```
Nota: Generamos el nombre del archivo donde se guardarán los datos y la función para cargar los datos del archivo

```javascript
def guardar_datos():
    with open(archivo_datos, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sueldos_y_fechas)
```
 
Nota: creamos otro def donde se guardaran los datos del archivo

```javascript
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
```
Nota: Ahora con ayuda de matplotlib.pyplot podemos generar la grafica y darle estilo

```javascript
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
```
Nota: añadimos la entrada a la lista y una limpieza de los datos

```javascript
def mostrar_grafica():
    if sueldos_y_fechas:
        generar_grafica(sueldos_y_fechas)
    else:
        messagebox.showwarning("Advertencia", "No hay datos para generar la gráfica.")

ventana = tk.Tk()
ventana.title("Generador de Gráficas de Sueldos")
ventana.geometry("300x200")

sueldos_y_fechas = []


cargar_datos()
```
Nota: generamos la grafica con los datos introducidos, creamos la ventana principal y cargamos los datos ya existentes

```javascript

label_fecha = tk.Label(ventana, text="Fecha (YYYY-MM-DD):")
label_fecha.pack(pady=5)
entry_fecha = tk.Entry(ventana)
entry_fecha.pack(pady=5)

label_sueldo = tk.Label(ventana, text="Sueldo:")
label_sueldo.pack(pady=5)
entry_sueldo = tk.Entry(ventana)
entry_sueldo.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_grafica = tk.Button(ventana, text="Generar Gráfica", command=mostrar_grafica)
boton_grafica.pack(pady=10)

ventana.mainloop()

```
Nota: por ultimo etiquetamos y creamos el campo de entrada a la fecha, sueldo, y ejecutamos la aplicacion

## interfaz de la toma de datos:
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.3/Modulo_1/Ejercicio02/images/1.png)
## muestra de la grafica:
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.3/Modulo_1/Ejercicio02/images/2.png)
## archivo csv de guardado de informacion:
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.3/Modulo_1/Ejercicio02/images/3.png)
