# info de la materia: ST0263 Topicos especiales en telematica

## Estudiantes: 
 - Stiven Yepes Vanegas, esyepesv@eafit.educo
 - Juan Pablo Cortes Gonzalez, jpcortesg@eafit.edu.co
 - Yhilmar Andres Chaverra, yachaverrc@eafit.edu.co

## Profesor: 
- Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Proyecto 1: Diseño e Implementación de un Middleware que Implemente un Servicio de Mensajería Asincrónica entre Aplicaciones

## 1. breve descripción de la actividad
Este proyecto consiste en la implementación de un MOM (Middleware Orientado a Mensajes) el cual debe permitir la conexión de múltiples clientes a estos servicios utilizando comunicación asíncrona. Este MOM utiliza colas para gestionar los mensajes Request-Response y permitir a estos servicios usar la metodología - Publicador - Suscriptor.

## 1.1. Qué aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Implementando el proyecto pudimos desarrollar distintas funcionalidades y requisitos asignados como el profesor:
- Se implementó la autenticación de usuarios
- CRUD de colas según el usuario y sus credenciales
- Mecanismo de recepción de mensajes en modo pull o push/eventos
- Persistencia de datos
- Tolerancia a fallos (Uso de memoria compartida)
- Interacción sincrónica / asincrónica
- Seguridad (Uso de credenciales para los mensajes)

## 1.2. Qué aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En este proyecto tuvimos un alcance limitado en el cual omitimos algunos requisitos para el cumplimiento de otros y la entrega de un MVP, por lo tanto, estos requisitos son:

- Particionamiento
- Replicación
- Encriptación
- Manejo de sesión

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![Diagrama Topicos (1)](https://user-images.githubusercontent.com/60229713/233505258-a6a198ed-28b1-4194-8ed2-f2d711ca5bd0.png)

La arquitectura de nuestro proyecto consiste en un MOM dividido en 2 servidores enlazados, una API implementada en Flask, la cual realizará la conexión de los clientes, y un servidor GRPC el cual es el encargado de hacer la comunicación efectiva con los servicios, en este caso, la persistencia de datos al ser manejada a través de un archivo .txt el cual guarda la información de los mensajes de cada servicio y también la información de las colas.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerías, paquetes, etc, con sus números de versiones.

Lenguaje de programación: Python 3.8.10

Librerías: os, Flask, jsonify, grpc, sys, pika, uuid, futures.

## como se compila y ejecuta.

Para la ejecución del proyecto, utilizamos el comando `python <filename>` para correr los archivos correspondientes. A continuación, explicamos cuáles archivos ejecutar:

- `GRPC.py` para correr el servidor GRPC dentro del MOM.
- `FLASK.py` para la ejecución de la API Flask dentro del MOM.
- `service1.py` para ejecutar el primer servicio.
- `service2.py` para ejecutar el segundo servicio.

Para hacer las peticiones a través de la API, usamos un cliente Postman que envía peticiones HTTP con las credenciales correspondientes.

## detalles del desarrollo.

### detalles técnicos

En el desarrollo del proyecto, hicimos uso de múltiples conceptos aprendidos en clase sobre la comunicación usando Middleware. Utilizamos los conceptos de la comunicación GRCP como protocolo sincrónico, utilizamos conceptos de memoria compartida para permitir al API y al servidor GRPC la comunicación y el almacenamiento de los distintos mensajes Request-Response en el flujo del programa. Se utilizó la nube de Google Cloud para el posterior despliegue en una máquina virtual EC2, además de un entorno virtual de Python para la ejecución de cada proceso dentro de la instancia.

### descripción y cómo se configura los parámetros del proyecto

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

![Screenshot_20230421_071242](https://user-images.githubusercontent.com/60229713/233635097-99d039d9-7cc6-4ae7-82d8-90ea27a8285d.png)

## opcionalmente - si quiere mostrar resultados o pantallazos 



