from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'likes'

urlpatterns = [
    path('create/', views.LikeCreateApiView.as_view(), name='like_create'),
    path('detail/<int:pk>/', views.LikeDetailAPIView.as_view(), name='like_detail'),
]