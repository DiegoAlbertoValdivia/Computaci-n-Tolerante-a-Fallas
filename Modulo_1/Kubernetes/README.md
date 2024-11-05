# Kubernetes

## Entregable

Genera un ejemplo similar al siguiente video:

Node.js listo para producción en Kubernetes
https://www.youtube.com/watch?v=T4lp6wtS--4

Cómo implementar una aplicación Go resiliente en Kubernetes en DigitalOcean
https://www.youtube.com/watch?v=g_-U5jddSuM&t=955s

## Se habilita la opcion de Kubernetes en docker
![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.7/Modulo_1/Kubernetes/images/Captura%20de%20pantalla%202024-10-13%20180226.png)

## Crea un nuevo proyecto de Node.js.
### npm init -y

## Instala express para manejar las peticiones HTTP:
### npm install express

## Crea el archivo app.js y agrega un código básico:
```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('Hello from Kubernetes!');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

## Crear un Dockerfile

```javascript
# Usa una imagen base de Node.js
FROM node:14

# Crea el directorio de la aplicación
WORKDIR /usr/src/app

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto de la aplicación
EXPOSE 3000

# Ejecuta el comando de inicio
CMD ["node", "app.js"]
```


##Construye la imagen de Docker:

###docker build -t my-node-app .

##Prueba la imagen para asegurarte de que funcione:
###docker run -p 3000:3000 my-node-app

##Deberías poder acceder a la aplicación en http://localhost:3000.

![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.7/Modulo_1/Kubernetes/images/Captura%20de%20pantalla%202024-11-04%20191548.png)

## Deployment: Crea un archivo deployment.yaml para describir el despliegue de la aplicación:
```javascript
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-node-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-node-app
  template:
    metadata:
      labels:
        app: my-node-app
    spec:
      containers:
      - name: my-node-app
        image: your-dockerhub-username/my-node-app:latest # Cambia esto si es necesario
        ports:
        - containerPort: 3000
```

## Service: Crea un archivo service.yaml para exponer la aplicación:
```javascript
apiVersion: v1
kind: Service
metadata:
  name: my-node-app-service
spec:
  selector:
    app: my-node-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

## Aplica los archivos de configuración:
##kubectl apply -f deployment.yaml
##kubectl apply -f service.yaml

##Verifica que los pods estén en ejecución:
###kubectl get pods

##Una vez que el servicio esté activo, obtén la dirección IP del balanceador de carga:
###kubectl get svc my-node-app-service

![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.7/Modulo_1/Kubernetes/images/Captura%20de%20pantalla%202024-11-04%20191847.png)
