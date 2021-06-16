from django.urls import path

from . import views 
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



urlpatterns = [

    # register endpoint
    path('register/', views.RegisterAPIView.as_view(), name='user-register'),

    #custom jwt tokens 
    path('', views.AuthView.as_view(), name='user-login'),

    #default jwt tokens
    # path('jwt/', obtain_jwt_token, name='jwt-token'),
    
    #jwt refresh endpoint 
    path('jwt/refresh/', refresh_jwt_token, name='jwt-refresh'),
    
    #verify token
    path('jwt/verify/', verify_jwt_token, name='jwt-verify'),


    # detail user view 
    path('users/', views.UserApiView.as_view(), name='users-all'),
    path('<username>/', views.UserDetailApiView.as_view(), name='user-detail'),
    path('posts/<username>/', views.UserPostsApiView.as_view(), name='user-detail'),
]