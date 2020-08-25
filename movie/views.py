from .models import Movie
from itertools import islice
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    movies = Movie.objects.order_by('-DateAdded')
    movies = list(filter(lambda x:x.IsMovieOfDay == True, movies))
    movies = list(islice(movies ,1, None))
    FilmOfTheDay = Movie.objects.order_by('-DateAdded')
    FilmOfTheDay = next(m for m in FilmOfTheDay if m.IsMovieOfDay)
    return render(request, 'movie/home.html',{'movies':movies,'FilmOfTheDay':FilmOfTheDay})

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/movie.html',{'movie':movie})


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'movie/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'movie/signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'movie/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'movie/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'movie/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
