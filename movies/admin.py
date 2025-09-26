from django.contrib import admin
from .models import Movie, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "get_genre", "description")

    def get_genre(self, obj):
        return obj.genre.name if obj.genre else "-"
    get_genre.short_description = "Genre"

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)

