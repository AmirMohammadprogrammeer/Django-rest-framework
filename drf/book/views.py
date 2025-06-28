from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import serializers
from .permissions import IsAuthorOrReadOnly
from .models import Book
from django.contrib.auth import get_user_model

# Create your views here.
class ListBookView(ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = serializers.ListBookSerializers

class UserListView(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = serializers.ListUserSerializers