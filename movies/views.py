from django.shortcuts import render
from .models import Movie, Genre
from django.db.models import Q

def movie_list(request):
    context = {
        "trending": Movie.objects.all()[:10],  # Example: first 10 movies
        "new_releases": Movie.objects.order_by('-release_date')[:10],
        "action_movies": Movie.objects.filter(genres__name__icontains="Action")[:10],
        "comedy_movies": Movie.objects.filter(genres__name__icontains="Comedy")[:10],
    }
    return render(request, "movies/movie_list.html", context)

