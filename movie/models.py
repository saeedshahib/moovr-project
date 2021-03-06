from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
import pytz

# Create your models here.

class Movie(models.Model):
    Title = models.CharField(max_length = 250)
    FilmOfTheDayImage = models.ImageField(upload_to = 'movie/images/')
    FilmOfTheDaySmallImage = models.ImageField(upload_to = 'movie/images/')
    BoxFilmImage = models.ImageField(upload_to = 'movie/images')
    SmallBoxFilmImage = models.ImageField(upload_to = 'movie/images/')
    FilmBackgroundImage = models.ImageField(upload_to = 'movie/images/')
    Time = models.IntegerField()
    Language = models.CharField(max_length = 250)
    Rating = models.FloatField(default=0)
    Director = models.CharField(max_length = 250)
    Country = models.CharField(max_length = 250)
    Jenre = models.CharField(max_length = 250)
    Cinematography = models.CharField(max_length = 250,blank=True)
    Screenplay = models.CharField(max_length = 250,blank=True)
    Music = models.CharField(max_length = 250,blank=True)
    Writer = models.CharField(max_length = 250,blank=True)
    Year = models.IntegerField()
    Cast = models.TextField()
    Synopsis = models.TextField()
    IsMovieOfDay = models.BooleanField(default=False)
    DateAdded = models.DateTimeField()
    FirstDownloadLink = models.URLField()
    SecondDownloadLink = models.URLField()
    SubtitleLink = models.URLField()
    
    def __str__(self):
        return self.Title
class Comment(models.Model):
    Content = models.TextField()
    Rating = models.SmallIntegerField()
    DateAdded = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Content