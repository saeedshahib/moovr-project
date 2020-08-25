from django.shortcuts import get_object_or_404, render
from .models import Movie
from itertools import islice
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
