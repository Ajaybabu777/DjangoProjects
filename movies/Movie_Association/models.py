from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)
    
class movie_table(models.Model):
    movie_name = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)