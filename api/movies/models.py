from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=250)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=50, default='action')

    def __str__(self):
        return self.name