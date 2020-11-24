from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Movie, Review, Genre
from .serializers import MovieSerializer, ReviewSerializer
from .CBF import overview_recommend, genre_recommend
from .pingpong import pingpong

from accounts.models import User
from .models import Review, Movie
# Create your views here.


@api_view(['GET'])
def movielist(request):
    # 영화 목록에 대한 권한은 관리자만 가질 것이고 POST로 조작 할 일은 없을 것 같아서 주석처리했어요. 나중에 토의하고 지우던가 하죠 머
    # if request.method == "GET":
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    # else:
    # serializer = MovieSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(user=request.user)
    #     return Response(serializer.data)


@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def review_create_list(request):
    # 리뷰 만드는 거는 GET으로 목록로 보여줘야하니까 아마 함수이름이랑 url이름 바꿔야 할 것 같음요
    # 어떤 영화에 달려있는지 알아오기 위해서 movie_pk 값 이랑 일치하는 영화 불러왔습니다.
    # vue에서 받은 username과 일치하는 user_id 값을 user에 저장
    if request.method == 'GET':
        reviews = Review.objects.all()
        for review in reviews:
            print(review.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, movie=Movie.objects.get(pk=request.data['movie']['id']))
            return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(['POST'])
def recommendGenre(request):
    # print(request.data)
    movies_recommended = genre_recommend(request.data['movie_title'])
    # print(movies_recommended)
    return Response(movies_recommended)


@api_view(['POST'])
def recommendOverview(request):
    # print(request.data)
    movies_recommended = overview_recommend(request.data['movie_title'])
    # print(movies_recommended)
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
