from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),            # Home / movie list
    path("favorites/", views.favorites, name="favorites"),   # Favorites page
    path("movie/<int:movie_id>/", views.movie_detail, name="movie_detail"),  # Movie detail page
]

