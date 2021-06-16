from django.urls import path

from . import views 

app_name = 'posts'

urlpatterns = [
    path('posts/<id>/',   views.PostAPIView.as_view(),   name='list'),  #Detail View, Update View, Delete View
    path('posts/',   views.postCreate.as_view(),   name='detail'), #List View, Create View
 
    # path('posts/detail/<id>/', views.PostDetailAPIview.as_view(), name='detail'),
    # path('posts/create/', views.PostCreateAPIview.as_view(), name='create'),
    # path('posts/list/',   views.PostListAPIView.as_view(),   name='list'),
    # path('posts/update/<id>/', views.PostUpdateAPIview.as_view(), name='update'),
    # path('posts/delete/<id>/', views.PostDeleteAPIview.as_view(), name='delete'),
]
    