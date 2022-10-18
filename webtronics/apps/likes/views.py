from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Like
from .serializers import LikeSerializer
from users.permissions import IsOwnerOrReadOnly


# Create your views here.

class LikeCreateApiView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)


class LikeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly,)
