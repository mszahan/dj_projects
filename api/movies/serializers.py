from rest_framework import serializers
from .models import Movie


class MovieSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'duration', 'rating', 'movie_type']