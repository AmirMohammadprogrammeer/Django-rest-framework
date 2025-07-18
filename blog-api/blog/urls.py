from . import views
from django.urls import path

urlpatterns = [
    path("",views.ListBlog.as_view(),name="api"),
    path("blog/<slug:slug>/",views.DetailBlog.as_view(),name="detail"),
    path("create/post/",views.CreatePost.as_view(),name="create"),
]