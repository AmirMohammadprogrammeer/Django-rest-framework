from rest_framework import serializers
from .models import Book

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name",]

class BookDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'