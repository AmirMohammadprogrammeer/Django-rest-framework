from rest_framework import serializers
from . import models

class ListBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'

class ListUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Writer
        fields = '__all__'