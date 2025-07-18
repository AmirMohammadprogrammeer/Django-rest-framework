from django.shortcuts import render
from . import serializers
from . import permission
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView ,RetrieveUpdateDestroyAPIView ,RetrieveAPIView ,DestroyAPIView ,CreateAPIView
from .models import Article
# Create your views here.
class ListBlog(ListAPIView):
    queryset = Article.objects.all().filter(status=True)
    serializer_class = serializers.ArticleListSerializer


class DetailBlog(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleListSerializer
    lookup_field = "slug"
    permission_classes = [permission.IsSuperUserAuthorOrReadOnly]

class CreatePost(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.CreateArticleSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
       serializer.save(author=self.request.user)

