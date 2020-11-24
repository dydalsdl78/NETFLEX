from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.movielist),
    path('<int:movie_pk>/<username>/reviews/', views.review_create),
    path('genre/', views.recommendGenre),
    path('overview/', views.recommendOverview),
    path('pingpong/', views.pingpongTransfer),
    path('search/', views.searchMovie),
    path('getgenre/', views.getGenre),
]
