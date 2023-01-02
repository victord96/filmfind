from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    rating = models.FloatField()
    synopsis = models.TextField()

class Series(models.Model):
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    rating = models.FloatField()
    synopsis = models.TextField()
    season_count = models.PositiveIntegerField()
