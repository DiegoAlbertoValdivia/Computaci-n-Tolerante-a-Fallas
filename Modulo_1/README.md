# UNIVERSIDAD DE GUADALAJARA
 ![image](https://upload.wikimedia.org/wikipedia/commons/5/5f/Escudo_UdeG.svg)

#!/bin/bash
# blogfoto
# Pequeño script que cambia la resolución de la imagenes del tamaño original a 800*600. Usa ImageMagick
# Además de reducir la calidad de la imagen resultante.

# Primero nos aseguramos que la extensión esté en minúsculas y creamos fotoblog
rename 's/.JPG/.jpg/' *.JPG
mkdir fotoblog

#Empezamos el ciclo con las fotos de extensión jpg para reducirlo a 800*600.
#Además de poner las fotos dentro de fotoblog

for file in $( ls *.jpg ); do
convert -size 2048x1536 $file -thumbnail 800x600 fotoblog/foto_$file
done
echo “Listo!

# Ahora procedemos a comprimir más las imágenes dentro de fotoblog
cd fotoblog
for N in *; do
convert -compress jpeg -quality 55 -enhance -font Bookman-DemiItalic  -fill white -pointsize 14 -draw "text 680,500 'hbautista'" $N $N;
done
echo "Hemos terminado!"
