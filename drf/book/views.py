from django.shortcuts import render
from rest_framework import generics
from .models import Book
from . import serializers
from rest_framework.permissions import IsAdminUser  ,IsAuthenticatedOrReadOnly
from . import permissions
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializers
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class =serializers.BookDetailSerializers
    permission_classes = (permissions.IsOwnerOrReadOnly,)

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookCreateSerializers
    permission_classes = [IsAdminUser]