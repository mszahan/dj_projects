from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerilizer
from .models import Movie



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerilizer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.filter(movie_type='action')
    serializer_class = MovieSerilizer


