from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.movielist),
    path('review_create_list/', views.review_create_list),
    path('recommend/', views.recommend),
    path('pingpong/', views.pingpongTransfer),
]
