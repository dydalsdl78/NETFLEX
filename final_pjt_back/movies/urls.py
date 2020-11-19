from django.urls import path
from . import views 

urlpatterns = [
    path('movielist/', views.movielist),
]