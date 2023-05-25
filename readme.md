## Creando base de datos

~~~
CREATE DATABASE db;
USE db;

CREATE TABLE curso(
    codigo INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    credios TINYINT
);
~~~

## virtualenv

Para activar un entorno virtual en donde podamos instalar bibliotecas sin causar conflictos con otros proyectos.

Revisar si se tiene instalado una versión de virualenv
~~~
virtualenv --version
~~~
Si no esta instalado, instalar con el siguiente comando
~~~
pip install virtualenv
~~~
Crear entorno de desarrollo con 

- python versión 3 
- nombre de entorno env

~~~
virtualenv -p python3 env
~~~
Para activar el entorno debes usar el siguiente comando

~~~
.\env\Scripts\activate
~~~

## PIP
Es un sistema de gestión de paquetes

Vamos a listar los paquetes actualmente instalados en nuestro proyecto.
~~~
pip list
~~~

## Instalar FLASK y MySQL
Paquete para crear un servidor web con python

~~~
pip install flask flask_mysqldb
~~~

Vamos a listar los paquetes actualmente instalados en nuestro proyecto y se verán muchos más paquetes.
~~~
pip list
~~~

