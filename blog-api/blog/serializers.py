from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username")
    class Meta:
        model = Article
        fields = ("title","slug","author","content","publish","updated","status")

class CreateArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title","slug","content","publish","status",]
        read_only_fields  = ["author",]