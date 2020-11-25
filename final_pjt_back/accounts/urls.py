from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('username/', views.username),
    path('userReview/', views.userReview),
    path('userMovie/', views.userMovie),
]
