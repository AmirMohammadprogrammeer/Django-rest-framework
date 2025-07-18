from django.shortcuts import render
from .serializers import RegistrationsUser ,ListsUserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

# Create your views here.
class RegistrationsUserView(APIView):
    def post(self,request):
        serializer = RegistrationsUser(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh_token = RefreshToken.for_user(user)
            access_token = str(refresh_token.access_token)
            return Response({"message":"Register is successfully.","refresh token":str(refresh_token),"access token":access_token},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ListUsers(ListAPIView):
    queryset = User
    serializer_class = ListsUserSerializer
    permission_classes = [IsAdminUser,]