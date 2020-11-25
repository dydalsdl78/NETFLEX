from django.urls import path
from . import views

urlpatterns = [
    path('movielist/', views.movielist),
    path('review_create_list/', views.review_create_list),
    path('genre/', views.recommendGenre),
    path('overview/', views.recommendOverview),
    path('pingpong/', views.pingpongTransfer),
    path('search/', views.searchMovie),
    path('getgenre/', views.getGenre),
    path('<int:review_pk>/', views.detail),
    path('<int:review_pk>/comment_crud/', views.comment_crud),
]
