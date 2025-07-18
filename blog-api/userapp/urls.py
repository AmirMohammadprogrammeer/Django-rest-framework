from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path("register/",views.RegistrationsUserView.as_view(),name="register"),
    path("list/users",views.ListUsers.as_view(),name="list"),
    path("login/",TokenObtainPairView.as_view(),name="login"),
    path("token/refresh/",TokenRefreshView.as_view(),name="logout"),
]
