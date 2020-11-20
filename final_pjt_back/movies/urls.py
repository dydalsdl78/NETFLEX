from django.urls import path
from . import views 

urlpatterns = [
    path('movielist/', views.movielist),
    path('reviews/', views.review_create),
]