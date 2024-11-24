# ¿Que es Istio?

## Charla sobre Microservicios con ISTIO:
- [Meetup] Microservicios con Istio en OpenShift:  https://www.youtube.com/watch?v=Qete_HitzgQ

## Aplicación utilizando ISTIO:
- Introducción a ISTIO / Service Mesh: 

https://youtu.be/ofJ5swfP2kQ

Un Service Mesh es una infraestructura dedicada a la gestión y observabilidad del tráfico
entre microservicios en una arquitectura de aplicación distribuida. Proporciona una capa de
abstracción sobre la red de comunicación entre servicios, permitiendo funciones como el
enrutamiento inteligente, la seguridad, la supervisión y la gestión del tráfico.
Istio es uno de los Service Mesh más populares y potentes disponibles actualmente. Aquí
tienes una descripción más detallada:

## Arquitectura:
Istio está compuesto principalmente por tres componentes:
- 1. Envoy Proxy: Este es el componente de data plane de Istio. Envoy es un proxy de
servicio de alto rendimiento y extensible que se despliega junto a cada instancia de
servicio en el clúster. Gestiona todo el tráfico de red entre los servicios,
proporcionando funcionalidades como balanceo de carga, descubrimiento de
servicios, enrutamiento, cifrado, etc.
- 2. Pilot: Pilot es el componente de control plane responsable de traducir la
configuración de alto nivel de Istio (definida por el usuario) en reglas y políticas
entendibles por Envoy Proxy. También se encarga del descubrimiento de servicios y
la gestión del tráfico.
- 3. Mixer: Mixer es responsable de la telemetría y la política de acceso. Recoge
información de telemetría de todos los proxies Envoy y aplica políticas de acceso y
autorización basadas en esta información.

## Funcionalidades clave de Istio:
- 1. Enrutamiento inteligente: Istio permite el enrutamiento de tráfico basado en
múltiples criterios como cabeceras HTTP, encuestas de tráfico, versiones de servicio,
etc. Esto facilita la implementación de estrategias de despliegue como canary
releases, blue-green deployments, etc.
- 2. Seguridad: Istio proporciona cifrado de extremo a extremo mediante TLS entre
servicios, autenticación y autorización basadas en reglas de acceso, y políticas de
control de acceso a nivel de red.
- 3. Supervisión y Telemetría: Istio recoge métricas detalladas sobre el tráfico de red,
latencia, errores, etc., lo que permite una supervisión exhaustiva del rendimiento de
la aplicación. Además, integra herramientas como Prometheus, Grafana, Jaeger, etc.,
para análisis y visualización de datos.
- 4. Gestión del tráfico: Istio facilita la implementación de circuit breakers, retries,
timeouts y otros patrones de gestión de tráfico para mejorar la resiliencia de la
aplicación.
- 5. Políticas de control de acceso: Permite definir reglas de autorización y autenticación
a nivel de servicio, lo que proporciona una capa adicional de seguridad para la
aplicación.

## Ventajas de usar Istio:
- Abstracción y desacoplamiento: Istio permite a los desarrolladores centrarse en la
lógica del negocio sin preocuparse por los aspectos de red y seguridad.
- Resiliencia: Mejora la resiliencia de la aplicación mediante la gestión inteligente del
tráfico y la detección de errores.
- Observabilidad: Proporciona una visibilidad completa del tráfico de red y el
rendimiento de la aplicación, facilitando la detección y resolución de problemas.
- Escalabilidad: Istio escala horizontalmente para adaptarse al crecimiento del
número de servicios y la carga de trabajo de la aplicación.

En resumen, Istio es una herramienta poderosa para la gestión de microservicios en
entornos de contenedores, que ofrece funcionalidades avanzadas de seguridad,
observabilidad y gestión del tráfico. Su adopción puede simplificar significativamente la
implementación y operación de aplicaciones distribuidas en la nube.

## Instalación de Istio:
Primero se debe descargar la última versión de Istio, en la página web:
https://github.com/istio/istio/releases.
Abrimos en la barra de tareas, editar "Editar las variables de entorno del sistema". Dentro
de las variables del usuario editamos la variable path y agregamos una nueva entrada a la
carpeta bin.

![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Service%20Mesh%2C%20principalmente%20de%20Istio/image/Captura%20de%20pantalla%202024-11-24%20171908.png)

Despues en el cmd se ejecuta el comando “istioctl”

![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Service%20Mesh%2C%20principalmente%20de%20Istio/image/Captura%20de%20pantalla%202024-11-24%20171931.png)

Finalmente, se debe instalar el perfil demo mediante el siguiente comando “istioctl manifest
apply --set profile=demo”

![](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.9/Modulo_1/Service%20Mesh%2C%20principalmente%20de%20Istio/image/Captura%20de%20pantalla%202024-11-24%20171952.png)
