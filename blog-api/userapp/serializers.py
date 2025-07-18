from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationsUser(serializers.ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username","first_name","last_name","password","password_confirmation")
    
    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop("password_confirmation",None)
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ListsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"