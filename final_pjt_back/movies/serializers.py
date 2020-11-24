from rest_framework import serializers
from .models import Movie, Review
from accounts.serializers import UserSerializer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = "__all__"