# FilmFind
FilmFind es una aplicación web que permite a los usuarios buscar y ver información sobre películas. La aplicación esta configurada para conectar con una bd en mysql y permite ver detalles de una película específica, y crear, actualizar y eliminar películas.

## Características principales

- Búsqueda y visualización de películas
- Detalles de película, incluyendo título, año, rating y sinopsis
- Tests con factory_boy

## Requisitos previos
- Python 3.6 o posterior
- Django 3.1 o posterior

## Instalación y uso

Para instalar y utilizar FilmFind, siga los siguientes pasos:

Clone este repositorio a su máquina local:

```sh
git clone https://github.com/victord96/filmfind
```

Cree un entorno virtual y actívelo:

```sh
python3 -m venv venv
source venv/bin/activate
```
Instale las dependencias necesarias:
```sh
pip install -r requirements.txt
```
Realice las migraciones necesarias:
```sh
python manage.py makemigrations
python manage.py migrate
```
Inicie el servidor de desarrollo:
```sh
python manage.py runserver
```
Acceda a la aplicación a través de su navegador web en la dirección http://127.0.0.1:8000/.
## Pruebas
Para ejecutar las pruebas de FilmFind, siga los siguientes pasos:

Asegúrese de que está en el directorio raíz del proyecto.

Ejecute el siguiente comando:
```sh
python manage.py test
```
