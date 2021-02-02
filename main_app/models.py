from django.db import models
from django.urls import reverse

WHERE = (
    ('B', 'Bed'),
    ('C', 'Couch'),
    ('P', 'Pillow Fort')
)

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('snack_detail', kwargs={'pk': self.id})
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    snacks = models.ManyToManyField(Snack)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})

class Showing(models.Model):
    date = models.DateField('Date Showing')
    time = models.TimeField()
    where = models.CharField(
        max_length=1,
        choices=WHERE,
        default=WHERE[0][1]
    )
    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_where_display()} on {self.date} at {self.time}"

    class Meta:
        ordering = ['-date']
