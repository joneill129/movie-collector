from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Movie, Snack
from . forms import ShowingForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello! This is the movie collector home page!</h1>')

def about(request):
    return render(request, 'about.html')

@login_required
def movies_index(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/index.html', { 'movies': movies })

@login_required
def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    snacks_movie_doesnt_have = Snack.objects.exclude(id__in = movie.snacks.all().values_list('id'))
    showing_form = ShowingForm()
    return render(request, 'movies/detail.html', { 'movie': movie, 'showing_form': showing_form, 'snacks': snacks_movie_doesnt_have})

@login_required
def add_showing(request, movie_id):
    form = ShowingForm(request.POST)
    if form.is_valid():
        new_showing = form.save(commit=False)
        new_showing.movie_id = movie_id
        new_showing.save()
        return redirect('detail', movie_id=movie_id)

@login_required
def assoc_snack(request, movie_id, snack_id):
    Movie.objects.get(id=movie_id).snacks.add(snack_id)
    return redirect('detail', movie_id=movie_id)

        

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'year', 'genre', 'description', 'language']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'

class MovieDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/movies/'

class SnackList(LoginRequiredMixin, ListView):
    model = Snack

class SnackDetail(LoginRequiredMixin, DetailView):
    model = Snack

class SnackCreate(LoginRequiredMixin, CreateView):
    model = Snack
    fields = ['name']

class SnackUpdate(LoginRequiredMixin, UpdateView):
    model = Snack
    fields = ['name']

class SnackDelete( DeleteView):
    model = Snack
    success_url = '/snacks/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



   
    
