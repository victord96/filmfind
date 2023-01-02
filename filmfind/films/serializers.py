from rest_framework import serializers
from .models import Film, Series

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'year', 'rating', 'synopsis')

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('title', 'year', 'rating', 'synopsis', 'season_count')
