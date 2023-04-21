# info de la materia: ST0263 Topicos especiales en telematica

## Estudiantes: 
 - Stiven Yepes Vanegas, esyepesv@eafit.educo
 - Juan Pablo Cortes Gonzalez, jpcortesg@eafit.edu.co
 - Yhilmar Andres Chaverra, yachaverrc@eafit.edu.co

## Profesor: 
- Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Proyecto 1: Diseño e Implementación de un Middleware que Implemente un Servicio de Mensajería Asincrónica entre Aplicaciones

## Breve descripción de la actividad
Este proyecto consiste en la implementación de un MOM (Middleware Orientado a Mensajes) el cual debe permitir la conexión de múltiples clientes a estos servicios utilizando comunicación asíncrona. Este MOM utiliza colas para gestionar los mensajes Request-Response y permitir a estos servicios usar la metodología - Publicador - Suscriptor.

## Qué aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Implementando el proyecto pudimos desarrollar distintas funcionalidades y requisitos asignados por el profesor:
- Se implementó la autenticación de usuarios
- CRUD de colas según el usuario y sus credenciales
- Mecanismo de recepción de mensajes en modo pull o push/eventos
- Persistencia de datos
- Tolerancia a fallos (Uso de memoria compartida)
- Interacción sincrónica / asincrónica
- Seguridad (Uso de credenciales para los mensajes)

## Qué aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En este proyecto tuvimos un alcance limitado en el cual omitimos algunos requisitos para el cumplimiento de otros, por lo tanto, estos requisitos son:

- Particionamiento
- Replicación
- Encriptación
- Manejo de sesión

## Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

![Diagrama Topicos (1)](https://user-images.githubusercontent.com/60229713/233505258-a6a198ed-28b1-4194-8ed2-f2d711ca5bd0.png)

La arquitectura de nuestro proyecto consiste en un MOM dividido en 2 servidores enlazados, una API implementada en Flask, la cual realizará la conexión de los clientes, y un servidor GRPC el cual es el encargado de hacer la comunicación efectiva con los servicios, en este caso, la persistencia de datos al ser manejada a través de un archivo .txt el cual guarda la información de los mensajes de cada servicio y también la información de las colas.

## Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerías, paquetes, etc, con sus números de versiones.

Lenguaje de programación: Python 3.8.10

Librerías: os, Flask, jsonify, grpc, sys, google, time, concurrent, futures, protobuf.

## Como se compila y ejecuta.

Para la ejecución del proyecto, utilizamos el comando `python3 <filename>` para correr los archivos correspondientes. A continuación, explicamos cuáles archivos ejecutar:

- `GRPC.py` para correr el servidor GRPC dentro del MOM.
- `FLASK.py` para la ejecución de la API Flask dentro del MOM.
- `service1.py` para ejecutar el primer servicio.
- `service2.py` para ejecutar el segundo servicio.

Para hacer las peticiones a través de la API, usamos un cliente Postman que envía peticiones HTTP con las credenciales correspondientes.

## Detalles técnicos

En el desarrollo del proyecto, hicimos uso de múltiples conceptos aprendidos en clase sobre la comunicación usando Middleware. Utilizamos los conceptos de la comunicación GRCP como protocolo sincrónico, utilizamos conceptos de memoria compartida para permitir al API y al servidor GRPC la comunicación y el almacenamiento de los distintos mensajes Request-Response en el flujo del programa. Se utilizó la nube de Google Cloud para el posterior despliegue en una máquina virtual EC2, además de un entorno virtual de Python para la ejecución de cada proceso dentro de la instancia.

## Descripción y cómo se configura los parámetros del proyecto

Para acceder a la aplicación API REST se hace a través del puerto 4000, accesible ya sea a través de la ip publica (34.170.228.98) o el nombre de dominio mom.stivenyepes.lat y la conexión a cada uno de los servidores de hace a través de GRPC usando el puerto (50051)

## Detalles de la organización del código por carpetas.

![Screenshot_20230421_071242](https://user-images.githubusercontent.com/60229713/233635097-99d039d9-7cc6-4ae7-82d8-90ea27a8285d.png)

## Resultados

### Run Program
![WhatsApp Image 2023-04-21 at 06 57 17](https://user-images.githubusercontent.com/60229713/233671678-88035c7b-6346-4e55-a7e5-e417a2b9b324.jpeg)
### Create User
![WhatsApp Image 2023-04-21 at 07 05 56](https://user-images.githubusercontent.com/60229713/233671745-2b437492-0344-418b-8f68-dcb532f8c210.jpeg)
### Crete Queue
![WhatsApp Image 2023-04-21 at 07 08 09](https://user-images.githubusercontent.com/60229713/233665106-e0174649-1e68-4dfa-b4e1-7ed647914fdf.jpeg)
### Update Queue
![WhatsApp Image 2023-04-21 at 07 10 17](https://user-images.githubusercontent.com/60229713/233665836-5b564829-43e1-4ebd-a96c-caed12ef5029.jpeg)
### Delete Queue
![WhatsApp Image 2023-04-21 at 07 11 19](https://user-images.githubusercontent.com/60229713/233665848-7cdf0335-510e-45d2-a436-37f30aa1f144.jpeg)
### Get Queue
![WhatsApp Image 2023-04-21 at 07 12 57](https://user-images.githubusercontent.com/60229713/233665871-9806f558-7c70-4db3-92ce-8c862fbe92dc.jpeg)
### Send Message
![WhatsApp Image 2023-04-21 at 07 14 25](https://user-images.githubusercontent.com/60229713/233665879-ed16a4ed-076f-42b9-af41-c5c74ea9590a.jpeg)
### Get Message
![WhatsApp Image 2023-04-21 at 07 16 23](https://user-images.githubusercontent.com/60229713/233665891-681f9dac-78d7-40ed-9ccf-eedc09bad9ba.jpeg)
### Persistence
![WhatsApp Image 2023-04-21 at 07 19 31](https://user-images.githubusercontent.com/60229713/233665904-b68b87d5-feed-4dab-bc6c-8d653e3d4d34.jpeg)



