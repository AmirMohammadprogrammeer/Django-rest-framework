from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ListBookView,UserListView

router = SimpleRouter()
router.register("",ListBookView,basename="book"),
router.register("user",UserListView,basename="user"),
urlpatterns = router.urls
