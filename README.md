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
- Private Cloud
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

![Arquitectura de la App](/home/mauricio/Documents/2022-1/Cloud/Proyecto_Cloud/Diagramas/arquitectura.png  "Arquitectura de la App")

#### Justificación

Este proyecto utiliza un modelo de aplicación ya existente que me encuentro trabajando desde hace un tiempo, con el objetivo de poder proporcionar un medio de acceso a la ejecución de procesos de manera centralizada a un grupo de personas que lo requieren.

La idea de utilizar esta aplicación previa es incorporar los conceptos de cloud para alcanzar un sistema que puede aprovechar sus ventajas. Además, sirve como un ejemplo de un SaaS que se basa en servicios en la nube, y permite analizar todas las consideraciones que se deben tomar al desplegarlo.

#### Conceptos de *Cloud Computing* utilizados

A continuación se detallarán los conceptos mencionados en la sección [Objetivos](#objetivos) con una explicación de cómo serán implementados por la App.

- **Escalabilidad y Monitoreo:**
- **Multi-Tenancy:**
- **Private Cloud:**
- **Load Balancing:**
- **Containerization:**

## Implementación

TODO