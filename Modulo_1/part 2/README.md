# (Par. 2) Ejemplo: Otras herramientas para el manejar errores 
## Genera un ejemplo en el lenguaje de tu preferencia utilizando las herramientas que encontraste.

## ¿Qué es Sentry y cómo funciona?

Sentry es una plataforma de software de código abierto que se emplea para rastrear, gestionar y corregir errores en aplicaciones. Funciona recopilando información sobre los errores y excepciones que ocurren en el código y proporcionando una interfaz intuitiva para visualizar y analizar estos problemas. Sentry puede ser usado en una amplia variedad de lenguajes de programación, como Python, JavaScript, Ruby y Java.

## Beneficios clave de utilizar esta plataforma

* Detección temprana de errores. Sentry brinda una visibilidad instantánea de los errores y las excepciones que ocurren en una aplicación. Esto permite a los desarrolladores identificar y solucionar problemas antes de que afecten a los usuarios finales.
* Notificaciones en tiempo real. Sentry envía notificaciones en tiempo real cuando se produce un error crítico en la aplicación. Esto permite a los equipos de desarrollo responder de inmediato y minimizar el impacto de los problemas en los usuarios.
* Información detallada del error. Recopila una amplia gama de información sobre los errores, incluyendo trazas de pila, variables locales y contexto del usuario. Esta información detallada facilita la reproducción y depuración de los problemas, lo que acelera el proceso de resolución de errores.
* Agrupación y clasificación de errores. Agrupa automáticamente los errores similares sobre la base de su causa raíz, lo que ayuda a los desarrolladores a identificar patrones comunes y abordar problemas recurrentes de manera eficiente.
* Integración con herramientas de desarrollo. Sentry se integra con una amplia gama de herramientas populares de desarrollo, como sistemas de control de versiones, servicios de seguimiento de problemas y plataformas de CI/CD. Esta integración permite una experiencia de desarrollo más fluida y simplifica el flujo de trabajo de corrección de errores.

Para empezar a utilizar Sentry necesitamos crear un nuevo proyecto y elegimos en este caso Python como el lenguaje a utilizar:

![Screenshot 1](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.2/Modulo_1/part%202/images/01.png)

Le asignamos un nombre al proyecto y dejamos puesta la opcion de que nos imforme con notificaciones:

![Screenshot 2](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.2/Modulo_1/part%202/images/02.png)

Intalamos Sentry SDK como una dependecia usando PIP y copiamos y pegamos el codigo de inicializacion:
![Screenshot 3](https://github.com/DiegoAlbertoValdivia/Computaci-n-Tolerante-a-Fallas/blob/1.2/Modulo_1/part%202/images/03.png)
