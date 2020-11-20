from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer

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


@api_view(['GET','POST'])
def review_create(request, movie_pk):
    # 리뷰 만드는 거는 GET으로 목록로 보여줘야하니까 아마 함수이름이랑 url이름 바꿔야 할 것 같음요
    # 어떤 영화에 달려있는지 알아오기 위해서 movie_pk 값 이랑 일치하는 영화 불러왔습니다. 
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # fields 에서 movie field가 비어있어서 넣었고
            serializer.save(movie=movie)
            # 원래 모델에는 user가 있어서 넣어줘야 했는데 현재 user값을 어떻게 불러와서 넣어야 할지 모르겠어서 일단 모델에서도 제거하고 해봤어요
            # serializer.save(user=request.user)
            return Response(serializer.data, status.HTTP_201_CREATED)

