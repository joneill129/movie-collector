from django.db import models
from django.urls import reverse 

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})
