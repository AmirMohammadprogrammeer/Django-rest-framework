from django.urls import path
from . import views

urlpatterns = [
    path("",views.BookListView.as_view(),name="api"),
    path("<int:pk>/",views.BookDetailView.as_view()),
    path("create",views.BookCreateView.as_view())
]
