from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.title
