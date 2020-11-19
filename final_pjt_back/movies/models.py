from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    video = models.BooleanField()
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True)
    original_language = models.CharField(max_length=10)
    original_title = models.CharField(max_length=50)
    genre_ids = models.ManyToManyField(Genre)