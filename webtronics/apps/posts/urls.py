
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='posts'),
    path('create/', views.PostCreateApiView.as_view(), name='post_create'),
    path('detail/<int:pk>/', views.PostDetailAPIView.as_view(), name='post_detail'),
]