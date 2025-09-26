from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="movies")

    def __str__(self):
        return self.title

