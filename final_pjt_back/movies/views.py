from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie, Review, Genre
from .serializers import MovieSerializer, ReviewSerializer, CommentSerializer
from .CBF import overview_recommend, genre_recommend
from .pingpong import pingpong

from accounts.models import User
from .models import Review, Movie, Comment
from django.contrib.auth import get_user_model
# API키와 URL불러오기 위해
# from decouple import config
# Create your views here.


@api_view(['GET'])
def movielist(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
def review_create_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        review = Review.objects.get(pk=request.data['id'])
        if not request.user.reviews.filter(pk=review.id).exists():
            return Response({'detail': '권한이 없습니다.'})

        print(review.title)
        serializer = ReviewSerializer(review, data=request.data)
        print('hererer')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review = Review.objects.get(pk=request.data['id'])
        review.delete()
        return Response({'detail': '삭제되었습니다.'})

    else:
        serializer = ReviewSerializer(data=request.data)
        print(request.data['movie']['id'])
        if serializer.is_valid():
            serializer.save(user=request.user, movie=Movie.objects.get(
                pk=request.data['movie']['id']))
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
def comment_crud(request, review_pk):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, review=Review.objects.get(
                pk=request.data['review']['id']))
            return Response(serializer.data, status.HTTP_201_CREATED)

    elif request.method == 'GET':
        review = Review.objects.get(pk=review_pk)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    else:
        comment_pk = request.data['id']
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return Response({'id': comment_pk})


@api_view(['POST'])
def get_movie(request):
    movie = Movie.objects.get(title=request.data['name'])
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def recommendGenre(request):
    movies_recommended = genre_recommend(request.data['movie_title'])
    return Response(movies_recommended)


@api_view(['POST'])
def recommendOverview(request):
    print(request.data)
    movies_recommended = overview_recommend(request.data['movie_title'])
    return Response(movies_recommended)


@api_view(['POST'])
def pingpongTransfer(request):
    print(request.data)
    answer = pingpong(request.data)
    return Response(answer)


@api_view(['POST'])
def searchMovie(request):
    movie = Movie.objects.get(title=request.data['search'])
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def getGenre(request):
    genres = request.data['genres']
    print(genres)
    print(request.data)
    res = []
    for genre_id in genres:
        genre = Genre.objects.values("name").get(id=genre_id)
        print(genre)
        res.append(genre)
    return Response(res)


@api_view(['GET'])
def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    return Response(review)


@api_view(['POST'])
def commentCount(request):
    res = []
    for i in range(len(request.data['reviewComment'])):
        movieId = request.data['reviewComment'][i]['movie']['id']
        name = request.data['reviewComment'][i]['user']['username']
        userId = get_user_model().objects.get(username=name)
        reviewId = Review.objects.values("id").get(
            movie_id=movieId, user_id=userId)
        review = Review.objects.get(pk=reviewId['id'])
        reviews = review.comments.all()
        res.append(len(reviews))

    return Response({"count": res})
