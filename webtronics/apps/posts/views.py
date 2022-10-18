from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from users.permissions import IsOwnerOrAdminOrReadOnly


class PostCreateApiView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
