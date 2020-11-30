from django.db import models
from django.shortcuts import reverse


class Countries(models.Model):
    country = models.CharField(max_length=50)


class Genres(models.Model):
    genre = models.CharField(max_length=50)
    movie = models.ManyToManyField('Movie', blank=True)
    people = models.ManyToManyField('People', blank=True)

    def __str__(self):
        return self.genre


class GenresInMovie(models.Model):
    pass


class Movie(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50, blank=True)
    video = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    marketing = models.CharField(max_length=50, blank=True)
    fees_in_usa = models.CharField(max_length=50, blank=True)
    fees_in_the_world = models.CharField(max_length=50, blank=True)
    premiere = models.DateTimeField(blank=True)
    duration = models.CharField(max_length=50, blank=True)
    production_year = models.DateTimeField(blank=True)
    age = models.CharField(max_length=50, blank=True)
    country = models.ForeignKey(Countries)


    # def get_absolute_url(self):
    #     return reverse('post_detail_url', kwargs={})

    def __str__(self):
        return self.name, self.production_year


class People(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Countries)
    date_birth = models.DateTimeField()

    def __str__(self):
        return self.name


class Professions(models.Model):
    profession = models.CharField(max_length=50)


class PeopleInMovie(models.Model):
    pass


class PeopleInProfession(models.Model):
    pass


class Rating(models.Model):
    pass
