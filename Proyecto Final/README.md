# Proyecto final
## Desarrolla una aplicación de microservicios en equipos máximo de 3 personas.

Formar equipos de máximo 3 personas para desarrollar la aplicación.
Deben seguir los siguientes pasos clave: 

División en Servicios Independientes: Dividir la aplicación en servicios independientes y modulares, cada uno responsable de una tarea o funcionalidad específica. Definir las interfaces y las formas de comunicación entre los microservicios.

Contenerización con Docker: Empaquetar cada microservicio en un contenedor Docker, que incluya todo el código, las dependencias y la configuración necesaria para que el servicio funcione de manera autónoma e independiente.

Orquestación con Kubernetes: Utilizar un orquestador de contenedores como Kubernetes para gestionar el ciclo de vida de los microservicios, incluyendo el despliegue, el escalado, el balanceo de carga y la recuperación ante fallos.

Comunicación entre Microservicios: Implementar mecanismos de comunicación entre los microservicios, como APIs REST, mensajería asíncrona o llamadas remotas, para que puedan interactuar entre sí.

Monitorización y Observabilidad: Configurar herramientas de monitorización y observabilidad, como Istio o Azure Monitor, para recopilar métricas, registros y trazas que permitan entender el comportamiento de la aplicación.

Automatización CI/CD: Automatizar el proceso de construcción, pruebas e implementación de los microservicios utilizando herramientas de integración y entrega continua (CI/CD).

Diseño Escalable y Resiliente: Diseñar la arquitectura para que los microservicios puedan escalarse horizontal y verticalmente según la demanda, y garantizar la disponibilidad de la aplicación incluso ante fallos.

 Implementar mecanismos de autenticación, autorización y cifrado de comunicaciones entre los microservicios y con los clientes. 

La ingeniería del caos, también conocida como Chaos Engineering: Implementar mecanismos para inyectar intencionadamente fallos en un sistema para probar su resistencia y capacidad de recuperación. Siguiendo estos pasos, se puede desarrollar una aplicación de microservicios robusta, escalable y fácil de mantener y evolucionar en el tiempo. 

Entregables. 
 En el readme de github deben de tener un tutorial o guía de como desplegar su proyecto. 
 Van a realizar una presentación de su proyecto, la cual va estar almacenada en el GitHub.
 
**Alumnos:** 
- Valdivia Guerra Diego Alberto
- Valdivia Guerra Ricardo Emmanuel


---
## Contenido
Para esta practica se utilicé la aplicación desarrollada en la practica pasada (9. Kubernetes) y cree una nueva versión de esta aplicación, esto para probar algunas cosas que ofrece Istio.

~~~python
from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


# V2 de la aplicacion de paises
@app.route('/<nombre_pais>')
def index(nombre_pais):
    url = 'https://restcountries.com/v3.1/name/'
    url_pais = url + nombre_pais
    response = requests.get(url_pais)
    data = json.loads(response.text)

    country = {
        'name': data[0]['name']['common'],
        'oficial_name': data[0]['name']['official'],
        'continent': data[0]['region'],
        'capital': data[0]['capital'][0],
        'population': data[0]['population'],
        'flag': data[0]['flags']['png'],
        'domain': data[0]['tld'][0],
        'independent': 'Estado soberano' if data[0]['independent'] else "Estado dependiente de otro país",
        'unMember': 'Miembro de naciones unidas' if data[0]['unMember'] else "No es miembro de naciones unidas",
    }


    return render_template('main.html', country=country)
~~~
Al igual que en la practica anterior, este contenedor se encuentra publicado en DockerHub para comodidad al momento de desplegarlo en Kubernetes. En esta vez no se hará un deploy en la nube, si no que se utilizará Minikube para desplegarlo localmente.

---
## Paso 1. Instalar Istio y configurarlo en nuestro Cluster
Para poder desplegar facilmente Istio, podemos utilizar su herramienta de consola, simplemente se descarga el archivo desde su página oficial, y una vez tenemos el ejecutable en nuestro PATH, podemos instalar Istio en nuestro cluster con el siguiente comando: 

~~~bash
istioctl install --set profile=demo
~~~
![Istioctl en acción](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/01.png "Istioctl en acción")

**Nota:** Al instalar istio con el perfil demo no incluirá todas las herramientas que se verán en este reporte, no incluirá Jaeger, Grafana ni el dashboard web Kiali, estos se necesitan instalar usando kubectl utilizando los manifiestos de ejemplo que vienen incluidos en la carpeta de istioctl. Es decisión de cada quien decidir que tanto instalar, tambien dependerá de que tantos recursos tienes disponibles en tu computadora/cluster, debido a que puedes sobrecargar de servicios que tal vez no termines utilizando.

