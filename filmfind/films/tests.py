#En este caso, vamos a crear una clase de test para nuestra vista de películas (FilmViewSet). Esta clase heredará de unittest.TestCase y tendrá un método setUp para inicializar nuestra vista y un conjunto de métodos de test para probar las distintas funcionalidades de la vista.

#Para utilizar factory_boy, debemos crear una clase de factory para nuestro modelo de películas. Esta clase heredará de Factory y especificará los campos que queremos incluir en nuestros objetos de prueba. Podemos usar el módulo Faker de factory_boy para generar valores aleatorios para estos campos, y el módulo FuzzyDecimal para generar números decimales aleatorios dentro de un rango especificado.

#Con esto en mente, podemos escribir nuestro código de tests de la siguiente manera:

import unittest

from factory import Factory, Faker
from factory.fuzzy import FuzzyDecimal

from films.models import Film
from films.views import FilmViewSet

class FilmFactory(Factory):
    class Meta:
        model = Film

    pk = Faker('pyint')
    title = Faker('sentence', nb_words=4)
    year = Faker('year')
    rating = FuzzyDecimal(low=1, high=10)
    synopsis = Faker('text')

class FilmViewSetTestCase(unittest.TestCase):
    def setUp(self):
        self.viewset = FilmViewSet()

    def test_create_film(self):
        # Creamos una película usando nuestro factory
        film = FilmFactory.create()
        film.save() # Guardamos la película en la base de datos

        # Aseguramos que la película se ha creado correctamente en la base de datos
        self.assertIsNotNone(Film.objects.get(pk=film.pk))

    def test_update_film(self):
        film = FilmFactory.create()


        # Actualizamos algunos de sus campos
        data = {
        'title': 'Cadena Perpetua',
        'year': 1994,
        'rating': 9.2,
        'synopsis': 'Dos hombres encarcelados se unen a lo largo de varios años, encontrando consuelo y redención final a través de actos de decencia común.'
        }

        # Actualizamos la película en la base de datos
        film.title = data['title']
        film.year = data['year']
        film.rating = data['rating']
        film.synopsis = data['synopsis']
        film.save()

        # Aseguramos que los cambios se han guardado correctamente en la base de datos
        film.refresh_from_db()
        self.assertEqual(film.title, data['title'])
        self.assertEqual(film.year, data['year'])
        self.assertEqual(film.rating, data['rating'])
        self.assertEqual(film.synopsis, data['synopsis'])

    def test_delete_film(self):
        film = FilmFactory.create()

        # Eliminamos la película
        film.delete()

        # Aseguramos que la película ha sido eliminada de la base de datos
        with self.assertRaises(Film.DoesNotExist):
            Film.objects.get(pk=film.pk)