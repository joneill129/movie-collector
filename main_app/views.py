from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Snack
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
    snacks_movie_doesnt_have = Snack.objects.exclude(id__in = movie.snacks.all().values_list('id'))
    showing_form = ShowingForm()
    return render(request, 'movies/detail.html', { 'movie': movie, 'showing_form': showing_form, 'snacks': snacks_movie_doesnt_have})

def add_showing(request, movie_id):
    form = ShowingForm(request.POST)
    if form.is_valid():
        new_showing = form.save(commit=False)
        new_showing.movie_id = movie_id
        new_showing.save()
        return redirect('detail', movie_id=movie_id)

def assoc_snack(request, movie_id, snack_id):
    Movie.objects.get(id=movie_id).snacks.add(snack_id)
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

class SnackList(ListView):
    model = Snack

class SnackDetail(DetailView):
    model = Snack

class SnackCreate(CreateView):
    model = Snack
    fields = ['name']

class SnackUpdate(UpdateView):
    model = Snack
    fields = ['name']

class SnackDelete(DeleteView):
    model = Snack
    success_url = '/snacks/'


   
    
