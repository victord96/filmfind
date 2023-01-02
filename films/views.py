from rest_framework import viewsets
from .serializers import FilmSerializer, SeriesSerializer
from .models import Film, Series

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    http_method_names = ['get', 'post', 'update', 'delete']

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    http_method_names = ['get', 'post', 'update', 'delete']
