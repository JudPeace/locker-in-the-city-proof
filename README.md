# Prueba técnica Judith Manchón Vállegas

## Instalación previa

Las dependencias de python3 necesarias para ejecutar el código se pueden instalar con el fichero *requirements.txt* a través del comando:

> pip install -r requirements.txt

## Ejecución

Ejecutar los scripts es muy sencillo, pero hay que seguir el siguente orden y utilizar dos terminales, ya que en una se quedará ejecutandose la API mientras que con la otra cargamos los datos:

1. Ejecutamos el script generate_data.py que genera los datos en formato csv dentro de la carpeta data:
>python3 generate_data.py
2. Lanzamos la API REST en modo debug con el script app.py (se lanzará en el puerto 5000):
>python3 app.py
3. Cargamos los datos con load_data.py
>python3 load_data.py

## Servicios de la API

Se pueden ver en el script de app.py, sin embargo dejo aquí también las rutas existentes:

- POST http://localhost:5000/api/products con las siguentes claves:
    - brand
    - type
    - calories
    - fats
    - sugar
- PATCH http://localhost:5000/api/products/<id\> con el id del producto y una, varias o todas las siguentes claves:
    - brand
    - type
    - calories
    - fats
    - sugar
- POST http://localhost:5000/api/establishments con las siguentes claves:
    - name
    - address
    - opening_time
    - closing_time
- POST http://localhost:5000/api/establishments/<name\>/products/<id\>/prices donde name es el nombre del establecimiento y el id es el del producto. Además le pasaremos la siguente:
    - price
- GET http://localhost:5000/api/establishments/<name\>/products/prices donde name es el nombre del establecimiento. Este método devuelve los productos y sus respectivos precios para el establecimiento solicitado.

## Otros scripts
En el resto de scripts de python3 encontramos:
- Models.py definiciones de las clases para utilizar el ORM (FLask-SQLALchemy)
- responses.py contiene funciones para generar respuestas a las peticiones
    
## Generación de datos
Los datos se han generado a partir de unos arrays que contienen strings de marcas, productos y establecimientos generados por ChatGPT.
