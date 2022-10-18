from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'likes'

urlpatterns = [
    path('create/', login_required(views.LikeCreateApiView.as_view()), name='like_create'),
    path('detail/<int:pk>/', login_required(views.LikeDetailAPIView.as_view()), name='like_detail'),
]