from django.contrib import admin
from .models import Movie, Showing, Snack

# Register your models here.
admin.site.register(Movie)
admin.site.register(Showing)
admin.site.register(Snack)