## Paso 2. Habilitar a istio en todos los deploys de nuestro espacio de trabajo.
Para que nuestros servicios desplegados en Kubernetes puedan utilizar los servicios ofrecidos por Istio, será necesario habilitar la inyección de los contenedores de Istio en cada uno de los pods de nuestro servicio. Esto debido a que Istio funcionará como un proxy, todas las solicitudes que entren a nuestro servicio pasarán primero por Istio y despues, si la configuración lo permite, sera redirigido a nuestra aplicación.
![Inyección de Istio en los deploys](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/02.png "Inyección de Istio en los deploys")

## Paso 3. Crear nuestros deploys, servicios y el gateway de Istio para acceder a los servicios
Ya que Istio esta listo para funcionar en nuestro Cluster, solo resta desplegar nuestras aplicaciones, cabe aclarar, que los servicios de las aplicaciones fueron creados como ClusterIP, por lo que no son accesibles desde fuera del Cluster, por lo que debemos configurar otro servicio para acceder desde fuera de el, en este caso utilizamos un IngressGateway:

~~~yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: countries-gateway
spec:
  selector:
    app: istio-ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
~~~

Y tambien utilizamos un VirtualService para añadir algunas reglas para acceder a nuestra aplicación, este servicio restringe el acceso a la versión 1 de nuestra aplicación a unicamente los clientes que utilicen Chrome, si utilizan Firefox u otro navegador que no este basado en Chromium será redirigido a la aplicación en su versión 2, el manifiesto es el siguiente:

~~~yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: countries-service-ingress
spec:
  hosts: 
  - '*'
  gateways:
  - countries-gateway
  http:
  - match:
    - headers:
        user-agent:
          regex: .*Chrome.*
    route:
    - destination:
        host: countries-service-v1
  - route:
    - destination:
        host: countries-service-v2
~~~

![Configuración de deploys y servicios](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/03.png "Configuración de deploys y servicios")

Cuando ya tenemos todo desplegado, podemos revisar que los servicios sean accesibles, para esto podemos utilizar el comando ``kubectl get svc -A`` y buscamos el servicio que se llame istio-ingressgateway, podremos ver que tiene configurada una IP externa a la que podremos acceder.

![Obteniendo la IP del Gateway](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/06.png) "Obteniendo la IP del Gateway")

Si accedemos desde Mozilla Firefox:
![Accediendo al servicio desde firefox](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/04.png "Accediendo al servicio desde firefox")

Si accedemos desde Chrome:
![Accediendo al servicio desde chrome](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/05.png "Accediendo al servicio desde chrome")

## Paso 4. Iniciar el dashboard kiali
Desde una terminal ejecutamos el siguiente comando para iniciar el dashboard web:

~~~bash
istioctl dashboard kiali
~~~

Podremos ver mucha información acerca de las aplicaciones en nuestro cluster, grafos, salud, etc. Para poder visualizar mejor la transferencia de datos entre servicios, simule un intercambio ejecutando el siguiente comando en un contenedor del servicio v1:

~~~bash
while true; do curl http://countries-service-v2:5000/mexico > /dev/null 2>&1; done
~~~

![Grafo de servicios](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/09.png "Grafo de servicios")

Podemos ver mucha información acerca de los servicios y la transferencia de datos entre ellos, por ejemplo, por varios segundos simule una solicitud correcta y por otros cuantos segundos una solicitud invalida, por lo que se observa que indica que la salud esta degradada. Si abrimos la pestaña de aplicaciones y seleccionamos nuestra aplicación, podremos ver graficos acerca de las metricas y estados de salud de la aplicación.

![Metricas de la aplicación](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Proyecto%20v1%20/img/10.png "Metricas de la aplicación")

---
## Conclusión
Para concluir, los servicios desplegados en Kubernetes son increiblemente resilientes a fallos por el simple hecho de estar desplegados en esta plataforma, debido a el posible escalamiento y replicas configuradas, sin embargo, podemos añadir aún más funciones y servicios a estos, como lo hace Istio, la capacidad de añadir un logger, estadisticas, reglas de seguridad y algunas practicas de tolerancia a fallos como las que vimos en la practica de Quarkus hacen a Istio una herramienta muy util y sencilla de acoplar con aplicaciones ya existentes, debido a que no necesitas cambiar nada en código, si no que se inyectan los servicios utilizando contenedores como intermediarios entre el cliente y nuestra aplicación.
