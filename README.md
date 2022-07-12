# CS3P02 - Cloud Computing: Proyecto Final

## Introducción

Los objetivos y motivaciones del proyecto, detalles funcionales y arquitectura de la app, su justificación y los conceptos de *Cloud Computing* aplicados serán explicados en esta sección. Esta está dividida en los siguientes puntos:

- [Objetivos](#objetivos)
- [Funcionalidades de la App](#funcionalidades-de-la-app)
- [Arquitectura de la App](#arquitectura-de-la-app)
- [Justificación](#justificacion)
- [Conceptos de Cloud Computing utilizados](#conceptos-de-cloud-computing-utilizados)

#### Objetivos

El proyecto se basa en una app web que permite a usuarios autenticados ejecutar procesos específicos, obtener sus resultados, observar información de la ejecución de procesos anteriores (fecha, hora, usuario, tiempo de ejecución y logs) y estadísticas de uso. Los detalles del funcionamiento de la aplicación se describirán más adelante en la sección de [Funcionalidades de la App](#funcionalidades-de-la-app).

Los objetivos principales de este proyecto están relacionados al uso de conceptos y herramientas de *Cloud Computing*. Para poder simplificar la implementación y hacer una propuesta más realista, se reducirá estos conceptos y herramientas para un mejor enfoque en:

- Escalabilidad y Monitoreo
- Multi-Tenancy
- Load Balancing
- Containerization (Docker, Kubernetes)

Finalmente, identificar las ventajas que surgen de su uso.

#### Funcionalidades de la App

**Login:** Los usuarios existentes (creados previamente) pueden acceder a la aplicación a través de una autenticación.

**Visualización de procesos:** Los usuarios pueden ver los procesos relacionados al cliente al cual pertenecen. No tienen acceso a procesos que no pertenezcan a su cliente.

**Ejecución de procesos:** Los usuarios pueden ejecutar los procesos relacionados al cliente al cual pertenecen. Al solicitar una ejecución, el servidor ejecuta el proceso con los parámetros enviados por el usuario, y se actualiza su estado.

**Visualización de estadísticas de los procesos:** Los usuarios pueden visualizar información de los procesos que han ejecutado. Esto incluye datos como el estado del proceso, la fecha de ejecución, el tiempo en ejecución, sus logs y su archivo de salida.

**Descarga de archivos:** Los usuarios pueden descargar los archivos de salida y logs de los procesos que han ejecutado.

#### Arquitectura de la App
La app está conformada por tres módulos principales: una aplicación React para manejar la interfaz web y permitir a los usuarios enviar solicitudes al servidor; una API principal encargada de manejar (crear, actualizar, proporcionar y remover) la información de los usuarios, clientes y procesos; y finalmente una API encargada de manejar las solicitudes para la ejecución de procesos, y de asignar los procesos a un grupo de *threads* trabajadores.

![Arquitectura de la App](/Diagramas/arquitectura.png  "Arquitectura de la App")

#### Justificación

Este proyecto utiliza un modelo de aplicación ya existente que me encuentro trabajando desde hace un tiempo, con el objetivo de poder proporcionar un medio de acceso a la ejecución de procesos de manera centralizada a un grupo de personas que lo requieren.

La idea de utilizar esta aplicación previa es incorporar los conceptos de cloud para alcanzar un sistema que puede aprovechar sus ventajas. Además, sirve como un ejemplo de un SaaS que se basa en servicios en la nube, y permite analizar todas las consideraciones que se deben tomar al desplegarlo.

#### Conceptos de *Cloud Computing* utilizados

A continuación se detallarán los conceptos mencionados en la sección [Objetivos](#objetivos) con una explicación de cómo serán implementados por la App.

- **Escalabilidad y Monitoreo:** Se utilizará un sistema de monitoreo para obtener información sobre el uso de recursos, la latencia, cantidad de solicitudes, etc. De esta manera, se puede escalar el servicio (*containers*) de ser necesario, equilibrar las cargas e identificar anomalías.

- **Multi-Tenancy:** La aplicación es un servicio web que será utilizado por múltiples usuarios simultáneamente, quienes utilizarán sus recursos de manera compartida. De esta manera, podemos aprovechar las capacidades de un sistema *multi-tenant* para satisfacer estas necesidades, implementando un servidor centralizado capaz de atender múltiples solicitudes junto con un grupo de containers a los cuáles se les asignará tareas creadas por los usuarios.

- **Private Cloud:** Dado que el servicio estará disponible únicamente para los usuarios creados por un cliente, podemos aprovechar para implementarlo dentro de una nube privada para así evitar tráfico no deseado al sistema.

- **Load Balancing:** Dado que el rendimiento es un punto importante del servicio, queremos que exista un balance de cargas de trabajo entre containers

- **Containerization:** Aprovechando las ventajas de *containerization*, podemos crear imágenes de cada componente para simplificar su *deployment* y sus actualizaciones. Por otro lado, si deseamos agregar otro *container* trabajador, es tan simple como contruirlo desde la misma imagen, y como estos no hacen más que ejecutar procesos específicos podemos reducir sus requerimientos y su tamaño lo máximo posible. Si se desea agregar un nuevo proceso, se genera una nueva imagen en base a la anterior y se actualiza los demás containers.

## Implementación

A continuación se presentan detalles de la implementación

#### Herramientas utilizadas

- Minikube (Deployment)
- Docker (Containerization)
- Prometheus (Monitoreo)

#### Detalles

Se crearon dos containers centrales para el funcionamiento de la app, uno para el *frontend* y uno para el *backend*. Los `Dockerfile`para ambos estan incluidos en sus respectivas carpetas. Se pueden generar las imágenes con los siguientes comandos:

	# Dado que las imágenes no están publicadas en DockerHub, se debe ejecutar el siguiente comando antes de construirlas para que estas estén disponibles en el ambiente de minikube.
	eval $(minikube -p minikube docker-env)

	# Para crear la imagen del Backend
	cd src/backend/
	docker build -t condata-backend .
	
	# Para crear la imagen del Frontend
	cd src/frontend/
	docker build -t condata-frontend .

Una vez generadas las imágenes, se genera el k8s cluster con el siguiente comando:

	minikube start

Ahora, ya podemos utilizar `kubectl` para manejar el cluster. El archivo `deployment.yaml` contiene los detalles del *deployment* que generará los pods de *backend* y *frontend* correspondientes. Para generar estos pods, ejecutamos:

	kubectl apply -f deployment.yaml
	
Una vez creados los *deployments* y servicios, podemos acceder a los endpoints accediendo a la URL del cluster en el puerto de cada servicio:

	minikube service --all
	
	# El resultado será algo similar a esto:
	#|-----------|--------------------------|------------------------------|-----------------------------|
	#| NAMESPACE |           NAME           |         TARGET PORT          |             URL             |
	#|-----------|--------------------------|------------------------------|-----------------------------|
	#| default   | kubernetes               | No node port                 |
	#| default   | proyecto-cloud-back-svc  | proyecto-cloud-back-pt/8000  | http://192.168.59.100:31478 |
	#| default   | proyecto-cloud-front-svc | proyecto-cloud-front-pt/3000 | http://192.168.59.100:30806 |

Para acceder a los servicios, ir al navegador e ingresar URL.

#### Monitoreo
Se utilizó **Prometheus** con las configuraciones encontradas en el repositorio de [Kube-Prometheus](https://github.com/prometheus-operator/kube-prometheus) para generar las instancias de monitoreo. Se crea un namespace llamado `monitoring` donde se ejecutan todos los *pods* necesarios para un monitoreo básico. Luego podemos acceder al dashboard ejecutando:

	kubectl -n monitoring port-forward svc/prometheus-operated 9090

En el navegador, ingresar a `http://localhost:9090` para acceder al operador.

