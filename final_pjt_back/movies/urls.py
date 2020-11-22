from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.movielist),
    path('<int:movie_pk>/<username>/reviews/', views.review_create),
    path('recommend/', views.recommend),
    path('pingpong/', views.pingpongTransfer),
]
