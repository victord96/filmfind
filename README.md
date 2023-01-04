# FilmFind
FilmFind is a web application that allows users to search and view information about films. The application is configured to connect to a MySQL database and allows users to view details of a specific film, and create, update, and delete films.

## Key features

- Search and view films
- Film details, including title, year, rating, and synopsis
- Testing with factory_boy

## Prerequisites
- Python 3.6 or later
- Django 3.1 or later

## Installation and usage

To install and use FilmFind, follow the following steps:

Clone this repository to your local machine:

```sh
git clone https://github.com/victord96/filmfind
```

Create and activate a virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate
```
Install the necessary dependencies:
```sh
pip install -r requirements.txt
```
Perform the necessary migrations:
```sh
python manage.py makemigrations
python manage.py migrate
```
Start the development server:
```sh
python manage.py runserver
```
Access the application through your web browser at http://127.0.0.1:8000/.
## Testing
To run the tests for FilmFind, follow the following steps:

Make sure you are in the root directory of the project.

Run the following command:
```sh
python manage.py test
```
