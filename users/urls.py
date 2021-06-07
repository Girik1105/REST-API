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
    path('api-token-verify/', verify_jwt_token, name='jwt-verify'),
]