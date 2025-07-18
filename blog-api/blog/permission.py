from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsSuperUserAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
       if request.method in SAFE_METHODS :
           return True
       return bool(
           request.user.is_authenticated and request.user.is_staff and (request.user.is_superuser or obj.author==request.user)
       )