import requests
from django.shortcuts import render, get_object_or_404
from django.conf import settings

TMDB_API_KEY = settings.TMDB_API_KEY

def movie_list(request):
    # TMDB Endpoints
    trending_url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={TMDB_API_KEY}&language=en-US"
    new_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=en-US&page=1"
    action_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=28&language=en-US"
    comedy_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_API_KEY}&with_genres=35&language=en-US"

    # Fetch Data
    trending = requests.get(trending_url).json().get("results", [])
    new_releases = requests.get(new_url).json().get("results", [])
    action_movies = requests.get(action_url).json().get("results", [])
    comedy_movies = requests.get(comedy_url).json().get("results", [])

    # Pass into context
    context = {
        "trending": trending[:10],
        "new_releases": new_releases[:10],
        "action_movies": action_movies[:10],
        "comedy_movies": comedy_movies[:10],
    }

    return render(request, "movies/movie_list.html", context)


def favorites(request):
    # Later we will filter by logged-in user
    return render(request, "movies/favorites.html")


def movie_detail(request, movie_id):
    # Fetch detailed info for a single movie by ID
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(url)
    movie = response.json()
    return render(request, "movies/movie_detail.html", {"movie": movie})

