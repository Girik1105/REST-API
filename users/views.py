from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
User = get_user_model()

from . import serializers
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView

from posts.models import Post
from posts.serializers import PostSerializer

from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler


jwt_payload_handler             = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler              = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler    = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


# Create your views here.
#  SOME ERROR OVER HERE CANOT CATCH

class AuthView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        #print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        data = request.data
        username = data.get('username') # username or email address
        password = data.get('password')
        qs = User.objects.filter(
                Q(username__iexact=username)|
                Q(email__iexact=username)
            ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response)
        return Response({"detail": "Invalid credentials"}, status=401)



class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegisterSerializer

    authentication_classes = []
    permission_classes = []

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class UserDetailApiView(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

class UserPostsApiView(ListAPIView):
    lookup_field = 'username'
    serializer_class = PostSerializer
    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['username']
        return Post.objects.filter(user__username=username)

class UserApiView(ListAPIView):
    serializer_class = serializers.UserSerializer
    def get_queryset(self, *args, **kwargs):
        return User.objects.all()