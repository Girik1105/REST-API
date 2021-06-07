from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.mixins import (CreateModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin, 
                                   DestroyModelMixin,
                                   ListModelMixin)

from rest_framework.generics import (GenericAPIView,
                                     ListAPIView, 
                                     CreateAPIView, 
                                     RetrieveAPIView, 
                                     UpdateAPIView,
                                     DestroyAPIView,)

from django.contrib.auth import get_user_model
User = get_user_model()
from . import serializers, models

from users.permissions import IsOwnerOrReadOnly

# Create your views here.


#  SEPERATE CRUD ENDPOINT VIEWS 

# class PostListAPIview(APIView):

#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     authentication_classes = []

#     def get(self, reques, format=None):
#         qs = models.Post.objects.all()
#         serializer = serializers.PostSerializer(qs, many=True)
#         return Response(serializer.data)



# class PostCreateAPIview(CreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     authentication_classes = []   
    
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer



# class PostUpdateAPIview(UpdateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     authentication_classes = []   
    
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer

#     lookup_field = 'id'


# class PostDeleteAPIview(DestroyAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     authentication_classes = []   
    
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer

#     lookup_field = 'id'

# class PostDetailAPIview(RetrieveAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     authentication_classes = []   
    
#     queryset = models.Post.objects.all()
#     serializer_class = serializers.PostSerializer

#     lookup_field = 'id'

#     def get(self, request, id, *args, **kwargs):
#         object = models.Post.objects.get(id=id)
#         serialized_data = serializers.PostSerializer(object)
#         return Response(serialized_data.data)
   

# ONE ENDPOINT VIEW 


class PostAPIView(UpdateModelMixin,
                  DestroyModelMixin, 
                  RetrieveAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)        

class PostCreateAPIView(CreateModelMixin,
                  RetrieveModelMixin,
                  ListModelMixin, 
                  GenericAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    lookup_field = 'id'

    def get_queryset(self):
        qs = models.Post.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs
    
    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id')
        queryset = self.get_queryset()
        obj = None 
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            # self.check_permissions(request, obj)
        return obj 

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id')
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)      


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
