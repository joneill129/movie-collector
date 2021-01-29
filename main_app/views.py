from django.shortcuts import render
from django.http import HttpResponse

class Movie:
    def __init__(self, title, year, genre, language, description):
        self.title = title
        self.year = year
        self.genre = genre
        self.language = language
        self.description = description

movies = [
    Movie('The Dark Knight', 2008, 'Action/Adventure', 'English, Mandarin', 'SO GOOD'),
    Movie('Pans Labyrinth', 2007, 'Drama/Fantasy', 'Spanish', 'In the Falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world.'),
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello! This is the movie collector home page!</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})
