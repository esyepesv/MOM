# info de la materia: ST0263 Topicos especiales en telematica

## Estudiantes: 
 - Stiven Yepes Vanegas, esyepesv@eafit.educo
 - Juan Pablo Cortes Gonzalez, jpcortesg@eafit.edu.co
 - Yhilmar Andres Chaverra, yachaverrc@eafit.edu.co

## Profesor: 
- Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

#
# Proyecto 1: Diseño e Implementación de un Middleware que Implemente un Servicio de Mensajería Asincrónica entre Aplicaciones
#

# 1. breve descripción de la actividad
Este proyecto consiste en la implementacion de un MOM (Middleware Orientado a Mensajes) el cual debe permitir la conexion de multiples clientes a estos servicios utilizando comunicacion asincrona, este MOM utiliza colas para gestionas los mensajes Request - Response y permitir a estos servicios usar la metodologia - Publicador - Suscriptor.

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Implemetando el proyecto pudimos desarrollar distintas funcionalidades y requisitos asignados como el profesor:
- Se implemento la autenticacion de usuarios
- CRUD de colas segun el usuario y sus credenciales
- Mecanismo de recepción de mensajes en modo pull o push/eventos
- Persistencia de datos
- Tolerancia a fallos (Uso de archivo .txt)
- interaccion sincronica / asincronica
- Seguridad (Uso de credenciales para los mensajes)

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En este proyecto tuvimos un alcance limitado en el cual omitimos algunos requisitos para el cumplimiento de otros y la entrega de un MVP, por lo tanto estos requisitos son:

- Particionamiento
- Replicacion
- Encriptacion
- Manejo de sesion

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![Diagrama Topicos](https://user-images.githubusercontent.com/60229713/233501638-981862ca-54f8-42c3-b05d-748607ec0475.png)

La arquitectura de nuestro proyecto consiste en un MOM dividido en 2 servidores conectados, una API implementada en Flask, la cual realizara la conexion de los clientes, y un servidor GRPC el cual es el encargado de hacer la comunicacion efectiva con los servicios, en este caso la persistencia de datos al ser manejada a traves de un archivo .txt el cual guarda la informacion de los mensajes de cada servicio y tambien la informacion de las colas.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

lenguaje de programación: Python 3.8.10

librerias: os, Flask, jsonify, grpc, sys, pika, uuid, futures.

## como se compila y ejecuta.

Para la ejecucion del proyecto, utilizamos el comando python <filename> para correr los archivos correspondientes, a continuacion explicamos cuales archivos ejecutar:

- GRPC.py para correr el servidor grpc dentro del MOM
- FLASK.py para la ejecucion la API Flask dentro del MOM
- Service1.py para ejecutar el primer servicio
- Service2.py para ejecutar el segundo servicio

para hacer las peticiones a a traves de la API usamos un cliente Postman el cual envia peticiones http con las credenciales correspondientes.

## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
