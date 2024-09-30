# Estatus 

## Realizar un programa que sea capaz de revisar el estado de tu aplicación.  

https://python-para-impacientes.blogspot.com/2016/12/threading-programacion-con-hilos-i.html


https://tecnobillo.com/sections/python-en-windows/servicios-windows-python/servicios-windows-python.html


https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python

## Función para verificar si la página existe
```javascript
import tkinter as tk
from tkinter import messagebox
import requests

def verificar_pagina():
    url = url_entry.get()
    try:
        response = requests.get(url)

        # Si el código de estado es 200, la página existe
        if response.status_code == 200:
            status_label.config(text="La página existe", bg="#4CAF50", fg="white")
        elif response.status_code == 404:
            status_label.config(text="La página no existe (Error 404)", bg="#F44336", fg="white")
        else:
            status_label.config(text=f"Estado de la página: {response.status_code}", bg="#FFEB3B", fg="black")
    except requests.exceptions.RequestException as e:
        # Si ocurre algún error en la solicitud
        status_label.config(text="Error al acceder a la página", bg="#FF9800", fg="black")
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
```
## Interfaz gráfica

```javascript
# Interfaz gráfica
root = tk.Tk()
root.title("Verificador de Páginas Web")
root.geometry("400x200")
root.config(bg="#F0F0F0")

# Estilos
entry_style = {"bg": "#FFFFFF", "font": ("Helvetica", 12), "bd": 0, "highlightthickness": 1, "highlightbackground": "#CCCCCC"}
button_style = {"bg": "#2196F3", "fg": "white", "font": ("Helvetica", 12), "bd": 0, "activebackground": "#1976D2", "activeforeground": "white"}
label_style = {"bg": "#F0F0F0", "font": ("Helvetica", 12)}

# Campo de entrada para la URL
url_label = tk.Label(root, text="Introduce la URL:", **label_style)
url_label.pack(pady=(20, 5))

url_entry = tk.Entry(root, width=40, **entry_style)
url_entry.pack(pady=5, ipady=5)
```
## Inicia el bucle principal de tkinter
```javascript
# Botón para verificar la página
verificar_button = tk.Button(root, text="Verificar", command=verificar_pagina, **button_style)
verificar_button.pack(pady=15, ipadx=10, ipady=5)

# Etiqueta para mostrar el estado de la página
status_label = tk.Label(root, text="Esperando URL...", width=50, height=2, **label_style)
status_label.pack(pady=10)

# Inicia el bucle principal de tkinter
root.mainloop()
```
## Interfaz grafica
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.5/Modulo_1/ejercicio04/images/Captura%20de%20pantalla%202024-09-29%20194542.png)
## pagina existente
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.5/Modulo_1/ejercicio04/images/Captura%20de%20pantalla%202024-09-29%20194722.png)
## Error de acceso
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.5/Modulo_1/ejercicio04/images/Captura%20de%20pantalla%202024-09-29%20194757.png)
## Estado de pagina 500
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.5/Modulo_1/ejercicio04/images/Captura%20de%20pantalla%202024-09-29%20195035.png)
## Error 404
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.5/Modulo_1/ejercicio04/images/Captura%20de%20pantalla%202024-09-29%20195058.png)
