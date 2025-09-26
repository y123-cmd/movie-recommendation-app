from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movie

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "movies/movie_list.html", {"movies": movies})

