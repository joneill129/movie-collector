from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie
from . forms import ShowingForm


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello! This is the movie collector home page!</h1>')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', { 'movies': movies })

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    showing_form = ShowingForm()
    return render(request, 'movies/detail.html', { 'movie': movie, 'showing_form': showing_form})

def add_showing(request, movie_id):
    form = ShowingForm(request.POST)
    if form.is_valid():
        new_showing = form.save(commit=False)
        new_showing.movie_id = movie_id
        new_showing.save()
        return redirect('detail', movie_id=movie_id)

class MovieCreate(CreateView):
    model = Movie
    fields = '__all__'

class MovieUpdate(UpdateView):
    model = Movie
    fields = '__all__'

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'   
    
