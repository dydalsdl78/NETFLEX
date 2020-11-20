from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def movielist(request):
    if request.method == "GET":
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_create(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        print(request.data['title'])
        print('end')
        if serializer.is_valid(raise_exception=True):
            print('valid')
            serializer.save(user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            print('invalid')
